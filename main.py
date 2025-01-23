# audio folder from google drive placed at root of project
# didn't include that in the project files for obvious reasons


from os import walk, path
import vlc
import songs
import language_info


INVALID_LANG_STRING = "lang_invalid"

def enumerate_files(audio_path: str):
    for (dirpath, _dirnames, filenames) in walk(audio_path):
        for name in filenames:
            yield path.join(dirpath, name)


def expand_input(input: str) -> tuple[str, bool]:
    only_one = False
    if input[-1] == '-':
        input = input[:-1]
        only_one = True
    if input == "j":
        return ("japanese", only_one)
    if input == "e":
        return ("english", only_one)
    if input in language_info.LANGUAGES.keys():
        return (language_info.LANGUAGES[input], only_one)
    if input in language_info.LANGUAGES.values():
        return (input, only_one)
    
    return (INVALID_LANG_STRING, False)

def main():
    audio_path = path.join(path.abspath(path.curdir), "audio")
    song_data = songs.SongData()
    for name in enumerate_files(audio_path):
        print(name)
        player = vlc.MediaPlayer("file://"+path.join(audio_path, name))
        player.play()
        res = ()
        while True:
            res = expand_input(input("Enter language (j: japanese, e:english, or 2 digit language code)").strip().lower())
            if res[0] != INVALID_LANG_STRING:
                break
            print("Language entered is not supported by whisper")
        player.stop()



if __name__ == "__main__":
    main()
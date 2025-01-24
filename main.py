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

def save_data(song_data: songs.SongData):
    with open(path.join(path.curdir, "data", "languages.json"), 'w') as f:
        song_data.write(f)

def main():
    audio_path = path.join(path.abspath(path.curdir), "audio")

    song_data = None
    try:
        with open(path.join(path.curdir, "data", "languages.json"), 'r') as f:
            song_data = songs.SongData(f)
    except:
        song_data = songs.SongData()        

    
    print("type s to save the data and exit, add - after the language if you know the song contains only that language")
    print("use numbers 0-9 to skip to positions in the song (can skip a long intro if you don't know the song)")
    for name in enumerate_files(audio_path):
        if song_data.contains(name):
            continue
        print(name)
        player = vlc.MediaPlayer("file://"+path.join(audio_path, name))
        player.play()
        res = ()
        while True:
            t_in = input("Enter language (j: japanese, e:english, or 2 digit language code)").strip().lower()
            if t_in == "s":
                save_data(song_data)
                exit()
            if len(t_in) == 1 and t_in.isdigit():
                player.set_position(int(t_in)/10)
                continue
            res = expand_input(t_in)
            if res[0] != INVALID_LANG_STRING:
                break
            print("Language entered is not supported by whisper")
        song_data.set(name, res)
        player.stop()



if __name__ == "__main__":
    main()
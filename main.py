# audio folder from google drive placed at root of project
# didn't include that in the project files for obvious reasons


from os import walk, path
import vlc
import songs

def enumerate_files(audio_path: str):
    for (dirpath, _dirnames, filenames) in walk(audio_path):
        for name in filenames:
            yield path.join(dirpath, name)

def main():
    audio_path = path.join(path.abspath(path.curdir), "audio")
    song_data = songs.SongData()
    for name in enumerate_files(audio_path):
        print(name)
        player = vlc.MediaPlayer("file://"+path.join(audio_path, name))
        player.play()
        input("Press Enter to go next")
        player.stop()


if __name__ == "__main__":
    main()
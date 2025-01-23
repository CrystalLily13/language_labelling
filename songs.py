
class SongData:

    # map of song paths to the language call and a boolean for if the song contains only the one language
    data: dict[str, (str, bool)] = {}

    def get(self, key) -> tuple[str, bool]:
        return self.data.get(key)
    
    def set(self, key, value: tuple[str, bool]):
        self.data[key] = value

    def contains(self, key) -> bool:
        return key in self.data.keys()
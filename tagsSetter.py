import music_tag


class MusicFeet:
    def __init__(self, FILEPATH):
        self.mp3File = music_tag.load_file(FILEPATH)

    def setTitle(self, Title):
        self.mp3File["title"] = Title

    def setAlbum(self, Album):
        self.mp3File["album"] = Album

    def setArtist(self, Artist):
        self.mp3File["artist"] = Artist

    def setGenre(self, Genre):
        self.mp3File["genre"] = Genre

    def setYear(self, Year):
        self.mp3File["year"] = Year

    def setArtwork(self, Artwork):
        with open(Artwork, "rb") as img_in:
            self.mp3File["artwork"] = img_in.read()
        with open(Artwork, "rb") as img_in:
            self.mp3File.append_tag("artwork", img_in.read())

    def mp3Save(self):
        self.mp3File.save()

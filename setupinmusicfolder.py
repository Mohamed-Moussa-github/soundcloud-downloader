from os import mkdir, path, listdir, rename
from shutil import move


class OsMove:
    def __init__(self, FILEPATH, FINALFP):
        self.CurrentFP = FILEPATH
        self.DestinationMain = FINALFP

    def SetNames(self, Song, Artist, Album):
        self.songN = Song
        self.artistN = Artist
        self.albumN = Album

    def MkArtistDir(self):
        try:
            mkdir(path.join(self.DestinationMain, self.artistN))

        except FileExistsError:
            pass

    def MkAlbumDir(self):
        try:
            mkdir(path.join(self.DestinationMain, self.artistN, self.albumN))

        except FileExistsError:
            pass

    def MoveFile(self):
        move(
            self.CurrentFP,
            path.join(self.DestinationMain, self.artistN, self.albumN),
        )
        print(path.join(self.DestinationMain, self.artistN, self.albumN))

    def RenameSong(self):
        self.FP = path.join(self.DestinationMain, self.artistN, self.albumN)
        rename(
            path.join(
                self.FP,
                listdir(self.FP)[0],
            ),
            path.join(self.FP, f"{self.artistN} - {self.songN}.mp3"),
        )


if __name__ == "__main__":
    osmovment = OsMove(
        r"C:\Users\man22\Downloads\Screenshot_20230823_222300_Discord.png",
        r"C:\Downloads",
    )
    osmovment.SetNames("IIBRAHIM", "ETOOOO", "EWUFBWEUFN")
    osmovment.MkArtistDir()

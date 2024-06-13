from metaDataFeet import metaData
import os
from config import Config


class Utilities:
    def fixForbiddenCharInFileName(self, textToCorrect: str):
        forbidden = ["?", ":", ">", "<", "|", "/", "\ "]
        for i in forbidden:
            textToCorrect = [k.replace(i, "_") for k in textToCorrect]

        textToCorrect = "".join(textToCorrect)

        return textToCorrect

    def songNotExists(self, songname, artistname, albumname, *args):
        DestFP = Config().getDestFP()
        FinalFP = os.path.join(
            DestFP,
            self.fixForbiddenCharInFileName(artistname),
            self.fixForbiddenCharInFileName(albumname),
        )
        songnameplus = f"{artistname} - {albumname} - {songname}.mp3"
        if os.path.isfile(os.path.join(FinalFP, songnameplus)):
            return False
        return True

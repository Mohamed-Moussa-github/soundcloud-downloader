from configparser import ConfigParser
from os import path, getcwd, mkdir


class Config:
    def __init__(self):
        self.config = ConfigParser()
        if path.isfile(path.join(getcwd(), r"config.ini")):
            self.config.read("config.ini")
        else:
            default_dest_fp = getcwd().split("\ ".strip())
            splitter = r"\ ".strip()
            default_dest_fp = splitter.join(default_dest_fp[0:3])
            default_dest_fp += "\Downloads\SoundCloudDownloader"

            try:
                mkdir(default_dest_fp)
            except FileExistsError:
                pass

            self.config["SETTINGS"] = {"DestFP": default_dest_fp}
            with open(path.join(getcwd(), r"config.ini"), "w") as f:
                self.config.write(f)

    def getDestFP(self):
        return self.config["SETTINGS"]["DestFP"]

    def setDestFP(self, newDestFP):
        self.config["SETTINGS"]["DestFP"] = newDestFP
        with open("config.ini", "w") as f:
            self.config.write(f)


if __name__ == "__main__":
    Chandler = Config()

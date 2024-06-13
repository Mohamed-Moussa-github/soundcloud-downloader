from requests import get
from html_to_json import convert
from shutil import copyfileobj


class metaData:
    def __init__(self, link):
        self.link = link
        self.shitter()

    def shitter(self):
        request = get(self.link)
        request.encoding = "utf-8"
        requestJson = convert(request.text)

        self.author = requestJson["html"][0]["body"][0]["div"][0]["noscript"][1][
            "article"
        ][0]["header"][0]["h1"][0]["a"][1]["_value"]
        self.genre = requestJson["html"][0]["body"][0]["div"][0]["noscript"][1][
            "article"
        ][0]["header"][0]["meta"][0]["meta"][0]["_attributes"]["content"]
        self.songTitle = requestJson["html"][0]["head"][0]["meta"][39]["_attributes"][
            "content"
        ]
        self.imageURL = requestJson["html"][0]["head"][0]["meta"][40]["_attributes"][
            "content"
        ]
        self.yearCreatedat = requestJson["html"][0]["body"][0]["div"][0]["noscript"][1][
            "article"
        ][0]["header"][0]["time"][0]["_value"][:4]
        del request, requestJson

    def getAuthor(self):
        return self.author

    def getGenre(self):
        if self.genre[0:9] == "UserLikes":
            self.genre = ""
        return self.genre

    def getsongTitle(self):
        return self.songTitle

    def getsongAlbum(self):
        return self.songTitle

    def getimgURL(self):
        return self.imageURL

    def getYear(self):
        return self.yearCreatedat

    def getMusicOBJ(self):
        r = get(self.getimgURL(), stream=True)

        forbidden = ["?", ":", ">", "<", "|", "/", "\ "]
        img_name = f"{self.getAuthor()}-{self.getsongTitle()}"

        for i in forbidden:
            img_name = [k.replace(i, "_") for k in img_name]

        img_name = "".join(img_name)

        with open(rf"C:\Windows\Temp\{img_name}.png", "wb") as f:
            r.raw.decode_content = True
            copyfileobj(r.raw, f)

        return rf"C:\Windows\Temp\{img_name}.png"

    def getMusicLoc(self):
        return rf"C:\Windows\Temp\{self.getAuthor()}-{self.getsongTitle()}.png"


if __name__ == "__main__":
    metadatacclass = metaData(f"https://soundcloud.com/leagueoflegends/kda-the-baddest")
    print(metadatacclass.getAuthor())

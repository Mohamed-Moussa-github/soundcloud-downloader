from requests import post, get


class RequestBetterThanSelenium:
    def __init__(self):
        self.cookies = {
            "PHPSESSID": "7t7p6nohni346hduodp6t42up6",
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-GB,en;q=0.5",
            # 'Accept-Encoding': 'gzip, deflate, br',
            "Referer": "https://www.forhub.io/soundcloud/en/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.forhub.io",
            "DNT": "1",
            "Connection": "keep-alive",
            # 'Cookie': 'PHPSESSID=7t7p6nohni346hduodp6t42up6',
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

    def getSongUrl(self, url):
        self.data = rf"formurl={url}"

        response = post(
            "https://www.forhub.io/download.php",
            cookies=self.cookies,
            headers=self.headers,
            data=self.data,
        )

        hopeium = response.text.split("downloadFile('")[1].split("'")[0]

        # print(hopeium)

        return hopeium

    def downloadSong(self, ActualSongURL):
        r = get(ActualSongURL)
        with open(r"C:\Windows\Temp\yes.mp3", "wb") as mp3file:
            mp3file.write(r.content)


if __name__ == "__main__":
    song = RequestBetterThanSelenium()
    song.getSongUrl(r"https://soundcloud.com/vampriest/bist-ein-blizzard")

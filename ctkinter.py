import customtkinter
from time import sleep
from pygame import mixer
from requestMUSIC import RequestBetterThanSelenium
from metaDataFeet import metaData
from tagsSetter import MusicFeet
from setupinmusicfolder import OsMove
from subprocess import Popen
from config import Config
from PIL import Image
from sys import exit
from utlisfixes import Utilities

global imageToBeUsed
imageToBeUsed = "data\girl_grass_city_213102_1600x900_edging.png"


class App(customtkinter.CTk):
    def __init__(self, title, size):
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")

        # customtkinter.CTkLabel(self, text="", bg_color="black").pack(expand=True, fill="both")

        global my_CTKfont
        my_CTKfont = customtkinter.CTkFont(
            family="Monaco",
            size=28,
            weight="bold",
            slant="roman",
        )
        global my_CTKfontS
        my_CTKfontS = customtkinter.CTkFont(
            family="Monaco",
            size=18,
            weight="bold",
            slant="roman",
        )

        global my_CTKfontVS
        my_CTKfontVS = customtkinter.CTkFont(
            family="Monaco",
            size=12,
            weight="bold",
            slant="roman",
        )

        # widgets
        self.menu = MenuF(self)

        # run app
        self.mainloop()


class MenuF(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        my_image = customtkinter.CTkImage(
            dark_image=Image.open(imageToBeUsed),
            size=(888, 500),
        )
        image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        image_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def command_Exit(self):
        mixer.init()
        mixer.music.load("data/byebye.mp3")
        mixer.music.play(loops=0)
        sleep(2)
        exit()

    def load_EnterF(self):
        EnterF(self)

    def load_OptionsF(self):
        OptionsF(self)

    def create_widgets(self):
        # create widgets
        menu_Enter = customtkinter.CTkButton(
            self,
            text="Enter",
            font=my_CTKfont,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.load_EnterF,
            bg_color="transparent",
            corner_radius=0,
        )
        menu_Option = customtkinter.CTkButton(
            self,
            text="Options",
            font=my_CTKfont,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.load_OptionsF,
            bg_color="transparent",
            corner_radius=0,
        )

        menu_Exit = customtkinter.CTkButton(
            self,
            text="Exit",
            font=my_CTKfont,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.command_Exit,
            bg_color="transparent",
            corner_radius=0,
        )

        # create grid
        self.columnconfigure(
            (0, 1, 2),
            weight=1,
            uniform="a",
        )
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place widgets
        menu_Enter.grid(row=1, column=1, sticky="nswe", pady=36, padx=16)
        menu_Option.grid(row=2, column=1, sticky="nswe", pady=36, padx=16)
        menu_Exit.grid(row=3, column=1, sticky="nswe", pady=36, padx=16)


class EnterF(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        my_image = customtkinter.CTkImage(
            dark_image=Image.open(imageToBeUsed),
            size=(888, 500),
        )
        image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        image_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def load_MenuF(self):
        MenuF(self)

    def on_done_label_entry(self, event):
        self.enterF_btndownload.configure(
            state="normal", text="Next", fg_color="#4D4DFF"
        )
        self.donelabel.grid_remove()
        self.enterF_btndownload.update()

    def downloadMusic(self):
        songlink = self.enterF_entrytext.get("0.0", "end").strip()

        utilieFeet = Utilities()
        configFeet = Config()
        MEEtaData = metaData(songlink)
        SelFeet = RequestBetterThanSelenium()

        if utilieFeet.songNotExists(
            MEEtaData.getsongTitle(), MEEtaData.getAuthor(), MEEtaData.getsongAlbum()
        ):
            SelFeet.downloadSong(SelFeet.getSongUrl(songlink))

            # set tag
            CURRENTLOC = r"C:\Windows\Temp\yes.mp3"
            MMusicFeet = MusicFeet(CURRENTLOC)
            MMusicFeet.setTitle(MEEtaData.getsongTitle())
            MMusicFeet.setAlbum(MEEtaData.getsongAlbum())
            MMusicFeet.setArtist(MEEtaData.getAuthor())
            MMusicFeet.setGenre(MEEtaData.getGenre())
            MMusicFeet.setYear(MEEtaData.getYear())
            MMusicFeet.setArtwork(MEEtaData.getMusicOBJ())
            MMusicFeet.mp3Save()

            # move

            MOVEMENT = OsMove(CURRENTLOC, configFeet.getDestFP())

            MOVEMENT.SetNames(
                utilieFeet.fixForbiddenCharInFileName(MEEtaData.getsongTitle()),
                utilieFeet.fixForbiddenCharInFileName(MEEtaData.getAuthor()),
                utilieFeet.fixForbiddenCharInFileName(MEEtaData.getsongTitle()),
            )
            MOVEMENT.MkArtistDir()
            MOVEMENT.MkAlbumDir()
            MOVEMENT.MoveFile()
            MOVEMENT.RenameSong()

        else:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(
                    self, "Song already exists"
                )  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

    def downloadMusicAesthics(self):
        if self.enterF_entrytext.get("0.0", "end").strip() != "":
            if self.enterF_btndownload.cget("text") == "Download":
                self.enterF_btndownload.configure(state="disabled")
                self.enterF_entrytext.configure(state="disabled")

                try:
                    self.downloadMusic()
                except Exception as e:
                    with open("e.txt", "w") as f:
                        f.write(str(e))

                    print(e)
                    if str(e).strip() == "list index out of range":
                        e = "Enter proper URL"
                    elif str(e).strip()[0:19] == "HTTPSConnectionPool":
                        e = "No internet connection"

                    if (
                        self.toplevel_window is None
                        or not self.toplevel_window.winfo_exists()
                    ):
                        self.toplevel_window = ToplevelWindow(
                            self, e
                        )  # create window if its None or destroyed
                    else:
                        self.toplevel_window.focus()  # if window exists focus it

                self.enterF_btndownload.configure(text="Done", width=140)
                self.donelabel = customtkinter.CTkLabel(
                    self,
                    text="Done",
                    font=my_CTKfontS,
                    width=140,
                    fg_color="#4D4DFF",
                )
                self.donelabel.grid(
                    column=1, columnspan=1, rowspan=1, row=3, padx=16, pady=16
                )
                self.donelabel.bind("<Enter>", self.on_done_label_entry)
                self.update()

            elif self.enterF_btndownload.cget("text") == "Next":
                self.enterF_btndownload.configure(text="Download")
                self.enterF_entrytext.configure(state="normal")

    def open_Folder(self):
        configFeet = Config()
        Popen(rf"explorer {configFeet.getDestFP()}")

    def create_widgets(self):
        # create widgets
        self.toplevel_window = None
        enterF_btnback = customtkinter.CTkButton(
            self,
            text="Back",
            font=my_CTKfontS,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.load_MenuF,
            corner_radius=0,
        )
        enterF_labelLink = customtkinter.CTkLabel(
            self,
            text="Link",
            font=my_CTKfont,
            fg_color="transparent",
            bg_color="transparent",
            corner_radius=0,
        )
        self.enterF_entrytext = customtkinter.CTkTextbox(
            self, font=("Monaco", 12), width=550, corner_radius=0, height=400
        )
        self.enterF_btndownload = customtkinter.CTkButton(
            self,
            text="Download",
            font=my_CTKfontS,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.downloadMusicAesthics,
            width=140,
            corner_radius=0,
        )
        enterF_btnopenfolder = customtkinter.CTkButton(
            self,
            text="Open Folder",
            font=my_CTKfontS,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.open_Folder,
        )

        # set up grid
        self.columnconfigure(
            (0, 1, 2, 3),
            weight=1,
            uniform="a",
        )
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place widgets
        enterF_btnback.grid(column=0, columnspan=1, rowspan=1, row=0, padx=8)
        enterF_labelLink.grid(
            column=1, columnspan=2, rowspan=1, row=1, padx=16, pady=16
        )
        self.enterF_entrytext.grid(column=1, columnspan=2, rowspan=1, row=2, pady=16)
        self.enterF_btndownload.grid(
            column=1, columnspan=1, rowspan=1, row=3, padx=16, pady=16
        )
        enterF_btnopenfolder.grid(
            column=2, columnspan=1, rowspan=1, row=3, padx=16, pady=16
        )


class OptionsF(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configfeet = Config()

        my_image = customtkinter.CTkImage(
            dark_image=Image.open(imageToBeUsed),
            size=(888, 500),
        )
        image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        image_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def load_MenuF(self):
        MenuF(self)

    def options_Save(self):
        self.configfeet.setDestFP(self.optionsF_entryDestFP.get())

    def create_widgets(self):
        # create widgets
        optionsF_btnBack = customtkinter.CTkButton(
            self,
            text="Back",
            font=my_CTKfontS,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.load_MenuF,
            corner_radius=0,
            width=100,
        )
        optionsF_labelDestFP = customtkinter.CTkLabel(
            self,
            text="Output Folder",
            font=my_CTKfontS,
            corner_radius=0,
            bg_color="transparent",
            fg_color="transparent",
            width=150,
        )
        self.optionsF_entryDestFP = customtkinter.CTkEntry(
            self,
            font=my_CTKfontVS,
            justify="center",
            corner_radius=0,
            bg_color="transparent",
            width=400,
        )

        self.optionsF_entryDestFP.insert(0, self.configfeet.getDestFP())

        optionsF_btnSave = customtkinter.CTkButton(
            self,
            text="Save",
            font=my_CTKfontS,
            fg_color="#4D4DFF",
            hover_color="#000099",
            command=self.options_Save,
            corner_radius=0,
        )

        # set up grid
        self.columnconfigure(
            (0, 1, 2, 3),
            weight=1,
        )
        self.rowconfigure((0, 1, 2, 3), weight=1)

        # layout
        optionsF_btnBack.grid(column=0, row=0, pady=16)
        optionsF_labelDestFP.grid(column=1, columnspan=1, row=1, padx=16, pady=16)
        self.optionsF_entryDestFP.grid(column=2, columnspan=2, row=1, padx=16, pady=16)
        optionsF_btnSave.grid(column=0, columnspan=4, row=3, pady=16)


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, ErrorMessageStr: str):
        super().__init__(parent)
        self.geometry("300x200")
        self.title("Error Message")
        self.resizable(False, False)

        self.label = customtkinter.CTkLabel(
            self, text=ErrorMessageStr, font=my_CTKfontS, width=300, wraplength=300
        )

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.label.grid(row=1, column=1, columnspan=3)


if __name__ == "__main__":
    App("Soundcloud downloader", (888, 500))

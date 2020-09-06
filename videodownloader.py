import tkinter as tk
from tkinter.ttk import Combobox 
import pytube
import time
import os
class wind():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Video Downloader")
        self.root.geometry("800x500")
        self.root.resizable(False,False)
        self.inp = tk.Text(height=2,width=30)
        self.inp.place(x=290,y=50)
        self.btn = tk.Button(text="Download",height=2,width=30,command=self.download)
        self.btn.place(x=285,y=245)
        self.dizin = tk.Entry()
        self.dizin.place(x=330,y=195)
        # self.chckbox = tk.Checkbutton(text="Bulundugum Dizine Indir")
        # self.chckbox.place(x=560,y=58)
        self.combo = Combobox(value=("mp3","mp4"))
        self.combo.place(x=330,y=126)
        self.lbl = tk.Label(text="")
        self.lbl.place(x=249,y=310)
        self.urllbl = tk.Label(text="Video urli:")
        self.urllbl.place(x=289,y=27)  
        self.formatlbl = tk.Label(text="Format:")
        self.formatlbl.place(x=289,y=104)
        self.dizinlbl = tk.Label(text="Indirilecek Dizin(eger dizin yoksa otomatik olusturulacak!):")
        self.dizinlbl.place(x=289,y=168)
        self.dizin.delete(0, "end")
        self.dizin.insert(0, os.getcwd())
        self.root.mainloop()

    def download(self):
        self.format = self.combo.get()
        self.url = self.inp.get("1.0","end")
        if self.format == "mp4":
            self.lbl["text"] = pytube.YouTube(self.url).title + " - Video Indiriliyor!"
            self.youtube = pytube.YouTube(self.url)
            self.video = self.youtube.streams.get_highest_resolution()
            self.video.download(self.dizin.get())
            # print(self.dizin.get())
            self.lbl["text"] = self.youtube.title + " - Video Indirildi!"
        elif self.format == "mp3":
            self.lbl["text"] = "Videonun ses fayli endirilir"
            os.system("youtube-dl -x --audio-format mp3 "+self.inp.get("1.0","end"))
            self.lbl["text"] = "Videonun ses fayli endirildi!"
        else:
            self.lbl["text"] = "Xahis olunur bosluqlari tamamlayin!"




wind1 = wind()




# dont forget:
# install atom
# add github this file
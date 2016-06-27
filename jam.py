# file: digital.py
# versi: python 2.7
# Program Jam Digital dengan Tkinter
# created by Exhacking.net
# update: 02/08/2012 12.13 AM
 
# memanggil modul Tkinter
from Tkinter import *
# memanggil modul time (untuk mengakses waktu saat ini)
import time
 
class JamDigital:
    """ Kelas Jam Digital"""
     
    def __init__(self, parent, title):
        self.parent = parent
         
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onTutup)
        self.parent.resizable(False, False)
         
        # buat variabel String untuk teks jam
        self.teksJam = StringVar()
         
        self.aturKomponen()
        # melalukan looping untuk tampilan jam
        self.update()
         
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        # teks jam dibuat dengan komponen Label, yang bisa berubah 
        # setiap waktu.
        self.lblJam = Label(mainFrame, textvariable=self.teksJam,
            font=('Helvetica', 40))
        self.lblJam.pack(expand=YES)
         
        self.lblInfo = Label(mainFrame, text="http://www.exhacking.net",
            fg='red')
        self.lblInfo.pack(side=TOP, pady=5)
         
    def update(self):
        # strftime() berfungsi untuk merubah data waktu secara lokal
        # menjadi bentuk string yang kita inginkan.
        datJam = time.strftime("%H:%M:%S", time.localtime())
         
        # mengubah teks jam sesuai dengan waktu saat ini
        self.teksJam.set(datJam)
         
        # perubahan teks jam dalam selang waktu 1 detik (1000 ms)
        self.timer = self.parent.after(1000, self.update)
         
    def onTutup(self, event=None):
        self.parent.destroy()
         
if __name__ == '__main__':
    root = Tk()
     
    app = JamDigital(root, "Jam Digital")
     
    root.mainloop()
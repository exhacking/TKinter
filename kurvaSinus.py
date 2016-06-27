# file: kurvaSinus.py
# program menggambar kurva sinus
# versi: Python 3.2
# sumber inspirasi: Delphi 5.0 - Inge Martina
 
from tkinter import *
import math
 
class DemoSinus:
    def __init__(self, parent, title):
        self.parent = parent
 
        self.parent.title(title)
        self.parent.geometry("640x200")
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
 
        self.aturKomponen()
 
    def aturKomponen(self):
        mainCanvas = Canvas(self.parent, bg="white")
        mainCanvas.pack(fill=BOTH, expand=YES)
 
        self.kanvas = mainCanvas
 
        self.btnProses = Button(mainCanvas, text="Proses", command=self.gambarSinus)
        self.btnProses.pack(expand=YES)
 
    def gambarSinus(self, event=None):
        setengahTinggi = int(self.parent.winfo_height() / 2)
        lebar = self.parent.winfo_width()
 
        x_awal = 0
        y_awal = setengahTinggi
 
        for px in range(lebar):
            x = px * (2 * math.pi / lebar)
            y = math.sin(x)
 
            py = math.trunc(0.7 * y * setengahTinggi) + setengahTinggi
 
            self.kanvas.create_line(x_awal, y_awal, px, py)
 
            x_awal = px
            y_awal = py
             
    def onKeluar(self, event=None):
        self.parent.destroy()
 
if __name__ == '__main__':
    root = Tk()
 
    aplikasi = DemoSinus(root, "Demo Grafik Sinus")
 
    root.mainloop()
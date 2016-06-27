# Nama File: bitview27.py
# Versi Python: 2.7
# Dibuat Tgl: 10 Juni 2012 01.15 AM
# Sumber Inspirasi: Tom Swan, Delphi 4 Bible, 1998 
 
 
from Tkinter import *
from tkFileDialog import *
from PIL import Image, ImageTk
 
class BitView27:
    def __init__(self, parent, title):
        self.parent = parent
         
        self.parent.geometry("600x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onTutup)
        self.parent.resizable(False, False)
         
        self.aturKomponen()
         
    def aturKomponen(self):
        # buat main frame
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        # buat label penampil image
        self.lblImage = Label(mainFrame, text='Image Preview')
        self.lblImage.pack(side=TOP, fill=BOTH, expand=YES)
         
        # buat menu
        menuBar = Menu(self.parent)
         
        fileMenu = Menu(menuBar, tearoff=1)
        fileMenu.add_command(label='Buka', underline=0, 
            command=self.onBuka)
        fileMenu.add_command(label='Keluar', underline=0, 
            command=self.onTutup)
        menuBar.add_cascade(label='File', underline=0, menu=fileMenu)
         
        self.parent.config(menu=menuBar)
         
    def onBuka(self, event=None):
        filename = askopenfilename(filetypes=[('File Gambar', 
            ('*.jpg', '*.bmp', '*.gif', '*.png'))])
             
        panjang = 600
        lebar = 450
         
        if filename:
            pict = Image.open(filename)
            gambar = ImageTk.PhotoImage(pict)
             
            self.lblImage.config(image=gambar)
            self.lblImage.image = gambar
             
            self.parent.title("Image Viewer :: " + filename)
          
    def onTutup(self, event=None):
        self.parent.destroy()
         
if __name__ == '__main__':
    root = Tk()
     
    app = BitView27(root, "Image Viewer")
     
    root.mainloop()
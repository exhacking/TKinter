# file: selamat_datang.py

from Tkinter import *

class DemoSelamatDatang:
	def __init__(self, parent, title):
		self.parent = parent

		self.parent.title(title)
		self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)

		self.aturKomponen()

	def aturKomponen(self):
		mainFrame = Frame(self.parent, bd=10)
		mainFrame.pack(fill=BOTH, expand=YES)

		# pasang kotak edit
		self.entPesan = Entry(mainFrame, width=25)
		self.entPesan.insert(0, "Selamat Datang di Exhacking.Net")
		self.entPesan.pack(side=TOP, pady=5)

		# pasang tombol keluar
		self.btnKeluar = Button(mainFrame, text="Keluar",
			command=self.onKeluar)
		self.btnKeluar.pack(side=TOP, pady=5)

	def onKeluar(self, event=None):
		self.parent.destroy()

if __name__ == '__main__':
	root = Tk()

	aplikasi = DemoSelamatDatang(root, "Exhacking.net Demo Tkinter")

	root.mainloop()
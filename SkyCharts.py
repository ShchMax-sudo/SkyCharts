from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd

typ = "png"
w = 800
h = 600
ew = 25
files = None
pref = "stellarium-"
DirError = False

def invert(im):
	pixels = im.load()
	x, y = im.size
	for i in range(x):
		for j in range(y):
			a = pixels[i, j]
			pixels[i, j] = (tuple([255 - sum(a) // 3] * 3))
	return im

def save(im, indeks):
	global typ, DirError
	try:
		im.save('./SkyCharts/skychart-{}'.format(str(indeks)) + '.' + typ)
	except:
		DirError = True
		raise IndexError()

def choose():
	global files
	files = fd.askopenfilename()
	files = files[:files.rfind("/") + 1]

def exir(e):
	raise SystemExit()

def obr():
	global begin, end, files, typ, pref, DirError
	b = int(begin.get())
	e = int(end.get())
	for i in range(b, e + 1):
		try:
			save(invert(Image.open(files + pref + ("000" + str(i))[-3:] + '.' + typ)), i)
			print("Обработана {} картинка.".format(i))
		except:
			print("Ошибка обработки {} картинки.".format(i))
		if (DirError):
			print("Не обнаружена папка SkyCharts в папке с программой.")
			raise SystemExit()
	print("Обработка окончена.")

root = tk.Tk()
root.geometry(str(w) + "x" + str(h))
root.title("Генератор скайчартов")
root.bind("<Escape>", exir)
but = tk.Button(root, text="Выберите скрин(любой из папки)", command=choose)
but.pack()
begin = tk.StringVar(root)
eb = tk.Entry(root, w=ew, justify=tk.CENTER, textvariable=begin)
eb.delete(0, tk.END)
eb.insert(0, "Введите начальный индекс")
eb.pack()
end = tk.StringVar(root)
ee = tk.Entry(root, w=ew, justify=tk.CENTER, textvariable=end)
ee.delete(0, tk.END)
ee.insert(0, "Введите конечный индекс")
ee.pack()
bi = tk.Button(root, text="Обработать", command=obr)
bi.pack()
root.mainloop()
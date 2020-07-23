from PIL import Image
from PIL import ImageOps
import os


def instaResize():
	maxsize = (1060, 1330)

	for f in os.listdir("images/"):
		if f.endswith(".jpg"):
			i = Image.open("images/"+f)
			fn, fext = os.path.splitext(f)
			i.thumbnail(maxsize, Image.ANTIALIAS)
			bordered = ImageOps.expand(i, border=20, fill="white")
			bordered.save("resized/{}_insta{}".format(fn, fext), quality=100)

instaResize()




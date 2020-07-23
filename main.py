from PIL import Image
from PIL import ImageOps
import os
import time
import sys

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Taken from StackOverflow user Greenstick.

    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write("\r{} |{}| {}% {}".format(prefix, bar, percent, suffix))
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total: 
        print("\n")

def instaResize():
	maxsize = (1060, 1330)
	l = len(os.listdir("images/"))
	printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
	i = 1
	for f in os.listdir("images/"):
		if f.endswith(".jpg"):
			#print(f"Resizing {f}.")
			img = Image.open("images/"+f)
			fn, fext = os.path.splitext(f)
			img.thumbnail(maxsize, Image.ANTIALIAS, Image.LANCZOS)
			#print(f"{f} resized.")
			#print(f"Adding border to {f}.")
			bordered = ImageOps.expand(img, border=20, fill="white")
			bordered.save("resized/{}_insta{}".format(fn, fext), quality=100)
			#print(f"{f} has been saved.")

			time.sleep(0.1)
			printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
			i += 1
			sys.stdout.flush()
			time.sleep(0.1)
	print(f"{i-1} photos resized for Instagram.")
instaResize()




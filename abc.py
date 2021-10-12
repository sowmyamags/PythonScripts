#!/usr/bin/env python3

import PIL
from PIL import Image
import os

path = "/mnt/c/users/sowmya/pythonscripts/images/"
print(path)
l = os.listdir(path)

for im in l:
  savefile = path + im + ".jpg"

  if 'jpg' in im:
    i = Image.open(path+im)
    print(i.format, i.size, i.mode)
  else:
    try:
      Image.open(path+im).convert("RGB").resize((600,400)).save(savefile, "JPEG")
    except OSError:
      print("Cannot conver")


"""file /mnt/c/users/sowmya/pythonscripts/images/Scan_1.jpg  by entering this command 
    we can retruve th eimage details"""


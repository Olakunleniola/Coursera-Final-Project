#! /usr/bin/env python3
from PIL import Image
import os
import send2trash
pwwd = '/mnt/c/Users/OLAKUNLE AKANDE/Downloads/COURSERA FILES/Coursera part 6 (Automating Real-World Tasks with Python)/Final_Project_Folder'
for img  in os.listdir(pwwd + '/supplier-data/images/'):
    try:
        im = Image.open(pwwd +'/supplier-data/images/' + img).convert("RGB")
        im.resize((600,400)).save(f"{pwwd}/supplier-data/images/{img.strip('.tiff')}.jpeg")
        send2trash.send2trash(pwwd + '/supplier-data/images/' + img)
    except:
        pass

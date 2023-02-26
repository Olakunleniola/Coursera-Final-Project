#! /usr/bin/env python3
from PIL import Image
import os
import send2trash
 
for img  in os.listdir('Final_Project_Folder/supplier-data/images/'):
    try:
        im = Image.open('Final_Project_Folder/supplier-data/images/' + img).convert("RGB")
        im.resize((600,400)).save(f"Final_Project_Folder/supplier-data/images/{img.strip('.tiff')}.jpeg")
        send2trash.send2trash('Final_Project_Folder/supplier-data/images/' + img)
    except:
        pass

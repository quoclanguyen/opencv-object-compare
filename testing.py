import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load an color image
root = tk.Tk()  
vid = cv2.VideoCapture(0) 
while True:
    
    _, img = vid.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(master = root, image=im) 
    tk.Label(root, image=imgtk).pack()
    root.update()

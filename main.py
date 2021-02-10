from tkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageFont, ImageDraw
from tkinter import filedialog, simpledialog
import os, sys

THUMB_SIZE = (128,128)

#Tk Window
window = Tk()
window.geometry('500x500')
window.resizable(width=True,height=True)
window.title('Watermark Add')

def openfn():
    filename = filedialog.askopenfilename(title='Open')
    return filename

def get_text():
    text = simpledialog.askstring("Input",'What to write?')
    return text

def open_img():
    x = openfn()
    text = get_text()
    img = Image.open(x)
    width, height = img.size
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = d1.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    d1.text((x,y), text, font=font)
    img = img.resize((500,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.pack()

btn = Button(window, text='open image', command=open_img)
btn.pack()

window.mainloop()

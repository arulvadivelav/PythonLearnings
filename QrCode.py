from tkinter import *
import pyqrcode
from PIL import Image, ImageTk
import easygui

root = Tk()

def generate_qr():
    link_name = input_link_name.get()
    link = input_link.get()
    qr_file_name = link_name+".png"
    file_path_to_save = easygui.filesavebox(default=qr_file_name)
    
    url = pyqrcode.create(link)
    url.png(file_path_to_save, scale=8)
    qr = ImageTk.PhotoImage(Image.open(file_path_to_save))
    image_label = Label(image=qr)
    image_label.image = qr
    canvas.create_window(200, 450, window=image_label)

canvas = Canvas(root, width=400, height=650)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(200,50, window = app_label)

link_name_label = Label(root, text="Link Name")
canvas.create_window(200, 100, window=link_name_label)

input_link_name = Entry(root)
canvas.create_window(200, 130, window=input_link_name)

link_label = Label(text="Link")
canvas.create_window(200, 170, window=link_label)

input_link = Entry(root)
canvas.create_window(200, 200, window=input_link)

button = Button(text = "Generate QR Code", command=generate_qr)
canvas.create_window(200, 250, window=button)

root.mainloop()

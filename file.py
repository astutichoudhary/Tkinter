from tkinter import *
from PIL import Image,ImageTk
window = Tk()

window.geometry("720x480")
window.title("Astuti's window")

# icon = PhotoImage(file ='meriphoto.jpg')
# window.iconphoto(True,icon)

opened_img = Image.open("meriphoto.jpg")
img = ImageTk.PhotoImage(opened_img)
window.iconphoto(True,img)

window.config(background='Sky Blue')
window.mainloop()

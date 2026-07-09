from tkinter import *

from PIL import Image,ImageTk # to avoid the error coming in accessing jpg file

window = Tk()

window.geometry("720x480")
window.title("Astuti's window")

# CANNOT FIGURE OUT HOW TO ADD PHOTO IMAGE AND ICON. WILL COME BACK LATER.

# icon = PhotoImage(file ='photo.png')
# window.iconphoto(True,icon)

# opened_img = Image.open("meriphoto.jpg")
# img = ImageTk.PhotoImage(opened_img)
# window.iconphoto(True,img)

window.config(background='Sky Blue')
window.mainloop()
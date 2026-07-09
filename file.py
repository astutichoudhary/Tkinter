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

# label and functions.
label = Label(window, text = "Astuti Choudhary learns Tkinter module.", font = ("Comic Sans",30,"italic"),
            fg = "#013D68",
            bg = "#8BB8F7",
            relief = RAISED,
            bd = 10 , padx=5, pady=15,
            )
label.pack()

#button and functions.
count = 0

def click():
    global count
    if count == 5:
        button.config(state = DISABLED)
    print("You clicked the button.")
    count += 1

button = Button(window, text = "Click Me.", command=click ,font = ("Comic Sans", 10, 'bold'),
                fg = "#8E0000", bg = "#330404",
                activebackground="#140043",
                activeforeground="#7F9FFF",
                )
button.pack()

# Entry widget(to input single line data from user.)
entername = Label(window, text = "Enter your name.", font=('Arial',20))
entername.pack(side = TOP)

entry = Entry(window,font=('Calibri',20,'underline'),
              fg = "#003C00", bg = "#B9C000",
              )
entry.insert(0,"Spongebob")
entry.pack(side = TOP)

def submit():
    name = entry.get()
    print("Hello",name)
    entry.config(state = DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    name = entry.get()
    length = len(name)
    entry.delete(length - 1,END)

def submitpass():
    password = passwordentry.get()

submit_button = Button(window, text= "Submit.", font=('Arial',10),
                       command= submit,)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text="Clear.",command=delete,
                        font=('Arial',10))
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text="Backspace.",command=backspace,
                        font=('Arial',10))
backspace_button.pack(side = RIGHT)



passwordentry = Entry(window, font=('Segoe Print',15),show = "*")
passwordentry.pack()

submit_pass = Button(window, text= "Submit password.",command = submitpass)
submit_pass.pack(side = "right")






window.mainloop()
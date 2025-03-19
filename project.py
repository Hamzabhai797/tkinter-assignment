from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("PIA managment system")
root.geometry("1200x700")
root.config(bg="light gray")
root.resizable(False,False)

root.iconphoto(False, PhotoImage(file='pia.logo.png'))

try:
  bg_img = Image.open('bga.png')
  bg_img = bg_img.resize((1200, 700), Image.LANCZOS)
  bg_photo = ImageTk.PhotoImage(bg_img)

  bg_lab = Label(root, image=bg_photo)
  bg_lab.place(relwidth=1, relheight=1)
except:
  print("errer loading image:", E)

img = PhotoImage(file='pia.logo.png')
img = img.subsample(3,7)
lab = Label(image=img)
lab.pack(side='left', anchor='n', padx=10, pady=10)

frame = Frame(root, width=300, height=380, bg="white")
frame.place(x=10, y=200)

try:
    frame_img = Image.open("airport.png")
    frame_img = frame_img.resize((300, 380), Image.LANCZOS)
    frame_photo = ImageTk.PhotoImage(frame_img)

    frame_label = Label(frame, image=frame_photo)
    frame_label.image = frame_photo  
    frame_label.place(x=0, y=0, relwidth=1, relheight=1) 

except Exception as e:
    print("Error loading frame image:", e)

frame1 = Frame(root, width=300, height=380, bg="white")
frame1.place(x=310, y=200)

user = Entry(root, width=17, fg='black', border=0, font=('Microsoft yahai ul light', 13))
user.insert(0, 'Create New Account')
user.place(x=380, y=210,)

user = Entry(root, width=23, fg='gray', border=2, bg='white', font=('Microsoft yahai ul light', 12))
user.insert(0, 'First Name')
user.place(x=345, y=270,)

def on_focus_in(event):
    if user.get() == "First Name":
        user.delete(0, END)
        user.config(fg="black")

def on_focus_out(event):
    if user.get() == "": 
        user.insert(0, "sign")
        user.config(fg="gray")

user.bind("<FocusIn>", on_focus_in)
user.bind("<FocusOut>", on_focus_out)

user = Entry(root, width=23, fg='gray', border=2, bg='white', font=('Microsoft yahai ul light', 12))
user.insert(0, 'Last Name')
user.place(x=345, y=320,)

def on_focus_in(event):
    if user.get() == "Last Name":
        user.delete(0, END)
        user.config(fg="black")

def on_focus_out(event):
    if user.get() == "": 
        user.insert(0, "sign")
        user.config(fg="gray")

user.bind("<FocusIn>", on_focus_in)
user.bind("<FocusOut>", on_focus_out)

user = Entry(root, width=23, fg='gray', border=2, bg='white', font=('Microsoft yahai ul light', 12))
user.insert(0, 'Email')
user.place(x=345, y=370,)

def on_focus_in(event):
    if user.get() == "Email":
        user.delete(0, END)
        user.config(fg="black")

def on_focus_out(event):
    if user.get() == "": 
        user.insert(0, "sign")
        user.config(fg="gray")

user.bind("<FocusIn>", on_focus_in)
user.bind("<FocusOut>", on_focus_out)

user = Entry(root, width=23, fg='gray', border=2, bg='white', font=('Microsoft yahai ul light', 12))
user.insert(0, 'Password')
user.place(x=345, y=420,)

def on_focus_in(event):
    if user.get() == "Password":
        user.delete(0, END)
        user.config(fg="black")

def on_focus_out(event):
    if user.get() == "": 
        user.insert(0, "sign")
        user.config(fg="gray")

user.bind("<FocusIn>", on_focus_in)
user.bind("<FocusOut>", on_focus_out)

butt = Button(root, text='Sign Up', width=13, background='lightblue', border=2)
butt.place(x=400, y=460)

root.mainloop()
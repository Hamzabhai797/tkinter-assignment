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

frame = Frame(root, width=270, height=350, bg="white")
frame.place(x=10, y=200)

try:
    frame_img = Image.open("images1.png")
    frame_img = frame_img.resize((270, 350), Image.LANCZOS)
    frame_photo = ImageTk.PhotoImage(frame_img)

    frame_label = Label(frame, image=frame_photo)
    frame_label.image = frame_photo  
    frame_label.place(x=0, y=0, relwidth=1, relheight=1) 

except Exception as e:
    print("Error loading frame image:", e)

frame1 = Frame(root, width=270, height=350, bg="white")
frame1.place(x=280, y=200)

root.mainloop()
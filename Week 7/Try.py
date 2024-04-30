from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

menu = Tk()
menu.title("menu")
menu.geometry("1000x1000")
#menu.resizeable(False,False)

img = ImageTk.PhotoImage(file="C:/Users/jhae4/Documents/jemmanuelCos102/Week 7/project_pic_3.png")

food = Canvas(menu,width=1000,height=1000)
food.pack(fill="both",expand=True)

food.create_image(0,0, image=img, anchor="nw")

menu.mainloop()
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Menu")
root.geometry("800x450")

#save file path to variable
pic = ImageTk.PhotoImage(file="C:/Users/jhae4/Documents/jemmanuelCos102/Week 7/project_pic_2.png")

#create canvas
background = Canvas(root, width=800, height=450)
background.pack(fill="both", expand=True)

# render image to canvas/Define image
background.create_image(0,0, image=pic , anchor="nw")

#write text
a = 400
background.create_text(a,50, text='Menu', font=("Ink free",50), fill="red")

def resizer(e):
    global pic_1,resized_pic,new_pic
    #open image
    pic_1 = Image.open("C:/Users/jhae4/Documents/jemmanuelCos102/Week 7/project_pic_2.png")
    #resize image
    resized_pic = pic_1.resize((e.width, e.height))
    #DEFINE YOUR NEW_IMAGE
    new_pic = ImageTk.PhotoImage(resized_pic)
    #return resized image to canvas
    background.create_image(0,0, image=new_pic, anchor="nw")
    #re-add text again
    c = (e.width/2)
    background.create_text(c,50, text='Menu', font=("Ink free",50), fill="red")

root.bind('<Configure>', resizer)
root.mainloop()
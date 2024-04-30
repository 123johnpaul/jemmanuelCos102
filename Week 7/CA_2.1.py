from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("Menu")
root.geometry("1200x650")
root.resizable(False,False)

#save file path to variable
pic = ImageTk.PhotoImage(file="C:/Users/jhae4/Documents/jemmanuelCos102/Week 7/project_pic_3.png")

#create canvas
background = Canvas(root, width=1000, height=750)
background.pack(fill="both", expand=True)

# render image to canvas/Define image
background.create_image(0,0, image=pic , anchor="nw")

#Creat text
background.create_text(850,50, text='Menu', font=("Ink free",50), fill="red")

#rice pasta part
background.create_text(500,100, text='Rice/Pasta', font=("Ink free",20), fill="red")
background.create_text(465,125, text='>jellof rice', font=("Ink free",15), fill="white")
background.create_text(490,148, text='>jellof spaghetti', font=("Ink free",15), fill="white")
background.create_text(499,170, text='>Coconut fried rice', font=("Ink free",15), fill="white")
#price of rice or pasta
background.create_text(680,125, text='@ #350', font=("Ink free",15), fill="white")
background.create_text(680,148, text='@ #350', font=("Ink free",15), fill="white")
background.create_text(680,170, text='@ #350', font=("Ink free",15), fill="white")

#Side dish part
background.create_text(500,220, text='Side dishes', font=("Ink free",20), fill="red")
background.create_text(485,245, text='>Savoury beans', font=("Ink free",15), fill="white")
background.create_text(525,270, text='>Roasted sweet potatoe', font=("Ink free",15), fill="white")
background.create_text(481,295, text='>Fried plantain', font=("Ink free",15), fill="white")
background.create_text(519,320, text='>Mixed vegetable salad', font=("Ink free",15), fill="white")
background.create_text(471,345, text='>Boiled yam', font=("Ink free",15), fill="white")
#prices for side dish
background.create_text(680,245, text='@ #350', font=("Ink free",15), fill="white")
background.create_text(680,270, text='@ #300', font=("Ink free",15), fill="white")
background.create_text(680,295, text='@ #150', font=("Ink free",15), fill="white")
background.create_text(680,320, text='@ #150', font=("Ink free",15), fill="white")
background.create_text(680,345, text='@ #150', font=("Ink free",15), fill="white")

#Beverages side
background.create_text(500,395, text='Beverages', font=("Ink free",20), fill="red")
background.create_text(455,420, text='>Water', font=("Ink free",15), fill="white")
background.create_text(495,445, text='>Glass drink 35cl', font=("Ink free",15), fill="white")
background.create_text(490,470, text='>PET drink 35cl', font=("Ink free",15), fill="white")
background.create_text(488,495, text='>PET drink 50cl', font=("Ink free",15), fill="white")
background.create_text(507,520, text='>Glass/Canned malt', font=("Ink free",15), fill="white")
background.create_text(485,545, text='>Pineapple juice', font=("Ink free",15), fill="white")
background.create_text(475,570, text='>Mango juice', font=("Ink free",15), fill="white")
background.create_text(468,595, text='>Zobo drink', font=("Ink free",15), fill="white")
#Prices of beverages
background.create_text(680,420, text='@ #200', font=("Ink free",15), fill="white")
background.create_text(680,445, text='@ #150', font=("Ink free",15), fill="white")
background.create_text(680,470, text='@ #300', font=("Ink free",15), fill="white")
background.create_text(680,495, text='@ #350', font=("Ink free",15), fill="white")
background.create_text(680,520, text='@ #500', font=("Ink free",15), fill="white")
background.create_text(680,545, text='@ #350', font=("Ink free",15), fill="white")
background.create_text(680,570, text='@ #350', font=("Ink free",15), fill="white")
background.create_text(680,595, text='@ #350', font=("Ink free",15), fill="white")

#Proteins part
background.create_text(950,100, text='Proteins', font=("Ink free",20), fill="red")
background.create_text(960,125, text='>Sweet grilled chicken', font=("Ink free",15), fill="white")
background.create_text(960,150, text='>Grilled chicken wings', font=("Ink free",15), fill="white")
background.create_text(918,175, text='>Fried beef', font=("Ink free",15), fill="white")
background.create_text(918,200, text='>Fried fish', font=("Ink free",15), fill="white")
background.create_text(922,225, text='>Boiled egg', font=("Ink free",15), fill="white")
background.create_text(949,250, text='>Salted sausages', font=("Ink free",15), fill="white")
#prices of protein
background.create_text(1103,125, text='@ #1,100', font=("Ink free",15), fill="white")
background.create_text(1100,150, text='@ #400', font=("Ink free",15), fill="white")
background.create_text(1100,175, text='@ #400', font=("Ink free",15), fill="white")
background.create_text(1100,200, text='@ #500', font=("Ink free",15), fill="white")
background.create_text(1100,225, text='@ #200', font=("Ink free",15), fill="white")
background.create_text(1100,250, text='@ #200', font=("Ink free",15), fill="white")


#Soup and swallow part
background.create_text(960,300, text='Soup & Swallow', font=("Ink free",20), fill="red")
background.create_text(900,325, text='>Eba', font=("Ink free",15), fill="white")
background.create_text(906,350, text='>Semo', font=("Ink free",15), fill="white")
background.create_text(940,375, text='>Pounded yam', font=("Ink free",15), fill="white")
background.create_text(912,400, text='>Egusi', font=("Ink free",15), fill="white")
background.create_text(930,425, text='>Ofe nsala', font=("Ink free",15), fill="white")
#prices for soup and swallow
background.create_text(1100,325, text='@ #100', font=("Ink free",15), fill="white")
background.create_text(1100,350, text='@ #100', font=("Ink free",15), fill="white")
background.create_text(1100,375, text='@ #100', font=("Ink free",15), fill="white")
background.create_text(1100,400, text='@ #400', font=("Ink free",15), fill="white")
background.create_text(1100,425, text='@ #450', font=("Ink free",15), fill="white")

def confirmation():
    global cost,cost1,cost2,cost3,cost4,cost5
    total_cost = 0
    if combo1.get() != "Choose":
        cost = 350 * int(label1.get())
        total_cost+=cost
    if combo2.get() != "Choose":
        if combo2.get() != "Ofe Nsala":
            cost1 = 400 * int(label2.get())
            total_cost+=cost1
        else:
            cost1 = 450 * int(label2.get())
            total_cost+=cost1
    if combo3.get() != "Choose":
        cost2 = 100 * int(label3.get())
        total_cost+=cost2
    if combo4.get() != "Choose":
        if combo4.get() == "Savoury beans":
            cost3 = 350 * int(label4.get())
            total_cost+=cost3
        if combo4.get() == "Roasted Sweet Potatoes":
            cost3 = 300 * int(label4.get())
            total_cost+=cost3
        else:
            cost3 = 150 * int(label4.get())
            total_cost+=cost3
    if combo5.get != "Choose":
        if combo5.get() == "Water":
            cost4 = 200 * int(label5.get())
            total_cost+=cost4
        if combo5.get() == "Glass drink":
            cost4 = 150 * int(label5.get())
            total_cost+=cost4
        if combo5.get() == "Pet drink 35cl":
            cost4 = 300 * int(label5.get())
            total_cost+=cost4
        if combo5.get() == "Fresh yo":
            cost4 = 600 * int(label5.get())
            total_cost+=cost4
        if combo5.get() == "Glass/Canned malt":
            cost4 = 500 * int(label5.get())
            total_cost+=cost4
        else:
            cost4 = 350 * int(label5.get())
            total_cost+=cost4
    if combo6.get() != "Choose":
        if combo6.get() == "Sweet grilled chiken":
            cost5 = 1100 * int(label6.get())
            total_cost+=cost5
        if combo6.get() == "Grilled chicken wing":
            cost5 = 400 * int(label6.get())
            total_cost+=cost5
        if combo6.get() == "Fried beef":
            cost5 = 400 * int(label6.get())
            total_cost+=cost5
        if combo6.get() == "Fried fish":
            cost5 = 500 * int(label6.get())
            total_cost+=cost5
        else:
            cost5 = 200 * int(label6.get())
            total_cost+=cost5
    if total_cost < 1000:
        price = total_cost
        messagebox.showinfo("Bills",f"{label_1.get()} you are to pay {price}")
    elif total_cost < 2500:
        price = 0.1 * total_cost
        messagebox.showinfo("Bill",f"{label_1.get()}you are to pay {price} due to discount of 10% ")
    elif total_cost > 2500 and total_cost <= 5000:
        price = 0.15 * total_cost
        messagebox.showinfo("Bill",f"{label_1.get()}you are to pay {price} due to discount of 15% ")
    elif total_cost > 5000:
        price = 0.25 * total_cost
        messagebox.showinfo("Bill",f"{label_1.get()}you are to pay {price} due to discount of 25% ")

def conditions():
    global label_1,label1,label2,label3,label4,label5,label6
    root2 = Tk()
    root2.title("confirm order")
    root2.geometry("800x500")
    label = Label(root2,text=f"Input your name")
    label.pack()
    label_1 = Entry(root2)
    label_1.pack()
    if combo1.get() != "Choose":
        food = combo1.get()
        label = Label(root2,text=f"how many portions of {food}")
        label.pack()
        label1 = Entry(root2)
        label1.pack()
    if combo2.get() != "Choose":
        food1 = combo2.get()
        label = Label(root2,text=f"how many portions of {food1}")
        label.pack()
        label2 = Entry(root2)
        label2.pack()
    if combo3.get() != "Choose":
        food2 = combo3.get()
        label = Label(root2,text=f"how many portions of {food2}")
        label.pack()
        label3 = Entry(root2)
        label3.pack()
    if combo4.get() != "Choose":
        food3 = combo4.get()
        label = Label(root2,text=f"how many portions of {food3}")
        label.pack()
        label4 = Entry(root2)
        label4.pack()
    if combo5.get() != "Choose":
        food4 = combo5.get()
        label = Label(root2,text=f"how many portions of {food4}")
        label.pack()
        label5 = Entry(root2)
        label5.pack()
    if combo6.get() != "Choose":
        food5 = combo6.get()
        label = Label(root2,text=f"how many portions of {food5}")
        label.pack()
        label6 = Entry(root2)
        label6.pack()
    
    button = Button(root2,text="check in",command=confirmation)
    button.pack()

    root2.mainloop()

def check():
    global combo1,combo2,combo6,combo3,combo4,combo5
    root1 = Tk()
    root1.title("Place order")
    root1.geometry("800x500")

    rice_or_pasta = ["Choose","Jellof rice","Coconut Fried rice", "Jellof spaghetti"]
    soup = ["Choose","Egusi","Ofe Nsala"]
    swallow = ["Choose","Eba","Semo","Pounded yam"]
    side_dish = ["Choose","Savoury beans","Roasted Sweet Potatoes","Fried plantains","Mixed vegetable salad","Boiled yam"]
    beverages = ["Choose","Water","Glass drink","Pet drink 35cl","Pet drink 50cl","Fresh yo","Glass/Canned malt",
                "Pineapple juice","Mango juice","Zobo drink"]
    proteins = ["Choose","Sweet grilled checken","Grilled chicken wing","Fried beef","Fried fish","Boiled egg","Salted sausages"]

    #create dropdown menus for each list
    label1 =Label(root1,text="Choose from the Rice/pasta options").pack()
    combo1 =ttk.Combobox(root1, value=rice_or_pasta)
    combo1.current(0)
    combo1.bind("<<CombovoxSelected>>")
    combo1.pack()

    label2 =Label(root1,text="Choose from the Soup options").pack()
    combo2 =ttk.Combobox(root1, value=soup)
    combo2.current(0)
    combo2.bind("<<CombovoxSelected>>")
    combo2.pack()

    label3 =Label(root1,text="Choose from the Swallow options").pack()
    combo3 =ttk.Combobox(root1, value=swallow)
    combo3.current(0)
    combo3.bind("<<CombovoxSelected>>")
    combo3.pack()

    label4 =Label(root1,text="Choose from the Side dish options").pack()
    combo4 =ttk.Combobox(root1, value=side_dish)
    combo4.current(0)
    combo4.bind("<<CombovoxSelected>>")
    combo4.pack()

    label5 =Label(root1,text="Choose from the Beverages options").pack()
    combo5 =ttk.Combobox(root1, value=beverages)
    combo5.current(0)
    combo5.bind("<<CombovoxSelected>>")
    combo5.pack()

    label6 =Label(root1,text="Choose from the Protein options").pack()
    combo6 =ttk.Combobox(root1, value=proteins)
    combo6.current(0)
    combo6.bind("<<CombovoxSelected>>")
    combo6.pack()

    button = Button(root1,text="confirm",command=conditions)
    button.pack()


    root1.mainloop()

#button creation
button = Button(root,text="Place an order", command=check)
background.create_window(850,620, window=button)

root.mainloop()
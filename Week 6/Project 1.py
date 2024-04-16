import tkinter as tk
from tkinter import messagebox

#login window
#create main window
root = tk.Tk()
root.title("waybill details")
root.geometry("500x200")

#create firstname label and entry
location_label = tk.Label(root,text="Location")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

#create surname label and entry
weight_label = tk.Label(root,text="Weight of object")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

def submit():

    #get the input that has been given by user
   
    weight = int(weight_entry.get())
    location = location_entry.get()

    if location == "ibeju-lekki" and weight >= 10:
        messagebox.showinfo("details","You are to pay #5,000")
    elif location == "ibeju-lekki" and weight < 10:
        messagebox.showinfo("details","You are to pay #3,500")
    elif location == "epe" and weight >= 10:
        messagebox.showinfo("details","You are to pay #10,500")
    elif location == "epe" and weight < 10:
        messagebox.showinfo("details","You are to pay #5,000")
    elif location != "epe" and location != "ibeju-lekki":
        messagebox.showerror("details","We do not deliver to those areas yet ")
    else:
        messagebox.showerror("details","Invalid input")

button = tk.Button(root,text="submit",command=submit)
button.pack()

#run the main event loop
root.mainloop()
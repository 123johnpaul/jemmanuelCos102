import csv
import tkinter as tk
from tkinter import messagebox

#data of employees
data = {'First name': [],'Surname': [],'Department': [], 'S/N': []}
file_path = r"C:\Users\jhae4\Documents\jemmanuelCos102\Week 5\GIG-logistics.csv"
with open(file_path,"r") as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        data['First name'].append(i[2])
        data['Surname'].append(i[1])
        data['Department'].append(i[3])
        data['S/N'].append(i[0])

names = data['Surname']
dept = data['Department']
name = data['First name']
#login window
#create main window
root = tk.Tk()
root.title("Login form")
root.geometry("500x200")

#create firstname label and entry
firstname_label = tk.Label(root,text="Firstname")
firstname_label.pack()
firstname_entry = tk.Entry(root)
firstname_entry.pack()

#create surname label and entry
surname_label = tk.Label(root,text="Surname")
surname_label.pack()
surname_entry = tk.Entry(root)
surname_entry.pack()

#create department label and entry
department_label = tk.Label(root,text="Department")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

#get the input that has been given by user
department = department_entry.get()
surname = surname_entry.get()
firstname = firstname_entry.get()

def welcomemessage(firstname):
    #create Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"welcome {firstname}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="this are the names of employees in your department")
    label_2.pack()

    for i in data.values():
        if i[2] == department.title() and i[0] != firstname.title():
            tk.Label(window, text=f"{i[0]} {i[1]}").pack()
        else:
            continue

    #run the tkinter event loop
    root.mainloop()


def submit():
    check = []
    for i in data.values():
        if i[1] == surname.upper() and i[0] == firstname.title() and i[2] == department.title():
            check = i
        else:
            continue

    if check in data.values():
        welcomemessage(firstname)
    else:
        messagebox.showerror("Login", "Invalid credentials!")

            
        

button = tk.Button(root,text="submit",command=submit)
button.pack()

#run the main event loop
root.mainloop()
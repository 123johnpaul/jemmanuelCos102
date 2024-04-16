import tkinter as tk
from tkinter import messagebox


admitted = {'firstname':[],'surname':[],'jamb score':[],'course':[],'subjects':[]}
not_admitted = {'firstname':[],'surname':[],'jamb score':[],'course':[],'subjects':[]}


#create main window
root = tk.Tk()
root.title("Admission eligibility verification")
root.geometry("500x200")

firstname_label = tk.Label(root,text="Firstname")
firstname_label.pack()
firstname_entry = tk.Entry(root)
firstname_entry.pack()

surname_label = tk.Label(root,text="Surname")
surname_label.pack()
surname_entry = tk.Entry(root)
surname_entry.pack()

jamb_label = tk.Label(root,text="jamb score")
jamb_label.pack()
jamb_entry = tk.Entry(root)
jamb_entry.pack()

desired_course_label = tk.Label(root,text="Desired course")
desired_course_label.pack()
desired_course_entry = tk.Entry(root)
desired_course_entry.pack()

label = tk.Label(root,text="input yes if you have credited the following subjects in your Waec/Neco/igse/Gce")
label.pack()

subject1_label = tk.Label(root,text="Mathematics")
subject1_label.pack()
subject1_entry = tk.Entry(root)
subject1_entry.pack()


subject2_label = tk.Label(root,text="English")
subject2_label.pack()
subject2_entry = tk.Entry(root)
subject2_entry.pack()


subject3_label = tk.Label(root,text="Physics")
subject3_label.pack()
subject3_entry = tk.Entry(root)
subject3_entry.pack()


subject4_label = tk.Label(root,text="Biology")
subject4_label.pack()
subject4_entry = tk.Entry(root)
subject4_entry.pack()


subject5_label = tk.Label(root,text="Chemistry")
subject5_label.pack()
subject5_entry = tk.Entry(root)
subject5_entry.pack()

subject6_label = tk.Label(root,text="Economics")
subject6_label.pack()
subject6_entry = tk.Entry(root)
subject6_entry.pack()


subject7_label = tk.Label(root,text="Governmeent")
subject7_label.pack()
subject7_entry = tk.Entry(root)
subject7_entry.pack()


subject8_label = tk.Label(root,text="History")
subject8_label.pack()
subject8_entry = tk.Entry(root)
subject8_entry.pack()


def computer_science():
    course = desired_course_entry.get()
    name = firstname_entry.get()
    names = surname_entry.get()
    score = jamb_entry.get()
    chem = (subject5_entry.get()).lower()
    bio = (subject4_entry.get()).lower()
    phy = (subject3_entry.get()).lower()
    eng = (subject2_entry.get()).lower() 
    math = (subject1_entry.get()).lower()

    if math == "yes" and bio == "yes" and eng == "yes" and phy == "yes" and chem == "yes":
        admitted['firstname'].append(name)
        admitted['surname'].append(names)
        admitted['jamb score'].append(score)
        admitted['course'].append(course)
        admitted['subjects'].append("biology")
        admitted['subjects'].append("mathematics")
        admitted['subjects'].append("physics")
        admitted['subjects'].append("english")
        admitted['subjects'].append("chemistry")
        messagebox.showinfo("Admission","You have been admitted!!!")
    else:
        messagebox.showinfo("Admission","Sorry,but you were not admitted")

def mass_communication():
    course = desired_course_entry.get()
    name = firstname_entry.get()
    names = surname_entry.get()
    score = jamb_entry.get()
    govt = (subject7_entry.get()).lower()
    his = (subject8_entry.get()).lower()
    econs = (subject6_entry.get()).lower()
    eng = (subject2_entry.get()).lower() 
    math = (subject1_entry.get()).lower()

    if math == "yes" and econs == "yes" and eng == "yes" and his == "yes" and govt == "yes":
        admitted['firstname'].append(name)
        admitted['surname'].append(names)
        admitted['jamb score'].append(score)
        admitted['course'].append(course)
        admitted['subjects'].append("economics")
        admitted['subjects'].append("mathematics")
        admitted['subjects'].append("government")
        admitted['subjects'].append("english")
        admitted['subjects'].append("history")
        messagebox.showinfo("Admission","You have been admitted!!!")
    else:
        messagebox.showinfo("Admission","Sorry,but you were not admitted")

def submit():
    course = (desired_course_entry.get()).lower()
    score = int(jamb_entry.get())
    if course == "computer science":
        if score >= 250:
            computer_science()
        else:
            messagebox.showerror("Admission","Unfortunately your jamb score does not meet criteria")
    elif course == "mass communication":
        if score >= 230:
            mass_communication()
        else:
            messagebox.showerror("Admission","Unfortunately your jamb score does not meet criteria")
    else:
        messagebox.showerror("Admission","We have not started admitting other courses for now!!!")

button = tk.Button(root,text="submit",command=submit)
button.pack()

#run the main event loop
root.mainloop()
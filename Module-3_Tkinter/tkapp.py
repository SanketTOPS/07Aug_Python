import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()
screen.title("FirstApp")
screen.geometry('400x500')
screen.config(background='gold')

"""tkinter.Label(text="Firstname:").pack()
tkinter.Label(text="Lastname:").pack()"""

"""tkinter.Label(text="Firstname:").place(x=0,y=0)
tkinter.Label(text="Lastname:").place(x=0,y=30)"""


tkinter.Label(text="Firstname:",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=1,column=0,sticky='w')

fnm=tkinter.Entry()
fnm.grid(row=0,column=1,sticky='w')
lnm=tkinter.Entry()
lnm.grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text="Male",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Python",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Android",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="iOS",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=5,column=0,sticky='w')
tkinter.Checkbutton(text="JAVA",bg='gold',font='Aptos 15 bold',fg='blue').grid(row=6,column=0,sticky='w')


city=['Rajkot','Ahmedabad','Baroda','Surat','Junagadh','Jamnagar']
ttk.Combobox(values=city).grid(row=7,column=0,sticky='w')

def btnclick():
    #print("Buttom clicked!")
    #messagebox.showerror('Error','Something went wrong...Try again!')
    #messagebox.showinfo("Success","Your form has been submitted!")
    #messagebox.showwarning("Warning","Your disk is full!")
    print("Firstname:",fnm.get())
    print("Lastname:",lnm.get())

tkinter.Button(text="Submit",font='Aptos 15 bold',fg='blue',command=btnclick).place(x=150,y=280)

tkinter.mainloop()
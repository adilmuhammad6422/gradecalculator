import tkinter
from tkinter import *

gui = Tk()
gui.title("Grade calculator")
gui.geometry("500x500")

def Calculation():
    exam1g = int(e1entry.get())
    exam2g = int(e2entry.get())
    exam3g = int(e3entry.get())
    hwg = int(hwentry.get())
    total = (exam1g+exam2g+exam3g+hwg)
    Label(text=f"{total}",font = "arial 15 bold").place(x=250,y=210)
    avg = int(total * 0.25)
    Label(text=f"{avg}",font="arial 15 bold").place(x=250,y=254)
    if avg < 50:
        grade = "F"
    elif avg > 50 and avg < 65:
        grade = "D"
    elif avg > 65 and avg < 79:
        grade = "C"
    elif avg > 79 and avg < 89:
        grade = "B"
    elif avg > 89 and avg < 100:
        grade = "A"
    Label(text=f"{grade}",font="arial 15 bold").place(x=250,y=300)




exam1 = Label(gui,text = "Exam 1:", font = "arial 10")
exam2 = Label(gui,text = "Exam 2:", font = "arial 10")
exam3 = Label(gui,text = "Exam 3:", font = "arial 10")
hw = Label(gui,text = "Homework:", font = "arial 10")
total = Label(gui,text = "Total:", font = "arial 10")
avg = Label(gui,text = "Average:", font = "arial 10")
grade = Label(gui,text = "Grade:", font = "arial 10")

exam1.place(x=50,y=20)
exam2.place(x=50,y=70)
exam3.place(x=50,y=120)
hw.place(x=50,y=170)
total.place(x=50,y=210)
avg.place(x=50,y=254)
grade.place(x=50,y=300)

e1value = StringVar()
e2value = StringVar()
e3value = StringVar()
hwvalue = StringVar()

e1entry = Entry(gui,textvariable=e1value,font= "arial 15",width=15)
e2entry = Entry(gui,textvariable=e2value,font= "arial 15",width=15)
e3entry = Entry(gui,textvariable=e3value,font= "arial 15",width=15)
hwentry = Entry(gui,textvariable=hwvalue,font= "arial 15",width=15)

e1entry.place(x=250,y=20)
e2entry.place(x=250,y=70)
e3entry.place(x=250,y=120)
hwentry.place(x=250,y=170)

Button(text="Calculuate",font="arial 15",bg="white",bd=10,command=Calculation).place(x=70,y=400)
Button(text="Exit",font="arial 15",bg="white",bd=10,width=8,command=lambda:exit()).place(x=300,y=400)

gui.mainloop()
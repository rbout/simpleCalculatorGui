from tkinter import *
import re


def button():
    linemather = re.compile(r'([0-9]+)([+]|[-]|[*]|[/]|[//])([0-9]+)')
    line = linemather.search(inp.get())
    if str(line.group(2)) in "+":
        ans = int(line.group(1)) + int(line.group(3))
        var.set("= " + str(ans))
    elif str(line.group(2)) in "-":
        ans = int(line.group(1)) - int(line.group(3))
        var.set("= " + str(ans))
    elif str(line.group(2)) in "*":
        ans = int(line.group(1)) * int(line.group(3))
        var.set("= " + str(ans))
    elif str(line.group(2)) in "/":
        ans = int(line.group(1)) / int(line.group(3))
        var.set("= " + str(ans))


def entered(e):
    linemather = re.compile(r'([0-9]+)([+]|[-]|[*]|[/]|[//])([0-9]+)')
    line = linemather.search(inp.get())
    if str(line.group(2)) in "+":
        ans = int(line.group(1)) + int(line.group(3))
        var.set("= " + str(ans))
    elif str(line.group(2)) in "-":
        ans = int(line.group(1)) - int(line.group(3))
        var.set("= " + str(ans))
    elif str(line.group(2)) in "*":
        ans = int(line.group(1)) * int(line.group(3))
        var.set("= " + str(ans))
    elif str(line.group(2)) in "/":
        ans = int(line.group(1)) / int(line.group(3))
        var.set("= " + str(ans))


top = Tk()
top.title("Math")
top.config(bg="white")
top.bind("<Return>", entered)
windowWidth = top.winfo_reqwidth()
windowHeight = top.winfo_reqheight()

positionRight = int(top.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(top.winfo_screenheight()/2 - windowHeight/2)

top.geometry("+{}+{}".format(positionRight, positionDown))

var = StringVar()
w = Label(top, textvariable=var)
inp = Entry(top, width=10)

b = Button(top, text="Calculate", command=lambda: button())

inp.grid(row=1, column=1)
b.grid(row=1, column=2)
w.grid(row=2, column=1)
top.mainloop()

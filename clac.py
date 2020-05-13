from tkinter import *

root = Tk()

root.title('CALCULATOR')
equa = ""
equation = StringVar()


# def evaluate(event):
#     # data="871 +3"
#     equation.set(eval(equation))
#     print(equation)

# def num(number):
#     data.append(number)
#     ans.configure(text=eval(str(data)))

def equalbtn():
    global equa
    total = eval(str(equa))
    equation.set(total)
    equa=""

def btnpress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def getclear():
    global equa
    equa=""
    equation.set(equa)

ans = Label(root)
ans.grid()


root.geometry("180x210")

# entry = Entry(root, textvariable=equation)
# entry.bind("<Return>", evaluate)
# entry.grid(row=0, column=0, columnspan=5, pady=5)

top=Label(root,textvariable=equation,relief=SUNKEN)
top.grid(row=0,column=1,columnspan=5,pady=5,sticky=E+W+N+S)


b9 = Button(root, text=9, width=4, height=2, command=lambda: btnpress(9))
b9.grid(row=1, column=0)

b8 = Button(root, text=8, width=4, height=2, command=lambda: btnpress(8))
b8.grid(row=1, column=1, padx=5)

b7 = Button(root, text=7, width=4, height=2, command=lambda: btnpress(7))
b7.grid(row=1, column=2)

b6 = Button(root, text=6, width=4, height=2, command=lambda: btnpress(6))
b6.grid(row=2, column=0)

b5 = Button(root, text=5, width=4, height=2, command=lambda: btnpress(5))
b5.grid(row=2, column=1)

b4 = Button(root, text=4, width=4, height=2, command=lambda: btnpress(4))
b4.grid(row=2, column=2)

b3 = Button(root, text=3, width=4, height=2, command=lambda: btnpress(3))
b3.grid(row=3, column=0)

b2 = Button(root, text=2, width=4, height=2, command=lambda: btnpress(2))
b2.grid(row=3, column=1)

b1 = Button(root, text=1, width=4, height=2, command=lambda: btnpress(1))
b1.grid(row=3, column=2)

bp = Button(root, text="+", width=4, height=2, command=lambda: btnpress("+"))
bp.grid(row=1, column=3, padx=5)

b0 = Button(root, text="0", width=4, height=2, command=lambda: btnpress(0))
b0.grid(row=4, column=0)

bde = Button(root, text=".", width=4, height=2, command=lambda: btnpress("."))
bde.grid(row=4, column=1)

be = Button(root, text="=", width=4, height=2, command=equalbtn,bg='grey')
be.grid(row=4, column=2)

bd = Button(root, text="/", width=4, height=2, command=lambda: btnpress("/"))
bd.grid(row=4, column=3)

bm = Button(root, text="-", width=4, height=2, command=lambda: btnpress("-"))
bm.grid(row=2, column=3)

bmt = Button(root, text="*", width=4, height=2, command=lambda: btnpress("*"))
bmt.grid(row=3, column=3)

clear = Button(root, text="C", width=4, height=2, command=getclear,bg='orange red')
clear.grid(row=0, column=0)

root.mainloop()

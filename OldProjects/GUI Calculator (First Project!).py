from tkinter import *
import math
#GUI calculator
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def pi():
    global expression
    expression = str(math.pi)
    equation.set(expression)

def back():
    global expression
    expression = expression
    equation.set(expression)

if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")

    frame_display = Frame(master=window, width=200, height=100)
    frame_display.grid(row=0, column=0)
    frame_buttons = Frame(master=window, width=200, height=400)
    frame_buttons.grid(row=1, column=0)

    equation = StringVar()

    frame_buttons.rowconfigure([0,1,2,3,4], minsize=50, weight=1)
    frame_buttons.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

    display_text = Entry(master=frame_display, textvariable=equation)
    display_text.pack()

    operator_clear = Button(master=frame_buttons, width=2, height=2, text="C", command=clear)
    operator_clear.grid(row=0, column=0)
    operator_R = Button(master=frame_buttons, width=2, height=2, text="\u03C0", command=pi)
    operator_R.grid(row=0, column=1)
    operator_back = Button(master=frame_buttons, width=2, height=2, text="B", command=back)
    operator_back.grid(row=0, column=2)
    operator_division = Button(master=frame_buttons, width=2, height=2, text=chr(247), command=lambda: press("/"))
    operator_division.grid(row=0, column=3)

    number1 = Button(master=frame_buttons, width=2, height=2, text="1", command=lambda: press(1))
    number1.grid(row=1, column=0)
    number2 = Button(master=frame_buttons, width=2, height=2, text="2", command=lambda: press(2))
    number2.grid(row=1, column=1)
    number3 = Button(master=frame_buttons, width=2, height=2, text="3", command=lambda: press(3))
    number3.grid(row=1, column=2)

    number4 = Button(master=frame_buttons, width=2, height=2, text="4", command=lambda: press(4))
    number4.grid(row=2, column=0)
    number5 = Button(master=frame_buttons, width=2, height=2, text="5", command=lambda: press(5))
    number5.grid(row=2, column=1)
    number6 = Button(master=frame_buttons, width=2, height=2, text="6", command=lambda: press(6))
    number6.grid(row=2, column=2)

    number7 = Button(master=frame_buttons, width=2, height=2, text="7", command=lambda: press(7))
    number7.grid(row=3, column=0)
    number8 = Button(master=frame_buttons, width=2, height=2, text="8", command=lambda: press(8))
    number8.grid(row=3, column=1)
    number9 = Button(master=frame_buttons, width=2, height=2, text="9", command=lambda: press(9))
    number9.grid(row=3, column=2)

    number_minus = Button(master=frame_buttons, width=2, height=2, text="-", command=lambda: press("-"))
    number_minus.grid(row=4, column=0)
    number0 = Button(master=frame_buttons, width=2, height=2, text="0", command=lambda: press(0))
    number0.grid(row=4, column=1)
    number_dot = Button(master=frame_buttons, width=2, height=2, text=".", command=lambda: press("."))
    number_dot.grid(row=4, column=2)

    operator_multiply = Button(master=frame_buttons, width=2, height=2, text=chr(215), command=lambda: press("*"))
    operator_multiply.grid(row=1, column=3)
    operator_add = Button(master=frame_buttons, width=2, height=2, text="+", command=lambda: press("+"))
    operator_add.grid(row=2, column=3)
    operator_minus = Button(master=frame_buttons, width=2, height=2, text="-", command=lambda: press("-"))
    operator_minus.grid(row=3, column=3)
    operator_equal = Button(master=frame_buttons, width=2, height=2, text="=", command=equal)
    operator_equal.grid(row=4, column=3)

    window.mainloop()

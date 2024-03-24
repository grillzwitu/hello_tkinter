from tkinter import *

window = Tk()
window.title("Basic Calculator")

#The display
display = Entry(window, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=12, pady=12)

# Helper Methods

def button_click(btn_txt):
    """
    Action for when a button is clicked
    """

    current = display.get()

    #Delete what is currently displayed
    display.delete(0, END)

    #Insert the button text
    display.insert(0, str(current) + str(btn_txt))

def btn_clear() -> None:
    """
    Action for when the clear button is clicked
    """
    #Delete what is currently displayed
    display.delete(0, END)

def btn_add() -> None:
    """
    Action for when the add button is clicked
    """
    first_num = display.get()
    global f_num
    global math_op
    math_op = "+"
    f_num = float(first_num)
    display.delete(0, END)

def btn_minus() -> None:
    """
    Action for when the add button is clicked
    """

    first_num = display.get()
    global f_num
    global math_op
    math_op = "-"
    f_num = float(first_num)
    display.delete(0, END)


def btn_multiply() -> None:
    """
    Action for when the add button is clicked
    """

    first_num = display.get()
    global f_num
    global math_op
    math_op = "*"
    f_num = float(first_num)
    display.delete(0, END)


def btn_divide() -> None:
    """
    Action for when the add button is clicked
    """

    first_num = display.get()
    global f_num
    global math_op
    math_op = "/"
    f_num = float(first_num)
    display.delete(0, END)


def btn_equals() -> None:
    """
    Action for when the equals button is clicked
    """
    sec_num = display.get()
    display.delete(0, END)
    if math_op == "+":
        display.insert(0, f_num + float(sec_num))
    elif math_op == "-":
        display.insert(0, f_num - float(sec_num))
    elif math_op == "*":
        display.insert(0, f_num * float(sec_num))
    elif math_op == "/":
        display.insert(0, f_num / float(sec_num))
    


#The buttons
button1 = Button(window, text="1", padx=30, pady=20, command=lambda: button_click(1))
button2 = Button(window, text="2", padx=30, pady=20, command=lambda: button_click(2))
button3 = Button(window, text="3", padx=30, pady=20, command=lambda: button_click(3))
button4 = Button(window, text="4", padx=30, pady=20, command=lambda: button_click(4))
button5 = Button(window, text="5", padx=30, pady=20, command=lambda: button_click(5))
button6 = Button(window, text="6", padx=30, pady=20, command=lambda: button_click(6))
button7 = Button(window, text="7", padx=30, pady=20, command=lambda: button_click(7))
button8 = Button(window, text="8", padx=30, pady=20, command=lambda: button_click(8))
button9 = Button(window, text="9", padx=30, pady=20, command=lambda: button_click(9))
button0 = Button(window, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=29, pady=20, command=lambda: btn_add())
button_equals = Button(window, text="=", padx=75, pady=20, command=lambda: btn_equals())
button_clear = Button(window, text="clear", padx=66.3, pady=20, command=lambda: btn_clear())

button_minus = Button(window, text="-", padx=30.3, pady=20, command=lambda: btn_minus())
button_multiply = Button(window, text="*", padx=30, pady=20, command=lambda: btn_multiply())
button_divide = Button(window, text="/", padx=31, pady=20, command=lambda: btn_divide())

#digits position
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5,column=0)
button_equals.grid(row=5, column=1, columnspan=2)

button_minus.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


window.mainloop()

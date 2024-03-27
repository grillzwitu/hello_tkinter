from tkinter import *
from PIL import ImageTk, Image

# Initializing the app/window/interface.
root = Tk()

# Change the window title
root.title("Hello Tkinter")

#Creating label Widgets
myLabel1 = Label(root, text="Hello Tkinter")
myLabel2 = Label(root, text="Another Label Here")
myLabel3 = Label(root, text="It's Label widgets here")

#simple click function

def click() :  
    clickLabel = Label(root, text=input1.get())
    clickLabel.grid(row=4, column=1)

#Creating a button widget
myButton1 = Button(root, text="Just a button", padx=20, pady=20, bg="red", command=click)

#Creating Input field Widget
input1 = Entry(root, width=20)
input1.insert(0, "Enter anything")

#Just packing widget into the app
# myLabel.pack()

#Using Grid to aad widgets to the app
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)
myButton1.grid(row=3, column=1)
input1.grid(row=2, column=1)


#Images, Icons and Exits buttons

# add/change window icon
root.iconbitmap("./assets/icons/currency_exchange_finance_coins_money_usd_dollar_icon_262507.ico")

#create an exit button
btn_exit = Button(root, text="Exit", command=root.quit)
btn_exit.grid(row=10, column=1)

#Images
img1 = ImageTk.PhotoImage(Image.open("./assets/images/apple_pic.jpg"))
img_label = Label(image=img1)
img_label.grid(row=5, column=1)

#Frames

frame = LabelFrame(root, text="A simple frame", padx=5, pady=5)
frame.grid(row=6, column=0, padx=10, pady=10)

frm_btn = Button(frame, text="Button in a Frame")
frm_btn.grid(row=0, column=0)

#Radio Button

treat_select = StringVar(value="None")

def  selected(value):
    """
    Faciclitates the selection of a radio button
    """
    global selection

    selection.grid_forget()

    selection = Label(frame, text=value)
    selection.grid(row=3, column=1)

rdio_btn1 = Radiobutton(frame, text="cake", variable=treat_select, value="cake", command= lambda: selected(treat_select.get()))
rdio_btn2 = Radiobutton(frame, text="cookie", variable=treat_select, value="cookie", command= lambda: selected(treat_select.get()))
rdio_btn1.grid(row=1, column=1)
rdio_btn2.grid(row=2, column=1)


selection = Label(frame)
selection.grid(row=3, column=1)

root.mainloop()

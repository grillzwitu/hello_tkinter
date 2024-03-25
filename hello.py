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
btn_exit.grid(row=7, column=1)

#Images
img1 = ImageTk.PhotoImage(Image.open("./assets/images/apple_pic.jpg"))
img_label = Label(image=img1)
img_label.grid(row=5, column=1)

root.mainloop()

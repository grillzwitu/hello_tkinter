from tkinter import *

# Initializing the app.
root = Tk()

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





root.mainloop()

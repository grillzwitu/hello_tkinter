from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Simple Image Viewer")

img_1 = ImageTk.PhotoImage(Image.open("./assets/images/apple_pic.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("./assets/images/dragonfly-pic.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("./assets/images/grasshopper-pic.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("./assets/images/poppy-pic.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("./assets/images/toadstool-pic.jpg"))

img_list = [img_1, img_2, img_3, img_4, img_5]

display = Label(image=img_1)
display.grid(row=0, column=0, columnspan=3)

#Helper functions

def next() -> None:
    """
    Handles clicking the forward button
    """

    global my_display
    global fwd_btn
    global bck_btn

    display.grid_forget()


def previous() -> None:
    """
    Handles clicking the back button
    """

    global display
    global fwd_btn
    global bck_btn

    display.grid_forget()


back_btn = Button(window, text="<<", padx=15, command= lambda: next())
back_btn.grid(row=1, column=0,)

forward_btn = Button(window, text=">>", padx=15, command= lambda: previous())
forward_btn.grid(row=1, column=2)


exit_btn = Button(window, text="Close", command=window.quit)
exit_btn.grid(row=3, column=1)


window.mainloop()

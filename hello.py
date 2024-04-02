from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

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
    """
    Implements the click action of a button
    """
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
btn_exit.grid(row=15, column=1)

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

treat_select = StringVar(value="None") #defining a variable for the group of radio buttons

def  selected(value):
    """
    Implements the selection of a radio button
    """
    global selection

    selection.grid_forget() #clear any current selection

    # Display the selection
    selection = Label(frame, text=value)
    selection.grid(row=3, column=1)

#creating the buttons and displaying them in a frame
rdio_btn1 = Radiobutton(frame, text="cake", variable=treat_select, value="cake", command= lambda: selected(treat_select.get()))
rdio_btn2 = Radiobutton(frame, text="cookie", variable=treat_select, value="cookie", command= lambda: selected(treat_select.get()))
rdio_btn1.grid(row=1, column=1)
rdio_btn2.grid(row=2, column=1)

# Display the radio button selection
selection = Label(frame)
selection.grid(row=3, column=1)

# Alternative approach to craeting radio buttons.

BREAKFAST_LIST = [
    ("Okpa", "Okpa"),
    ("Ewa-goin", "Ewa-goin"),
    ("Fruit-salad", "Fuit-salad")
]

breakfast = StringVar(value="None") #the variable for the radio buttons

#creating the buttons

row_pos: int = 4

for key, val in BREAKFAST_LIST:
    Radiobutton(frame, text=key, variable=breakfast, value=val, command= lambda: selected(breakfast.get())).grid(row=row_pos, column=1)
    row_pos += 1


# Message Box
    
def pop_mb() -> None:
    """
    Implements the opening the message box 
    """

#    messagebox.showinfo(title="Info Message box", message="You wanted to see a message box")
    decision = messagebox.askyesnocancel(title="Simple yes or no message box", message="Say yes or no") #stored in a variable because it requires further action

    # print(type(decision))

    if decision == 1:
        your_answer = Label(root, text="You clicked Yes").grid(row=8, column=1)
    elif decision == 0:
        your_answer = Label(root, text="You clicked No").grid(row=8, column=1)
    else:
        return

    
prompt_btn = Button(root, text="Pop the message box", command=pop_mb).grid(row=7, column=0)

#Create new windows

def new_window() -> None:
    """
    Implements creating the new window
    """

    new_window = Toplevel() #creates the new window.
    Label(new_window, text="This is a new window").grid(row=0, column=0) # creates and adds this label to the new window

nu_window_btn = Button(root, text="Pop a new window", command=new_window).grid(row=7, column=1)

# Upload a file (File upload dialog)

def upload_img():
    """
    Implements file upload 
    """

    root.filename = filedialog.askopenfilename(initialdir="./assets/images/", title="Select a File", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))
    file_uploaded = Label(root, text=root.filename).grid(row=8, column=1, pady=20) #display the location of the uploded image

    new_window1 = Toplevel()
    global uploaded_img #define the image as a global variable to prevent from being garbage collected.
    uploaded_img = ImageTk.PhotoImage(Image.open(root.filename)) #open the image
    img_label = Label(new_window1, image=uploaded_img).grid(row=1, column=1) # display the image in a label, in the new window
    # img_label.image = uploaded_img # set the image and have it display for as long as the label widget exists. N/B the image does not display without this line of code, however it throws an exception


upload_file_btn = Button(root, text="upload an image", command=upload_img).grid(row=7, column=2)

#Sliders
vertical_slider = Scale(root, from_=0, to=100)
vertical_slider.grid(row=0, column=15)

horizontal_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal_slider.grid(row=1, column=15)

#root.geometry(str(horizontal_slider.get()) + "x" + str(vertical_slider.get())) #changes the size of the main window

#Check Boxes

def new_window1() -> None:
    """
    Implements creating the new window
    """

    new_window = Toplevel() #creates the new window.
    Label(new_window, text="This is a new window").grid(row=0, column=0) # creates and adds this label to the new window

    # creating a frame container for the check bx
    cont_frame = LabelFrame(new_window, text="Check a box or some boxes",pady=10, padx=10)
    cont_frame.grid(row=1, column=0, pady=5, padx=5)

    #Defining a variable to store the value for the checkbox
    check_selection = StringVar()

    #Creating the checkbox
    check_box1 = Checkbutton(cont_frame, text="check for checking sakes", variable=check_selection, onvalue="Checked", offvalue="Not checked")
    #check_box1.deselect()
    check_box1.grid(row=0, column=0)
    
    print_selection = Label(cont_frame, text=check_selection.get()).grid(row=2, column=1)

    def check_selection_value():

        #print_selection = Label(cont_frame, text="").grid(row=2, column=1)

        print_selection = Label(cont_frame, text=check_selection.get()).grid(row=2, column=1)

    check_selection_value_btn = Button(cont_frame, text="What is checked", command=check_selection_value).grid(row=3, column=1)



nu_window_btn1 = Button(root, text="Pop another new window, try check boxes", command=new_window1).grid(row=9, column=0, pady=10, padx=10)


#Define a variable to store the value for the selected box(es)

# check_selection = IntVar()

# check_box1 = Checkbutton(cont_frame, text="check for checking sakes", variable=check_selection).grid(row=0, column=1)

#To Do: Try to clear old value instead of displaying over.

#Drop down 

dd_value = StringVar(value="None") # variable to store the selected value from the menu options

drp_menu = OptionMenu(frame, dd_value, "Rice", "Corn", "Millet", "Groundnut").grid(row=8, column=0) # drop-down menu in a frame

#Integrating Databases (sqlite3)

connct = sqlite3.connect("test.db") #initialize db
the_cursr = connct.cursor() #create cursor

#Creating a table

# the_cursr.execute("""CREATE TABLE contacts (
#                   first_name text,
#                   last_name text,
#                   phone_number integer,
#                   zip_code integer
# )""")


def toggleDbUI():
    """Opens a new window for database UI"""

    new_window2 = Toplevel() #new window to for db inputs

    f_name_lbl = Label(new_window2, text="First name").grid(row=0, column=0)
    first_name = Entry(new_window2, width=30)
    first_name.insert(0, "First name")
    first_name.grid(row=0, column=1)

    l_name_lbl = Label(new_window2, text="Last name").grid(row=1, column=0)
    last_name = Entry(new_window2, width=30)
    last_name.insert(0, "Last name")
    last_name.grid(row=1, column=1)

    phone_num_lbl = Label(new_window2, text="Phone number").grid(row=2, column=0)
    phone_number = Entry(new_window2, width=30)
    phone_number.insert(0, "Phone number")
    phone_number.grid(row=2, column=1)

    zp_code_lbl = Label(new_window2, text="Zip Code").grid(row=3, column=0)
    zip_code = Entry(new_window2, width=30)
    zip_code.insert(0, "Zip code")
    zip_code.grid(row=3, column=1)

    submit_btn = Button(new_window2, text="Submit" ).grid(row=4, column=0, pady=10)


db_ui_btn = Button(root, text="see db UI", command=toggleDbUI).grid(row=9, column=1)

connct.commit() #commit changes
connct.close() #close connection

root.mainloop()

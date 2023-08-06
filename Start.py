# -------------------------------------------  IMPORT Library
import sqlite3
from tkinter import *
from tkcalendar import *



#Welcome window main function
def welcomeWindow():
    Welcome = Tk()
    Welcome.geometry("1280x720")
    Welcome.configure(background="white")
    Welcome.title("Welcome")
    Welcome.resizable(False, False)
    Welcome.grab_set()

    #Black frame around outisde
    mainborder = Frame(Welcome, bg="gray16")
    mainborder.place(height=720,width=1235,x=0, y=0)
    viewborder = Frame(Welcome, bg="white")
    viewborder.place(height=720,width=1235,x=20, y=20)

    #Label for welcome
    welcome_Text = Label(viewborder, text="New York Restaurent Inspection Tool", fg="red", font="Leelawadee 25")
    welcome_Text.place(height=35, width=1110, x=0, y=0)
    #Text for instructions 
    welcome_Text = Label(viewborder, text="Instructions", fg="red", font="Leelawadee 25")
    welcome_Text.place(height=35, width=1110, x=0, y=30)

    #Text for welcome instructions
    welcome_Text = Label(viewborder, text="Welcome! \n Please read the user manual for instructions for how to \n use the program. Once ready, press the start button the \n right to begin.", fg="#000000",
                   font="Leelawadee 25")
    welcome_Text.place(height=180, width=1110, x=0, y=60)

    welcome_Text = Label(viewborder, text="To start the Analysis click on Start then select your parameters", fg="#000000",
                   font="Leelawadee 25")
    welcome_Text.place(height=180, width=1110, x=0, y=240)



    #Function to change to main window
    def Skip():
                Welcome.destroy()
                from report_window import report
                report()
        
    button_details_ = Button(viewborder, text="Start", bg="gray35",fg="black",font="Leelawadee 18", command=Skip)
    button_details_.place(height=40,width=120,x=950,y=20)

    #Run Window 
    Welcome.mainloop()
    Welcome.widthdraw()



welcomeWindow()
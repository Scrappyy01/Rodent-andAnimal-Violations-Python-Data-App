from tkinter import *


def Animal_Violations():
        Animals = Tk()
        Animals.geometry("1280x720")
        Animals.configure(background="white")
        Animals.title("Animal Violations")
        Animals.resizable(False, False)
        Animals.grab_set()

        #Frame
        mainborder = Frame(Animals, bg="black")
        mainborder.place(height=735,width=1280,x=0, y=0)

        viewborder = Frame(Animals, bg="white")
        viewborder.place(height=610,width=1235,x=20, y=20)

        #Image of data
        photo = PhotoImage(file="Animals2.png", height = 600, width = 1200)
        label = Label(viewborder, image=photo, bg="white")
        label.pack()
        

   
        #Function to return back to main page.
        def back():
                Animals.destroy()
                from report_window import report
                report()
        add_details_ = Button(viewborder, text="X", bg="gray35",fg="#6699cc",font="Leelawadee 18", command=back)
        add_details_.place(height=40,width=40,x=1170,y=20)

        Animals.mainloop()
        Animals.withdraw()
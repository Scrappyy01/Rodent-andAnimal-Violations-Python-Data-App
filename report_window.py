import sqlite3
from tkinter import *
from tkcalendar import *
from tkinter import ttk,messagebox
import tkinter as tk

from ExecReport import Exec
from Animal_Violations_Report import Animal_Violations
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)


def report():
        report_window = Tk()
        report_window.geometry("1280x720")
        report_window.configure(background="gray16")
        report_window.title("Report Window")
        report_window.resizable(False, False)
        report_window.grab_set()

        #Connect to database
        mydb = sqlite3.connect("data_file.db")
        mycursor = mydb.cursor()

        #Black Frame around program
        mainborder = Frame(report_window, bg="gray16")
        mainborder.place(height=720,width=1235,x=0, y=0)

        viewborder = Frame(report_window, bg="white")
        viewborder.place(height=720,width=1235,x=20, y=20)


        #Page Title 
        label_=Label(viewborder, bg="white",text="New York Restaurent Report",fg="black",font="Times 20")
        label_.place(height=35,width=1110,x=0, y=0)
 
        #Drop down box for searching by retaurant name or Inspection Data
        combo2_for_search_by =ttk.Combobox (report_window, values=['Restaurant Name','Violation Keyword'],width=5)
        combo2_for_search_by.place(height=30,width=140,x=500, y=70)


        #Search box to query database with keyword
        SEARCH_ENTRY= Entry(report_window,font="Leelawadee 14",bg="#ffffff",fg="black",insertbackground="white")
        SEARCH_ENTRY.place(height=40,width=190,x=460, y=105)


        #Lables for Start date, Enddate and Keyword 

        endDateLabel = Label(report_window, text= "End Date", fg="#000000")  
        endDateLabel.place(height=40,width=90,x=310,y=100)
        
        startDateLabel=Label(report_window, text= "Start Date", fg="#000000")
        startDateLabel.place(height=40,width=90,x=70,y=100)

        endDateLabel = Label(report_window, text= "Keyword", fg="#000000")  
        endDateLabel.place(height=40,width=90,x=510,y=150)

        #Variables for storing user input date data
        other = tk.StringVar()
        other2 = tk.StringVar()

        #Start Date Input 
        START_DATE = DateEntry(report_window, textvariable = other, width= 16, background= "magenta3", foreground= "white",bd=2)
        START_DATE.place(height=40,width=190,x=30,y=55)
        
        #End Date Input 
        END_DATE = DateEntry(report_window, textvariable = other2, width= 16, background= "green", foreground= "white",bd=2)
        END_DATE.place(height=40,width=190,x=250,y=55)

        #View Graph 
        graphview = Frame(report_window, bg="gray40")
        graphview.place(height=400,width=1300,x=20, y=240)
        

        limit = Label(graphview,bg='#6699cc',fg="white",text="New York Restaurant data. 100 Listings",font="Leelawadee 12",justify=CENTER)
        limit.place(height=30,width=1250,x=0, y=0)

        #Table Placement
        Table = ttk.Treeview(graphview, selectmode ='browse')

        Table.place(height = 370,width=1110, x=00,y=30)

        #Vertical Scroll bar 
        vsb = ttk.Scrollbar(graphview,orient="vertical",command=Table.yview)
        vsb.place(x=1100, y=31, height=368)
        Table.configure(yscrollcommand=vsb.set)

        #Horizontal Scroll bar 
        vsb = ttk.Scrollbar(graphview,orient="horizontal",command=Table.xview)
        vsb.place(x=1, y=379, width=1092,height=20)
        Table.configure(xscrollcommand=vsb.set)

        


        #Creating Data Table

        #Establish columns

        Table["columns"] = ("1","2","3","4","5","6","7","8","9","10","11")
        # Defining heading
        Table['show'] = 'headings'
        

        #Create columns with number and width size

        Table.column("1", width = 120, anchor ='c')
        Table.column("2", width =300, anchor ='c')
        Table.column("3", width = 120, anchor ='c')
        Table.column("4", width = 150, anchor ='c')
        Table.column("5", width = 120, anchor ='c')
        Table.column("6", width = 300, anchor ='c')
        Table.column("7", width = 120, anchor ='c')
        Table.column("8", width = 400, anchor ='c')
        Table.column("9", width = 110, anchor ='c')
        Table.column("10", width = 150, anchor ='c')
        Table.column("11", width = 300, anchor ='c')
        

        #Giving each column a heading
        Table.heading("1", text ="CAMIS")
        Table.heading("2", text ="DBA (Restaurant Name)")
        Table.heading("3", text ="BORO")
        Table.heading("4", text ="CUISINE DESCRIPTION")
        Table.heading("5", text ="INSPECTION DATE")
        Table.heading("6", text ="ACTIONS")
        Table.heading("7", text ="VIOLATION CODE")
        Table.heading("8", text ="VIOLATION DESCRIPTION")
        Table.heading("9", text ="GRADE")
        Table.heading("10", text ="SCORE")
        Table.heading("11", text ="INSPECTION TYPE")

        #Delete current data within table
        Table.delete(*Table.get_children())
        #Query Database and grab new data
        mycursor.execute("""SELECT CAMIS,DBA,BORO,CUISINEDESCRIPTION,INSPECTION_DATE,ACTIONS,VIOLATION_CODE,VIOLATION_DESCRIPTION,GRADE,SCORE,INSPECTION_TYPE  FROM record LIMIT 100;""")
        table_data = mycursor.fetchall()
        

        #For loop to iterate through data and place each value one after the other into each array
        indexer = 1
        for value in table_data:
                Table.insert("", 'end', text ="L"+str(indexer),values =(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]))
                indexer +=1







        def bar_graph():
                
                record = []
                new = []
                # access data from treeview
                try:
                        for parent in Table.get_children():
                                for child in Table.item(parent)['values']:
                                        record.append(child)

                        start = 0
                        end = 11
                        RECORDS = int(len(record) / 11)

                        for i in range(RECORDS):
                                tuple_ = tuple(record[start:end])
                                new.append(tuple_)
                                start = start + 11
                                end = end + 12

                        # empty lists to store data from database
                        CAMIS = []
                        DBA = []
                        BORO = []
                        CUSINE_DESCRIPTION = []
                        INSPECTION_DATE = []
                        ACTION = []
                        VOILATION_CODE = []
                        VOILATION_DESCRIPTION = []
                        GRADE = []
                        SCORE = []
                        INSPECTION_TYPE = []

                        # append data into the empty lists
                        for record in new:
                                CAMIS.append(record[0])
                                DBA.append(record[1])
                                BORO.append(record[2])
                                CUSINE_DESCRIPTION.append(record[3])
                                INSPECTION_DATE.append(record[4])
                                ACTION.append(record[5])
                                VOILATION_CODE.append(record[6])
                                VOILATION_DESCRIPTION.append(record[7])
                                GRADE.append(record[8])
                                SCORE.append(record[9])
                                INSPECTION_TYPE.append(record[10])

                        # convert all lists into the dataframe
                        whole_dictionary = {'CAMIS': CAMIS
                                , 'DBA': DBA
                                , 'BORO': BORO
                                , 'Cusine_description': CUSINE_DESCRIPTION
                                , 'Inspection_date': INSPECTION_DATE
                                , 'Action': ACTION
                                , 'Voilation_code': VOILATION_CODE
                                , 'Voilation_description': VOILATION_DESCRIPTION
                                , 'Grade': GRADE
                                , 'Score': SCORE
                                , 'Inspection_type': INSPECTION_TYPE}
                        # convert dictionart into dataframe
                        df = pd.DataFrame(whole_dictionary)

                        search = combo2_for_search_by.get()
                        if search == "Violation Keyword":

                                        #Creating new window for graph
                                        window = Tk()
                                        window.title('Violation Keyword Plot')
                                        window.geometry("1150x650")

                                        # Size of figure
                                        fig = Figure(figsize=(10, 10), dpi=100)
                                        # lists for graph
                                        inspection_date = df["Inspection_date"]
                                        grade = df["Grade"]
                                        # adding the subplot
                                        bar = fig.add_subplot(111)
                                        # plotting the graph
                                        bar.bar(grade, inspection_date, width=0.5, color="cyan")
                                        bar.set_xlabel("Grade", c='Black')
                                        # bar.xticks(size = 4)
                                        bar.tick_params(axis='y', which='major', labelsize=5)

                                        bar.set_ylabel("Inspection Date", c="Black")
                                        bar.set_title("Inspection VS Grade", c='Black')
                                        

                                        #Canvas for Graph
                                        canvas = FigureCanvasTkAgg(fig, master=window)
                                        canvas.draw()
                                        # placing the canvas on the Tkinter window
                                        canvas.get_tk_widget().pack()
                                        # creating the Matplotlib toolbar
                                        toolbar = NavigationToolbar2Tk(canvas, window)
                                        toolbar.update()
                                      
                                        canvas.get_tk_widget().pack()
                                        #Run window
                                        window.mainloop() 
                        if search == "Restaurant Name":
                                        # the main Tkinter window
                                        window = Tk()
                                        # setting the title
                                        window.title('Restaurant name Plot')
                                        # dimensions of the main window
                                        window.geometry("1150x650")

                                        # the figure that will contain the plot
                                        fig = Figure(figsize=(10, 10), dpi=100)
                                        # lists
                                        inspection_date = df["Inspection_date"]
                                        grade = df["Grade"]
                                        # adding the subplot
                                        bar = fig.add_subplot(111)
                                        # plotting the graph
                                        bar.bar(grade, inspection_date, width=0.5, color="cyan")
                                        bar.set_xlabel("Grade", c='Black')
                                        # bar.xticks(size = 4)
                                        bar.tick_params(axis='y', which='major', labelsize=4)

                                        bar.set_ylabel("Inspection Date", c="Black")
                                        bar.set_title("Inspection VS Grade", c='Black')
                                        

                                        #Canvas for Graph
                                        canvas = FigureCanvasTkAgg(fig, master=window)
                                        canvas.draw()
                                        # placing the canvas on the Tkinter window
                                        canvas.get_tk_widget().pack()
                                        # creating the Matplotlib toolbar
                                        toolbar = NavigationToolbar2Tk(canvas, window)
                                        toolbar.update()
                                      
                                        canvas.get_tk_widget().pack()
                                        #Run window
                                        window.mainloop() 
                                        
                                        

                                        

                           

                except Exception as es:
                        messagebox.showerror("Error", f"Error Due To:  {str(es)}", parent=report_window)

        def graph_hist():
                record = []
                new = []
                
                # access data from treeview
                try:
                        for parent in Table.get_children():
                                for child in Table.item(parent)['values']:
                                        record.append(child)

                        start = 0
                        end = 11
                        RECORDS = int(len(record) / 11)

                        for i in range(RECORDS):
                                tuple_ = tuple(record[start:end])
                                new.append(tuple_)
                                start = start + 11
                                end = end + 12

                        # empty lists to store data from database
                        CAMIS = []
                        DBA = []
                        BORO = []
                        CUSINE_DESCRIPTION = []
                        INSPECTION_DATE = []
                        ACTION = []
                        VOILATION_CODE = []
                        VOILATION_DESCRIPTION = []
                        GRADE = []
                        SCORE = []
                        INSPECTION_TYPE = []

                        # append data into the empty lists
                        for record in new:
                                CAMIS.append(record[0])
                                DBA.append(record[1])
                                BORO.append(record[2])
                                CUSINE_DESCRIPTION.append(record[3])
                                INSPECTION_DATE.append(record[4])
                                ACTION.append(record[5])
                                VOILATION_CODE.append(record[6])
                                VOILATION_DESCRIPTION.append(record[7])
                                GRADE.append(record[8])
                                SCORE.append(record[9])
                                INSPECTION_TYPE.append(record[10])

                        # convert all lists into the dataframe
                        whole_dictionary = {'CAMIS': CAMIS
                                , 'DBA': DBA
                                , 'BORO': BORO
                                , 'Cusine_description': CUSINE_DESCRIPTION
                                , 'Inspection_date': INSPECTION_DATE
                                , 'Action': ACTION
                                , 'Voilation_code': VOILATION_CODE
                                , 'Voilation_description': VOILATION_DESCRIPTION
                                , 'Grade': GRADE
                                , 'Score': SCORE
                                , 'Inspection_type': INSPECTION_TYPE}
                        # convert dictionart into dataframe
                        df = pd.DataFrame(whole_dictionary)

                        search = combo2_for_search_by.get()
                        if search == "Violation Keyword":
                                        # the main Tkinter window
                                        window = Tk()
                                        # setting the title
                                        window.title('Violation Keyword Plot')
                                        # dimensions of the main window
                                        window.geometry("1150x650")

                                        # the figure that will contain the plot
                                        fig = Figure(figsize=(10, 10), dpi=100)
                                        # lists
                               
                                        grade = df["Grade"]
                                        # adding the subplot
                                    


                                        fig, Histo = plt.subplots(1, 1)

                                        Histo.hist(grade, bins=5,  color="red")
                                        Histo.set_title("histogram ")
      
                                        Histo.set_xlabel('grades')
                                        Histo.set_ylabel('no of restaurants')



                                        #Canvas for Graph
                                        canvas = FigureCanvasTkAgg(fig, master=window)
                                        canvas.draw()
                                        # placing the canvas on the Tkinter window
                                        canvas.get_tk_widget().pack()
                                        # creating the Matplotlib toolbar
                                        toolbar = NavigationToolbar2Tk(canvas, window)
                                        toolbar.update()
                                      
                                        canvas.get_tk_widget().pack()
                                        #Run window
                                        window.mainloop() 
                        if search == "Restaurant Name":
                                        # the main Tkinter window
                                        window = Tk()
                                        # setting the title
                                        window.title('Restaurant Name Plot')
                                        # dimensions of the main window
                                        window.geometry("1150x650")

                                        # the figure that will contain the plot
                                        fig = Figure(figsize=(10, 10), dpi=100)
                                        # lists
                                        inspection_date = df["Inspection_date"]
                                        grade = df["Grade"]
                                        # adding the subplot
                                        


                                        fig, Histo = plt.subplots(1, 1)

                                        Histo.hist(grade, bins=5,  color="red")
                                        Histo.set_title("histogram ")
      
                                        Histo.set_xlabel('grades')
                                        Histo.set_ylabel('no of restaurants')



                                        #Canvas for Graph
                                        canvas = FigureCanvasTkAgg(fig, master=window)
                                        canvas.draw()
                                        # placing the canvas on the Tkinter window
                                        canvas.get_tk_widget().pack()
                                        # creating the Matplotlib toolbar
                                        toolbar = NavigationToolbar2Tk(canvas, window)
                                        toolbar.update()
                                      
                                        canvas.get_tk_widget().pack()
                                        #Run window
                                        window.mainloop()               
                              
                                
                            
                 #Throw error if value is wrong or missing
                except Exception as es:
                        messagebox.showerror("Error", f"Error Due To:  {str(es)}", parent=report_window)


               #Function to refresh data table
        def clear():
                #Clear data from each user input section
                combo2_for_search_by.delete(0,END)
                SEARCH_ENTRY.delete(0,END)
   
                #SQL Query to grab all data 
                mycursor.execute("""SELECT CAMIS,DBA,BORO,CUISINEDESCRIPTION,INSPECTION_DATE,ACTIONS,VIOLATION_CODE,VIOLATION_DESCRIPTION,GRADE,SCORE,INSPECTION_TYPE FROM record LIMIT 100""")
                table_data = mycursor.fetchall()

                #Deletes all data currently in table
                Table.delete(*Table.get_children())

                #Loop iterates through each tables and places data.
                indexer = 1
                for value in table_data:
                        Table.insert("", 'end', text ="L"+str(indexer),values =(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]))
                        indexer +=1

        #Function to grab and display data for cleanest Restaurants
        def Cleanest_Restaurant():
              
                #Query Database present data of score listing in ascending order  
                mycursor.execute("""SELECT CAMIS,DBA,BORO,CUISINEDESCRIPTION,INSPECTION_DATE,ACTIONS,VIOLATION_CODE,VIOLATION_DESCRIPTION,GRADE,SCORE,INSPECTION_TYPE FROM record ORDER BY SCORE ASC;""") 
                table_data = mycursor.fetchall()
                  
                #Delete current data
                Table.delete(*Table.get_children())

                #For loop to place new query data
                indexer = 1
                for value in table_data:
                                Table.insert("", 'end', text ="L"+str(indexer),values =(value[9],value[8],value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[10]))
                                indexer +=1


        #Function to grab date values and query database
        def timelines():

                #Grab Start and End date strings
                Date1 = other.get()
                Date2 = other2.get()
                                     
                #Query Database with strings
                mycursor.execute("""SELECT CAMIS,DBA,BORO,CUISINEDESCRIPTION,INSPECTION_DATE,ACTIONS,VIOLATION_CODE,VIOLATION_DESCRIPTION,GRADE,SCORE,INSPECTION_TYPE FROM record WHERE INSPECTION_DATE BETWEEN (?) AND (?) ORDER BY INSPECTION_DATE ASC LIMIT 20;""",(Date1,Date2))
                table_data = mycursor.fetchall()
                #Grab Data and delete current table values
                Table.delete(*Table.get_children())
               
                #For loop inserts new data into table
                indexer = 1
                for value in table_data:
                                Table.insert("", 'end', text ="L"+str(indexer),values =(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]))
                                indexer +=1


        #Function to search database using keywords
        def FIND():
                #Grabs values from each input box
                search = combo2_for_search_by.get()
                search_place  =SEARCH_ENTRY.get()
              


                #Throws Error if values are missing
                if (search =="" or search_place==""):
                        messagebox.showerror("Please place a value in each of the boxes",parent=report_window)
                else:
                        if search == "Restaurant Name" :
                                try:
                                        #Query Database
                                        mycursor.execute("""SELECT CAMIS,DBA,BORO,CUISINEDESCRIPTION,INSPECTION_DATE,ACTIONS,VIOLATION_CODE,VIOLATION_DESCRIPTION,GRADE,SCORE,INSPECTION_TYPE FROM record WHERE DBA = '{}' ;""".format(search_place))
                                        table_data = mycursor.fetchall()
                                        
                                        #Fetch all data and delete current data in table 
                                        Table.delete(*Table.get_children())
                                      
                                        #Loop through each array and place data one by one in each cell
                                        indexer = 1
                                        for value in table_data:
                                                Table.insert("", 'end', text ="L"+str(indexer),values =(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]))
                                                indexer +=1

                                #Throw error if value is wrong or missing
                                except Exception as es:
                                        messagebox.showerror("Error",f"error due to:  {str(es)}",parent=report_window)


                        elif search == "Violation Keyword" :
                                try:
                                        #Query Database with keyword and use LIKE parameter to search for similar words in database.
                                        mycursor.execute("""SELECT CAMIS,DBA,BORO,CUISINEDESCRIPTION,INSPECTION_DATE,ACTIONS,VIOLATION_CODE,VIOLATION_DESCRIPTION,GRADE,SCORE,INSPECTION_TYPE FROM record WHERE VIOLATION_DESCRIPTION LIKE '%{}%' ;""".format(search_place))
                                        table_data = mycursor.fetchall()
                                       #Fetch all data and delete current data in table 
                                        Table.delete(*Table.get_children())
                                  
                                        #Loop through each array and place data one by one in each cell
                                        indexer = 1
                                        for value in table_data:
                                                Table.insert("", 'end', text ="L"+str(indexer),values =(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]))
                                                indexer +=1
                                
                                #Throw error if value is wrong or missing
                                except Exception as es:
                                        messagebox.showerror("Error",f"error due to:  {str(es)}",parent=report_window)


 
        
        # Function to change to report page
        def report():
                report_window.destroy()
                Exec()
                
        # Function to change to The Animal Violations Report page
        def animals():
                report_window.destroy()
                Animal_Violations()

        find = Button(report_window, anchor=CENTER,text="Search Keyword", bg="#6699cc",fg="black",font="Leelawadee 12", command=FIND)
        find.place(height=30,width=150,x=700,y=90)
        clear = Button(report_window, anchor=CENTER,text="Clear", bg="#6699cc",fg="black",font="Leelawadee 12", command=clear)
        clear.place(height=30,width=150,x=1060,y=60)

        find = Button(report_window, anchor=CENTER,text="Cleanest Restaurant", bg="#6699cc",fg="white",font="Leelawadee 12", command=Cleanest_Restaurant)
        find.place(height=50,width=150,x=50,y=160)

        find = Button(report_window, anchor=CENTER,text="Search Date", bg="#6699cc",fg="black",font="Leelawadee 12", command=timelines)
        find.place(height=30,width=120,x=175,y=110)

        button_bar_graph = Button(master = report_window, text="Bar Chart", bg="#6699cc",fg="white",font="Leelawadee 14", command=bar_graph)
        button_bar_graph.place(height=50,width=150,x=900,y=160)

        button_graph_hist = Button(report_window, text="Histogram", bg="#6699cc",fg="white",font="Leelawadee 14", command=graph_hist)
        button_graph_hist.place(height=50,width=150,x=1100,y=160)

        button_graph_hist = Button(report_window, text="Animal Violations", bg="#6699cc",fg="white",font="Leelawadee 14", command=animals)
        button_graph_hist.place(height=50,width=150,x=250,y=160)

   
        button_exec_report = Button(report_window, text="Exec Report", bg="#6699cc",fg="white",font="Leelawadee 14", command=report)
        button_exec_report.place(height=50,width=150,x=700,y=160)

        #Run Window
        
        report_window.mainloop()
        mydb.close()
        report_window.widthdraw()
report()

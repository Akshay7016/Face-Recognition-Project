from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import mysql.connector
import cv2 # contains more than 2500 algorithms



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x864+0+0")
        self.root.title("Student Details")

        #-------------------------------Variables-----------------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_searchCombo = StringVar()
        self.var_search_entry = StringVar()

        #Background Image
        img=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Background2.jpg")
        img=img.resize((1536,864), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimage)
        bg_img.place(x=0,y=0, width=1536, height=864)

        # Label
        frame = Frame(bg_img,borderwidth=5,relief=SOLID)
        frame.place(x=0,y=0,width=1531,height=100)

        title_label = Label(frame, text="STUDENT  MANAGEMENT",font=("times new roman", 35, "bold"),bg="lightyellow",fg="black")
        title_label.place(x=0,y=0,width=1520,height=90)

         # Time label
        def time():
            string = strftime('%H:%M:%S %p')
            time_label.config(text = string)
            time_label.after(1000,time)   #1000ms = 1 sec
        
        time_label = Label(title_label,font = ("times new roman",14,"bold"),background="white",fg="red")
        time_label.place(x=1410,y=67,width=110,height=20)
        time()


        #Main frame
        Main_frame = Frame(bg_img,bd=2,bg="White")
        Main_frame.place(x=11,y=115,width=1500,height=660)
        

        #Left side label frame
        Left_frame = LabelFrame(Main_frame,relief=RIDGE,bd=2,text="Student Information",font=("times new roman",18,"bold"),bg="white")
        Left_frame.place(x=20,y=15,width=720,height=620)

        #Current course information
        current_course_frame = LabelFrame(Left_frame,relief=RIDGE,bd=2,text="Current course information",font=("times new roman",15,"bold"),bg="white",fg="green")
        current_course_frame.place(x=20,y=20,width=672,height=150)

        #Department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=15,pady=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical","ENTC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=11,sticky=W)

        #Course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=3,padx=15,pady=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=4,padx=2,pady=11,sticky=W)

        #Year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=15,pady=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=11,sticky=W)


        #Semester
        course_label = Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=1,column=3,padx=15,pady=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Semester","Semester-1","Semester-2")
        course_combo.current(0)
        course_combo.grid(row=1,column=4,padx=2,pady=11,sticky=W)


        #Class Student information
        class_student_frame = LabelFrame(Left_frame,relief=RIDGE,bd=2,text="Class student information",font=("times new roman",15,"bold"),bg="white",fg="green")
        class_student_frame.place(x=20,y=185,width=672,height=385)

        #Student ID
        studentID_label = Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=12,pady=10,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12))
        studentId_entry.grid(row=0,column=1,padx=12,pady=10,sticky=W)

        #Student Name
        studentName_label = Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=12,pady=10,sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=12,pady=10,sticky=W)

        #Class Division
        class_div_label = Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=12,pady=10,sticky=W)

        division_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12),width=18,state="readonly")
        division_combo["values"]=("Select Division","A","B","C","D","E")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=12,pady=10,sticky=W)

        #Roll No
        RollNo_label = Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        RollNo_label.grid(row=1,column=2,padx=12,pady=10,sticky=W)

        RollNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12))
        RollNo_entry.grid(row=1,column=3,padx=12,pady=10,sticky=W)

         #Gender
        gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=12,pady=10,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=12,pady=10,sticky=W)

        #Date of Birth
        DOB_label = Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=12,pady=10,sticky=W)

        DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        DOB_entry.grid(row=2,column=3,padx=12,pady=10,sticky=W)

        #Email
        email_label = Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=12,pady=10,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12))
        email_entry.grid(row=3,column=1,padx=12,pady=10,sticky=W)

         #Phone Number
        phoneNo_label = Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phoneNo_label.grid(row=3,column=2,padx=12,pady=10,sticky=W)

        phoneNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        phoneNo_entry.grid(row=3,column=3,padx=12,pady=10,sticky=W)

        #Address
        address_label = Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=12,pady=10,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12))
        address_entry.grid(row=4,column=1,padx=12,pady=10,sticky=W)

        #Teacher Name
        teacher_name_label = Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=12,pady=10,sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12))
        teacher_name_entry.grid(row=4,column=3,padx=12,pady=10,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()  #Both values are stored in one variable

        radio1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radio1.grid(row=6,column=0,padx=12,pady=10,sticky=W)

        radio2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radio2.grid(row=6,column=1,padx=12,pady=10,sticky=W)

        #------------------------Last Button Frame------------------------------
        button_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=12,y=270,width=648,height=35)

        #Save Button
        save_button = Button(button_frame,command=self.add_data,text="Save",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

         #Update Button
        update_button = Button(button_frame,command=self.update_data,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

         #Delete Button
        delete_button = Button(button_frame,command=self.delete_data,text="Delete",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        #Reset Button
        reset_button = Button(button_frame,command=self.reset_data,text="Reset",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        #Frame for buttons
        photo_button_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        photo_button_frame.place(x=12,y=305,width=648,height=35)

        #Take a photo sample
        take_photo_button = Button(photo_button_frame,command=self.generate_dataset,text="Take photo",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0)

        #update a photo sample
        update_photo_button = Button(photo_button_frame,command=self.generate_dataset,text="Update photo",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_button.grid(row=0,column=1)


        #------------------------------------------------------------------------------------
        

        #Right side label frame
        Right_frame = LabelFrame(Main_frame,relief=RIDGE,bd=2,text="Student Details",font=("times new roman",18,"bold"),bg="white")
        Right_frame.place(x=770,y=15,width=700,height=620)

        #Right label image
        img_right=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\student_info.jpg")
        img_right=img_right.resize((720,152), Image.ANTIALIAS)
        self.photoimage_right = ImageTk.PhotoImage(img_right)

        
        right = Label(Right_frame, image=self.photoimage_right)
        right.place(x=15,y=15, width=655, height=152)


        #Search system
        search_frame = LabelFrame(Right_frame,relief=RIDGE,bd=2,text="Search System",font=("times new roman",15,"bold"),bg="white",fg="green")
        search_frame.place(x=20,y=185,width=655,height=90)

        searchBy_label = Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        searchBy_label.grid(row=0,column=0,padx=12,pady=10,sticky=W)

        #Combobox
        search_combo = ttk.Combobox(search_frame,textvariable=self.var_searchCombo,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Name","Roll","Phone","teacher")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=11,sticky=W)

        #Entry Field
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search_entry,width=15,font=("times new roman",12))
        search_entry.grid(row=0,column=2,padx=12,pady=10,sticky=W)

        #Search button
        search_button = Button(search_frame,text="Search",command=self.search_data,width=11,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=5)

        #Show all Button
        show_button = Button(search_frame,text="Show all",command=self.fetch_data,width=11,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_button.grid(row=0,column=4)

        #-------------------------Table Frame----------------------------------
        table_frame = Frame(Right_frame,relief=RIDGE,bd=2,bg="white")
        table_frame.place(x=20,y=290,width=655,height=280)

        #Scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # Give dummy name here
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #Show Header of table
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        #set column width of table
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)  #only get_cursor not to call
        self.fetch_data()

        
    #***************************Function Declaration**********************

    #***********Save Button****************
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) #show error message on same window
        else:
            try:
                #save data in MYSQL database
                conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                mycursor = conn.cursor()

                mycursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)                                                                                            


    #**************Fetch Data (show data in table frame)*************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
        mycursor = conn.cursor()
        mycursor.execute("Select * from student")

        data = mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #***************get_cursor Function***************
    #When we click on student entry then it will also opens in entry and combo boxes
    def get_cursor(self,event=""):  #event is a parameter
        #focus the cursor into student table
        cursor_focus = self.student_table.focus()
        #take that content into variable
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

        #Now Bind cursor with student_table(Binded above)

    #*************Update Button**************
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) #show error message on same window
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if update>0:     # Yes=1 or No=0
                    conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                    mycursor = conn.cursor()

                    mycursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_std_id.get()

                                                                                                                                                                                                            ))

                else:
                    if not update:  #if we click on NO option in messagebox
                        return

                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()

                #to fetch new updated data of database
                self.fetch_data()

                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{es}",parent=self.root)

    #****************Delete Function*****************
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student information",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                    mycursor = conn.cursor()
                    #sql query to delete data - 2nd way
                    sql_delete_query = "Delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql_delete_query,val)  # sql query works for val in which student id is stored
                
                else:
                    if not delete:
                        return
                    
                conn.commit()
                #to fetch new updated data of database
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{es}",parent=self.root)


    #****************Reset Function********************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #************************Search Data***************************************
    def search_data(self):
        if self.var_searchCombo.get()=="Select" or self.var_search_entry.get()=="":
                messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='akshay',database='face_recognizer')
                mycursor=conn.cursor()
                mycursor.execute("select * from student where " +str(self.var_searchCombo.get())+" LIKE '%"+str(self.var_search_entry.get())+"%'")
                rows=mycursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                else:
                    messagebox.showerror("Error","Data Not Found",parent=self.root)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   

    #**********************Generate Dataset(Take photo samples)********************
    def generate_dataset(self):
        #update function
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) #show error message on same window
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                mycursor = conn.cursor()
                mycursor.execute("Select * from student")
                myresult = mycursor.fetchall()

                id=0  # match these id with student id
                for x in myresult:
                    id+=1

                mycursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_std_id.get()==(id+1)

                                                                                                                                                                                                            ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #Now make cascade classifier object to detect faces
                #Load predefined data on face frontal from opencv

                # pyhton 3.7 -> open file location -> pyhton 3.7 -> open file location -> Lib -> site-packages -> cv2 -> data -> haarcascade_frontalface_default copy to project folder

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #These file is in current working folder so take only name
                #function to crop images
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor = 1.3
                    #Minimum Neighbour = 5

                    #Crop images by height and width
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]  #y+h and x+w will crop images
                        return face_cropped

                #Open Camera
                cap = cv2.VideoCapture(0)
                img_id=0   #For calculation purpose
                while True:
                    check , my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1   # img_id for counting 100 samples
                    
                        #resize image
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        #convert colour image to grayscale
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        # Now store faces in data folder with name as "user.1.1.jpg"
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)  # Saves image to specified location

                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    # Either using ENTER(13) or by taking 100 Samples stop taking images
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating dataset has been completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{es}",parent=self.root)







if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
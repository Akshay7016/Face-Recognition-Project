from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import mysql.connector
import cv2 # contains more than 2500 algorithms
import os # for opening CSV file
import csv
from tkinter import filedialog 
from datetime import datetime
from time import strftime

mydata = []  # Global variable for storing all Excel sheet data



class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x864+0+0")
        self.root.title("Attendance Record")

        # Variables
        self.var_attendance_id = StringVar()
        self.var_attendance_roll = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_dep = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_status = StringVar()
        self.var_attendance_lecture = StringVar()

        #variables for Subject and Time
        self.var_lecture = StringVar()
        self.var_time = StringVar()

        #Background Image
        img=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Background2.jpg")
        img=img.resize((1536,864), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimage)
        bg_img.place(x=0,y=0, width=1536, height=864)

        # Label
        frame = Frame(bg_img,borderwidth=5,relief=SOLID)
        frame.place(x=0,y=0,width=1531,height=100)

        title_label = Label(frame, text="Attendance Record",font=("times new roman", 35, "bold"),bg="lightyellow",fg="black")
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
        Left_frame = LabelFrame(Main_frame,relief=RIDGE,bd=2,text="Attendance Details",font=("times new roman",18,"bold"),bg="white")
        Left_frame.place(x=20,y=15,width=680,height=620)

        # Left upper inside frame
        left_upper_inside_frame = LabelFrame(Left_frame,relief=RIDGE,bd=2,font=("times new roman",15,"bold"),bg="white",fg="green")
        left_upper_inside_frame.place(x=15,y=20,width=645,height=120)

        #Lecture Combobox
        lecture_label = Label(left_upper_inside_frame,text="Subject:",font=("times new roman",13,"bold"),bg="white")
        lecture_label.grid(row=0,column=0,padx=12,pady=20,sticky=W)
        
        lecture_combo = ttk.Combobox(left_upper_inside_frame,textvariable=self.var_lecture,font=("times new roman",12),width=14,state="readonly")
        lecture_combo["values"]=("Select subject","Math","Science","Geography")
        lecture_combo.current(0)
        lecture_combo.grid(row=0,column=1,padx=12,pady=20,sticky=W)

        #Timing Combobox
        lect_time_label = Label(left_upper_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        lect_time_label.grid(row=1,column=0,padx=12,pady=6,sticky=W)
        
        lect_time_combo = ttk.Combobox(left_upper_inside_frame,textvariable=self.var_time,font=("times new roman",12),width=14,state="readonly")
        lect_time_combo["values"]=("Select time","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:30-3:30","3:30-4:30")
        lect_time_combo.current(0)
        lect_time_combo.grid(row=1,column=1,padx=12,pady=6,sticky=W)
        
        #face Recognize Button
        face_recog_button = Button(left_upper_inside_frame,text="Recognize Face",command=self.face_recog,width=16,font=("times new roman",16,"bold"),bg="blue",fg="white")
        face_recog_button.place(x=300,y=32,width=200,height=50)

        

        #**************************************************************************

        # Left bottom inside frame
        left_inside_frame = LabelFrame(Left_frame,relief=RIDGE,bd=2,font=("times new roman",15,"bold"),bg="white",fg="green")
        left_inside_frame.place(x=15,y=180,width=645,height=395)

        # Labels and Entries

        #Attendace ID
        attendance_id_label = Label(left_inside_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=12,pady=10,sticky=W)

        attendance_id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_id,width=16,font=("times new roman",12))
        attendance_id_entry.grid(row=0,column=1,padx=12,pady=10,sticky=W)

        #Roll Number
        attendance_roll_label = Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        attendance_roll_label.grid(row=0,column=2,padx=12,pady=10,sticky=W)

        attendance_roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_roll,width=16,font=("times new roman",12))
        attendance_roll_entry.grid(row=0,column=3,padx=12,pady=10,sticky=W)

        #Name
        attendance_name_label = Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        attendance_name_label.grid(row=1,column=0,padx=12,pady=10,sticky=W)

        attendance_name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_name,width=16,font=("times new roman",12))
        attendance_name_entry.grid(row=1,column=1,padx=12,pady=10,sticky=W)

        #Department
        attendance_dept_label = Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        attendance_dept_label.grid(row=1,column=2,padx=12,pady=10,sticky=W)

        attendance_dept_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_dep,width=16,font=("times new roman",12))
        attendance_dept_entry.grid(row=1,column=3,padx=12,pady=10,sticky=W)

        #Time
        attendance_time_label = Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        attendance_time_label.grid(row=2,column=0,padx=12,pady=10,sticky=W)

        attendance_time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_time,width=16,font=("times new roman",12))
        attendance_time_entry.grid(row=2,column=1,padx=12,pady=10,sticky=W)

        #Date
        attendance_date_label = Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        attendance_date_label.grid(row=2,column=2,padx=12,pady=10,sticky=W)

        attendance_date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_date,width=16,font=("times new roman",12))
        attendance_date_entry.grid(row=2,column=3,padx=12,pady=10,sticky=W)

        #Subject
        subject_label = Label(left_inside_frame,text="Subject:",font=("times new roman",13,"bold"),bg="white")
        subject_label.grid(row=3,column=0,padx=12,pady=10,sticky=W)

        subject_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attendance_lecture,width=16,font=("times new roman",12))
        subject_entry.grid(row=3,column=1,padx=12,pady=10,sticky=W)

        #Attendance
        attendance_label = Label(left_inside_frame,text="Attendance status:",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=3,column=2,padx=12,pady=10,sticky=W)

        attendance_status_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_attendance_status,font=("times new roman",12),width=14,state="readonly")
        attendance_status_combo["values"]=("Status","Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3,column=3,padx=12,pady=10,sticky=W)

        #Last Button Frame
        button_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=12,y=330,width=612,height=35)

        #Import CSV Button
        save_button = Button(button_frame,text="Import CSV",command=self.importCSV,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        #Export CSV Button
        update_button = Button(button_frame,text="Export CSV",command=self.exportCSV,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

         #Update Button
        delete_button = Button(button_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        #Delete Button
        delete_button = Button(button_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=3)


        #************************************************************************

        #Right side label frame
        Right_frame = LabelFrame(Main_frame,relief=RIDGE,bd=2,text="Student Attendance Record",font=("times new roman",18,"bold"),bg="white")
        Right_frame.place(x=730,y=15,width=740,height=620)

        #def search_system():
            # #Search system
            # search_frame = LabelFrame(Right_frame,relief=RIDGE,bd=2,text="Search System",font=("times new roman",15,"bold"),bg="white",fg="green")
            # search_frame.place(x=20,y=10,width=655,height=130)

            # searchBy_label = Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
            # searchBy_label.grid(row=0,column=0,padx=12,pady=10,sticky=W)

            # #Get Date
            # self.var_getDate = StringVar()

            # date_label = Label(search_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
            # date_label.grid(row=0,column=1,padx=5,pady=10,sticky=W)

            # date_entry = ttk.Entry(search_frame,textVariable = self.var_getDate,width=16,font=("times new roman",12))
            # date_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)


            # #Combobox

            # self.var_searchCombo = StringVar()

            # search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),textVariable=self.var_searchCombo,width=15,state="readonly")
            # search_combo["values"]=("Select","Subject","Time","Roll")
            # search_combo.current(0)
            # search_combo.grid(row=0,column=3,padx=20,pady=11,sticky=W)

            # #Entry Field
            # search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",12))
            # search_entry.grid(row=0,column=4,pady=10,sticky=W)

            # #Search button
            # search_button = Button(search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
            # search_button.grid(row=1,column=2,padx=5,pady=5)

            # #Show all Button
            # show_button = Button(search_frame,text="Show all",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
            # show_button.grid(row=1,column=3)

        #Table Frame
        table_frame = Frame(Right_frame,relief=RIDGE,bd=2,bg="white")
        table_frame.place(x=17,y=20,width=700,height=555)

        #Scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # Give dummy name here
        self.attendance_Table_Report = ttk.Treeview(table_frame,column=("att_id","roll","name","department","time","date","sub","attendance","stud_id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendance_Table_Report.xview)
        scroll_y.config(command=self.attendance_Table_Report.yview)

        #Show Header of table
        self.attendance_Table_Report.heading("att_id",text="Attendance ID")
        self.attendance_Table_Report.heading("roll",text="Roll")
        self.attendance_Table_Report.heading("name",text="Name")
        self.attendance_Table_Report.heading("department",text="Department")
        self.attendance_Table_Report.heading("time",text="Time")
        self.attendance_Table_Report.heading("date",text="Date")
        self.attendance_Table_Report.heading("sub",text="Subject")
        self.attendance_Table_Report.heading("attendance",text="Attendance")
        self.attendance_Table_Report.heading("stud_id",text="Student ID")
        self.attendance_Table_Report["show"]="headings"

        #set column width of table
        self.attendance_Table_Report.column("att_id",width=90)
        self.attendance_Table_Report.column("roll",width=50)
        self.attendance_Table_Report.column("name",width=120)
        self.attendance_Table_Report.column("department",width=80)
        self.attendance_Table_Report.column("time",width=85)
        self.attendance_Table_Report.column("date",width=85)
        self.attendance_Table_Report.column("sub",width=85)
        self.attendance_Table_Report.column("attendance",width=85)
        self.attendance_Table_Report.column("stud_id",width=100)


        
        self.attendance_Table_Report.pack(fill=BOTH,expand=1)

        self.attendance_Table_Report.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #********************Fetch Data******************************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
        mycursor = conn.cursor()
        mycursor.execute("Select * from attendance")

        data = mycursor.fetchall()

        if len(data)!=0:
            self.attendance_Table_Report.delete(*self.attendance_Table_Report.get_children())
            for i in data:
                self.attendance_Table_Report.insert("",END,values=i)
            conn.commit()
        conn.close()

    #**********************get cursor***********************************
    def get_cursor(self,event=""):   # Bind given function with table
        cursor_row = self.attendance_Table_Report.focus()
        content=self.attendance_Table_Report.item(cursor_row)
        rows = content['values']
        self.var_attendance_id.set(rows[0])
        self.var_attendance_roll.set(rows[1])
        self.var_attendance_name.set(rows[2])
        self.var_attendance_dep.set(rows[3])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_lecture.set(rows[6])
        self.var_attendance_status.set(rows[7])

    #******************Import CSV file*********************
    def importCSV(self):
        global mydata
        mydata.clear()
        fileName = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv file",filetypes=(("csv file","*.csv"),("All File","*.*")),parent = self.root)
        with open(fileName) as myFile:
            csvRead = csv.reader(myFile,delimiter=",")
            for i in csvRead:
                mydata.append(i)
            
            self.fetch_data(mydata)

    
    #******************Export CSV file*********************
    def exportCSV(self):
        # Check whether data present in attendance_Table_Report or not
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to Export!!!",parent=self.root)
                return False
            
            fileName = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv file",filetypes=(("csv file","*.csv"),("All File","*.*")),parent = self.root)
            with open(fileName,mode="w",newline="") as myFile:
                export_write = csv.writer(myFile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export","Data successfully exported to "+os.path.basename(fileName))
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{es}",parent=self.root)

    

    #**************************Update Function**********************
    def update_data(self):
        try:
            update = messagebox.askyesno("Update","Do you want to update student attendance record?",parent=self.root)
            if update>0:     # Yes=1 or No=0
                conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                mycursor = conn.cursor()

                mycursor.execute("Update attendance set Time=%s,Date=%s,Subject=%s,Status=%s where Attendance_id=%s",(

                                                                                                                      self.var_attendance_time.get(),
                                                                                                                      self.var_attendance_date.get(),
                                                                                                                      self.var_attendance_lecture.get(),
                                                                                                                      self.var_attendance_status.get(),
                                                                                                                                                                            
                                                                                                                      self.var_attendance_id.get()

                                                                                                                                              ))

            else:
                if not update:  #if we click on NO option in messagebox
                    return

            messagebox.showinfo("Success","Student attendance successfully updated",parent=self.root)
            conn.commit()

            #to fetch new updated data of database
            self.fetch_data()

            conn.close()

        except Exception as es:
            messagebox.showerror("Error",f"Due to:{es}")
    


    #*****************Delete Function****************************
    def delete_data(self):
        try:
            delete = messagebox.askyesno("Delete Record","Do you want to delete this student attendance",parent=self.root)
            if delete>0:
                conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                mycursor = conn.cursor()
                #sql query to delete data - 2nd way
                sql_delete_query = "Delete from attendance where Attendance_id=%s"
                val=(self.var_attendance_id.get(),)
                mycursor.execute(sql_delete_query,val)  # sql query works for val in which student id is stored
                
            else:
                if not delete:
                    return
                    
            conn.commit()
            #to fetch new updated data of database
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Delete","Successfully deleted student attendance",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error",f"Due to:{es}",parent=self.root)

    #__________________________________________________________________________
    #__________________________________________________________________________
    #__________________________________________________________________________
    #__________________________________________________________________________

    def mark_attendance(self,i,r,n,d,t,lec):
        with open("class_Attendance.csv","r+",newline="\n") as f:
                myDataList = f.readlines()
                name_List=[]

                for line in myDataList:
                    entry = line.split(",")
                    name_List.append(entry[0])
            
                # marks attendance of student only once, Not Repeat
                if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List) and (lec not in name_List)):
                    now = datetime.now()
                    d1=now.strftime("%d/%m/%Y") # day-month-year
                    # dtString = now.strftime("%H:%M:%S") # Hour-Minute-Second
                    f.writelines(f"{r},{n},{d},{t},{d1},{lec},Present,{i}\n")

    # def mark_attendance(self,i,r,n,d):
    #     now=datetime.now()
    #     time1=now.strftime("%Y-%m-%d %H:%M:%S")
    #     print(time1)
    #     try:
    #         conn=mysql.connector.connect(host='localhost',username='root',password='akshay',database='face_recognizer')
    #         my_cursor=conn.cursor()
    #         my_cursor.execute("select Date from attendance_mysql where Roll LIKE '%"+r+"%'")
    #         rows=my_cursor.fetchone()
    #         if (rows==None):
    #             my_cursor.execute("insert into attendance_mysql values(%s,%s,%s,%s,%s,%s)",(i,r,n,d,time1,"Present"))
    #             conn.commit()
    #         else:
    #             #create_time=datetime.strftime("%Y-%m-%d %H:%M:%S")
    #             diff=((datetime.strptime(time1,'%Y-%m-%d %H:%M:%S'))-(datetime.strptime(rows[0],'%Y-%m-%d %H:%M:%S'))).total_seconds()
    #             print(diff)
    #             diff1=diff/60
    #             print(diff1)
    #             if(diff1>2):
    #                 my_cursor.execute("update attendance_mysql set Date=%s where Student_id=%s",(time1,i))
    #             conn.commit()
    #         conn.close()
    #     except Exception as es:
    #         messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                


    #*****************************Face Recognition*****************************
    def face_recog(self):
        current_lecture = self.var_lecture.get()
        current_time = self.var_time.get()

        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coordinates = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                # Predict image
                id,predict = clf.predict(gray_image[y:y+h,x:x+w]) # which rectangle wnat to predict
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                mycursor = conn.cursor()

                # For showing Name
                mycursor.execute("Select Name from student where Student_id="+str(id))
                n = mycursor.fetchone()  # because we want fetch only Name
                n = "+".join(n)

                # For showing Roll no
                mycursor.execute("Select Roll from student where Student_id="+str(id))
                r = mycursor.fetchone()  # because we want fetch only Name
                r = "+".join(r)

                # For showing Department
                mycursor.execute("Select Dep from student where Student_id="+str(id))
                d = mycursor.fetchone()  # because we want fetch only Name
                d = "+".join(d)

                mycursor.execute("Select Student_id from student where Student_id="+str(id))
                i = mycursor.fetchone()  # because we want fetch only Name
                i = "+".join(i)

                if confidence>77:
                    # Show name and id of recognized image
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d,current_time,current_lecture)

                else: # If no face matches
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coordinates = [x,y,w,h]

            return coordinates

        def recognize(img,clf,faceCascade):
            coordinates = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        # Store harcascade frontal face into file
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        # Read classsifier which we write in train.py
        clf.read("classifier.xml")

        # Open camera
        video_cap = cv2.VideoCapture(0)
        while True:
            check,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                video_cap.release()
                cv2.destroyAllWindows()

                # storing data to Mysql
                conn = mysql.connector.connect(host="localhost", username="root",password="akshay",database="face_recognizer")
                mycursor = conn.cursor()
                with open("class_Attendance.csv",'r') as f:
                    csv_data = csv.reader(f)
                    for row in csv_data:
                        mycursor.execute("Insert into attendance(Roll,Name,Department,Time,Date,Subject,Status,Student_id) values(%s,%s,%s,%s,%s,%s,%s,%s)",row)

                conn.commit()
                conn.close()

                # Opening the file with w+ mode truncates the file
                filename = "class_Attendance.csv"
                f = open(filename,"w+")
                f.close()

                break



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
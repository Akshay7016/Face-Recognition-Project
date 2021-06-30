from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os # To access photos from Directory
from time import strftime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x864+0+0")
        self.root.title("Face Recognition System")

        #Background Image
        img=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Background2.jpg")
        img=img.resize((1536,864), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        
        bg_img = Label(self.root, image=self.photoimage)
        bg_img.place(x=0,y=0, width=1536, height=864)

        # Label
        frame = Frame(bg_img,borderwidth=5,relief=SOLID)
        frame.place(x=0,y=0,width=1531,height=100)

        title_label = Label(frame, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("times new roman", 35, "bold"),bg="SteelBlue",fg="black")
        title_label.place(x=0,y=0,width=1520,height=90)


        # Time label
        def time():
            string = strftime('%H:%M:%S %p')
            time_label.config(text = string)
            time_label.after(1000,time)   #1000ms = 1 sec
        
        time_label = Label(title_label,font = ("times new roman",14,"bold"),background="white",fg="red")
        time_label.place(x=1410,y=67,width=110,height=20)
        time()

        #Student Button
        img1=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\student_details.jpg")
        img1=img1.resize((200,200), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        frame1 = Frame(bg_img,bg="grey",borderwidth=5)
        frame1.place(x=160,y=160,width=208,height=248)

        b1=Button(frame1,image=self.photoimage1,command=self.student_details,cursor="hand2")
        b1.place(x=0, y=0, width=200, height=200)

        b1_1=Button(frame1,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b1_1.place(x=0, y=200, width=200, height=40)


        #Detect Face Button
        img2=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Face_Detect.jpeg")
        img2=img2.resize((200,200), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        frame2 = Frame(bg_img,bg="grey",borderwidth=5)
        frame2.place(x=490,y=160,width=208,height=248)

        b2=Button(frame2,image=self.photoimage2,command=self.Face_Detect,cursor="hand2")
        b2.place(x=0, y=0, width=200, height=200)

        b2_1=Button(frame2,text="Face Detector",command=self.Face_Detect,cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b2_1.place(x=0, y=200, width=200, height=40)


        #Attendance Record Button
        img3=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Attendace_icon.jpeg")
        img3=img3.resize((200,200), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        frame3 = Frame(bg_img,bg="grey",borderwidth=5)
        frame3.place(x=820,y=160,width=208,height=248)

        b3=Button(frame3,image=self.photoimage3,command=self.attendance_data,cursor="hand2")
        b3.place(x=0, y=0, width=200, height=200)

        b3_1=Button(frame3,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b3_1.place(x=0, y=200, width=200, height=40)


        #Train data Button
        img4=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\train_Data.jpg")
        img4=img4.resize((200,200), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        frame4 = Frame(bg_img,bg="grey",borderwidth=5)
        frame4.place(x=1150,y=160,width=208,height=248)

        b4=Button(frame4,image=self.photoimage4,command=self.train_Data,cursor="hand2")
        b4.place(x=0, y=0, width=200, height=200)

        b4_1=Button(frame4,text="Train Data",cursor="hand2",command=self.train_Data,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b4_1.place(x=0, y=200, width=200, height=40)


        #Student photos Button
        img5=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Student_Photos.jpg")
        img5=img5.resize((200,200), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        frame5 = Frame(bg_img,bg="grey",borderwidth=5)
        frame5.place(x=160,y=470,width=208,height=248)

        b5=Button(frame5,image=self.photoimage5,command=self.open_images,cursor="hand2")
        b5.place(x=0, y=0, width=200, height=200)

        b5_1=Button(frame5,text="Photos",cursor="hand2",command=self.open_images,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b5_1.place(x=0, y=200, width=200, height=40)


        #Developer info Button
        img6=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Developer.jpg")
        img6=img6.resize((200,200), Image.ANTIALIAS)
        self.photoimage6 = ImageTk.PhotoImage(img6)

        frame6 = Frame(bg_img,bg="grey",borderwidth=5)
        frame6.place(x=490,y=470,width=208,height=248)

        b6=Button(frame6,image=self.photoimage6,cursor="hand2")
        b6.place(x=0, y=0, width=200, height=200)

        b6_1=Button(frame6,text="Developers",cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b6_1.place(x=0, y=200, width=200, height=40)


        #Help Desk Button
        img7=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Help_desk.jpg")
        img7=img7.resize((200,200), Image.ANTIALIAS)
        self.photoimage7 = ImageTk.PhotoImage(img7)

        frame7 = Frame(bg_img,bg="grey",borderwidth=5)
        frame7.place(x=820,y=470,width=208,height=248)

        b7=Button(frame7,image=self.photoimage7,cursor="hand2")
        b7.place(x=0, y=0, width=200, height=200)

        b7_1=Button(frame7,text="Help Desk",cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b7_1.place(x=0, y=200, width=200, height=40)


         #Quit Button
        img8=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\exit.jpg")
        img8=img8.resize((200,200), Image.ANTIALIAS)
        self.photoimage8 = ImageTk.PhotoImage(img8)

        frame8 = Frame(bg_img,bg="grey",borderwidth=5)
        frame8.place(x=1150,y=470,width=208,height=248)

        b8=Button(frame8,image=self.photoimage8,command=self.exit_project,cursor="hand2")
        b8.place(x=0, y=0, width=200, height=200)

        b8_1=Button(frame8,text="Quit",cursor="hand2",command=self.exit_project,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b8_1.place(x=0, y=200, width=200, height=40)

    def open_images(self):
        os.startfile("data")  #Folder name


    #**************************Buttons function***************************************

    def student_details(self):
        self.new_window=Toplevel(self.root)   #place student details window above root window
        self.app=Student(self.new_window)     #To declare class

    #**************************Train Photos Button***************************************
    def train_Data(self):
        self.new_window=Toplevel(self.root)   #place Train photos window above root window
        self.app=Train(self.new_window)     #To declare class

    #*************************Face Recognize Button*******************************************
    def Face_Detect(self):
        self.new_window=Toplevel(self.root)   
        self.app=Face_Recognition(self.new_window)

    #***********************Attendance Record Button**************************************
    def attendance_data(self):
        self.new_window=Toplevel(self.root)   
        self.app=Attendance(self.new_window)

    #***********************EXIT Button*********************************
    def exit_project(self):
        self.exit_project = tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.exit_project > 0:
            self.root.destroy()
        else:
            return









if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import mysql.connector
import cv2 # contains more than 2500 algorithms
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x864+0+0")
        self.root.title("Train data")


        #Background Image
        img=Image.open(r"C:\Users\Akshay\Desktop\Face_Recognition_System\Images\Background2.jpg")
        img=img.resize((1536,864), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimage)
        bg_img.place(x=0,y=0, width=1536, height=864)

        # Label
        frame = Frame(bg_img,borderwidth=5,relief=SOLID)
        frame.place(x=0,y=0,width=1531,height=100)

        title_label = Label(frame, text="Train Dataset",font=("times new roman", 35, "bold"),bg="lightyellow",fg="red")
        title_label.place(x=0,y=0,width=1520,height=90)

         # Time label
        def time():
            string = strftime('%H:%M:%S %p')
            time_label.config(text = string)
            time_label.after(1000,time)   #1000ms = 1 sec
        
        time_label = Label(title_label,font = ("times new roman",14,"bold"),background="white",fg="red")
        time_label.place(x=1410,y=67,width=110,height=20)
        time()

        #Button
        my_Button=Button(bg_img,text="Train data",command=self.train_classifier,cursor="hand2",font=("times new roman", 15, "bold"),bg="Black",fg="white")
        my_Button.place(x=630, y=400, width=300, height=40)


    def train_classifier(self):
        data_dir = ("data")  # Working directory so only folder name
        #We give path in List and use List Comprehension
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale image

            # For Grid X and Grid Y we need Numpy Array
            image_np = np.array(img,'uint8')  # uint8 = Array datatype
            image_id = int(os.path.split(image)[1].split('.')[1])
            # C:\Users\Akshay\Desktop\Face_Recognition_System\data\user.1.1.jpg
            # 0----------------------------------------------------1 
            # ----------------------------------------------------------1  

            faces.append(image_np)  
            ids.append(image_id) 
            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13

        # convert ids to Numpy array
        ids = np.array(ids)

        #-------------Train the classifier And save--------------------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)

        # Store trained data to file
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!!!")



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
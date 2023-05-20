from tkinter import *

from PIL import Image, ImageTk
from PIL import Image
from student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Developer:
    def __init__(self, root):

         self.root = root
         self.root.geometry("1450x820+0+0")
         self.root.title("Face Recognition System")

         title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 30, "bold"), bg="white", fg="Red")
         title_lbl.place(x=0, y=0, width=1530, height=45)

         img_top = Image.open(r"C:\Users\admin\OneDrive\Pictures\devlp.PNG")
         img_top = img_top.resize((1530, 720),
                             Image.ANTIALIAS)  # Antialias lea high level image lai low level mah convert garxa
         self.photoimg_top = ImageTk.PhotoImage(img_top)

         f_lbl = Label(self.root, image=self.photoimg_top)
         f_lbl.place(x=0, y=55, width=1530, height=720)

         dev_label = Label(f_lbl, text="Vanshika Barange(vanshikabarange08@gmail.com)", font=("times new roman",14, "bold"),
                           fg="blue")
         dev_label.place(x=950, y=150)

         dev_label = Label(f_lbl, text="Shivani Bhagat(Shivanibhagat1701@gmail.com)",
                           font=("times new roman", 14, "bold"),
                           fg="blue")
         dev_label.place(x=950, y=200)

         dev_label = Label(f_lbl, text="Manisha Dadhore(dhadoremanisha@gmail.com)",
                           font=("times new roman", 14, "bold"),
                           fg="blue")
         dev_label.place(x=950, y=250)

         dev_label = Label(f_lbl, text="Kirti Ghidode(kirtighidode@gmail.com)",
                           font=("times new roman", 14, "bold"),
                           fg="blue")
         dev_label.place(x=950, y=300)






if __name__ == "__main__":
    root = Tk()
    obj =  Developer(root)
    root.mainloop()

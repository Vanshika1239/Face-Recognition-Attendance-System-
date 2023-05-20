from tkinter import *

from PIL import Image, ImageTk
from PIL import Image
from student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Helpdeck:
    def __init__(self, root):

         self.root = root
         self.root.geometry("1450x820+0+0")
         self.root.title("Face Recognition System")
if __name__ == "__main__":
    root = Tk()
    obj =  Helpdeck(root)
    root.mainloop()



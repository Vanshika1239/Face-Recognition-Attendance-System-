from logging import root
from os import close, path
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import os
import numpy as np
import cv2
from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import pyttsx3
# mera
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()
    #end



class Train:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recognition System")


         title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="Red")
         title_lbl.place(x=0, y=0, width=1530,height=45)

         img_top=Image.open(r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\scan.PNG")
         img_top=img_top.resize((1530,325),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
         self.photoimg_top=ImageTk.PhotoImage(img_top)

         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0, y=55,width=1530,height=325)

#         # Button....................

         btn1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn1.place(x=0, y=380, width=1530, height=60)


         img_bottom=Image.open(r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\scan.PNG")
         img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

         f_lbl=Label(self.root,image=self.photoimg_bottom)
         f_lbl.place(x=0, y=440,width=1530,height=325)


    def train_classifier(self):
          data_dir=("data")
          path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

          faces=[]
          ids=[]


          for image in path:
              img= Image.open(image).convert('L')

              imageNp=np.array(img,'uint8')
              id =int(os.path.split(image)[1].split('.')[1])
              faces.append(imageNp)
              ids.append(id)
              cv2.imshow("Training",imageNp)
              cv2.waitKey(1)==13
          ids=np.array(ids)
#     #         # ....................Train classifier....

          clf=cv2.face.LBPHFaceRecognizer_create()
          clf.train(faces,ids)
          clf.Write("classifier.xml")
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Training dataset completed")
    def train_classifier(self):
         data_dir=("data")
         path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

         faces=[]
         ids=[]

         for image in path:
             img=Image.open(image).convert('L')  # grAY SCALE image
             imageNp=np.array(img,'uint8')
             id=int(os.path.split(image)[1].split('.')[1])
             faces.append(imageNp)
             ids.append(id)
             cv2.imshow("Training",imageNp)
             cv2.waitKey(1)==13
         ids=np.array(ids)

        # Train the classifier and save
         clf=cv2.face.LBPHFaceRecognizer_create()
         clf.train(faces,ids)
         clf.write("classifier.xml")
         cv2.destroyAllWindows()
         speak_va(' Training datasets completed ! ')
         messagebox.showinfo("Result","Training datasets completed !")

if __name__=="__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()
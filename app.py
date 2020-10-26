



#All the required librarires are place here 




from tkinter import *
import pythoncom
from tkinter.ttk import Combobox
import tkinter.messagebox
from gtts import gTTS
from time import sleep
import threading
import os
from textblob import TextBlob
import pyglet
from PyDictionary import *
from playsound import playsound
import win32com.client
from multiprocessing import Process









class Translate:
    def __init__(self,root):
        self.root=root
        self.root.title("Spelling Checker")
        self.root.geometry("500x505")
        self.root.resizable(0,0)
        self.root.iconbitmap("logo419.ico")



        
        
        to_TRANS_lan=StringVar()
        select=StringVar()
        TRANSl=StringVar()







        
        def on_enter1(e):
            but_check['background']="black"
            but_check['foreground']="cyan"
  
        def on_leave1(e):
            but_check['background']="SystemButtonFace"
            but_check['foreground']="SystemButtonText"


        def on_enter2(e):
            but_listen['background']="black"
            but_listen['foreground']="cyan"
  
        def on_leave2(e):
            but_listen['background']="SystemButtonFace"
            but_listen['foreground']="SystemButtonText"

        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"






        def clear():
            texttopaste1.delete('1.0',END)
            texttopaste.delete('1.0',END)


        def checks():
            try:
                texttopaste1.delete('1.0',END)              
                get_text=texttopaste.get("1.0","end")
                convert_text=TextBlob(get_text)
                texttopaste1.insert(1.0,convert_text.correct())
            except Exception as e:
                print(e)
                


        def thread_trans():
            t1=threading.Thread(target=checks)
            t1.start()


        """ online"""
        """
        def speak():
            try:
                
                texts=texttopaste1.get("1.0","end")
                tts = gTTS(text=texts)
                filename = 'C:\\TEMP\\speeling.mp3'
                tts.save(filename)
                playsound('C:\\TEMP\\speeling.mp3')
                os.remove(filename) #remove temperory file                
            except Exception as e:
                print(e)
        """


        def offline():
            try:
                pythoncom.CoInitialize()
                speaker=win32com.client.Dispatch("SAPI.spVoice")
                sp=texttopaste1.get("1.0","end")
                speaker.Speak(sp)
            except Exception as e:
                print(e)
                tkinter.messagebox.showerror("Error","No text written here")




        def thread_speak():
            t1=threading.Thread(target=offline)
            t1.start()
            

            #music = pyglet.media.load(filename, streaming=False)
            #music.play()

            #pyglet.app.run()

            #sleep(4)

            #music.pause()

            #print(player.time())
            #sleep(music.duration) #prevent from killing
            




        

#===================================================#
        
        Mainframe=LabelFrame(height=505,width=500,bd=3,text="Speeling Checker")
        Mainframe.place(x=1,y=0)

        frame1=Frame(Mainframe,width=493,height=200,bg="yellow")
        frame1.place(x=0,y=0)

        frame2=Frame(Mainframe,width=493,height=100,relief="ridge",bd=4,bg="cyan")
        frame2.place(x=0,y=202)

        frame3=Frame(Mainframe,width=493,height=180,bg="red")
        frame3.place(x=0,y=303)

#=========================================text/frame1=======================#
        Scol=Scrollbar(frame1,orient="vertical")
        Scol.grid(column=10,sticky="NS")
        
        texttopaste=Text(frame1,height=10,width=59,font=('times new roman',12,'bold'),yscrollcommand=Scol.set)
        texttopaste.grid(row=0,column=0)
        Scol.config(command=texttopaste.yview)


#-----------------------------------------------------------------
        but_check=Button(frame2,text="Check",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=thread_trans)
        but_check.place(x=25,y=25)
        but_check.bind("<Enter>",on_enter1)
        but_check.bind("<Leave>",on_leave1)


        but_listen=Button(frame2,text="Listen",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=thread_speak)
        but_listen.place(x=180,y=25)
        but_listen.bind("<Enter>",on_enter2)
        but_listen.bind("<Leave>",on_leave2)

        but_clear=Button(frame2,text="Clear",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=clear)
        but_clear.place(x=335,y=25)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)


        

        """
        Lang_list=["en","hi","ur","te","la","iw","kn","af","sq","am","ar","hy","az","eu","basque","be","bn","bs","bg","ca","ceb","ny","zh-cn","zh-tw","co","hr","cs","da","mr","nl","fr","ja","pt","ko","ru"]
        Lang_list_combo=Combobox(frame2,values=Lang_list,font=('arial',10),width=14,state="readonly",textvariable=select)
        Lang_list_combo.set("select language")
        Lang_list_combo.place(x=25,y=30)
        """



        






#=======================================================================
        Scol1=Scrollbar(frame3,orient="vertical")
        Scol1.grid(column=10,sticky="NS")
        
        texttopaste1=Text(frame3,height=9,width=58,font=('times new roman',12,'bold'),yscrollcommand=Scol1.set,relief="sunken",bd=3)
        texttopaste1.grid(row=0,column=0)
        Scol1.config(command=texttopaste1.yview)


#=====================================================
        
        




        




if __name__ == "__main__":
    root=Tk()
    app=Translate(root)
    root.mainloop()

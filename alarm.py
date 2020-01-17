#Alarm clock using Python Tkinter module 
from tkinter import *
from tkinter import ttk
import time
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
#import os


#def main():
root = Tk()
root.title("Alarm clock")


def SubmitButton():
    label3 = Label(root, text = "", font = ('calibri', 12), foreground = 'white', background = 'sky blue')
    label4 = Label(root, text = "", font = ('calibri', 12), foreground = 'white', background = 'sky blue')
    AlarmTime= entry1.get()
    Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
    CurrentTime = time.strftime("%H:%M")
    label3.config(text = "the alarm time is: {}".format(AlarmTime))
    label3.pack()
    #label2.config(text="")
    while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
        if AlarmTime == CurrentTime:
            label4.config(text = "now Alarm Musing Playing")
            #os.system("omxplayer alarm-music.mp3")
            label2.config(text = "Alarm music playing...")
            sound = AudioSegment.from_wav('alarm-music.wav')
            play(sound)
           # playsound('alarm-music.wav')
           # pygame.mixer.Sound.play(sound)
           # pygame.mixer.music.stop()
     # you can also put the path of the mp3 or wav file if it didn't work
         
     #label5 = Label(title= 'Alarm Message', message= "{}".format(entry2.get()))
     #label5.pack()

def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    #messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))     
#frame1 = ttk.Frame(root)
#frame1.pack()
#frame1.config(height = 100, width = 100)

label1= ttk.Label(root,text = "Enter the Alarm time :")
label1.pack()


entry1 = ttk.Entry(root, width = 30)
entry1.pack()
entry1.insert(3,"example - 13:15")

labelAlarmMessage= ttk.Label(root, text="Alarm Message:")
labelAlarmMessage.pack()

entry2= ttk.Entry(root, width=30)
entry2.pack()

button1= ttk.Button(root, text= "submit", command=SubmitButton)
button1.pack()
#this Label2 will show the Last Alarm Time
label2= ttk.Label(root)
label2.pack()

    
#label2.config(text="hello")

root.mainloop()


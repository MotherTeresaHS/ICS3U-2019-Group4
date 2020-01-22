.. Alarm:

Alarm
==========

For this I made in a different python script and then imported it to the main script that contains all of my code but make sure that both of the python scripts are on the same folder so they would be able to run. To start here you will need 2 libraries which are pydub which is for the sound and time and it's to countdown the time unti lthe clock time 

.. code-block:: python

    #Alarm clock using Python Tkinter module 
    from tkinter import *
    from tkinter import ttk 
    import time
    from playsound import playsound
    from pydub import AudioSegment
    from pydub.playback import play

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
    # this Label2 will show the Last Alarm Time
    label2= ttk.Label(root)
    label2.pack()


    root.mainloop()

======

As you can see here I created another gui app then I asked the user for entry in the gui app and then compared it with the current time. Then I created an if statment thai they both were equal display the messages that was created on the labels then play the alarm sound. 

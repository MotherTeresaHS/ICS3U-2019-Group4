#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on December 2019
# This program fFinds the weather of a certain city

import pyowm
from tkinter import * 
from tkinter.ttk import *
from time import strftime
import datetime
import requests
from playsound import playsound
# from PIL import ImageTk,Image

root = Tk() 
root.title('Smart Clock')
# root.configure(background = "black")
# root.geometry("320x480")

# opening images getting them ready
# img = Image.open(r'C:\\Users\\marwa\\OneDrive\\Pictures\\cloudy.gif') 


# adding an image to tkinter
# canvas=Canvas(root,width=300,height=480)
# image=ImageTk.PhotoImage(Image.open("C:\\Users\\marwa\\OneDrive\\Pictures\\cloudy.gif"))
# label = Label(image=image)



def news():
    # This program runs the news

    root.configure(background="black")
    label = Label(root, text="NEWS", font=('calibri', 25),
                  foreground='white', background='black')
    label.pack()

    url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apikey=e4ba43e5a4e54ab8a1d130127eeb888a'

    # Make the request
    response = requests.get(url).json()

    article = response["articles"]
    # Convert the response to JSON format and pretty print it
    results = []
    lstbox = Listbox(root)
    lstbox.config(bg='black', fg='white', width='100', height='30',
                  font='Helvetica')
    lstbox.pack()

    for item in article:
        lstbox.insert(END, item['title'], "\ndetails: ", item['description'])


def weather():
    # This

    label = Label(root, text = "Weather", font = ('calibri', 25), foreground = 'white', background = 'sky blue')
    label2 = Label(root, text = "clouds :", font = ('calibri', 16), foreground = 'white', background = 'sky blue')
    label3 = Label(root, text = "", font = ('calibri', 12), foreground = 'white', background = 'sky blue')
    label4 = Label(root, text = "rain : ",  font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label5 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
    label6 = Label(root, text = "snow :", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label7 = Label(root, text = "", font = ('calibri', 12), foreground = 'white', background = 'sky blue')
    label8 = Label(root, text = "fog :",font = ('calibri', 16), foreground = 'white', background = 'sky blue')
    label9 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
    label10 = Label(root, text = "Temprature in Celsius :", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label11 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
    label12 = Label(root, text = "weather details", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label13 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
    label14 = Label(root, text = "Wind Speed", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label15 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
    label16 = Label(root, text = "Cloud coverage (in percent) :", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label17 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
    label20 = Label(root, text = "location : ", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
    label21 = Label(root, text = "", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')

    label.grid(row = 1, column = 1)
    label2.grid(row = 5, column = 0)
    label3.grid(row = 5, column = 2)
    label4.grid(row = 6, column = 0)
    label5.grid(row = 6, column = 2)
    label6.grid(row = 7, column = 0)
    label7.grid(row = 7, column = 2)
    label8.grid(row = 8, column = 0)
    label9.grid(row = 8, column = 2)
    label10.grid(row = 9, column = 0)
    label11.grid(row = 9, column = 2)
    label12.grid(row = 10, column = 0)
    label13.grid(row = 10, column = 2)
    label14.grid(row = 11, column = 0)
    label15.grid(row = 11, column = 2)
    label16.grid(row = 12, column = 0)
    label17.grid(row = 12, column = 2)
    label20.grid(row = 13, column = 0)
    label21.grid(row = 13, column = 2)

    owm = pyowm.OWM('3a65677897148889d39423a3ce8e1716')  # You MUST provide a valid API key
    ottawa = owm.three_hours_forecast('Ottawa, Canada')
    
    loc = "Ottawa"
    label21.config(text = loc)

    clouds = ottawa.will_have_clouds()
    fog = ottawa.will_have_fog()
    rain = ottawa.will_have_rain()
    snow = ottawa.will_have_snow()

    #if clouds == 1:
     #   img = Image.open(r'C:\\Users\\marwa\\Downloads\\clearSky.jpg') 
      #  tkimage = ImageTk.PhotoImage(img)
       # img = img.resize((250, 250), Image.ANTIALIAS)
        #tkimage.geometry("120x80")
        #Label(root, image=tkimage, text=" There is clouds today").grid(row = 5, column = 2) # Put it in the display window
   # else:
    #    img = Image.open(r'C:\\Users\\marwa\\Downloads\\clearSky.jpg') 
     #   tkimage = ImageTk.PhotoImage(img)
      #  img = img.resize((250, 250), Image.ANTIALIAS)
        #tkimage.geometry("120x80")
       # Label(root, image=tkimage, text=" There is no clouds today").grid(row = 5, column = 2) # Put it in the display window

    if rain == 1:
        rain = "there is rain today"
    else:
        rain = "there is no rain today"
    if snow == 1:
        snow = "there is snow today"
    else:
        snow = "there is no snow today"
    if fog == 1:
        fog = "there is fog today"
    else:
        fog = "there is no fog today"
    if clouds == 1:
        clouds = "there is clouds today "
    else:
        clouds = "there is no clouds today"

    label3.config(text = clouds)
    label5.config(text = rain)
    label7.config(text = snow)
    label9.config(text = fog)
   # label19.config(text = sun)
    
    ott = owm.weather_at_place('Ottawa, Canada')
    weather = ott.get_weather()
    temp = weather.get_temperature('celsius')['temp']
    temp = round(temp)
    label11.config(text = temp)

    description = weather.get_detailed_status()
    label13.config(text = description)

    wind =  weather.get_wind()
    label15.config(text = wind)

    cloud_cov =  weather.get_clouds()    
    label17.config(text = cloud_cov)

def main():
    #

    label18 = Label(root, text = "Sun: ", font = ('calibri', 16),  foreground = 'white', background = 'black')
    label18.grid(row = 1, column = 0)
    string = strftime('%H:%M:%S \n%d-%m-%Y')
    label18.config(text=string)
    label18.after(1000, main)


if __name__ == "__main__":
    main()

root.mainloop()

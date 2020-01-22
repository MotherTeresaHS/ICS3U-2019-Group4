#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on January 2020
# This program is a smart clock that shows news, weather, calendar and time

import pyowm
from tkinter import Tk, Frame
from tkinter.ttk import *
import tkinter as tk
from time import strftime
# import datetime
import requests
from PIL import ImageTk, Image
from tkinter import *
from tkcalendar import *
from gpiozero import Button


root = Tk()
root.title('Smart Clock')
root.geometry("+200+200")
# root.configure(background = "black")

# defining buttons
button1 = Button(26)
button2 = Button(19)
button3 = Button(6)
button4 = Button(5)
button5 = Button(16)

# creating frames for each function

news_frame = tk.Frame(root, bg='black')
news_frame.grid()

weather_frame = tk.Frame(root, bg='sky blue')
weather_frame.grid()

clock_frame = tk.Frame(root, bg='black')
clock_frame.grid()

calendar_frame = tk.Frame(root, bg='white')
calendar_frame.grid()

time_frame = tk.Frame(root, bg='black')
time_frame.grid()


def calendar():
    # This function gets the calendar

    cal = Calendar(calendar_frame)
    cal.grid()


def news():
    # This function runs the news

    root.configure(background="grey")
    label = Label(news_frame, text="NEWS", font=('calibri', 25),
                  foreground='white', background='grey')
    label.grid()

    url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apikey=e4ba43e5a4e54ab8a1d130127eeb888a'

    # Make the request
    response = requests.get(url).json()

    article = response["articles"]
    # Convert the response to JSON format

    # creating a list to accept api calls

    lstbox = Listbox(news_frame)
    lstbox.config(bg='grey', fg='white', width='100', height='30',
                  font='Helvetica')
    lstbox.grid()

    # showing the list in the gui

    for item in article:
        lstbox.insert(END, item['title'], "\ndetails: ", item['description'])


def forecast():
    # This function shows the weather through weathermap api

    # creating the labels in the weather frame
    root.configure(background="sky blue")
    label = Label(weather_frame, text="Weather", font=('calibri', 25),
                  foreground='yellow', background='sky blue')
    label2 = Label(weather_frame, text="Humidity (in percentage) :", font=('calibri', 16),
                   foreground='white', background='sky blue')
    label3 = Label(weather_frame, text="", font=('calibri', 12),
                   foreground='white', background='sky blue')
    label4 = Label(weather_frame, text="rain : ", font=('calibri', 16),
                   foreground='white', background='sky blue')
    label5 = Label(weather_frame, text="", font=('calibri', 12),
                   foreground='white', background='sky blue')
    label6 = Label(weather_frame, text="snow :", font=('calibri', 16),
                   foreground='white', background='sky blue')
    label7 = Label(weather_frame, text="", font=('calibri', 12),
                   foreground='white', background='sky blue')
    label8 = Label(weather_frame, text="fog :", font=('calibri', 16),
                   foreground='white', background='sky blue')
    label9 = Label(weather_frame, text="", font=('calibri', 12),
                   foreground='white', background='sky blue')
    label10 = Label(weather_frame, text="Temprature in Celsius :",
                    font=('calibri', 16),
                    foreground='white', background='sky blue')
    label11 = Label(weather_frame, text="", font=('calibri', 12),
                    foreground='white', background='sky blue')
    label12 = Label(weather_frame, text="weather details",
                    font=('calibri', 16),
                    foreground='white', background='sky blue')
    label13 = Label(weather_frame, text="", font=('calibri', 12),
                    foreground='white', background='sky blue')
    label14 = Label(weather_frame, text="Wind Speed", font=('calibri', 16),
                    foreground='white', background='sky blue')
    label15 = Label(weather_frame, text="", font=('calibri', 12),
                    foreground='white', background='sky blue')
    label16 = Label(weather_frame, text="Cloud coverage (in percent) :",
                    font=('calibri', 16), foreground='white',
                    background='sky blue')
    label17 = Label(weather_frame, text="", font=('calibri', 12),
                    foreground='white', background='sky blue')
    label20 = Label(weather_frame, text="location : ", font=('calibri', 16),
                    foreground='white', background='sky blue')
    label21 = Label(weather_frame, text="", font=('calibri', 12),
                    foreground='white', background='sky blue')

    # showing the label in the gui in a ccertain location through grid

    label.grid(row=1, column=1)
    label2.grid(row=13, column=0)
    label3.grid(row=13, column=2)
    label4.grid(row=6, column=0)
    label5.grid(row=6, column=2)
    label6.grid(row=7, column=0)
    label7.grid(row=7, column=2)
    label8.grid(row=8, column=0)
    label9.grid(row=8, column=2)
    label10.grid(row=9, column=0)
    label11.grid(row=9, column=2)
    label12.grid(row=10, column=0)
    label13.grid(row=10, column=2)
    label14.grid(row=11, column=0)
    label15.grid(row=11, column=2)
    label16.grid(row=12, column=0)
    label17.grid(row=12, column=2)
    label20.grid(row=5, column=0)
    label21.grid(row=5, column=2)

    # calling the api

    owm = pyowm.OWM('3a65677897148889d39423a3ce8e1716')
    # You MUST provide a valid API key
    ottawa = owm.three_hours_forecast('Ottawa, Canada')

    # location

    loc = "Ottawa"
    label21.config(text=loc)

    # asks the api for weather details

    fog = ottawa.will_have_fog()
    rain = ottawa.will_have_rain()
    snow = ottawa.will_have_snow()

    # shows images depending on weather state

#    if snow == 1 or clouds and snow == 1:
#        load = Image.open("snow.jpeg")
#        render = ImageTk.PhotoImage(load)
#        img = Label(root, image=render)
#        img.image = render
#        img.place(x=650, y=40)
#    elif clouds == 0:
#        load = Image.open("sun.jpeg")
#        render = ImageTk.PhotoImage(load)
#        img = Label(root, image=render)
#        img.image = render
#        img.place(x=650, y=40)
#    if snow and rain and clouds == 1:
#        Image.open("mix.jpeg")
#        render = ImageTk.PhotoImage(load)
#        img = Label(root, image=render)
#        img.image = render
#        img.place(x=650, y=40)
#    elif clouds == 0:
#        Image.open("sun.jpeg")
#        render = ImageTk.PhotoImage(load)
#        img = Label(root, image=render)
#        img.image = render
#        img.place(x=650, y=40)
    # depending on weather state show if it's happening or no

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
#    if clouds == 1:
#        clouds = "there is clouds today "
#    else:
#        clouds = "there is no clouds today"

    # showing the labels

    
    label5.config(text=rain)
    label7.config(text=snow)
    label9.config(text=fog)

    # calling api for different funcion

    ott = owm.weather_at_place('Ottawa, Canada')
    weather = ott.get_weather()

    humidity = weather.get_humidity()
    label3.config(text=humidity)

    temp = weather.get_temperature('celsius')['temp']
    temp = round(temp)
    label11.config(text=temp)

    description = weather.get_detailed_status()
    label13.config(text=description)

    wind = weather.get_wind()
    label15.config(text=wind)

    cloud_cov = weather.get_clouds()
    label17.config(text=cloud_cov)


def time():
    #

    labl = Label(time_frame, text="", font=('calibri', 40),
                 foreground='white', background='black')
    labl.grid(row=1, column=0)
    string = strftime('%H:%M:%S \n%d-%m-%Y')
    labl .config(text=string)
    labl.after(1000, main)


def main():
    # This function gets the time and date and calls other function

    label18 = Label(clock_frame, text="", font=('calibri', 40),
                    foreground='white', background='black')
    label18.grid(row=0, column=0)
    string = strftime('%H:%M:%S \n%d-%m-%Y')
    label18.config(text=string)
    label18.after(1000, main)

    # if button state changes call the function associated with it

    if button1.is_pressed:
        weather_frame.grid_forget()
        clock_frame.grid_forget()
        calendar_frame.grid_forget()
        time_frame.grid_forget()
        news_frame.grid()
        news()
    if button2.is_pressed:
        news_frame.grid_forget()
        time_frame.grid_forget()
        clock_frame.grid_forget()
        weather_frame.grid()
        forecast()
    if button3.is_pressed:
        import alarm
    if button4.is_pressed:
        news_frame.grid_forget()
        weather_frame.grid_forget()
        time_frame.grid_forget()
        clock_frame.grid_forget()
        calendar_frame.grid()
        calendar()
    if button5.is_pressed:
        news_frame.grid_forget()
        weather_frame.grid_forget()
        clock_frame.grid_forget()
        calendar_frame.grid_forget()
        time_frame.grid()
        time()


if __name__ == "__main__":
    main()

root.mainloop()

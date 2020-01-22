.. Weather:

Weather function
==========

In this function we are going to show the weather details. first we will create our labels for this function we are going to make 20 labels. the first one will be for the title and the others will be for other detials that we will be getting from the Api I am using which is `open weather map <https://openweathermap.org/>`_ and there is a library that was created to help use it which is the `pyowm <https://pyowm.readthedocs.io/en/latest/>`_

.. code-block:: python
    
    
    # creating the labels in the weather frame
    root.configure(background="sky blue")
    label = Label(weather_frame, text="Weather", font=('calibri', 25),
                  foreground='yellow', background='sky blue')
    label2 = Label(weather_frame, text="clouds :", font=('calibri', 16),
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
    label2.grid(row=5, column=0)
    label3.grid(row=5, column=2)
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
    label20.grid(row=13, column=0)
    label21.grid(row=13, column=2)

    # calling the api

    owm = pyowm.OWM('3a65677897148889d39423a3ce8e1716')
    # You MUST provide a valid API key
    ottawa = owm.three_hours_forecast('Ottawa, Canada')

    # location

    loc = "Ottawa"
    label21.config(text=loc)

    # asks the api for weather details

    clouds = ottawa.will_have_clouds()
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
    if clouds == 1:
        clouds = "there is clouds today "
    else:
        clouds = "there is no clouds today"

    # showing the labels

    label3.config(text=clouds)
    label5.config(text=rain)
    label7.config(text=snow)
    label9.config(text=fog)

    # calling api for different funcion

    ott = owm.weather_at_place('Ottawa, Canada')
    weather = ott.get_weather()

    temp = weather.get_temperature('celsius')['temp']
    temp = round(temp)
    label11.config(text=temp)

    description = weather.get_detailed_status()
    label13.config(text=description)

    wind = weather.get_wind()
    label15.config(text=wind)

    cloud_cov = weather.get_clouds()
    label17.config(text=cloud_cov)
=========

So after creating the labels and showing them in the gui using grid. we are going to call the api with and we will access it with the key that we have then we are going to get details for what is the weather in the next 3 hours in our location. After that we are going to get the data we wnat from the api and put it in the labels we created. you can also add images and you will find its code in here but I commented because since I am using an lcd screen there will be no space to place my image in the tkinter window.

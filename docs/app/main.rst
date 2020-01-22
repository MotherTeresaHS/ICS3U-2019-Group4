.. Main:

Main function
==========

First we will start by displaying the date and time you will need the library of time and it will be in our main function

.. code-block:: python

   label18 = Label(clock_frame, text="", font=('calibri', 40),
                    foreground='white', background='black')
    label18.grid(row=0, column=0)
    string = strftime('%H:%M:%S \n%d-%m-%Y')
    label18.config(text=string)
    label18.after(1000, main)
    
===========

As you can see first I made a tkinter label with font = 40, text colour should be white and the background should be black. Then I sould it in my screen by the next line using grid, then I assigned a string to the time and date and lastly I added it to the label to show up in the gui.


After showing the time I will make the if statements for the buttons so that if they were pressed to call the other functions.

 .. code-block:: python
     
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
============

For each if statment i made the frames to get forgotten and then shown again if the button they are assigned is called except for button 3 which imports calls another script wwhich is for the alarm.
 
 

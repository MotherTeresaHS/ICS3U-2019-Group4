
Time function
=======

Since I faced the problem if not being able to return to the time again after running any function that you wanted. So I decided to make another function that shows time and it would be accesible some of you would say why not call the main again the reason behind that it will give you errors and it will not always works since you are asking the program to run the main function twice.

.. code-block:: python

    labl = Label(time_frame, text="", font=('calibri', 40),
                 foreground='white', background='black')
    labl.grid(row=1, column=0)
    string = strftime('%H:%M:%S \n%d-%m-%Y')
    labl .config(text=string)
    labl.after(1000, main)

=======

As you can see it is exactly the same code as the main function time but we changed the frame we are using and the label name. That is it congruations you have finally completed the tutorial and built the program

This is what it should look like:

.. image:: ./time/time .jpg
      :width: 320 px
      :height: 240 px

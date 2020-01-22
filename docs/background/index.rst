.. Gui:

Creating the gui
==========

After writing your import statements you will go ahead and start in coding to show and create your Gui 

.. code-block:: python

   root = Tk()
   root.title('Smart Clock')
   root.geometry("+200+200")
   
   ===========

The first line creates the Gui itself then the second one is to give it a title lastly the geometry is to resize your window or to open in a certain place in your desktop so since I am using a an lcd screen I need it to open in a certain place which is the middle of the screen

.. code-block:: python

    button1 = Button(26)
    button2 = Button(19)
    button3 = Button(6)
    button4 = Button(5)
    button5 = Button(16)
=========

Those lines are to set the buttons for each gpio pin I used. you will need the gpio zero library to do that. you can't run the buttons code from your pc or laptop it has to be from the raspberry pi so make sure to comment it in your pc or laptop

.. code-block:: python

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

==========

Lastly this is were we create the frames for each function so that we would be able to hide it if the other function runs. So for each of them the first line is to create it and set the background color and the second is to make it show up in the Gui screen if called.

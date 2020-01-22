
Your IDE
========

One of the great things about raspbbery pi  is that it is just a small sized a computer you simply need to install raspian on it then when you attach it to a monitor it will work as a computer. This means that you can access and save your code using any text editor installed at raspian. This is particularly helpful in schools, where computers are likely to be locked down so students can not load anything. To control the raspbbery pi from your own computer you will need an ssh connection


 your best beat for an IDE is `Thonny Editor <https://thonny.org/>`_. it comes installed on the raspbbery pi. It works seamlessly and it will give you debugging information.

.. figure:: ./circuitpython_mu-front-page.png
   :width: 480 px
   :alt: Thonny Editor
   :align: center

   Thonny IDE

Since with CircuitPython devices you are just writing Python files, you are more than welcome to use any IDE that you are familiar using.

Hello, World!
-------------

Yes, you know that first program you should always run when starting a new coding adventure, just to ensure everything is running correctly! Once you have access to your IDE and you have Raspian loaded, you should make sure everything is working before you move on. To do this we will do the traditional "Hello, World!" program.

.. code-block:: python
	:linenos:

	print("Hello, World!")

As soon as you save the file onto the pi, the terminal should come up and you should see something like:

.. figure:: ./hello_world.png
   :width: 480 px
   :alt: Hello, World!
   :align: center

   Hello, World! program 

Although this code does work just as is, it is always nice to ensure we are following proper coding conventions, including style and comments. Here is a better version of Hello, World! You will notice that I have a call to a :py:func:`main()` function. This is common in Python code but not normally seen in CircuitPython. I am including it because by breaking the code into different functions to match different scenes, eventually will be really helpful.


.. literalinclude:: ./example.py
   :language: py
   :lines: 10-20

.. code-block:: python
	:linenos:

	#!/usr/bin/env python3

	# Created by : Marwan Mashaly
	# Created on : January 2020
	# This program prints out Hello, World! onto the PyBadge

	  
	def main():
	    # this function prints out Hello, World! onto the PyBadge

	    print("Hello, World!")


	if __name__ == "__main__":
	    main()
    

Congratulations, we are ready to start.

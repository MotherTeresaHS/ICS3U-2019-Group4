.. News:

News
==========

For the news I have used  `News Api <https://newsapi.org/>`_  to get the data from the BBC and display it in my gui. After you create the frame you will call it inside the label that you will create 

.. code-block:: python
    
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

===========

After creating the label you will call the json file in requests then you will get a response and you will put it in a list as you can see in line 11 then you will create a tkinter list as you can see in line 16 and you will display by grid. Lastly you will display each time the list articles in order throught the other list we created.

This is what it should look like:

.. image:: ./news/news.jpg
      :width: 320 px
      :height: 240 px
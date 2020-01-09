from tkinter import *
from tkinter.ttk import *
import requests


def news():
    # This program runs the weather

    
    root.title('News')
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


if __name__ == "__main__":
    news()

root.mainloop()

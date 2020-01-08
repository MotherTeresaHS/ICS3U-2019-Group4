#import requests
#url = ('https://newsapi.org/v2/top-headlines?'
  #     'country=ca&'
 #      'apiKey=e4ba43e5a4e54ab8a1d130127eeb888a')
#response = requests.get(url)
#print (response.json())

# importing requests package 
#import requests	 

#def NewsFromBBC(): 
	
	# BBC news api 
#	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"

	# fetching data in json format 
#	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
#	article = open_bbc_page["articles"] 

	# empty list which will 
	# contain all trending news 
#	results = [] 
	
#	for ar in article: 
#		results.append(ar["title"]) 
		
#	for i in range(len(results)): 
		
		# printing all trending news 
#		print(i + 1, results[i])				 

# Driver Code 
#if __name__ == '__main__': 
	
	# function call 
#	NewsFromBBC() 

from tkinter import * 
from tkinter.ttk import *
import requests

root = Tk() 
root.title('news')
root.configure(background = "black")

label = Label(root, text = "NEWS", font = ('calibri', 25), foreground = 'white', background = 'sky blue')
label2 = Label(root, text = "2.", font = ('calibri', 16), foreground = 'white', background = 'sky blue')
label3 = Label(root, text = "3.", font = ('calibri', 12), foreground = 'white', background = 'sky blue')
label4 = Label(root, text = "4.",  font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
label5 = Label(root, text = "5.", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
label6 = Label(root, text = "6.", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
label7 = Label(root, text = "7.", font = ('calibri', 12), foreground = 'white', background = 'sky blue')
label8 = Label(root, text = "8.",font = ('calibri', 16), foreground = 'white', background = 'sky blue')
label9 = Label(root, text = "9.", font = ('calibri', 12),  foreground = 'white', background = 'sky blue')
label10 = Label(root, text = "10.", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')
label11 = Label(root, text = "10.", font = ('calibri', 16),  foreground = 'white', background = 'sky blue')

label.grid(row = 1, column = 1)
label2.grid(row = 3, column = 0)
label3.grid(row = 5, column = 2)
label4.grid(row = 7, column = 0)
label5.grid(row = 9, column = 2)
label6.grid(row = 11, column = 0)
label7.grid(row = 13, column = 2)
label8.grid(row = 15, column = 0)
label9.grid(row = 17, column = 2)
label10.grid(row = 19, column = 0)
label11.grid(row = 21, column = 0)


def main():
    #
 
    secret = 'e4ba43e5a4e54ab8a1d130127eeb888a'
    url = 'https://newsapi.org/v2/everything?'

    # Specify the query and number of returns
    parameters = {
        'q': 'big data', # query phrase
        'pageSize': 10,  # maximum is 100
        'apiKey': secret # your own API key
    }
    # Make the request
    response = requests.get(url, params=parameters)

    # Convert the response to JSON format and pretty print it
    response_json = response.json()


    for i in response_json['articles']:
        label2.config(text = i['title'])   #,  i['description'])
        print("Header: ", i['title'], " \ndetails: ",  i['description'])
        print("")


if __name__ == "__main__":
    main()

root.mainloop()

import requests
from bs4 import BeautifulSoup
import os
from twilio.rest import Client

# Setting up the variables 
stock = input("Enter Valid Stock Ticker: ")
number = input("Enter Number to send information: ")
targetPrice = input("Please enter the target price for the stock as a float: ")


# This will scrape yahoo finance using the BeautifulSoup library 
def getPrice():
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')


    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return float(price)


# This will alert the user if/when the stock is above their target price
def sendMessage():
    account_sid = 'ACac8529bcc4b7dd6ebc222e6879755b75'
    auth_token = '67f3e0909e8a3a9fe947cd4ee159dbc7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to= number,
        from_= '+12515729901',
        
        body= stock +" Is at your target of " + targetPrice
    )


# this will constantly run and get the 
while True:
    if getPrice() > float(targetPrice):
        sendMessage()
        print('done')
        break
 








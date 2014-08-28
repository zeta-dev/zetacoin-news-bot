#!/usr/bin/env python

__author__ = 'Tecem'
__version__ = "0.1"

import urllib2, cookielib, json

#HTTP header to acces the exchange api.
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#Function to get the latest coin price on Bittrex. It takes the string of a coin as input.
#Example bittrex('zet') will return the latest Zetacoin price.
def bittrex(coin):
    URL = "https://bittrex.com/api/v1.1/public/getticker?market=btc-"+coin
    f = urllib2.urlopen(URL)
    s = f.read()
    data = json.loads(s)
    f.close()
    message= str(data['success'])
    
    if str(message) == "True":
        return float((data['result']['Last']))
    else:
        return "False"
        
#Function to get the latest coin price on Atomic Trade. It takes the string of a coin as input.
#Example atomictrade('zet') will return the latest Zetacoin price.
def atomictrade(coin):
    URL = "https://www.atomic-trade.com/GetPrices?c=" + coin + "&p=BTC"
    req = urllib2.Request(URL, headers=hdr)
    page = urllib2.urlopen(req)
    content = page.read()
    page.close()
    data = json.loads(content)
    price = data['price']
    error=0.00000000
    if float(price) != float(error):
        return float(price)
    else:
        return "False"

#Function to get the latest coin price on Mintpal. It takes the string of a coin as input.
#Example mintpal('zet') will return the latest Zetacoin price.
def mintpal(coin):
    URL = 'https://api.mintpal.com/v1/market/stats/' + coin + '/' + "BTC"
    data = []    
    try:
        f = urllib2.urlopen(URL)
    except urllib2.HTTPError, e:  
        if e.code == 404:
            price="False"
            return price
    else:
        s = f.read()
        data = json.loads(s)
        f.close()
        price = (data[0]['last_price'])
        return float(price)

#Function to get the latest coin price on Cryptsy. Market is fixed so it doesn't need an argument.
#Example cryptsy() will return the latest Zetacoin price.
def cryptsy():
    URL = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=85"
    data = [] 
    req = urllib2.Request(URL, headers=hdr)
    page = urllib2.urlopen(req)
     
    content = page.read()
    page.close()
    data = json.loads(content)
    if data['success'] == 1:
        price= data['return']['markets']['ZET']['lasttradeprice']
        return float(price)
    else:
        price = "False"
        return price
    
#Function to get the latest coin price on bter. It takes the string of a coin as input.
#Example bter('zet') will return the latest Zetacoin price.
def bter(coin):
    URL = "http://data.bter.com/api/1/ticker/"+ coin + "_BTC"
    data = [] 
    req = urllib2.Request(URL, headers=hdr)
    page = urllib2.urlopen(req)  
    content = page.read()
    page.close()
    data = json.loads(content) 
    if data['result'] == 'true':
        price = data['last']
        return float(price)
    else:
        price = "False"
        return price

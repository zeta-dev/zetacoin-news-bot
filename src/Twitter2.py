from twitter import *
import Exchanges
import os
import time

#App website https://dev.twitter.com/apps/

#authenticate met twitter
def autehnticate():
    CONSUMER_KEY="API KEY HERE" #app key
    CONSUMER_SECRET="APP SECRET HERE" #app secret
    MY_TWITTER_CREDS = os.path.expanduser('~/.zetbotcred')   #twitter user data
    if not os.path.exists(MY_TWITTER_CREDS):#als er geen data is dan toestemming geven.
        oauth_dance("Zet Price ticker", CONSUMER_KEY, CONSUMER_SECRET,MY_TWITTER_CREDS)
    OAUTH_TOKEN, OAUTH_SECRET = read_token_file(MY_TWITTER_CREDS)
    t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY, CONSUMER_SECRET))
    return t #geef de authenticatie key terug
   
   
def sendtweet():
    bittrexprice=Exchanges.bittrex('zet')
    mintpalprice=Exchanges.mintpal('zet')
    bterprice=Exchanges.bter('zet')
    
    message = "1 $ZET = " '%.8f' % bittrexprice + " BTC " + "@ " +"Bittrex" + "\n" + "1 $ZET = " '%.8f' % mintpalprice + " BTC " + "@ " +"Mintpal" + "\n" + "1 $ZET = " '%.8f' % bterprice + " BTC " + "@ " +"Bter"
    if len(message) <= 144:
        t=t=autehnticate()
        t.statuses.update(status=message)   
       

def start():
    while True: 
        sendtweet()
        time.sleep(3600)  
        lol =lol +1
start()          



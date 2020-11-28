import tweepy as tw
import csv
import pandas as pd
from tqdm import tqdm
import re

API_key="GcCte6U4qMqm3Pkva9SRWJpd5"
API_key_secret="98yOQET4OHaPTMGEhnfw9nOvkg12zBEV8BJ6zazXbQVZd1ptTj"
Access_token = "236194542-tCfu9u9qkpWUx0DgBzZmPJ6S7h7VzZ7ybCvpEqfx"
Access_token_secret= "iCZwNZWBuUNpknUHQrIIxqSlJqTe4UGbyZdOEFZCbYZwt"

auth = tw.OAuthHandler(API_key,API_key_secret)
auth.set_access_token(Access_token,Access_token_secret)

api = tw.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

word = '#trump' +' -filter:retweets'

places = api.geo_search(query="USA", granularity="country")
place_id = places[0].id

tweets = tw.Cursor(api.search, q=word,lang="en").items()




with open('data.csv', 'w') as file:
    writer = csv.writer(file,lineterminator='\n')
    writer.writerow(['user_id','tweet'])
    for tweet in tweets:
        if('\n' in tweet.text):
            tweet.text = tweet.text.replace('\n','')
        try:
            url = re.search("(?P<url>https?://[^\s]+)", tweet.text).group("url")
            tweet.text = tweet.text.replace(url,'')
            print('{}/{}'.format(tweet.id_str,tweet.text))     
            writer.writerow([tweet.id_str,tweet.text])
        except:
            writer.writerow([tweet.id_str,tweet.text])

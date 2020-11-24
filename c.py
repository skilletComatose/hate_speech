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

word = '@IvanDuque' +' -filter:retweets'

tweets = tw.Cursor(api.search, q=word,lang="es").items(100)

with open('data.csv', 'w') as file:
    writer = csv.writer(file,lineterminator='\n')
    writer.writerow(['user_id','tweets','url'])
    for tweet in tweets:
        if('\n' in tweet.text):
            tweet.text = tweet.text.replace('\n','')
        try:
            url = re.search("(?P<url>https?://[^\s]+)", tweet.text).group("url")
            tweet.text = tweet.text.replace(url,'')     
            writer.writerow([tweet.id_str,tweet.text,url])
        except:
            writer.writerow([tweet.id_str,tweet.text,None])

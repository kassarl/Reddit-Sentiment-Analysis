from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

import praw

# Initializes Reddit API
reddit = praw.Reddit(client_id='Jsv3bswI2GWJ4w',
                     client_secret='FxCqFkRtCLBKpMytakuJ33RDiVI',
                     user_agent='daydragons')
# creates empty array?
#headlines = set()
headlines = []

# Select subreddit of interest
#userInput = str(input('What subreddit are you interested in?\n'))
#userInput = userInput + "/hot"
print('-' * 100)

# for every sub in "Hot" up to limit #
for submission in reddit.subreddit("leagueoflegends").hot(limit=None):
    # If the headline has "__" in the title
    if "Discussion" in submission.title:
        # Makes array of headlines of interest
        headlines.append(submission.title)
        # Prints out the titles
        print("\n"+ submission.title)
        #display.clear_output()
        #print(len(headlines))

# Empty dictionary for storage of titles and sentiment
bloblib = {}

# Writes Entry and Key Values (#NOTE KEY VALUES ARE WRONG B/C NEED COMMENTS / UPVOTE RATIO) 
for i in range(0,len(headlines)):
    l = headlines[i]
    bloblib[l] = TextBlob(l)

# Prints out the dictionary values
for i in bloblib :
    print("The headLine \n " + str(i) + "\nthe polarity: \n " + str(bloblib[i].sentiment.polarity))
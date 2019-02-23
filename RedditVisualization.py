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

# Empty dictionary for storage of titles and sentiment array
bloblib = {}
limit = 10

# Summing Bins
Very_Negative = 0
Somewhat_Negative = 0
Neutral = 0
Somewhat_Positive = 0
Very_Positive = 0


# for every sub in "Hot" up to limit #
for submission in reddit.subreddit("politics").top('week',limit=limit):
    sentArray = []
    #If the headline has "__" in the title
    if "Trump" in submission.title:
        print('#' * 100)
        print("\n")
        # Dictionary Entry : Title Post
        bloblib[submission.title] =  submission.comments.list()

        print("TITLE: "  + submission.title)
        print("Sent: " + str(TextBlob(submission.title).sentiment.polarity))
        j = 0; i = 0;

        # Grabbing top 5 comments
        while j < 5:
            # first comment's HEX key
            comment = submission.comments[i]
            score = (submission.comments[i].score)
            if "I am a bot" in comment.body:
                i = i + 1
                pass
            else:
                # Prints out the content of the comment and its key
                print("\n COMMENT " + str(j+1) + ": " + comment.body)
                print(" SCORE: " + str(score))

                sentiment = TextBlob(comment.body).sentiment.polarity

                # Appends top 5 sentiment.polarity values for each comment
                sentArray.append(sentiment)
                print(" SENTIMENT: " + str(sentiment))
                
                # Bin addition
                if sentiment <= 1 and sentiment >= .6:
                    Very_Positive = Very_Positive + 1 * score 
                elif sentiment < .6 and sentiment >= .1:
                    Somewhat_Positive = Somewhat_Positive + 1 * score
                elif sentiment < .1 and sentiment >= -.1:
                    Neutral = Neutral + 1 * score
                elif sentiment < -.1 and sentiment >= -.6:
                    Somewhat_Negative = Somewhat_Negative + 1 * score
                else:
                    Very_Negative = Very_Negative + 1 * score

                j = j + 1
                i = i + 1

        # Assigns array keys to title
        bloblib[submission.title] = sentArray

print('#' * 100)
print("\nThere were " + str(len(bloblib)) + " threads about the topic in the last " + str(limit) + " posts.")
print("\n Outputting graphs now...")
print("Very Positive Responses: " + str(Very_Positive))
print("Somewhat Positive Responses: " + str(Somewhat_Positive))
print("Neutral Responses: " + str(Neutral))
print("Somewhat Negative Responses: " + str(Somewhat_Negative))
print("Very Negative Responses: " + str(Very_Negative))






labels = "Very Positive", "Somewhat Positive", "Neutral", "Somewhat Negative", "Very Negative"
sizes = [Very_Positive, Somewhat_Positive, Neutral, Somewhat_Negative, Very_Negative]

fig1,ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
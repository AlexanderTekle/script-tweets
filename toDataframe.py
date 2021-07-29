import jsonlines
import os
import pandas as pd


count=0
df_tweets = pd.DataFrame({'tweet': [], 'tweetid': [], 'timestamp': [], 'lang': [], 'user': []})

for filename in os.listdir('./tweets'):
    #print(count)
    if (str(filename) != ".DS_Store") and (str(filename) != "tweet-ids") and (str(filename) != "zipped-tweets"):
        with jsonlines.open("./tweets/" + filename) as f:
            print(str(filename))
            for obj in f:
                try:
                    str(obj["retweeted_status"])
                except KeyError:
                    df_tweets.loc[count]=[str(obj['full_text']), str(obj['id']), str(obj['created_at']), str(obj['lang']), str(obj['user']['screen_name'])]
                    #print(str(count) + ". " + obj['full_text'])         # printing full tweet
                    count=count+1
                    if count % 1000 == 0:
                       print("1000")
    print(count)
# Write to dataset
df_tweets.to_pickle("covid-tweets-ids.pkl")
print(df_tweets.head())

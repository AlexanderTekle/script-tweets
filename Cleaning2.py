import pickle
import emoji
from emoji import UNICODE_EMOJI
import pandas as pd
import pickle5 as pickle

def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)

def filtering(text):
    text_split = text.split();
    for i in range(len(text_split)):
        if text_split[i].startswith('http'):
            text_split[i] = ''
        elif text_split[i].startswith('<user>'):
            text_split[i] = ''
        #elif text_split[i].startswith(' '):
             #text_split[i] = ''
        elif text_split[i].startswith('<url>'):
             text_split[i] = ''
        elif text_split[i].startswith('@'):
            text_split[i] = ''
        elif text_split[i].startswith('#'):
            text_split[i] = ''
        elif(bool(emoji.get_emoji_regexp().search(text_split[i]))): 
            text_split[i] = ''

    ret=' '.join(text_split)
    ret=ret.strip('"')
    ret=ret.replace('\"','')
    #print(ret)
    #print(ret)
    return ret



#df=pd.read_pickle("./covid-tweets.pkl")
with open("./covid-tweets-February-fasttext.pkl", "rb") as f:
    df = pickle.load(f)
df['tweet'] = df['tweet'].apply(lambda x : filtering(x))
df.to_pickle("./covid-tweets-cleaned-February.pkl")

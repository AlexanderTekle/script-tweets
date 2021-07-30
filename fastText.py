import fasttext
import pickle
import pandas as pd

#df_old=pd.read_pickle("./covid-tweets-filtered.pkl")
df_old=pd.read_pickle("./covid-tweets-ids.pkl")
lang_model = fasttext.load_model("./lid.176.ftz")
langs = []
count=0; 

df_new = pd.DataFrame({'tweet': [], 'tweetid': [], 'timestamp': [], 'lang': [], 'user': []})

for index, row in df_old.iterrows():
    if (count % 25000 == 0):
        print(count)
    #print(count)
    row['tweet']=row['tweet'].replace('\n','')
    #print(row['tweet'])
    lang = lang_model.predict(row['tweet'])
    twitter_lang = "('__label__" + row['lang'] + "',)"
    if (str(lang[0]) == twitter_lang): 
        df_new.loc[count]=[row['tweet'], row['tweetid'], row['timestamp'], row['lang'], row['user']]
        count+=1; 

print(count)
df_new.to_pickle("./covid-tweets-ids-fastext.pkl")
print(df_new.head())
#print(lang_model.predict("Incapaz de distinguir la luna y la cara de esta chica,Las estrellas se ponen nerviosas en el cielo.")[0])

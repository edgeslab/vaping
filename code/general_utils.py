import matplotlib.ticker as tick
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import pandas as pd
import re
import string

def ticks_in_K(value, pos):
    return "{}K".format(int(value/1000))

def plot_statewise_stats(df, popDf):
    statedf = df.groupby('state')['userID'].nunique()
    statedf.index.name = 'state'
    statedf = statedf.reset_index(name='count')
    statedf = statedf.merge(popDf, on='state',  how='left')
    statedf = statedf.sort_values(by='Population', ascending=False)
    ax = sns.barplot(x='State', y='count', data=statedf, orient='v', dodge=True)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=6)
    ax.yaxis.set_major_formatter(tick.FuncFormatter(ticks_in_K))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.xticks(rotation=90)
    plt.ylabel("Number of Users", fontsize=8)
    plt.xlabel("U.S. States (Sorted by Population Size)", fontsize=8)
    plt.tight_layout()
    
    
# should contain one of the keywords in the tweet or hashtags
juulKeywords = ['juul', 'juulvapor', 'juulnation', 'doitjuul']
weedKeywords = ['weed',  'ganja',  'marijuana',  'cannabis',
                'mary jane',  'thc','marihuana', 'hash', 'reefer',
                'hashish', 'bhang', 'cbd', 'greengoddess',
                'locoweed',   'maryjane',   'spliff',   'hemp',
                'wackybaccy', 'sinsemilla', 'doobie', 'acapulco gold']
def check_keywords(text, hashtags, lookup):
    if any(word in text.lower() for word in lookup):
        return True
    if hashtags is None or hashtags == '':
        return False
    else:
        match = set(hashtags)
        overlap = set(lookup).intersection(match)
        if len(overlap)>0:
            return True
        else:
            return False
        
def filter_tweets_with_keywords(df, keywords):
    df['hasKeywords'] = df[['tweetText', 'hashtags']].apply(lambda x: check_keywords(
    x[0],x[1], keywords), axis=1)
    df = df[df['hasKeywords']==True]
    return df

posMapping = {
      "N":'n',
      "V":'v',
      "J":'a',
      "R":'r'
  }

def blind_url(text):
    text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '<URL>',text)
    return text

def clean_text(text, lemmatizer=nltk.stem.wordnet.WordNetLemmatizer()):
#     #Remove urls
#     text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',text)
    ## Convert words to lower case and split them
    text = text.lower()
    ## Clean the text
    text = re.sub(r"<url>", "url", text)
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    
    ## Remove puncuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    tokens = nltk.word_tokenize(text, preserve_line=True)
    tokens_pos = nltk.pos_tag(tokens)
    tokens_root = []
    for token, pos in tokens_pos:
        try:
            root_word = lemmatizer.lemmatize(token, pos=posMapping.get(pos[0],'n'))
            tokens_root.append(root_word)
        except Exception as e:
            print(e)
            continue
    text = " ".join(tokens_root)
    return text



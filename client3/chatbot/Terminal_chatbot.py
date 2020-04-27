
#Meet Robo: your friend

#import necessary libraries
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import tkinter as tk
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only


#Reading in the corpus
with open('chatbot/chatbot.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


val=230
valx=200

root= tk.Tk()
canvas1 = tk.Canvas(root, width =400, height =500)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

 
#x1 = entry1.get()
    
#    label1 = tk.Label(root, text= float(x1)**0.5)
#    canvas1.create_window(200, 230, window=label1)

print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
def getSquareRoot (): 
    user_response = entry1.get()
    global val
    valy=val+20
    val=valy
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            data="ROBO :Thank you its my pleasure to help you"
            label1 = tk.Label(root, text=data)
            canvas1.create_window(valx, valy, window=label1)
            #sent_tokens.remove(user_response)
        else:
            if(greeting(user_response)!=None):
                data="ROBO: "+greeting(user_response)
                label1 = tk.Label(root, text=data)
                canvas1.create_window(valx, valy, window=label1)
                #sent_tokens.remove(user_response)
            else:
                data=user_response
                data="Question: "+data
                label1 = tk.Label(root, text=data)
                val=val+20
                valy=val
                canvas1.create_window(valx, valy, window=label1)
                
                data=response(user_response)
                data="ROBO:"+data
                label1 = tk.Label(root, text=data)
                val=val+20
                valy=val
                canvas1.create_window(valx, valy, window=label1)
    else:
        data='bye thanks'
        label1 = tk.Label(root, text=data)
        canvas1.create_window(valx, valy, window=label1)
        #sent_tokens.remove(user_response)
        




    
button1 = tk.Button(text='Get the answer', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()





        



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
import tkinter
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only


#Reading in the corpus
with open('chatbot.txt','r', encoding='utf8', errors ='ignore') as fin:
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



top = tkinter.Tk()
top.title("Rohiths covid19 bot")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbary = tkinter.Scrollbar(messages_frame)
scrollbarx = tkinter.Scrollbar(messages_frame, orient=tkinter.HORIZONTAL)
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=50, width=100,xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

scrollbarx.pack(side=tkinter.BOTTOM, fill=tkinter.X)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
scrollbary.pack(side=tkinter.RIGHT, fill=tkinter.Y)

messages_frame.pack()
 
#x1 = entry1.get()
    
#    label1 = tk.Label(root, text= float(x1)**0.5)
#    canvas1.create_window(200, 230, window=label1)

print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
def getSquareRoot (): 
    user_response = my_msg.get()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            data="ROBO :Thank you its my pleasure to help you"
            msg_list.insert(tkinter.END, data)
            #sent_tokens.remove(user_response)
        else:
            if(greeting(user_response)!=None):
                data="ROBO: "+greeting(user_response)
                msg_list.insert(tkinter.END, data)
                #sent_tokens.remove(user_response)
            else:
                data=user_response
                data="Question: "+data
                msg_list.insert(tkinter.END, data)
                
                data=response(user_response)
                data="ROBO:"+data
                msg_list.insert(tkinter.END, data)
    else:
        data='bye thanks'
        msg_list.insert(tkinter.END, data)

  
        




    
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>",getSquareRoot)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=getSquareRoot)
send_button.pack()


tkinter.mainloop()






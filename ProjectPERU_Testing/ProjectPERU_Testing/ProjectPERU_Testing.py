import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
import praw 
import json


def build_regression(X,y):
    # 10 folder cross validation to estimate the best w and b
    regress = LogisticRegression()
    regress.fit(X,y)
    return regress

#TODO: Fix Testing, need to fix matrix
def testing(reg,data):
    with open(data,"r") as file:
        store = json.load(file)
    predictions = reg.predict(store)
    print predictions
    





def load_obj_from_file(filename):
    with open(filename, 'rb') as in_file:
        obj = pickle.load(in_file)
    return obj


def main():
    subFile = open("subredditsubData.txt","w")
    reddit = praw.Reddit(client_id='iPfvVyGHka22BA',
                     client_secret='ed6HNahtptNuldBkduE_up753as',
                     user_agent='Python Political Predictor by /u/Snazlie',
                     username='*************************************',
                     password='*************************************')
    
    subData = []
    subreddit = raw_input("Please enter A subreddit to test determine political views: \n")
    print subreddit
    sub = reddit.subreddit(subreddit)
    for submission in sub.hot(limit=10):
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=10)
        for comment in submission.comments:
            print comment
            parsed_comment = comment.body
            subData.append(parsed_comment.encode('utf-8'))
    for element in subData:
        element = element.replace(',','')
        subFile.write(' ,' + element.replace('\n',' ') + '\n')
    subFile.close()
    X = load_obj_from_file("X_all.pkl")
    Y = load_obj_from_file("Y.pkl")
    regression = build_regression(X,Y)
    testing(regression,"subredditsubData.txt")
    
    
if __name__ == '__main__':
    main()


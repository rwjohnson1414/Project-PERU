import operator
from sklearn import *
from sklearn.model_selection import GridSearchCV
import io
import pandas as pd
import numpy as np

def meaningful(rep,dem):
    file = open("meaningfulData.txt","w")
    t = 0
    for line in rep:
        analysis = line.split(",")
        if analysis[0] == '1':
            t = t + 1
            if t == 3200:
                break
            else:
                line = line.lower()
                file.write(line)
        else:
            pass
    print t
    print "completed"
    i = 0
    for line in dem:
        analysis = line.split(",")
        if analysis[0] == '0':
            i = i + 1
            if i == 3200:
                break
            else:
                line = line.lower()
                file.write(line)
        else:
            pass
    print i
    print "completed"


def main():
    repData = open("labeled_republican_data.txt","r")
    demData = open("democraticData.txt","r")

    meaningful(repData,demData)
    

if __name__ == '__main__':
    main()

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics



def build_regression(X_train,X_test,y_train,y_test):
    # 10 folder cross validation to estimate the best w and b
    regress = LogisticRegression()
    regress.fit(X_train,y_train)
    
    predictions = regress.predict(X_test)
    score = regress.score(X_test,y_test)
    print score
    w1 = regress.coef_[0,0]
    w2 = regress.coef_[0,1]
    b = regress.intercept_[0]
    x = [min(item[0] for item in X_train),max(item[0] for item in X_train)]
    y = [(-1 * w1 * i -1 * b) / w2 for i in x]
    cm = metrics.confusion_matrix(y_test, predictions)

   #TODO: split into Pos & Neg classes for visualization

    #plt.scatter(X_test[:,0], y_test,  color='black')
    #plt.plot(x, y, label= 'Logistic Regression', color='red')

    #plt.legend()
    #plt.show()

    plt.figure(figsize=(9,9))
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
    plt.ylabel('Actual label');
    plt.xlabel('Predicted label');
    all_sample_title = 'Accuracy Score: {0}'.format(score)
    plt.title(all_sample_title, size = 15)
    plt.show()

def load_obj_from_file(filename):
    with open(filename, 'rb') as in_file:
        obj = pickle.load(in_file)
    return obj


def main():
    X = load_obj_from_file("X.pkl")
    Y = load_obj_from_file("Y.pkl")
    
    X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.33,random_state=50)

    build_regression(X_train,X_test,y_train,y_test)



if __name__ == '__main__':
    main()

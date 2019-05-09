import pickle
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import numpy as np


def build_naive_bayes(X, y):
    # 10 folder cross validation to estimate the best w and b
    svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
                       param_grid={"C": [1,2]})
    svr.fit(X, y)

    print "Best accuracy: "
    print svr.best_score_

    return svr


def save_obj_to_file(obj, filename):
    with open(filename, 'wb') as out_file:
        pickle.dump(obj, out_file)


def load_obj_from_file(filename):
    with open(filename, 'rb') as in_file:
        obj = pickle.load(in_file)
    return obj


def main():
    X = load_obj_from_file("X.pkl")
    Y = load_obj_from_file("Y.pkl")
    build_naive_bayes(X, Y)


if __name__ == '__main__':
    main()

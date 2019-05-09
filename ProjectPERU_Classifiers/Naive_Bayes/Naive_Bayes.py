import pickle
from sklearn import naive_bayes
from sklearn.model_selection import GridSearchCV


def build_naive_bayes(X, y):
    # 10 folder cross validation to estimate the best w and b
    mnnb = naive_bayes.MultinomialNB()
    clf = GridSearchCV(estimator=mnnb, param_grid={'alpha': (1e-2, 1e-3)}, cv=10)
    clf.fit(X, y)

    print "The estimated w: "
    print clf.best_estimator_.coef_

    print "The estimated b: "
    print clf.best_estimator_.intercept_

    print "The estimated C after the grid search for 10 fold cross validation: "
    print clf.best_params_

    print "Best accuracy: "
    print clf.best_score_

    return clf


def save_obj_to_file(obj, filename):
    with open(filename, 'wb') as out_file:
        pickle.dump(obj, out_file)


def load_obj_from_file(filename):
    with open(filename, 'rb') as in_file:
        obj = pickle.load(in_file)
    return obj


def main():
    X = load_obj_from_file("X_3.pkl")
    Y = load_obj_from_file("Y_3.pkl")
    build_naive_bayes(X, Y)


if __name__ == '__main__':
    main()


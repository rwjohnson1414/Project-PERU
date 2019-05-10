import pickle
from sklearn import svm
from sklearn.model_selection import GridSearchCV


def build_svm(X, y):
    # 10 folder cross validation to estimate the best w and b
    svc = svm.SVC(kernel='linear')
    Cs = range(1,2)
    clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv=10)
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
    X = load_obj_from_file("X_all.pkl")
    Y = load_obj_from_file("Y.pkl")
    build_svm(X,Y)


if __name__ == '__main__':
    main()


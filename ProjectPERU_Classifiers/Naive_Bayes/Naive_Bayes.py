import pickle
from sklearn import naive_bayes
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

def build_naive_bayes(X_train, X_test, y_train, y_test):
    # 10 folder cross validation to estimate the best w and b
    mnnb = naive_bayes.MultinomialNB()
    clf = GridSearchCV(estimator=mnnb, param_grid={'alpha': (1e-2, 1e-3)}, cv=10)
    clf.fit(X_train,y_train)
    predictions = clf.predict(X_test)
    score = clf.score(X_test, y_test)
    cm = metrics.confusion_matrix(y_test, predictions)

    print ("The estimated w: ")
    print (clf.best_estimator_.coef_)

    print ("The estimated b: ")
    print (clf.best_estimator_.intercept_)

    print ("The estimated C after the grid search for 10 fold cross validation: ")
    print (clf.best_params_)

    print ("Best accuracy: ")
    print (score)#clf.best_score_

    plt.figure(figsize=(9, 9))
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r');
    plt.ylabel('Actual label');
    plt.xlabel('Predicted label');
    all_sample_title = 'Accuracy Score: {0}'.format(score)
    plt.title(all_sample_title, size=15)
    plt.show()

    #return clf


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

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=50)

    build_naive_bayes(X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    main()


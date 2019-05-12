import pickle
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import metrics


def build_neighbor(X_train, X_test, y_train, y_test):
    # 10 folder cross validation to estimate the best w and b
    k_range = list(range(1, 3))
    k_scores = []
    param_grid = dict(n_neighbors=k_range)
    #neigh = NearestNeighbors(n_neighbors=1)
    #neigh.fit(X,y)
    #NearestNeighbors(algorithm='auto', leaf_size=10)
    #nca=NeighborhoodComponentsAnalysis(random_state=50)

    knn=KNeighborsClassifier()
    knn.fit(X_train,y_train)
    clf = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
    clf.fit(X_train, y_train)
    scores = cross_val_score(knn, X_test,y_test, cv=10, scoring='accuracy')
    predictions = clf.predict(X_test)
    cm = metrics.confusion_matrix(y_test, predictions)
    # 4. append mean of scores for k neighbors to k_scores list
    score = clf.score(X_test, y_test)
    k_scores.append(scores.mean())

    #print(neigh.kneighbors_graph())
    #A = neigh.kneighbors_graph(X)
    #A.toarray()
    #print(A)

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


    #plt.plot(k_range, k_scores)
    #plt.xlabel('Value of K for KNN')
    #plt.ylabel('Cross-Validated Accuracy')
    #plt.show()

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

    build_neighbor(X_train, X_test, y_train, y_test)



if __name__ == '__main__':
    main()


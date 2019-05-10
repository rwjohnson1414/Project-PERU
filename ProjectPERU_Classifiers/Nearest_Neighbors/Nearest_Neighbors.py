import pickle
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


def build_neighbor(X, y):
    # 10 folder cross validation to estimate the best w and b
    k_range = list(range(1, 3))
    k_scores = []
    param_grid = dict(n_neighbors=k_range)
    #neigh = NearestNeighbors(n_neighbors=1)
    #neigh.fit(X,y)
    #NearestNeighbors(algorithm='auto', leaf_size=10)
    #nca=NeighborhoodComponentsAnalysis(random_state=50)

    knn=KNeighborsClassifier()
    knn.fit(X,y)
    clf = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
    clf.fit(X, y)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    # 4. append mean of scores for k neighbors to k_scores list
    k_scores.append(scores.mean())


    #print(neigh.kneighbors_graph())
    #A = neigh.kneighbors_graph(X)
    #A.toarray()
    #print(A)

    print ("The estimated w: -deleted")
    print(clf.best_estimator_)

    print ("The estimated b: -deleted")
    print(clf.best_index_)

    print ("The estimated C after the grid search for 10 fold cross validation: ")
    print (clf.best_params_)

    print ("Best accuracy: ")
    print (clf.best_score_)





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
    X = load_obj_from_file("X.pkl")
    Y = load_obj_from_file("Y.pkl")
    build_neighbor(X,Y)



if __name__ == '__main__':
    main()


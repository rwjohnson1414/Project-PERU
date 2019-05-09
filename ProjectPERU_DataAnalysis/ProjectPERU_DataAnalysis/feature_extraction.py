import re
from sklearn.feature_extraction.text import CountVectorizer
from ast import literal_eval
import pickle
import operator
import numpy as np
from nltk.corpus import stopwords


def extract_ngrams_sklearn(filename):
    file_strings = []
    # class vector
    Y = []

    with open(filename, 'r') as infile:
        for line in infile:
            class_label, text = line.split(",")
            # remove extra characters and \n
            s = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
            s = s.strip('\n')
            file_strings.append(s)
            # cast as num
            Y.append(literal_eval(class_label))

    # initialize CountVectorizer
    en_stopwords = set(stopwords.words('english'))
    my_stopwords = {'like', 'people', 'would', 'get', 'us', 'go', 'lot', 'http', 'https', 'www', 'x200b', 'lol', 'com', 'youtube', 'org', 'wikipedia'}
    all_stopwords = en_stopwords.union(my_stopwords)
    vectorizer = CountVectorizer(ngram_range=(3, 3), analyzer='word', stop_words=all_stopwords, max_features=100)
    # feature matrix
    X = (vectorizer.fit_transform(file_strings)).toarray()
    # list of features
    features_vector = vectorizer.get_feature_names()

    # create feature frequency dict (key = feature, value = frequency)
    frequencies_vector = (X.sum(axis=0))
    feature_frequencies = zip(features_vector, frequencies_vector)
    frequencies_dict = {f:freq for f,freq in feature_frequencies}

    # dump objects to files
    save_obj_to_file(Y, "Y_3.pkl")
    save_obj_to_file(features_vector, "features_3.pkl")
    save_obj_to_file(X, "X_3.pkl")
    save_obj_to_file(frequencies_dict, "frequencies_3.pkl")


def save_obj_to_file(obj, filename):
    with open(filename, 'wb') as out_file:
        pickle.dump(obj, out_file)


def load_obj_from_file(filename):
    with open(filename, 'rb') as in_file:
        obj = pickle.load(in_file)
    return obj


def main():
    extract_ngrams_sklearn("meaningfulData.txt")

    features_vector = load_obj_from_file("features_3.pkl")
    # print features_vector

    X = load_obj_from_file("X_3.pkl")
    # print X
    print np.array(X).shape
    Y = load_obj_from_file("Y_3.pkl")
    # print X
    print np.array(Y).shape

    frequencies_dict = load_obj_from_file("frequencies_3.pkl")
    # print frequencies_dict
    sorted_dict = sorted(frequencies_dict.items(), key=operator.itemgetter(1), reverse=True)
    for line in sorted_dict:
        print line


if __name__ == '__main__':
    main()

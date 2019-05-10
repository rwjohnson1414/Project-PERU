import re
from sklearn.feature_extraction.text import CountVectorizer
from ast import literal_eval
from numpy.core import multiarray
import pickle
import operator
import numpy as np
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


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
    vectorizer = CountVectorizer(ngram_range=(1, 1), analyzer='word', stop_words=all_stopwords, max_features=100)
    
    # feature matrix
    X = (vectorizer.fit_transform(file_strings)).toarray()
   
   # list of features
    features_vector = vectorizer.get_feature_names()

    # create feature frequency dict (key = feature, value = frequency)
    frequencies_vector = (X.sum(axis=0))
    feature_frequencies = zip(features_vector, frequencies_vector)
    frequencies_dict = {f:freq for f,freq in feature_frequencies}

    # dump objects to files
    save_obj_to_file(Y, "Y.pkl")
    save_obj_to_file(features_vector, "features.pkl")
    save_obj_to_file(X, "X.pkl")
    save_obj_to_file(frequencies_dict, "frequencies.pkl")


def save_obj_to_file(obj, filename):
    with open(filename, 'wb') as out_file:
        pickle.dump(obj, out_file)


def load_obj_from_file(filename):
    with open(filename, 'rb') as in_file:
        obj = pickle.load(in_file)
    return obj


def combine_ngrams():
    X = load_obj_from_file("X.pkl")
    X = np.array(X)
    print X.shape
    X_2 = np.array(load_obj_from_file("X_2.pkl"))
    print X_2.shape
    X_3 = np.array(load_obj_from_file("X_3.pkl"))
    print X_3.shape
    X_all = np.concatenate((X, X_2), axis=1)
    X_all = np.concatenate((X_all, X_3), axis=1)
    print X_all.shape
    save_obj_to_file(X_all, "X_all.pkl")
    frequencies_dict = {}
    frequencies_dict.update(load_obj_from_file("frequencies.pkl"))
    frequencies_dict.update(load_obj_from_file("frequencies_2.pkl"))
    frequencies_dict.update(load_obj_from_file("frequencies_3.pkl"))
    print len(frequencies_dict)
    save_obj_to_file(frequencies_dict, "frequencies_all.pkl")
    sorted_dict = sorted(frequencies_dict.items(), key=operator.itemgetter(1), reverse=True)
    for line in sorted_dict:
        print line


def boxplot(numbers, ylabel, title):
    objects = []
    performance = []
    for object, p in numbers[0:10]:
        objects.append(object)
        performance.append(p)
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.show()
    plt.clf()


def visualize():
    freq_dict = load_obj_from_file("frequencies.pkl")
    sorted_dict = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)

    boxplot(sorted_dict, "frequency", "unigram features")

def main():
    # extract_ngrams_sklearn("meaningfulData.txt")
    # combine_ngrams()
    visualize()


if __name__ == '__main__':
    main()


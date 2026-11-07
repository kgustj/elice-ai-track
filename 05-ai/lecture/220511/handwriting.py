import numpy as np
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from visual import *
import warnings

np.random.seed(100)
warnings.filterwarnings(action="ignore")


def load_data(X, Y):
    X_train = X[:1600]
    Y_train = Y[:1600]

    X_test = X[1600:]
    Y_test = Y[1600:]

    return X_train, Y_train, X_test, Y_test


def train_MLP_classifier(X, Y):
    clf = MLPClassifier(hidden_layer_sizes=(20, 20))
    clf.fit(X, Y)
    return clf


def report_clf_stats(clf, X, Y):
    hit = 0
    miss = 0

    for x, y in zip(X, Y):
        if clf.predict([x])[0] == y:
            hit += 1
        else:
            miss += 1

    score = float(100 * (hit / (hit + miss)))
    print("Accuracy: %.1lf%% (%d hit / %d miss)" % (score, hit, miss))


def main():
    digits = load_digits()

    X = digits.data
    Y = digits.target

    X_train, Y_train, X_test, Y_test = load_data(X, Y)
    clf = train_MLP_classifier(X_train, Y_train)
    return report_clf_stats(clf, X_test, Y_test)


if __name__ == "__main__":
    main()

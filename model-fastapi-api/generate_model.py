import pathlib

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import joblib


def main():
    iris_dataset = load_iris()

    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset["data"], iris_dataset["target"], random_state=0
    )

    kn = KNeighborsClassifier(n_neighbors=1)
    kn.fit(X_train, y_train)
    joblib.dump(kn, pathlib.Path(__file__).parent.joinpath("models", "clf_iris.joblib"))


if __name__ == '__main__':
    main()

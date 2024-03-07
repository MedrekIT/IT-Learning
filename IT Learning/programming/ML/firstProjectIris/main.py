import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    iris_dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
    iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
    grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20},
                                     s=60, alpha=0.8, cmap=mglearn.cm3)
    plt.show()
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    X_new = np.array([[5, 2.9, 1, 0.2]])
    prediction = knn.predict(X_new)
    print(prediction, iris_dataset['target_names'][prediction])
    y_pred = knn.predict(X_test)
    print(y_pred)
    print(y_test)
    print('{:.2f}'.format(np.mean(y_pred == y_test)))

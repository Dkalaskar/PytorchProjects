import numpy as np
from sklearn import datasets
iris = datasets.load_iris()

def IrisData(): 
    X = iris.data[:5]
    Y = iris.target[:5]
    return {'X':X,'Y': Y}

X, Y = IrisData()
print(X)
print(Y)



#training knn classification on whole dataset
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import pickle 

df = pd.read_csv('datasets/numerical_plants.csv')

y = df.iloc[:,0].values
X = df.iloc[:,1:].values

classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski')
classifier.fit(X,y)

filename = 'content/knn_classifier.svn'
pickle.dump(classifier, open(filename, 'wb'))
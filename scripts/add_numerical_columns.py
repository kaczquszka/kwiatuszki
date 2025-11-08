import pandas as pd
df = pd.read_csv("datasets/plants.csv", encoding = "latin1")

#TO DO
#skrypt ktory dodaje numeryczne kolumny tworzac ostateczny csv na ktorym wytrenujemy knn
#WAZNE!!!!
#skrypt musi zachowac kolejnosc kolumn tak jak startowy dataset, czyli numeryczne wartosci sa w kolejnosci: growth, soil, sunlight, watering fertilizer
#numeryczne moga byc : num_growth etc.

#docelowo jeden skrypt ktory robi calosc - datacleanisng itd i zwraca model albo model osobno? nie wiem
# w main ipynb mozna dac logike po kolei

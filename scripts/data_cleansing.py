import pandas as pd
import numpy as np

df = pd.read_csv("datasets/plants.csv", encoding = "latin1")

#drop duplicates of plant entry
df = df.drop_duplicates(subset=df.columns[0], keep='first')

#fix spelling mistake in watering column
#TO DO:
#wszystko do malych liter i potem capital pierwsze?
df['Watering'][df["Watering"]=="Regular watering"]="Regular Watering"

#drop duplicates of the same values in every column (to avoid having plants with identical attributes)
df = df.drop_duplicates(subset=df.columns[1:], keep='first')

df.to_csv('datasets/cleaned_plants.csv', index=False)
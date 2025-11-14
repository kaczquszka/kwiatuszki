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

df_numerical = pd.DataFrame()

#from loves water to doesnt
watering = [
    "Keep soil consistently moist",
    "Keep soil evenly moist",
    "Keep soil moist",
    "Keep soil slightly moist",
    "Regular, moist soil",
    "Regular Watering",
    "Regular, well-drained soil",
    "Water weekly",
    "Water when soil feels dry",
    "Water when topsoil is dry",
    "Water when soil is dry",
    "Let soil dry between watering"
]

#from good diet to bad
fertilization =[
    "Balanced",
    "Organic",
    "No",
    "Low-nitrogen",
    "Acidic"
]

#from fast learing to slow
growth=[
    "fast",
    "moderate",
    "slow"
]

#from universal - extravert to indiviudal small friend group
soil = [
    "loamy",
    "moist",
    "well-drained",
    "sandy",
    "acidic"
]

#loves sun to hate it
dict ={
'sun' :['full sunlight',
    'partial sunlight',
     'indirect sunlight'
]}

for column_name in df.columns[1:]:
    print(column_name)

level = np.linspace(1,-1,len(moisture_levels))
mapping = dict(zip(moisture_levels,level))
mapping

df_numerical['Watering']=df["Watering"].map(mapping)

df.to_csv('datasets/cleaned_plants.csv', index=False)
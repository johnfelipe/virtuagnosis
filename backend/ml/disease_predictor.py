import numpy as np
import pandas as pd
import json


df = pd.read_csv("final_disease_data.csv")
df.columns = df.columns.str.strip()
df.pop("Unnamed: 0")


with open("ml/symptoms.json","r") as file:
    symptoms = json.loads(file.read())

with open("ml/diseases.json","r") as file:
    diseases_data = json.loads(file.read())


def vectorize_symptoms(user_symptoms):
    return np.array([1 if symp in user_symptoms else 0 for symp in symptoms])


def find_closest_diseases(diseases):
    disease_feature_vector = vectorize_symptoms(diseases)
    arr = df.loc[:, df.columns != 'Disease'].to_numpy()
    common = disease_feature_vector * arr
    points = np.sum(common, axis = 1)
    closest_five_df = df.loc[points.argsort()[::-1][:5]]
    d_names = [name for name in closest_five_df["Disease"]]
    return {name : diseases_data[name] for name in d_names}



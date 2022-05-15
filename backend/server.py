from flask import Flask, request, send_from_directory
from ml.disease_predictor import find_closest_diseases
import json

app = Flask(__name__)

STATIC_PATH = "../public"

@app.route("/")
def base():
    return send_from_directory(STATIC_PATH, 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory(STATIC_PATH, path)

@app.route("/symptoms",methods=["GET"])
def symptoms():
    with open("./ml/symptoms.json","r") as file:
        symptoms = json.loads(file.read())
    return {"data":symptoms},200

@app.route("/diseaseinfo",methods=["GET"])
def disease_info():
    with open("./ml/diseases.json","r") as file:
        disease_info = json.loads(file.read())
    return disease_info,200

@app.route("/bodyparts",methods=["GET"])
def bodyparts():
    body_part_data = {}
    with open("arm.txt","r") as file:
        body_part_data["arms"] = file.read().splitlines()
    
    with open("face.txt","r") as file:
        body_part_data["face"] = file.read().splitlines()

    with open("head.txt","r") as file:
        body_part_data["head"] = file.read().splitlines()
    
    with open("legs.txt","r") as file:
        body_part_data["legs"] = file.read().splitlines()
        
    with open("lower-body.txt","r") as file:
        body_part_data["lower_body"] = file.read().splitlines()
    
    with open("upper-body.txt","r") as file:
        body_part_data["upper_body"] = file.read().splitlines()
        
    return body_part_data,200
        
@app.route("/predict",methods=["POST"])
def predict_disease():
    if request.method == "POST":
        request_data = request.get_json()
        symptoms = request_data["symptoms"]
        results = find_closest_diseases(symptoms)
        return results,200
    else:
        return {"status":"this endpoint does not support GET requests, please try again!"},401
    
        

if __name__ == "__main__":
    app.run(debug=True)
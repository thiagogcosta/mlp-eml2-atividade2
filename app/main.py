from flask import Flask, request
import pandas as pd
import joblib

def model_predict(amt:str, merchant_1:str, merchant_2: str, category: str, year: str, city_pop: str):
    
    df = pd.DataFrame(
        {
            'amt': [amt],
            'merchant_1': [merchant_1],
            'merchant_2': [merchant_2],
            'category': [category],
            'year': [year],
            'city_pop': [city_pop],

        }
    )
    scaler = joblib.load('./data/scaler.sav')

    df = scaler.transform(df)

    model = joblib.load('./data/rf_modelo_identificacao_fraud.sav')

    return model.predict(df)[0]

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    response = "Invalid response!"
    
    if request.method == 'GET':
        amt = request.args.get("amt")
        merchant_1 = request.args.get("merchant_1")
        merchant_2 = request.args.get("merchant_2")
        category = request.args.get("category")
        year = request.args.get("year")
        city_pop = request.args.get("city_pop")

        if model_predict(amt, merchant_1, merchant_2, category, year, city_pop):
            response = "It is a fraud!"
        else:
            response = "It is not a fraud!"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
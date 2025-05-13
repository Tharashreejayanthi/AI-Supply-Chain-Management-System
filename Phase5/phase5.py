from fastapi import FastAPI
import pandas as pd
import random

app = FastAPI()

inventory_db = {
    "P001": 120,
    "P002": 80,
    "P003": 45,
}

def predict_demand(product_id: str):
    day_of_week = random.randint(0, 6)
    marketing_spend = random.randint(100, 1000)
    holiday = random.choice([0, 1])
    sample_data = pd.DataFrame({
        'day_of_week': [day_of_week],
        'marketing_spend': [marketing_spend],
        'holiday': [holiday]
    })
    prediction = 100 + day_of_week * 10 + marketing_spend * 0.05 - holiday * 20
    return round(prediction)

def get_inventory_status():
    return inventory_db

def update_inventory(product_id: str, quantity: int):
    if product_id in inventory_db:
        inventory_db[product_id] += quantity
    else:
        inventory_db[product_id] = quantity
    return {product_id: inventory_db[product_id]}

def get_iot_data():
    return {
        "temperature": round(random.uniform(15.0, 25.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "location": "Warehouse A"
    }

@app.get("/")
def read_root():
    return {"message": "AI Supply Chain Management API"}

@app.get("/predict-demand/")
def demand_prediction(product_id: str):
    prediction = predict_demand(product_id)
    return {"product_id": product_id, "forecasted_demand": prediction}

@app.get("/inventory/")
def inventory_status():
    return get_inventory_status()

@app.post("/inventory/update/")
def inventory_update(product_id: str, quantity: int):
    return update_inventory(product_id, quantity)

@app.get("/iot/")
def get_iot_status():
    return get_iot_data()

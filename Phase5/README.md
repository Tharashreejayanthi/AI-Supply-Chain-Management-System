# AI Supply Chain API (Phase 5)

## Description
This is a FastAPI-based backend for a supply chain management system. It provides endpoints for:
- Predicting demand
- Checking and updating inventory
- Retrieving IoT sensor data

## How to Run

Install dependencies:

```bash
pip install fastapi uvicorn pandas
```

Run the server:

```bash
uvicorn phase5_fastapi_app:app --reload
```

Visit API docs at:
```
http://127.0.0.1:8000/docs
```

## Endpoints

- `GET /` – Root
- `GET /predict-demand/` – Predict demand for a product
- `GET /inventory/` – View current inventory
- `POST /inventory/update/` – Update inventory quantity
- `GET /iot/` – Simulated IoT status

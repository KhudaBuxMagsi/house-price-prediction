# California House Price Prediction API
<div align="center">

# California House Price Prediction API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

A production-ready ML API for predicting California house prices.

</div>
A production-ready ML API that predicts California house prices using a trained RandomForestRegressor, served with FastAPI.

## Features

- 🏠 **Single prediction** — POST house features, get a price
- 📄 **Batch prediction** — Upload a CSV, download results with predictions
- ⚡ **Concurrent-safe** — Model runs in a threadpool, event loop stays free
- 🧪 **Load tested** — Verified with Locust for concurrent users
- 🐳 **Production-ready structure** — `src`-layout, separated concerns

## Tech Stack

- **Python 3.12**
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **scikit-learn** — RandomForestRegressor
- **pandas** — data handling
- **uv** — dependency management

## Project Structure

```
.
├── src/house_price/
│   ├── api/              # FastAPI app, routes, schemas
│   ├── model/            # Model loading logic
│   └── config.py         # Paths and settings
├── models/               # Trained .joblib artifacts
├── scripts/              # Training, exploration, load tests
├── tests/                # pytest tests
└── notebooks/            # EDA notebooks
```

## Quick Start

### 1. Install dependencies

```bash
uv sync
```

### 2. Run the API

```bash
uv run uvicorn house_price.api.main:app --reload --app-dir src
```

API will be available at `http://localhost:8000`.

### 3. Explore the docs

Open `http://localhost:8000/docs` for interactive Swagger UI.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Home |
| GET | `/health` | Health check |
| POST | `/predict` | Single house price prediction |
| POST | `/predict-csv` | Batch prediction from CSV |

### Example: Single Prediction

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3252,
    "HouseAge": 41,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'
```

**Response:**

```json
{
  "predicted_price": "$430,217",
  "predicted_price_short": "$4.30 hundred thousands",
  "finance_range": "$393,217 to $430,217"
}
```

### Example: Batch Prediction

```bash
curl -X POST http://localhost:8000/predict-csv \
  -F "file=@test.csv" \
  -o predictions.csv
```

## Training the Model

```bash
uv run python scripts/train.py
```

The trained model and feature list are saved to `models/`.

## Load Testing

```bash
uv run locust -f scripts/load_test.py --host=http://localhost:8000
```

Open `http://localhost:8089` to configure the test.

## License

MIT

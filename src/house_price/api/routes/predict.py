from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
import pandas as pd
import io
from fastapi import File, UploadFile
from fastapi.responses import StreamingResponse
from house_price.model.loader import get_model, get_features  
from house_price.api.schemas import HouseFeatures
from house_price.model.loader import get_model

router = APIRouter(tags=["predict"])


@router.post("/predict")
async def predict(house: HouseFeatures):
    try:
        input_data = pd.DataFrame([{
            "MedInc":     house.MedInc,
            "HouseAge":   house.HouseAge,
            "AveRooms":   house.AveRooms,
            "AveBedrms":  house.AveBedrms,
            "Population": house.Population,
            "AveOccup":   house.AveOccup,
            "Latitude":   house.Latitude,
            "Longitude":  house.Longitude,
        }])

        model = get_model()
        predicted = (await run_in_threadpool(model.predict, input_data))[0]
        price_usd = predicted * 100_000

        return {                                       # ← THE LINE TO CHECK
            "predicted_price": f"${price_usd:,.0f}",
            "predicted_price_short": f"${predicted:.2f} hundred thousands",
            "finance_range": f"${price_usd - 37000:,.0f} to ${price_usd:,.0f}",
        }
    except Exception as e:
        raise HTTPException(500, f"prediction failed: {str(e)}")




@router.post("/predict-csv")
async def predict_csv(file: UploadFile = File(...)):
    # 1. Validate file type
    if file.content_type not in {
        "text/csv",
        "application/vnd.ms-excel",
        "application/octet-stream",
    }:
        raise HTTPException(400, f"Expected CSV, got {file.content_type}")

    # 2. Read + parse
    content = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(content))
    except Exception as e:
        raise HTTPException(400, f"Could not parse CSV: {str(e)}")

    # 3. Validate required columns
    features = get_features()
    missing = set(features) - set(df.columns)
    if missing:
        raise HTTPException(422, f"CSV missing columns: {sorted(missing)}")

    # 4. Predict
    try:
        model = get_model()
        X = df[features]
        predictions = await run_in_threadpool(model.predict, X)
    except Exception as e:
        raise HTTPException(500, f"Prediction failed: {str(e)}")

    # 5. Add prediction columns
    df["predicted_price"] = predictions * 100_000
    df["predicted_price_formatted"] = df["predicted_price"].apply(
        lambda x: f"${x:,.0f}"
    )

    # 6. Return as downloadable CSV
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"},
    )
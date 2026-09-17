from fastapi import FastAPI
from contextlib import asynccontextmanager
from house_price.model.loader import load_model
from house_price.api.routes import health, predict

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(health.router)
app.include_router(predict.router)
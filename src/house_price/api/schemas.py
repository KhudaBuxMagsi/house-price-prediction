from pydantic import BaseModel, Field

class HouseFeatures(BaseModel):
    MedInc:     float = Field(gt=0)
    HouseAge:   float = Field(gt=0)
    AveRooms:   float = Field(gt=0)
    AveBedrms:  float = Field(gt=0)
    Population: float = Field(gt=0)
    AveOccup:   float = Field(gt=0)
    Latitude:   float = Field(ge=32, le=42)
    Longitude:  float = Field(ge=-125, le=-114)
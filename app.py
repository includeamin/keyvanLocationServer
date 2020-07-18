from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class CoordinateModel(BaseModel):
    latitude: float
    longitude: float


class LocationModel(BaseModel):
    username: str
    coordinate: CoordinateModel


class UpdateResponseModel(BaseModel):
    result: List[LocationModel]


client_data: List[LocationModel] = []


@app.post("/update", description="update location", status_code=200, response_model=UpdateResponseModel)
async def update_location(username: str, latitude: float, longitude: float):
    try:
        item = next(item for item in client_data if item.username == username)
        client_data[client_data.index(item)].coordinate = CoordinateModel(latitude=latitude, longitude=longitude)
    except StopIteration:
        client_data.append(
            LocationModel(username=username, coordinate=CoordinateModel(latitude=latitude, longitude=longitude)))
    return UpdateResponseModel(result=client_data)

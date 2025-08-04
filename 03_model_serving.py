from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

def predict_iris(data: IrisInput) -> Literal["setosa", "versicolor", "virginica"]:
    if data.petal_length < 2:
        return "setosa"
    elif data.petal_length > 5:
        return "versicolor"
    else:
        return "virginica"

@app.post("/predict-iris")
def predict_species(iris: IrisInput):
    prediction = predict_iris(iris)
    return {
        "input": iris,
        "prediction": prediction
    }

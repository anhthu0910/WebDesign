from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class HouseInput(BaseModel):
    area: float
    bedrooms: int
    location: str = "other"

def predict_price(area: float, bedrooms: int, location: str) -> float:
    base_price = 500000000
    price = base_price + (area * 15000000)
    price += bedrooms * 50000000
    
    if location.lower() == "hanoi":
        price *= 1.3
    elif location.lower() == "hcmc":
        price *= 1.25    
        
    # Round the final result to the nearest million VND.
    price = round(price / 1000000) * 1000000
    return price

@app.get("/predict")
# Use def instead of async def because 
# the predict function performs synchronous calculations and 
# does not involve any I/O-bound operations that would benefit from asynchronous execution.
def predict(area: float, bedrooms: int, location: str = "other"):
    predicted_price = predict_price(area, bedrooms, location)
    return {
        "area": area, 
        "bedrooms": bedrooms,
        "location": location,
        "predicted_price": predicted_price
    }


@app.post("/predict")
def predict_from_body(house: HouseInput):
    predicted_price = predict_price(house.area, house.bedrooms, house.location)
    return {
        "area": house.area,
        "bedrooms": house.bedrooms,
        "location": house.location,
        "predicted_price": predicted_price,
    }
    

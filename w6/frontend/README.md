# Week 06 Assignment — Mini House-Price Prediction API

## 1. How to run this project

Open a terminal in the `w6/backend` directory and install the dependencies:

```bash
cd w6/backend
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/static/house_form.html` in a browser to use the form.

## 2. Answers to Task 3:

### 2.1 Explain why calling `/predict` without `location` still works

Calling `/predict` without `location` works because both endpoints define a default value:
- GET endpoint: `location="other"`
- POST model: `location: str = "other"`
When `location` is omitted, FastAPI automatically uses `"other"`. In `predict_price()`, only `"hanoi"` and `"hcmc"` apply special multipliers. Any other value, including `"other"`, uses the base price without an extra location adjustment.

### 2.2 Explain why calling `/predict` without `area` gets a 422 error

Calling `/predict` without `area` returns `422 Unprocessable Entity` because `area` is required in both endpoint definitions:

```python
def predict(area: float, bedrooms: int, location="other"):
```

and:

```python
class HouseInput(BaseModel):
    area: float
    bedrooms: int
    location: str = "other"
```

Only `location` has a default value. Since FastAPI cannot calculate the price without an area, it rejects the request during validation before the function runs. A `422` response indicates invalid or incomplete request data, not a server crash.

## 3. Answers to Task 5:

### Why does a relative URL work?

The code uses a relative URL here:

```javascript
fetch(`/predict?${query}`)
```

A relative URL does not specify a hostname or port. The browser automatically attaches the current page’s origin.

For example, if the form is opened at:

```text
http://127.0.0.1:8000/static/house_form.html
```

then the request is sent to:

```text
http://127.0.0.1:8000/predict
```

This works because the frontend and FastAPI backend are served from the same host and port. It avoids hardcoding a hostname such as `http://localhost:8000`.

The page must be opened through the FastAPI server. Opening `house_form.html` directly with a `` URL would not work correctly with `/predict`.

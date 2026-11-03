# Airline Passenger Satisfaction Prediction API

An end-to-end Machine Learning project that predicts whether an airline passenger is satisfied or dissatisfied based on their flight experience. The model is served via a FastAPI backend and is fully containerized with Docker for production deployment.

## Architecture & Tech Stack
*   **Machine Learning:** `scikit-learn`, `pandas`, `numpy`
*   **Web Framework:** `FastAPI`, `Pydantic`
*   **Dependency Management:** `uv`
*   **Containerization:** `Docker`
*   **Model Serialization:** `joblib`

## How to Run Locally (Without Docker)

**1. Install dependencies:**
This project uses `uv` for lightning-fast dependency management.
```bash
uv sync
```

**2. Start the API server:**
```bash
uv run uvicorn app.main:app --reload
```

or

```bash
uv run fastapi dev --reload
```

**3. Access the API:**
*   **Interactive Swagger UI:** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the model directly in your browser.
*   **Direct Endpoint:** `POST http://127.0.0.1:8000/prediction`

---

## How to Run with Docker (Production)

**1. Build the Docker image:**
```bash
docker build -t airline-api:v1.0 .
```

**2. Run the container:**
```bash
docker run -p 8000:8000 airline-api:v1.0
```

**3. Access the API:**
Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser. 

---

## API Usage Example

You can test the endpoint using a `curl` request. Note that the API expects the specific data structure defined in the `Observation` Pydantic schema.

```bash
curl -X POST http://127.0.0.1:8000/prediction \
  -H "Content-Type: application/json" \
  -d '{
    "id": 70172,
    "Gender": "Female",
    "Customer_Type": "Loyal Customer",
    "Age": 35,
    "Type_of_Travel": "Business travel",
    "Class": "Business",
    "Flight_Distance": 1200,
    "Inflight_wifi_service": 5,
    "Departure_Arrival_time_convenient": 4,
    "Ease_of_Online_booking": 5,
    "Gate_location": 4,
    "Food_and_drink": 5,
    "Online_boarding": 5,
    "Seat_comfort": 4,
    "Inflight_entertainment": 5,
    "On_board_service": 5,
    "Leg_room_service": 4,
    "Baggage_handling": 5,
    "Checkin_service": 4,
    "Inflight_service": 5,
    "Cleanliness": 5,
    "Departure_Delay_in_Minutes": 0,
    "Arrival_Delay_in_Minutes": 0
  }'
```

**Response:**
```json
{
  "prediction": "satisfied"
}
```

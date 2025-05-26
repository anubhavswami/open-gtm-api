# ⚡ Open GTM API

This is the backend API for the **Open GTM Strategy Service** — a tool that helps early-stage startups determine the most suitable Go-To-Market (GTM) strategy based on a short questionnaire.

Built with [FastAPI](https://fastapi.tiangolo.com/) for speed, flexibility, and ease of integration with the React frontend (`open-gtm-ui`).

---

## 🧩 What This Does

- Accepts GTM-related questionnaire responses via POST request
- Maps inputs to a GTM strategy (e.g. Sales-led, PLG, Community-led)
- Returns a simple JSON response
- Includes CORS setup for integration with frontend at `http://localhost:3000`

---

## 📦 Folder Structure

open-gtm-api/
├── main.py # FastAPI app entry point
├── models.py # Pydantic request/response models
├── logic.py # GTM framework suggestion logic
└── requirements.txt # Dependencies

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/anubhavswami/open-gtm-api.git
cd open-gtm-api

2. Install dependencies(bash)
python3 -m pip install -r requirements.txt
3. Start the API server
bash
Copy
Edit
python3 -m uvicorn main:app --reload
Visit:

Swagger docs: http://localhost:8000/docs

Root check: http://localhost:8000

📬 Example Request(http)

POST /suggest
Content-Type: application/json

{
  "audience": "Enterprises",
  "growth": "Community",
  "pricing": "Freemium"
}
Response:(json)

{
  "framework": "Sales-led GTM"
}

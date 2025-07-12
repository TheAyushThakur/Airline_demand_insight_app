✈️ Airline Demand Insight App

A lightweight web application that provides insights into airline route popularity and fare trends using AI-generated summaries. It uses Flask as the backend and integrates with Groq's `llama3-70b-8192` model to generate summaries. Optionally, a Streamlit frontend can be added for quick UI testing.

---

## 🚀 Features

- 📊 Analyzes most popular airline routes
- 📈 Detects fare trends across routes
- 🤖 Summarizes key insights using LLaMA 3 (Groq API)
- 🌐 Built with Flask (backend) and optionally Streamlit (frontend)
- 🔐 API key and configuration via `.env`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/airline-demand-app.git
cd airline-demand-app

### 2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
 or
source venv/bin/activate   # On macOS/Linux
### 3. Install Required Packages
pip install -r requirements.txt
### 4. Set Up Environment Variables
Create a .env file in the root directory and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

### 5. Running the Flask Server
python flask_server.py
By default, the API will be hosted at http://localhost:5000

### 6. API Endpoint
POST /api/get_insights
Request Format:
json
{

}
(This API generates the summary from precomputed route and trend data.)

Response:
json
{
  "routes": {...},
  "trends": {...},
  "summary": "Top routes include ..."
}
### 7. Run Streamlit App (If Added)
streamlit run app.py
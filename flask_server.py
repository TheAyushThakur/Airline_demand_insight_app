# flask_server.py
from flask import Flask, jsonify
from scraper import fetch_airline_data
from processor import process_data
from ai_insight import generate_insight_summary
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

@app.route('/api/data')
def get_processed_data():
    df = fetch_airline_data()
    popular_routes, price_trends = process_data(df)
    trends_dict = {
        str(k.date()) if hasattr(k, 'date') else str(k): v
        for k, v in price_trends.items()
    }

    routes_dict = popular_routes.to_dict()

    ai_summary = generate_insight_summary(routes_dict, trends_dict)

    response = {
        "routes": routes_dict,
        "trends": trends_dict,
        "summary": ai_summary
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# scraper.py
import pandas as pd
from datetime import datetime, timedelta
import random

def fetch_airline_data():
    routes = [
        "Sydney - Melbourne", "Brisbane - Sydney", "Perth - Adelaide", 
        "Melbourne - Gold Coast", "Sydney - Brisbane"
    ]
    data = []

    for _ in range(100):
        route = random.choice(routes)
        price = round(random.uniform(50, 350), 2)
        date = datetime.today() - timedelta(days=random.randint(0, 30))
        data.append({"route": route, "price": price, "date": date.strftime("%Y-%m-%d")})

    return pd.DataFrame(data)

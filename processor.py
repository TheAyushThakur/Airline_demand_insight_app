import pandas as pd
def process_data(df):
    df['date'] = pd.to_datetime(df['date'])
    popular_routes = df['route'].value_counts().head(5)
    price_trends = df.groupby('date')['price'].mean().sort_index()
    return popular_routes, price_trends

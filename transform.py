import pandas as pd
from datetime import datetime

def transform_data(raw_data):
    data_cleaned = {
        'city': raw_data['name'],
        'temp': raw_data['main']['temp'],
        'humidity': raw_data['main']['humidity'],
        'description': raw_data['weather'][0]['description'],
        'extraction_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([data_cleaned])
    
    df['temp']= df['temp'].astype(float)
    return df
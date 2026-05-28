from extract import extract_data
from transform import transform_data
from load import load_to_bigquery

def run_pipeline(request=None): 
    API_KEY = 'e50815c90d5a1d6281815d2dc01459a6'
    PROJECT_ID = 'etl-weather-pipeline-497715'
    DATASET_ID = 'weather_data'
    TABLE_ID = 'weather_bogota'

    print("Iniciando pipeline...")
    rawjson = extract_data('Bogota', API_KEY)

    print("Transformando datos...")
    df_transformed = transform_data(rawjson)
    print("Cargando datos a BigQuery...")
    load_to_bigquery(df_transformed, PROJECT_ID, DATASET_ID, TABLE_ID)

    return "Pipeline ejecutada exitosamente!"
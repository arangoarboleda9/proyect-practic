from extract import extract_data
from transform import transform_data
from load import load_to_bigquery

def run_pipeline(request=None): 
    API_KEY = 'your_api_key'
    PROJECT_ID = 'your_project_id'
    DATASET_ID = 'your_dataset_id'
    TABLE_ID = 'your_table_id'

    print("Iniciando pipeline...")
    rawjson = extract_data('Bogota', API_KEY)

    print("Transformando datos...")
    df_transformed = transform_data(rawjson)
    print("Cargando datos a BigQuery...")
    load_to_bigquery(df_transformed, PROJECT_ID, DATASET_ID, TABLE_ID)

    return "Pipeline ejecutada exitosamente!"
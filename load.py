from google.cloud import bigquery
import pandas as pd

def load_to_bigquery(df, project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    
    # --- CORRECCIÓN AQUÍ ---
    # Busca columnas que contengan fechas y asegúrate de convertirlas
    # Si sabes el nombre exacto, cámbialo por 'nombre_de_tu_columna'
    for col in df.columns:
        # Detectamos si la columna parece ser de tipo fecha basándonos en el nombre o contenido
        if 'timestamp' in col.lower() or 'date' in col.lower():
            df[col] = pd.to_datetime(df[col])
            # Si el error persiste, intenta forzar la zona horaria UTC:
            # df[col] = pd.to_datetime(df[col]).dt.tz_localize('UTC')
    # -----------------------

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    
    print(f"Datos cargados exitosamente en: {table_ref}")
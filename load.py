from google.cloud import bigquery
import pandas as pd # Asegúrate de tener esto

def load_to_bigquery(df, project_id, dataset_id, table_id):
    # 1. Creamos el cliente
    client = bigquery.Client(project=project_id)
    
    # 2. CONVERSIÓN DE SEGURIDAD: Convertir todas las columnas tipo objeto a datetime
    # Esto soluciona el error 'Failed to parse string'
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col], utc=True)
            except (ValueError, TypeError):
                continue # Si no es fecha, lo ignoramos

    # 3. Formamos la referencia
    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    
    # 4. Configuramos la carga
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    
    # 5. Cargamos el DataFrame
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    
    print(f"Datos cargados exitosamente en: {table_ref}")
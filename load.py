from google.cloud import bigquery

def load_to_bigquery(df, project_id, dataset_id, table_id):
    # 1. Creamos el cliente de BigQuery
    client = bigquery.Client(project=project_id)
    
    # 2. Formamos la referencia de la tabla como un string completo: 'proyecto.dataset.tabla'
    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    
    # 3. Configuramos la carga para añadir datos al final (APPEND)
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    
    # 4. Cargamos el DataFrame
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Esto espera a que la operación termine
    
    print(f"Datos cargados exitosamente en: {table_ref}")
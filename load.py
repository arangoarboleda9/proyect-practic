from google.cloud import bigquery

def load_to_bigquery(df, project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    table_ref = (dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND)
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    print(f"datos cargados en BigQuery: {table_id}")
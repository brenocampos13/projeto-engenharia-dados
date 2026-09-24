from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

def inicio():
    print("Início")

def processamento():
    print("Processando dados")

def fim():
    print("Fim")

with DAG(
    dag_id="dag_python_operator",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:


    extract = PythonOperator(
        task_id="extract",
        python_callable=inicio
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=processamento
    )

    load = PythonOperator(
        task_id="load",
        python_callable=fim
    )

    extract >> transform >> load
from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    dag_id="ETL_Projeto",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract_load",
        bash_command="python /projeto/main.py"
    )

    extract
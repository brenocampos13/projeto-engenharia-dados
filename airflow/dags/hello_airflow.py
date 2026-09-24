from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    inicio = BashOperator(
        task_id="inicio",
        bash_command='echo "Início da DAG"'
    )

    ola = BashOperator(
        task_id="meio",
        bash_command='echo "Olá Breno, sua primeira DAG está funcionando!"'
    )

    fim = BashOperator(
        task_id="fim",
        bash_command='echo "Fim da DAG"'
    )

    inicio >> ola >> fim
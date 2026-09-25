from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

with DAG(
    dag_id="ELT_Projeto",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    seed = DockerOperator(
        task_id="seed_oltp",
        image="etl_app:latest",
        command="python seed_oltp.py",
        auto_remove="success",
        network_mode="projetoengenhariadedados_default"
    )

    extract_load = DockerOperator(
        task_id="extract_load",
        image="etl_app",
        command="python main.py",
        auto_remove="success",
        network_mode="projetoengenhariadedados_default"

    )

    transform = DockerOperator(
        task_id="dbt_transform",
        image="dbt_runner:latest",
        command="dbt run",
        auto_remove="success",
        network_mode="projetoengenhariadedados_default"
    )
    
    test = DockerOperator(
        task_id="dbt_test",
        image="dbt_runner:latest",
        command="dbt test",
        auto_remove="success",
        network_mode="projetoengenhariadedados_default"
    )

    seed >> extract_load >> transform >> test
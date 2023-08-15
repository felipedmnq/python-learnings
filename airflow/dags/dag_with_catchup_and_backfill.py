from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

from airflow import DAG

default_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="dag_wit_catchup_and_backfill",
    default_args=default_args,
    start_date=datetime(2023, 8, 6, 2),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task_1 = BashOperator(
        task_id="first_task", bash_command="echo This is juist a bash command"
    )

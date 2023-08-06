from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="AA_first_dag_v2",
    description="first dag",
    default_args=default_args,
    start_date=datetime(2023, 8, 6, 2),
    schedule_interval="@daily",
) as dag:
    task_1 = BashOperator(task_id="first_task", bash_command="echo 'Hello World!'")
    task_2 = BashOperator(task_id="second_task", bash_command="echo 'second task'")

    task_1 >> task_2

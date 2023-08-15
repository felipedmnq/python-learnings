from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="dag_with_cron_expression",
    default_args=default_args,
    start_date=datetime(2023, 8, 6, 2),
    # schedule_interval="@daily",
    # schedule_interval="0 0 * * *", # every day at midnight
    # schedule_interval="0 0 * * Tue,Fri", # every Tuesday and Friday at midnight
    schedule_interval="0 0 * * Mon-Fri",  # from Monday to Friday at midnight
) as dag:
    task_1 = BashOperator(
        task_id="first_task", bash_command="echo This is juist a bash command"
    )

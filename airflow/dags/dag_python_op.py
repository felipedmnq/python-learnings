from datetime import datetime, timedelta

from airflow.models.taskinstance import TaskInstance
from airflow.operators.python import PythonOperator

from airflow import DAG

defaul_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


def return_name(first_name: str, last_name: str, ti: TaskInstance) -> str:
    ti.xcom_push(key="first_name", value=first_name)
    ti.xcom_push(key="last_name", value=last_name)


def return_age(age: int, ti: TaskInstance) -> int:
    ti.xcom_push(key="age", value=age)


def greed(ti: TaskInstance) -> None:
    first_name = ti.xcom_pull(task_ids="return_name", key="first_name")
    last_name = ti.xcom_pull(task_ids="return_name", key="last_name")
    age = ti.xcom_pull(task_ids="return_age", key="age")

    print(f"Hello, my name is {first_name} {last_name} and I am {age} years old!")


with DAG(
    default_args=defaul_args,
    dag_id="dag_python_operator_v7",
    description="dag python operator",
    start_date=datetime(2023, 8, 7, 2),
    schedule_interval="@daily",
) as dag:
    python_task_01 = PythonOperator(
        task_id="greed",
        python_callable=greed,
    )

    python_task_02 = PythonOperator(
        task_id="return_name",
        python_callable=return_name,
        op_kwargs={"first_name": "Felipe", "last_name": "Felix"},
    )

    python_task_03 = PythonOperator(
        task_id="return_age",
        python_callable=return_age,
        op_kwargs={"age": 25},
    )
    [python_task_02, python_task_03] >> python_task_01

from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


@dag(
    dag_id="dag_taskflow_v1",
    default_args=default_args,
    start_date=datetime(2023, 8, 7, 2),
)
def hello_world_etl():
    @task(multiple_outputs=True)
    def return_name(first_name: str, last_name: str) -> dict[str]:
        return {"first_name": first_name, "last_name": last_name}

    @task()
    def return_age(age: int) -> int:
        return age

    @task()
    def greed(first_name: str, last_name: str, age: int) -> None:
        print(f"Hello, my name is {first_name} {last_name} and I am {age} years old!")

    names = return_name("Felipe", "Felix")
    age = return_age(25)
    greed(first_name=names["first_name"], last_name=names["last_name"], age=age)


greed_dag = hello_world_etl()

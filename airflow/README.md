# Apache Airflow

* [DOCS](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [Instalation](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

## Basics and core concepts

* **DAG** - Directed Acyclic Graph - is the core concept of Airflow, collecting Tasks together, organized with dependencies and relationships to say how they should run.
* **TASK** - A Task is the basic unit of execution in Airflow. Tasks are arranged into DAGs, and then have upstream and downstream dependencies set between them into order to express the order they should run in.
* **OPERATOR** - Predefined tasks that you can string together quickly to build most parts of your DAGs.

The operator determines what will be done. The task implements an operator by defining specific values for that operator. a DAG is a collection of all the tasks that you want to run organized in a way that reflects their relationships and dependecies.

* **Execution date** - The logical date and time which the DAG, and its task instances, are running for. 
* **Task instance+** - It is a run of a task at a specific point in time (**Execution date**).
* **Dag run** - It is an instantiation of a DAG, containing task instances that run for a specific **execution_date**.

## airflow.cfg

* The first time you run Airflow, it will create a file called airflow.cfg in your $AIRFLOW_HOME directory (~/airflow by default). This file contains Airflow’s configuration and you can edit it to change any of the settings. 

### Task lifecycle

* There are different kinds of stages in Airflow.
    * no_status - scheduler created empty task instance
    * none - the task has not yet been queued for execution
    * scheduled - scheduler determined task dependencies to run
    * queued - scheduler sent task to executor to run and it is waiting for a worker
    * running - worker picked up a task and is now running it
    * success - the task is completed without fails
    * shutdown - the task run has been aborted when it was running
    * restarting - the task was requested to restart
    * failed - the task had an error during execution and has failed
    * skipped - the task has been skipped due to branching, LatestOnly or similar
    * upstream_failed - the upstream task failed and the trigger rule says we need it
    * up_for_retry - the task has failed but has retry attempts left and will be rescheduleed
    * up_for_reschedule - the task is a Sensor that is in reschedule mode
    * deferred - the task has been deferred to a trigger
    * removed - The task has vanished from the DAG since the run started    

![airfklow-status](airflow/images/airflow_status.png)

**HAPPY WORKFLOW**

![happy-workflow](airflow/images/happy workflow.png)

## Basic Architecture

![basic-architecture](airflow/images/basic_architecture.png)

## Airflow use

### Bash operator

- `from airflow.operators.bash import BashOperator`

* DAG CONFIGS:
```
default_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}
```

* CREATE DAG:
```
with DAG(
    dag_id="AA_first_dag_v2",
    description="first dag",
    default_args=default_args,
    start_date=datetime(2023, 8, 6, 2),
    schedule_interval="@daily",
) as dag:
```

* CREATE TASKS:
```
task_1 = BashOperator(task_id="first_task", bash_command="echo 'Hello World!'")
task_2 = BashOperator(task_id="second_task", bash_command="echo 'second task'")
task_3 = BashOperator(task_id="third_task", bash_command="echo 'THIRD TASK'")
```

* SET TASK DEPENDENCIES:
```
task_1.set_downstream(task_2)
task_1.set_downstream(task_3)
```
OR
```
task_1 >> task_2
task_1 >> task_3
```
OR
```
task_1 >> [task_2, task_3]
```

### Python operator

- `from airflow.operators.python import PythonOperator`

- To set the callable to the PythonOperator use `python_callable=<CALLABLE>`
- To set the callable parameters use `op_kwargs={<dict with args>}`


```
from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

from airflow import DAG

defaul_args = {
    "owner": "Felipe",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


def greed(name: str, age: int) -> None:
    print(f"Hello, my name is {name} and I am {age} years old!")


with DAG(
    default_args=defaul_args,
    dag_id="dag_python_operator_v2",
    description="dag python operator",
    start_date=datetime(2023, 8, 7, 2),
    schedule_interval="@daily",
) as dag:
    python_task_01 = PythonOperator(
        task_id="python_task_01",
        python_callable=greed,
        op_kwargs={"name": "Felipe", "age": 25},
    )
    python_task_01
```

### Exchange data between tasks

- Values returned by tasks are stored in `XComs`
- To pass values through airflow it is necessary to use a `TaskInstance` object and the `xcom_pull` method.
- It is also necessary to set the `key` and `value`.
- To retieve values from `XComs` it is necessary to use a `TaskInstance` object and the `xcom_push` method.
- It is also necessary to set the `task_ids` (the task that is setting the arguments) and `key`.
- WARNING - the max size of a XCom is 48KB - DO NOT WORKS WITH LARGE DATA

```
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
```

## Schedule DAGs with Cron

#### Cron expression Preset

- `none` - No schedule - exclusivelly for "externally triggered" DAGs
- `@once` - Schedule only once
- `@hourly` - Run once an hour at the beggining of the hour
- `@daily` - Run once a day at midnight
- `@weekly` - Run once a week at midnight on Sunday
- `@monthly` - Run once a month at midnight of the first day of the month
- `@yearly` - Run once a year at midnight of January 1st.

## TaskFlow API

- 

## Commands 

* Init database - `airflow db init`
* Init local server - `airflow webserver -p <PORT>`
* Create user - `airflow users create --username admin --firstname firstname --lastname lastname --role Admin --email admin@admin.com`
* Check DB - `airflow db check`
* Reset DB - `airflow db reset`
* Init scheduler - `airflow scheduler`
* Get database path - `airflow config get-value database sql_alchemy_conn`
* Database connection EnvVar - `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`
* Run DAGs "in the past" with `backfill` - `airflow dags backfill -s <START DATE - YYYY-MM-DD> -e <END DATE - YYYY-MM-DD> <DAG ID>`



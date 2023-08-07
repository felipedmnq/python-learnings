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

* There are in total 11 diffenrent kinds of stages in Airflow.
    * queued - scheduler sent task to executor to eun on the queue
    * running - worker picked up a task and is now running it
    * success - the task is completed without fails
    * failed - the task has failed
    * up_for_retry - the task will schedulled and reruned
    * up_for_reschedule - the task will be rescheduled avery certain time interval
    * upstream_failed - the upstream task failed
    * skipped - the task has been skipped
    * scheduled - scheduler determined task instance needs to run
    * no_status - scheduler created empty task instance
    * shutdown - the task run has been aborted

![airfklow-status](airflow/images/airflow_status.png)

**HAPPY WORKFLOW**

![happy-workflow](airflow/images/happy workflow.png)

## Basic Architecture

![basic-architecture](airflow/images/basic_architecture.png)

## Operators

## Airflow use

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
## Commands 

* Init database - `airflow db init`
* Init local server - `airflow webserver -p <PORT>`
* Create user - `airflow users create --username admin --firstname firstname --lastname lastname --role Admin --email admin@admin.com`
* Check DB - `airflow db check`
* Reset DB - `airflow db reset`
* Init scheduler - `airflow scheduler`
* Get database path - `airflow config get-value database sql_alchemy_conn`
* Database connection EnvVar - `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`



from pendulum import datetime

from airflow.decorators import (
    dag,
    task,
)  # DAG and task decorators for interfacing with the TaskFlow API

from airflow.hooks.base_hook import BaseHook


@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={
        "retries": 2,  # If a task fails, it will retry 2 times.
    },
    tags=["example"],
)  # If set, this tag is shown in the DAG view of the Airflow UI
def example_get_conn_attributes():
    @task()
    def print_conn():
        """
        #### Extract task
        A simple "extract" task to get data ready for the rest of the
        pipeline. In this case, getting data is simulated by reading from a
        hardcoded JSON string.
        """
        conn = BaseHook.get_connection("aws").to_dict()
        print(conn)

    print_conn()

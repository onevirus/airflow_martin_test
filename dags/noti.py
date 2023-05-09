# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    "noti",
    start_date=datetime(2023, 5, 5),
    schedule=timedelta(hours=1),
) as dag:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )
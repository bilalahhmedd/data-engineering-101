import datetime
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
	dag_id='example_bash_operator',
	schedule_interval= '0 0 * * *',
	start_date = pendulum.datetime(2022,10,14, tz='utc'),
	catchup=False,
	dagrun_timeout=datetime.timedelta(minutes=60),
	tags=['example','example2'],
	params={"example_key","example_value"}
) as dag:
    run_this_last = EmptyOperator(
        task_id='run_this_last',
    )

    # [START howto_operator_bash]
    run_this = BashOperator(
        task_id='run_after_loop',
        bash_command='echo 1',
    )
    # [END howto_operator_bash]
    task >> run_this

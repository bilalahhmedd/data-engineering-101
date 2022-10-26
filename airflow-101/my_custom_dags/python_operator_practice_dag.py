import datetime
import pendulum

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
#from ../py_scripts import hello_world

class hello_world():

    def print_hello_world():
        print('hello world')

    def print_my_world():
        print('my world')

# [End import module]
dag_1 = DAG('hello_world', start_date=datetime.datetime(2022,10,25))

'''
with DAG(
    'hello_world_dag',
    start_date=datetime.date(2022,25,10)
) as dag_1:
    t1 = PythonOperator(task_id='hello_world_task',python_callable=hello_world.print_hello_world)
    t2 = PythonOperator(task_id='my_world_task',python_callable=hello_world.print_my_world)

    t1 >> t2
'''


hello_world_task = PythonOperator(task_id='hellow_world_task',python_callable=hello_world.print_hello_world,dag=dag_1)
my_world_task = PythonOperator(task_id='my_world_task',python_callable=hello_world.print_my_world,dag=dag_1)

hello_world_task >> my_world_task

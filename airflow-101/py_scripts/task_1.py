# [Start import module]
import json
import pendulum
from airflow.decorators import dag, task

# [End import module]

@dag(
    #schedule_interval=None,
    start_date=pendulum.datetime(2022,10,14,tz='UTC'),
    catchup=False,
    tags=['taskflow_api_expample'],
)
def taskflow_api():
    @task
    def gen_data():
        return [1,2,3,4]
    @task
    def process_data(data):
        return [x**2 for x in data]
    @task
    def send_data(data):
        print(data)
    
    
    data=gen_data()
    processed_data=process_data(data)
    send_data(process_data)

taskflow_api()

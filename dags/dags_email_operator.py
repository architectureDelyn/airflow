from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="42 21 * * *",
    start_date=pendulum.datetime(2025, 3, 6, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_eamil_task = EmailOperator(
        task_id="sedn_eamil_task",
        to='wjdalsgur12@naver.com',
        subject='Airflow 성공메일',
        html_content='Airflow 작업이 완료되었습니다.'
    )

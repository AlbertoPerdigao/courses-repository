from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
 
from datetime import datetime
 
def _t1(ti):
    ti.xcom_push(key='my_key', value=42)
 
def _t2(ti):
    print(ti.xcom_pull(key='my_key', task_ids='t1'))
 
def _branch(ti):
    value = ti.xcom_pull(key='my_key', task_ids='t1')
    if (value == 42):
        return 't2'
    return 't3'

with DAG("xcom_dag", start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
 
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )
 
    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )
 
    t3 = BashOperator(
        task_id='t3',
        bash_command="echo ''"
    )

    t4 = BashOperator(
        task_id='t4',
        bash_command="echo ''",
        trigger_rule='none_failed_min_one_success' 
        # Foi preciso alterar a trigger_rule porque a trigger_rule default utilizada seria a all_success, 
        # o que obriga o t2 e o t3 retornarem sucesso, e no caso, como temos um branch operator, apenas uma task (t2 ou t3)
        # poderá ter um retorno de sucesso, o outro não é executado (skiped), fazendo com que o t4 não seja chamado.
        # Com o trigger_rule='none_failed_min_one_success', caso uma das tasks (t2 ou t3) retorne sucesso, pois a outra
        # obrigatoriamente sera skiped, o t4 será chamado.
    )    
 
    t1 >> branch >> [t2, t3] >> t4
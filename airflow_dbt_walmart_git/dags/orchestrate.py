from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator
from utils import trigger_databricks_job

@dag
def orchestrate():

    @task.python
    def ingest_cdc():
        trigger_databricks_job()

    @task.bash
    def clean_target():
        return "rm -rf /opt/airflow/walmart_project/target && rm -rf /opt/airflow/walmart_project/logs"

    @task.bash
    def source_freshness():
        return "cd /opt/airflow/walmart_project && dbt source freshness"

    silver_technical = BashOperator(
        task_id="silver_technical",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select silver_t"
    )

    silver_technical_test = BashOperator(
        task_id="silver_technical_test",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt test --select silver_t"
    )

    silver_business = BashOperator(
        task_id="silver_business",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select silver_b"
    )

    silver_business_test = BashOperator(
        task_id="silver_business_test",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt test --select silver_b"
    )

    gold_ephemeral = BashOperator(
        task_id="gold_ephemeral",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select gold/ephemeral"
    )

    gold_dimensions = BashOperator(
        task_id="gold_dimensions",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt snapshot"
    )

    gold_fact = BashOperator(
        task_id="gold_fact",
        cwd="/opt/airflow/walmart_project",
        bash_command="dbt run --select gold/fact"
    )

    ingest_cdc()>>clean_target()>>source_freshness() >> silver_technical >> silver_technical_test >> silver_business >> silver_business_test >> gold_ephemeral >> gold_dimensions >> gold_fact

orchestrate_dag = orchestrate()
from databricks.sdk import WorkspaceClient
import time
from databricks.sdk.service.jobs import RunLifeCycleState, RunResultState

def trigger_databricks_job():
    ws = WorkspaceClient(
        host="your_databricks_host",
        token="your_databricks_token"
    )
    job_trigger = ws.jobs.run_now(job_id="your_databricks_job_id")  
    while True:
        job_status = ws.jobs.get_run(run_id=job_trigger.run_id)
        print(f"Job status: {job_status.state.life_cycle_state}, Result state: {job_status.state.result_state}")
        if job_status.state.life_cycle_state in [RunLifeCycleState.TERMINATED, RunLifeCycleState.SKIPPED, RunLifeCycleState.INTERNAL_ERROR]:
            if job_status.state.result_state == RunResultState.SUCCESS:
                print("Job completed successfully.")
                break
            else:
                raise Exception(f"Job failed with state: {job_status.state.result_state}")
        time.sleep(10)  # Wait for 10 seconds before checking again
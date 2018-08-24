import time
import boto3

CLUSTER_ARN = os.environ.get(CLUSTER_ARN)
SCHEDULER_TASK_ARN = os.environ.get(SCHEDULER_TASK_ARN)

def wait_for_capacity():
    has_capacity = False
    client = boto3.client('ecs')
    while not has_capacity:
        response = client.describe_clusters(
            clusters = [
                CLUSTER_ARN
            ]
        )
        has_capacity = bool(
            response['clusters'][0]['registeredContainerInstancesCount']
        )
        print(response)
        time.sleep(0.1)
    
def start_scheduler_task():
    client = boto3.client('ecs')
    response = client.run_task(
        cluster=CLUSTER_ARN,
        taskDefinition=SCHEDULER_TASK_ARN
    )
    print(response)

def main():
    wait_for_capacity()
    start_scheduler_task()

if __name__ == "__main__":
    main()

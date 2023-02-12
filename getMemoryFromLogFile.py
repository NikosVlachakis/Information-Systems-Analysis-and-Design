import requests
import json

# Get the Spark application ID
def get_app_id():
    response = requests.get("http://<driver-node>:4040/api/v1/applications")
    applications = json.loads(response.text)
    app_id = applications[0]["id"]
    return app_id

# Get the executor summary
def get_executor_summary(app_id):
    response = requests.get(f"http://<driver-node>:4040/api/v1/applications/{app_id}/executors")
    executors = json.loads(response.text)
    return executors

# Calculate the average CPU usage
def get_average_cpu_usage(executors):
    total_cpu = 0
    for executor in executors:
        total_cpu += executor["totalCores"]
    average_cpu = total_cpu / len(executors)
    return average_cpu

app_id = get_app_id()
executors = get_executor_summary(app_id)
average_cpu = get_average_cpu_usage(executors)
print("Average CPU usage:", average_cpu)

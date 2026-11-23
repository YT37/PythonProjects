import json

from todoist_api_python.api import TodoistAPI
from tqdm import tqdm

print("Starting")

# Setup API
"""
api = TodoistAPI("API Key Here")
"""

# Get Projects
"""
print(api.get_projects())
"""

# Add Tasks to Project
"""project = api.projects.add("Project Name Here")
api.commit()

tasks = []
with open("Tasks.json") as file:
    tasks = json.load(file)["tasks"]

print(f"\nNo. of Tasks: {len(tasks)}\n")

for task in tqdm(tasks):
    api.items.add(task, project_id=project["id"])
    api.commit()"""

# Add Subtasks
"""main_task = api.items.add("Task Name Here")
](
tasks = []
with open("Tasks.json") as file:
    tasks = json.load(file)["tasks"]

print(f"\nNo. of Tasks: {len(tasks)}\n")

for task in tqdm(tasks):
    api.items.add(task, parent_id=main_task["id"])
    api.commit()"""

# Get Project Data by ID
"""
tasks = api.get_tasks(project_id="Project Name Here")

content = []
for task in tasks:
    content.append(task.content)

with open("Tasks.json", "w") as f:
    f.write(json.dumps({"tasks": content}))
"""

# Move Tasks
"""project_id = ""

data = api.projects.get_data(project_id)
task_ids = []

print(f"\nNo. of Tasks: {len(task_ids)}\n")

for item in data["items"]:
    task_ids.append(item["id"])

for id in tqdm(task_ids):
    item = api.items.get_by_id(id)
    item.move(project_id=project_id)

    api.commit()"""

print("\nFinished")

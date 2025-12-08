import argparse
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
VALID_STATUSES = ["todo", "in-progress","done"]

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []

def find_task(tasks,task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return task, i
    return None, None

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def current_timestamp():
    return datetime.now().isoformat(timespec="seconds")

def change_status(task_id, new_status):
    tasks = load_tasks()
    task, index = find_task(tasks, task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return
    tasks[index]["status"] = new_status
    tasks[index]["updatedAt"] = current_timestamp()
    save_tasks(tasks)
    print(f"Task {task_id} marked as {new_status}.")

def cmd_mark_in_progress(args):
    change_status(args.id, "in-progress")

def cmd_mark_done(args):
    change_status(args.id, "done")

def cmd_add(args):
    tasks = load_tasks()
    new_id = get_next_id(tasks)
    now = current_timestamp()

    task = {
        "id": new_id,
        "description": args.description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task has bin added (ID: {new_id})")

def cmd_list(args):
    tasks = load_tasks()
    status_filter = args.status

    if status_filter and status_filter not in VALID_STATUSES:
        print("Error: Invalid status. Use: todo, in-progress, done")
        return
    if status_filter:
        tasks = [t for t in tasks if t ["status"] == status_filter]

    if not tasks:
        if status_filter:
            print(f"No tasks with status “{status_filter}“.")
        else:
            print("No status")
        return
    for task in tasks:
        print(
            f"[{task['id']}] "
            f"({task['status']}) "
            f"{task['description']} "
            f"(created: {task['createdAt']}, updated: {task['updatedAt']})"
        )

def cmd_update(args):
    tasks = load_tasks()
    task_id = args.id
    task, index = find_task(tasks, task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    tasks[index]["description"] = args.description
    tasks[index]["updateAt"] = current_timestamp()
    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")

def cmd_delete(args):
    tasks = load_tasks()
    task_id = args.id
    task, index = find_task(tasks, task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found")
        return

    tasks.pop(index)
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")

def build_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = subparsers.add_parser("add", help="New task")
    p_add.add_argument("description", type=str, help="Description of task")
    p_add.set_defaults(func=cmd_add)

    # list
    p_list = subparsers.add_parser("list", help="List tasks")
    p_list.add_argument(
        "status",
        nargs="?",
        help="Optional filter: todo, in-progress, done"
    )
    p_list.set_defaults(func=cmd_list)

    #update
    p_update = subparsers.add_parser("update", help="Update an existing task")
    p_update.add_argument("id", type=int, help="ID of the task to update")
    p_update.add_argument("description", type=str, help="New description")
    p_update.set_defaults(func=cmd_update)

    #delete
    p_delete = subparsers.add_parser("delete", help="Delete a task")
    p_delete.add_argument("id", type=int, help="ID of the task to delete")
    p_delete.set_defaults(func=cmd_delete)

    #mark-in-progress
    p_mip = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    p_mip.add_argument("id", type=int, help="ID of task")
    p_mip.set_defaults(func=cmd_mark_in_progress)

    #mark-done
    p_md = subparsers.add_parser("mark-done", help="Mark a task as done")
    p_md.add_argument("id", type=int, help="ID of task")
    p_md.set_defaults(func=cmd_mark_done)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

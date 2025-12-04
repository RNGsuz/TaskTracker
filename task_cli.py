import argparse
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

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

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def current_timestamp():
    return datetime.now().isoformat(timespec="seconds")

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
    print("LIST aufgerufen")

def build_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = subparsers.add_parser("add", help="New task")
    p_add.add_argument("description", type=str, help="Description of task")
    p_add.set_defaults(func=cmd_add)

    # list
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

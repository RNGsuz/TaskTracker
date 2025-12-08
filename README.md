
# Task Tracker CLI

Task Tracker is a simple command-line task management application written in Python.  
All tasks are stored locally in a file called `tasks.json` in the same directory as the script.
Project idea from: https://roadmap.sh/projects/task-tracker

---

## Features

- Add new tasks
- List tasks (optional status filtering)
- Update existing tasks
- Delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- Automatically stores creation and update timestamps

---

## Valid Task Statuses

- `todo`
- `in-progress`
- `done`

---

## Requirements

- Python 3.7 or higher
- No external libraries required

---

## Installation

1. Save the script as:

   ```bash
   task_tracker.py


2. (Optional) Make it executable:

   ```bash
   chmod +x task_tracker.py
   ```

3. Run it from the same directory or add it to your system `PATH`.

---

## Task Storage Format

All tasks are stored in `tasks.json`:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2025-12-08T10:00:00",
    "updatedAt": "2025-12-08T10:00:00"
  }
]
```

---

## General Usage

```bash
python task_tracker.py <command> [arguments]
```

---

## Available Commands

* `add`
* `list`
* `update`
* `delete`
* `mark-in-progress`
* `mark-done`

---

## Command Reference

### 1. Add a Task

```bash
python task_tracker.py add "Task description"
```

Example:

```bash
python task_tracker.py add "Write project documentation"
```

---

### 2. List Tasks

```bash
python task_tracker.py list
```

Filter by status:

```bash
python task_tracker.py list todo
python task_tracker.py list in-progress
python task_tracker.py list done
```

---

### 3. Update a Task

```bash
python task_tracker.py update <id> "New description"
```

Example:

```bash
python task_tracker.py update 1 "Write detailed documentation"
```

---

### 4. Delete a Task

```bash
python task_tracker.py delete <id>
```

---

### 5. Mark Task as In-Progress

```bash
python task_tracker.py mark-in-progress <id>
```

---

### 6. Mark Task as Done

```bash
python task_tracker.py mark-done <id>
```

---

## Notes

* Task IDs auto-increment.
* `createdAt` is set when the task is added.
* `updatedAt` is updated whenever a task is changed.
* If `tasks.json` is missing or corrupted, it is recreated automatically.

---

## Example Workflow

```bash
python task_tracker.py add "Buy milk"
python task_tracker.py add "Finish homework"
python task_tracker.py list
python task_tracker.py update 1 "Buy milk and bread"
python task_tracker.py mark-in-progress 1
python task_tracker.py mark-done 1
python task_tracker.py delete 2
```

from src.task import Task


class TaskManager:
    def __init__(self):
        self._tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        task_id = len(self._tasks) + 1
        task = Task(id=task_id, title=title)
        self._tasks.append(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self._tasks.copy()
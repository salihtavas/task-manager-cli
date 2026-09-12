from src.task import Task


class TaskManager:
    def __init__(self, tasks: list[Task] | None = None):
        self._tasks: list[Task] = tasks or []

    def add_task(self, title: str) -> Task:
        task_id = self._get_next_id()
        task = Task(id=task_id, title=title)
        self._tasks.append(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self._tasks.copy()

    def complete_task(self, task_id: int) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                return True
        return False

    def _get_next_id(self) -> int:
        if not self._tasks:
            return 1

        return max(task.id for task in self._tasks) + 1
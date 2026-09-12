import json
from pathlib import Path

from src.task import Task


class JsonStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def save_tasks(self, tasks: list[Task]) -> None:
        data = [
            {
                "id": task.id,
                "title": task.title,
                "completed": task.completed,
            }
            for task in tasks
        ]

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load_tasks(self) -> list[Task]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Task(
                id=item["id"],
                title=item["title"],
                completed=item["completed"],
            )
            for item in data
        ]
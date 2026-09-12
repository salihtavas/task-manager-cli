from src.storage import JsonStorage
from src.task import Task


def test_save_and_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage = JsonStorage(str(file_path))

    tasks = [
        Task(id=1, title="Learn Git"),
        Task(id=2, title="Learn pytest", completed=True),
    ]

    storage.save_tasks(tasks)
    loaded_tasks = storage.load_tasks()

    assert loaded_tasks == tasks


def test_load_tasks_returns_empty_list_when_file_does_not_exist(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage = JsonStorage(str(file_path))

    assert storage.load_tasks() == []
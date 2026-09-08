from src.task import Task


def test_task_is_created_with_default_completed_false():
    task = Task(id=1, title="Learn Git")

    assert task.id == 1
    assert task.title == "Learn Git"
    assert task.completed is False


def test_task_can_be_created_as_completed():
    task = Task(id=2, title="Learn pytest", completed=True)

    assert task.id == 2
    assert task.title == "Learn pytest"
    assert task.completed is True
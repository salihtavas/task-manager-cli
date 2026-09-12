from src.task_manager import TaskManager


def test_task_manager_starts_with_no_tasks():
    manager = TaskManager()

    assert manager.list_tasks() == []


def test_add_task_creates_a_task():
    manager = TaskManager()

    task = manager.add_task("Learn Git")

    assert task.id == 1
    assert task.title == "Learn Git"
    assert task.completed is False


def test_add_task_stores_the_task():
    manager = TaskManager()

    task = manager.add_task("Learn Git")

    assert manager.list_tasks() == [task]


def test_add_task_assigns_incrementing_ids():
    manager = TaskManager()

    first_task = manager.add_task("Learn Git")
    second_task = manager.add_task("Learn pytest")

    assert first_task.id == 1
    assert second_task.id == 2


def test_list_tasks_returns_a_copy():
    manager = TaskManager()
    manager.add_task("Learn Git")

    tasks = manager.list_tasks()
    tasks.clear()

    assert len(manager.list_tasks()) == 1

def test_list_tasks_returns_tasks_in_added_order():
    manager = TaskManager()

    first_task = manager.add_task("Learn Git")
    second_task = manager.add_task("Learn pytest")

    assert manager.list_tasks() == [first_task, second_task]

def test_complete_task_marks_task_as_completed():
    manager = TaskManager()
    task = manager.add_task("Learn Git")

    result = manager.complete_task(task.id)

    assert result is True
    assert task.completed is True
    result = manager.complete_task(task.id)

    assert result is True
    assert task.completed is True


def test_complete_task_returns_false_for_unknown_id():
    manager = TaskManager()

    result = manager.complete_task(999)

    assert result is False


def test_delete_task_removes_task():
    manager = TaskManager()
    task = manager.add_task("Learn Git")

    result = manager.delete_task(task.id)

    assert result is True
    assert manager.list_tasks() == []


def test_delete_task_returns_false_for_unknown_id():
    manager = TaskManager()

    result = manager.delete_task(999)

    assert result is False
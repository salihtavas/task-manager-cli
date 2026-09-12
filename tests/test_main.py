from src.main import main


def test_exit_option_closes_application(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    main()

    captured = capsys.readouterr()

    assert "Goodbye!" in captured.out


def test_invalid_option_shows_error(monkeypatch, capsys):
    inputs = iter(["invalid", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()

    assert "Invalid option." in captured.out

def test_user_can_add_and_list_a_task(monkeypatch, capsys):
    inputs = iter(
        [
            "1",
            "Learn Git",
            "2",
            "5",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    captured = capsys.readouterr()

    assert "Task added: Learn Git" in captured.out
    assert "1. Learn Git" in captured.out
from src import employees


def test_manager_role():
    manager = employees.Manager(1, 'Zakaria', 700)
    assert manager.work(40) == 'Top of the food chain, and works for 40 hours'

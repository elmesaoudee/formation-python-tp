import pytest

from src import employees, productivity


@pytest.fixture
def manager_role():
    return productivity.ManagerRole()


@pytest.fixture
def secretary_role():
    return productivity.SecretaryRole()


@pytest.fixture
def sales_person_role():
    return productivity.SalesPersonRole()


@pytest.fixture
def factory_worker_role():
    return productivity.FactoryWorkerRole()


def test_productivity_system():
    manager = employees.Manager(1, 'Zakaria', 700)
    secretary = employees.Secretary(1, 'Zakaria', 700)
    sales_person = employees.SalesPerson(3, 'Meryem', 500, 300)
    factory_worker = employees.FactoryWorker(2, 'Amine', 28, 20)
    temporary_secretary = employees.TemporarySecretary(5, 'Amina', 40, 15)
    emps = [
        manager,
        secretary,
        sales_person,
        factory_worker,
        temporary_secretary
    ]
    productivity_system_actual = productivity.ProductivitySystem.track_productivity(emps, 40)
    productivity_system_expected = (
        'Tracking employee productivity\n'
        '------------------------------\n'
        'Zakaria : Top of the food chain, and works for 40 hours\n'
        'Zakaria : Does paper work and, works for 40 hours\n'
        'Meryem : Gets phone calls and, works for 40 hours\n'
        'Amine : Bottom of the food chain, and works for 40 hours\n'
        'Amina : Does paper work and, works for 40 hours'
    )
    assert productivity_system_actual == productivity_system_expected


def test_manager_role(manager_role):
    assert manager_role.work(40) == 'Top of the food chain, and works for 40 hours'


def test_manager_role_raises_exception(manager_role):
    with pytest.raises(productivity.EmployeeExhaustedException):
        manager_role.work(120)


def test_secretary_role(secretary_role):
    assert secretary_role.work(30) == 'Does paper work and, works for 30 hours'


def test_secretary_role_raises_exception(secretary_role):
    with pytest.raises(productivity.EmployeeExhaustedException):
        secretary_role.work(120)


def test_sales_person_role(sales_person_role):
    assert sales_person_role.work(20) == 'Gets phone calls and, works for 20 hours'


def test_sales_person_role_raises_exception(sales_person_role):
    with pytest.raises(productivity.EmployeeExhaustedException):
        sales_person_role.work(120)


def test_factory_worker_role(factory_worker_role):
    assert factory_worker_role.work(20) == 'Bottom of the food chain, and works for 20 hours'


def test_factory_worker_role_raises_exception(factory_worker_role):
    with pytest.raises(productivity.EmployeeExhaustedException):
        factory_worker_role.work(120)

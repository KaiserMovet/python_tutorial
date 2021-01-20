from .fixtures import CalcInterface
import pytest


@pytest.fixture(scope='module')
def calc_interface():
    print("CREATE FIXTURE")
    a = CalcInterface()
    yield a
    a.clean()
    print("DELETE FIXTURE")

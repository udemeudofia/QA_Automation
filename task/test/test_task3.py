import pytest
from task.task3 import task_3


def test_3(setup):
    assert task_3('http://the-internet.herokuapp.com/challenging_dom', setup) == 'Test case finished ....'

import pytest
from task.task1 import task_1


def test_1(setup):
    assert task_1('https://www.tiketa.lt/EN/search', setup) == 'Test case finished ....'

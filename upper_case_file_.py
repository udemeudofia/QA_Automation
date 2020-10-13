import pytest

def test_betty():
    with open('data/betty.input.txt') as file1:
        with open('data/betty.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'


def test_cross():
    with open('data/cross.input.txt') as file1:
        with open('data/cross.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'



def test_peter():
    with open('data/peter.input.txt') as file1:
        with open('data/peter.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'


def test_shell():
    with open('data/shell.input.txt') as file1:
        with open('data/shell.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'



def test_silence():
    with open('data/silence.input.txt') as file1:
        with open('data/silence.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'


def test_something():
    with open('data/something.input.txt') as file1:
        with open('data/something.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'



def test_thought():
    with open('data/thought.input.txt') as file1:
        with open('data/thought.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'


def test_toast():
    with open('data/toast.input.txt') as file1:
        with open('data/toast.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'



def test_wood():
    with open('data/wood.input.txt') as file1:
        with open('data/wood.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'



def test_yellow():
    with open('data/yellow.input.txt') as file1:
        with open('data/yellow.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            print(len(f1))
            print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i].upper() == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, different file length'
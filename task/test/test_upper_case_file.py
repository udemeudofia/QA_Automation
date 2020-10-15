import pytest
import os
import shutil
from click.testing import CliRunner
from upper_case_file import upper_case_file

runner = CliRunner()


def test_betty_file():
    if os.path.exists('results'):
        shutil.rmtree('results')
    os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/betty.input.txt', "--output-file", 'results/betty_output.txt'])
    with open('results/betty_output.txt') as file1:
        with open('data/betty.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_cross_file():
    if os.path.exists('results/cross_output.txt'):
        os.remove('results/cross_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/cross.input.txt', "--output-file", 'results/cross_output.txt'])
    with open('results/cross_output.txt') as file1:
        with open('data/cross.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_peter_file():
    if os.path.exists('results/peter_output.txt'):
        os.remove('results/peter_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/peter.input.txt', "--output-file", 'results/peter_output.txt'])
    with open('results/peter_output.txt') as file1:
        with open('data/peter.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_shell_file():
    if os.path.exists('results/shell_output.txt'):
        os.remove('results/shell_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/shell.input.txt', "--output-file", 'results/shell_output.txt'])
    with open('results/shell_output.txt') as file1:
        with open('data/shell.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_silence_file():
    if os.path.exists('results/silence_output.txt'):
        os.remove('results/silence_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/silence.input.txt', "--output-file", 'results/silence_output.txt'])
    with open('results/silence_output.txt') as file1:
        with open('data/silence.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_something_file():
    if os.path.exists('results/something_output.txt'):
        os.remove('results/something_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/something.input.txt', "--output-file", 'results/something_output.txt'])
    with open('results/something_output.txt') as file1:
        with open('data/something.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_thought_file():
    if os.path.exists('results/thought_output.txt'):
        os.remove('results/thought_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/thought.input.txt', "--output-file", 'results/thought_output.txt'])
    with open('results/thought_output.txt') as file1:
        with open('data/thought.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_toast_file():
    if os.path.exists('results/toast_output.txt'):
        os.remove('results/toast_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/toast.input.txt', "--output-file", 'results/toast_output.txt'])
    with open('results/toast_output.txt') as file1:
        with open('data/toast.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_wood_file():
    if os.path.exists('results/wood_output.txt'):
        os.remove('results/wood_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/wood.input.txt', "--output-file", 'results/wood_output.txt'])
    with open('results/wood_output.txt') as file1:
        with open('data/wood.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


def test_yellow_file():
    if os.path.exists('results/yellow_output.txt'):
        os.remove('results/yellow_output.txt')
    # os.mkdir('results')

    result = runner.invoke(upper_case_file, ["--input-file", 'data/yellow.input.txt', "--output-file", 'results/yellow_output.txt'])
    with open('results/yellow_output.txt') as file1:
        with open('data/yellow.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            # print(len(f1))
            # print(len(f2))
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'

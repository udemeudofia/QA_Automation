import pytest
import os
import shutil
# filenames = ['betty', 'cross', 'peter', 'shell', 'silence', 'something', 'thought', 'toast', 'wood', 'yellow']


def upper_case_file(input_file, output_file):
    print(f"Converting {input_file} file to upper case in {output_file}!")

    with open(input_file, "r") as input_f:
        with open(output_file, "w") as output_f:
            output_f.write(input_f.read().upper())

    return output_file
#    print("Done!")

# upper_case_file('data/betty.input.txt', 'results/betty_output.txt')


def test_betty_file():
    if os.path.exists('results'):
        shutil.rmtree('results')
    os.mkdir('results')

    with open(upper_case_file('data/betty.input.txt', 'results/betty_output.txt')) as file1:
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

    with open(upper_case_file('data/cross.input.txt', 'results/cross_output.txt')) as file1:
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

    with open(upper_case_file('data/peter.input.txt', 'results/peter_output.txt')) as file1:
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

    with open(upper_case_file('data/shell.input.txt', 'results/shell_output.txt')) as file1:
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

    with open(upper_case_file('data/silence.input.txt', 'results/silence_output.txt')) as file1:
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

    with open(upper_case_file('data/something.input.txt', 'results/something_output.txt')) as file1:
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

    with open(upper_case_file('data/thought.input.txt', 'results/thought_output.txt')) as file1:
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

    with open(upper_case_file('data/toast.input.txt', 'results/toast_output.txt')) as file1:
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

    with open(upper_case_file('data/wood.input.txt', 'results/wood_output.txt')) as file1:
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

    with open(upper_case_file('data/yellow.input.txt', 'results/yellow_output.txt')) as file1:
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

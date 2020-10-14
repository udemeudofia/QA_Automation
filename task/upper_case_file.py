import pytest
filenames = ['betty', 'cross', 'peter', 'shell', 'silence', 'something', 'thought', 'toast', 'wood', 'yellow']

def test_check():
    for f_name in filenames:
        with open(f'data/{f_name}.input.txt') as file1:
            with open(f'data/{f_name}.output.txt') as file2:
                f1 = file1.readlines()
                f2 = file2.readlines()
                print(len(f1))
                print(len(f2))
                if len(f1) == len(f2):
                    for i in range(len(f1)):
                        assert f1[i].upper() == (f2[i]), f'test failed on {f_name}.input.txt'
                else:
                    assert len(f1) == len(f2), f'test failed, {f_name}.input.txt and {f_name}.output.txt' \
                                               f' have different file length'
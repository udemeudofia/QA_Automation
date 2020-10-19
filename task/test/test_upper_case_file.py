import pytest
from click.testing import CliRunner
import upper_case_file

runner = CliRunner()


@pytest.mark.parametrize('fname', [
    'betty', 'cross', 'peter', 'shell', 'silence', 'something', 'thought', 'toast', 'wood', 'yellow'
])
def test_file(tmp_path, pytestconfig, fname):
    f2 = tmp_path/'{fname}_output.txt'

    result = runner.invoke(upper_case_file,
                           ["--input-file", f'{pytestconfig.rootdir}/task/data/{fname}.input.txt', "--output-file", f2])

    with open(f2) as file1:
        with open(f'{pytestconfig.rootdir}/task/data/{fname}.output.txt') as file2:
            f1 = file1.readlines()
            f2 = file2.readlines()
            if len(f1) == len(f2):
                for i in range(len(f1)):
                    assert f1[i] == (f2[i]), 'test failed'
            else:
                assert len(f1) == len(f2), 'test failed, both files have different file length'


if __name__ == '__main__':
    test_file()

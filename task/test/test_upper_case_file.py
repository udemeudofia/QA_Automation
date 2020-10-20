# pylint: disable=unused-variable
"""
Testing upper_case_file.py
"""
import pytest
from click.testing import CliRunner
from task.upper_case_file import upper_case_file

runner = CliRunner()


@pytest.mark.parametrize(
    "fname",
    [
        "betty",
        "cross",
        "peter",
        "shell",
        "silence",
        "something",
        "thought",
        "toast",
        "wood",
        "yellow",
    ],
)
def test_file(tmp_path, pytestconfig, fname):
    """Testing upper_case_file function"""
    file1 = tmp_path / "{fname}_output.txt"

    result = runner.invoke(
        upper_case_file,
        [
            "--input-file",
            f"{pytestconfig.rootdir}/task/test/data/{fname}.input.txt",
            "--output-file",
            file1,
        ],
    )

    with open(file1) as item1:
        with open(f"{pytestconfig.rootdir}/task/test/data/{fname}.output.txt") as item2:
            file2 = item1.readlines()
            file1 = item2.readlines()
            if len(file2) == len(file1):
                for count, names in enumerate(file2):
                    assert file2[count] == file1[count], "test failed"
            else:
                assert len(file2) == len(
                    file1
                ), "test failed, both files have different file length"

from subprocess import CalledProcessError

import pytest

from ..dotfiles import Command


def test_fails_silently(failed_exit_code):
    cmd = Command(f"exit {failed_exit_code}")
    result = cmd.execute()
    assert result.exit_code == failed_exit_code


def test_fails_with_exception_raised_on_check(failed_exit_code):
    cmd = Command(f"exit {failed_exit_code}")
    with pytest.raises(CalledProcessError):
        cmd.execute(check=True)


def test_succeeds_with_stdout():
    cmd = Command('echo "successful echo test"')
    result = cmd.execute()
    assert result.output.strip() == "successful echo test"


def test_wraps_command_on_exception(failed_exit_code):
    cmd = Command(f"exit {failed_exit_code}")
    result = cmd.execute()
    assert result.command == f"exit {failed_exit_code}"


def test_wraps_command_on_success():
    cmd = Command("echo success")
    result = cmd.execute()
    assert result.command == "echo success"


def test_wraps_retruncode_on_exception(failed_exit_code):
    cmd = Command(f"exit {failed_exit_code}")
    result = cmd.execute()
    assert result.exit_code == failed_exit_code


def test_wraps_returncode_on_success():
    cmd = Command("exit 0")
    result = cmd.execute()
    assert result.exit_code == 0


def test_wraps_stderr_on_exception(failed_exit_code):
    directory_name = f"directory_that_does_not_exist_{failed_exit_code}"
    cmd = Command(f"ls {directory_name}")
    result = cmd.execute()
    assert "No such file or directory" in result.error
    assert directory_name in result.error
    assert result.output == ""


def test_wraps_stderr_on_success():
    cmd = Command("echo success")
    result = cmd.execute()
    assert result.error == ""


def test_wraps_stdout_on_exception(failed_exit_code):
    cmd = Command(f'echo "stdout is still caught" && exit {failed_exit_code}')
    result = cmd.execute()
    assert result.output.strip() == "stdout is still caught"
    assert result.exit_code == failed_exit_code


def test_wraps_stdout_on_success():
    cmd = Command("echo success")
    result = cmd.execute()
    assert result.output.strip() == "success"
    assert result.error == ""

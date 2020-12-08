from ..dotfiles import CommandResult


def test_expected_data_members_exist():
    result = CommandResult(
        command="some command",
        output="some output",
        exit_code=0,
        error="some error",
    )
    assert isinstance(result, CommandResult)

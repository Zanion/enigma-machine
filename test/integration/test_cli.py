import pytest
from click.testing import CliRunner
from enigma_machine.__main__ import cli


def test_cli_with_no_arguments():
    # Given no arguments
    text = "Some text"
    args = []

    # When I execute the CLI
    #runner = CliRunner()
    #with pytest.raises(TypeError, match='Options cannot have nargs < 0'):
    #result = runner.invoke(cli, args)

    # Then I see the output and successful return code
    #assert result.exit_code == 1
    #assert text in result.output

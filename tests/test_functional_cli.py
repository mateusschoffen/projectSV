from typer.testing import CliRunner

from fornecedorlog.cli import main

runner = CliRunner()


def test_add_fornecedor():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "fornecedor added" in result.stdout

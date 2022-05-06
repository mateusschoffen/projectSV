from typer.testing import CliRunner

from fornecedorlog.cli import main

runner = CliRunner()


def test_add_fornecedor():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--distance=1", "--limit=1", "--payment=2"]
    )
    assert result.exit_code == 0
    assert "fornecedor added" in result.stdout

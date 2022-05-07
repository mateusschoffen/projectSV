from typer.testing import CliRunner

from fornecedorlog.cli import main

runner = CliRunner()


def test_add_fornecedor():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--pagamento=1", "--image=1", "--limite=2"]
    )
    assert result.exit_code == 0
    assert "fornecedor added" in result.stdout

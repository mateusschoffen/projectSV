import typer
from typing import Optional
from fornecedorlog.core import add_fornecedor_to_database, get_fornecedors_from_database
from rich.table import Table
from rich.console import Console


main = typer.Typer(help="fornecedor Management Application")


console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    distance: int = typer.Option(...),
    limit: int = typer.Option(...),
    payment: int = typer.Option(...),
):
    """Adds a new fornecedor to database."""
    if add_fornecedor_to_database(name, style, distance, limit, payment):
        print(" fornecedor added to database")


@main.command("list")
def list_fornecedors(style: Optional[str] = None):
    """Lists fornecedors in database."""
    fornecedors = get_fornecedors_from_database()
    table = Table(title="fornecedorlog :fornecedor_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="purple")
    for fornecedor in fornecedors:
        fornecedor.date = fornecedor.date.strftime("%Y-%m-%d")
        values = [str(getattr(fornecedor, header)) for header in headers]
        table.add_row(*values)
    console.print(table)

from typing import Optional

import typer
from rich import print
from rich.console import Console
from rich.table import Table

from fornecedorlog.core import add_fornecedor_to_database, get_fornecedors_from_database

main = typer.Typer(help="fornecedor Management Application")
console = Console()


@main.command()
def add(
    name: str,
    style: str,
    pagamento: int = typer.Option(...),
    image: int = typer.Option(...),
    limite: int = typer.Option(...),
):
    """Adds a new fornecedor to the database"""
    if add_fornecedor_to_database(name, style, pagamento, image, limite):
        print(":fornecedor_mug: fornecedor added!!!")
    else:
        print(":no_entry: - Cannot add fornecedor.")


@main.command("list")
def list_fornecedors(style: Optional[str] = None):
    """Lists fornecedors from the database"""
    fornecedors = get_fornecedors_from_database(style)
    table = Table(
        title="fornecedorlog Database" if not style else f"fornecedorlog {style}"
    )
    headers = [
        "id",
        "name",
        "style",
        "pagamento",
        "image",
        "limite",
        "rate",
        "date",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for fornecedor in fornecedors:
        fornecedor.date = fornecedor.date.strftime("%Y-%m-%d")
        values = [str(getattr(fornecedor, header)) for header in headers]
        table.add_row(*values)
    console.print(table)

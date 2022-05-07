from fornecedorlog.core import get_fornecedors_from_database, add_fornecedor_to_database


def test_add_fornecedor_to_database():
    assert add_fornecedor_to_database("Fornecedor A", "NY", 10, 3, 6)


def test_get_fornecedors_from_database():
    add_fornecedor_to_database("Fornecedor A", "NY", 10, 3, 6)
    results = get_fornecedors_from_database()
    assert len(results) > 0

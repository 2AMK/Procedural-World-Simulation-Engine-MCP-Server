"""
Testes unitários para a ferramenta `tree_file` no módulo `tools.tree_file`
"""
import pytest
import tools.tree_file as tf


def test_tree_file_ok(fake_file_tree):
    """
    Testa o comportamento esperado da função `tree_file` quando chamada com um caminho válido.
    """
    # Act
    result = tf.tree_file({"path": ".", "max_depth": 2}, base_dir= fake_file_tree)

    # Assert 
    assert result["type"] == "dir"
    assert isinstance(result["children"], list)
    assert any(child["name"]== "subdir" for child in result["children"])

def test_tree_file_dir_empty(fake_file_tree):
    """
    Testa o comportamento quando a função `tree_file` é chamada com o diretório vazio.
    """
    # Arrange
    empty_dir = fake_file_tree/"empty_dir"
    empty_dir.mkdir()

    # Act
    result = tf.tree_file({"path":"."}, base_dir=empty_dir)

    # Assert
    assert result["children"]==[]
    
def test_tree_file_outside_allowed(fake_file_tree):
    """
    Testa o comportamento esperado da função tree_file quando tenta ler fora do diretório permitido
    """
    # Assert
    with pytest.raises(PermissionError):
        tf.tree_file({"path":"../"}, base_dir=fake_file_tree)


def test_tree_subdir_ok(fake_file_tree):
    """
    Testa o comportamento esperado ao usar a função `tree_file` em um subdiretório. 
    """
    # Act
    result = tf.tree_file({"path":"subdir", "max_depth":1}, base_dir=fake_file_tree)

    # Assert
    assert result["type"]== "dir"
    assert any(child["name"]== "c.txt" for child in result["children"])


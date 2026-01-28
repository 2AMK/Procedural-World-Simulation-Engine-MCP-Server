"""
Teste unitário para a função `list_files` no módulo `tools.list`

"""

from tools.list_files import list_files
import tools.list_files as lf
import pytest
from pathlib import Path


def test_list_files_ok(fake_fs):
    """
    Testa o comportamento esperado da ferramenta list_files quando chamada com um caminho válido.

    """
    # Arrange and Act
    result = list_files({"path":"."}, base_dir=fake_fs) # Chama a função list_files com um caminho

    # Assert
    assert result["path"] == "."

    names = [e["name"] for e in result["entries"]] # forma uma lista com os nomes dos arquivos e diretório
    types = {e["name"]: e["type"] for e in result["entries"]} # forma um dicionário com nome e tipo do arquivo


    assert names == ["a.txt", "b.txt", "subdir"]
    assert types["a.txt"] == "file"
    assert types["b.txt"] == "file"
    assert types["subdir"] == "dir"

def test_list_files_subdir(fake_fs):
    """
    Testa o comportamento de ferramenta list_files quando chamada com um caminho válido para um subdiretório.

    """

    # Arrange
    # Act
    result = list_files({"path":"subdir"}, base_dir=fake_fs)

    # Assert
    assert result["path"] == "subdir"
    assert result["entries"] == []

#___________#
def test_list_files_not_dir(fake_fs):
    """
    Testa o comportamento da ferramenta list_files caso chamada com caminho não válido
    """
    # Assert
    with pytest.raises(ValueError):
        list_files({"path":"a.txt"}, base_dir=fake_fs)

def test_list_files_outside_allowed(fake_fs):
    """
    Testa o comportamento fora do diretório permitido
    """
    #Assert
    with pytest.raises(PermissionError):
        list_files({"path":"../"}, base_dir=fake_fs)


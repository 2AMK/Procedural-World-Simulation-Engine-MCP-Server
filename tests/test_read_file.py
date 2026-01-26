"""
Testes unitários para a ferramenta read_file no módulo tools.read_file

"""

import tools.read_file as rf
from tools.read_file import read_file
import pytest

def test_read_file_ok(fake_file_content):
    """
    Testa o comportamento esperado da função read_file quando chamada com um caminho válido para um arquivo de texto.
    """
    # Arrange
    
    # Act
    result = read_file({"path": "file.txt"}, base_dir=fake_file_content)

    # Assert
    assert result["path"] == "file.txt"
    assert result["content"] == "Hello, world!"


def test_read_file_is_directory(fake_file_content): #OK
    """
    Testa o comportamento esperado da função read_file quando chamada com um caminho que aponta para o diretório
    """

    # Assert
    with pytest.raises(ValueError):
        rf.read_file({"path":"subdir"}, base_dir=fake_file_content)

def test_read_file_not_exists(fake_file_content): # OK
    """
    Testa o comportamento esperado da função read_file quando chamada com um caminho que aponta para arquivo inexistente
    """
    # Assert
    with pytest.raises(ValueError):
        rf.read_file({"path":"c.txt"}, base_dir=fake_file_content)

def test_read_file_outside_allowed(fake_file_content): #OK
    """
    Testa o comportamento esperado da função read_file quando tenta ler um arquivo fora do diretório permitido.
    """
    # Assert
    with pytest.raises(PermissionError):
        rf.read_file({"path":"../c.txt"}, base_dir=fake_file_content)

def test_read_file_empty(fake_file_content):
    """
    Testa a ferramenta read_file quando chamada com um arquivo vazio.
    """
    # Arrange
    empty = fake_file_content/"vazio.txt"
    empty.write_text("", encoding = "UTF-8")

    # Act
    result = rf.read_file({"path":"vazio.txt"}, base_dir=fake_file_content)

    # Assert
    assert result["content"] == ""


    







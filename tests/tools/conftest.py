
"""
Fixture para criar um ambiente de teste falso com arquivos e subdiretórios para testes
"""
import pytest
@pytest.fixture
def fake_fs(tmp_path):
    """
    Cria um diretório falso com arquivos e subdiretórios:
    root/
        a.txt
        b.txt
        subdir/
    """
    (tmp_path / "a.txt").write_text("A")
    (tmp_path / "b.txt").write_text("B")
    (tmp_path / "subdir").mkdir()
    return tmp_path

@pytest.fixture
def fake_file_content(tmp_path):
    """
    Cria um arquivo falso com conteúdo para testes.

    """
    (tmp_path/ "file.txt").write_text("Hello, world!")
    (tmp_path/ "subdir").mkdir()
    return tmp_path

@pytest.fixture
def fake_file_tree(tmp_path):
    """
    Docstring for fake_file_tree
    
    :param tmp_path: Description
    :type tmp_path: Path

    Args:
        tmp_path (Path): Um objeto Path para o diretório temporário.

    """
    (tmp_path / "a.txt").write_text("A")
    (tmp_path / "b.txt").write_text("B")
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir"/ "c.txt").write_text("C")
    (tmp_path / "subdir"/ "d.txt").write_text("D")
    (tmp_path / "subdir" / "subsubdir").mkdir()
    (tmp_path / "subdir" / "subsubdir"/ "e.txt").write_text("E")
    # Estrutura de diretórios esperada:
    # - a.txt
    # - b.txt
    # - subdir/
    #   - c.txt
    #   - d.txt
    #   - subsubdir/
    #     - e.txt
    return tmp_path

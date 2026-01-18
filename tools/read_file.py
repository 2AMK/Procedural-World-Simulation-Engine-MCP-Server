"""
Docstring for tools.read_file

Ferramenta modular usada para ler arquivos de texto.

"""
from utils.resolve_safe_path import resolve_safe_path

def read_file(arg:dict):
    """
    Lê um arquivo de texto e retorna seu conteúdo.
    """

    path = resolve_safe_path(arg.get("path","."))

    if not path.is_file():
        raise ValueError(f"O caminho fornecido não é um arquivo")

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    return{
        "path": str(path.relative_to()),
        "content": content,

    }
"""
Docstring for tools.read_file

Ferramenta modular usada para ler arquivos de texto.

"""
from utils.resolve_safe_path import resolve_safe_path, ALLOWED_DIR

MAX_FILE_SIXE = 200_000 # 200 KB

def read_file(args: dict):
    """
    Lê um arquivo de texto e retorna seu conteúdo.
    """

    path = resolve_safe_path(args.get("path","."))

    if not path.is_file():
        raise ValueError(f"O caminho fornecido não é um arquivo")

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    return{
        "path": str(path.relative_to(ALLOWED_DIR)),
        "content": content,
    }
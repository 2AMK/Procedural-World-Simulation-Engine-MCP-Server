"""
Ferramenta modular usada para listar arquivos em um diretório específico.
"""

from utils.resolve_safe_path import resolve_safe_path, ALLOWED_DIR

def list_files(args:dict):
    """
    Lista arquivo e diretório imediatamente abaixo de um caminho relativo
    """

    path = resolve_safe_path(args.get("path","."))

    if not path.is_dir():
        raise ValueError(f"O caminho fornecido não é um diretório")
    
    entries = []
    for file in sorted(path.iterdir(), key=lambda p: p.name.lower()):
        entries.append({
            "name": file.name,
            "type": "file" if file.is_file() else "dir"})


    return {
        "path": str(path.relative_to(ALLOWED_DIR)),
        "entries": entries
        }
# tools/list_files.py
"""
Ferramenta modular usada para listar arquivos em um diretório específico.
"""

from utils.resolve_safe_path import resolve_safe_path

def list_files(args:dict):
    """
    Lista arquivo e diretório imediatamente abaixo de um caminho relativo
    """

    path = resolve_safe_path(args.get("path","."))

    if not path.is_dir():
        raise ValueError(f"O caminho fornecido não é um diretório")
    
    return [

        {
            "name": file.name,
            "is_file": file.is_file(),
            "is_dir": file.is_dir()
        } for file in path.iterdir()
    ]

# tools/list_files.py
"""
Ferramenta modular usada para listar arquivos em um diretório específico.
"""

from utils.resolve_safe_path import resolve_safe_path, ALLOWED_DIR


def list_files(args:dict, *, base_dir= ALLOWED_DIR):
    """
    Lista arquivo e diretório imediatamente abaixo de um caminho relativo
    Args:
        args (dict): Dicionário contendo o caminho relativo sob a chave "path".
        base_dir (Path, opcional): Diretório base permitido. Padrão é ALLOWED_DIR.
    Returns:
        dict: Dicionário contendo o caminho relativo e a lista de entradas (arquivos e diretórios).
    Raises:
        PermissionError: Se o caminho estiver fora do diretório permitido.
        ValueError: Se o caminho fornecido não for um diretório.
    Usage:
        result = list_files({"path": "subdir"}, base_dir=ALLOWED_DIR)
    """
    # Resolve o caminho de forma segura e verifica se está dentro do diretório permitido.
    path = resolve_safe_path(args.get("path","."), base_dir=base_dir)

    # Caso o caminho não esteja dentro do diretório permitido, levanta uma exceção.
    if base_dir not in path.parents and path != base_dir:
        raise PermissionError("Caminho não permitido. Tente novamente com um caminho permitido")

    # Caso o caminho não seja diretório, levanta uma exceção
    if not path.is_dir():
        raise ValueError(f"O caminho fornecido não é um diretório")
    
    entries = []
    for file in sorted(path.iterdir(), key=lambda p: p.name.lower()):
        entries.append({
            "name": file.name,
            "type": "file" if file.is_file() else "dir"})


    return {
        "path": str(path.relative_to(base_dir)),
        "entries": entries
        }
# tools/list_files.py
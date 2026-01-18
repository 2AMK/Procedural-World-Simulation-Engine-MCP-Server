"""
Ferramenta modular usada para listar a estrutura de diretório
em um caminho específico.
"""

from pathlib import Path
from utils.resolve_safe_path import resolve_safe_path


def tree_file(args: dict):
    """
    Retorna a árvore de diretórios até um determinado nível.
    """

    max_depth = args.get("max_depth", 3)
    root = resolve_safe_path(args.get("path", "."))

    def walk(current: Path, depth: int):
        """
        Função recursiva para percorrer a árvore de diretórios.
        """

        if depth > max_depth:
            return None

        node = {
            "name": current.name,
            "type": "dir" if current.is_dir() else "file",
        }

        if current.is_dir():
            children = []

            try:
                for child in current.iterdir():
                    result = walk(child, depth + 1)
                    if result is not None:
                        children.append(result)
            except PermissionError:
                # Evita quebrar o MCP server
                pass

            node["children"] = children

        return node

    return walk(root, 0)

"""
Ferramenta modular usada para listar a estrutura de diretório
em um caminho específico.
"""

from pathlib import Path
from utils.resolve_safe_path import resolve_safe_path, ALLOWED_DIR


def tree_file(args: dict, *, base_dir=ALLOWED_DIR):
    """
    Retorna a árvore de diretórios até um determinado nível.
    """

    max_depth = args.get("max_depth", 3)
    root = resolve_safe_path(args.get("path", "."))

    def walk(current: Path, depth: int):
        """
        Função recursiva para percorrer a árvore de diretórios.

        Args:
            current (Path): Caminho atual.
            depth (int): Profundidade atual na árvore.
        Returns:
            dict: Dicionário representando a estrutura do diretório.
        Raises:
            PermissionError: Se o caminho estiver fora do diretório permitido.
            ValueError: Se o caminho fornecido não for um diretório.
        """

        if depth > max_depth:
            return None

        node = {
            "name": current.name,
            "path": str(current.relative_to(base_dir)),
            "type": "dir" if current.is_dir() else "file"
        }

        if current.is_dir():
            children = []

            try:
                for child in sorted(current.iterdir(), key=lambda p: p.name.lower()):
                    result = walk(child, depth + 1)
                    if result is not None:
                        children.append(result)
            except PermissionError:
                # Evita quebrar o MCP server
                pass

            node["children"] = children

        return node

    return walk(root, 0)

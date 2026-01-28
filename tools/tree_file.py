"""
Ferramenta modular usada para listar a estrutura de diretório
em um caminho específico.
"""

from pathlib import Path
from utils.resolve_safe_path import resolve_safe_path, ALLOWED_DIR


def tree_file(args: dict,
              path = ".",
              max_depth = 3,
               *, 
               base_dir=ALLOWED_DIR):
    """
    Retorna a árvore de diretórios até um determinado nível.

    Args:
        args (dict): Dicionário contendo o caminho relativo sob a chave "path" e a profundidade máxima sob a chave "max_depth".
        base_dir (Path, opcional): Diretório base permitido. Padrão é ALLOWED_DIR.
    Returns:
        dict: Dicionário representando a estrutura do diretório.
    Raises:
        PermissionError: Se o caminho estiver fora do diretório permitido.
        ValueError: Se o caminho fornecido não for um diretório.
    Usage:
        result = tree_file({"path": "subdir", "max_depth": 2}, base_dir=ALLOWED_DIR)

    """
    # Puxar o argumento 
    path = args.get("path", path)
    root = resolve_safe_path(path, base_dir=base_dir)
    max_depth = args.get("max_depth", max_depth)


    if not root.is_dir():
        raise ValueError(f"O caminho fornecido não é um diretório: {root}")
    
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

        node = {
            "name": current.name,
            "path": str(Path(*current.parts[len(base_dir.parts):])),
            "type": "dir" if current.is_dir() else "file",
            "children": [] if current.is_dir() else None
        }

        # Verifica se o depth atual é maior do que a profundidade máxima
        # Caso se for maior, irá parar a função e retornar o que já tem até
        # agora.
        if depth >= max_depth:
            return node

        # Se o caminho atual é um diretório, não caminho, irá tentar pegar 
        # os diretórios e arquivos filhos 
        if current.is_dir():
            children = []

            try:
                for child in sorted(current.iterdir(), key=lambda p: p.name.lower()):
                    result = walk(child, depth + 1)
                    if result is not None:
                        children.append(result)
                        
            except (PermissionError, OSError):
                pass # Evitar quebrar o servidor MCP                
            node["children"] = children
        return node
    return walk(root, 0)

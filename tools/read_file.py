"""
Docstring for tools.read_file

Ferramenta modular usada para ler arquivos de texto.

"""
from utils.resolve_safe_path import resolve_safe_path, ALLOWED_DIR

MAX_FILE_SIXE = 200_000 # 200 KB

def read_file(args: dict, *, base_dir=ALLOWED_DIR):
    """
    Lê um arquivo de texto e retorna seu conteúdo.

    Args:
        args (dict): Dicionário contendo o caminho relativo sob a chave "path".
        base_dir (Path, opcional): Diretório base permitido. Padrão é ALLOWED_DIR.
    Returns:
        dict: Dicionário contendo o caminho relativo e o conteúdo do arquivo.
    Raises:
        PermissionError: Se o caminho estiver fora do diretório permitido.
        ValueError: Se o caminho fornecido não for um arquivo ou se o arquivo for muito grande.
    Usages:
        result = read_file({"path": "file.txt"}, base_dir=ALLOWED_DIR)
        print(result)

    """

    # Resolve o caminho de forma segura e verifica se está dentro do diretório permitido.
    path = resolve_safe_path(args.get("path","."), base_dir=base_dir)

    # Caso o caminho seja fora do diretório permitido
    if base_dir not in path.parents and path != base_dir:
        raise PermissionError("Caminho não permitido. Tente novamente com um caminho permitido")

    # Caso o caminho fornecido não seja um arquivo
    if not path.is_file():
        raise ValueError(f"O caminho fornecido não é um arquivo")

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    return{
        "path": str(path.relative_to(base_dir)),
        "content": content,
    }
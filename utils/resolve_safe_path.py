"""
Módulo utilitário para resolver caminhos de arquivo de forma segura.
Verifica se o caminho está dentro do diretório permitido e resolve o caminho

Evitar caminhos absolutos ou relativas que possam levar à saída do diretório permitido.

"""
from pathlib import Path 
# =============================
# CONFIGURAÇÃO DE SEGURANÇA
# =============================

ALLOWED_DIR = Path(r'C:\Users\alark\OneDrive\Documentos\GitHub\Procedural-World-Simulation-Engine').resolve()



# =============================
# FUNÇÕES UTILITÁRIAS
# =============================

def resolve_safe_path(relative_str:str, *, base_dir=ALLOWED_DIR) -> Path:

    """
    Resolve um caminho de arquivo de forma segura, e garantir que 
    ele esteja dentro do diretório permitido.

    Args:
        relative_str (str): Caminho relativo a ser resolvido.
        base_dir (Path, opcional): Diretório base permitido. Padrão é ALLOWED_DIR.
    Returns:
        Path: Caminho resolvido dentro do diretório permitido.
    Raises:
        PermissionError: Se o caminho estiver fora do diretório permitido.

    """

    path = (base_dir / relative_str).resolve()

    if base_dir not in path.parents and path != base_dir:
        raise PermissionError('Acesso fora do diretório permitido')
    
    return path
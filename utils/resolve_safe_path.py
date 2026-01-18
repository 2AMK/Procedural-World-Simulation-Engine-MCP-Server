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

def resolve_safe_path(relative_str:str) -> Path:

    """
    Resolve um caminho de arquivo de forma segura, e garantir que 
    ele esteja dentro do diretório permitido.

    """

    path = (ALLOWED_DIR / relative_str).resolve()

    if ALLOWED_DIR not in path.parents and path != ALLOWED_DIR:
        raise PermissionError('Acesso fora do diretório permitido')
    
    return path
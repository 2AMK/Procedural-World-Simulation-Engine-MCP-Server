"""
Docstring for tools.get_info

Ferramenta modular que retorna a informação geral do sistema

"""
from utils.resolve_safe_path import ALLOWED_DIR

def get_info(args: dict):
    """
    Informações gerais sobre o repositório.

    Args:
        args (dict): Um dicionário. Atualmente não há argumentos necessários.

    Returns:
       dict: Um dicionário com informações gerais sobre o repositório
    Usage:
        get_info({})

    """
    return {
        "base_dir": str(ALLOWED_DIR),
        "description": "Procedural World Simulation Engine",
        "language": "Python",
        "focus": [
            "Procedural generation",
            "Layered world (z-levels)",
            "Simulation engine",
            "Software architecture"
        ]
    }
"""
Servidor FastMCP que expõe diversas ferramentas de introspecção
sobre o próprio código‑base.  O objetivo é fornecer um ponto de
entrada simples para LLMs (ou outras ferramentas) que necessitem
de informações contextuais do repositório.

A estrutura de ferramentas segue o padrão:
    @app.tool()
    async def nome_da_funcao(args: dict):
        # implementação
"""

import sys
from pathlib import Path

# Importa as utilidades e as ferramentas
from utils.resolve_safe_path import resolve_safe_path
from tools.list_files import list_files
from tools.read_file import read_file
from tools.tree_file import tree_file
from tools.get_info import get_info

# FastMCP é a camada que transforma async functions em endpoints HTTP
from mcp.server.fastmcp import FastMCP # Optei por FastMCP pois é compatível com Continue

# --- Configuração do servidor ---------------------------------------------

# Inicializa o servidor FastMCP
app = FastMCP(
    name="procedural-world-simulation-engine",
    version="0.1.0",
    instructions="""
    Este servidor expõe as informações do codebase para fornecer o contexto que LLM necessita
    """
)

# --- Ferramentas (expostas ao mundo) --------------------------------------
# Cada função é registrada como ferramenta com @app.tool
@app.tool()
async def list_files_tool(path: str = "."):
    """
    Lista arquivos e diretórios imediatamente abaixo de `path`.

    Parameters
    ----------
    path : str, optional
        Caminho relativo a partir da raiz do repositório. Padrão é `"."`.

    Returns
    -------
    dict
        Estrutura contendo `path` e uma lista `entries` com
        `name` e `type` ('file' ou 'dir').
    """
    return list_files({"path": path})

@app.tool()
async def read_file_tool(path: str):
    """
    Lê o conteúdo de um arquivo especificado por `path`.

    Parameters
    ----------
    path : str
        Caminho relativo ao repositório.

    Returns
    -------
    dict
        Contém a chave `content` com o texto lido.
    """
    return read_file({"path": path})

@app.tool()
async def tree_file_tool(path: str = ".", max_depth: int = 3):
    """
    Exibe uma representação em árvore dos diretórios.

    Parameters
    ----------
    path : str, optional
        Raiz da árvore. Padrão é `"."`.
    max_depth : int, optional
        Profundidade máxima da recursão. Padrão 3.

    Returns
    -------
    dict
        Estrutura JSON com a hierarquia de diretórios e arquivos.
    """
    return tree_file({"path": path, "max_depth": max_depth})

@app.tool()
async def get_info_tool():
    """
    Retorna metadados do repositório (nome, versão, instruções, etc.).
    """
    return get_info({})
    
# -------------------------------------------------------------------------
# Ponto de entrada principal
# -------------------------------------------------------------------------
# Inicia o servidor
if __name__ == "__main__":
    print("Server started", file=sys.stderr)
        # O método `run()` inicia o FastAPI / Uvicorn no background
    app.run()

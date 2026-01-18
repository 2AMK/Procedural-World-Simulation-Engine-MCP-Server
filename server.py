import sys
from pathlib import Path
from utils.resolve_safe_path import resolve_safe_path
from tools.list_files import list_files
from tools.read_file import read_file
from tools.tree_file import tree_file
from tools.get_info import get_info

from mcp.server.fastmcp import FastMCP

# Optei por FastMCP pois é compatível com Continue 

# Inicializa o servidor FastMCP
app = FastMCP(
    name="procedural-world-simulation-engine",
    version="0.1.0",
    instructions="""
    Este servidor expõe as informações do codebase para fornecer o contexto que LLM necessita
    """
)


# Cada função é registrada como ferramenta com @app.tool
@app.tool()
async def list_files_tool(path: str = "."):
    """Lista arquivos e diretórios"""
    return list_files({"path": path})

@app.tool()
async def read_file_tool(path: str):
    """Lê um arquivo"""
    return read_file({"path": path})

@app.tool()
async def tree_file_tool(path: str = ".", max_depth: int = 3):
    """Exibe árvore de diretórios"""
    return tree_file({"path": path, "max_depth": max_depth})

@app.tool()
async def get_info_tool():
    """Informações do repositório"""
    return get_info({})
    
# Inicia o servidor
if __name__ == "__main__":
    print("Server started", file=sys.stderr)
    app.run()

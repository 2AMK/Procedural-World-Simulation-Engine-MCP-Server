"""
Docstring for tests.test_server

Módulo de teste unitário para o servidor MCP.
"""


from anyio import Path
import pytest

from server import tree_file_tool

class FakeMCPServer:
    """Servidor MCP falso para testes unitários.
    
    Queremos testar o comportamento do servidor MCP sem iniciar o servidor real.
    """
    def __init__(self, base_dir:Path):
        self.base_dir = base_dir

    # Importar as funções reais do servidor MCP aqui
    def list_files_tool(self, path: str = "."):
        # Implementação simulada
        from tools.list_files import list_files
        return list_files({"path": path}, base_dir=self.base_dir)
    
    def read_file_tool(self, path: str):
        # Implementação simulada
        from tools.read_file import read_file
        content = read_file({"path": path}, base_dir=self.base_dir)
        return {"content": content}

    def tree_file_tool(self, path: str, max_depth: int = 2):
        # Implementação simulada
        from tools.tree_file import tree_file
        tree = tree_file({"path": path, "max_depth": max_depth}, base_dir=self.base_dir)

        return {"tree": tree}

    def get_info_tool(self):
        # Implementação simulada
        from tools.get_info import get_info
        return get_info(self.base_dir)
    

class TestFakeMCPServer:
    """Testes unitários para verificar se o fake server está chamando e retornando corretamente.
    Também verifica se as ferramentas estão integradas corretamente.
    """
    def setup_mock_mcp(self, name, version, instructions):
        from pathlib import Path
        return FakeMCPServer(base_dir=Path.cwd())

    @pytest.fixture
    def server(self):
        return self.setup_mock_mcp(
            name="procedural-world-simulation-engine",
            version="0.1.0",
            instructions="Este servidor expõe as informações do codebase para fornecer o contexto que LLM necessita"
        )

    def test_list_files_tool(self, server):
        result = server.list_files_tool(path=".")
        assert "entries" in result
        assert isinstance(result["entries"], list)

    def test_read_file_tool(self, server):
        result = server.read_file_tool(path="tests/test_server.py")
        assert "content" in result
        assert isinstance(result["content"], dict)

    def test_tree_file_tool(self, server):
        result = server.tree_file_tool(path=".", max_depth=2)
        assert "tree" in result
        assert isinstance(result["tree"], dict)
"""
Servidor MCP para projeto procedural-world-simulation-engine

Expõe as informações do codebase para fornecer o contexto que LLM precisará para gerar respostas.
Para isso, utiliza-se JSON para formatar as respostas (com a comunicação stdin/stdout).


"""
import sys
import json
from pathlib import Path
from utils.resolve_safe_path import resolve_safe_path
from tools.list_files import list_files
from tools.read_file import read_file
from tools.tree_file import tree_file
from tools.get_info import get_info


# =============================
# FUNÇÕES DE IO (MCP CORE)
# =============================

def send(msg:dict):
    """
    Esse módulo é responsável por enviar mensagens ao cliente. Ele aceita uma mensagem como parâmetro e a envia para o cliente. 
    A mensagem é convertida em JSON antes de ser enviada.

    Também sempre faz o stdour e faz flush para garantir que a mensagem seja enviada imediatamente.
    
    """
    sys.stdout.write(json.dumps(msg) + '\n') 
    sys.stdout.flush()

def read() -> dict:
    """
    Esse módulo é responsável por ler as mensagens do cliente. 
    Ele espera uma mensagem do cliente no formato de JSON formatado

    Lê a mensagem no formato de stdin e a converte em um objeto JSON. 
    Retorna o objeto JSON.
    """
    line = sys.stdin.readline()
    if not line:
        sys.exit(0) # Caso não haja mais linhas para ler, encerra o programa.
    return json.loads(line)  # Converte a linha lida em um objeto JSON.

# =============================
# UTILITÁRIOS INTERNOS
# =============================


# Função principal que processa as requisições do cliente.
# É um conjunto de ferramentas que podem ser chamadas pelo cliente.
# Ter cuidado com a segurança ao permitir que o cliente chame funções arbitrárias.


# =============================
# REGISTRO DAS TOOLS (MCP)
# =============================

TOOLS = {
    "list_files": {
        "description": "Lista arquivos e diretórios em um caminho",
        "input_schema": {
            "path": "string (opcional)"
        },
        "handler": list_files
    },
    "read_file": {
        "description": "Lê o conteúdo de um arquivo",
        "input_schema": {
            "path": "string (obrigatório)"
        },
        "handler": read_file
    },
    "tree_file": {
        "description": "Exibe a árvore de diretórios",
        "input_schema": {
            "path": "string (opcional)",
            "max_depth": "int (opcional)"
        },
        "handler": tree_file
    },
    "get_info": {
        "description": "Obtém informações gerais do repositório",
        "input_schema": {},
        "handler": get_info
    }
}



# =============================
# LOOP PRINCIPAL MCP
# =============================

while True:
    request = read()

    req_type = request.get("type")

    # Cliente pedindo lista de ferramentas
    if req_type == "list_tools":
        send({
            "type": "tools",
            "tools": [
                {
                    "name": name,
                    "description": tool["description"],
                    "input_schema": tool["input_schema"]
                }
                for name, tool in TOOLS.items()
            ]
        })

    # Cliente chamando uma ferramenta
    elif req_type == "call_tool":
        tool_name = request["name"]
        arguments = request.get("arguments", {})

        if tool_name not in TOOLS:
            send({
                "type": "error",
                "message": f"Tool '{tool_name}' not found"
            })
            continue

        try:
            result = TOOLS[tool_name]["handler"](arguments)
            send({
                "type": "tool_result",
                "name": tool_name,
                "content": result
            })
        except Exception as e:
            send({
                "type": "error",
                "message": str(e)
            })
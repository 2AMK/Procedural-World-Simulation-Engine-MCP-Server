# Procedural‑World‑Simulation‑Engine‑MCP‑Server
Um servidor de MCP que expõe informações de um repositório para LLM, fornecendo contextos necessários para as respostas.

## Funcionalidades
No momento, o projeto pode se servir como *boilerplate* para qualquer novo repositório que precise:

1. **Expor** metadados de arquivos e diretórios.
2. **Responder** consultas automatizadas via LLM (Large Language Model).
3. **Ser** simples de iniciar (um único comando `python server.py`).

Porém eventualmente, o projeto irá se especializar 


## Estrutura do Projeto
```
procedural‑world‑simulation‑engine-mcp-server/ 
│
├── README.md                ← Esta documentação
├── requirements.txt         ← Dependências Python
├── server.py                ← Ponto de entrada do servidor
├── tools/                   ← Ferramentas que o servidor expõe
│   ├── list_files.py
│   ├── read_file.py
│   ├── tree_file.py
│   └── get_info.py
└── utils/                   ← Utilitários de segurança e caminho
    └── resolve_safe_path.py
```

## Dependências
O servidor depende apenas de bibliotecas de propósito geral e da própria *FastMCP*:

```text
fastmcp==0.6.0
```

Instale tudo com:

```bash
pip install -r requirements.txt
```

*(Em produção, recomendamos criar um ambiente virtual `python -m venv venv` e ativá‑lo antes de instalar.)*

## Como rodar
Esse projeto é projetado para ser usado no Continue, porém é possível utilizar em outras aplicações que suportem MCP. Para rodar diretamente:

```bash
python server.py
```

O servidor escutará na porta **8000** (padrão do FastMCP).  
Você pode chamar as ferramentas via HTTP, por exemplo:

```bash
curl -X POST http://localhost:8000/tool/list_files_tool \
  -H "Content-Type: application/json" \
  -d '{"path": "."}'
```

## Como testar
Para rodar os testes unitários, tem que utilizar o Pytest.

Para rodar os testes no diretório `tests`, no terminal execute o comando:
```bash
pytest tests/

```
Alternativamente, caso não tivert acesso direto ao pytest, você pode rodar os testes via módulo do Python:
```bash
python -m pytest tests/
```


## Cobertura de testes
É possível verificar a cobertura dos testes utilizando o módulo `coverage`. 

Para rodar a cobertura dos testes, no terminal execute:
```bash
coverage run -m pytest tests/
coverage report -m
```
Para gerar um relatório de cobertura:
```bash
coverage html
```
Depois de executar esse comando, é só abrir o arquivo `index.html` gerado na pasta.

## Ferramentas Expostas

| Função | Descrição | Argumentos | Retorno |
|--------|-----------|------------|---------|
| `list_files_tool` | Lista arquivos e diretórios dentro de um caminho relativo | `path: str` | Lista de entradas (`name`, `type`) |
| `read_file_tool` | Lê o conteúdo de um arquivo | `path: str` | Conteúdo textual |
| `tree_file_tool` | Mostra árvore de diretórios (recursiva) | `path: str`, `max_depth: int` | Estrutura JSON da árvore |
| `get_info_tool` | Retorna informações básicas do repositório | _nenhum_ | JSON com nome, versão, instruções, etc. |

## Uso como Boilerplate
1. **Copie** a pasta do projeto para o seu novo repositório.
2. **Renomeie** os arquivos de configuração (`README.md`, `requirements.txt`, `server.py`).
3. **Atualize** a constante `name` e `version` em `server.py` para refletir seu projeto.
4. **Adicione** novas ferramentas na pasta `tools/` seguindo o mesmo padrão (`@app.tool()`).
5. **Instale** as dependências adicionais em `requirements.txt`.

## Contribuindo
Pull requests são bem-vindos! Se precisar de uma nova ferramenta ou correção, abra uma issue primeiro.

## Licença

A licença desse repositório é MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
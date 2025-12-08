# SENTINELA

## Instalação

Recomenda-se criar um ambiente virtual e instalar as dependências do projeto.

Opção A — venv + pip

```bash
python3 -m venv .venv
source .venv/bin/activate
cd fast_sentinela
python -m pip install --upgrade pip
python -m pip install .
```

Opção B — Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

> Observação: o `pyproject.toml` declara `requires-python = ">=3.14,<4.0"`. Se sua máquina não tiver Python 3.14, ajuste localmente para `>=3.10` ou use um ambiente que suporte 3.14.

## Como rodar

Inicie o servidor com `uvicorn` apontando para a instância `app` em `fast_sentinela.app`:

```bash
# com venv ativo
uvicorn fast_sentinela.app:app --reload --host 0.0.0.0 --port 8000

# ou com poetry
poetry run uvicorn fast_sentinela.app:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints úteis

- `GET /sent/ping` — checa se a API está no ar (retorna `{"pong"}`).
- `GET /sent/predict?latitude=<lat>&longitude=<lon>&data_pas=<iso>` — endpoint de predição; `data_pas` é opcional.

## Testes rápidos

```bash
curl http://127.0.0.1:8000/sent/ping
curl "http://127.0.0.1:8000/sent/predict?latitude=-23.5489&longitude=-46.6388"
```

## Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

Se quiser, eu posso ajustar `pyproject.toml` para uma faixa de Python mais comum (`>=3.10`) ou rodar os comandos aqui para testar o servidor.
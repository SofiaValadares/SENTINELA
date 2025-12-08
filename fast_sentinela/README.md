# fast_sentinela

Este `README.md` existe para permitir a geração de metadata durante a instalação do pacote.

Para instruções completas de instalação e execução, veja o `README.md` na raiz do repositório.

Instruções rápidas (dentro do diretório `fast_sentinela`):

```bash
# ative o virtualenv (.venv) e execute:
python -m pip install --upgrade pip
python -m pip install .

# para iniciar o servidor
uvicorn fast_sentinela.app:app --reload --host 0.0.0.0 --port 8000
```

Swagger UI: `http://127.0.0.1:8000/docs`

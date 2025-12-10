# 🌱 **SENTINELA**

O **Sentinela** é um sistema de **monitoramento e análise ambiental focado na Caatinga**, desenvolvido por estudantes de **Ciência da Computação da CESAR School**, integrantes do grupo **Canidé**.

Seu objetivo é oferecer uma **API simples, acessível e eficiente** para **analisar dados relacionados ao risco de incêndios e focos de queimadas** na região da Caatinga, utilizando conjuntos de dados ambientais reais.

Além disso, o Sentinela foi pensado com um viés **educativo**, permitindo que estudantes em períodos iniciais de computação possam **aprender a trabalhar com APIs, dados reais e aplicações ambientais**, explorando tecnologia em um tema relevante para o Brasil.

🔎 **O Sentinela transforma dados brutos em informações úteis**, auxiliando pesquisas, iniciativas ambientais e o desenvolvimento de soluções tecnológicas voltadas à preservação do bioma — de forma simplificada para facilitar o aprendizado.

📌 **Documentação completa**  
Disponível em breve. *(link será adicionado futuramente)*

---

## 👥 **Grupo Canidé**

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LuizaCalife">
        <img src="https://avatars.githubusercontent.com/u/109395661?v=4" width="100px;" alt="Maria Luiza Calife"/><br>
        <sub><b>Maria Luiza Calife</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/dan-albuquerque">
        <img src="https://avatars.githubusercontent.com/u/114592376?v=4" width="100px;" alt="Foto Danilo Albuquerque"/><br>
        <sub><b>Danilo Albuquerque</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/guiga-sa">
        <img src="https://avatars.githubusercontent.com/u/123979639?v=4" width="100px;" alt="Foto Guilherme Silveira"/><br>
        <sub><b>Guilherme Silveira</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SofiaValadares">
        <img src="https://avatars.githubusercontent.com/u/113111708?v=4" width="100px;" alt="Foto Sofia Valadares"/><br>
        <sub><b>Sofia Valadares</b></sub>
      </a>
    </td>
</table>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/joaovfittipaldi">
        <img src="https://avatars.githubusercontent.com/u/132574730?v=4" width="100px;" alt="Foto João Vítor Fittipaldi"/><br>
        <sub><b>João Vítor Fittipaldi</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/caetrias">
        <img src="https://avatars.githubusercontent.com/u/127201879?v=4" width="100px;" alt="Foto Gabriel Caetano"/><br>
        <sub><b>Gabriel Caetano</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/guiga-sa">
        <img src="https://avatars.githubusercontent.com/u/123979639?v=4" width="100px;" alt="Foto Guilherme Silveira"/><br>
        <sub><b>Guilherme Silveira</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SofiaValadares">
        <img src="https://avatars.githubusercontent.com/u/113111708?v=4" width="100px;" alt="Foto Sofia Valadares"/><br>
        <sub><b>Sofia Valadares</b></sub>
      </a>
    </td>
</table>

---

## 🧩 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Git**
- **Python 3.10+** (ou versão compatível definida no `pyproject.toml`)
- Opcionalmente: **Postman** para testar a API usando a coleção fornecida ao final deste arquivo.

---

## 📥 Como clonar o repositório

Em qualquer sistema operacional (Windows, Linux ou macOS):

```bash
git clone https://github.com/SofiaValadares/SENTINELA.git
cd SENTINELA
````

> Certifique-se de sempre rodar os próximos comandos dentro da pasta do projeto (`SENTINELA`), onde estão o `pyproject.toml` e o código da API.

---

## 🐍 Configurando o ambiente virtual (venv)

### Windows (PowerShell ou CMD)

```bash
# ainda dentro da pasta SENTINELA
python -m venv .venv

# Ativar o ambiente virtual
# PowerShell:
.\.venv\Scripts\Activate.ps1

# CMD:
.\.venv\Scripts\activate.bat

# Atualizar o pip e instalar o projeto
cd .\fast_sentinela 
python -m pip install --upgrade pip
python -m pip install .
```

### Linux / macOS

```bash
# ainda dentro da pasta SENTINELA
python3 -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Atualizar o pip e instalar o projeto
cd ./fast_sentinela 
python -m pip install --upgrade pip
python -m pip install .
```

> Observação: o `pyproject.toml` pode declarar algo como `requires-python = ">=3.14,<4.0"`.
> Se sua máquina não tiver Python 3.14, você pode:
>
> * Ajustar localmente para `>=3.10` **apenas para desenvolvimento**, ou
> * Usar um ambiente que suporte Python 3.14 (ex.: pyenv, containers, etc.).

---

## ▶️ Como rodar o projeto (qualquer sistema operacional)

Com o ambiente virtual **ativo** (`.venv`) e dentro da pasta **fast_sentinela**, suba a API com o `uvicorn`:

```bash
uvicorn fast_sentinela.app:app --reload --host 0.0.0.0 --port 8000
```

* A API ficará disponível em: `http://127.0.0.1:8000`
* Os endpoints principais ficam sob o prefixo: `/sent`

---

## 🔌 Endpoints úteis

* `GET /sent/ping`
  Verifica se a API está no ar.
  **Resposta esperada:** `{"pong": true}` (ou similar)

* `GET /sent/predict?latitude=<lat>&longitude=<lon>&days_without_rain=<dias>`
  Endpoint de predição de risco, usando latitude, longitude e dias sem chuva.
  Parâmetros:

  * `latitude` (obrigatório)
  * `longitude` (obrigatório)
  * `days_without_rain` (obrigatório)
  * `data_pas` (opcional, usado em alguns cenários de teste)

* `POST /sent/image`
  Recebe uma imagem (campo `file` em `form-data`) e retorna uma análise da imagem, incluindo:

  * se há **incêndio** detectado
  * a imagem tratada/recortada em **base64**

Para mais detalhes sobre os endponts visite a documentação completa em  *(link será adicionado futuramente)*
---

## 📬 Coleção Postman

Você pode importar o JSON abaixo diretamente no **Postman** para testar os endpoints `ping`, `predict` e `image`.

```json
{
  "info": {
    "_postman_id": "acb38050-d6df-4c33-86a5-6c1744df2e3f",
    "name": "Sentinela",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    "_exporter_id": "38646115"
  },
  "item": [
    {
      "name": "predict",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "GET",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "{{localhost}}/predict?latitude=-10.145694&longitude=-36.876551&days_without_rain=10",
          "host": [
            "{{localhost}}"
          ],
          "path": [
            "predict"
          ],
          "query": [
            {
              "key": "data_pas",
              "value": "0",
              "disabled": true
            },
            {
              "key": "latitude",
              "value": "-10.145694"
            },
            {
              "key": "longitude",
              "value": "-36.876551"
            },
            {
              "key": "days_without_rain",
              "value": "10"
            }
          ]
        }
      },
      "response": []
    },
    {
      "name": "ping",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{localhost}}/ping",
          "host": [
            "{{localhost}}"
          ],
          "path": [
            "ping"
          ]
        }
      },
      "response": []
    },
    {
      "name": "image",
      "event": [
        {
          "listen": "test",
          "script": {
            "exec": [
              "let data = pm.response.json();\r",
              "\r",
              "pm.visualizer.set(\r",
              "    `\r",
              "    <html>\r",
              "      <body>\r",
              "        <h3>insendio: {{insendio}}</h3>\r",
              "        <img src=\"data:image/png;base64,{{img}}\" style=\"max-width: 100%; border: 1px solid #ccc;\" />\r",
              "      </body>\r",
              "    </html>\r",
              "    `,\r",
              "    {\r",
              "        insendio: data.insendio,\r",
              "        img: data.imagem_base64\r",
              "    }\r",
              ");\r",
              ""
            ],
            "type": "text/javascript",
            "packages": {},
            "requests": {}
          }
        }
      ],
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "formdata",
          "formdata": [
            {
              "key": "file",
              "type": "file",
              "src": "postman-cloud:///1f0d5ef7-6b3f-42d0-9658-1f66ef754dc5"
            }
          ]
        },
        "url": {
          "raw": "{{localhost}}/image",
          "host": [
            "{{localhost}}"
          ],
          "path": [
            "image"
          ]
        }
      },
      "response": []
    }
  ],
  "variable": [
    {
      "key": "localhost",
      "value": "http://127.0.0.1:8000/sent",
      "type": "default"
    }
  ]
}
```

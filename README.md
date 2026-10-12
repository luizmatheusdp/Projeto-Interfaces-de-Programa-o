# CC0464 — Projeto de Extensão

Projeto desenvolvido para a disciplina **CC0464 — Interfaces de Programação de Aplicação**, da **Universidade Federal do Ceará (UFC)**, semestre **2026.2**.

## 👥 Equipe

- **Luiz Matheus**
- **Wanderson Soares**

## 📌 Sobre o projeto

Este repositório contém o desenvolvimento de uma ação de extensão voltada à criação de uma **API pública para consulta de dados sobre municípios do Ceará**.

A API utilizará dados públicos do **Instituto Brasileiro de Geografia e Estatística (IBGE)**, disponibilizando uma forma simples e documentada de consultar informações municipais.

O projeto busca facilitar o acesso e o reúso de dados públicos por pessoas externas à universidade, especialmente:

- Professores e estudantes da educação básica;
- Jornalistas e produtores de conteúdo;
- Organizações e coletivos que utilizem dados públicos;
- Pessoas que necessitem consultar informações sobre municípios cearenses.

## 🎯 Objetivo

Disponibilizar uma API simples que permita consultar informações sobre municípios do Ceará a partir de seu código IBGE.

A primeira versão terá como objetivo disponibilizar uma rota funcional, utilizando dados reais do IBGE e retornando as informações em formato JSON.

Exemplo de rota:

```
GET /municipios/{codigo}
```

## 🚀 Como instalar e executar

Recomenda-se usar um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API (http://127.0.0.1:8000):

```bash
uvicorn src.main:app --reload
```

Documentação interativa disponível em http://127.0.0.1:8000/docs.

## 📡 Exemplo de chamada

```bash
curl http://127.0.0.1:8000/municipios/2304400
```

Resposta:

```json
{
  "codigo": 2304400,
  "nome": "Fortaleza",
  "microrregiao": "Fortaleza",
  "mesorregiao": "Metropolitana de Fortaleza",
  "regiao_imediata": "Fortaleza",
  "regiao_intermediaria": "Fortaleza",
  "uf": "CE",
  "uf_nome": "Ceará",
  "regiao": "Nordeste"
}
```

## 📚 Fonte de dados e licença

Os dados são fornecidos pela **API de Localidades do IBGE** (Instituto Brasileiro de Geografia e Estatística):

- Fonte: https://servicodados.ibge.gov.br/api/docs/localidades
- Os dados do IBGE podem ser usados livremente, desde que citada a fonte (CC BY 2.5 BR).
  Mais informações: https://www.ibge.gov.br/acesso-informacao/acoes-e-programas/termos-de-uso.html

## ⚠️ Limitações

- A API depende do serviço online do IBGE: se ele estiver indisponível, a API responde com erro **503**.
- Aceita apenas consulta de **um município por vez**, pelo código IBGE de 7 dígitos. Não há busca por nome nem listagem dos municípios.
- Retorna somente dados de localização (nome, microrregião, mesorregião, regiões e UF). Ainda **não** inclui população nem indicadores socioeconômicos.
- Não há cache: cada requisição consulta o IBGE novamente, o que pode tornar respostas repetidas mais lentas.
- Em caso de falha inesperada do serviço do IBGE, a resposta pode ser **502**.

## 📝 Como cada parte da estrutura funciona

- `src/main.py` → contém a implementação da API de consulta dos municípios do Ceará.
- `testes/test_municipios.py` → contém os testes automatizados para verificar o funcionamento da API.
- `dados/README.md` → apresenta informações sobre as fontes de dados utilizadas, incluindo os dados disponibilizados pelo IBGE.
- `evidencias/` → armazena as evidências relacionadas à execução e aos resultados da ação de extensão (`evidencias.csv`).
- `docs/plano-de-acao.md` → contém o plano de ação da equipe, com o problema, público, produto, cronograma, papéis e indicadores.
- `diario-de-bordo.md` → registra semanalmente as atividades, dificuldades e conhecimentos da equipe.
- `README.md` → apresenta o projeto e explica como instalar, executar e utilizar a API.
- `marco-1.md` → contém a ficha de entrega e autopontuação do Marco 1.
- `requirements.txt` → lista as dependências necessárias para instalar e executar o projeto.



## 📁 Estrutura do repositório

```text
.
├── docs/
│   └── plano-de-acao.md
├── dados/
│   └── README.md
├── src/
│   ├── __init__.py
│   └── main.py
├── testes/
│   └── test_municipios.py
├── evidencias/
│   ├── README.md
│   └── evidencias.csv
├── diario-de-bordo.md
├── README.md
├── requirements.txt
├── .gitignore
└── marco-1.md


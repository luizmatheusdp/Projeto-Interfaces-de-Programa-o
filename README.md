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

http
GET /municipios/{codigo}

Como cada parte da estrutura funciona:

- `src/main.py` → contém a implementação da API de consulta dos municípios do Ceará.
- `testes/test_municipios.py` → contém os testes automatizados para verificar o funcionamento da API.
- `dados/README.md` → apresenta informações sobre as fontes de dados utilizadas, incluindo os dados disponibilizados pelo IBGE.
- `evidencias/` → armazena as evidências relacionadas à execução e aos resultados da ação de extensão.
- `docs/plano-de-acao.md` → contém o plano de ação da equipe, com o problema, público, produto, cronograma, papéis e indicadores.
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
│   └── README.md
├── README.md
├── requirements.txt
├── .gitignore
└── marco-1.md


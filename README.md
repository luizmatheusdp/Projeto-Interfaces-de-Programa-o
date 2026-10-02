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

## 📁 Estrutura do repositório

```text
.
├── docs/
│   └── plano-de-acao.md
├── dados/
│   └── README.md
├── src/
│   └── README.md
├── evidencias/
│   └── README.md
└── README.md

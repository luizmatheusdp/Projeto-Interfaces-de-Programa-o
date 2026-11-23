
# CC0464 — Projeto de Extensão

Projeto desenvolvido para a disciplina **CC0464 — Interfaces de Programação de Aplicação**, da **Universidade Federal do Ceará (UFC)**, semestre **2026.2**.

## 👥 Equipe

- **Luiz Matheus Silva Carvalho**
- **Wanderson Soares da Silva**

## 📌 Sobre o projeto

Este repositório contém o desenvolvimento de uma ação de extensão voltada à criação de uma **API pública para consulta de dados sobre municípios do Ceará**.

A API utiliza dados públicos do **Instituto Brasileiro de Geografia e Estatística (IBGE)**, oferecendo uma forma simples e documentada de consultar informações municipais.

O projeto busca facilitar o acesso e o reúso de dados públicos por pessoas externas à universidade, especialmente:

- Professores e estudantes da educação básica;
- Jornalistas e produtores de conteúdo;
- Organizações e coletivos que utilizem dados públicos;
- Pessoas que necessitem consultar informações sobre municípios cearenses.

## 🎯 Objetivo

Disponibilizar uma API simples que permita consultar informações sobre municípios do Ceará a partir de seu código IBGE.

A API recebe uma solicitação, consulta os dados do IBGE e retorna as informações do município em formato JSON.

## 🌐 Acesse a API

A API está publicada e pode ser utilizada diretamente pela internet, sem necessidade de instalação.

**Endereço público:**

https://api-municipios-ceara.onrender.com

**Documentação interativa:**

https://api-municipios-ceara.onrender.com/docs

Na documentação interativa, é possível visualizar a rota disponível, informar um código de município e executar uma consulta.

## 📖 Como utilizar a API

### 1. Consultar um município

A API possui a seguinte rota:

`GET /municipios/{codigo}`

Parâmetro:

| Parâmetro | Tipo | Descrição |
|---|---|---|
| codigo | String | Código IBGE de 7 dígitos do município |

Exemplo: consultar Fortaleza.

**URL completa:**

https://api-municipios-ceara.onrender.com/municipios/2304400

### 2. Exemplo utilizando navegador

Basta copiar o endereço abaixo e abrir no navegador:

https://api-municipios-ceara.onrender.com/municipios/2304400

O resultado será apresentado em formato JSON.

### 3. Exemplo utilizando cURL

```bash
curl https://api-municipios-ceara.onrender.com/municipios/2304400
```

### 4. Exemplo de resposta

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

### 5. Entendendo os campos da resposta

| Campo | Descrição |
|---|---|
| codigo | Código oficial do município no IBGE |
| nome | Nome do município |
| microrregiao | Microrregião do município |
| mesorregiao | Mesorregião do município |
| regiao_imediata | Região geográfica imediata |
| regiao_intermediaria | Região geográfica intermediária |
| uf | Sigla do estado |
| uf_nome | Nome do estado |
| regiao | Região brasileira |

## ⚠️ Validações e possíveis erros

A API realiza validações para evitar consultas inválidas e garantir que sejam retornados somente municípios do Ceará.

| Situação | Código HTTP | Descrição |
|---|---|---|
| Consulta válida | 200 | Município encontrado e pertencente ao Ceará |
| Código inválido | 404 | Código diferente de 7 dígitos numéricos |
| Município inexistente | 404 | Município não encontrado |
| Município de outro estado | 404 | Município não pertence ao Ceará |
| Falha de conexão com IBGE | 503 | Não foi possível consultar o serviço do IBGE |
| Erro inesperado do IBGE | 502 | O serviço do IBGE retornou um erro |

### Exemplos de consultas inválidas

**Código fora do padrão:**

```bash
curl https://api-municipios-ceara.onrender.com/municipios/abc
```

Resposta esperada:

```json
{
  "detail": "Código inválido. Informe um código IBGE com 7 dígitos numéricos."
}
```

**Município de outro estado:**

```bash
curl https://api-municipios-ceara.onrender.com/municipios/3304557
```

Resposta esperada:

```json
{
  "detail": "Município fora do estado do Ceará."
}
```

## 🚀 Como instalar e executar localmente

Para executar o projeto em seu computador, é necessário ter Python 3 instalado.

### 1. Clonar o repositório

```bash
git clone https://github.com/luizmatheusdp/Projeto-Interfaces-de-Programa-o.git
```

Entre na pasta:

```bash
cd Projeto-Interfaces-de-Programa-o
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

Ativar no Linux/macOS:

```bash
source .venv/bin/activate
```

Ativar no Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a API

```bash
uvicorn src.main:app --reload
```

A API ficará disponível localmente em:

http://127.0.0.1:8000

A documentação interativa local estará disponível em:

http://127.0.0.1:8000/docs

## 🧪 Como executar os testes

O projeto utiliza pytest para verificar o funcionamento da API.

Execute:

```bash
python -m pytest -v
```

Os testes verificam:

- Consulta válida de Fortaleza;
- Rejeição de códigos inválidos;
- Rejeição de municípios que não pertencem ao Ceará.

Resultado esperado:

```text
3 passed
```

## 📚 Fonte de dados e licença

Os dados são fornecidos pela **API de Localidades do IBGE** (Instituto Brasileiro de Geografia e Estatística).

- Documentação: https://servicodados.ibge.gov.br/api/docs/localidades
- Serviço utilizado: https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}
- Órgão responsável: Instituto Brasileiro de Geografia e Estatística (IBGE).

Os dados do IBGE podem ser utilizados e reproduzidos livremente, desde que citada a fonte, conforme os termos de uso e licença CC BY 2.5 BR.

Mais informações:

https://www.ibge.gov.br/acesso-informacao/acoes-e-programas/termos-de-uso.html

## ⚠️ Limitações

- A API consulta somente municípios do Ceará.
- Aceita somente códigos IBGE de 7 dígitos numéricos.
- Não possui busca por nome nem listagem de municípios.
- Retorna somente informações de localização e divisão regional.
- Ainda não disponibiliza população ou indicadores socioeconômicos.
- Depende da disponibilidade do serviço online do IBGE.
- Não possui cache, realizando uma consulta ao IBGE a cada requisição.
- O serviço gratuito de hospedagem pode apresentar demora na primeira requisição após períodos de inatividade.

## 🔮 Melhorias futuras

A partir dos testes e sugestões recebidas de usuários externos, foram identificadas possibilidades de evolução:

- Simplificar ainda mais a experiência de utilização;
- Ampliar os exemplos de consultas na documentação;
- Avaliar a inclusão de informações populacionais;
- Estudar a possibilidade de disponibilizar informações climáticas por município.

Essas sugestões serão avaliadas conforme a disponibilidade de tempo, fontes de dados e escopo do projeto.

## 📝 Como cada parte da estrutura funciona

- `src/main.py` → implementação da API de consulta dos municípios do Ceará.
- `testes/test_municipios.py` → testes automatizados da API.
- `dados/README.md` → documentação das fontes de dados utilizadas.
- `evidencias/` → registros e evidências relacionadas à ação de extensão.
- `docs/plano-de-acao.md` → plano de ação da equipe.
- `diario-de-bordo.md` → registro semanal das atividades e dificuldades.
- `marco-1.md` → ficha de entrega e autopontuação do Marco 1.
- `marco-2.md` → ficha de entrega e autopontuação do Marco 2.
- `requirements.txt` → dependências necessárias para executar o projeto.

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
│   ├── prints/
│   ├── README.md
│   ├── convite-externo.md
│   ├── evidencias.csv
│   ├── requisicao-fortaleza.txt
│   ├── requisicao-codigo-invalido.txt
│   ├── requisicao-fora-do-ce.txt
│   └── testes-pytest.txt
├── diario-de-bordo.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

**Projeto desenvolvido como ação de extensão da disciplina CC0464 — Interfaces de Programação de Aplicação, Universidade Federal do Ceará (UFC), semestre 2026.2.**

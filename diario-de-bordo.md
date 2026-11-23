# Diário de Bordo

Registro semanal das atividades da equipe. Cada entrada é adicionada **na semana**, durante a execução, e lista **os dois integrantes** (Luiz Matheus e Wanderson), o que foi feito e as dificuldades encontradas.

---

## 11/10/2026 — Correções, testes e documentação da API

**Participantes:** Wanderson Soares

**O que foi feito:**

- Corrigido o tratamento de código inválido na API: códigos inexistentes ou não numéricos (ex.: `9999999`, `abc`) agora retornam erro **404** em vez de erro 500.
- Corrigido o campo `microrregiao`, que retornava a sigla da UF; agora retorna o nome da microrregião.
- Ampliada a resposta da rota `/municipios/{codigo}` com os campos `mesorregiao`, `regiao_imediata`, `regiao_intermediaria`, `uf` e `uf_nome`.
- Adicionados testes automatizados cobrindo dois casos: Fortaleza (`2304400`) retorna **200** e código inválido retorna **404**.
- Atualizado o `README.md` com instruções de instalação e execução, exemplo de chamada, fonte dos dados e licença do IBGE.
- Validados os códigos `2304400` (Fortaleza/CE), `3304557` (Rio de Janeiro/RJ) e `2927408` (Salvador/BA) contra a API real do IBGE.

**Dificuldades encontradas:**

- A API do IBGE responde com lista vazia (HTTP 200) para códigos inválidos, o que causava erro 500 no código anterior; o tratamento foi ajustado para devolver 404 nesses casos.
- Ocorreu um timeout transitório ao consultar um dos municípios; a API já trata essa situação retornando 503.

**Próximos passos:**

- Validar a API com usuários externos à UFC antes do Marco 2.
- Avaliar inclusão de novos dados (população, indicadores) e melhorias de desempenho.

  ---

## 13/11/2026 — Marco 2: filtro do Ceará, validação e alcance

**Participantes:** Wanderson Soares, Luiz Matheus Silva Carvalho

**O que foi feito:**

- Implementado o **filtro do Ceará**: a API agora só retorna municípios do Ceará; códigos de outros estados retornam erro **404** ("Município fora do estado do Ceará").
- Adicionada a **validação do código** (7 dígitos numéricos): códigos fora do padrão retornam **404** imediatamente, sem consultar o IBGE, eliminando os erros 500/502 causados por entradas malformadas.
- Adicionado teste automatizado para o filtro do Ceará (`test_codigo_fora_do_ce_devolve_404`), totalizando 3 testes passando.
- Atualizado o `README.md` com o comando `python -m pytest` e com a documentação coerente com o comportamento atual da API (somente Ceará, código de 7 dígitos).
- Preenchido o `dados/README.md` com a fonte (URL), os termos de uso do IBGE conferidos (CC BY 2.5 BR) e a periodicidade de atualização.
- Iniciado o contato com os **3 usuários externos** previstos no plano de ação, cujo alcance será contabilizado na nota do Marco 2.

**Dificuldades encontradas:**

- A validação de 7 dígitos exige cuidado para não bloquear códigos válidos; optou-se por validar o formato antes de chamar o serviço do IBGE.
- O contato com usuários externos depende da disponibilidade das pessoas; os retornos serão registrados no `evidencias.csv` conforme chegarem.


---

## 22/11/2026 — Publicação da API, testes externos e melhorias na documentação

**Participantes:** Luiz Matheus Silva Carvalho e Wanderson Soares da Silva.

**O que foi feito:**

- Publicada a API de consulta de municípios do Ceará na plataforma Render, disponibilizando acesso público ao produto.
- Configurado o serviço de hospedagem utilizando o repositório do GitHub.
- Disponibilizado o endereço público da API: https://api-municipios-ceara.onrender.com.
- Disponibilizada a documentação interativa da API por meio do Swagger: https://api-municipios-ceara.onrender.com/docs.
- Realizados testes automatizados localmente, com os três testes existentes passando.
- Atualizado o arquivo `evidencias/convite-externo.md` com o endereço público da API, substituindo o endereço local que não permitia o acesso por pessoas externas.
- Enviados convites para três pessoas externas à UFC, solicitando que utilizassem a API e avaliassem sua facilidade de uso.
- Registrados os três contatos e seus respectivos retornos no arquivo `evidencias/evidencias.csv`.
- Recebidos três feedbacks de usuários externos:
  - O primeiro relatou dificuldade para compreender o funcionamento da API.
  - O segundo sugeriu disponibilizar informações climáticas dos municípios.
  - O terceiro apontou a necessidade de uma documentação mais completa, com explicação das rotas e dos parâmetros.
- Iniciada a melhoria da documentação do `README.md`, incluindo exemplos de utilização, explicação dos campos retornados, parâmetros, possíveis erros e endereço público do serviço.

**Dificuldades encontradas:**

- Inicialmente, o convite externo utilizava o endereço `127.0.0.1`, que permite acesso somente ao computador onde a API está executando.
- Foi necessário configurar a hospedagem em uma plataforma externa para disponibilizar o produto publicamente.
- Os feedbacks demonstraram que a existência de uma rota funcional não garante que todos os usuários consigam compreender e utilizar a API facilmente.
- A sugestão de inclusão de informações climáticas exigiria uma nova fonte de dados e ampliação do escopo, sendo considerada uma possibilidade de melhoria futura.

**Aprendizados:**

- A publicação de uma API é importante para permitir que pessoas externas consigam realmente utilizar o produto.
- A documentação precisa explicar não apenas como executar a aplicação, mas também como realizar consultas e interpretar as respostas.
- O retorno de usuários externos permite identificar dificuldades que podem não ser percebidas durante o desenvolvimento pela própria equipe.
- Foi possível compreender melhor a importância de validar a utilidade e a facilidade de uso do produto com pessoas fora da equipe.

**Próximos passos:**

- Finalizar e revisar a documentação da API.
- Registrar os prints dos convites enviados e dos retornos recebidos.
- Atualizar as evidências de alcançabilidade e resultados no repositório.
- Continuar acompanhando a utilização da API e avaliar possíveis melhorias.
- Consolidar o diário de bordo e preparar a entrega final do projeto.

- Consolidar os retornos dos usuários externos e registrar as evidências de alcance.
- Avaliar inclusão de novos dados (população, indicadores) e melhorias de desempenho.


# Entrega de marco — Marco 2

## Identificação

- **Equipe:** Luiz Matheus Silva Carvalho — 515145; Wanderson Soares da Silva — 538348
- **Marco e data:** Marco 2 — 13/11/2026 (atualização em 22/11/2026)
- **Trilha:** A - API sobre municípios do Ceará com dados do IBGE
- **Endereço público do produto:** https://api-municipios-ceara.onrender.com
- **Commit ou tag desta entrega:** `59beca1` (atualizar caso exista um commit mais recente para esta entrega).

O endereço público permite que outras pessoas acessem a API sem precisar executar o projeto localmente.

## Campo 1 — O que funciona hoje

1. Acessar a API publicamente pelo endereço https://api-municipios-ceara.onrender.com.

2. Consultar a documentação interativa pelo endereço https://api-municipios-ceara.onrender.com/docs.

3. Fazer uma requisição para a rota de municípios informando o código `2304400` (Fortaleza) e receber uma resposta em formato JSON:

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

4. Fazer uma requisição informando um código de outro estado (ex.: `3304557`, Rio de Janeiro) e receber erro `404` ("Município fora do estado do Ceará.").

5. Fazer uma requisição informando um código que não tenha 7 dígitos numéricos (ex.: `abc` ou `23`) e receber erro `404`, sem derrubar a API.

6. Executar os testes automatizados com `python -m pytest -v`, obtendo 3 testes aprovados.

## Campo 2 — O que mudou desde o marco anterior

- **Passou a existir:**
  - Filtro do Ceará: a API aceita somente municípios do Ceará;
  - Validação de códigos IBGE com 7 dígitos numéricos;
  - Terceiro teste automatizado para verificar códigos de outros estados, totalizando 3 testes passando;
  - Documentação atualizada no `README.md`, com instruções de instalação, execução e testes;
  - `dados/README.md` com informações sobre a fonte de dados, termos de uso e periodicidade;
  - Publicação da API na plataforma Render, utilizando o plano gratuito;
  - Disponibilização de um endereço público para acesso externo;
  - Envio de convites para três pessoas externas à UFC por WhatsApp;
  - Registro das evidências dos convites enviados em `evidencias/prints/`;
  - Recebimento de três retornos qualitativos de usuários externos;
  - Atualização do `evidencias/evidencias.csv` com os registros de alcance e feedbacks;
  - Atualização do `diario-de-bordo.md` com o registro das atividades de publicação e avaliação externa.

- **Foi cortado, e por quê:** o comportamento de retornar dados de municípios de qualquer estado foi removido, pois o escopo da ação é o Ceará.

## Campo 3 — Alcance

Os números são baseados nos registros do arquivo `evidencias/evidencias.csv`.

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| Alcançabilidade | 3 pessoas externas à UFC utilizando a API | 3 convites enviados | `evidencias/prints/` e `evidencias/evidencias.csv` |
| Retorno qualitativo | 3 retornos de usuários externos | 3 retornos recebidos | `evidencias/convite-externo.md` e `evidencias/evidencias.csv` |
| Resultado do produto | Pelo menos 1 rota funcional, documentada e acessível publicamente | 1 rota funcional e publicada | https://api-municipios-ceara.onrender.com |
| Formação acadêmica | 1 entrada por semana no diário de bordo | Entradas registradas em 11/10, 13/11 e 22/11 | `diario-de-bordo.md` |

### Feedback dos usuários externos

- **Usuário 1:** relatou dificuldade para entender como a API funciona.
- **Usuário 2:** sugeriu a inclusão de informações sobre o clima do município consultado.
- **Usuário 3:** apontou a necessidade de uma documentação mais completa, explicando os endpoints e parâmetros disponíveis.

Os retornos demonstram que a API atende à funcionalidade técnica proposta, mas ainda existem oportunidades de melhoria na experiência de utilização e na documentação.

## Campo 4 — Obstáculo e replanejamento

Durante o desenvolvimento e a publicação da API, foram identificados os seguintes obstáculos:

- A API do IBGE responde com lista vazia (HTTP 200) para códigos inválidos, o que poderia causar erro 500. O problema foi resolvido com a validação do código e o tratamento adequado de municípios não encontrados.
- Ocorreram timeouts transitórios do serviço do IBGE, tratados pela API com resposta 503.
- Inicialmente, o convite enviado aos usuários continha o endereço `127.0.0.1`, que permite acesso somente à máquina onde a aplicação está sendo executada.
- Para solucionar esse problema, a equipe publicou a API no Render, disponibilizando um endereço acessível pela internet.
- Os usuários externos apontaram dificuldades para compreender o funcionamento da API e sugeriram melhorias na documentação.

### Replanejamento

Para o próximo marco, a equipe pretende:

- Melhorar a documentação do README, explicando detalhadamente a rota, os parâmetros e as respostas;
- Avaliar a possibilidade de adicionar informações climáticas em versões futuras;
- Manter a API publicada e disponível para consultas externas;
- Organizar as evidências e os feedbacks recebidos;
- Finalizar a documentação e preparar a entrega do Marco 3.

## Campo 5 — Autopontuação

Marque `n.a.` na dimensão que ainda não tem como existir. A nota é `10 × pontos obtidos / pontos aplicáveis`.

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | 2 | API funcional, publicada, com filtro do Ceará, tratamento de erros e 3 testes automatizados aprovados. |
| D2 Alcance e adequação ao público | | 2 | Três pessoas externas foram convidadas e três retornos qualitativos foram registrados. |
| D3 Documentação e reprodutibilidade | | 2 | README, documentação da fonte de dados e instruções de execução e testes disponíveis. |
| D4 Registro do processo | | 2 | Diário de bordo, evidências dos convites e feedbacks registrados. |
| D5 Autoavaliação e reflexão | | 2 | Dificuldades identificadas e melhorias planejadas com base nos retornos dos usuários. |


## Antes de entregar

- [x] O endereço público da API está disponível.
- [x] O que o Campo 1 promete foi testado.
- [x] O README corresponde ao funcionamento atual da API.
- [ ] O diário tem entrada de todas as semanas desde o último marco.
- [x] As evidências dos convites e retornos estão registradas.
- [ ] O commit informado está atualizado e publicado.

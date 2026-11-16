# Entrega de marco — Marco 2

## Identificação

- **Equipe:** Luiz Matheus Silva Carvalho — 515145; Wanderson Soares da Silva — 538348
- **Marco e data:** Marco 2 — 13/11/2026
- **Trilha:** A - API sobre municípios do Ceará com dados do IBGE
- **Endereço público do produto:** n.a. — publicação pública prevista para o Marco 3
- **Commit ou tag desta entrega:** `59beca1`

O endereço tem de abrir em outra máquina, sem a equipe por perto. O commit congela o que está sendo
avaliado.

## Campo 1 — O que funciona hoje

1. Executar a API localmente seguindo as instruções do `README.md` e acessar a rota de consulta de municípios, recebendo uma resposta em formato JSON.

2. Fazer uma requisição para a rota de municípios informando o código `2304400` (Fortaleza) e receber como resposta:

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

3. Fazer uma requisição para a rota de municípios informando um código de **outro estado** (ex.: `3304557`, Rio de Janeiro) e receber o erro `404` ("Município fora do estado do Ceará.") — a API atende apenas municípios do Ceará.

4. Fazer uma requisição para a rota de municípios informando um código que não tenha 7 dígitos numéricos (ex.: `abc` ou `23`) e receber o erro `404` ("Código inválido. Informe um código IBGE com 7 dígitos numéricos."), sem derrubar a API.

## Campo 2 — O que mudou desde o marco anterior

- **Passou a existir:**
  - Filtro do Ceará: a API passou a aceitar somente municípios do Ceará, devolvendo `404` para códigos de outros estados;
  - Validação do código (7 dígitos numéricos), eliminando os erros 500/502 causados por entradas malformadas;
  - Terceiro teste automatizado (`test_codigo_fora_do_ce_devolve_404`), totalizando 3 testes passando;
  - `README.md` com o comando `python -m pytest` e documentação coerente com o comportamento atual;
  - `dados/README.md` com a fonte (URL), termos de uso do IBGE e periodicidade de atualização;
  - `diario-de-bordo.md` com entrada semanal do Marco 2 e registro dos dois integrantes;
  - `evidencias/evidencias.csv` no formato de 8 colunas e arquivos de evidência (requisições e saída dos testes);
  - Início do contato com os 3 usuários externos previstos no plano.
- **Foi cortado, e por quê:** o comportamento de retornar dados de municípios de qualquer estado foi removido, pois o escopo da ação é o Ceará e o produto mínimo define a API de municípios do Ceará.

## Campo 3 — Alcance

Os números saem do `evidencias.csv`. Esta tabela é o resumo dele.

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| Alcançabilidade | 3 pessoas externas à UFC testando a API até o final da ação | 0 (contato iniciado) | `evidencias/convite-externo.md` |
| Retorno qualitativo | 3 retornos de usuários externos | 0 | `evidencias/evidencias.csv` |
| Resultado do produto | Pelo menos 1 rota funcional, documentada e acessível publicamente até o Marco 3 | 1 rota funcional e testada | Repositório e histórico de commits |
| Formação acadêmica | 1 entrada por semana no diário de bordo | 2 entradas | `diario-de-bordo.md` |

## Campo 4 — Obstáculo e replanejamento

No Marco 2, os principais obstáculos foram:

- A API do IBGE responde com lista vazia (HTTP 200) para códigos inválidos, o que causava erro 500; resolvido com a validação do código (7 dígitos) antes da consulta e com o tratamento de 404 para municípios não encontrados.
- Ocorrência de timeout transitório do serviço do IBGE, tratado pela API retornando 503.
- O contato com usuários externos depende da disponibilidade das pessoas; por isso, os convites foram enviados com antecedência, e os retornos serão registrados no `evidencias.csv` conforme chegarem.

## Campo 5 — Autopontuação

Marque `n.a.` na dimensão que ainda não tem como existir. A nota é `10 × pontos obtidos / pontos aplicáveis`.

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | 2 | Rota funcional com tratamento de erros (404/502/503), filtro do Ceará e testes automatizados passando. |
| D2 Alcance e adequação ao público | | 0 | Contato iniciado, mas ainda sem retornos de usuários externos. |
| D3 Documentação e reprodutibilidade | | 2 | README, `dados/README.md` e instruções de teste atualizados e coerentes. |
| D4 Registro do processo | | 2 | Diário de bordo, `evidencias.csv` e plano com papéis e indicadores registrados. |
| D5 Autoavaliação e reflexão | | 2 | Diário registra atividades, dificuldades e planejamento para os próximos passos. |

**Nota:** `10 × 8 / 10 = 8`

## Antes de entregar

- [ ] O endereço do produto abre numa máquina que não é a nossa.
- [x] O que o Campo 1 promete foi testado hoje.
- [x] O `README.md` corresponde ao que o produto faz agora.
- [x] O diário tem entrada de todas as semanas desde o último marco.
- [x] Toda evidência do Campo 3 tem data e está em `evidencias/`.
- [x] O commit informado está publicado.
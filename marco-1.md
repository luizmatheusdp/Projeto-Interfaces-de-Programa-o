# Entrega de marco — modelo

Copie este arquivo **uma vez por marco**, como `marco-1.md`, `marco-2.md` e `marco-3.md`. O critério
de cada campo está no PDF `extensao/entrega-de-marco.pdf`.

O objeto avaliado é sempre o mesmo produto; o que muda é o quanto ele já existe:

| Marco | Data | Estado esperado do produto |
| :-- | :-- | :-- |
| Marco 1 | 02/10 | Plano final aprovado; o produto existe e faz uma coisa, mesmo que feia — **em 2026.2, entrega remota até 04/10** |
| Marco 2 | 13/11 | Funciona de ponta a ponta; alguém de fora consegue usar |
| Marco 3 | 27/11 | Documentado, publicado, com evidência; diário consolidado |

Presença obrigatória nos três. **Marco perdido não se repõe com entrega por e-mail.**

> **Exceção em 2026.2, só no Marco 1.** A entrega de 02/10 é **remota, pelo repositório da equipe
> no GitHub**: esta ficha, preenchida e autopontuada, vai **commitada como `marco-1.md`**, e o
> prazo vai até **domingo, 04/10, fim do dia**. Nada em papel. O repositório é a via normal daqui
> até dezembro — é por ele que o professor acompanha o trabalho sem depender de anexo, e é o commit
> que registra a data e o autor de cada entrega. Os Marcos 2 e 3 seguem presenciais.

---

## Identificação

- **Equipe:** Luiz Matheus Silva Carvalho — 515145; Wanderson Soares da Silva — 538348
- **Marco e data:** Marco 1 — 04/10/2026
- **Trilha:** A - API sobre municípios do Ceará com dados do IBGE:
- **Endereço público do produto:** n.a. — publicação pública prevista para o Marco 3
- **Commit ou tag desta entrega:** `c04d7b8`


O endereço tem de abrir em outra máquina, sem a equipe por perto. O commit congela o que está sendo
avaliado.

## Campo 1 — O que funciona hoje

1. Executar a API localmente seguindo as instruções do `README.md` e acessar a rota de consulta de municípios, recebendo uma resposta em formato JSON.

2. Fazer uma requisição para a rota de municípios informando o código `2304400` e receber como resposta:

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

3. Fazer uma requisição para a rota de municípios informando um código inválido (`9999999` ou `abc`) e receber como resposta o erro `404` ("Município não encontrado."), sem derrubar a API.

## Campo 2 — O que mudou desde o marco anterior

Está é o primeiro marco

## Campo 3 — Alcance

Os números saem do `evidencias.csv`. Esta tabela é o resumo dele, não uma segunda contabilidade.

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| Alcançabilidade | 3 pessoas externas à UFC testando a API até o final da ação | 0 até o Marco 1 | `evidencias/evidencias.csv` |
| Retorno qualitativo | 3 retornos de usuários externos | 0 até o Marco 1 | `evidencias/evidencias.csv` |
| Resultado do produto | Pelo menos 1 rota funcional, documentada e acessível publicamente até o Marco 3 | 1 rota funcional e testada | Repositório e histórico de commits |
| Formação acadêmica | 1 entrada por semana no diário de bordo | 1 entrada (11/10) | `diario-de-bordo.md` |

**O que o público externo disse:** Até o momento, nenhum usuário externo forneceu retorno. A equipe pretende realizar testes com pessoas externas antes do Marco 2.

## Campo 4 — Obstáculo e replanejamento

O principal obstáculo no primeiro marco foi o tempo para estruturar o projeto e implementar a primeira versão da API. Durante os testes, identificamos dois problemas adicionais:

- Códigos inválidos faziam a API retornar erro 500, pois o IBGE responde com uma lista vazia (HTTP 200) em vez de um objeto; o tratamento foi corrigido para devolver 404.
- Ocorrência de timeout transitório do serviço do IBGE, que a API trata retornando 503.

Para o próximo marco, a equipe pretende validar a API com usuários externos, avaliar a inclusão de novos dados (população e indicadores) e considerar melhorias de desempenho, como cache.

## Campo 5 — Autopontuação

Marque `n.a.` na dimensão que ainda não tem como existir — no Marco 1, tipicamente D2 e D5.
A nota é `10 × pontos obtidos / pontos aplicáveis`.

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | 2 | Rota funcional com tratamento de erros (404/502/503), resposta corrigida e testes automatizados passando. |
| D2 Alcance e adequação ao público | X | | O alcance externo ainda não foi realizado neste marco. |
| D3 Documentação e reprodutibilidade | | 2 | README completo com instalação, execução, exemplo de chamada, fonte e licença; plano de ação revisado. |
| D4 Registro do processo | | 2 | Diário de bordo, `evidencias.csv` e plano com papéis e indicadores registrados. |
| D5 Autoavaliação e reflexão | X | | A autoavaliação será desenvolvida nos próximos marcos. |

**Nota:** `10 × 6 / 6 = 10`

Não vale nota por si. Vale porque a diferença entre a autopontuação e a do professor é o assunto mais produtivo da devolutiva.

## Antes de entregar

- [ ] O endereço do produto abre numa máquina que não é a nossa.
- [x] O que o Campo 1 promete foi testado hoje.
- [x] O `README.md` corresponde ao que o produto faz agora.
- [ ] O diário tem entrada de todas as semanas desde o último marco.
- [x] Toda evidência do Campo 3 tem data e está em `evidencias/`.
- [x] O commit informado está publicado.

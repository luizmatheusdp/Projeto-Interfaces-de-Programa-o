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
- **Commit ou tag desta entrega:** a definir após o commit final do Marco 1


O endereço tem de abrir em outra máquina, sem a equipe por perto. O commit congela o que está sendo
avaliado.

## Campo 1 — O que funciona hoje

1. Executar a API localmente seguindo as instruções do `README.md` e acessar a rota de consulta de municípios, recebendo uma resposta em formato JSON.

2. Fazer uma requisição para a rota de municípios informando o código `2304400` e receber como resposta:

json
{"codigo":2304400,"nome":"Fortaleza","microrregiao":"CE"}

## Campo 2 — O que mudou desde o marco anterior

Está é o primeiro marco

## Campo 3 — Alcance

Os números saem do `evidencias.csv`. Esta tabela é o resumo dele, não uma segunda contabilidade.

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| Alcançabilidade | 3 pessoas externas à UFC testando a API até o final da ação | 0 até o Marco 1 | http://127.0.0.1:8000/municipios/2304400 |
| Retorno qualitativo | 3 retornos de usuários externos | 0 até o Marco 1 | http://127.0.0.1:8000/municipios/2304400 |
| Resultado do produto | Pelo menos 1 rota funcional, documentada e acessível publicamente até o Marco 3 | 1 rota inicial funcional | Repositório e histórico de commits |
| Formação acadêmica | Registrar as atividades, dificuldades e conhecimentos adquiridos durante a execução | Em andamento | `diario-de-bordo.md` |

**O que o público externo disse:** Até o momento, nenhum usuário externo forneceu retorno. A equipe pretende realizar testes com pessoas externas antes do Marco 2.

## Campo 4 — Obstáculo e replanejamento

O principal obstáculo no primeiro marco foi o tempo para estruturar o projeto e implementar a primeira versão da API.

Para o próximo marco, a equipe pretende integrar efetivamente os dados do IBGE, melhorar a resposta da API, ampliar os testes e iniciar a validação com usuários externos.

## Campo 5 — Autopontuação

Marque `n.a.` na dimensão que ainda não tem como existir — no Marco 1, tipicamente D2 e D5.
A nota é `10 × pontos obtidos / pontos aplicáveis`.

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | 1 | Existe uma rota funcional, mas o produto ainda está em estágio inicial. |
| D2 Alcance e adequação ao público | X | | O alcance externo ainda não foi realizado neste marco. |
| D3 Documentação e reprodutibilidade | | 1 | O repositório possui README e instruções iniciais para execução. |
| D4 Registro do processo | | 1 | O desenvolvimento está sendo registrado no repositório e nos arquivos da equipe. |
| D5 Autoavaliação e reflexão | X | | A autoavaliação será desenvolvida nos próximos marcos. |

Não vale nota por si. Vale porque a diferença entre a autopontuação e a do professor é o assunto mais produtivo da devolutiva.

## Antes de entregar

- [ ] O endereço do produto abre numa máquina que não é a nossa.
- [x] O que o Campo 1 promete foi testado hoje.
- [x] O `README.md` corresponde ao que o produto faz agora.
- [ ] O diário tem entrada de todas as semanas desde o último marco.
- [ ] Toda evidência do Campo 3 tem data e está em `evidencias/`.
- [ ] O commit informado está publicado.

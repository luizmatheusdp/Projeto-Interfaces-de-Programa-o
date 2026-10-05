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
{
  "codigo": "2304400",
  "mensagem": "Consulta de município"
}

## Campo 2 — O que mudou desde o marco anterior

No Marco 1, escreva `n.a.`. Nos demais, o que passou a existir **e o que foi cortado** — corte
também é resultado.

- **Passou a existir:**
- **Foi cortado, e por quê:**

## Campo 3 — Alcance

Os números saem do `evidencias.csv`. Esta tabela é o resumo dele, não uma segunda contabilidade.

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| | | | |
| | | | |

**O que o público externo disse.** Uma frase, de alguém que não é da turma nem da equipe. Se ninguém
disse nada ainda, escreva isso — e diga qual é o plano para mudar até o próximo marco.

## Campo 4 — Obstáculo e replanejamento

O que travou desde o último marco, quanto tempo custou e o que fizemos a respeito. Obstáculo
declarado a tempo é insumo para a orientação; revelado em 27/11, é só desculpa.

## Campo 5 — Autopontuação

Marque `n.a.` na dimensão que ainda não tem como existir — no Marco 1, tipicamente D2 e D5.
A nota é `10 × pontos obtidos / pontos aplicáveis`.

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | | |
| D2 Alcance e adequação ao público | | | |
| D3 Documentação e reprodutibilidade | | | |
| D4 Registro do processo | | | |
| D5 Autoavaliação e reflexão | | | |

Não vale nota por si. Vale porque a diferença entre a autopontuação e a do professor é o assunto
mais produtivo da devolutiva.

## Antes de entregar

- [ ] O endereço do produto abre numa máquina que não é a nossa.
- [ ] O que o Campo 1 promete foi testado hoje, não na semana passada.
- [ ] O `README.md` corresponde ao que o produto faz agora.
- [ ] O diário tem entrada de todas as semanas desde o último marco.
- [ ] Toda evidência do Campo 3 tem data e está em `evidencias/`.
- [ ] O commit informado está publicado.

---

## Exemplo de Campo 1 preenchido

> 1. Abrir `https://censo-escolas.exemplo.br/escolas?bairro=Benfica` e receber as 12 escolas do
>    bairro em JSON, com matrículas e infraestrutura.
> 2. Rodar `curl https://censo-escolas.exemplo.br/escolas/23041589` e receber a ficha de uma escola
>    pelo código do INEP.
> 3. Abrir `https://censo-escolas.exemplo.br/docs` e ver as três rotas documentadas, com um exemplo
>    que roda em cada uma.

Compare com o que **não** serve: "a API está funcionando e consulta o banco de dados do censo".
Isso não diz o que a pessoa digita nem o que ela recebe.

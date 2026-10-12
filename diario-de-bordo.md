# Diário de Bordo

Registro semanal das atividades da equipe. Cada entrada contém a data, os participantes, o que foi feito e as dificuldades encontradas.

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
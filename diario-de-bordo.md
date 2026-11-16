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

**Próximos passos:**

- Consolidar os retornos dos usuários externos e registrar as evidências de alcance.
- Avaliar inclusão de novos dados (população, indicadores) e melhorias de desempenho.

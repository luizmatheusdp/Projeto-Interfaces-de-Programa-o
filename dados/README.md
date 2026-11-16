# Fonte de dados

## Instituto Brasileiro de Geografia e Estatística (IBGE)

A API utiliza dados públicos da **API de Localidades do IBGE** para consultar municípios do Ceará.

- **Fonte:** Instituto Brasileiro de Geografia e Estatística (IBGE)
- **Órgão responsável:** IBGE
- **Endereço de acesso (URL):**
  - API: https://servicodados.ibge.gov.br/api/docs/localidades
  - Serviço usado: `https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}`
- **Termos de uso (conferidos):** os dados podem ser utilizados e reproduzidos livremente, desde que citada a fonte (IBGE), conforme licença **CC BY 2.5 BR**. Termos de uso: https://www.ibge.gov.br/acesso-informacao/acoes-e-programas/termos-de-uso.html
- **Periodicidade de atualização:** a divisão territorial e os identificadores oficiais dos municípios são **revisados periodicamente** pelo IBGE. As regiões geográficas imediatas e intermediárias, por exemplo, são revisadas periodicamente para refletir as mudanças da realidade brasileira; mudanças na divisão municipal ocorrem conforme revisões oficiais do IBGE (ex.: após atualizações censitárias).
- **Existência de dados pessoais:** não há dados pessoais identificáveis. São utilizados apenas dados agregados de localização (nome e códigos dos municípios e suas divisões regionais).
- **Forma de uso no produto:** a API recebe o código IBGE do município (7 dígitos), consulta a fonte e devolve, em JSON, o nome e as divisões regionais do município, **desde que ele pertença ao estado do Ceará**.
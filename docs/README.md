# Plano de Ação

## 1. Identificação

**Disciplina:** CC0464 — Interfaces de Programação de Aplicação  
**Instituição:** Universidade Federal do Ceará (UFC)  
**Semestre:** 2026.2  

### Equipe

- **LUIZ MATHEUS SILVA CARVALHO - 515145**
- **WANDERSON SOARES DA SILVA - 538348**

---

## 2. Trilha

**Trilha:** A — API pública de dados abertos

**Área temática:** Tecnologia e Produção

A ação pretende facilitar o acesso e o uso de dados públicos sobre municípios do Ceará, disponibilizando uma API simples e documentada para consulta dessas informações por pessoas externas à universidade.

---

## 3. Problema

**Problema identificado:** dificuldade para consultar e reutilizar informações públicas sobre municípios do Ceará.

Pessoas que precisam consultar informações sobre municípios cearenses precisam localizar os dados diretamente nas fontes do IBGE e compreender a estrutura dos dados e dos serviços disponíveis.

Para pessoas que não trabalham diretamente com programação ou com bases de dados, esse processo pode dificultar o acesso e o reúso das informações.

A equipe pretende reduzir essa dificuldade disponibilizando uma interface simples para consulta dos dados municipais.

---

## 4. Público externo

**Público:** Professores e estudantes da educação básica que utilizem informações sobre municípios do Ceará.

Como público secundário, o produto poderá ser utilizado por:

- Jornalistas e produtores de conteúdo;
- Organizações e coletivos que utilizem dados públicos;
- Pessoas que necessitem consultar informações básicas sobre municípios cearenses.

Durante a execução da ação, a equipe buscará realizar testes com pelo menos **3 pessoas externas à UFC**, registrando os resultados e as dificuldades encontradas durante a utilização do produto.

---

## 5. Produto

**Produto:** API pública para consulta de dados dos municípios do Ceará.

A API utilizará dados públicos do **Instituto Brasileiro de Geografia e Estatística (IBGE)** e permitirá consultar informações de um município a partir de seu código IBGE.

### Produto mínimo

A primeira versão deverá possuir pelo menos uma rota funcional:

Exemplo:

`GET /municipios/2304400`

A resposta deverá ser disponibilizada em formato JSON contendo o código do município e informações municipais disponíveis na fonte utilizada.

A equipe pretende posteriormente incluir informações como população e outros indicadores municipais selecionados.



## 6. Fontes de dados

A principal fonte de dados será o Instituto Brasileiro de Geografia e Estatística (IBGE), utilizando seus serviços e bases públicas relacionados aos municípios brasileiros.

Para a fonte utilizada serão registrados:

- Nome da fonte: Instituto Brasileiro de Geografia e Estatística (IBGE);
- Órgão responsável: IBGE;
- Endereço de acesso: documentação e serviço de dados do IBGE;
- Licença ou termos de uso;
- Data e periodicidade de atualização, quando disponíveis;
- Existência de dados pessoais;
- Forma como os dados serão utilizados no produto.

A equipe priorizará dados agregados sobre municípios e não utilizará dados pessoais identificáveis.


---

## 7. Papéis da equipe

### Luiz Matheus

- Participação na definição do problema e do público;
- Desenvolvimento do produto;
- Coleta e tratamento dos dados;
- Documentação;
- Registro das evidências da execução.

### Wanderson Soares

- Participação na definição do problema e do público;
- Desenvolvimento do produto;
- Coleta e tratamento dos dados;
- Testes;
- Documentação;
- Registro das evidências da execução.

Os papéis poderão ser ajustados conforme as necessidades do projeto, sendo registrados no histórico da equipe.

---

## 8. Cronograma

| Marco | Data | Entrega prevista |
|---|---|---|
| **Marco 1** | 02/10/2026 | Plano de ação definido e primeira versão funcional do produto |
| **Marco 2** | 13/11/2026 | Produto funcionando de ponta a ponta e utilizável por alguém externo |
| **Marco 3** | 27/11/2026 | Produto documentado, publicado e evidências de uso coletadas |

### Planejamento

**Até 02/10/2026**
- Definir o problema;
- Definir o público externo;
- Escolher a trilha;
- Identificar a primeira fonte de dados;
- Definir o produto mínimo;
- Implementar a primeira versão do produto.

**Até 13/11/2026**
- Finalizar a funcionalidade principal;
- Realizar testes;
- Permitir que alguém externo consiga utilizar o produto;
- Atualizar a documentação;
- Registrar os primeiros resultados de uso.

**Até 27/11/2026**
- Publicar a versão final;
- Finalizar a documentação;
- Coletar as evidências;
- Registrar os resultados obtidos;
- Registrar as dificuldades encontradas durante o desenvolvimento.

---

## 9. Indicadores

Os indicadores serão definidos antes da execução final da ação.

### Indicador de alcançabilidade

Será registrada a quantidade de pessoas externas que utilizaram ou tiveram contato com o produto.

**Instrumento de coleta:** registros de acesso, testes realizados e/ou retorno dos usuários.

### Indicador qualitativo

Será coletado o retorno de pessoas que utilizarem o produto, buscando identificar se a solução ajudou na dificuldade inicialmente identificada.

**Instrumento de coleta:** formulário, mensagem ou entrevista curta.

### Indicador de resultado

Será verificado se o produto foi desenvolvido, publicado e disponibilizado para utilização externa.

**Instrumento de coleta:** endereço público do produto, repositório e histórico de desenvolvimento.

### Indicador de formação

A equipe registrará no diário do projeto os conhecimentos adquiridos, dificuldades encontradas e soluções desenvolvidas durante a execução.

**Instrumento de coleta:** diário de desenvolvimento e histórico do repositório.

---

## 10. Evidências

Serão utilizadas como evidências da ação:

- histórico de commits do repositório;
- diário de bordo;
- documentação da API;
- registros dos testes realizados;
- registros de contato com usuários externos;
- retornos recebidos dos usuários;
- arquivo `evidencias.csv`;
- endereço público da API, quando publicado no Marco 3.

---

## 11. Status

Em desenvolvimento — Marco 1.

O tema, a trilha, o público externo e o produto mínimo foram definidos. A equipe está desenvolvendo a primeira versão da API, os testes e as evidências da ação.

O próximo passo é integrar os dados do IBGE à API e realizar testes com usuários externos antes do Marco 2.


O plano será atualizado após a definição do problema, público externo, trilha, fontes de dados e produto mínimo.

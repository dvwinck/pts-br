# 05 — Governança do PTS-BR

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · **05 Governança** · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

Versão da especificação: 1.0.0 (2026-11-18)

Este documento define como uma empresa começa a usar, verifica e mantém o PTS-BR.
O documento descreve os papéis, as fases de adoção e a revisão de conformidade. O
documento também descreve as métricas, o linter, a manutenção do dicionário, as
versões, o treinamento e os riscos.

As regras de escrita estão em [`02-regras.md`](02-regras.md). Este documento indica as regras pelo
ID (por exemplo, [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)) ou pelo número da seção (Seção 1 a Seção 10). Se 2 arquivos
tiverem decisões diferentes, use esta ordem:
1. Para o vocabulário (palavras e significados aprovados), use o [`03-dicionario.md`](03-dicionario.md).
2. Para a gramática e a estrutura do texto, use o [`02-regras.md`](02-regras.md).
3. Se um item deste documento for diferente de uma regra, use a regra. O
   mantenedor corrige a diferença na próxima versão PATCH.

Este documento descreve apenas as ferramentas que existem na pasta `tools/` desta
versão. A seção 6 lista cada ferramenta e os limites de cada ferramenta. O linter em
Python ([`tools/check_spec.py`](https://github.com/dvwinck/pts-br/blob/main/tools/check_spec.py)) é a ferramenta de referência da versão 1.0.0 (ver 6.1).

## Sumário

1. [Termos usados neste documento](#1-termos-usados-neste-documento)
2. [Papéis e responsabilidades](#2-papéis-e-responsabilidades)
3. [Adoção do PTS-BR em fases](#3-adoção-do-pts-br-em-fases)
4. [Verificação de conformidade](#4-verificação-de-conformidade)
5. [Métricas](#5-métricas)
6. [Ferramentas de verificação](#6-ferramentas-de-verificação)
7. [Manutenção do dicionário e das regras](#7-manutenção-do-dicionário-e-das-regras)
8. [Versões da especificação](#8-versões-da-especificação)
9. [Treinamento](#9-treinamento)
10. [Riscos da adoção e ações](#10-riscos-da-adoção-e-ações)
11. [Anexo A — Protocolo do teste de compreensão](#11-anexo-a--protocolo-do-teste-de-compreensão)
12. [Anexo B — Questionário dos redatores](#12-anexo-b--questionário-dos-redatores)
13. [Anexo C — Tabela de revisão para documentos fora do Git](#13-anexo-c--tabela-de-revisão-para-documentos-fora-do-git)

---

## 1. Termos usados neste documento

Esta tabela é o glossário do projeto da especificação ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 7](04-termos-tecnicos.md#7-glossário-do-projeto)).
Cada termo tem um gênero, uma categoria e um significado. Os termos do glossário-base
têm a definição do [`04-termos-tecnicos.md`](04-termos-tecnicos.md), por exemplo: auditoria, conformidade,
desvio, ação corretiva, indicador, meta, registro e dia útil.

| Termo | Gênero | Categoria | Significado |
|---|---|---|---|
| documento PTS-BR | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Documento que declara a versão do PTS-BR no cabeçalho (ver 8.4). |
| severidade do desvio | a | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | Nível de impacto de um desvio de redação: S1, S2 ou S3 (ver 4.3). A severidade de um incidente (SEV1 a SEV4, [`04-termos-tecnicos.md`](04-termos-tecnicos.md)) é outra escala. |
| exceção aprovada | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Desvio S2 que o revisor aceita com uma justificativa registrada e que o aprovador aprova. |
| registro de revisão | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Os comentários de revisão no pull request (ver 4.1) ou a tabela de revisão do Anexo C (ver 4.5). |
| adoção | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | O início do trabalho de uma empresa com o PTS-BR, nas 3 fases da seção 3 ([`03-dicionario.md`](03-dicionario.md), ADOÇÃO). |
| submissão | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | O primeiro envio do documento para a revisão ([`03-dicionario.md`](03-dicionario.md), SUBMISSÃO). M1, M2 e M3 "na submissão" usam a versão do documento deste envio (ver 5.2). |
| publicação | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | A versão do documento que o aprovador aprova. Também: a versão da especificação que o mantenedor publica. |
| linha de base | a | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | Os valores das métricas medidos antes do Piloto, em documentos publicados antes do PTS-BR (ver 5.8). |
| fase de adoção | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Uma etapa da adoção do PTS-BR com critérios de entrada e de saída: Piloto, Expansão e Padrão (ver 3). |
| Piloto, Expansão, Padrão | o, a, o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Os nomes das 3 fases de adoção. Escreva o nome com a letra maiúscula. |
| instrumento de medição | o | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | O documento, o registro ou o comando que mostra o valor de um critério. |
| amostra | a | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | Os documentos publicados que o auditor escolhe para a auditoria (ver 3.4). |
| falso positivo | o | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | Um alerta do linter que o revisor descarta, porque o texto segue a regra (métrica M6). |
| trilha | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | O conjunto de módulos de treinamento de um papel (ver 9). |
| treinamento | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Os módulos, os documentos de treinamento e o teste de uma trilha. |
| gabarito | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | A lista dos desvios corretos de um documento de treinamento, com a severidade de cada desvio. |
| calibração | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Uma sessão de revisão: 2 ou mais revisores revisam o mesmo documento e comparam os resultados (ver 9.3). |
| teste de compreensão | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | O teste com leitores do Anexo A. |
| questionário | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | As frases do Anexo B que os redatores avaliam com uma nota de 1 a 5. |
| revisor fundador | o | [NT-19](04-termos-tecnicos.md#nt-19-papéis-de-pessoas-em-processos) | Revisor que faz a trilha do revisor antes do Piloto, com a exceção da seção 9.4. |
| substituto do mantenedor | o | [NT-19](04-termos-tecnicos.md#nt-19-papéis-de-pessoas-em-processos) | A pessoa que faz as atividades do mantenedor quando o mantenedor não está disponível. |
| eficácia | a | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | O resultado de uma ação corretiva: a causa do desvio não existe mais (ISO 9001, seção 10.2). |
| mediana | a | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | O valor do meio de uma lista de valores em ordem. |
| índice de legibilidade | o | [NT-21](04-termos-tecnicos.md#nt-21-métricas-indicadores-e-níveis-de-serviço) | Um número que uma fórmula calcula com o tamanho das frases e das palavras de um texto (métrica M4). |
| período de transição | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | O tempo em que o revisor aceita a versão anterior e a versão nova da especificação (ver 8.3). |
| triagem | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | A primeira análise de um pedido: o mantenedor confirma o tipo e o destino do pedido. |
| documento legado | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Documento escrito antes da fase Padrão, sem a versão do PTS-BR declarada. |
| motor do linter | o | [NT-02](04-termos-tecnicos.md#nt-02-componentes-do-sistema-do-projeto) | O programa que aplica as regras do linter: o linter em Python (`check_spec.py`) ou o Vale. |
| lista branca | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | As formas de palavra que um texto PTS-BR usa: as palavras aprovadas do 03, os termos do 04 e as preposições com artigo (ver 6.8). |
| POP | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Procedimento operacional padrão: procedimento de um processo da empresa, com mais de um responsável. |
| PMD, pedido de mudança no dicionário | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Pedido de uma palavra nova, de uma alteração ou da exclusão de uma palavra do dicionário. |
| PMR, pedido de mudança de regra | o | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Pedido de alteração de uma regra das Seções 1 a 10 de [`02-regras.md`](02-regras.md). |
| dono do glossário | o | [NT-19](04-termos-tecnicos.md#nt-19-papéis-de-pessoas-em-processos) | O papel que mantém o glossário do projeto (ver 2.1). |
| RACI | a | [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo) | Matriz de responsabilidades: R faz a atividade, A responde pelo resultado, C é consultado, I é informado. |

---

## 2. Papéis e responsabilidades

### 2.1 Papéis

**Mantenedor da especificação**
- Mantém os arquivos 01 a 06, os arquivos de origem do dicionário e as regras do linter (ver 6.2).
- Decide os PMD e os PMR.
- Publica as versões MINOR e PATCH. Prepara as versões MAJOR.
- Decide o significado de uma regra quando o redator e o revisor têm decisões diferentes.
- Mede e publica as métricas.
- Faz o teste de compreensão e o questionário.
- Exemplos de cargo: redator técnico, gestor de documentação.
- Quantidade: 1 mantenedor e 1 substituto do mantenedor. Com o substituto do mantenedor, o
  processo não para quando o mantenedor não está disponível.

**Redator**
- Escreve e atualiza documentos em PTS-BR.
- Executa o linter antes de pedir a revisão.
- Corrige os desvios da revisão (ver 4.1).
- Cria um PMD quando nenhuma palavra aprovada tem o significado correto.
- Exemplos de cargo: desenvolvedor, SRE, analista de plantão, gestor de processos,
  redator técnico.

**Revisor PTS-BR**
- Aplica a lista de verificação (ver 4.2) e classifica cada desvio.
- Pede ao aprovador as exceções S2, dentro do limite da fase.
- Registra o tempo de revisão e os falsos positivos do linter de cada regra (métrica M6).
- Exemplos de cargo: redator com a trilha do revisor (ver 9.3), revisor fundador (ver 9.4).
- Quantidade: no mínimo 1 revisor por equipe na fase Expansão.

**Dono do glossário do projeto**
- Mantém os termos do projeto: nomes de módulos, telas, tipos de dados, papéis de
  acesso e siglas internas ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 7](04-termos-tecnicos.md#7-glossário-do-projeto)).
- Confirma que o glossário usa os mesmos rótulos da interface.
- Envia ao mantenedor os termos de mais de um projeto.
- Exemplos de cargo: gerente de produto, gestor técnico do produto.

**Aprovador**
- Aprova a publicação de documentos.
- Decide as exceções S2 que o revisor pede (ver 4.1).
- Decide a entrada na próxima fase.
- Aprova as versões MAJOR.
- Escolhe o auditor.
- Exemplos de cargo: gestor de desenvolvimento, gestor de documentação, gestor do processo
  na área da qualidade.
- Quantidade: no mínimo 2 aprovadores. Com 2 aprovadores, o fluxo de revisão não para
  quando um aprovador não está disponível.

**Auditor**
- Aplica a lista de verificação a uma amostra de documentos publicados (ver 3.4).
- Audita as decisões do mantenedor 1 vez por ano (ver 3.5).
- É um revisor de outra equipe. O auditor não audita um documento que o auditor escreveu ou revisou.
- No Piloto, o auditor é um revisor fundador de outra equipe (ver 9.4).

Uma pessoa pode ter mais de um papel. Siga sempre estas 4 regras:
1. O redator e o revisor de um documento são pessoas diferentes.
2. O mantenedor não decide um PMD ou um PMR do mantenedor. O substituto do mantenedor
   decide este pedido.
3. O mantenedor não audita as métricas, as decisões e os treinamentos do mantenedor.
   O auditor faz esta auditoria (ver 3.5).
4. O aprovador de um documento não é o redator do documento. O aprovador não decide as
   exceções S2 e a publicação de um texto que o aprovador escreveu.

A revisão PTS-BR verifica a redação. A revisão PTS-BR não substitui a revisão
técnica do conteúdo. O revisor técnico da equipe revisa o conteúdo técnico.

### 2.2 Matriz RACI

R = faz a atividade. A = responde pelo resultado (1 por linha). C = é consultado.
I = é informado. Sem letra = sem papel.

| Atividade | Mantenedor | Redator | Revisor | Dono do glossário | Aprovador | Auditor |
|---|---|---|---|---|---|---|
| Escrever ou atualizar um documento | | R/A | C | C | I | |
| Executar o linter antes da revisão | | R/A | | | | |
| Revisar a conformidade (lista de verificação) | C | I | R/A | C | | |
| Revisar o conteúdo técnico | | C | | C | A | |
| Aprovar a publicação de um documento | | I | C | | R/A | |
| Pedir uma exceção S2 | I | I | R/A | | C | |
| Decidir uma exceção S2 | I | I | C | | R/A | |
| Corrigir os desvios da revisão | | R/A | C | | | |
| Decidir um conflito de revisão | R/A | C | C | | I | |
| Decidir um PMD (vocabulário geral) | R/A | I | C | C | I | |
| Manter o glossário do projeto | C | I | C | R/A | | |
| Decidir um PMR (regras) | R/A | I | C | C | I | |
| Publicar uma versão PATCH ou MINOR | R/A | I | I | I | I | |
| Publicar uma versão MAJOR | R | I | C | C | A | |
| Manter as regras do linter | R/A | I | C | | | |
| Medir e publicar as métricas | R/A | | C | | I | |
| Fazer o teste de compreensão e o questionário | R | | C | | A | |
| Auditar a amostra (a cada mês ou a cada 3 meses) | I | I | | | A | R |
| Analisar a causa e criar uma ação corretiva | R/A | C | C | | I | I |
| Verificar a eficácia de uma ação corretiva | I | | | | A | R |
| Auditar as decisões do mantenedor (1 vez por ano) | C | | | | A | R |
| Fazer os módulos de treinamento com os redatores e os revisores | R/A | I | C | | I | |
| Decidir a entrada na próxima fase | R | I | C | C | A | |

Na linha "Revisar o conteúdo técnico", o revisor técnico da equipe revisa o conteúdo (R).
O revisor técnico não é um papel PTS-BR.

---

## 3. Adoção do PTS-BR em fases

A adoção do PTS-BR tem 3 fases: Piloto, Expansão e Padrão. Cada fase tem critérios de
entrada e de saída. Cada critério tem um instrumento de medição. O
aprovador decide a entrada na próxima fase com as métricas da seção 5.

### 3.1 Ordem dos tipos de documento

Comece pelos documentos com mais risco e menos texto. O risco é alto se um erro
de leitura causar dano, perda de dados ou incidente.

| Ordem | Tipo de documento | Fase | Justificativa |
|---|---|---|---|
| 1 | Avisos de segurança (PERIGO, ATENÇÃO, CUIDADO) | Piloto | Risco mais alto. Texto curto. Seção 7. |
| 2 | Runbooks de incidente | Piloto | O leitor usa o runbook durante um incidente. Uma frase com 2 significados aumenta o tempo de recuperação. |
| 3 | Procedimentos de operação (publicação de versão, rollback, migração de dados) | Expansão | Os passos têm ações que o leitor não desfaz. Seção 5. |
| 3 | Procedimentos de processos da empresa (POP, instrução de trabalho) | Expansão | Vários responsáveis, decisões e prazos. Seção 5, regras [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) a [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor). |
| 4 | Mensagens de interface (erros, mensagens de sucesso, rótulos) | Expansão | O número de leitores é alto. As mensagens estão no código. O fluxo de desenvolvimento e o dono do glossário verificam as mensagens. Seção 10. |
| 5 | Documentação de API, notas de versão, texto descritivo | Padrão | Risco menor por frase. Mais texto. Seções 6 e 9. |

O [`01-introducao.md`](01-introducao.md) define o escopo e os textos fora do escopo.

### 3.2 Fase 1 — Piloto

Duração: 8 a 12 semanas. 1 equipe.

**Critérios de entrada**

| Critério | Instrumento de medição |
|---|---|
| A versão 1.0.0 da especificação está publicada. | Entrada `[1.0.0]` do [`CHANGELOG.md`](CHANGELOG.md), com o resultado de cada critério da seção 8.5. |
| A tag `v1.0.0` existe no repositório da especificação. O [`CHANGELOG.md`](CHANGELOG.md) tem os números do commit da tag. | Tag `v1.0.0`. O mantenedor cria a tag na publicação (ver 8.5, critério 9). |
| Os testes das regras da versão 1.0.0 têm o resultado correto com o Vale 3.27.0. | Arquivo `tools/vale/testes/resultado-vale-3.27.0.txt` com a data, a versão do Vale e o número de testes (ver 6.6). |
| O mantenedor e o substituto do mantenedor estão escolhidos. | Decisão registrada pelo aprovador. |
| O mantenedor e no mínimo 2 revisores fundadores fizeram a trilha do revisor. | Registro do treinamento (ver 9.4). |
| O auditor do Piloto está escolhido: 1 revisor fundador de outra equipe. | Decisão registrada pelo aprovador (ver 9.4). |
| O teste de 20 itens, o gabarito do RV3 e o resumo de 1 página estão publicados. | Pasta `treinamento/` do repositório da especificação (ver 9.1 e 9.4). |
| O linter está no CI da equipe com `FASE: 'piloto'`: o linter mostra os alertas e não bloqueia o merge. | Pipeline [`tools/ci/docs-lint-equipe.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint-equipe.yml) (ver 6.7). |
| A linha de base está medida em no mínimo 20 documentos publicados antes do PTS-BR. | Seção 5.8. |
| O aprovador definiu a equipe do Piloto e os documentos do Piloto. | Decisão registrada pelo aprovador. |

**Atividades**
1. Escreva de novo em PTS-BR os avisos de segurança e os runbooks da equipe do Piloto.
2. Revise cada documento com o fluxo da seção 4.1 ou da seção 4.5.
3. Registre os desvios, as exceções e o tempo de revisão com os formatos da seção 4.1.
   Registre também os alertas de cada regra do linter.
4. Decida os PMD dentro do prazo da seção 7.4.
5. Faça o teste de compreensão do Anexo A com 2 runbooks.

**Critérios de saída**

| Critério | Instrumento de medição |
|---|---|
| No mínimo 15 documentos revisados e publicados em PTS-BR. | Número de registros de revisão com o resultado "Aprovado" ou "Aprovado com exceções". |
| No mínimo 80% dos documentos publicados cumprem as metas de M1 e M2 na submissão da fase Piloto. | Seção 5.9, por documento: os campos `M1-sub` e `M2-sub` dos comentários de resultado (ver 4.1) e da tabela do Anexo C. |
| M5 (duração), M6 e M7 cumprem a meta da fase Piloto. | Seção 5.9, no total da fase. |
| Nenhum desvio S1 nos documentos publicados. | Registros de revisão e auditoria de 10 documentos publicados (ver 3.4). |
| O teste de compreensão tem o resultado **Melhor ou igual**. Outra opção: o resultado **Inconclusivo**, com a decisão registrada do aprovador e um teste novo na Expansão. | Anexo A. |
| Cada regra do linter tem M6 medido. Cada regra com M6 maior que 20% está corrigida ou desligada. | Seção 5.7. |
| O mantenedor publicou os problemas e as decisões do Piloto e, se necessário, uma versão MINOR ou PATCH. | [`CHANGELOG.md`](CHANGELOG.md). |
| O aprovador registrou a decisão: continuar, repetir o Piloto ou parar. | Decisão registrada pelo aprovador. |

### 3.3 Fase 2 — Expansão

Duração: 3 a 6 meses. 3 a 5 equipes.

**Critérios de entrada**

| Critério | Instrumento de medição |
|---|---|
| Os critérios de saída do Piloto estão cumpridos. | Decisão registrada pelo aprovador. |
| Cada equipe nova tem no mínimo 1 revisor com a trilha do revisor, com a regra da seção 9.5 para o primeiro revisor da equipe. | Registro do treinamento (ver 9.3 e 9.5). |
| Cada regra do linter com M6 de no máximo 5%, medido com no mínimo 50 alertas, está no nível `error`. O CI bloqueia o merge apenas para estas regras. | Versão MINOR com a entrada "Alterado (linter)" no [`CHANGELOG.md`](CHANGELOG.md) e `FASE: 'expansao'` no pipeline da equipe (ver 6.4 e 6.7). |
| Para mensagens de interface: o dono do glossário de cada projeto está escolhido. A variável `MENSAGENS` do pipeline tem os arquivos de tradução da equipe (ver 6.9). | Decisão registrada e 1 execução do passo de mensagens no CI. |
| Para POP fora do Git: o fluxo da seção 4.5 está definido para a ferramenta da equipe. | 1 revisão de teste com a tabela do Anexo C. |

**Atividades**
1. Aplique o PTS-BR a todo aviso, runbook, procedimento e POP novo ou alterado nas
   equipes da fase.
2. Aplique o PTS-BR às mensagens de interface novas ou alteradas.
3. Faça 1 sessão de calibração entre revisores a cada mês (ver 9.3).
4. Publique as métricas de cada equipe a cada mês.

**Critérios de saída**

| Critério | Instrumento de medição |
|---|---|
| No mínimo 80% dos documentos publicados cumprem as metas de M1 e M2 na submissão da fase Expansão, em 3 meses seguidos. | Seção 5.9, por documento: os campos `M1-sub` e `M2-sub` dos registros de revisão. |
| M5, M6 e M7 cumprem a meta da fase Expansão no total de cada mês, em 3 meses seguidos. | Seção 5.9. |
| Nenhum desvio S1 em documentos publicados em 2 meses seguidos. | Registros de revisão e auditoria de 10 documentos a cada mês (ver 3.4). |
| No mínimo 70% dos redatores aprovam o processo. Se o teste de compreensão do Piloto teve o resultado **Inconclusivo**, o teste novo tem o resultado **Melhor ou igual**. | Anexo B. Anexo A. |

### 3.4 Fase 3 — Padrão

Todas as equipes. O PTS-BR é obrigatório para os documentos novos e alterados do escopo.

**Critérios de entrada**
- Os critérios de saída da Expansão estão cumpridos.
- O aprovador publicou a política de documentos legados.

**Política de documentos legados**
1. Converta primeiro os avisos de segurança e os runbooks legados. Prazo: 6 meses.
2. Converta os outros documentos quando você alterar o documento.
   Converta no mínimo a seção alterada.
3. Não converta um documento que o responsável pelo documento vai excluir em menos de 6 meses.

**Auditoria da amostra**

O aprovador escolhe o auditor (ver 2.1).

| Item | Regra |
|---|---|
| Frequência | Piloto e Expansão: 1 vez por mês, 10 documentos publicados no mês. Se o mês tiver menos de 10 documentos publicados, todos os documentos publicados no mês. Padrão: 1 vez a cada 3 meses. Um documento auditado não volta à amostra sem uma alteração. |
| Amostra na fase Padrão | 5% dos documentos publicados nos 3 meses, no mínimo 10. O auditor escolhe os documentos sem critério de conteúdo, por exemplo com números escolhidos por um programa. |
| Método | O auditor aplica todos os itens da lista de verificação e decide o resultado de cada documento com a seção 4.4. |
| Critério de aceite | No mínimo 90% da amostra com o resultado "Aprovado" ou "Aprovado com exceções". |
| S1 publicado | O mantenedor analisa a causa e cria uma ação corretiva. Prazo: 10 dias úteis. |
| S2 publicado sem exceção | O mantenedor cria uma ação corretiva. Prazo: 20 dias úteis. |
| Amostra com o resultado menor que o critério | O aprovador decide uma ação: treinamento da equipe, auditoria de uma amostra nova no próximo mês, ou a equipe volta para a fase anterior. |
| Eficácia | Na próxima auditoria, o auditor verifica cada ação corretiva sem verificação de eficácia: a causa foi removida? Uma ação sem eficácia volta ao mantenedor com um prazo novo. |
| Registro | O auditor grava o resultado, a lista dos documentos, as ações corretivas e a eficácia de cada ação no repositório da especificação, em `auditorias/AAAA-MM.md`. |

Revise as metas da seção 5.9 1 vez por ano.

### 3.5 Auditoria das decisões do mantenedor

O auditor audita o mantenedor 1 vez por ano. Esta auditoria cumpre a regra 3 da
seção 2.1.

| Item | Regra |
|---|---|
| Métricas | O auditor calcula de novo M1 a M7 de 1 mês com os registros de revisão e o registro de decisões. O auditor compara estes valores com os valores publicados. |
| Decisões | O auditor escolhe 5 decisões de PMD ou de PMR do registro da seção 7.6. Para cada decisão, o auditor verifica o critério de aceite, o prazo e a publicação. |
| Treinamento | O auditor verifica os registros de treinamento de 3 pessoas. |
| Resultado | Cada diferença é um desvio de processo. O mantenedor cria uma ação corretiva com prazo de 20 dias úteis. |
| Registro | `auditorias/AAAA-mantenedor.md`, no repositório da especificação. |

---

## 4. Verificação de conformidade

### 4.1 Fluxo de revisão de um documento no Git

O fluxo tem 6 procedimentos, 1 para cada responsável e etapa (regra [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor)). Os
procedimentos usam os formatos fixos do fim desta seção.

| Procedimento | Responsável | Procedimento que recebe a saída |
|---|---|---|
| Pedir a revisão de um documento | Redator | Revisar um documento |
| Revisar um documento | Revisor | Decidir uma exceção S2, Corrigir os desvios da revisão, Aprovar a publicação de um documento |
| Decidir uma exceção S2 | Aprovador | Revisar um documento, passo 6 |
| Corrigir os desvios da revisão | Redator | Revisar um documento, passo 8 |
| Aprovar a publicação de um documento | Aprovador | Revisar um documento, passo 10 |
| Decidir um conflito de revisão | Mantenedor | Corrigir os desvios da revisão, Revisar um documento, Aprovar a publicação de um documento |

#### Pedir a revisão de um documento

- **Responsável:** redator
- **Entrada:** o documento novo ou alterado, no branch do redator
- **Gatilho e prazo:** o redator termina o texto. Prazo: nenhum. A duração da revisão (M5) começa no pedido de revisão.

1. Declare a versão do PTS-BR no cabeçalho do documento (ver 8.4).
2. Execute o linter no seu computador (ver 6.5).
3. Corrija cada alerta. Se o texto seguir a regra, escreva a justificativa do alerta na descrição do pull request.
4. Crie o pull request. Escreva o tipo de documento e o leitor-alvo na descrição.

   O CI mostra M1 e as palavras de M2 no resumo do job, no passo "Métricas M1 e M2" (ver 6.7).
5. Verifique o resultado do linter no CI:
   - Se o CI não mostrar um alerta de nível `error`, vá para o passo 6.
   - Se o CI mostrar um alerta de nível `error`, corrija o texto e volte ao passo 5. Depois de 3 vezes, peça ajuda ao mantenedor num comentário do pull request. Este procedimento termina neste passo. O mantenedor recebe o pull request no procedimento "Decidir um conflito de revisão".
6. Peça a revisão a um revisor no campo **Reviewers**. O revisor não é o redator do documento (ver 2.1).
7. Verifique que o pull request mostra o revisor no campo **Reviewers**.

   O revisor recebe o pull request no procedimento "Revisar um documento".

#### Revisar um documento

- **Responsável:** revisor
- **Entrada:** o pull request do redator
- **Gatilho e prazo:** o pedido de revisão no campo **Reviewers**. Prazo: 3 dias úteis para a primeira revisão e 2 dias úteis para cada revisão depois de uma correção.

1. Na primeira revisão, copie do resumo do job do CI os valores da linha `[METRICAS]` de cada documento.

   O resumo da primeira execução do CI no pull request mostra M1 e as palavras de M2 na submissão (ver 5.2).
2. Aplique a lista de verificação da seção 4.2 ao documento. Depois de uma correção, verifique o texto alterado e cada desvio com o estado `ABERTO`.
3. Confirme ou descarte cada alerta do linter e cada palavra de M2.

   Registro: os alertas e os falsos positivos de cada regra, na linha `[LINTER]`. M1 e M2 na submissão, nos campos `M1-sub` e `M2-sub`. As 2 linhas estão no comentário de resultado.
4. Escreva 1 comentário no pull request para cada desvio novo, com o formato de desvio. Escreva o estado `CORRIGIDO` em cada desvio corrigido.

   Registro: os comentários de desvio, no pull request.
5. Peça ao aprovador cada exceção S2 necessária. No comentário do desvio, escreva a justificativa, o estado `EXCECAO-PEDIDA` e o usuário do aprovador.

   O aprovador recebe o pedido no procedimento "Decidir uma exceção S2".
6. Aguarde a decisão de cada exceção pedida:
   - Se nenhum desvio tiver o estado `EXCECAO-PEDIDA`, vá para o passo 7.
   - Se o aprovador decidir cada exceção pedida, vá para o passo 7.
   - Se o aprovador não decidir uma exceção em 2 dias úteis, escreva o estado `ABERTO` e a causa "sem decisão no prazo" no desvio. Vá para o passo 7.
7. Decida o resultado com o critério da seção 4.4:
   - Se o resultado for "Aprovado" ou "Aprovado com exceções", vá para o passo 9.
   - Se o resultado for "Reprovado", vá para o passo 8.
8. Escreva o comentário de resultado "Reprovado" com a lista dos desvios com o estado `ABERTO`. O redator recebe o pull request no procedimento "Corrigir os desvios da revisão". Aguarde o novo pedido de revisão:
   - Se o redator pedir a revisão de novo, volte ao passo 2. Depois do 3º resultado "Reprovado", envie o pull request ao mantenedor num comentário. Este procedimento termina neste passo. O mantenedor recebe o pull request no procedimento "Decidir um conflito de revisão".
   - Se o redator não pedir a revisão de novo em 10 dias úteis, feche o pull request. Registro: o comentário de resultado "Reprovado", no pull request. O processo termina neste passo.
9. Escreva o comentário de resultado com o formato de resultado. Calcule `M1-pub` e `M2-pub` na versão aprovada com o comando `check_spec.py --metricas`.

   Registro: o comentário de resultado, no pull request. O aprovador recebe o pull request no procedimento "Aprovar a publicação de um documento".
10. Verifique a decisão do aprovador no pull request:
    - Se o pull request tiver o estado **Approved**, o processo termina neste passo.
    - Se o aprovador recusar o resultado, volte ao passo 7 (no máximo 2 vezes). Depois, envie o pull request ao mantenedor. Este procedimento termina neste passo. O mantenedor recebe o pull request no procedimento "Decidir um conflito de revisão".
    - Se o aprovador não decidir em 2 dias úteis, envie o pull request ao mantenedor. Este procedimento termina neste passo. O mantenedor recebe o pull request no procedimento "Decidir um conflito de revisão".

#### Decidir uma exceção S2

- **Responsável:** aprovador
- **Entrada:** um comentário de desvio com o estado `EXCECAO-PEDIDA`, que o revisor escreve
- **Gatilho e prazo:** o comentário de desvio com o usuário do aprovador. Prazo: 2 dias úteis.

1. Leia o desvio, a parte do texto e a justificativa do revisor.
2. Compare o pedido com a seção 4.3 e com o limite de exceções da fase (ver 4.4):
   - Se o pedido cumprir a seção 4.3 e o limite, responda ao comentário do desvio com `[EXCECAO @<seu-usuário>]`. Um desvio num aviso de segurança não tem exceção. Vá para o passo 3.
   - Se o pedido não cumprir uma destas condições, responda ao comentário do desvio com `[ABERTO]` e a causa da recusa. Vá para o passo 3.

   Registro: a resposta do aprovador, no pull request.
3. Verifique que a resposta mostra o estado novo do desvio.

   Este procedimento termina neste passo. O revisor recebe a decisão no passo 6 de "Revisar um documento".

#### Corrigir os desvios da revisão

- **Responsável:** redator
- **Entrada:** o comentário de resultado "Reprovado" do revisor, ou a decisão do mantenedor
- **Gatilho e prazo:** o comentário "Reprovado" ou a decisão do mantenedor no pull request. Prazo: 10 dias úteis.

1. Leia cada comentário de desvio com o estado `ABERTO`.
2. Decida cada desvio:
   - Se você aceitar o desvio, corrija o texto. Vá para o passo 3.
   - Se o texto seguir a regra, escreva a justificativa numa resposta ao comentário do desvio. O revisor decide o desvio na próxima revisão. Vá para o passo 3.
3. Execute o linter no seu computador (ver 6.5).
4. Envie as alterações ao branch do pull request.

   Registro: o commit, no histórico do pull request.
5. Peça a revisão de novo no campo **Reviewers**.
6. Verifique que o pull request mostra o novo pedido de revisão.

   Este procedimento termina neste passo. O revisor recebe o pull request no passo 8 de "Revisar um documento".

#### Aprovar a publicação de um documento

- **Responsável:** aprovador
- **Entrada:** o pull request com o comentário de resultado do revisor
- **Gatilho e prazo:** o comentário de resultado. Prazo: 2 dias úteis.

1. Leia o comentário de resultado e os comentários de desvio.
2. Confirme o estado de cada exceção do resultado:
   - Se cada exceção tiver o estado `EXCECAO` com o usuário de um aprovador, vá para o passo 3.
   - Se uma exceção não tiver este estado, vá para o passo 5.
3. Compare o resultado com o critério da seção 4.4:
   - Se o resultado cumprir a seção 4.4, aprove o pull request. Registro: a aprovação do pull request, no histórico do pull request. Vá para o passo 4.
   - Se o resultado não cumprir a seção 4.4, vá para o passo 5.
4. Verifique o estado do pull request. O estado é **Approved**. O processo termina neste passo.
5. Recuse o resultado: escreva a causa da recusa num comentário do pull request.

   Registro: o comentário de recusa, no pull request. Este procedimento termina neste passo. O revisor recebe o pull request no passo 10 de "Revisar um documento".

#### Decidir um conflito de revisão

- **Responsável:** mantenedor. Se o mantenedor não estiver disponível, o substituto do mantenedor segue este procedimento.
- **Entrada:** o pull request, com o pedido do redator ou do revisor
- **Gatilho e prazo:** um comentário do pull request com o usuário do mantenedor. Prazo: 5 dias úteis.

1. Leia o pull request, os comentários de desvio e o pedido.
2. Decida a causa do conflito:
   - Se uma regra tiver 2 leituras, escreva a leitura correta e crie um PMR (ver 7.7). Vá para o passo 3.
   - Se o desvio existir, escreva os desvios que o redator corrige. Vá para o passo 3.
   - Se o alerta for um falso positivo, escreva a exceção com o comentário do Vale (ver 6.4). Vá para o passo 3.
   - Se o aprovador não decidir no prazo, escolha outro aprovador (ver 2.1). Vá para o passo 3.
3. Escreva a decisão num comentário do pull request. A decisão do mantenedor é a decisão final deste pull request.

   Registro: o comentário de decisão do mantenedor, no pull request.
4. Envie o pull request ao responsável da próxima etapa:
   - Se o redator precisar corrigir o texto, este procedimento termina neste passo. O redator recebe o pull request no procedimento "Corrigir os desvios da revisão".
   - Se o revisor precisar decidir o resultado de novo, este procedimento termina neste passo. O revisor recebe o pull request no passo 7 de "Revisar um documento".
   - Se outro aprovador decidir a publicação, este procedimento termina neste passo. O aprovador recebe o pull request no procedimento "Aprovar a publicação de um documento".

**Formato do registro de um desvio**

```text
[S2][R4.2][ABERTO] Frase com 31 palavras no passo 3.
```

| Campo | Valores |
|---|---|
| Severidade do desvio | `S1`, `S2` ou `S3` (ver 4.3). |
| Regra | O ID de [`02-regras.md`](02-regras.md), por exemplo `R4.2`. Para o item CK-0.1, use `CK-0.1`. |
| Estado | `ABERTO`: o desvio existe e não tem correção. `CORRIGIDO`: o redator corrigiu o desvio. `EXCECAO-PEDIDA`: o revisor pede ao aprovador uma exceção S2, com a justificativa. `EXCECAO @aprovador`: exceção S2 aprovada, com o nome do aprovador. `REGISTRADO`: desvio S3 publicado para o treinamento. |

O estado de um desvio é o último estado do comentário do desvio ou das respostas ao comentário.

**Formato do resultado da revisão**

```text
[RESULTADO: Aprovado com exceções][S1: 0][S2-exc: 2][S3: 1][palavras: 640][min: 25][pedido: 2026-12-01][resultado: 2026-12-03]
[METRICAS][M1-sub: 88,0][M2-sub: 4,7][M1-pub: 96,0][M2-pub: 0,0]
[LINTER][PTSBR.FraseLonga: 4/1][PTSBR.PalavrasNaoAprovadas: 6/0][PTSBR.OndeRelativo: 2/2]
```

Na linha `[METRICAS]`, `M1-sub` e `M2-sub` são os valores na submissão, e `M1-pub` e
`M2-pub` são os valores na publicação (ver 5.2). M1 é a porcentagem de frases dentro do
limite. M2 é o número de palavras não aprovadas confirmadas por 1 000 palavras. Cada
palavra conta 1 vez (ver 5.4).

Na linha `[LINTER]`, cada regra tem 2 números: os alertas da regra e os falsos positivos
da regra. Exemplo: `4/1` = 4 alertas, 1 falso positivo. Escreva as regras com 1 alerta
ou mais. Os campos `pedido` e `resultado` são as datas do pedido de revisão e do
resultado (métrica M5).

O comentário de resultado é o registro permanente de M1, M2, M3, M5 e M6. O log e o resumo
do job do CI não são permanentes. Com os formatos fixos, o comando `grep` nos comentários
calcula as métricas. Nesta versão, a pasta `tools/` não tem um script para este cálculo.

### 4.2 Lista de verificação do revisor

O revisor responde a todos os itens. Cada item tem a resposta "sim" ou "não". Um
"não" é um desvio. A coluna "Regras" mostra os IDs de [`02-regras.md`](02-regras.md). Se o item e a
regra forem diferentes, use a regra.

A coluna "Severidade" mostra a severidade padrão do desvio. O revisor aumenta a severidade do desvio
com a regra da seção 4.3. A coluna "Linter" mostra o arquivo de regra Vale que
encontra parte dos desvios do item (ver 6.3). O sinal "—" indica que nenhuma
regra do linter encontra os desvios do item. Um item com regra de linter também precisa da
leitura do revisor: o linter não encontra todos os desvios.

**Seção 0 — Documento**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-0.1 | O cabeçalho declara a versão do PTS-BR (`pts-br: "1.0"`)? | Seção 8.4 deste documento | S2 | — |

**Seção 1 — Palavras**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-1.1 | Cada palavra do vocabulário geral está aprovada no [`03-dicionario.md`](03-dicionario.md)? Os outros termos estão no [`04-termos-tecnicos.md`](04-termos-tecnicos.md) ou no glossário do projeto? | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | S2 | `PalavrasNaoAprovadas`, `GlossarioProjeto` (com `--glossario`). Lista branca (`check_spec.py --lista-branca`, ver 6.8): apenas a forma da palavra |
| CK-1.2 | Cada palavra aprovada tem o significado e a classe gramatical aprovados? | [R1.2](02-regras.md#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor), [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor) | S2 | — (a lista branca não verifica o significado) |
| CK-1.3 | O documento usa sempre o mesmo termo para o mesmo conceito? | [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | S2 | — |
| CK-1.4 | Os artigos, o substantivo de classe antes de literais e a crase seguem as regras? | [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor), [R1.6](02-regras.md#r16-use-a-crase-apenas-antes-de-palavra-feminina-com-artigo-e-antes-de-horas-revisor) | S3 | — |
| CK-1.5 | Os termos em inglês estão na lista de [`04-termos-tecnicos.md`](04-termos-tecnicos.md), como substantivo e com o gênero da lista? O texto não tem verbos com radical estrangeiro? | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | S2 | `PalavrasNaoAprovadas` (verbos do 03 e da tabela 5.4 do 04) |
| CK-1.6 | O texto não usa "o mesmo" como pronome? Cada pronome tem 1 referência possível? | [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) | S2 | `OMesmo` |
| CK-1.7 | O texto usa "onde" apenas para lugar? | [R1.9](02-regras.md#r19-use-onde-apenas-para-lugar-vale) | S3 | `OndeRelativo` |
| CK-1.8 | O texto não usa a forma "para" do verbo "parar" numa frase com a leitura da preposição "para"? | [R1.10](02-regras.md#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor) | S2 | — |

**Seção 2 — Cadeias nominais**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-2.1 | Nenhuma cadeia tem mais de 3 substantivos ligados por "de"? | [R2.1](02-regras.md#r21-use-no-máximo-3-substantivos-em-uma-cadeia-com-de-revisor) | S2 | — |
| CK-2.2 | Cada adjetivo tem 1 substantivo possível? Os compostos usam a ordem do português? | [R2.2](02-regras.md#r22-escreva-o-adjetivo-imediatamente-depois-do-substantivo-revisor), [R2.3](02-regras.md#r23-não-use-a-ordem-do-inglês-em-substantivos-compostos-revisor) | S2 | — |
| CK-2.3 | Cada conceito longo tem um nome curto, definido na primeira ocorrência? | [R2.4](02-regras.md#r24-nomeie-um-conceito-longo-com-um-nome-curto-revisor) | S3 | — |

**Seção 3 — Verbos**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-3.1 | O texto usa apenas os tempos verbais aprovados? O subjuntivo aparece apenas depois de "se" ou "quando"? | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | S2 | `FuturoSimples` (apenas o futuro simples e "irá" + infinitivo) |
| CK-3.2 | A voz passiva aparece apenas em texto descritivo e apenas se o leitor não precisar saber o autor da ação? | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | S2 | — |
| CK-3.3 | O texto não tem passiva sintética com "se" ("Instala-se") nem "se" indeterminado? | [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale) | S2 | `PassivaSintetica` |
| CK-3.4 | O texto não tem verbo-suporte com substantivo ("realize a instalação") nem um verbo geral no lugar do verbo específico? | [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R3.10](02-regras.md#r310-use-o-verbo-específico-não-um-verbo-geral-revisor) | S2 | `VerboSuporte` (apenas [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale)) |
| CK-3.5 | O texto não tem gerundismo nem 2 gerúndios seguidos? | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale) | S2 | `Gerundismo` |
| CK-3.6 | O texto não tem pronome átono nem mesóclise? | [R3.7](02-regras.md#r37-não-use-pronomes-oblíquos-átonos-nem-mesóclise-vale) | S2 | `Enclise` |
| CK-3.7 | "Poder" e "dever" têm o significado aprovado? Os verbos de ligação são apenas "ser", "estar" e "ficar" (estado novo)? | [R3.8](02-regras.md#r38-use-poder-e-dever-com-um-único-significado-revisor), [R3.9](02-regras.md#r39-use-apenas-ser-estar-e-ficar-como-verbos-de-ligação-revisor) | S2 | — |

**Seção 4 — Frases**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-4.1 | Cada frase tem uma instrução ou uma afirmação? | [R4.1](02-regras.md#r41-escreva-uma-instrução-ou-uma-afirmação-por-frase-revisor) | S2 | — |
| CK-4.2 | Cada frase de procedimento tem no máximo 20 palavras? Cada frase descritiva tem no máximo 25 palavras? | [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale) | S2 | `FraseLongaProcedimento`, `FraseLonga` |
| CK-4.3 | O sujeito está antes do verbo, com concordância? O texto não usa "haver"? O sujeito está escrito se existir mais de um agente possível? | [R4.3](02-regras.md#r43-escreva-o-sujeito-antes-do-verbo-e-faça-a-concordância-vale), [R4.4](02-regras.md#r44-escreva-o-sujeito-se-o-texto-tiver-mais-de-um-autor-de-ação-revisor) | S2 | `Haver` (apenas "haver") |
| CK-4.4 | Cada frase tem no máximo 1 negação e no máximo 1 oração subordinada? | [R4.5](02-regras.md#r45-use-no-máximo-uma-negação-por-frase-revisor), [R4.6](02-regras.md#r46-use-no-máximo-uma-oração-subordinada-por-frase-revisor) | S2 | — |

**Seção 5 — Procedimentos**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-5.1 | Cada passo tem um número? Os passos estão na ordem de execução? | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) | S1 | — |
| CK-5.2 | Cada passo usa o imperativo ("Remova", "Instale")? O infinitivo aparece apenas no título? | [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor) | S2 | — |
| CK-5.3 | Cada passo tem 1 instrução, ou ações que o leitor faz ao mesmo tempo? | [R5.3](02-regras.md#r53-escreva-uma-instrução-por-passo-revisor) | S2 | — |
| CK-5.4 | A condição e o local estão antes da ação? | [R5.4](02-regras.md#r54-escreva-a-condição-e-o-local-antes-da-ação-revisor) | S1 | — |
| CK-5.5 | O resultado esperado está numa frase separada? Os comandos para digitar estão em blocos de código? | [R5.5](02-regras.md#r55-escreva-o-resultado-esperado-em-uma-frase-separada-revisor), [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | S3 | — |
| CK-5.6 | A seção "Antes de começar" está antes do passo 1? O procedimento tem no máximo 10 passos e 1 nível de lista dentro de um passo? | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R5.7](02-regras.md#r57-limite-o-número-de-passos-e-de-níveis-do-procedimento-revisor) | S2 | — |
| CK-5.7 | O último passo verifica o resultado? | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | S2 | — |
| CK-5.8 | O procedimento tem o bloco com o responsável, a entrada, o gatilho e o prazo? | [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | S2 | — |
| CK-5.9 | Cada ponto de decisão mostra todas as saídas, também "recusado" e "sem resposta no prazo"? Cada saída termina num passo, em outro procedimento, no fim do procedimento com quem continua o processo, ou no fim do processo? | [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | S1 | — |
| CK-5.10 | Cada passo que gera um registro tem a frase "Registro:" com o nome e o lugar do registro? | [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor) | S2 | — |
| CK-5.11 | Cada procedimento que altera o ambiente de produção tem um procedimento para reverter a alteração? Se não for possível reverter a alteração, o texto diz o plano? | [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) | S2 | — |

**Seção 6 — Texto descritivo**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-6.1 | A primeira frase de cada parágrafo diz o assunto do parágrafo? | [R6.1](02-regras.md#r61-comece-o-parágrafo-com-a-frase-principal-revisor) | S3 | — |
| CK-6.2 | Cada parágrafo tem no máximo 6 frases e 1 assunto? | [R6.2](02-regras.md#r62-escreva-parágrafos-com-no-máximo-6-frases-e-um-assunto-revisor) | S3 | — |
| CK-6.3 | O texto usa apenas os conectores aprovados e valores exatos? Os itens paralelos estão em listas ou tabelas? | [R6.3](02-regras.md#r63-use-conectores-simples-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R6.5](02-regras.md#r65-use-listas-e-tabelas-para-itens-paralelos-revisor) | S2 | — |
| CK-6.4 | O texto descritivo não tem instruções? As instruções estão em procedimentos? | [R6.6](02-regras.md#r66-não-escreva-instruções-em-texto-descritivo-revisor) | S2 | — |

**Seção 7 — Avisos de segurança**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-7.1 | Cada aviso usa a palavra de sinalização da consequência mais grave (PERIGO, ATENÇÃO, CUIDADO)? Nenhuma NOTA tem um risco? | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.2](02-regras.md#r72-use-nota-apenas-para-informação-sem-risco-revisor) | S1 | — |
| CK-7.2 | Cada aviso tem a instrução, o risco e a consequência exata, nesta ordem? | [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor) | S1 | — |
| CK-7.3 | Cada aviso está antes do passo perigoso? | [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | S1 | — |
| CK-7.4 | Cada aviso tem 1 risco? | [R7.5](02-regras.md#r75-escreva-um-risco-por-aviso-revisor) | S1 | — |
| CK-7.5 | A palavra de sinalização está em maiúsculas e negrito, num bloco separado? O texto não tem outro negrito, itálico ou maiúsculas? Exceção: os rótulos de interface e os valores de estado seguem a regra [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor). | [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | S2 | — |
| CK-7.6 | O aviso e o comando que altera ou exclui dados mostram o nome do ambiente? Antes do comando, um passo mostra o alvo com a mesma opção de alvo do comando (tabela "opção de alvo por ferramenta" de [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor))? | [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) | S1 | — |
| CK-7.7 | O texto e os comandos não mostram segredos (senha, token, chave)? | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) | S1 | — |

**Seção 8 — Pontuação e formatação**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-8.1 | As frases terminam com ponto final? A vírgula segue a estrutura da frase? O texto não tem ponto e vírgula, barra entre palavras nem frases dentro de outra frase entre parênteses ou travessões? | [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor), [R8.2](02-regras.md#r82-use-a-vírgula-de-acordo-com-a-estrutura-da-frase-revisor), [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor) | S3 | — |
| CK-8.2 | Os números e as unidades seguem o formato fixo: algarismos, espaço como separador de milhar, símbolo da unidade depois de um espaço? | [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale) | S3 | `SeparadorMilhar`, `Unidades` |
| CK-8.3 | As datas, as horas e as maiúsculas seguem o formato fixo? | [R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor), [R8.6](02-regras.md#r86-use-maiúsculas-apenas-no-início-das-frases-e-em-nomes-próprios-revisor) | S3 | — |
| CK-8.4 | Cada sigla fora da tabela de siglas de [`04-termos-tecnicos.md`](04-termos-tecnicos.md) tem a forma completa na primeira ocorrência? | [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) | S3 | — |
| CK-8.5 | Comandos, caminhos de arquivo, valores, rótulos e espaços reservados têm a formatação da Seção 8? | [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor), [R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor) | S3 | — |

**Seção 9 — Práticas de escrita**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-9.1 | O texto fala com o leitor na forma "você"? O texto não tem o pronome "nós", "a gente" nem "o usuário deve"? | [R9.1](02-regras.md#r91-escreva-para-o-leitor-na-forma-você-revisor) | S2 | `PalavrasNaoAprovadas` (apenas "nós" e "a gente") |
| CK-9.2 | O texto não tem linguagem figurada, gíria, palavras vazias nem palavras de cortesia? | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R9.3](02-regras.md#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor) | S2 | `PalavrasNaoAprovadas` (apenas as palavras do 03) |
| CK-9.3 | As referências são estáveis (seção, passo, tabela, versão)? | [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | S2 | — |
| CK-9.4 | As listas estão completas, sem "etc."? | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | S2 | `PalavrasNaoAprovadas` (apenas "etc.") |

**Seção 10 — Interface e mensagens de software**

| Item | Verificação | Regras | Severidade | Linter |
|---|---|---|---|---|
| CK-10.1 | Os rótulos do texto são iguais aos rótulos da interface, em negrito? O verbo é o verbo do tipo de elemento? Os caminhos de menu e as teclas têm o formato fixo? | [R10.1](02-regras.md#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor), [R10.2](02-regras.md#r102-use-o-verbo-do-tipo-de-elemento-revisor), [R10.3](02-regras.md#r103-escreva-caminhos-de-menu-e-teclas-em-um-formato-fixo-revisor) | S2 | — |
| CK-10.2 | Cada mensagem de erro diz o que aconteceu e o que o leitor faz depois? | [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) | S2 | — |
| CK-10.3 | A mensagem de erro não diz que o erro é do leitor, não tem humor e não é apenas "Erro"? | [R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor) | S3 | `Mensagens` (com `--mensagens`, ver 6.9): interjeições, ponto de exclamação e mensagens gerais |
| CK-10.4 | Os rótulos de botão, as mensagens de sucesso e de estado e os textos com variáveis seguem as regras? | [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor), [R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor), [R10.8](02-regras.md#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor) | S2 | `Mensagens` (com `--mensagens`, ver 6.9): "(s)", variável por posição, artigo antes de variável, "com sucesso" |
| CK-10.5 | Cada texto de validação de campo, de acessibilidade, de link e de estado vazio diz a ação e o formato esperado? | [R10.9](02-regras.md#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor) | S2 | — |
| CK-10.6 | Os textos de desenvolvimento (mensagem de commit, descrição de pull request, ajuda de CLI, log) seguem o formato fixo? | [R10.10](02-regras.md#r1010-escreva-textos-de-desenvolvimento-com-um-formato-fixo-revisor) | S3 | — |

A lista de verificação PTS-BR verifica a redação. O conteúdo técnico (comandos e
valores testados, leitor-alvo correto) é da revisão técnica (ver 2.1).

### 4.3 Níveis de severidade do desvio

| Nível | Nome | Definição | Exemplos |
|---|---|---|---|
| S1 | Crítico | O desvio causa uma ação incorreta, dano, perda de dados ou incidente quando o leitor segue o texto. | Aviso depois do passo perigoso. Passos fora de ordem. Instrução com 2 significados. Palavra com 2 significados num passo de exclusão. Decisão sem a saída "recusado". |
| S2 | Maior | O desvio não cumpre uma regra que o revisor verifica, e o leitor entende o texto com mais esforço. | Frase com mais palavras que o limite. Voz passiva com "se". Cadeia de 4 substantivos. Palavra não aprovada. Infinitivo como ordem. Documento sem a versão declarada. |
| S3 | Menor | O desvio é de forma, e o leitor entende o texto sem esforço a mais. | Lista não numerada para passos curtos. Comando sem formatação de código. Sigla sem forma completa. |

Um comando incorreto é um defeito da revisão técnica. Este defeito não está na escala S1 a S3.

**Regra para aumentar a severidade.** Um desvio S2 num aviso de segurança tem a severidade S1.
Um desvio S2 num passo com uma ação que o leitor não desfaz também tem a severidade S1. Exemplos:
excluir dados, revogar acesso, parar um serviço em produção.

**Exceções.**
- Um desvio S1 nunca tem exceção. O redator corrige o desvio antes da publicação.
  Um S1 com o estado `CORRIGIDO` não altera o resultado do documento (ver 4.4).
- Um desvio S2 pode ter exceção. O revisor pede a exceção com a justificativa e o estado
  `EXCECAO-PEDIDA`. O aprovador decide a exceção (ver 4.1). Exemplo de justificativa
  válida: o rótulo da interface tem 6 palavras, e o texto precisa mostrar o rótulo exato.
- Um desvio S3 não bloqueia a publicação. O revisor registra o desvio com o estado
  `REGISTRADO` para o treinamento.
- Para desligar uma regra do linter numa parte do texto, use o comentário do Vale (ver 6.4)
  e escreva a exceção no registro de revisão.

### 4.4 Critério de aprovação de um documento

O revisor escolhe 1 destes 3 resultados. Cada documento cumpre as condições de 1 resultado
apenas.

| Resultado | Condições (todas verdadeiras) |
|---|---|
| Aprovado | Nenhum S1 com o estado `ABERTO`. Nenhum S2 com o estado `ABERTO`, `EXCECAO-PEDIDA` ou `EXCECAO`. CK-0.1 = sim. |
| Aprovado com exceções | Nenhum S1 com o estado `ABERTO`. Nenhum S2 com o estado `ABERTO` ou `EXCECAO-PEDIDA`. 1 S2 ou mais com o estado `EXCECAO`. As exceções estão dentro do limite da fase (tabela abaixo). Nenhuma exceção está num aviso de segurança. CK-0.1 = sim. |
| Reprovado | 1 destas condições: 1 S1 ou mais com o estado `ABERTO`. 1 S2 ou mais com o estado `ABERTO` ou `EXCECAO-PEDIDA`. Mais exceções que o limite da fase. 1 exceção num aviso de segurança. CK-0.1 = não. |

Um documento sem a versão declarada (CK-0.1 = não) é um desvio S2 sem exceção.
Portanto, o resultado deste documento é "Reprovado" até o redator declarar a versão.

Limite de exceções S2 por 1 000 palavras:

| Fase | Limite |
|---|---|
| Piloto | 5 |
| Expansão | 3 |
| Padrão | 1,5 |

Para um documento com menos de 1 000 palavras, calcule o limite com o número de palavras
do documento. Se o valor tiver uma parte depois da vírgula, use o próximo número sem
vírgula. Exemplo: um runbook com 400 palavras na fase Expansão aceita no máximo 2
exceções S2 (400 × 3 / 1 000 = 1,2. O próximo número sem vírgula é 2).

Um alerta do linter não é um desvio. O revisor confirma ou descarta cada alerta.
Cada alerta confirmado é um desvio com a severidade da lista de verificação.

### 4.5 Documentos fora do Git

Use estes procedimentos para documentos em Confluence, Google Docs, SharePoint ou num
sistema da qualidade. Os procedimentos têm as mesmas verificações e os mesmos estados da
seção 4.1. A tabela do Anexo C substitui os comentários de resultado do pull request.

Os procedimentos "Decidir uma exceção S2", "Corrigir os desvios da revisão" e "Decidir um
conflito de revisão" da seção 4.1 também valem fora do Git. Fora do Git, use os nomes da coluna da direita:

| Na seção 4.1 | Fora do Git |
|---|---|
| O pull request | A página do documento |
| Um comentário do pull request | Um comentário da página |
| Enviar as alterações ao branch (commit) | Gravar uma versão nova da página. Registro: a versão, no histórico da página. |
| O campo **Reviewers** | Um comentário da página com o usuário do revisor |
| O passo 6, 8 ou 10 de "Revisar um documento" | O passo 6, 7 ou 9 de "Revisar um documento fora do Git" |

#### Pedir a revisão de um documento fora do Git

- **Responsável:** redator
- **Entrada:** o documento novo ou alterado, numa versão da página
- **Gatilho e prazo:** o redator termina o texto. Prazo: nenhum. A duração da revisão (M5) começa no pedido de revisão.

1. Declare a versão do PTS-BR na primeira linha ou num campo da página: `pts-br: "1.0"`.
2. Exporte o texto para um arquivo `.md` e execute o linter (ver os passos 1 e 2 de "Revisar um documento fora do Git").
3. Corrija cada alerta. Se o texto seguir a regra, escreva a justificativa num comentário da página.
4. Envie ao revisor o link da versão da página, num comentário com o usuário do revisor.

   Registro: o comentário de pedido, na página. A data do comentário é o campo "Data do pedido de revisão" do Anexo C.
5. Verifique que o comentário mostra o usuário do revisor.

   Este procedimento termina neste passo. O revisor recebe o pedido no procedimento "Revisar um documento fora do Git".

#### Revisar um documento fora do Git

- **Responsável:** revisor
- **Entrada:** o link da versão do documento, que o redator envia
- **Gatilho e prazo:** o pedido de revisão do redator. Prazo: 3 dias úteis para a primeira revisão e 2 dias úteis para cada revisão depois de uma correção.

**Antes de começar**

- Confirme que o documento tem `pts-br: "1.0"` na primeira linha ou num campo da página.
- Copie a tabela do Anexo C para um anexo da página.

1. Exporte o texto para um arquivo `.md`:
   - Google Docs: clique em **Arquivo** > **Fazer download** > **Markdown (.md)**.
   - Confluence ou SharePoint: exporte a página para o formato Word (`.docx`). Converta o arquivo para Markdown:

     ```shell
     pandoc --from docx --to gfm --output documento.md documento.docx
     ```
2. Execute o linter e calcule M1 e as palavras de M2 no arquivo `.md`:

   ```shell
   python3 tools/check_spec.py --limite-frase auto documento.md
   python3 tools/check_spec.py --metricas documento.md
   ```

   Registro: na primeira revisão, M1 e M2 na submissão, na tabela do Anexo C.
3. Aplique a lista de verificação da seção 4.2. Escreva cada desvio novo num comentário da página, com o formato da seção 4.1. Escreva o estado `CORRIGIDO` em cada desvio corrigido.
4. Preencha a tabela do Anexo C com os desvios, os alertas de cada regra e os falsos positivos.

   Registro: a tabela do Anexo C, no anexo da página.
5. Peça ao aprovador cada exceção S2 necessária. No comentário do desvio, escreva a justificativa, o estado `EXCECAO-PEDIDA` e o usuário do aprovador.

   O aprovador recebe o pedido no procedimento "Decidir uma exceção S2" (ver 4.1).
6. Aguarde a decisão de cada exceção pedida:
   - Se nenhum desvio tiver o estado `EXCECAO-PEDIDA`, vá para o passo 7.
   - Se o aprovador decidir cada exceção pedida, escreva a decisão na tabela. Vá para o passo 7.
   - Se o aprovador não decidir uma exceção em 2 dias úteis, escreva o estado `ABERTO` e a causa "sem decisão no prazo" na tabela. Vá para o passo 7.
7. Decida o resultado com o critério da seção 4.4:
   - Se o resultado for "Aprovado" ou "Aprovado com exceções", vá para o passo 8.
   - Se o resultado for "Reprovado", escreva o resultado na tabela e informe ao redator os desvios com o estado `ABERTO`. O redator recebe a página no procedimento "Corrigir os desvios da revisão". Aguarde o novo pedido. Se o redator pedir a revisão de novo, volte ao passo 1. Depois do 3º resultado "Reprovado", envie a página ao mantenedor. Este procedimento termina neste passo. O mantenedor recebe a página no procedimento "Decidir um conflito de revisão".
   - Se o resultado for "Reprovado" e o redator não pedir a revisão de novo em 10 dias úteis, escreva o resultado na tabela. O processo termina neste passo.
8. Escreva o resultado, M1 e M2 na publicação e o tempo de revisão na tabela do Anexo C. Peça a aprovação ao aprovador num comentário da página.

   Registro: a tabela do Anexo C, no anexo da página. O aprovador recebe a página no procedimento "Aprovar a publicação de um documento fora do Git".
9. Verifique a decisão do aprovador na página:
   - Se a tabela do Anexo C mostrar o nome do aprovador e a data da aprovação, o processo termina neste passo.
   - Se o aprovador recusar o resultado, volte ao passo 7 (no máximo 2 vezes). Depois, envie a página ao mantenedor. Este procedimento termina neste passo. O mantenedor recebe a página no procedimento "Decidir um conflito de revisão".
   - Se o aprovador não decidir em 2 dias úteis, envie a página ao mantenedor. Este procedimento termina neste passo. O mantenedor recebe a página no procedimento "Decidir um conflito de revisão".

#### Aprovar a publicação de um documento fora do Git

- **Responsável:** aprovador
- **Entrada:** a página com a tabela do Anexo C preenchida pelo revisor
- **Gatilho e prazo:** o pedido de aprovação do revisor. Prazo: 2 dias úteis.

1. Leia a tabela do Anexo C e os comentários de desvio.
2. Compare o resultado com o critério da seção 4.4. Confirme que cada exceção tem o estado `EXCECAO` com o usuário de um aprovador:
   - Se o resultado cumprir a seção 4.4, vá para o passo 3.
   - Se o resultado não cumprir a seção 4.4, escreva a causa da recusa num comentário da página. Registro: o comentário de recusa, na página. Este procedimento termina neste passo. O revisor recebe a página no passo 9 de "Revisar um documento fora do Git".
3. Aprove a versão com o recurso de aprovação da ferramenta. Se a ferramenta não tiver este recurso, escreva o seu nome e a data na tabela do Anexo C.

   Registro: a aprovação, no histórico da página ou na tabela do Anexo C.
4. Verifique que a tabela do Anexo C está anexada à versão publicada do documento.

   A tabela mostra o resultado e a aprovação. O processo termina neste passo.

**Retenção.** Mantenha a tabela de revisão enquanto o documento existir e mais 1 ano.
A tabela é a informação documentada da revisão (ISO 9001, seção 7.5).

---

## 5. Métricas

### 5.1 Como contar as palavras e as frases

Use as mesmas regras em todas as métricas.
- Não conte o cabeçalho, os blocos de código, as URLs e as tabelas.
- Conte o código em linha (`assim`) como 1 palavra.
- Conte como 1 palavra cada literal de código, cada rótulo de interface, cada
  espaço reservado e cada número com a unidade ("10 GB") ([R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)).
- Conte as contrações e as palavras com hífen como 1 palavra ([R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)).
- Separe as frases pelo ponto final, pelo ponto de interrogação, pelo ponto de
  exclamação e pelos dois-pontos no fim de linha. Um item de lista sem ponto é uma
  frase.

O `tools/check_spec.py --metricas` segue estas regras, com 2 diferenças. O script conta
"10 GB" como 2 palavras. O script conta um texto em negrito como 1 palavra apenas se o
texto tiver até 3 palavras. O revisor confirma as frases com o número de palavras do limite, mais ou menos 2 palavras.

### 5.2 Instrumentos de medição

| Métrica | O que mede | Instrumento de medição | Quem mede | Quando |
|---|---|---|---|---|
| M1 | Frases dentro do limite de [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale) | `python3 tools/check_spec.py --metricas`. Registro: o campo `M1-sub` ou `M1-pub` do comentário de resultado ou do Anexo C. | Revisor | Na submissão e na publicação |
| M2 | Palavras não aprovadas confirmadas por 1 000 palavras | `python3 tools/check_spec.py --metricas`: as palavras do linter e da lista branca, cada uma 1 vez. O revisor confirma cada palavra. Registro: o campo `M2-sub` ou `M2-pub`. | Revisor | Na submissão e na publicação |
| M3 | Desvios por 1 000 palavras | Registros de revisão (formato da seção 4.1) | Mantenedor | A cada mês |
| M4 | Índice de legibilidade (opcional) | Ferramenta escolhida pelo mantenedor. A pasta `tools/` não tem esta ferramenta. | Mantenedor | A cada 3 meses |
| M5 | Tempo e duração da revisão | Campos `min`, `pedido` e `resultado` do registro de revisão | Mantenedor | A cada mês |
| M6 | Falsos positivos do linter, por regra | Linha `[LINTER]` do registro de revisão | Mantenedor | A cada mês |
| M7 | Prazo dos PMD | Colunas de data e de prioridade do registro de decisões (ver 7.6) | Mantenedor | A cada mês |

**Submissão e publicação.** O revisor mede M1 e M2 2 vezes. A primeira vez é na
submissão: a primeira execução do CI no pull request (passo "Métricas M1 e M2", ver 6.7),
ou a primeira revisão fora do Git. A outra vez é na publicação: a versão aprovada. A meta da
fase (ver 5.9) usa o valor da submissão: este valor mostra a escrita do redator. O
valor da publicação mostra o texto que o leitor recebe. O auditor usa o valor da
publicação.

### 5.3 M1 — Frases dentro do limite

- Como calcular: frases dentro do limite ÷ total de frases × 100.
- Limite: 20 palavras nos passos de procedimento, 25 palavras no texto descritivo ([R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)).
- Instrumento de medição: `tools/check_spec.py --metricas`. O script usa o limite de 20 palavras
  nos itens de uma lista com números e o limite de 25 palavras nas outras frases.

### 5.4 M2 — Palavras não aprovadas

- Como calcular: palavras não aprovadas confirmadas ÷ total de palavras × 1 000.
- Instrumento de medição: `tools/check_spec.py --metricas`. O comando junta 2 listas:
  - Os alertas das regras `PalavrasNaoAprovadas`, `Haver` e `GlossarioProjeto`. Estas regras
    têm as palavras "Não aprovada" do 03, as tabelas 5.4 e 6.3 do 04 e os sinônimos não
    aprovados do glossário do projeto (`--glossario`).
  - As palavras fora da lista branca: uma palavra sem entrada no 03 e no 04 também é não
    aprovada (regra D9 do 03). Um termo do glossário do projeto é aprovado (`--glossario`).
- Conte cada palavra 1 vez. Uma palavra que as 2 listas mostram na mesma linha conta 1 vez.
- Um tempo verbal não aprovado de um verbo aprovado ("enviava", "irá") é um desvio de
  CK-3.1, e M2 não conta a palavra. O comando mostra estas palavras à parte.
- O revisor confirma cada palavra com o item CK-1.1. M2 conta apenas as palavras
  confirmadas. M6 conta os falsos positivos do linter.
- Não conte as tabelas (seção 5.1).

### 5.5 M3 — Desvios por 1 000 palavras

- Como calcular: quantidade de desvios ÷ total de palavras × 1 000.
- Meça M3 2 vezes:
  - **Na submissão:** todos os desvios registrados, com qualquer estado. M3 na
    submissão mostra o que o redator já sabe aplicar.
  - **Na publicação:** os desvios S1 e S2 com o estado `ABERTO` ou `EXCECAO` no
    resultado final. M3 na publicação mostra a qualidade que o leitor recebe.
- Separe M3 por severidade do desvio (S1, S2, S3).
- Instrumento de medição: os registros de revisão (formato da seção 4.1).

### 5.6 M4 — Índice de legibilidade (opcional)

O Índice de Legibilidade de Flesch para o português (Martins e outros, 1996) usa esta fórmula de cálculo:

```text
ILF = 248,835 − (1,015 × palavras por frase) − (84,6 × sílabas por palavra)
```

| Índice | Leitura |
|---|---|
| 75 a 100 | Leitura sem esforço, nível 1 |
| 50 a 75 | Leitura sem esforço, nível 2 |
| 25 a 50 | Leitura com esforço, nível 1 |
| 0 a 25 | Leitura com esforço, nível 2 |

Referência: Martins, Ghiraldelo, Nunes e Oliveira Jr. (1996), "Readability formulas applied to textbooks in Brazilian Portuguese", Notas do ICMC-USP, Série Computação, n. 28 [verificar], São Carlos.

**Limites de M4. Leia estes limites antes de usar M4.**
1. Os autores ajustaram os números com textos que não são técnicos, não com texto técnico de software.
2. O índice mede apenas o tamanho da frase e o tamanho da palavra. O índice não mede
   frases com 2 significados, a ordem dos passos, a voz passiva nem as palavras não aprovadas.
3. Termos técnicos longos e corretos ("autenticação", "configuração") diminuem o
   índice. Um leitor da área entende estes termos sem esforço a mais.
4. As ferramentas dividem as palavras do português com regras diferentes. Use sempre a
   mesma ferramenta e a mesma versão. Não compare valores de ferramentas diferentes.
5. 2 textos com menos de 100 palavras e com a mesma qualidade têm valores diferentes. Não aplique M4 a
   mensagens de interface.
6. Alguns textos com um índice alto têm desvios do PTS-BR.

Use M4 apenas para comparar períodos. M4 nunca é critério de aprovação de um documento
nem critério de fase.

### 5.7 M5, M6 e M7

- **M5 — Tempo de revisão:** minutos de revisão PTS-BR por 1 000 palavras. Dados:
  campos `min` e `palavras` do resultado.
- **M5 — Duração da revisão:** dias úteis entre o pedido de revisão e o resultado final.
  Dados: campos `pedido` e `resultado` do resultado. O valor da fase é a mediana das
  durações dos documentos da fase.
- **M6 — Falsos positivos do linter, por regra:** falsos positivos da regra ÷
  total de alertas da regra × 100. Dados: a linha `[LINTER]` de cada registro de revisão.
  O mantenedor soma os 2 números de cada regra em todos os registros do mês.
- **M7 — Prazo dos PMD:** PMD com a triagem, a decisão e a publicação no prazo da
  seção 7.4 ÷ total de PMD × 100. Dados: as colunas de data e de prioridade do registro de
  decisões (ver 7.6).

Um tempo de revisão alto e estável indica falta de treinamento ou regras difíceis de aplicar.
Com uma regra de M6 alto, o redator para de ler os alertas do linter.

### 5.8 Linha de base

Meça a linha de base antes do Piloto, em no mínimo 20 documentos da equipe do Piloto
publicados antes do PTS-BR.

| Métrica | Como medir a linha de base |
|---|---|
| M1 e M2 | `python3 tools/check_spec.py --metricas` nos 20 documentos. O revisor confirma as palavras de M2. |
| M3 (submissão) e M5 (tempo) | Os revisores fundadores revisam os 20 documentos com a lista de verificação e registram os desvios e os minutos com os formatos da seção 4.1. |
| M4 (opcional) | A ferramenta escolhida pelo mantenedor. |

### 5.9 Metas por fase

| Métrica | Unidade | Piloto | Expansão | Padrão |
|---|---|---|---|---|
| M1 — Frases dentro do limite, na submissão | Por documento | ≥ 85% | ≥ 92% | ≥ 95% |
| M2 — Palavras não aprovadas, na submissão | Por documento | ≤ 10 por 1 000 palavras | ≤ 5 por 1 000 palavras | ≤ 2 por 1 000 palavras |
| M3 — S1 na publicação | Por documento | 0 | 0 | 0 |
| M3 — S2 na publicação | Por documento | ≤ 5 por 1 000 palavras | ≤ 3 por 1 000 palavras | ≤ 1,5 por 1 000 palavras |
| M3 — Desvios na submissão | Total da fase | Sem meta | 30% menor que a linha de base | 50% menor que a linha de base |
| M5 — Tempo de revisão | Total da fase | Sem meta | ≤ 30 min por 1 000 palavras | ≤ 20 min por 1 000 palavras |
| M5 — Duração da revisão | Mediana da fase | ≤ 5 dias úteis | ≤ 3 dias úteis | ≤ 2 dias úteis |
| M6 — Falsos positivos | Por regra | ≤ 20% | ≤ 10% | ≤ 5% nas regras `error` |
| M7 — Prazo dos PMD | Total da fase | ≥ 80% | ≥ 90% | ≥ 95% |

"Sem meta" indica que o Piloto mede o valor e não tem um limite. Um documento publicado
cumpre sempre as metas de M3 na publicação, porque as metas são iguais ao critério da
seção 4.4. Portanto, o critério de saída "por documento" das fases usa apenas M1 e M2 na
submissão (ver 3.2 e 3.3). As metas da fase
Padrão são valores iniciais. O mantenedor revisa as metas 1 vez por ano com os
dados reais.

---

## 6. Ferramentas de verificação

### 6.1 Ferramentas desta versão

| Ferramenta | Arquivo | Uso |
|---|---|---|
| Linter em Python | [`tools/check_spec.py`](https://github.com/dvwinck/pts-br/blob/main/tools/check_spec.py) | Motor do linter de referência da versão 1.0.0. Aplica as regras de `tools/vale/PTSBR/*.yml` sem o Vale. Também testa as regras e verifica o texto da especificação. Calcula M1 e M2 e mostra as palavras fora da lista branca. Verifica as mensagens de interface dos arquivos de tradução (`--mensagens`). Lê o `.vale.ini` (`--config`) e o glossário do projeto (`--glossario`). |
| Lista branca | [`tools/lista_branca.py`](https://github.com/dvwinck/pts-br/blob/main/tools/lista_branca.py) | Gera as formas válidas das palavras aprovadas do 03 e dos termos do 04. Um termo composto do 04 é uma unidade. O modo `check_spec.py --lista-branca` usa este arquivo (ver 6.8). A lista branca verifica a forma, não o significado. |
| Vale (versão do CI: 3.27.0) | [`tools/vale/`](https://github.com/dvwinck/pts-br/tree/main/tools/vale) | Segundo motor do linter. Lê Markdown e não lê o código. |
| Script das regras de palavras | [`tools/gerar_regras_dicionario.py`](https://github.com/dvwinck/pts-br/blob/main/tools/gerar_regras_dicionario.py) | Gera `PalavrasNaoAprovadas.yml` com as palavras não aprovadas do 03 e com os termos não aprovados do 04 (tabelas 5.4 e 6.3). Também lê a coluna de formas flexionadas da tabela 5.4. A regra não tem as formas iguais a uma palavra aprovada do 03 ou do 04 ("seta", "roda do mouse"). Gera `PalavrasObsoletas.yml` com as palavras obsoletas do 03 (ver 8.1). |
| Script do dicionário | [`tools/build.py`](https://github.com/dvwinck/pts-br/blob/main/tools/build.py) | Verifica os arquivos de origem do dicionário e gera o [`03-dicionario.md`](03-dicionario.md). |
| Pipeline de CI da especificação | [`tools/ci/docs-lint.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint.yml) | GitHub Actions: testes das regras e verificação do texto da especificação. |
| Pipeline de CI de uma equipe | [`tools/ci/docs-lint-equipe.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint-equipe.yml) | GitHub Actions: o linter num repositório de equipe, com as regras de uma versão fixa (ver 6.7). |

**Motor de referência.** Na versão 1.0.0, o linter em Python é a referência: um
critério de publicação ou de fase usa o resultado do `check_spec.py`.
As regras da versão 1.0.0 não têm resultado com o Vale. A revisão 2 da especificação
testou com o Vale 3.27.0 uma versão anterior das regras (87 testes). Depois deste teste, o
mantenedor alterou 8 dos 13 arquivos de regra. O teste das regras atuais com o Vale é um critério de
entrada do Piloto (ver 3.2), não um critério de publicação da versão 1.0.0.

O Vale e o `check_spec.py` encontram apenas padrões de texto. As 2 ferramentas
não fazem análise das classes de palavras. O LanguageTool e um programa de análise
de palavras (por exemplo, spaCy) encontram mais desvios, mas não fazem parte desta versão.

### 6.2 Estrutura da pasta `tools/`

```text
tools/
├── build.py                      # d*.txt -> 03-dicionario.md, com verificações
├── .gitignore                    # __pycache__/
├── d1.txt a d4.txt               # origem das entradas do dicionário
├── intro.md                      # origem do texto inicial do 03
├── gerar_regras_dicionario.py    # 03 e 04 -> vale/PTSBR/PalavrasNaoAprovadas.yml e PalavrasObsoletas.yml
├── check_spec.py                 # linter em Python, testes, métricas, lista branca, mensagens
├── lista_branca.py               # formas válidas: 03, 04 e 01 (seção 11.2)
├── ci/
│   ├── docs-lint.yml             # pipeline do repositório da especificação
│   └── docs-lint-equipe.yml      # pipeline de um repositório de equipe
└── vale/
    ├── .vale.ini                 # configuração do Vale e dos limites de frase por pasta
    ├── PTSBR/                    # 14 regras e PalavrasObsoletas.yml, se o 03 tiver palavras obsoletas (ver 6.3)
    ├── config/vocabularies/PTSBR/
    │   └── accept.txt            # nomes próprios com uma palavra não aprovada ("Time Machine")
    └── testes/
        └── <NomeDaRegra>/
            ├── deve_alertar.md      # 1 teste por linha: a regra precisa alertar
            └── nao_deve_alertar.md  # 1 teste por linha: a regra não pode alertar
```

A pasta `tools/` tem apenas os arquivos desta lista. Os scripts de trabalho da
revisão da especificação não fazem parte da versão.

Regras para a pasta [`tools/vale/`](https://github.com/dvwinck/pts-br/tree/main/tools/vale):
- Cada regra mostra o ID da regra de [`02-regras.md`](02-regras.md) na primeira linha do arquivo e no
  início da mensagem.
- Cada regra tem os 2 arquivos de teste.
- Não altere os arquivos `PalavrasNaoAprovadas.yml` e `PalavrasObsoletas.yml` manualmente. Gere os arquivos com o script.
- Os padrões usam `nonword: true`, `\s+` entre palavras e os limites de palavra
  `(?<![\p{L}-])` e `(?![\p{L}-])`. Com o hífen no limite, "o mesmo e-mail" não
  gera alerta.

### 6.3 Regras implementadas

Nesta versão, as regras têm o nível `warning`. A regra gerada `PalavrasObsoletas` tem o nível `suggestion`.

| Arquivo em [`tools/vale/PTSBR/`](https://github.com/dvwinck/pts-br/tree/main/tools/vale/PTSBR) | Regra | O que a regra encontra | Limite conhecido |
|---|---|---|---|
| `PalavrasObsoletas.yml` | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Gerada apenas se o 03 tiver palavras obsoletas. As formas de cada palavra obsoleta, com a alternativa aprovada. | Nesta versão, o 03 não tem palavras obsoletas, e a regra não existe. |
| `Mensagens.yml` | [R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor), [R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor), [R10.8](02-regras.md#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor) | Apenas no modo `--mensagens` (ver 6.9). Encontra "(s)" e "(es)", a variável por posição (`%s`, `{0}`) e um artigo antes de uma variável. Também encontra "com sucesso", "Algo deu errado", "Erro desconhecido", "Falha na operação", as interjeições e o ponto de exclamação. | Não conta as palavras de uma mensagem de sucesso ([R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor)). Não verifica as 3 formas do plural. O `.vale.ini` desliga a regra nos arquivos Markdown. |
| `PalavrasNaoAprovadas.yml` | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | As entradas "Não aprovada" do 03 e os termos não aprovados do 04 (tabela 5.4, verbos com radical estrangeiro, e tabela 6.3), com as formas flexionadas. As formas são o plural, o feminino e as formas verbais de todos os tempos. Exemplos: "deployei", "commite", "mergeie", "dê push". | O script não cria a 1ª pessoa do singular do presente ("-o"). Não encontra palavras ausentes do 03: o modo `--lista-branca` mostra estas palavras (ver 6.8). Não alerta "status" nos nomes técnicos "código de status" (04, [NT-08](04-termos-tecnicos.md#nt-08-códigos-identificadores-e-números-de-referência)) e "página de status". Não alerta uma forma igual a uma palavra aprovada ("seta") nem uma forma dentro de um termo composto aprovado ("roda do mouse"). |
| `Haver.yml` | [R4.3](02-regras.md#r43-escreva-o-sujeito-antes-do-verbo-e-faça-a-concordância-vale) | O verbo "haver": "há", "houve", "houveram", "havia", "houver". O 03 também marca "haver" como não aprovada. | Não verifica as outras inversões nem a concordância. |
| `OMesmo.yml` | [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) | "o mesmo" antes de pontuação, verbo, conector ou preposição. Não alerta "é o mesmo" (adjetivo). | Não encontra "o mesmo" antes de um verbo fora da lista. |
| `OndeRelativo.yml` | [R1.9](02-regras.md#r19-use-onde-apenas-para-lugar-vale) | "onde" depois de uma palavra que não é um lugar da lista (pasta, arquivo, servidor, ambiente, região, tabela). Não alerta uma pergunta ("Onde fica o arquivo?"). | O revisor confirma cada alerta. Um lugar com complemento ("o servidor de produção onde") gera um alerta. |
| `FuturoSimples.yml` | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale) | O futuro simples ("enviará", "será") e "irá" + infinitivo. | Não encontra o futuro do pretérito nem o pretérito imperfeito. O modo `--lista-branca` mostra estas formas. |
| `PassivaSintetica.yml` | [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale) | A voz passiva com "se" depois do verbo ("Instala-se", "Deve-se"). | Não encontra o "se" antes do verbo ("não se recomenda"). |
| `VerboSuporte.yml` | [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale) | "realizar", "efetuar", "proceder", "promover", "fazer" ou "dar" + artigo + substantivo em "-ção", "-são", "-mento", "-agem". | Não alerta "ação", "função", "versão", "permissão", "sessão", "mensagem", "imagem", "documento", "argumento", "procedimento". |
| `Gerundismo.yml` | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale) | "vai estar enviando" e 2 gerúndios seguidos. | Não encontra 2 gerúndios com outras palavras entre os gerúndios. |
| `Enclise.yml` | [R3.7](02-regras.md#r37-não-use-pronomes-oblíquos-átonos-nem-mesóclise-vale) | Pronome átono com hífen ("cole-o", "instalá-lo") e mesóclise ("enviar-lhe-á"). | Não encontra o pronome antes do verbo ("o instale"). |
| `FraseLonga.yml` | [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale) | Frase com mais de 25 palavras. | O Vale não conta o código em linha nem o negrito e conta "10 GB" como 2 palavras. |
| `FraseLongaProcedimento.yml` | [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale) | Frase com mais de 20 palavras. Ative a regra nas pastas de procedimentos (ver 6.5). | Igual a `FraseLonga.yml`. |
| `SeparadorMilhar.yml` | [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale) | Ponto como separador de milhar ("1.000", "R$ 1.500,00"). | Também encontra um endereço IP fora de código. |
| `Unidades.yml` | [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale) | Unidade por extenso depois de número ("10 segundos"), símbolo não aprovado ("2.5seg", "10 KB", "100 Mbps") e número sem espaço antes do símbolo ("30s"). | Não verifica números por extenso. Não verifica o formato da hora ([R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor)): "às 14h" não gera alerta. |

Os 2 motores do linter não verificam os literais da regra [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor): o código em linha e o negrito.
O negrito marca um rótulo de interface, um valor de estado da interface ou uma palavra
de sinalização. O Vale não lê o negrito (`IgnoredScopes = code, tt, strong` no
`.vale.ini`). O `check_spec.py` não lê o negrito de até 3 palavras e conta este negrito
como 1 palavra. Exemplo: "o estado **Concluído**" não gera alerta, porque "Concluído" é
o rótulo exato da interface.

As regras sem arquivo nesta tabela são verificadas apenas pelo revisor. A coluna
"Linter" da lista de verificação (ver 4.2) mostra a mesma relação.

### 6.4 Nível das regras e severidade

| Nível do Vale | Condição | Efeito no CI |
|---|---|---|
| `error` | Regra com M6 de no máximo 5%, medido com no mínimo 50 alertas. | Bloqueia o merge a partir da fase Expansão. |
| `warning` | Regra sem M6 medido ou com M6 maior que 5%. O revisor confirma cada alerta. | Mostra o alerta no log do CI. Não bloqueia. |
| `suggestion` | Regra para desvios S3 ou para palavras obsoletas (ver 8.1). | Mostra o alerta no log do CI. Não bloqueia. |

Nesta versão, as regras têm o nível `warning`, e `PalavrasObsoletas` tem o nível
`suggestion`. O nível `error` não altera a conformidade de um texto, porque o revisor já
verifica a regra. Portanto, a alteração de uma regra para o nível `error` é uma versão MINOR. O mantenedor escreve a entrada "Alterado (linter)" no [`CHANGELOG.md`](CHANGELOG.md), com o
valor de M6 e o número de alertas medidos (ver 8.1).

A maior parte dos desvios S1 depende da decisão do revisor. O linter não
substitui o revisor nos itens S1.

Para desligar uma regra numa parte do texto, use o comentário do Vale e registre a exceção
no registro de revisão. O `check_spec.py` também lê este comentário.

```markdown
<!-- vale PTSBR.FraseLonga = NO -->
Texto com o rótulo exato da interface.
<!-- vale PTSBR.FraseLonga = YES -->
```

### 6.5 Executar o linter no seu computador

**Linter em Python (Python 3.9 ou mais novo, sem instalação)**

No repositório da especificação:

Verifique o documento com as regras do linter:

```shell
python3 tools/check_spec.py docs/runbook.md
```

Calcule M1 e as palavras de M2. O comando mostra a linha `[METRICAS]` do registro de revisão (ver 4.1):

```shell
python3 tools/check_spec.py --metricas docs/runbook.md
```

Mostre as palavras fora da lista branca:

```shell
python3 tools/check_spec.py --lista-branca docs/runbook.md
```

Num repositório de equipe, obtenha a versão da especificação que a equipe declara (por
exemplo, a tag `v1.0.0`) na pasta `.pts-br/`. Depois, informe as pastas e os arquivos
das regras. Verifique o documento com as regras do linter e com o `.vale.ini` da equipe:

```shell
python3 .pts-br/tools/check_spec.py \
  --regras .pts-br/tools/vale \
  --config .vale.ini \
  --glossario docs/glossario.md \
  docs/runbook.md
```

Verifique as mensagens de interface de um arquivo de tradução (ver 6.9):

```shell
python3 .pts-br/tools/check_spec.py \
  --regras .pts-br/tools/vale \
  --mensagens \
  locales/pt-BR.json
```

Mostre as palavras fora da lista branca:

```shell
python3 .pts-br/tools/check_spec.py \
  --lista-branca \
  --dicionario .pts-br/03-dicionario.md \
  --termos .pts-br/04-termos-tecnicos.md \
  --glossario docs/glossario.md \
  docs/runbook.md
```

| Opção | Valor |
|---|---|
| `--regras PASTA` | A pasta `PTSBR` com as regras ou a pasta que contém a pasta `PTSBR`. |
| `--dicionario ARQUIVO` | O [`03-dicionario.md`](03-dicionario.md) da versão (modo `--lista-branca`). |
| `--termos ARQUIVO` | O [`04-termos-tecnicos.md`](04-termos-tecnicos.md) da versão (modo `--lista-branca`). |
| `--limite-frase` | `auto` (padrão): 20 palavras nos itens de lista numerada e 25 nas outras frases ([R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)). `pasta`: o limite do Vale para a pasta do arquivo, de acordo com as seções do `.vale.ini`. `descritivo` ou `procedimento`: 1 limite para todo o arquivo. |
| `--config ARQUIVO` | Um `.vale.ini`. O script lê `MinAlertLevel`, `StylesPath`, as seções de pastas, `BasedOnStyles` e `PTSBR.<Regra> = YES`, `NO` ou um nível, como o Vale. O script compara o caminho do documento com as seções a partir da pasta do `.vale.ini`, também para um caminho completo. Sem `--config`, o script usa todas as regras, exceto `Mensagens`. Com `--limite-frase pasta` e sem `--config`, o script lê o `.vale.ini` da pasta atual ou o `.vale.ini` das regras. |
| `--glossario ARQUIVO` | O glossário do projeto, com a tabela do modelo de [`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 7](04-termos-tecnicos.md#7-glossário-do-projeto). A coluna "Termo" entra na lista branca e em M2. A coluna "Sinônimos não aprovados" gera a regra `GlossarioProjeto` ([R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale)): "[R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale): 'billing' não é aprovado no glossário do projeto. Use 'serviço de cobrança'." |
| `--mensagens` | Os arquivos são arquivos de tradução: JSON plano ou com níveis (`.json`) e `gettext` (`.po`, `.pot`). Ver 6.9. |

Use a opção `--spec` apenas no texto da própria especificação. O script recusa
`--spec` com um arquivo fora da pasta da especificação.

**Vale**

1. Instale o Vale 3.27.0. No macOS, use o Homebrew:
   ```shell
   brew install vale
   ```
   Nos outros sistemas, copie o arquivo do Vale da página de versões do projeto
   (`https://github.com/vale-cli/vale/releases`).
2. Execute o Vale com a configuração da versão da especificação:
   ```shell
   vale --config .pts-br/tools/vale/.vale.ini docs/
   ```

Para alterar as pastas de procedimentos e de runbooks, copie o `.vale.ini` para a pasta
principal do repositório e altere o `StylesPath` para `.pts-br/tools/vale`. Use o mesmo
arquivo no Vale (`vale --config`) e no `check_spec.py` (`--config`): os 2 motores do linter
aplicam as mesmas regras às mesmas pastas.

### 6.6 Testes das regras

Execute os testes depois de cada alteração numa regra ou no dicionário:

Teste as regras com o motor do linter em Python:

```shell
python3 tools/check_spec.py --teste
```

Teste as regras com o Vale:

```shell
python3 tools/check_spec.py --teste --motor vale --vale "$(command -v vale)"
```

Os testes verificam 3 conjuntos de textos:
1. Os testes de `tools/vale/testes/<NomeDaRegra>/`. Cada linha de `deve_alertar.md`
   precisa gerar um alerta da regra. Cada linha de `nao_deve_alertar.md` não pode
   gerar um alerta da regra.
2. Os textos "Antes" e "PTS-BR" de cada exemplo de [`06-exemplos.md`](06-exemplos.md). Cada texto
   "Antes" precisa gerar no mínimo 1 alerta. Cada alerta num texto "PTS-BR" é um
   falso positivo ou um desvio do exemplo. O teste mostra estes alertas.
3. As frases de teste da lista branca (ver 6.8). As frases PTS-BR não têm palavras fora
   da lista. Nas outras frases, o teste encontra a palavra não aprovada.

Os testes leem como texto as mensagens de interface entre crases do 06, se a
mensagem começa com maiúscula e termina com ponto.

Resultado em 2026-11-18, com o linter em Python (referência da versão 1.0.0):
- Os 160 testes de regra estão corretos.
- Os textos "Antes" dos 10 exemplos do 06 geram 122 alertas.
- Os textos "PTS-BR" do 06 geram 0 alertas.
- As 24 frases da lista branca estão corretas.
- Os 13 testes das opções `--config`, `--glossario`, `--mensagens` e `--metricas` estão corretos.

Resultado com o Vale: as regras da versão 1.0.0 não têm resultado com o Vale. A revisão 2
testou uma versão anterior das regras (87 testes). Antes do Piloto, o mantenedor executa o
job `vale` do pipeline (ver 6.7). O mantenedor grava a saída em
`tools/vale/testes/resultado-vale-3.27.0.txt`, com a data, a versão e o número de testes.
Os 2 motores do linter contam as palavras e dividem as frases com regras diferentes (ver
6.3). O revisor confirma os alertas de frase longa com 1 ou 2 palavras a mais que o limite.

### 6.7 Integração no CI

A pasta [`tools/ci/`](https://github.com/dvwinck/pts-br/tree/main/tools/ci) tem 2 pipelines para o GitHub Actions. Os 2 pipelines dão ao token
apenas a permissão `contents: read`. Os pipelines usam apenas a ação oficial
`actions/checkout`, com a tag `v5`. Esta versão da especificação não verificou o hash
do commit desta tag. Antes de usar um pipeline em produção, escreva no pipeline o hash do
commit da versão de `actions/checkout` que a sua equipe verificou. O passo que instala o Vale
compara o hash SHA-256 do arquivo com a lista de hashes da mesma página de versões do Vale.
Para não depender desta lista, escreva o hash SHA-256 do arquivo no pipeline.

**Repositório da especificação (`docs-lint.yml`)**

| Job | Passos |
|---|---|
| `regras` | Executa `build.py` (critério 1 da seção 8.5) e compara o 03 com o resultado de `build.py --render` (critério 2). Confirma que `PalavrasNaoAprovadas.yml` é igual ao resultado do script com o 03 e o 04 (`gerar_regras_dicionario.py --verificar`). Executa os testes com o linter em Python. Executa `check_spec.py --spec --falhar`: 1 alerta bloqueia o merge. Executa `check_spec.py --lista-branca --spec --meta 1`: mais de 1% de palavras fora da lista branca bloqueia o merge. |
| `vale` | Instala o Vale 3.27.0, executa os testes com o Vale e grava a saída em `tools/vale/testes/resultado-vale-3.27.0.txt` no computador do job. O mantenedor copia a saída do log para este arquivo no repositório. |

No repositório da especificação, o Vale não verifica o texto da especificação. O Vale
não tem as regras do modo `--spec` para os exemplos e as menções (ver 6.8).

**Repositório de equipe (`docs-lint-equipe.yml`)**

O pipeline não depende da estrutura de pastas da especificação nem do repositório
da equipe. A equipe altera estas variáveis no bloco `env`:

| Variável | Valor |
|---|---|
| `PTSBR_REPO` | O repositório da especificação. |
| `PTSBR_REF` | A tag da última PATCH da versão que os documentos declaram, por exemplo `v1.0.1` para `pts-br: "1.0"` (ver 8.4). |
| `DOCS` | As pastas e os arquivos Markdown que o linter verifica. Um item que não existe não para o job. |
| `GLOSSARIO` | O arquivo do glossário do projeto (opção `--glossario`). Vazio: sem glossário. |
| `MENSAGENS` | Os arquivos de tradução `.json` ou `.po` (opção `--mensagens`, ver 6.9). Vazio: sem o passo de mensagens. |
| `FASE` | `piloto`, `expansao` ou `padrao`. |

O job obtém as regras da versão `PTSBR_REF` na pasta `.pts-br/` e executa estes passos:
1. O Vale, com o `.vale.ini` da equipe ou da versão. O código de saída 2 do Vale (erro de
   configuração ou de regra) falha o job também no Piloto.
2. O `check_spec.py` com o mesmo `.vale.ini` (`--config`) e o limite de frase de [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)
   (`--limite-frase auto`).
3. O `check_spec.py --mensagens`, se a variável `MENSAGENS` tiver um arquivo.
4. O relatório da lista branca. Este passo não bloqueia o merge.
5. O `check_spec.py --metricas`: a linha `[METRICAS]` de cada documento, no resumo do job.
   O revisor copia os valores da primeira execução para o comentário de resultado (ver
   4.1). O log e o resumo do job não são permanentes.

O resultado está no log do job. Se o repositório da especificação for privado, o
`GITHUB_TOKEN` do repositório da equipe não lê a especificação. Crie um token apenas com
permissão de leitura do repositório da especificação. Grave o token no segredo
`PTSBR_TOKEN` e use o segredo na opção `token` do passo que obtém as regras.

O mantenedor informa cada versão PATCH às equipes no dia da publicação. Cada equipe
altera `PTSBR_REF` para a tag nova.

Configuração por fase:
- **Piloto:** `FASE: 'piloto'`. O linter mostra os alertas e não bloqueia o merge.
- **Expansão e Padrão:** `FASE: 'expansao'` ou `FASE: 'padrao'`. Um alerta de uma regra
  com o nível `error` bloqueia o merge (ver 6.4).

### 6.8 Verificação do texto da especificação

Verifique o texto com as regras do linter:

```shell
python3 tools/check_spec.py --spec --resumo
```

Mostre as palavras fora da lista branca:

```shell
python3 tools/check_spec.py --lista-branca --spec
```

O modo `--spec` verifica o `README.md`, o 01, o 02, o 04, o 05 e as seções "PTS-BR" do 06
com as regras do linter. O modo `--lista-branca --spec` também verifica o 03. Os 2 modos
não verificam estas partes do texto:
- Os blocos de código e o código em linha.
- Os exemplos "Não aprovado".
- As colunas de tabela com usos não aprovados, por exemplo "Não aprovado" e "Trecho original".
- As colunas de tabela com nomes em inglês, por exemplo "Termo em inglês" e "Nome completo" das siglas.
- As menções entre aspas, quando o texto fala de uma palavra.
- O negrito de até 3 palavras: um literal da regra [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) (ver 6.3). Os outros modos também não verificam este negrito.

**Lista branca.** O modo `--lista-branca` aplica a regra D9 do 03: uma palavra sem
entrada no 03 e no 04 não é aprovada. A lista branca verifica a forma da palavra, não o
significado. O revisor verifica o significado (item CK-1.2). Uma palavra é válida se for:
1. uma forma de uma entrada aprovada do 03: o plural, o feminino e as formas verbais
   aprovadas ([`01-introducao.md`](01-introducao.md), [seção 5](01-introducao.md#5-decisões-de-base-sobre-a-língua)). O script gera as formas regulares e tem uma
   tabela de verbos irregulares;
2. um nome técnico, um termo do glossário-base ou uma sigla do 04. Um termo composto
   ("banco de dados", "roda do mouse") é uma unidade: as palavras do termo valem apenas na
   sequência do termo. As locuções do 03 ("dentro de", "em andamento") seguem a mesma regra;
3. no texto da especificação, uma palavra de metalinguagem ([`01-introducao.md`](01-introducao.md), seção
   11.2, e 04, [NT-25](04-termos-tecnicos.md#nt-25-termos-de-linguagem-e-de-redação)). Também um termo do glossário do projeto da especificação
   ([`01-introducao.md`](01-introducao.md), [seção 9](01-introducao.md#9-definições), e a seção 1 deste documento);
4. uma contração de uma preposição aprovada com um artigo ou com "este" (03, regra D2);
5. com `--glossario`, um termo do glossário do projeto.

Uma palavra "Obsoleta" do 03 continua válida até a próxima versão MAJOR (ver 8.1).

O script aceita como nome técnico ([NT-01](04-termos-tecnicos.md#nt-01-produtos-softwares-e-serviços-externos)) uma palavra com maiúscula depois do início da frase e
conta estes nomes à parte. O relatório mostra cada palavra fora da lista, a frequência,
os locais (`arquivo:linha`) e a porcentagem de palavras sem aprovação em cada arquivo.

A seção 8.5 usa os 2 resultados como critérios de publicação.

### 6.9 Mensagens de interface

As mensagens de interface estão em arquivos de tradução. O modo `--mensagens` lê estes
arquivos sem uma cópia para Markdown:
- JSON plano ou com níveis (`.json`). A chave de uma mensagem junta os níveis com ponto:
  `arquivo.salvo`.
- `gettext` (`.po`, `.pot`). O texto é o `msgstr`, ou cada `msgstr[n]` do plural. Se o
  `msgstr` estiver vazio, o texto é o `msgid` e o `msgid_plural`. O alerta mostra a linha
  da entrada.

O modo aplica a cada mensagem as regras do linter e a regra `Mensagens` ([R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor), [R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor) e
[R10.8](02-regras.md#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor), ver 6.3). Cada alerta mostra o arquivo, a chave ou a linha, e a regra:

```text
locales/pt-BR.json: arquivo.salvo: [warning] PTSBR.Mensagens: R10.5, R10.7, R10.8: 'com sucesso' não é aprovado numa mensagem de interface.
```

O revisor confirma cada alerta. Os outros pontos da Seção 10 são itens do revisor:
o número de palavras de uma mensagem de sucesso, as 3 formas do plural e a ação de uma
mensagem de erro.

### 6.10 Limites das ferramentas

Apenas o revisor verifica estes pontos:
- Se a palavra aprovada tem o significado aprovado (CK-1.2). O linter e a lista branca
  verificam a forma da palavra, não o significado.
- Se a ordem dos passos é a ordem real de execução (CK-5.1).
- Se o passo tem uma ação (CK-5.3).
- Se o aviso tem a palavra de sinalização correta e está no lugar correto (CK-7.1, CK-7.3).
- Se o rótulo do texto é igual ao rótulo da interface (CK-10.1).
- Se um pronome tem uma referência possível (CK-1.6).
- Se um termo novo é um nome técnico correto ou uma gíria da equipe.
- Se o comando ou o valor do texto funciona (revisão técnica, ver 2.1).

Um resultado sem alertas no linter não significa conformidade.

---

## 7. Manutenção do dicionário e das regras

### 7.1 Tipos de pedido

| Tipo | Destino |
|---|---|
| Palavra nova no vocabulário geral | Mantenedor ([`03-dicionario.md`](03-dicionario.md)) |
| Alteração de significado ou de classe | Mantenedor ([`03-dicionario.md`](03-dicionario.md)) |
| Exclusão de palavra, com a palavra obsoleta antes da exclusão (estado `O` em `tools/d*.txt`) | Mantenedor ([`03-dicionario.md`](03-dicionario.md)) |
| Nome técnico ou verbo técnico novo de TI | Mantenedor ([`04-termos-tecnicos.md`](04-termos-tecnicos.md)) |
| Termo de um projeto | Dono do glossário do projeto |
| Alteração de regra (PMR) | Mantenedor ([`02-regras.md`](02-regras.md)), seção 7.7 |

### 7.2 Formulário de PMD

Use este modelo como formulário de issue no repositório da especificação.

```markdown
## Pedido de mudança no dicionário (PMD)

- Tipo: palavra nova | alteração | exclusão | nome técnico | termo de projeto
- Palavra:
- Classe gramatical: substantivo | verbo | adjetivo | advérbio | preposição | conjunção | outra
- Significado proposto (uma frase):
- Por que nenhuma palavra aprovada serve:
  (Escreva as palavras aprovadas que você testou e o problema de cada uma.)
- Exemplos (no mínimo 2, de documentos reais):
  1. Frase com a palavra proposta:
     Frase com palavras aprovadas:
  2. Frase com a palavra proposta:
     Frase com palavras aprovadas:
- Documentos ou equipes que precisam da palavra:
- Prioridade: normal | urgente (aviso de segurança, passo com ação irreversível ou incidente)
- Solicitante e data:
```

### 7.3 Fluxo do pedido

**Arquivos de origem.** A origem das entradas do dicionário são os arquivos [`tools/d1.txt`](https://github.com/dvwinck/pts-br/blob/main/tools/d1.txt)
a [`tools/d4.txt`](https://github.com/dvwinck/pts-br/blob/main/tools/d4.txt). O texto inicial do 03 está em [`tools/intro.md`](https://github.com/dvwinck/pts-br/blob/main/tools/intro.md). O
[`tools/build.py`](https://github.com/dvwinck/pts-br/blob/main/tools/build.py) gera o [`03-dicionario.md`](03-dicionario.md) a partir destes arquivos. Uma alteração
manual no [`03-dicionario.md`](03-dicionario.md) não existe mais depois do próximo build.

O fluxo tem 3 procedimentos, 1 para cada responsável e etapa (regra [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor)).

#### Criar um PMD

- **Responsável:** solicitante
- **Entrada:** uma frase que precisa de uma palavra sem entrada no 03, no 04 ou no glossário do projeto
- **Gatilho e prazo:** o redator, o revisor ou o linter encontra a palavra. Prazo: nenhum.

1. Procure a palavra no [`03-dicionario.md`](03-dicionario.md), no [`04-termos-tecnicos.md`](04-termos-tecnicos.md) e no glossário do projeto.
   - Se a palavra tiver uma entrada aprovada, use a palavra. O processo termina neste passo.
   - Se a palavra não tiver uma entrada aprovada, vá para o passo 2.
2. Escreva a frase de novo com palavras aprovadas.
   - Se a frase nova tiver o mesmo significado, use a frase nova. O processo termina neste passo.
   - Se a frase nova perder o significado, vá para o passo 3.
3. Crie a issue do PMD com o formulário da seção 7.2. Escreva a prioridade.

   Registro: a issue do PMD, no repositório da especificação.
4. Verifique que a issue tem o rótulo `PMD`.

   Este procedimento termina neste passo. O mantenedor recebe a issue no procedimento "Decidir um PMD".

#### Decidir um PMD

- **Responsável:** mantenedor
- **Entrada:** a issue do PMD, que o solicitante cria
- **Gatilho e prazo:** uma issue nova com o rótulo `PMD`. Prazos: seção 7.4. Um pedido urgente tem a triagem em 1 dia útil.

1. Confirme o tipo e a prioridade do pedido (triagem).

   Registro: o ID, a prioridade e as datas do pedido e da triagem, no registro de decisões (ver 7.6).
2. Escolha o destino do pedido:
   - Se o pedido for um termo de um projeto, envie a issue ao dono do glossário do projeto. Registro: o resultado "Encaminhado", no registro de decisões. Este procedimento termina neste passo. O dono do glossário decide o termo no glossário do projeto.
   - Se o pedido for do 03 ou do 04, vá para o passo 3.
3. Consulte no mínimo 1 revisor e, se necessário, o dono do glossário.
4. Compare o pedido com os critérios de aceite da seção 7.5 e decida o resultado:
   - "Aceito" ou "Aceito com outro significado ou outra classe": vá para o passo 5.
   - "Recusado": escreva na issue a palavra aprovada ou a frase nova. Vá para o passo 5.
   - "Pendente": escreva na issue a informação que falta e aguarde 10 dias úteis. Se o solicitante responder, volte ao passo 4 (no máximo 1 vez). Sem resposta no prazo, o resultado é "Recusado". Vá para o passo 5.
5. Registre a decisão no registro de decisões e na issue.

   Registro: a linha da decisão, com a data e a justificativa, no registro de decisões.
6. Verifique o resultado na linha do registro:
   - Se o resultado for "Aceito" ou "Aceito com outro significado ou outra classe", siga o procedimento "Publicar uma alteração do dicionário".
   - Se o resultado for "Recusado", feche a issue. O processo termina neste passo.

#### Publicar uma alteração do dicionário

- **Responsável:** mantenedor
- **Entrada:** um PMD com o resultado "Aceito" ou "Aceito com outro significado ou outra classe"
- **Gatilho e prazo:** a decisão do PMD. Prazos: seção 7.4.

1. Altere a fonte da palavra:
   - Para o 03, altere a entrada no arquivo `tools/d*.txt`. Para uma alteração ou exclusão, escreva o estado `O` (obsoleta) e a alternativa aprovada (ver 8.1). Vá para o passo 2.
   - Para o 04, altere a tabela do [`04-termos-tecnicos.md`](04-termos-tecnicos.md). Vá para o passo 4.
2. Verifique os arquivos de origem:

   ```shell
   python3 tools/build.py
   ```

   - Se o script mostrar uma linha `PROBLEM`, corrija a entrada e repita este passo.
   - Se o script não mostrar uma linha `PROBLEM`, vá para o passo 3.

   Uma linha `PROBLEM` indica 2 entradas iguais, uma alternativa sem entrada ou uma palavra não aprovada numa entrada aprovada.
3. Gere o 03:

   ```shell
   python3 tools/build.py --render 03-dicionario.md
   ```
4. Gere as regras de palavras do linter (`PalavrasNaoAprovadas.yml` e, se o 03 tiver palavras obsoletas, `PalavrasObsoletas.yml`):

   ```shell
   python3 tools/gerar_regras_dicionario.py
   ```
5. Execute os testes da seção 6.6 e as verificações da seção 6.8. Use `--teste`, `--spec --falhar` e `--lista-branca --spec --meta 1`.
   - Se uma verificação falhar, corrija a entrada ou o teste e volte ao passo 1 (no máximo 3 vezes). Depois, escreva a causa na issue. O processo termina neste passo.
   - Se todas as verificações tiverem sucesso, vá para o passo 6.
6. Confirme os critérios da seção 8.5. Escreva o resultado na entrada do [`CHANGELOG.md`](CHANGELOG.md) e publique a versão no prazo da seção 7.4.

   Registro: a entrada do [`CHANGELOG.md`](CHANGELOG.md), com o ID do PMD e o resultado de cada critério.
7. Escreva a data de publicação e a versão na linha do PMD no registro de decisões.

   Registro: as colunas "Publicação" e "Versão" do registro de decisões.
8. Informe a versão nova às equipes no dia da publicação. Numa versão PATCH, cada equipe altera `PTSBR_REF` (ver 6.7).
9. Verifique a palavra no [`03-dicionario.md`](03-dicionario.md) ou no [`04-termos-tecnicos.md`](04-termos-tecnicos.md) publicado. O processo termina neste passo.

**Uso antes da decisão.** Antes da decisão do PMD, o redator pode usar a palavra como
exceção S2 registrada. Num aviso de segurança ou num passo com ação irreversível, a
palavra é um desvio S1 (ver 4.3), e S1 não tem exceção. Nestas partes do texto, use o pedido
urgente. Não publique o texto com a palavra pendente. Se o mantenedor recusar o
pedido, escreva a frase de novo na próxima alteração do documento.

### 7.4 Prazos

| Etapa | Prazo |
|---|---|
| Triagem, pedido normal | 3 dias úteis depois do pedido |
| Triagem, pedido urgente | 1 dia útil depois do pedido |
| Decisão, pedido normal | 10 dias úteis depois da triagem |
| Decisão, pedido urgente | 2 dias úteis depois do pedido |
| Publicação de uma palavra nova urgente aceita | Versão PATCH em até 5 dias úteis depois da decisão. A próxima versão MINOR registra a palavra nova no [`CHANGELOG.md`](CHANGELOG.md). |
| Publicação de uma palavra nova normal aceita | Na próxima versão MINOR, no máximo 30 dias depois da decisão |
| Publicação de uma alteração ou exclusão aceita | Na próxima versão MINOR, a palavra recebe o estado "Obsoleta" (no máximo 30 dias depois da decisão). A alteração ou a exclusão é obrigatória a partir da próxima versão MAJOR (ver 8.1). |

### 7.5 Critérios de aceite

O mantenedor aceita uma palavra nova apenas se todos os critérios abaixo forem verdadeiros:
1. Nenhuma palavra aprovada tem o mesmo significado sem perda de informação. Uma
   frase nova com 2 vezes o número de palavras também conta como perda.
2. A palavra tem 1 significado e 1 classe gramatical no PTS-BR.
3. O significado não é igual a uma parte do significado de outra palavra aprovada.
4. No mínimo 2 documentos ou 2 equipes precisam da palavra.
5. A palavra é comum no português do Brasil. Um leitor não nativo entende a
   palavra. Uma palavra igual no espanhol ou no inglês também é aceita.
6. A palavra não é um nome técnico. Os nomes técnicos vão para o `04` ou para o
   glossário do projeto.

O mantenedor nunca recusa um PMD com a proposta de alterar um requisito da empresa.
Exemplo: um POP com o prazo "5 dias úteis" não substitui o prazo por "1 semana" para
usar uma palavra aprovada.

Resultados possíveis:
- **Aceito.**
- **Aceito com outro significado ou outra classe.** A decisão escreve o significado ou a classe aprovada.
- **Recusado.** A decisão indica a palavra aprovada ou a frase nova com palavras aprovadas.
- **Encaminhado.** O termo vai para o glossário do projeto.
- **Pendente.** Falta informação. A decisão diz qual informação falta.

### 7.6 Registro de decisões

Mantenha o registro em `decisoes/dicionario.md`, no repositório da especificação.
Escreva 1 linha por pedido. Nunca exclua uma linha. As colunas de data e de prioridade
calculam M7 (ver 5.7).

| ID | Palavra (classe) | Tipo | Prioridade | Pedido | Triagem | Decisão | Resultado | Justificativa | Alternativa | Quem decidiu | Publicação | Versão |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PMD-2026-001 | exemplo (v) | palavra nova | normal | 2026-12-01 | 2026-12-02 | 2026-12-09 | Recusado | Critério 1: "X" aprovado tem o mesmo significado. | X | Mantenedor | — | — |

### 7.7 Pedido de mudança de regra (PMR)

Use o mesmo registro da seção 7.6, com o prefixo PMR. Use este formulário:

```markdown
## Pedido de mudança de regra (PMR)

- Regra (ID de 02-regras.md):
- Problema (uma frase):
- Exemplos reais (no mínimo 2): texto atual e texto com a regra proposta
- Proposta de texto da regra:
- Impacto na versão: MAJOR | MINOR | PATCH (ver 8.1)
- Origem: calibração | auditoria | revisão | outra
- Solicitante e data:
```

| Etapa | Prazo |
|---|---|
| Triagem | 5 dias úteis depois do pedido |
| Decisão | 20 dias úteis depois da triagem |
| Publicação | Na próxima versão do tipo do impacto (ver 8.1) |

O mantenedor aceita um PMR apenas se as 2 condições forem verdadeiras:
1. A regra nova tem no mínimo 2 exemplos reais.
2. O revisor verifica a regra com uma pergunta da lista de verificação.

Uma regra nova também recebe um item na seção 4.2. Se o linter encontrar o padrão
da regra, o PMR também adiciona o arquivo de regra e os 2 arquivos de teste.

---

## 8. Versões da especificação

### 8.1 Versão `MAJOR.MINOR.PATCH` aplicada a uma linguagem controlada

A especificação usa a versão `MAJOR.MINOR.PATCH`. O critério é esta pergunta:
um texto em conformidade com a versão anterior continua em conformidade com a versão nova?

| Tipo | Critério | Exemplos |
|---|---|---|
| MAJOR | Um texto em conformidade com a versão anterior fica fora de conformidade. | Remover uma palavra aprovada. Alterar o significado aprovado de uma palavra. Diminuir um limite de palavras. Fazer uma regra nova obrigatória. Alterar o formato dos avisos. |
| MINOR | Alteração compatível com os textos. Todo texto em conformidade continua em conformidade. | Adicionar uma palavra aprovada. Adicionar um nome técnico. Marcar uma palavra como obsoleta. Adicionar uma regra apenas como recomendação. Adicionar exemplos. Alterar o nível de uma regra do linter para `error` (ver 6.4). |
| PATCH | Alteração sem efeito na conformidade. | Corrigir uma letra incorreta. Melhorar um exemplo. Escrever uma regra com palavras mais simples sem alterar o significado. Corrigir um falso positivo do linter. Adicionar uma palavra com um PMD urgente aceito (ver 7.4). |

Uma palavra nova de um PMD urgente é compatível com os textos, como uma versão MINOR.
A versão PATCH publica esta palavra antes da próxima versão MINOR.

**Palavras obsoletas.** Antes de remover uma palavra, marque a palavra como obsoleta
numa versão MINOR. Em `tools/d*.txt`, escreva o estado `O`, a alternativa aprovada e a versão
da exclusão. O `build.py` publica a palavra no 03 com o estado "Obsoleta" e a coluna
"Use: SUBSTITUTA". O `gerar_regras_dicionario.py` gera a regra `PalavrasObsoletas.yml` com o
nível `suggestion`. A palavra obsoleta continua válida na lista branca. A próxima versão
MAJOR remove a palavra.

**Frequência.**
- PATCH: quando necessário.
- MINOR: no máximo 1 por mês.
- MAJOR: no máximo 1 por ano. Junte as alterações incompatíveis com os textos numa versão.

### 8.2 Changelog

Mantenha o [`CHANGELOG.md`](CHANGELOG.md) na pasta principal da especificação. Use estas seções em
cada versão: Adicionado, Alterado, Obsoleto, Removido, Corrigido. Cada linha mostra a
seção ou a regra afetada e o ID do pedido.

```markdown
## [1.1.0] - AAAA-MM-DD
### Adicionado
- Dicionário: <PALAVRA> (v), significado "<significado>". PMD-2026-014.
### Alterado (linter)
- PTSBR.Haver: nível error. M6 = 2% em 120 alertas.
### Obsoleto
- Dicionário: <palavra> (s). Use <PALAVRA APROVADA>. Exclusão na versão 2.0.0. PMD-2026-019.
### Corrigido
- R4.2: exemplo de frase descritiva com o número de palavras incorreto. PMR-2026-003.
```

### 8.3 Período de transição

| Tipo | Transição |
|---|---|
| PATCH | Nenhuma. A versão é obrigatória a partir da publicação. |
| MINOR | Nenhuma. A alteração é compatível com os textos. |
| MAJOR | 6 meses. O revisor aceita a versão anterior e a versão nova. O linter mostra as regras novas como `warning`. No fim do período, o mantenedor aplica a seção 6.4 às regras novas, numa versão MINOR. |

Durante a transição de uma versão MAJOR:
1. Escreva os documentos novos na versão nova.
2. Atualize um documento publicado para a versão nova quando você alterar o documento.
3. Atualize os avisos de segurança afetados dentro do período de transição.
4. O mantenedor publica um guia de migração com a lista de alterações e exemplos
   antes e depois.
5. A equipe usa no CI a versão nova (`PTSBR_REF`, ver 6.7). As regras novas têm o nível
   `warning` e não bloqueiam os documentos da versão anterior.

### 8.4 Versão declarada no documento

Cada documento PTS-BR declara a versão `MAJOR.MINOR` no cabeçalho. A versão PATCH
não aparece no documento. O revisor usa a última PATCH da versão declarada: uma PATCH
publica uma palavra de um PMD urgente aceito (ver 7.4).

```yaml
---
pts-br: "1.0"
---
```

O revisor verifica o documento com as regras da versão declarada (item CK-0.1). Um
documento sem a versão declarada tem o resultado "Reprovado" (ver 4.4).

### 8.5 Critérios para publicar uma versão

O mantenedor publica uma versão apenas se todos os critérios abaixo forem verdadeiros.
O mantenedor escreve o resultado de cada critério na entrada da versão no [`CHANGELOG.md`](CHANGELOG.md).
1. O `python3 tools/build.py` não mostra nenhuma linha `PROBLEM`.
2. O [`03-dicionario.md`](03-dicionario.md) foi gerado com `tools/build.py --render` a partir dos arquivos de
   origem do mesmo commit.
3. O `python3 tools/gerar_regras_dicionario.py --verificar` termina sem erro.
4. O `python3 tools/check_spec.py --teste` termina sem erro com o linter em Python, o motor do linter
   de referência (ver 6.1). O teste com o Vale é um critério de entrada do Piloto (ver 3.2).
5. Palavras não aprovadas do 03 e do 04 ([`01-introducao.md`](01-introducao.md), [seção 11.1](01-introducao.md#111-autoconformidade)): o comando
   `python3 tools/check_spec.py --spec --falhar` termina sem erro.
6. Lista branca: o comando
   `python3 tools/check_spec.py --lista-branca --spec --meta 1` termina sem erro. O
   mantenedor confirma cada palavra fora da lista. Para cada palavra, o mantenedor
   registra a decisão: entrada nova, termo do glossário ou frase nova. A lista branca
   verifica a forma, não o significado: o significado é um item do revisor (CK-1.2).
7. Cada regra nova tem um item na lista de verificação (seção 4.2).
8. O [`CHANGELOG.md`](CHANGELOG.md) tem a entrada da versão, com as seções da seção 8.2.
9. O mantenedor cria a tag `vMAJOR.MINOR.PATCH` no commit da publicação. Os números do
   [`CHANGELOG.md`](CHANGELOG.md) são os números deste commit. A tag `v1.0.0` é criada na publicação da
   versão 1.0.0.

---

## 9. Treinamento

Os documentos de treinamento estão na pasta `treinamento/` do repositório da especificação.
O mantenedor publica estes documentos antes do Piloto (ver 3.2).

### 9.1 Trilha do redator

Duração total: 6 h 15 min. Formato: com as pessoas no mesmo local ou numa reunião remota, em grupos de até 12 pessoas.

| Módulo | Conteúdo | Documentos | Duração |
|---|---|---|---|
| 1. Por que usar uma linguagem controlada | Leitor-alvo, princípios, escopo | [`01-introducao.md`](01-introducao.md) | 30 min |
| 2. Palavras e dicionário | 1 palavra, 1 significado. Uso do dicionário. Nomes técnicos. | Seção 1, `03`, `04` | 60 min |
| 3. Verbos e frases | Voz ativa, tempos aprovados, cadeias nominais, limite de palavras | Seções 2, 3 e 4 | 60 min |
| 4. Procedimentos e avisos | Imperativo, 1 passo por ação, responsáveis e decisões de POP, palavras de sinalização | Seções 5 e 7 | 60 min |
| 5. Descritivo, formatação e interface | Parágrafos, formatação, mensagens de erro | Seções 6, 8, 9 e 10 | 45 min |
| 6. Ferramentas e fluxo | Linter no computador, fluxo do pull request ou fluxo fora do Git, PMD | Este documento | 30 min |
| 7. Prática | Textos reais da equipe escritos de novo em PTS-BR | Textos da equipe, [`06-exemplos.md`](06-exemplos.md) | 90 min |

**Prática.** Escreva de novo em PTS-BR:
1. Um runbook ou um POP real da equipe, com 300 a 400 palavras.
2. 2 mensagens de erro reais.
3. Um aviso de segurança.

**Avaliação.**
- Teste com 20 itens: a pessoa em treinamento identifica o desvio e o ID da regra.
  Nota mínima: 80%. O mantenedor escreve o teste e o gabarito do teste.
- O revisor avalia a prática com a lista de verificação. Critério: nenhum
  S1 e no máximo 3 S2 por 1 000 palavras.
- Uma pessoa com o resultado menor que o critério faz a prática de novo. A pessoa não
  repete os módulos.

**Resumo.** Um resumo de 1 página com as regras mais usadas e
os limites de palavras.

### 9.2 Treinamento depois de uma versão

- A cada versão MAJOR: sessão de 60 min sobre as alterações.
- A cada versão MINOR: nota de 1 página para os redatores.

### 9.3 Trilha do revisor

Antes da trilha do revisor: trilha do redator e 5 documentos aprovados como redator. A seção 9.4
define a exceção para o início do Piloto.

| Módulo | Conteúdo | Duração |
|---|---|---|
| RV1. Lista de verificação e severidade | Seções 4.2 a 4.5 deste documento. Regra para aumentar a severidade. Exceções. | 60 min |
| RV2. Revisão com um revisor | Revisão de 2 documentos com um revisor com a trilha do revisor | 60 min |
| RV3. Calibração | Revisão de 3 documentos sem ajuda. O revisor compara os resultados com o gabarito. | 60 min |

**Avaliação.** No módulo RV3, a pessoa em treinamento classifica no mínimo 80% dos
desvios como no gabarito. A pessoa encontra todos os desvios S1 do gabarito.

**Calibração a cada mês.** Na fase Expansão, faça 1 sessão a cada mês. 2 ou mais
revisores revisam o mesmo documento sem comparar as decisões antes. O mantenedor
compara os resultados e explica as diferenças. Se a causa de uma diferença for uma regra com 2
significados, crie um PMR (ver 7.7).

### 9.4 Exceção para o início: revisores fundadores

Antes do Piloto, ninguém tem documentos PTS-BR aprovados. Portanto, a trilha do
revisor tem esta exceção:
1. Antes do Piloto, o mantenedor escreve o gabarito do RV3 com 3 exemplos do
   [`06-exemplos.md`](06-exemplos.md). O aprovador registra o gabarito em `treinamento/`.
2. O mantenedor faz o módulo RV2 com o aprovador. O mantenedor revisa
   2 textos "Antes" do 06 e compara o resultado com a tabela "Alterações" do exemplo.
3. Antes do Piloto, o mantenedor e até 3 revisores fundadores fazem a trilha do revisor.
   Os revisores fundadores não precisam dos 5 documentos aprovados. O mantenedor
   faz o módulo RV2 com cada revisor fundador.
4. No mínimo 1 revisor fundador é de outra equipe e não revisa os documentos do Piloto.
   Este revisor fundador é o auditor do Piloto.
5. Durante o Piloto, o mantenedor revisa de novo os 5 primeiros documentos de cada
   revisor fundador. O mantenedor registra as diferenças como treinamento.
6. Um revisor fundador com uma diferença S1 nestes 5 documentos faz o módulo RV3 de novo.

O aprovador registra o nome dos revisores fundadores, o nome do auditor do Piloto e a
data do treinamento.

### 9.5 Primeiro revisor de uma equipe nova na Expansão

Uma equipe nova na Expansão não tem documentos PTS-BR aprovados. Portanto, o primeiro
revisor da equipe faz a trilha do revisor com estas regras:
1. O aprovador da equipe escolhe 1 pessoa para a trilha do revisor. A pessoa faz a trilha do redator.
2. A pessoa faz a trilha do revisor sem os 5 documentos aprovados como redator.
3. O aprovador escolhe o revisor responsável pela pessoa. O revisor responsável tem a
   trilha do revisor e 10 revisões no Piloto ou na Expansão.
4. O revisor responsável faz o módulo RV2 com a pessoa.
5. O revisor responsável revisa de novo as 5 primeiras revisões da pessoa. O revisor
   responsável registra as diferenças como treinamento.
6. Uma pessoa com uma diferença S1 nestas 5 revisões faz o módulo RV3 de novo.
7. Depois das 5 revisões, a pessoa é revisor da equipe. O aprovador registra o nome da
   pessoa, o nome do revisor responsável e a data.

O segundo revisor de uma equipe segue a seção 9.3.

### 9.6 Trilha do aprovador e do auditor

- Aprovador: uma sessão de 30 min sobre o critério de aprovação, as exceções, as
  métricas e a decisão de fase.
- Auditor: a trilha do revisor e uma sessão de 30 min sobre as seções 3.4 e 3.5.

---

## 10. Riscos da adoção e ações

| Risco | Sinal de alerta | Ação |
|---|---|---|
| Os redatores dizem que o texto é "infantil" e recusam o padrão. | Questionário do Anexo B com média baixa. Um número alto de exceções. | Mostre o resultado do teste de compreensão do Piloto. Explique o leitor-alvo. Comece pelos documentos de risco alto: nestes documentos, o resultado é visível. |
| A revisão demora e bloqueia as equipes. | M5 maior que a meta. Pull requests sem resposta. | Faça a trilha do revisor com 1 pessoa por equipe. Ajuste o escopo da fase. |
| O linter tem um número alto de falsos positivos, e os redatores não leem os alertas. | M6 alto. Um número alto de comentários que desligam uma regra. | Teste cada regra antes do nível `error`. Corrija ou desligue as regras com M6 maior que a meta. |
| O dicionário não tem uma palavra necessária e bloqueia a escrita. | Um número alto de PMD sem decisão. Prazos não cumpridos. | Uso antes da decisão, com exceção registrada. Pedido urgente para avisos e passos que o leitor não desfaz. Substituto do mantenedor. |
| A especificação e o linter são diferentes. | Alertas diferentes do [`02-regras.md`](02-regras.md). | Gere a regra de palavras a partir do dicionário. Escreva o ID da regra em cada regra do linter. Execute os testes no CI (ver 6.6). |
| A equipe escreve para melhorar as métricas, não para o leitor. Exemplo: frases curtas, mas com 2 significados. | M1 alto e resultado baixo no teste de compreensão. Leitores informam problemas no texto. | Nunca use M4 como critério. Use as métricas com a auditoria e o teste de compreensão. |
| As equipes usam termos em inglês diferentes. | O mesmo conceito com nomes diferentes. | Siga o [`04-termos-tecnicos.md`](04-termos-tecnicos.md). Cada dono do glossário revisa os glossários dos outros projetos a cada 3 meses. |
| O mantenedor é a única pessoa com a informação. | O mantenedor não está disponível e os PMD param. | Escolha um substituto do mantenedor. Registre todas as decisões (ver 7.6). |
| O número de documentos legados é alto, e a equipe não converte os documentos. | Pedidos para alterar a data da fase Padrão. | Converta por risco e na alteração (ver 3.4). Não peça a conversão de todos os documentos. |
| O PTS-BR é diferente do guia de escrita de interface da empresa. | Os revisores de interface e de PTS-BR pedem alterações diferentes no mesmo texto. | Adicione o dono do glossário e a equipe de interface à fase Expansão. Registre as decisões como PMR. |
| As equipes declaram o PTS-BR, mas não aplicam as regras. | Documentos sem a versão declarada. Revisões sem registro de desvios. | Faça a auditoria da seção 3.4. Publique as métricas de cada equipe. |
| Os POP estão fora do Git e sem registro de revisão. | Documentos de processo sem a tabela do Anexo C. | Use o procedimento da seção 4.5. A amostra da auditoria também tem documentos fora do Git. |

---

## 11. Anexo A — Protocolo do teste de compreensão

**Objetivo.** Comparar o resultado dos leitores com um documento original e com a versão PTS-BR
do mesmo documento.

**Responsável.** O mantenedor faz o teste. O aprovador responde pelo resultado (ver 2.2).

**Documentos.** 2 runbooks ou procedimentos com 8 a 15 passos. Cada documento tem a
versão original e a versão PTS-BR. Um ambiente de teste com o sistema do documento.

**Leitores.** No mínimo 5 leitores do público-alvo do documento. Escolha no mínimo 1
leitor não nativo de português ou 1 leitor de outra área, se a equipe tiver estes leitores.
Os leitores não escreveram nem revisaram os documentos.

**Procedimento**
1. Divida os leitores em 2 grupos. O grupo 1 usa o original do documento A e a
   versão PTS-BR do documento B. O grupo 2 usa a versão PTS-BR do documento A e o
   original do documento B.
2. Atribua a tarefa a cada leitor: seguir o procedimento no ambiente de teste, sem ajuda.
3. Para cada leitor e documento, registre:
   - Os passos sem erro.
   - O tempo total, em minutos.
   - As dúvidas que o leitor informou.
4. Calcule para cada versão: a porcentagem média de passos sem erro e a mediana do tempo.

   Registro: os dados de cada leitor e o resultado, em `auditorias/teste-compreensao-AAAA-MM.md`.

**Critério.** Verifique 2 condições:
1. A porcentagem média de passos sem erro da versão PTS-BR é igual ou maior que a do original.
2. A mediana do tempo da versão PTS-BR é no máximo 10% maior que a do original.

| Condições verdadeiras | Resultado | Decisão |
|---|---|---|
| 2 | **Melhor ou igual** | O critério de saída do Piloto está cumprido. |
| 1 | **Inconclusivo** | O aprovador registra a decisão de continuar ou de repetir o Piloto. Se o Piloto continuar, faça um teste novo na Expansão (ver 3.3). |
| 0 | **Pior** | Repita o Piloto. O mantenedor analisa as diferenças e publica uma versão PATCH ou MINOR antes do Piloto novo. |

Com 5 a 9 leitores, o resultado **Melhor ou igual** cumpre o critério de saída do Piloto,
e o resultado **Pior** passa a **Inconclusivo**. Com 5 leitores, os grupos têm 2 e 3
leitores, e uma diferença de 1 passo altera o resultado. Na Expansão, repita o teste com
no mínimo 10 leitores. Escreva o número de leitores no registro.

---

## 12. Anexo B — Questionário dos redatores

**Quando aplicar.** No fim do Piloto e no fim de cada período de 3 meses da Expansão.

**Responsável.** O mantenedor envia o questionário e calcula o resultado. O aprovador
responde pelo resultado (ver 2.2).

**Escala.** De 1 a 5. 1 = a frase não é verdadeira para você. 5 = a frase é
verdadeira para você.

| Pergunta | Frase |
|---|---|
| Q1 | Você encontra a palavra aprovada necessária em menos de 2 min. |
| Q2 | Você entende as regras de [`02-regras.md`](02-regras.md) sem ajuda. |
| Q3 | O tempo da revisão PTS-BR é correto para o seu trabalho. |
| Q4 | Os alertas do linter mostram a você como corrigir o texto. |
| Q5 | Você usa o PTS-BR no seu trabalho de todos os dias sem problemas. |

**Critério.** Um redator aprova o processo se a média das 5 respostas for
4 ou mais. O critério de saída da Expansão (ver 3.3) usa a porcentagem de redatores
com média 4 ou mais. Registre as respostas sem o nome do redator.

---

## 13. Anexo C — Tabela de revisão para documentos fora do Git

Copie esta tabela para um anexo da página ou para um arquivo ligado ao documento.
Os campos são iguais aos campos do comentário de resultado da seção 4.1, também as linhas `[METRICAS]` e `[LINTER]`.

**Dados da revisão**

| Campo | Valor |
|---|---|
| Documento e link da versão revisada | |
| Versão do PTS-BR declarada | |
| Redator | |
| Revisor | |
| Data do pedido de revisão | |
| Data do resultado | |
| Palavras (`check_spec.py --metricas`) | |
| M1 na submissão (`M1-sub`) | |
| M2 na submissão (`M2-sub`): palavras confirmadas por 1 000 palavras | |
| M1 na publicação (`M1-pub`) | |
| M2 na publicação (`M2-pub`) | |
| Exceções pedidas e decisão do aprovador | |
| Tempo de revisão (min) | |
| Resultado (ver 4.4) | Aprovado / Aprovado com exceções / Reprovado |
| Aprovador e data da aprovação | |

**Alertas do linter por regra**

| Regra | Alertas | Falsos positivos |
|---|---|---|
| `PTSBR.FraseLonga` | 4 | 1 |
| | | |

**Desvios**

| Número | Parte do texto ou passo | Severidade | Regra | Estado | Justificativa da exceção |
|---|---|---|---|---|---|
| 1 | Passo 3 | S2 | [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale) | CORRIGIDO | — |
| 2 | | | | | |

---

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · **05 Governança** · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

<!-- rodape -->
Feito com ❤️ em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Nenhum direito reservado.

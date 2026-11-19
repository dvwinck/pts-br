---
lente: processos
rodada: 4
notas: {correcao: 8, completude: 7.5, aplicabilidade: 8, coerencia: 8.5, valor: 8.5}
nota_final: 8.1
---

Lente: BPM, qualidade (ISO 9001), governança de documentação, POP, fluxos de aprovação,
auditoria e gestão de mudanças.

Verificações feitas nesta rodada (nenhuma edita a especificação, nenhuma executa o Vale):
- `python3 build.py`: nenhuma linha `PROBLEM`; "approved 723 not approved 362 obsolete 0".
  `build.py --teste`: os testes do estado `O` (obsoleta) passam (3 casos, linha renderizada
  "| SETAR (v) | Obsoleta | Use: DEFINIR (v) — exclusão na versão 2.0.0. |").
- `gerar_regras_dicionario.py --verificar`: OK, 421 entradas, 0 palavras obsoletas.
- `check_spec.py --teste`: 160 testes de regra corretos (soma conferida por regra: 7+6+6+7+6+6+19+8+7+52+6+7+13+10),
  "Antes" 122 alertas, "PTS-BR" 0, lista branca 24/24, opções de equipe 13/13. Confere com o CHANGELOG.
- `check_spec.py --spec`: 0 alertas. `--lista-branca --spec`: 62 de 74 430 palavras (0,08%),
  05 com 0,03%. Confere com o critério 6 do CHANGELOG (a divergência 66 327 × 66 329 da rodada 3 acabou).
- `--metricas` num arquivo de teste: "irá", "deverá", "enviava" saem como "tempo verbal (CK-3.1,
  fora de M2)"; "Há" e "realizar" entram em M2 1 vez cada ocorrência. A linha impressa é
  `[METRICAS][palavras: 51][M1: 85,7][M2-candidatas: 4]`.
- `tools/ci/docs-lint-equipe.yml` l. 143-153: o passo "Métricas M1 e M2" executa `--metricas` e
  grava a saída em `$GITHUB_STEP_SUMMARY`. O código 2 do Vale falha o job em todas as fases (l. 113).
- Busca por "merge", "proteção", "required", "CODEOWNERS", "retenção" e "commit" no 05 e nos
  pipelines (ver problemas 1 e 3).

## Status dos problemas da rodada 3

Resumo: **12 resolvidos, 2 parciais, 0 abertos** (de 14). Nenhuma correção criou contradição
grave; as lacunas que sobram estão fora dos 14 itens (problemas novos abaixo).

| # R3 | Problema | Status | Evidência no texto atual |
|---|---|---|---|
| 1 | "Aprovado com exceções" sem caminho (impasse) | RESOLVIDO | 05 l. 379 "escreva a justificativa, o estado `EXCECAO-PEDIDA` e o usuário do aprovador"; l. 382-385 passo 6 aguarda a decisão com saída de prazo; procedimento "Decidir uma exceção S2" l. 400-414; estado no formato l. 483; §4.4 l. 671-673 trata `EXCECAO-PEDIDA` em "Aprovado" e "Reprovado". |
| 2 | POP violam R5.11 (laços, esperas, "Pendente", destino, escalonamento) | RESOLVIDO (resíduo menor) | (a) l. 390 "volte ao passo 2. Depois do 3º resultado "Reprovado", envie o pull request ao mantenedor"; (b) l. 385, 391, 398 com "sem resposta"/"não decidir em 2 dias úteis"; (c) l. 1424 "aguarde 10 dias úteis ... Sem resposta no prazo, o resultado é "Recusado""; (d) 02 R5.11 l. 879 tem o destino "Este procedimento termina neste passo"; (e) "Decidir um conflito de revisão" l. 453-471, prazo de 5 dias úteis. Resíduo: o próprio mantenedor não tem saída "sem resposta" (problema novo 5). |
| 3 | Etapas sem procedimento (redator, §4.5, verificação, "Sem prazo") | RESOLVIDO | (a) "Corrigir os desvios da revisão" l. 416-433; (b) §4.5 com 3 procedimentos (l. 711-791), pedido de exceção (l. 757) e `--metricas` (l. 749); (c) "Pedir a revisão" passo 7 l. 359 "Verifique que o pull request mostra o revisor"; "Prazo: nenhum." aceito por 02 R5.10 l. 842. |
| 4 | M1/M2 sem registro durável; contagem dupla; M3 trivial | RESOLVIDO | Linha `[METRICAS][M1-sub ...][M2-sub ...][M1-pub ...][M2-pub ...]` l. 491; CI com `--metricas` (yml l. 143-153); §5.4 l. 851-853 "Uma palavra que as 2 listas mostram na mesma linha conta 1 vez" e tempo verbal fora de M2 (conferido na ferramenta); §5.9 l. 943-946 tira M3 na publicação do critério "por documento". |
| 5 | Manutenção do dicionário só cobre inclusão | RESOLVIDO | Estado `O` em `build.py` l. 50-51 e `--teste`; `gerar_regras_dicionario.py` gera `PalavrasObsoletas.yml` (l. 18-20, 38); "Publicar uma alteração" passo 1 l. 1439-1440 separa 03 e 04; passo 5 l. 1461 com `--spec --falhar` e `--meta 1`; passo 6 l. 1464 "Confirme os critérios da seção 8.5". |
| 6 | Impasse do revisor de equipe nova na Expansão | RESOLVIDO | §9.5 l. 1738-1753 (trilha sem os 5 documentos, revisor responsável com 10 revisões, revisão das 5 primeiras revisões); §3.3 l. 259 cita a regra. |
| 7 | Teste de compreensão com 5 a 9 leitores | RESOLVIDO | Anexo A l. 1819-1822 "Com 5 a 9 leitores, o resultado **Melhor ou igual** cumpre o critério ... **Pior** passa a **Inconclusivo** ... Na Expansão, repita o teste com no mínimo 10 leitores." |
| 8 | `error` no fim da transição MAJOR × gate de M6 | RESOLVIDO | §8.3 l. 1608 "o mantenedor aplica a seção 6.4 às regras novas, numa versão MINOR"; §6.4 l. 1055 "O nível `error` não altera a conformidade de um texto". |
| 9 | PATCH urgente não chega ao revisor nem ao CI | PARCIAL | Resolvido para a PATCH: §8.4 l. 1622 "O revisor usa a última PATCH da versão declarada"; §6.7 l. 1229 e l. 1251-1252; triagem urgente 1 dia útil l. 1484. Falta a mesma regra para a MINOR (problema novo 9). |
| 10 | Amostra mensal maior que o número de documentos | RESOLVIDO | §3.4 l. 300 "Se o mês tiver menos de 10 documentos publicados, todos ... Um documento auditado não volta à amostra sem uma alteração." |
| 11 | Agregação de M5 indefinida | PARCIAL | Duração resolvida: §5.7 l. 906-907 "mediana", §5.9 l. 939, prazo do revisor 3/2 dias úteis l. 367. "M5 — Tempo de revisão | Total da fase" (l. 938) continua sem a fórmula de agregação (problema novo 7). |
| 12 | Exemplo 7: ordem do controle, verificação final, entrega da senha | RESOLVIDO | 06 l. 1063-1065 verifica a MFA no passo 6, antes do passo 7 que compartilha a senha; l. 1078-1080 passo 10 verifica **Resolvido**; l. 1013-1018 o gestor mostra a senha no primeiro dia, com saída de erro. A tabela "Alterações" l. 1108 e l. 1111 explica as 2 correções. |
| 13 | Separação de funções e papéis sem definição | RESOLVIDO | 05 l. 146-147 regra 4; README "Licença" "Esta é a licença decidida para a versão 1.0.0."; 01 l. 358 "O revisor pede a exceção ao aprovador"; "revisões parciais" não existe mais no 01. |
| 14 | Registro de publicação não confere; tag inexistente | RESOLVIDO | CHANGELOG critério 6 "62 de 74 430" = medição atual; CHANGELOG "A tag `v1.0.0` ainda não existe: o mantenedor cria a tag no commit da publicação"; §3.2 l. 219 e §8.5 critério 9 l. 1653-1655. O texto não afirma mais um fato falso. |

## Pontos fortes (até 5)

1. **Fluxo de revisão fechado como um BPMN.** A tabela de l. 334-341 liga cada um dos 6
   procedimentos ao procedimento que recebe a saída, e os números de passo citados (passos 6, 8
   e 10 de "Revisar"; 6, 7 e 9 fora do Git, l. 709) conferem com o texto. Cada espera tem prazo e
   saída de prazo; cada laço tem limite e destino. A exceção S2 tem um estado próprio
   (`EXCECAO-PEDIDA`), um dono e um prazo, e §4.4 trata o estado nos 3 resultados.
2. **Registros auditáveis e métricas recalculáveis.** A linha `[METRICAS]` (l. 491) e a linha
   `[LINTER]` (l. 492) dão ao auditor os campos de M1, M2, M5 e M6 por documento, com a regra
   explícita de que o log do CI não é registro (l. 505-507). §5.4 elimina a contagem dupla de M2
   e a ferramenta faz o mesmo (conferido). §5.9 l. 943-946 explica por que M3 na publicação saiu do
   critério de fase: o critério mede agora o que varia.
3. **Controles de independência e melhoria contínua.** Regra 4 de §2.1 (aprovador ≠ redator),
   2 aprovadores, substituto do mantenedor, auditor de outra equipe, auditoria anual do mantenedor
   (§3.5), eficácia da ação corretiva (l. 307), qualificação controlada do primeiro revisor de cada
   equipe (§9.5). O desenho segue ISO 9001 §5.3, §9.2 e §10.2 sem copiar o texto da norma.
4. **Gestão da mudança do vocabulário com ferramenta.** Estado `O` real nas fontes, no build e
   no linter (`suggestion`), PATCH para o PMD urgente com caminho até o `PTSBR_REF` das equipes,
   e os 9 critérios de §8.5 no procedimento de publicação. O pacote cumpre o que promete: "Este
   documento descreve apenas as ferramentas que existem" (l. 18) é verdade nesta rodada.
5. **Honestidade de medição.** O CHANGELOG, o README e §6.1/§6.6 dizem que as regras atuais não
   têm resultado com o Vale e que a tag não existe, e põem os 2 itens como critério de entrada do
   Piloto. A lista branca diz que verifica a forma, não o sentido. Todos os números que conferi
   estão corretos.

## Problemas (ordenados por impacto)

1. **[IMPORTANTE] 05:§4.1, §6.7 — no Git, a publicação não tem ponto de controle: ninguém faz o
   merge, a aprovação não fica ligada ao commit e o bloqueio do CI não é exigido.**
   (a) "Aprovar a publicação" termina em "O estado é **Approved**. O processo termina neste passo."
   (l. 448), e "Revisar" passo 10 também termina o processo (l. 396). Nenhum passo, papel ou linha
   da RACI faz o merge, que é o evento real de publicação do documento. (b) Nem o formato de
   resultado (l. 490-492) nem a aprovação registram o commit revisado. O redator pode enviar um
   commit depois da aprovação, e o texto publicado fica diferente do texto aprovado (ISO 9001
   §7.5.2 e §8.5.6). Fora do Git, o Anexo C tem "link da versão revisada" (l. 1859); no Git, não há
   equivalente. (c) §6.4 e §6.7 dizem "Bloqueia o merge a partir da fase Expansão" (l. 1050, 1256-1257),
   mas o 05 e os pipelines não pedem a proteção do branch (busca por "proteção", "required",
   "CODEOWNERS": 0 ocorrências). Sem a verificação obrigatória e sem o aprovador obrigatório, um job
   com falha não bloqueia nada, e qualquer pessoa com acesso de escrita faz o merge sem o aprovador.
   (d) O passo 9 de "Revisar" diz "O aprovador recebe o pull request" (l. 394), mas não tem a ação
   que notifica o aprovador nem a escolha de um aprovador que não é o redator (regra 4).
   **Correção:** em "Antes de começar" do Piloto (§3.2, critério novo): "O branch principal do
   repositório da equipe exige: o job `docs-lint` com sucesso, 1 aprovação do grupo de aprovadores
   (`CODEOWNERS`) e a opção **Dismiss stale pull request approvals when new commits are pushed**.
   Instrumento: captura da regra de proteção." Em "Revisar", passo 9: "Escreva no campo `commit`
   do resultado o hash do último commit revisado. Adicione ao campo **Reviewers** um aprovador que
   não é o redator." Em "Aprovar", passo 4: "Verifique que o último commit do pull request é o
   commit do resultado. Faça o merge. Registro: o merge, no histórico do pull request." Linha nova
   na RACI: "Publicar o documento (merge)" — Aprovador R/A.

2. **[IMPORTANTE] 05:§7.3, §7.7, §8 — a publicação de uma versão da especificação não tem
   procedimento; o procedimento atual publica 1 versão por PMD.** "Publicar uma alteração do
   dicionário" tem a entrada "um PMD" (l. 1435) e o passo 6 "publique a versão no prazo da seção 7.4"
   (l. 1464). Um PMD normal espera "a próxima versão MINOR" (l. 1488), e a MINOR tem "no máximo 1 por
   mês" (l. 1581). Com 5 PMD no mês, o procedimento manda publicar 5 versões ou não diz como juntar
   os pedidos. O PMR (l. 1541-1552) só tem uma tabela de prazos, sem procedimento de publicação. A
   versão MAJOR tem "Aprova as versões MAJOR" (l. 127) e A do aprovador na RACI (l. 172), mas nenhum
   passo, registro ou critério de §8.5 tem a aprovação; o guia de migração (l. 1614) e a sessão de 60 min
   (§9.2) não têm prazo nem dono num procedimento. **Correção:** dividir em 2 procedimentos.
   "Preparar uma alteração" (por PMD ou PMR: passos 1-5 atuais; saída: "a alteração está no branch
   `proxima-versao`; o PMD fica com o estado `Aceito, não publicado`"). "Publicar uma versão"
   (mantenedor; gatilho: PMD urgente aceito (PATCH), 1 vez por mês com alterações (MINOR), ou
   decisão MAJOR; passos: juntar as alterações, critérios de §8.5, para MAJOR "Peça a aprovação ao
   aprovador. Registro: a aprovação, na issue da versão" e "Publique o guia de migração", criar a
   tag, informar as equipes, atualizar as colunas "Publicação" e "Versão" de cada PMD/PMR da versão).
   Critério 10 novo em §8.5: "Versão MAJOR: a aprovação do aprovador está registrada."

3. **[IMPORTANTE] 05:§4.1, §3.5, §5.2 — o registro de revisão no Git não tem regra de retenção,
   de proteção nem de coleta.** O comentário de resultado é "o registro permanente de M1, M2, M3, M5 e
   M6" (l. 505), mas a regra de retenção existe apenas fora do Git (l. 793 "Mantenha a tabela de
   revisão enquanto o documento existir e mais 1 ano"). Um comentário do pull request é editável e
   pode ser excluído pelo autor, e se perde numa migração do repositório (ISO 9001 §7.5.3.2: proteção
   contra alteração e retenção). A coleta também não tem instrumento: "Nesta versão, a pasta `tools/`
   não tem um script para este cálculo" (l. 507). O critério "80% dos documentos" (l. 242, 275) e o
   recálculo do auditor (l. 319) dependem de ler à mão os comentários de 3 a 5 repositórios. **Correção:**
   "O revisor copia as 3 linhas do resultado para `revisoes/AAAA-MM.md` do repositório da equipe, no
   mesmo pull request. Registro: a linha do documento, no arquivo do mês." (o arquivo fica no
   histórico do Git, com a mesma retenção de l. 793); ou um script `coletar_resultados.py` que lê os
   comentários pela API e grava o arquivo do mês. Em §4.1: "Não altere um comentário de resultado;
   escreva um comentário novo com a correção."

4. **[MENOR] 05:§4.5 — o revisor não encontra a aprovação quando a ferramenta tem o recurso de
   aprovação.** "Aprovar fora do Git", passo 3: "Aprove a versão com o recurso de aprovação da
   ferramenta. Se a ferramenta não tiver este recurso, escreva o seu nome e a data na tabela" (l. 786).
   O revisor, passo 9, termina o processo apenas "Se a tabela do Anexo C mostrar o nome do aprovador e
   a data da aprovação" (l. 772). Com o recurso da ferramenta, a tabela fica vazia, e o revisor segue
   a saída de prazo e envia a página ao mantenedor (l. 774). O passo 4 do aprovador também afirma "A
   tabela mostra o resultado e a aprovação" (l. 791), contra o passo 3. **Correção:** passo 3: "Aprove
   a versão com o recurso da ferramenta, se existir. Escreva também o seu nome e a data na tabela do
   Anexo C."

5. **[MENOR] 05:§4.1 — 4 defeitos de POP no próprio fluxo (CK-5.4, CK-5.7, CK-5.9).**
   (a) "Decidir um conflito de revisão" termina no passo 4 "Envie o pull request ao responsável"
   (l. 468) sem verificação (CK-5.7, S2) e sem a ação concreta (comentário com o usuário). O
   mantenedor tem prazo de 5 dias úteis (l. 457), mas nenhum procedimento tem a saída "sem resposta"
   para este prazo, e nenhum passo chama o substituto. (b) "Decidir uma exceção", passo 2: "responda
   ... com `[EXCECAO @<seu-usuário>]`. Um desvio num aviso de segurança não tem exceção." (l. 408): a
   condição está depois da ação (CK-5.4). (c) "Revisar", passo 6: a exceção sem decisão no prazo
   passa a `ABERTO` e reprova o documento (l. 385), mas a aprovação sem decisão no prazo vai ao
   mantenedor (l. 398), que "escolhe outro aprovador" (l. 464). O redator recebe um "Reprovado" que
   não pode corrigir. (d) Passo 8: o limite "Depois do 3º resultado "Reprovado"" está dentro do item
   "Se o redator pedir a revisão de novo" (l. 390); o texto não diz se o contador volta a zero depois
   da decisão do mantenedor. **Correção:** (a) passo 5 novo: "Verifique que o comentário tem o
   usuário do responsável. Se o mantenedor não decidir em 5 dias úteis, o revisor envie o pedido ao
   substituto do mantenedor."; (b) "Se o pedido cumprir a seção 4.3 e o limite, e o desvio não estiver
   num aviso de segurança, responda ..."; (c) passo 6, terceira saída: "envie o pull request ao
   mantenedor. Este procedimento termina neste passo. O mantenedor recebe o pull request no
   procedimento "Decidir um conflito de revisão"."; (d) item próprio antes da espera: "Se este for o
   3º resultado "Reprovado" deste pull request desde a última decisão do mantenedor, envie ...".

6. **[MENOR] 05:§1, §5.2, §4.1 — "submissão" tem 2 definições, e a linha `[METRICAS]` tem 2
   formatos.** §1: "O primeiro envio do documento para a revisão" (l. 49), isto é, o passo 6 de
   "Pedir a revisão". §5.2: "a primeira execução do CI no pull request" (l. 829), que acontece no
   passo 4, antes das correções do passo 5 e de qualquer rascunho (pull request "draft"). O CI grava
   `[METRICAS][palavras: N][M1: N][M2-candidatas: N]` (yml l. 26; conferido), e o comentário usa
   `[METRICAS][M1-sub: ...][M2-sub: ...]` (l. 491): o `grep` de l. 506 encontra as 2 linhas se o
   revisor colar a linha do CI. **Correção:** §5.2: "a execução do CI no último commit antes do
   pedido de revisão (passo 6)"; renomear a linha do CI para `[METRICAS-CI]`.

7. **[MENOR] 05:§5.4, §5.7, §5.9, §7.3 — 3 regras de cálculo sem uma leitura única.** (a) "Conte
   cada palavra 1 vez" (l. 851, l. 497) permite a leitura "cada palavra diferente"; a ferramenta conta
   cada ocorrência (3 ocorrências de "realizar" = 3, conferido). (b) "M5 — Tempo de revisão | Total da
   fase" (l. 938) sem fórmula: média dos documentos ou Σmin ÷ Σpalavras × 1 000. (c) M7 com
   "Pendente": a espera de 10 dias úteis do solicitante (l. 1424) consome o prazo de decisão de 10 dias
   úteis (l. 1485), e o registro tem 1 coluna "Decisão" (l. 1521). **Correção:** (a) "Conte cada
   ocorrência 1 vez. Uma ocorrência que as 2 listas mostram conta 1 vez."; (b) "Σ `min` ÷ Σ `palavras`
   × 1 000 dos documentos da fase"; (c) "O prazo de decisão para durante o estado "Pendente". Registro:
   as datas de início e de fim de "Pendente", na coluna "Pendente"."

8. **[MENOR] 05:§7.3 — 2 saídas que terminam o processo sem dono.** (a) "Publicar uma alteração",
   passo 5: depois de 3 falhas, "escreva a causa na issue. O processo termina neste passo." (l. 1462):
   um PMD aceito fica sem publicação, sem responsável e fora do prazo de M7. (b) "Decidir um PMD",
   passo 2: "O dono do glossário decide o termo" (l. 1418), sem prazo e sem procedimento. **Correção:**
   (a) "envie a issue ao substituto do mantenedor. Este procedimento termina neste passo. O substituto
   recebe a issue no passo 1."; (b) "Prazo do dono do glossário: 10 dias úteis. Registro: a decisão,
   no glossário do projeto."

9. **[MENOR] 05:§6.7, §8.4 — `PTSBR_REF` não acompanha a versão MINOR.** "A tag da última PATCH da
   versão que os documentos declaram" (l. 1229). Um repositório com documentos que declaram `"1.0"` e
   `"1.1"` precisa de 2 valores, e o pipeline aceita 1. A MINOR é compatível (l. 1566), portanto a tag
   mais nova serve aos 2 documentos. **Correção:** "A tag da última versão publicada com o mesmo MAJOR
   da versão mais nova que os documentos declaram."

10. **[MENOR] 05:§9.5, §2.1 — "o aprovador da equipe" não é um papel definido.** §9.5 item 1 (l. 1742)
    usa "O aprovador da equipe"; §2.1 define apenas "no mínimo 2 aprovadores" (l. 131), sem equipe.
    **Correção:** "Um aprovador escolhe ..." ou definir em §2.1 "1 aprovador por equipe na Expansão".

## O que levaria a nota a 9

1. Fechar o controle de publicação no Git (problema 1): merge com dono, commit revisado no
   resultado, proteção do branch como critério de entrada do Piloto. É a única lacuna em que o
   processo descrito não impede um documento não aprovado de ser publicado.
2. Escrever o procedimento "Publicar uma versão" que junta PMD e PMR, registra a aprovação da
   MAJOR e o guia de migração (problema 2), e separar a preparação por pedido.
3. Dar ao registro de revisão no Git a mesma retenção e proteção do Anexo C e um instrumento de
   coleta (problema 3), para que o critério de 80% e a auditoria anual sejam recalculáveis sem
   leitura manual.
4. Corrigir os 4 defeitos de POP do problema 5 e a aprovação fora do Git (problema 4): o 05 é o
   modelo de POP da especificação e precisa passar no CK-5.4, no CK-5.7 e no CK-5.9 sem resíduo.
5. Unificar as definições de cálculo (problemas 6 e 7). Os problemas 8 a 10 são cosméticos.

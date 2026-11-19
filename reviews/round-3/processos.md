---
lente: processos
rodada: 3
notas: {correcao: 8, completude: 8, aplicabilidade: 7, coerencia: 7.5, valor: 8.5}
nota_final: 7.8
---

Lente: BPM, qualidade (ISO 9001), governança de documentação, POP e adoção de padrões.

Verificações feitas nesta rodada (nenhuma edita a especificação):
- `python3 build.py`: nenhuma linha `PROBLEM` (711 aprovadas, 360 não aprovadas).
- `build.py --render` numa cópia da especificação no scratchpad, executado da raiz como manda
  §7.3: o resultado é idêntico ao `03-dicionario.md`. `gerar_regras_dicionario.py --verificar`: OK
  (418 entradas). Os comandos do procedimento "Publicar uma mudança do dicionário" funcionam como estão escritos.
- `check_spec.py --teste`: 133 testes de regra corretos; textos "Antes" do 06 com 118 alertas;
  textos PTS-BR com 0; 20 frases da lista branca corretas. Confere com o CHANGELOG.
- `check_spec.py --spec`: 0 alertas.
- `check_spec.py --lista-branca --spec`: 19 palavras fora em **66 329** (0,03%); o CHANGELOG diz
  "19 de 66 327". Conferi os 155 "nomes próprios" aceitos pela heurística da maiúscula
  (`scratchpad/nomes.py`): quase todos são nomes reais (Git, SharePoint, Flesch). Vazam apenas
  "Matriz" (05), "Encadeie", "Respeite" e "Destaque" (02). O resultado da lista branca é honesto.
- Teste de comportamento do CI: `check_spec.py` com 7 alertas `warning` sai com código 0 (correto
  para §6.4). O `docs-lint-equipe.yml` **não executa** `--metricas` (ver problema 4).
- Arquivo de teste com "Há", "realizar", "irá", "deverá": as duas ferramentas de M2 contam
  "realizar" e "há". A lista branca também conta "irá" e "deverá", que são desvios de tempo verbal (R3.1) (ver problema 4).
- Formato de `tools/d*.txt` (`build.py`, linha 8: "6 campos"; estados `A` e `N`): não existe estado
  "obsoleta" (ver problema 5).
- A pasta não é um repositório Git (`git rev-parse` falha): a tag `v1.0.0`, que o
  `PTSBR_REF` usa, ainda não existe.

## Status dos problemas da rodada 2

Resumo: **12 resolvidos, 2 parcialmente resolvidos, 0 não resolvidos** (de 14). Quatro correções
criaram problemas novos. Os problemas 1, 4, 7 e 9 da lista abaixo mostram estes casos.

| # R2 | Problema | Status | Evidência |
|---|---|---|---|
| 1 | §4.4 com sobreposição e caso sem resultado | Resolvido | l. 579-581: "Aprovado" exige "Nenhum S2 com o estado `ABERTO` ou `EXCECAO`"; "Aprovado com exceções" exige "1 S2 ou mais com o estado `EXCECAO`". Os resultados não se sobrepõem. S1 `CORRIGIDO` não reprova (l. 563). CK-0.1 é S2 (l. 434) e aparece nos 3 resultados. **Mas** o fluxo de §4.1 não chega ao resultado "Aprovado com exceções" (problema novo 1). |
| 2 | M1, M2, M6, M7 não auditáveis | Resolvido, com um problema novo | (a) §5.2 l. 682-687: medição na submissão e na publicação; a meta usa a submissão; M2 conta apenas as palavras confirmadas (l. 706). (b) Linha `[LINTER][PTSBR.FraseLonga: 4/1]...` (l. 407) e tabela por regra no Anexo C (l. 1631-1636). (c) §7.6 tem as colunas Prioridade, Pedido, Triagem, Decisão, Publicação e Versão (l. 1306). **Mas** M1 e M2 da submissão não ficam em nenhum registro durável do fluxo Git (problema novo 4). |
| 3 | Auditor do Piloto e auditoria do mantenedor | Resolvido | §9.4 item 4 (l. 1506-1507): "No mínimo 1 revisor fundador é de outra equipe e não revisa os documentos do Piloto. Este revisor fundador é o auditor do Piloto." §3.5 nova (métricas, 5 decisões, treinamento, `auditorias/AAAA-mantenedor.md`). Critério de entrada do Piloto l. 213. |
| 4 | 1.0.0 publicada sem cumprir §8.5 | Parcial | (a) O teste com o Vale passou a critério de entrada do Piloto (l. 210, l. 1424; decisão E8), declarado em §6.1 e no CHANGELOG. (b) O instrumento da l. 209 é agora "Entrada `[1.0.0]` ... com o resultado de cada critério da seção 8.5", e o CHANGELOG tem estes resultados. (d) O CI executa `--spec --falhar` (docs-lint.yml l. 54). **Falta:** (c) licença continua "recomendada" e "O dono da especificação decide a licença antes do Piloto" (README l. 141-143): o papel não existe em §2.1, e a decisão não está nos critérios de entrada de §3.2. O registro de publicação também diverge da medição (66 327 × 66 329), e a tag `v1.0.0` não existe. |
| 5 | D9 não verificada; autoconformidade | Resolvido | `lista_branca.py` + `--lista-branca --spec --meta 1` no CI e em §8.5 item 6; 05 com 0,03% (4 palavras: "governança" do título, "martins", "icmc-usp"). "Perfil típico" passou a "Exemplos de cargo" (l. 96); "Rejeitado" passou a "Recusado"; os termos de adoção estão na tabela de §1. |
| 6 | "registro", "dia útil", "glossário do produto" | Resolvido | REGISTRO (s) no 03 l. 1230 e no 01 l. 403; "linha (de tabela)" NT-15 no 04 l. 937; "evidência" não aprovada (03 l. 728). "dia útil" só no 04 l. 886; o 05 §1 l. 44-45 remete ao 04. "glossário do produto": 0 ocorrências fora do CHANGELOG. |
| 7 | PMD urgente decide em 2 dias e publica em 30 | Resolvido, com um problema novo | §7.4 l. 1272: "Versão PATCH em até 5 dias úteis depois da decisão"; §8.1 l. 1352. A PATCH conflita com §8.4 e com a triagem (problema novo 9). |
| 8 | POP da governança e Exemplo 7 violam R5.10-R5.12 | Parcial | Feito: §4.1 tem 3 procedimentos com o bloco de R5.10 e linhas "Registro:"; §7.3 tem 3 procedimentos e inclui "Aceito com outro significado ou outra classe" (l. 1211, 1218); §4.5 tem o bloco. 02 R5.11/R5.12 corrigidos (l. 893 "vá para o passo 3"; l. 911 "Clique em **Aprovar**"). Exemplo 7: passo 5 de "Pedir o acesso" com destino para cada estado, verificação da MFA (l. 1013-1015), passo 5 de "Analisar" verifica o estado. **Falta:** laços sem retorno escrito, esperas sem saída "sem resposta no prazo", redator sem procedimento de correção, §4.5 sem aprovador, "Pendente" sem caminho (problemas novos 2 e 3); Exemplo 7 com 3 defeitos novos (problema 12). |
| 9 | Anexo A: 2 resultados para 3 casos, sem responsável | Resolvido, com um problema novo | l. 1573-1577: **Melhor ou igual** / **Inconclusivo** / **Pior**; §3.2 l. 235 aceita **Inconclusivo** com decisão e teste novo; RACI l. 166; responsável l. 1547. A nota "Com menos de 10 leitores, use o resultado apenas como informação" (l. 1579) conflita com o critério de saída (problema novo 7). |
| 10 | Material de treinamento inexistente e gabarito sem autor | Resolvido | Critério de entrada l. 214 ("O teste de 20 itens, o gabarito do RV3 e o resumo de 1 página estão publicados"); §9.4 item 1: o mantenedor escreve o gabarito e o aprovador registra; item 2: RV2 do mantenedor com a tabela "Mudanças" do 06. |
| 11 | Papéis sem definição e RACI incompleta | Resolvido | "revisor sênior" → substituto (l. 138-139); coluna "Auditor"; linhas "Analisar a causa...", "Verificar a eficácia...", "Auditar as decisões do mantenedor" (l. 168-170); "Eficácia" em §3.4 (l. 297); `auditorias/AAAA-MM.md` (l. 298). |
| 12 | Scripts sem dono em `tools/` | Resolvido | `tools/` tem só os arquivos de §6.2; os scripts de trabalho foram para `reviews/scripts-de-trabalho/`; `.gitignore` com `__pycache__/` (l. 828). |
| 13 | Gate de M6 sem os 50 alertas; POP exportado com limite 25 | Resolvido | §3.3 l. 250 "medido com no mínimo 50 alertas"; §4.5 passo 2 `--limite-frase auto` (l. 628). |
| 14 | Versão "1.0" nos cabeçalhos; `pts-br: 1.0` sem aspas | Resolvido | 03 l. 3, 04 l. 3, 06 l. 5: "versão 1.0.0"; §4.5 l. 615 `pts-br: "1.0"`. |

## Pontos fortes (até 5)

1. **Critério de aprovação fechado e coerente com a severidade.** A tabela de §4.4 cobre todos os
   casos sem sobreposição. O S1 corrigido não reprova. CK-0.1 é S2 sem exceção, com a mesma regra em §8.4
   (l. 1412-1413). O limite de exceções tem a regra de arredondamento com exemplo (l. 594-597).
   Um auditor aplica a tabela sem interpretação.
2. **Independência e melhoria contínua no padrão ISO 9001.** Auditor de outra equipe, auditor
   do Piloto definido (§9.4), auditoria anual do mantenedor com recálculo das métricas e 5 decisões
   (§3.5, ISO 9001 §9.2), ação corretiva com prazo e **verificação de eficácia** (l. 297, ISO 9001
   §10.2.1 d), regra de que o mantenedor não decide o próprio PMD. Cada controle tem um registro
   com nome de arquivo.
3. **Manutenção do dicionário reproduzível.** Fonte única (`d*.txt`), regeneração com resultado
   idêntico, regra do linter gerada e verificada no CI, registro de decisões com todas as datas que
   M7 precisa e prazos por prioridade, com caminho PATCH para o pedido urgente.
4. **Autoconformidade comprovada por ferramenta.** A lista branca aplica D9 ao texto normativo
   inteiro, com relatório por arquivo e gate de 1% no CI. O CHANGELOG lista a decisão para cada uma
   das 15 palavras fora da lista. Conferi a heurística de nomes próprios: o resultado não é inflado.
5. **Governança escrita como POP.** Os 7 procedimentos de §4.1, §4.5 e §7.3 têm responsável único,
   entrada, gatilho, prazo, linhas "Registro:" e destino no último passo. Os passos e as saídas
   têm limites de repetição. Um auditor sabe qual registro procurar em cada etapa.

## Problemas (ordenados por impacto)

1. **[IMPORTANTE] 05:§4.1 × §4.4 — o resultado "Aprovado com exceções" não tem caminho no fluxo
   (impasse).** O revisor pede a exceção no passo 5 ("Peça ao aprovador cada exceção S2 necessária,
   no comentário do desvio", l. 359) e decide o resultado no passo 7 com §4.4. O aprovador só
   escreve `EXCECAO @<seu-usuário>` no passo 2 do procedimento dele (l. 378-379), e o gatilho deste
   procedimento é "o comentário de resultado" (l. 375), que o revisor escreve **depois** do passo 7.
   No passo 7, a exceção pedida ainda tem o estado `ABERTO` (não existe estado "exceção pedida",
   l. 401), e §4.4 dá "Reprovado" (l. 581). Resultado: ou o revisor escreve "Aprovado com exceções"
   contra a tabela, ou o documento volta ao redator sem fim. No Piloto, o limite é de 5 exceções por
   1 000 palavras: este é um caminho frequente. **Correção:** acrescentar o estado
   `EXCECAO-PEDIDA` a l. 401; criar o procedimento "Decidir uma exceção S2" (responsável: aprovador;
   gatilho: um comentário de desvio com `EXCECAO-PEDIDA`; prazo: 2 dias úteis; saídas: `EXCECAO
   @aprovador` ou `ABERTO` com a causa); no passo 6 de "Revisar", esperar o texto corrigido **e** a
   decisão de cada exceção pedida; no aprovador, o passo 2 passa a "Confirme que cada exceção tem o
   estado `EXCECAO`".

2. **[IMPORTANTE] 05:§4.1, §4.5, §7.3 — os POP da governança ainda violam R5.11 (laços sem retorno,
   esperas sem prazo, saída que encerra um processo aberto).** Por CK-5.9 (S1, l. 490), o 05
   reprova pela própria escala.
   (a) "Revisar", passo 7 (l. 363): "Se o resultado for "Reprovado", informe ao redator os desvios
   ... Se o passo 6 acontecer 3 vezes, envie o pull request ao mantenedor. O processo termina neste
   passo." Nenhuma frase diz "volte ao passo 6". À letra, o processo termina no primeiro "Reprovado".
   R5.11 (02 l. 880) exige a volta, o número máximo e a saída depois do número. O mesmo defeito está em §4.5
   passo 6 (l. 639).
   (b) Esperas sem a saída "sem resposta no prazo" (02 l. 874): "Aguarde o texto corrigido do
   redator" (l. 360, l. 636); o aprovador com prazo de 2 dias úteis (l. 375) sem saída para o
   revisor quando o prazo termina.
   (c) "Decidir um PMD", passos 4 e 6 (l. 1213, 1219): "Pendente: ... Se o solicitante não responder
   em 10 dias úteis, o resultado é "Recusado". Vá para o passo 5." e depois "Se o resultado for
   ... "Pendente", feche a issue. O processo termina neste passo." A issue fecha no mesmo dia. Nenhum passo
   espera os 10 dias nem troca "Pendente" por "Recusado". A resposta do solicitante chega numa issue
   fechada.
   (d) "O processo termina neste passo" é usado para encerrar o **procedimento** quando o processo
   continua (l. 337 "peça ajuda ao mantenedor. O processo termina", l. 363, l. 639). O 06 usa uma
   4ª forma, "Este procedimento termina neste passo" (19 ocorrências), que não está entre os 3
   destinos de R5.11 (02 l. 876-878). Um auditor que lê "O processo termina" depois de "Reprovado"
   fecha o caso. O documento continua aberto.
   (e) O escalonamento ao mantenedor (l. 337, 363, 639) não tem procedimento nem prazo de resposta.
   **Correção:** (a) "Se o resultado for "Reprovado", informe ao redator os desvios com o estado
   `ABERTO` e volte ao passo 6. Depois de 3 vezes, envie o pull request ao mantenedor. Siga o
   procedimento "Decidir um conflito de revisão"." (b) no passo 6: "Se o redator não enviar o texto
   em 10 dias úteis, escreva o resultado "Reprovado" e feche o pull request. O processo termina neste
   passo."; (c) "Pendente: escreva a informação que falta e aguarde 10 dias úteis. Se o solicitante
   responder, volte ao passo 4 (1 vez). Sem resposta, o resultado é "Recusado"; vá para o passo 5." e
   retirar "Pendente" do passo 6; (d) acrescentar a R5.11 o 4º destino "Este procedimento termina
   neste passo. O procedimento "X" recebe ..." e usar "O processo termina" apenas no fim real;
   (e) procedimento de 4-5 passos para o mantenedor, com prazo de 5 dias úteis.

3. **[IMPORTANTE] 05:§4.1, §4.5 — etapas sem procedimento (R5.10) no fluxo de revisão.**
   (a) O redator corrige os desvios, mas "Pedir a revisão" termina no passo 6 (l. 339). Nenhum
   procedimento do redator recebe a saída "informe ao redator" (l. 363) nem a recusa do aprovador.
   O aprovador informa ao **revisor** (l. 387-389), que espera o redator. Ninguém informa o redator.
   R5.10 (02 l. 843): "O último passo de cada procedimento diz qual procedimento recebe a saída."
   (b) §4.5 é o fluxo dos POP fora do Git, mas tem só o procedimento do revisor. O redator não tem
   procedimento, o aprovador também não, e a recusa da aprovação não tem caminho. O pedido de exceção S2 também não tem passo, mas "Aprovado
   com exceções" (passo 6) depende de `EXCECAO` do aprovador. O passo 2 executa o linter sem
   `--metricas`, mas o Anexo C pede "Palavras (`check_spec.py --metricas`)" e "M1 e M2 na submissão"
   (l. 1624-1625).
   (c) "Pedir a revisão" altera o estado do pull request e termina em "Peça a revisão" (l. 339),
   sem verificação (R5.9, CK-5.7). "Sem prazo" (l. 328, 1184) não é "o prazo, com o número e a
   unidade" (R5.10, 02 l. 841).
   **Correção:** (a) procedimento "Corrigir os desvios da revisão" (responsável: redator; gatilho:
   comentário "Reprovado" ou recusa; prazo: 5 dias úteis; último passo: "Peça a revisão de novo. O
   revisor recebe o pull request no passo 6 de "Revisar um documento""). (b) em §4.5, os mesmos
   3+1 procedimentos de §4.1, com os passos da ferramenta, e o passo "Calcule M1 e M2:
   `check_spec.py --metricas documento.md`. Registro: o valor, na tabela do Anexo C."
   (c) passo 7 novo em "Pedir a revisão": "Verifique que o pull request mostra o revisor no campo
   **Reviewers**."; trocar "Sem prazo" por "Prazo: nenhum. O prazo começa no pedido de revisão (M5)."
   ou definir em R5.10 que "Sem prazo" é um valor aceito.

4. **[IMPORTANTE] 05:§4.1, §5.2, §3.5 × `tools/ci/docs-lint-equipe.yml` — M1 e M2 por documento
   não ficam num registro, e as 2 ferramentas de M2 contam a mesma palavra.** O critério de saída
   do Piloto e da Expansão é "80% dos documentos publicados cumprem as metas de M1, M2 e M3 ... Seção
   5.9, por documento" (l. 232, 265), e §3.5 manda o auditor calcular "de novo M1 a M7 de 1 mês com
   os registros de revisão" (l. 309).
   (a) O registro de M1/M2 da submissão é "a primeira execução do linter no CI do pull request" (l. 335). O
   pipeline da equipe executa só os alertas e a lista branca. O pipeline não executa `--metricas`, e só `--metricas`
   calcula M1, porque M1 precisa do total de frases. O log do job também expira.
   (b) O formato fixo do resultado (l. 406-407) não tem M1 nem M2. O Anexo C tem os 2 campos (l. 1625-1626),
   embora diga "Os campos são iguais aos campos do registro de revisão da seção 4.1" (l. 1612).
   (c) M2 usa 2 instrumentos (l. 699-705) sem regra contra a contagem dupla. Conferi:
   "realizar" e "há" aparecem nos 2, e a lista branca também mostra "irá" e "deverá", que são
   desvios de R3.1 (CK-3.1), não palavras não aprovadas.
   (d) As metas de M3 na publicação (l. 784-785: S1 = 0; S2 ≤ 5/3/1,5) são iguais ao critério de
   §4.4 e ao limite de exceções (l. 590-592): todo documento publicado as cumpre. Na prática, o
   critério de 80% mede apenas M1 e M2, os 2 valores sem registro.
   **Correção:** acrescentar ao formato de l. 406 os campos `[M1-sub: 88%][M2-sub: 4,2][M1-pub:
   96%][M2-pub: 0,0]`; no passo 1 de "Revisar", "Calcule M1 e M2 com `--metricas`. Registro: os
   campos M1-sub e M2-sub do comentário de resultado"; acrescentar ao `docs-lint-equipe.yml` um passo
   `check_spec.py --metricas`; em §5.4: "Conte cada palavra 1 vez. Uma palavra que os 2 instrumentos
   mostram conta 1 vez. Um tempo verbal não aprovado é um desvio de CK-3.1 e fica fora de M2."; em
   §5.9, retirar M3 na publicação do critério "por documento" ou trocar por "M3 S3 na publicação".

5. **[IMPORTANTE] 05:§7.3-§7.4, §8.1 × `tools/` — a manutenção do dicionário cobre apenas a
   inclusão no 03.** (a) §7.4 (l. 1274) e §8.1 (l. 1357-1359): "marque a palavra como obsoleta numa
   versão MINOR. O linter mostra um alerta `suggestion` para as palavras obsoletas." O formato de
   `tools/d*.txt` tem apenas os estados `A` e `N` (6 campos, `build.py` l. 8). `build.py`,
   `gerar_regras_dicionario.py` e `check_spec.py` não têm a palavra "obsolet" nem uma regra de nível
   `suggestion`. O exemplo de CHANGELOG (l. 1378-1379) e o caminho de alteração e exclusão não
   têm ferramenta, contra a l. 18 ("Este documento descreve apenas as ferramentas que existem").
   (b) §7.1 envia "Nome técnico ou verbo técnico novo de TI" ao `04-termos-tecnicos.md` (l. 1144).
   O passo 1 de "Publicar uma mudança do dicionário" diz só "Altere a entrada no arquivo
   `tools/d*.txt`" (l. 1227), embora o gerador leia as tabelas 5.4 e 6.3 do 04. (c) O passo 6 manda
   "publique a versão" sem citar os 8 critérios de §8.5. Os passos 2-5 só executam o build e
   `--teste`, sem `--spec --falhar` e sem `--lista-branca --meta 1`. **Correção:** (a) estado `O`
   (obsoleta) em `d*.txt`, com a palavra substituta; o `build.py` publica a coluna "Obsoleta: use X" e
   o gerador cria `PalavrasObsoletas.yml` com `level: suggestion` e os casos de teste; ou retirar de
   §7.4 e §8.1 a promessa do alerta até a ferramenta existir. (b) passo 1: "Para o 03, altere
   `tools/d*.txt`. Para o 04, altere a tabela do 04 e execute `gerar_regras_dicionario.py`." (c)
   passo 6: "Confirme os critérios da seção 8.5 e escreva o resultado na entrada do CHANGELOG."

6. **[IMPORTANTE] 05:§9.3 × §3.3 — impasse para qualificar o revisor de uma equipe nova na
   Expansão.** Critério de entrada da Expansão: "Cada equipe nova tem no mínimo 1 revisor com a
   trilha do revisor" (l. 249). Pré-requisito da trilha: "trilha do redator e 5 documentos aprovados
   como redator" (l. 1478). A exceção de §9.4 vale só "Antes do Piloto" (l. 1503). O Piloto tem
   "1 equipe" (l. 203). Uma equipe nova não escreveu documentos PTS-BR, portanto ninguém dela tem os 5
   documentos aprovados. A entrada na Expansão fica bloqueada, ou exige uma exceção sem regra.
   **Correção:** em §3.2 Atividades, item 6: "Cada equipe da Expansão escolhe 1 candidato a revisor.
   O candidato faz a trilha do redator e escreve 5 documentos da equipe em PTS-BR. Um revisor do
   Piloto revisa estes documentos." Ou estender §9.4 à Expansão: "o revisor da equipe nova faz a
   trilha sem os 5 documentos, e o mantenedor revisa de novo os 5 primeiros documentos do revisor".

7. **[IMPORTANTE] 05:§11 (Anexo A) × §3.2 — o teste de compreensão com 5 a 9 leitores não decide
   o gate.** O mínimo é "5 leitores" (l. 1552). O critério de saída do Piloto exige o resultado
   **Melhor ou igual** ou **Inconclusivo** com decisão (l. 235). A nota nova diz: "Com menos de 10
   leitores, use o resultado apenas como informação" (l. 1579). Com 1 equipe no Piloto, o caso
   normal é ter menos de 10 leitores. O aprovador não sabe se um "Melhor ou igual" com 6 leitores
   cumpre o critério, nem se um "Pior" com 6 leitores obriga a repetir o Piloto (l. 1577). **Correção:**
   "Com 5 a 9 leitores, o resultado **Melhor ou igual** cumpre o critério de saída do Piloto, e o
   resultado **Pior** passa a **Inconclusivo**. Na Expansão, repita o teste com no mínimo 10 leitores."

8. **[MENOR] 05:§8.3 × §6.4 × §8.1 — a mudança de nível no fim da transição MAJOR contradiz o gate
   de M6.** §8.3 (l. 1390): "No fim do período, o mantenedor altera o nível das regras novas para
   `error`." §6.4 (l. 894): `error` só para "Regra com M6 de no máximo 5%, medido com no mínimo 50
   alertas", e §8.1 (l. 1351) faz desta mudança uma versão MINOR. §6.4 (l. 898-900) também tem um
   argumento contrário à própria conclusão: "Uma regra com o nível `error` bloqueia um pull request
   que teve sucesso com o nível `warning`. Portanto, esta mudança é uma versão MINOR." **Correção:**
   §8.3: "No fim do período, o mantenedor aplica a seção 6.4 às regras novas, numa versão MINOR."
   §6.4: "O nível `error` não altera a conformidade de um texto: o revisor já verifica a regra.
   Portanto, esta mudança é uma versão MINOR."

9. **[MENOR] 05:§7.4, §8.1, §8.4, §6.7 — a PATCH do PMD urgente não chega ao revisor nem ao CI.**
   §8.4 (l. 1403-1404): "A versão PATCH não altera a conformidade e não aparece no documento"; mas a
   PATCH do PMD urgente (l. 1352) torna aprovada uma palavra. Um documento declara `"1.0"`. O CI da
   equipe usa `PTSBR_REF: 'v1.0.0'` e mostra a palavra nova como fora da lista branca, até alguém
   alterar a variável. §8.3 diz "obrigatória a partir da publicação" (l. 1388), mas nenhum papel
   atualiza o `PTSBR_REF`. A triagem tem prazo de 3 dias úteis para todo pedido (l. 1269), e a decisão
   urgente tem prazo de 2 dias úteis **depois do pedido** (l. 1271). **Correção:** em §8.4, "O revisor usa a
   última PATCH da versão declarada"; em §6.7, "Use em `PTSBR_REF` a tag da última PATCH. O
   mantenedor informa cada PATCH às equipes no dia da publicação"; em §7.4, "Triagem, pedido urgente:
   1 dia útil".

10. **[MENOR] 05:§3.4 — a auditoria mensal do Piloto pede mais documentos do que existem.** "Piloto
    e Expansão: 1 vez por mês, 10 documentos" (l. 290). O Piloto tem 8 a 12 semanas e um mínimo de
    15 documentos publicados (l. 231). No 1º mês, o número de documentos publicados pode ser menor
    que 10. A regra não diz se o auditor repete documentos já auditados. **Correção:** "10
    documentos publicados no mês, ou todos os documentos publicados no mês se forem menos de 10. Um
    documento auditado não volta à amostra sem uma alteração."

11. **[MENOR] 05:§5.9 — a agregação de M5 "Total da fase" não está definida.** "M5 — Duração da
    revisão | Total da fase | ≤ 5 dias úteis" (l. 788): o texto não diz se o valor é a média, a mediana, o máximo
    ou um percentil. A tabela de §1 define "mediana" (l. 71), mas §5 não usa a palavra. A duração também mede
    o tempo de correção do redator, e o prazo do revisor é esta meta (l. 345). **Correção:** "Mediana
    da duração dos documentos da fase"; prazo do revisor: "3 dias úteis para a primeira revisão,
    2 dias úteis para cada revisão depois de uma correção".

12. **[MENOR] 06:Exemplo 7 — ordem de controle e verificação final.** (a) A senha temporária é
    compartilhada no passo 6 (l. 1009), e a MFA é verificada no passo 8 (l. 1013). Se a MFA estiver
    inativa, a conta já tem uma senha conhecida e nenhuma MFA, e o procedimento só abre um incidente.
    O controle está depois da liberação. (b) O passo 9 altera o estado para **Resolvido** e termina
    (l. 1017), sem verificar o estado. Esta é a falha que o 02 corrige no exemplo de R5.12 ("O
    procedimento altera o estado do chamado. Portanto, o passo 4 verifica o estado", 02 l. 920).
    (c) Nenhum procedimento entrega a senha ao colaborador novo: o gestor recebe a senha e o processo
    termina. **Correção:** mover a verificação da MFA para antes do passo 6; passo 10: "Verifique
    que o chamado tem o estado **Resolvido**. O processo termina neste passo."; passo 6 de "Pedir o
    acesso": "No primeiro dia, abra o cofre de segredos e mostre a senha temporária ao colaborador
    novo."

13. **[MENOR] 05:§2.1, README, 01 — separação de funções e papéis sem definição.** (a) As 3 regras
    de l. 136-141 não impedem que o aprovador seja o redator: o gestor que escreve um POP aprova
    as próprias exceções e a própria publicação. (b) "O dono da especificação decide a licença" (README
    l. 142-143): este papel não está em §2.1. (c) 01 §8.1 passo 8 (l. 357): o redator "peça uma
    exceção", mas a RACI dá o pedido ao revisor (l. 158), e 01 §8.2 cita "revisões parciais"
    (l. 364), que o 05 não define. **Correção:** regra 4 em §2.1: "O aprovador de um documento não
    é o redator do documento."; README: "O aprovador decide a licença. Critério de entrada do Piloto:
    a licença está registrada no README."; 01 l. 357: "escreva a justificativa no pedido de revisão.
    O revisor pede a exceção (`05-governanca.md`, seção 4.1)"; retirar "revisões parciais" ou
    definir o termo.

14. **[MENOR] CHANGELOG × pacote — o registro de publicação não confere e a tag não existe.** O
    critério 6 diz "19 de 66 327 palavras", e a medição atual dá 66 329. O critério 2 diz "a partir
    dos arquivos de origem do mesmo commit", mas a pasta não é um repositório Git, e a tag `v1.0.0`
    que o `PTSBR_REF` usa não existe. **Correção:** gerar os números do CHANGELOG no último build
    (ou escrever o hash do pacote medido) e criar o repositório com a tag antes do Piloto. Este é
    um critério novo de §3.2: "A tag `v1.0.0` existe e o CHANGELOG tem os números do commit da tag."

## O que levaria a nota a ≥ 8

1. Fechar o caminho da exceção S2: estado `EXCECAO-PEDIDA` e procedimento do aprovador antes do
   resultado (problema 1). Hoje o resultado "Aprovado com exceções" não tem caminho no fluxo principal.
2. Fazer os POP do 05 passarem no CK-5.9 e no R5.10: volta explícita ao passo 6, saída "sem resposta
   no prazo" em cada espera, "Pendente" com espera real, procedimento do redator para a correção,
   §4.5 com aprovador e pedido de exceção, e um destino-padrão para "este procedimento termina"
   (problemas 2 e 3).
3. Registrar M1 e M2 por documento no comentário de resultado, executar `--metricas` no CI e contar
   cada palavra de M2 1 vez (problema 4). Sem isto, o critério de saída das fases e a auditoria do
   mantenedor não podem ser recalculados.
4. Completar a manutenção do dicionário: estado "obsoleta" nas fontes e no linter (ou retirar a
   promessa), publicação de mudanças no 04 e o gate de §8.5 no procedimento (problema 5).
5. Remover os 2 impasses de fase: qualificação do revisor de uma equipe nova (problema 6) e
   validade do teste de compreensão com 5 a 9 leitores (problema 7).

---
lente: processos
rodada: 2
notas: {correcao: 7, completude: 8, aplicabilidade: 7, coerencia: 7, valor: 8}
nota_final: 7.4
---

Lente: BPM, qualidade (ISO 9001), governança de documentação, POP e adoção de padrões.

Verificações feitas nesta rodada (nenhuma edita a especificação):
- `python3 tools/build.py`: sem linha `PROBLEM` (562 aprovadas, 316 não aprovadas).
- `python3 tools/build.py --render <scratchpad>/03-render.md` + `diff`: idêntico ao `03-dicionario.md`
  (o 03 é de fato regenerável a partir de `d*.txt` + `intro.md`).
- `python3 tools/gerar_regras_dicionario.py --verificar`: OK (313 entradas).
- `python3 tools/check_spec.py --spec`: 0 alertas. `--teste`: 95 casos corretos; textos "Antes" do 06
  com 102 alertas; textos PTS-BR com 0. Motor Vale: não executado (Vale não instalado nesta máquina);
  ver problema 4.
- `check_spec.py --metricas` no Exemplo 7 (POP) extraído do 06: 647 palavras, M1 100%, M2 0.
- `scratchpad/cobertura_r2.py`: 81 regras, 59 itens CK, zero regra sem item; as 11 regras `[vale]`
  têm arquivo Vale e coluna "Linter" preenchida; referências "(ver X.Y)" de 05 apontam para a seção certa.
- `tools/check04.py ../05-governanca.md` (script da própria pasta `tools/`, que aplica D9: palavra
  ausente do 03 e do 04 = não aprovada).
- Script de vazamento da rodada 1 (`tools/naousadas.py`) sobre README, 01, 02, 04, 05, 06.

## Status dos problemas da rodada 1

Resumo: **13 resolvidos, 5 parcialmente resolvidos, 0 não resolvidos** (de 18).

| # R1 | Problema | Status | Evidência |
|---|---|---|---|
| 1 | Impasse de partida (revisores) | Resolvido | 05 §9.4 "Exceção de partida: revisores fundadores"; §3.2 critério de entrada cita "no mínimo 2 revisores fundadores"; §5.8 usa os fundadores para a linha de base. Um impasse análogo apareceu para o **auditor** (problema novo 3). |
| 2 | `[lint]` delega ao linter regras que ele não tem | Resolvido | 02: 11 `[vale]` + 70 `[revisor]`; 13 arquivos YAML reais em `tools/vale/PTSBR/`, cada um com o ID na 1ª linha; coluna "Linter" de §4.2 com o nome do arquivo e o limite ("apenas o futuro simples..."); 01 §8.2: "Aplique a lista de verificação inteira". |
| 3 | A especificação não segue o próprio dicionário | Parcial | Lista explícita "Não aprovada": resolvido (`--spec` = 0; o script da R1 só acha falsos positivos: "o mesmo" adjetivo, "completa", "esperada"). Mas D9 (palavra ausente = não aprovada) não é verificado: `check04.py` relata 349 tipos/771 ocorrências em 05 sem entrada no 03 nem no 04, fora a metalinguagem de 01 §11.2 (problema novo 5). |
| 4 | Seção 5 não serve para POP | Resolvido (regras) | R5.9 estendida ("um registro ou o estado de um pedido"); R5.10 (bloco Responsável/Entrada/Gatilho e prazo), R5.11 (todas as saídas, limite de repetição), R5.12 ("Registro:"); 01 §2.1 e 05 §3.1 incluem POP; Exemplo 7 com 3 procedimentos e caminho de recusa. O Exemplo 7 ainda viola R5.11 e R5.9 (problema novo 8). |
| 5 | Vocabulário de processo ausente; prazo alterado | Parcial | Adicionados: 03 PRAZO, ETAPA, RESPONSÁVEL, ENTRADA, SAÍDA, RECUSAR, ENCAMINHAR, CARGO; 04 NT-19/20/21 colaborador, gestor, solicitante, aprovador, auditoria, conformidade, desvio, evidência, ação corretiva, causa raiz, indicador, meta, dia útil. "5 dias úteis" restaurado no Exemplo 7; 05 §7.5 l. 990 proíbe trocar requisito. Faltam: `registro` (sentido de processo), trimestre, mensal, anual, rejeitar, setor, departamento, devolver; "dia útil" tem 2 definições (problema novo 6). |
| 6 | SLA de publicação × versionamento | Resolvido | 05 §7.4 l. 974-975: inclusão → próxima MINOR; alteração/remoção → obsoleta na MINOR, efetiva na MAJOR. |
| 7 | Fluxo do dicionário não descreve a fonte real | Resolvido | 05 §7.3 "Fonte única" + passos 7-11 (`d*.txt` → `build.py` → `--render` → `gerar_regras_dicionario.py` → testes). Regeneração conferida com `diff` (idêntico). |
| 8 | Registro sem estado; M3 incalculável | Resolvido | §4.1: estados `ABERTO`, `CORRIGIDO`, `EXCECAO @aprovador`, `REGISTRADO`; resultado fixo `[RESULTADO: ...][S1][S2-exc][S3][palavras][min][linter-descartados]`. M6 e M7 continuam incalculáveis (problema novo 2). |
| 9 | Instrumentos de fase indefinidos; auditoria sem critério | Parcial | Anexo A (protocolo), Anexo B (questionário, "viável = média ≥ 4"), critério de saída separado por documento × total, auditoria com critério 90%, S2 publicado → ação corretiva 20 dias úteis, auditor de outra equipe. Restam: Anexo A sem resultado "pior" e com "Empate" em conflito com o critério de saída; a restrição 3 de §2.1 aponta para uma auditoria que §3.4 não define (problema novo 3). |
| 10 | Governança só para docs-as-code | Resolvido | §4.5 (Confluence/Google Docs/SharePoint/SGQ, exportação para `.md`, linter, aprovação na ferramenta) + Anexo C + retenção "vida do documento e mais 1 ano" (ISO 9001 §7.5). |
| 11 | Referência "ver 5.7" errada | Resolvido | Critérios de saída citam "Seção 5.9" (metas); "Seção 5.7" só para M6, que está em 5.7. Script: zero referência para seção errada. |
| 12 | S1 "comando incorreto" × checklist | Resolvido | §4.3 l. 448 "Comando com dois significados possíveis"; l. 452 "Um comando incorreto é um defeito da revisão técnica". |
| 13 | Linha de base depende de ferramenta inexistente | Resolvido | `check_spec.py --metricas` existe e funciona; §5.8 define M3/M5 da linha de base pelos fundadores; §6 descreve só o que existe. |
| 14 | PMR sem formulário, SLA, critério | Resolvido | §7.7: formulário, triagem 5 / decisão 20 dias úteis, 2 critérios de aceite, item novo em §4.2 e teste do linter. |
| 15 | Uso provisório × S1 | Parcial | Pedido urgente agora cobre "passo com ação irreversível" (§7.2, §7.3). Mas a decisão urgente (2 dias) não tem caminho rápido de publicação: a palavra só vale na próxima MINOR, até 30 dias depois (problema novo 7). |
| 16 | Taxonomia paralela em 01 | Resolvido | 01 §8.2 usa `[S2][R3.4]`; 01 §8.5 remete a 05 §4.3 e §4.4. |
| 17 | Identificação de versão inconsistente | Parcial | `[1.0.0]` no CHANGELOG; README, 01, 02, 05 = "1.0.0"; §8.4 define `pts-br: "1.0"` (MAJOR.MINOR). Mas 03 l. 3, 04 l. 3 e 06 l. 5 dizem "versão 1.0"; §4.5 l. 498 usa `pts-br: 1.0` sem aspas; e a 1.0.0 consta como publicada sem cumprir §8.5 (problema novo 4). |
| 18 | CK-5.4 / CK-0.1 | Resolvido | CK-0.1 criado (l. 331). CK-5.4 agora "—", coerente com R5.4 `[revisor]`. |

## Pontos fortes (até 5)

1. **Ligação regra → checklist → linter verificável.** 81 regras, 59 itens CK, zero regra órfã;
   cada regra `[vale]` tem arquivo YAML com o ID na primeira linha e casos `deve_alertar` /
   `nao_deve_alertar` (95 casos corretos). A coluna "Linter" declara o limite de cada regra
   ("VerboSuporte (apenas R3.5)"), e §6.10 diz o que só o revisor verifica. Um auditor consegue
   reconstruir quem verifica o quê.
2. **Manutenção do dicionário com fonte única e regeneração comprovada.** §7.3 manda editar
   `tools/d*.txt`, executar `build.py`, `--render`, gerar a regra Vale e testar; o CI (`regras`)
   executa `gerar_regras_dicionario.py --verificar`. Conferi: o 03 regenerado é idêntico ao publicado.
3. **Seção 5 agora serve para POP.** R5.10 (um responsável por procedimento, entrada com origem,
   gatilho e prazo com número e unidade), R5.11 (todas as saídas, "sem resposta no prazo", limite de
   repetições) e R5.12 ("Registro:" com nome e lugar) são o núcleo de uma instrução de trabalho
   auditável. P10 em 01 dá a justificativa; CK-5.8 a CK-5.10 tornam isso revisável.
4. **Registro de revisão com estados e formato fixo, também fora do Git.** `[S2][R4.2][ABERTO]`,
   o resultado com contagens e o Anexo C com os mesmos campos e regra de retenção dão a informação
   documentada que ISO 9001 §7.5 pede, nos dois fluxos.
5. **Adoção com gates mensuráveis e instrumentos nomeados.** Cada critério de entrada e de saída de
   §3.2-§3.3 tem a coluna "Instrumento"; o Anexo A define tarefa, medida, desenho cruzado (grupo 1
   e 2) e critério; o Anexo B define escala e corte; §3.4 tem critério de aceite da amostra e prazo
   de ação corretiva.

## Problemas (ordenados por impacto)

1. **[IMPORTANTE] 05:§4.4 — o critério de aprovação tem sobreposição e um caso sem resultado.**
   (a) "Aprovado: Zero S1. Zero S2 com o estado `ABERTO`. Versão ... declarada" (l. 474) também é
   verdadeiro para um documento com exceções `EXCECAO`; os resultados "Aprovado" e "Aprovado com
   exceções" se sobrepõem, e M3/auditoria contam resultados diferentes para o mesmo documento.
   (b) "Reprovado: Um S1 ou mais" (l. 476) não diz o estado: um S1 que o revisor registrou e o
   redator corrigiu (`CORRIGIDO`) reprova o documento à letra, embora §4.3 diga "Corrija o desvio
   antes da publicação". (c) CK-0.1 é S3 (l. 331) e "S3 não bloqueia a publicação" (l. 463), mas a
   versão declarada é condição de "Aprovado" e não aparece em "Aprovado com exceções" nem em
   "Reprovado": um documento sem `pts-br` não tem resultado definido, ou passa como "com exceções".
   **Correção:** reescrever a tabela: "Aprovado: zero S1 e zero S2 com estado `ABERTO` ou
   `EXCECAO`; CK-0.1 = sim." / "Aprovado com exceções: zero S1 `ABERTO`; cada S2 `CORRIGIDO` ou
   `EXCECAO`; exceções ≤ limite; nenhuma exceção em aviso; CK-0.1 = sim." / "Reprovado: qualquer
   S1 ou S2 `ABERTO`, exceções acima do limite, ou CK-0.1 = não." e subir CK-0.1 para S2.

2. **[IMPORTANTE] 05:§5.2-§5.9, §7.6 — M1, M2, M6 e M7 não são auditáveis com os dados definidos.**
   (a) M1 e M2 são medidos "Em cada revisão" (l. 545-546), sem dizer se na submissão ou na
   publicação. Na publicação a meta é vazia: cada frase longa ou palavra não aprovada confirmada
   precisa de `CORRIGIDO` ou `EXCECAO`, limitada a 5 por 1 000 palavras no Piloto, então "M2 ≤ 10 por
   1 000" (l. 643) nunca reprova nada. Na submissão a meta compete com "M3 na submissão". Além disso,
   M2 conta alertas brutos ("O script conta os alertas", l. 563-564), com falsos positivos.
   (b) M6 é "por regra" e precisa do total de alertas de cada regra (l. 619-621), mas o resultado de
   §4.1 só grava `linter-descartados` total, a etiqueta `[FP][PTSBR.Regra]` não está entre os
   "formatos fixos" de §4.1, e o Anexo C só tem "Alertas do linter / alertas descartados" totais. O
   total por regra vive no log do CI, que expira. M6 é o gate de `error` (§6.4, "no mínimo 50
   alertas") e de entrada na Expansão. (c) M7 precisa da data de abertura, da data de triagem, da
   data de decisão e da urgência (§7.4), mas o registro de §7.6 (l. 1006) tem uma única coluna "Data"
   e nenhuma coluna de urgência.
   **Correção:** (a) definir em §5.2: "M1 e M2: medidos na submissão (primeira execução do linter no
   pull request); a meta da fase é por documento"; contar em M2 apenas alertas confirmados.
   (b) acrescentar ao formato fixo de §4.1 a linha `[LINTER][PTSBR.FraseLonga: 4/1][PTSBR.Haver: 2/0]`
   (alertas/descartados por regra) e a mesma coluna no Anexo C. (c) trocar a coluna "Data" de §7.6
   por "Abertura | Urgência | Triagem | Decisão | Publicação".

3. **[IMPORTANTE] 05:§3.2, §2.1, §9.5 — impasse de partida do auditor e auditoria do mantenedor
   inexistente.** A saída do Piloto exige "auditoria de 10 documentos publicados por um auditor"
   (l. 205); o auditor "É um revisor de outra equipe" e "não audita os documentos que o auditor
   escreveu ou revisou" (l. 112); a trilha do auditor exige a trilha do revisor (l. 1195), cujo
   pré-requisito são "5 documentos aprovados como redator" (l. 1160), e a exceção de §9.4 vale só
   para "até 3 revisores fundadores" antes do Piloto. No Piloto existe uma equipe; os fundadores
   revisam os documentos e o mantenedor revisa de novo os 5 primeiros de cada um (l. 1185). À letra,
   ninguém qualifica como auditor. Além disso, a restrição 3 (l. 117-118) diz que "Um auditor faz
   esta auditoria (ver 3.4)" das métricas, regras e treinamentos do mantenedor, mas §3.4 só define
   auditoria de documentos publicados: o controle de independência (ISO 9001 §9.2.2) aponta para um
   processo que não existe.
   **Correção:** em §9.4, item novo: "No mínimo 1 revisor fundador é de outra equipe e não revisa
   documentos do Piloto. Este revisor fundador é o auditor do Piloto." Em §3.4, linha nova na tabela
   "Auditoria do mantenedor: 1 vez por ano, um auditor verifica o cálculo de M1-M7 de 1 mês, 5
   decisões de PMD/PMR do registro e os registros de treinamento; resultado em
   `auditorias/AAAA-mantenedor.md`".

4. **[IMPORTANTE] 05:§6.6 × §8.5 × §3.2, CHANGELOG — a versão 1.0.0 consta como publicada sem
   cumprir o critério de publicação.** §8.5 item 4 exige `--teste` "com o motor Python e com o Vale".
   §6.6 (l. 820-822): "Os 8 casos novos ... ainda não têm um resultado com o Vale. O mantenedor
   executa os testes com o Vale antes de publicar a versão 1.0.0". Mas o README, 01, 02 e 05 já dizem
   "Versão 1.0.0", e o CHANGELOG tem `[1.0.0] - 2026-11-18`. O critério de entrada do Piloto usa como
   instrumento "Entrada `[1.0.0]` no `CHANGELOG.md`" (l. 182): o instrumento confirma a entrada, não
   o gate. O README também diz "O mantenedor confirma a licença antes da primeira publicação" (licença
   apenas "recomendada"). O job `regras` do CI executa `--spec --resumo` como "relatório, não
   bloqueia", embora §8.5 item 5 exija zero alertas.
   **Correção:** (a) marcar a versão como `1.0.0-rc2` até os testes com o Vale passarem, ou executar
   os testes e registrar o resultado em §6.6; (b) trocar o instrumento de l. 182 por "Registro de
   publicação com o resultado dos 7 critérios de §8.5 (`auditorias/release-1.0.0.md`)"; (c) decidir
   a licença antes da 1.0.0; (d) no CI, `check_spec.py --spec --falhar`.

5. **[IMPORTANTE] 05 inteiro, 01 §11.1 — autoconformidade verificada só contra a lista explícita;
   D9 não é verificada.** 01 §11.1 diz "O texto normativo desta especificação segue o PTS-BR"; R1.1
   e D9 do 03 dizem que palavra ausente do 03 e do 04 não é aprovada. O gate de §8.5 item 5 só procura
   a lista "Não aprovada". O `tools/check04.py` (que existe na pasta, mas não está em §6.2 nem em §8.5)
   relata em 05 349 tipos e 771 ocorrências sem entrada, fora a metalinguagem de 01 §11.2. Parte é
   forma flexionada que o script não reconhece, mas os termos centrais da própria governança não
   existem no 03 nem no 04: "fase" (34×), "publicação" (15×), "piloto", "amostra", "trilha",
   "triagem", "adoção", "treinamento", "linha de base", "substituto", "rejeitar"/"Rejeitado" (resultado
   de PMD, l. 942 e 997), "trimestre". "Perfil típico" aparece 5× (l. 77-107), e "perfil de acesso" é
   não aprovada no 03 (D9 de DECISOES-R2). 05 também escreve números por extenso, contra R8.4: "Três
   restrições" (l. 114), "Três a cinco equipes" (l. 213), "dois", "duas" (18 ocorrências pelo
   `check04.py`). Um auditor que aplica CK-1.1 e CK-8.2 ao 05 registra centenas de S2.
   **Correção:** (a) acrescentar a 01 §11.2 um grupo "Processo de adoção" (fase, piloto, expansão,
   amostra, trilha, triagem, linha de base, publicação, treinamento, substituto) ou criar entradas no
   03/04; (b) trocar "Perfil típico" por "Exemplos de cargo"; trocar "Rejeitado" por "Recusado"
   (RECUSAR é aprovada); (c) documentar o `check04.py` em §6.2 e incluir em §8.5 "zero UNKNOWN e zero
   STYLE no texto normativo, salvo lista de exceções registrada".

6. **[IMPORTANTE] 04 × 05 × 02 — termos de processo com dois significados ou dois nomes.**
   (a) "registro": o 04 (l. 914) define apenas "Uma linha de uma tabela de banco de dados" (NT-15),
   e o 03 não tem o substantivo; mas R5.12 ("Registro:"), P10, 05 ("registro de revisão", "Registro
   de decisões") e o Exemplo 7 usam "registro" como evidência de processo. A regra central de
   auditoria usa a palavra fora do único significado aprovado (P1). (b) "dia útil": 04 l. 818 "Dia em
   que a empresa funciona, de acordo com o calendário da empresa"; 05 l. 62 "Dia de segunda-feira a
   sexta-feira, exceto feriados do local da equipe". Uma empresa que trabalha no sábado mede os SLA de
   §7.4 de 2 formas. (c) "glossário do projeto" (01, 02 R5.10, 04 §7) e "glossário do produto" (05
   l. 58, 137, 337, 900, 934, 988, 998) nomeiam o mesmo artefato (P2); o 04 §7 l. 989 cita 05 §7.1 com
   o outro nome.
   **Correção:** (a) acrescentar ao 04 NT-20 `registro (de processo)`: "Evidência que uma etapa gera
   e que uma pessoa ou um sistema armazena"; renomear NT-15 para "registro do banco" ou "linha da
   tabela"; (b) manter apenas a definição do 04 e, em 05 §1, remeter a ela; (c) adotar "glossário do
   projeto" em 05 (7 ocorrências).

7. **[IMPORTANTE] 05:§7.3-§7.4 — o pedido urgente decide em 2 dias, mas publica em até 30.**
   "Decisão, pedido urgente: 2 dias úteis" (l. 973), mas "Publicação de uma inclusão aceita: Na próxima
   versão MINOR, no máximo 30 dias depois da decisão" (l. 974), e "MINOR: no máximo uma por mês"
   (l. 1060). No uso provisório, "Num aviso de segurança ou num passo com ação irreversível, a palavra
   é um desvio S1 ... Não publique o texto com a palavra pendente" (l. 962-964). Resultado: a correção
   de um runbook de incidente com palavra nova fica bloqueada até 30 dias depois de a decisão sair.
   **Correção:** linha nova em §7.4: "Publicação de uma inclusão urgente aceita: versão PATCH no mesmo
   dia útil da decisão; a próxima MINOR registra a inclusão no CHANGELOG". Em §8.1, PATCH: "Adicionar
   uma palavra com PMD urgente aceito". Ou: "a decisão urgente registrada em §7.6 vale como aprovação
   da palavra até a publicação".

8. **[IMPORTANTE] 05:§4.1, §4.5, §7.3 e 06:Exemplo 7 — os POP da própria governança e o exemplo de
   POP violam as regras de POP.** 05 §1 define POP como "procedimento de um processo da empresa, com
   mais de um responsável". Os fluxos §4.1 (redator, revisor, aprovador), §4.5 e §7.3 (solicitante,
   mantenedor) são exatamente isto, mas: não têm o bloco de R5.10 (Responsável, Entrada, Gatilho e
   prazo) e misturam responsáveis num procedimento ("Corrija os desvios. O revisor altera o estado",
   l. 285); 05 não tem nenhuma linha "Registro:" (R5.12), embora gere registros em §4.1 passos 6-9 e
   §7.3 passo 6; §7.3 tem 11 passos (R5.7: no máximo 10); o passo 6 de §7.3 lista "Rejeitado",
   "Encaminhado", "Adiado" e "Aceito", mas não o resultado "Aceito com outro significado ou outra
   classe" de §7.5 (l. 996): uma decisão sem saída, que §4.3 classifica como S1 ("Decisão sem a saída
   ..."). No 06, Exemplo 7: "Depois de 2 chamados recusados, envie o número do chamado ao gestor da
   equipe de segurança" (l. 829) não tem destino (R5.11 "Cada saída termina em um destino explícito");
   a saída de falha de "Criar as contas" (l. 876) encaminha ao analista de segurança, que não tem
   procedimento para esta entrada, e declara "O processo termina neste passo" com o colaborador sem os
   grupos; "Analisar o pedido de acesso" altera o estado do pedido e não termina com verificação (R5.9
   estendida); o passo 8 de "Criar as contas" não verifica o MFA do passo 5. No 02, os exemplos de
   R5.11 e R5.12 dizem ser o mesmo procedimento, mas o passo 2 de R5.11 já manda "clique em
   **Aprovar** e vá para o passo 3" (l. 878), e o passo 3 de R5.12 manda de novo "Clique em
   **Aprovar**" (l. 896).
   **Correção:** reescrever §4.1 como 3 procedimentos (Redator: "Pedir a revisão"; Revisor: "Revisar o
   documento"; Aprovador: "Aprovar a publicação"), cada um com o bloco de R5.10 e linhas "Registro:"
   (comentário `[RESULTADO]`, aprovação do pull request); dividir §7.3 em "Abrir um PMD" (solicitante)
   e "Decidir um PMD" (mantenedor), com a saída "Aceito com outro significado → passo 7"; no Exemplo 7,
   completar a saída do passo 5 com "O processo termina neste passo", trocar a saída de falha do passo
   8 por "volte ao passo 3; depois de 1 repetição, abra um incidente com o procedimento X", e
   acrescentar "5. Abra o chamado de novo e confirme o estado. Registro: ..." a "Analisar o pedido";
   no R5.12, trocar o passo 3 por "O portal envia o pedido à equipe de segurança." como resultado do
   passo 2.

9. **[IMPORTANTE] 05:§11 (Anexo A) × §3.2 — o teste de compreensão tem 2 resultados para 3 casos e
   não tem responsável.** O critério dá "PTS-BR igual ou melhor" (2 condições verdadeiras) e "Empate"
   (1 verdadeira). Com 0 condições verdadeiras não existe resultado. "Empate" leva a "O aprovador decide
   se o Piloto continua" (l. 1246-1247), mas o critério de saída de §3.2 (l. 206) exige "igual ou
   melhor": o aprovador não sabe se "Empate" cumpre a saída. Com 5 leitores, os grupos têm 2 e 3
   leitores; uma diferença de 1 passo decide o resultado, e o anexo não diz isto. "Igual ou melhor"
   aceita até 10% mais tempo. Nenhum papel faz o teste (o Anexo A e o Anexo B não têm responsável, e a
   RACI não tem a linha).
   **Correção:** 3 resultados: "Melhor ou igual" (2 condições), "Inconclusivo" (1), "Pior" (0);
   critério de saída de §3.2: "Melhor ou igual; ou Inconclusivo com decisão registrada do aprovador e
   um novo teste na Expansão"; "Pior" = repetir o Piloto. Linha nova na RACI: "Fazer o teste de
   compreensão e o questionário: Mantenedor R, Aprovador A". Nota: "Com menos de 10 leitores, o
   resultado é indicativo".

10. **[MENOR] 05:§9.3-§9.4 — a trilha depende de material que não existe e de um gabarito sem autor.**
    A avaliação do revisor é "classifica no mínimo 80% dos desvios como no gabarito" (l. 1169-1170), e
    a do redator é "Teste com 20 perguntas" (l. 1145); o pacote não tem o teste, o gabarito, os 3
    documentos de RV3 nem o "cartão de uma página". No início do Piloto, ninguém experiente faz o RV2
    do mantenedor ("O mantenedor faz o módulo RV2 com um revisor fundador", l. 1183) nem escreve o
    gabarito do RV3. **Correção:** em §9.4: "O mantenedor escreve o gabarito do RV3 com 3 documentos do
    06 e o aprovador registra o gabarito"; acrescentar ao critério de entrada do Piloto "O teste de 20
    perguntas e o gabarito do RV3 estão publicados em `treinamento/`".

11. **[MENOR] 05:§2.1-§2.2 — papéis sem definição e RACI incompleta.** "Outro revisor sênior decide"
    (l. 116) usa um papel que não existe; o substituto do mantenedor é o candidato natural. A RACI não
    tem as linhas "Analisar a causa e abrir ação corretiva" (§3.4 dá ao mantenedor), "Verificar a
    eficácia da ação corretiva" (ausente em todo o 05; ISO 9001 §10.2.1 d) e a coluna "Auditor" (aparece
    como "R (auditor)" na coluna Revisor). A linha "Auditar a amostra trimestral" não cobre a auditoria
    mensal do Piloto e da Expansão. O registro `auditorias/AAAA-TN.md` só tem nome para trimestre.
    **Correção:** trocar "revisor sênior" por "o substituto do mantenedor"; coluna "Auditor"; linhas
    novas; acrescentar à tabela de §3.4 "Eficácia: o auditor verifica cada ação corretiva na próxima
    auditoria"; nome do arquivo `auditorias/AAAA-MM.md`.

12. **[MENOR] 05:§6.2 × `tools/` — a pasta tem scripts que o 05 não descreve.** 05 l. 18: "Este
    documento descreve apenas as ferramentas que existem na pasta `tools/`". A pasta também tem
    `check04.py`, `check_a.py`, `cobertura.py`, `naousadas.py` (com o caminho absoluto
    `/Users/<usuário>/...` no código), `fix1.py` e `fmt.py` (scripts de uma vez que alteram a
    especificação) e `__pycache__/`. Para controle de informação documentada (ISO 9001 §7.5.3), o
    pacote publicado tem artefatos sem dono nem função declarada. **Correção:** remover os scripts de
    uma vez e `__pycache__`; manter o `check04.py` (ver problema 5) com caminho relativo e descrever o
    script em §6.2.

13. **[MENOR] 05:§3.3, §6.4, `.vale.ini` — detalhes de gate.** O critério de entrada da Expansão
    (l. 221) diz "M6 de no máximo 5%" sem o "medido com no mínimo 50 alertas" de §6.4 (l. 740). O
    `.vale.ini` ativa `FraseLongaProcedimento` só em `docs/{procedimentos,runbooks}`; um POP exportado
    pelo fluxo de §4.5 fica com o limite de 25 palavras. **Correção:** copiar a condição de 50 alertas
    para §3.3; em §4.5 passo 3, "Execute o linter com `--limite-frase auto`" (o `check_spec.py` já
    aplica 20 palavras aos itens numerados).

14. **[MENOR] 03, 04, 06 e 05 §4.5 — versão.** 03 l. 3, 04 l. 3, 06 l. 5: "versão 1.0"; 05 l. 498:
    `pts-br: 1.0` sem aspas, contra `pts-br: "1.0"` de §8.4 e CK-0.1. **Correção:** "Versão 1.0.0" nos
    3 cabeçalhos (`tools/intro.md` para o 03); `pts-br: "1.0"` em §4.5.

## O que levaria a nota a ≥ 8

1. Tornar o resultado da revisão e as métricas auditáveis: tabela de §4.4 sem sobreposição e com
   CK-0.1 em todos os resultados; momento de medição de M1/M2; alertas por regra no registro (M6);
   colunas de data e urgência em §7.6 (M7) (problemas 1 e 2).
2. Fazer a governança seguir as regras de POP que ela mesma criou: §4.1, §4.5 e §7.3 com o bloco de
   R5.10, linhas "Registro:", no máximo 10 passos e todas as saídas; Exemplo 7 sem saídas sem destino
   (problema 8). Hoje o 05 reprova no CK-5.9 (S1) pela própria escala.
3. Fechar os impasses e lacunas de independência: auditor do Piloto, auditoria do mantenedor, eficácia
   das ações corretivas, resultados do Anexo A (problemas 3, 9 e 11).
4. Caminho de publicação rápida para PMD urgente (problema 7) e gate de publicação honesto: testes
   com o Vale executados ou versão como release candidate (problema 4).
5. Autoconformidade com D9 e termos de processo com um significado: `registro`, `dia útil`, glossário
   do projeto; `check04.py` no gate de §8.5 (problemas 5 e 6).

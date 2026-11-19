---
lente: processos
rodada: 1
notas: {correcao: 6, completude: 6, aplicabilidade: 6, coerencia: 5, valor: 7}
nota_final: 6.0
---

Lente: BPM, qualidade (ISO 9001), governança de documentação, POP e adoção de padrões.
Verificações objetivas feitas com scripts (não editam a especificação):
- `scratchpad/naousadas.py`: procura as formas das 298 entradas "Não aprovada" do 03 no texto
  em prosa do README e de 01, 02, 04, 05 e 06 (seções PTS-BR). Ignora blocos de código, código
  em linha, trechos entre aspas e os exemplos "Não aprovado".
- `scratchpad/cobertura.py`: cruza as regras R1.1–R10.8 de 02 com o checklist CK-x de 05, a
  marca `[lint]` com as regras Vale de 05 §6.3 e as referências "(ver X.Y)" de 05 com os
  títulos reais.

## Pontos fortes (até 5)

1. **Rastreabilidade checklist → regra completa.** As 73 regras de 02 têm item de checklist
   em 05 §4.2 (zero regra órfã, verificado por script). A coluna "Regras" e a frase "Se o item
   e a regra divergem, vale a regra" dão uma hierarquia documental clara (05 l. 10-12 e 250-251).
2. **Critério de aprovação objetivo e auditável.** 05 §4.4: três resultados com condições
   booleanas, limite de exceções S2 por 1.000 palavras por fase, regra de arredondamento com
   exemplo calculado ("400 × 3 / 1.000 = 1,2, arredondado para 2"). A regra de subir S2 para S1
   em aviso ou ação irreversível (§4.3) é o tipo de regra que um auditor consegue aplicar.
3. **Adoção em fases com critérios de entrada e saída.** Piloto, Expansão e Padrão têm gates
   mensuráveis (≥ 15 documentos, zero S1, falsos positivos ≤ 20%, 90% de PMD no SLA) e um dono
   da decisão (o aprovador, RACI §2.2). A política de legados (§3.4) é realista: risco primeiro,
   conversão na alteração.
4. **Segregação de funções.** "O redator e o revisor de um documento são pessoas diferentes" e
   "O mantenedor não decide um PMD que ele mesmo abriu" (05 §2.1). Substituto do mantenedor
   para evitar ponto único de falha.
5. **Métricas com limitações declaradas.** M4 (Flesch adaptado) vem com 6 limitações e com a
   proibição de uso como critério de aprovação (05 §5.5); M3 é medido na submissão e na
   publicação, o que separa aprendizado do redator de qualidade entregue.

## Problemas (ordenados por impacto)

1. **[BLOQUEANTE] 05:§3.2 × §9.3 — impasse de partida (bootstrap) na adoção.** O critério de
   entrada do Piloto exige "No mínimo 2 revisores concluíram a trilha de revisor". O
   pré-requisito da trilha do revisor é "trilha do redator concluída e 5 documentos aprovados
   como redator" (§9.3). Antes do Piloto não existe documento PTS-BR aprovado nem revisor que
   possa aprová-lo. Uma organização que segue o texto à letra não consegue começar.
   **Correção:** acrescentar em §9.3: "Exceção de partida: antes da fase Piloto, o mantenedor e
   até 3 revisores fundadores fazem a trilha do revisor sem o pré-requisito de 5 documentos. O
   mantenedor revisa os 5 primeiros documentos de cada revisor fundador durante o Piloto." e
   ajustar o critério de entrada do Piloto para citar "revisores fundadores".

2. **[BLOQUEANTE] 01:§8.2 × 05:§6.3 — o revisor delega ao linter 48 regras que o linter não
   tem.** 01 §8.2 manda: "Verifique primeiro as regras sem a marca `[lint]`. O linter verifica
   as outras regras." 02 marca 54 regras com `[lint]`; 05 §6.3 entrega regra Vale para só 6
   (R1.1, R1.8, R3.4, R3.5, R3.6, R4.2). Resultado: 48 regras (por exemplo R5.1, R5.2, R7.3,
   R8.5, R9.1) ficam sem verificação de ninguém, e 05 §6.7 diz o contrário ("Zero alertas no
   linter não significa conformidade"). Para auditoria isso é falha de controle.
   **Correção:** (a) em 02, separar a marca em `[lint]` (regra implementada no pacote de regras
   da versão) e `[lint-possível]`; (b) em 05 §4.2, a coluna "Verificação" passa a dizer "L"
   só para regras com arquivo Vale publicado, com o nome do arquivo; (c) em 01 §8.2, trocar por
   "Verifique cada item do checklist de 05 §4.2. O linter só substitui o revisor nos itens com
   verificação L."

3. **[IMPORTANTE] 05 (texto inteiro), 02 e 01 — a especificação não segue o próprio
   dicionário.** O script encontrou ~80 ocorrências de palavras "Não aprovada" na prosa de 05,
   ~135 em 02 e ~35 em 01. Exemplos reais de 05: "4. Espere o resultado do linter no CI."
   (l. 237; `esperar` não aprovado, use AGUARDAR — o CHANGELOG diz que "esperar" já foi
   corrigido); "irreversível: apagar dados" (l. 363; use EXCLUIR — também listado como
   corrigido); "ação errada" (l. 357; use INCORRETO); "Concede exceções S2" e a linha RACI
   "Conceder exceção S2" (`conceder` → DAR); "Rode o linter", "roda" 7× (`rodar` → EXECUTAR);
   "subir a severidade" 3× (`subir` não aprovado); "atingem as metas" (`atingir` → CHEGAR).
   Em 02, 15 títulos de regra usam "só" (`só` → APENAS), a começar pelo próprio
   "R1.1 Use só palavras aprovadas". Um auditor que aplica o CK-1.1 ao próprio padrão reprova o
   padrão; isso mina a credibilidade na adoção.
   **Correção:** rodar o mesmo script de vazamento de `tools/build.py` sobre a prosa de todos
   os arquivos (não só sobre os exemplos, como diz o CHANGELOG), corrigir as ocorrências e
   adicionar esse passo como gate de release em 05 §8 ("nenhuma versão é publicada com palavra
   não aprovada fora dos exemplos 'Não aprovado'").

4. **[IMPORTANTE] 02:Seção 5 e 01:§2.1 — procedimentos servem para runbook, não para POP de
   processo de negócio.** A Seção 5 assume um único executor ("você"), passos técnicos e
   verificação de sistema: R5.9 só exige verificação "Se o procedimento alterar um sistema
   (deploy, migração, configuração ou permissão)"; R5.8 trata de blocos de código. Faltam
   regras para o que um POP/BPM precisa: (a) responsável por procedimento quando há vários
   papéis; (b) passagem de bastão entre papéis (entrada que um papel recebe de outro);
   (c) ponto de decisão com os dois caminhos (aprovado/recusado); (d) registro ou evidência que
   o passo gera; (e) gatilho e prazo ("até o 5º dia útil do mês"); (f) caminho de exceção com
   saída (escalonamento). O Exemplo 7 de 06 mostra as lacunas: 3 papéis, mas só 2
   procedimentos — o analista de segurança não tem procedimento e o caminho "pedido recusado"
   não existe; o passo 7 manda "volte ao passo 4" sem limite de repetições nem escalonamento.
   01 §2.1 nem lista "procedimentos de processos de negócio / instruções de trabalho" como
   texto no escopo, e 05 §3.1 não os coloca em nenhuma fase.
   **Correção:** criar R5.10 "Escreva o papel que executa o procedimento antes de 'Antes de
   começar'" (formato fixo: "**Executor:** <papel do glossário>"), R5.11 "Escreva cada decisão
   como sublista com todas as saídas, e cada saída termina em um passo, outro procedimento ou
   o fim do processo" e R5.12 "Escreva o registro que o passo gera" (formato: "Registro: <nome
   do artefato NT-20>"); estender R5.9 para "alterar um sistema, um registro ou o estado de um
   pedido"; adicionar a linha "Procedimentos de processos da empresa (POP, instrução de
   trabalho)" em 01 §2.1 e na ordem 3 de 05 §3.1; completar o Exemplo 7 com o procedimento do
   analista de segurança e o caminho de recusa.

5. **[IMPORTANTE] 03/04 — vocabulário de processos ausente, e o exemplo muda o requisito para
   caber no dicionário.** Não há entrada em 03 nem em 04 para: dia útil, colaborador, gestor,
   cargo, setor, departamento, auditoria, conformidade, desvio, exceção, meta, indicador,
   evidência, trimestre, mensal, anual, rejeitar, devolver, ação corretiva, causa raiz. Os
   termos centrais de 05 (conformidade, desvio, exceção) só existem na tabela local de 05 §1.
   O Exemplo 7 troca "antecedência mínima de 5 dias úteis" por "1 semana ou mais" — outro
   requisito (feriados, contagem de dias); ao mesmo tempo, 05 usa "dias úteis" 6 vezes nos
   próprios SLA (l. 225, 484, 506, 875-877). Num POP, trocar o prazo para obedecer ao
   vocabulário é um defeito S1 pela própria definição de 05 §4.3.
   **Correção:** adicionar a 03 `DIA ÚTIL (s)`, `TRIMESTRE (s)`, `PRAZO` já existe; adicionar
   ao glossário-base de 04 (NT-19/NT-20/NT-21) colaborador, gestor, auditoria, conformidade,
   desvio, exceção, evidência, meta, indicador, ação corretiva, causa raiz; restaurar "5 dias
   úteis" no Exemplo 7; acrescentar a 05 §7.5 a regra "Um PMD nunca é rejeitado com a
   alternativa de alterar um requisito de negócio".

6. **[IMPORTANTE] 05:§7.4 × §8.1 — SLA de publicação contradiz o versionamento.** §7.4:
   "Publicação de pedido aceito: Na próxima versão MINOR, no máximo 30 dias depois da
   decisão". Mas §8.1 classifica "Alterar o significado aprovado de uma palavra" e "Remover uma
   palavra aprovada" como MAJOR, com "no máximo uma por ano". Um PMD de alteração ou remoção
   aceito não consegue cumprir o SLA.
   **Correção:** dividir a linha do SLA: "Inclusão aceita: próxima MINOR, no máximo 30 dias.
   Alteração ou remoção aceita: marcar como obsoleta na próxima MINOR (30 dias) e efetivar na
   próxima MAJOR."

7. **[IMPORTANTE] 05:§7.3 e §6.2 — o fluxo de manutenção do dicionário não descreve a fonte
   real.** 05 §6.2 diz que `PalavrasNaoAprovadas.yml` é gerado do `03-dicionario.md` e que
   "Assim o dicionário é a única fonte". Na prática, o 03 é gerado por `tools/build.py
   --render` a partir de `tools/d1.txt`, `d2.txt`, `d3.txt` e `intro.md`; uma edição manual do
   03 some no próximo build. O passo 7 de §7.3 ("O mantenedor inclui a mudança na próxima
   versão e atualiza o linter") não manda editar o `d*.txt`, rodar as verificações do
   build.py (duplicata, alternativa inexistente, vazamento) nem regenerar a regra Vale.
   **Correção:** reescrever o passo 7 em 4 passos: "7. Edite a entrada em `tools/d*.txt`.
   8. Execute `python tools/build.py` e corrija cada linha PROBLEM. 9. Gere o 03 com
   `--render`. 10. Gere `PalavrasNaoAprovadas.yml` e execute os testes do repositório de
   regras." e corrigir §6.2: "A fonte única são os arquivos `tools/d*.txt`."

8. **[IMPORTANTE] 05:§4.1 e §5.4 — M3 "na publicação" e o limite de exceções não são
   calculáveis a partir do registro definido.** O único formato obrigatório é
   `[S2][R4.2] <descrição>`, e "Um script conta os desvios a partir desses comentários". O
   formato não diz se o desvio foi corrigido, virou exceção aprovada (e por quem) ou ficou
   aberto como S3. Sem isso, M3 na publicação, o limite de exceções por fase (§4.4) e a
   auditoria trimestral dependem de leitura manual de cada PR.
   **Correção:** definir o estado no registro: `[S2][R4.2][ABERTO]`, `[CORRIGIDO]`,
   `[EXCEÇÃO: aprovado por @papel]`; o script de M3 conta só os estados finais; o resultado da
   revisão (§4.1, passo 8) vira um comentário fixo
   `[RESULTADO: Aprovado com exceções][S2-exc: 2][palavras: 640][min: 25]`.

9. **[IMPORTANTE] 05:§3.2-§3.4 — critérios de fase com instrumento indefinido.** (a) "O teste
   de compreensão mostra resultado igual ou melhor": sem protocolo (tarefa, medida — acerto?
   tempo? erros? —, n = 5 leitores, critério de empate). (b) "A pesquisa com redatores mostra
   que no mínimo 70% consideram o processo viável": sem questionário nem escala. (c) "No
   mínimo 80% dos documentos publicados atingem as metas da fase Piloto (ver 5.7)": as metas
   de §5.8 misturam métricas por documento (M1, M2, M3) e por processo (M5 ciclo, M6, M7) e
   incluem "Medir linha de base", que não é meta. (d) A auditoria trimestral só define ação
   para S1 publicado; não há critério de aceitação da amostra, tratamento de S2 publicado sem
   exceção, nem independência do auditor (o mantenedor audita regras, treinamento e métricas
   que ele mesmo mantém — contra o princípio de ISO 9001 §9.2).
   **Correção:** anexar a 05 um "Protocolo do teste de compreensão" (tarefa por runbook,
   medida = % de passos executados sem erro + tempo, 5 leitores por versão em ordem
   alternada, critério "acertos PTS-BR ≥ acertos original"); um questionário de 5 itens em
   escala 1-5 com "viável = média ≥ 4"; trocar o critério (c) por "≥ 80% dos documentos
   cumprem M1, M2 e M3 da fase; M5, M6 e M7 cumprem a meta no agregado"; na auditoria,
   "critério: ≥ 90% da amostra 'Aprovado' na reauditoria; um revisor de outra equipe audita;
   cada S2 publicado sem exceção abre uma ação corretiva com prazo de 20 dias úteis".

10. **[IMPORTANTE] 05 (§4.1, §6.5) — governança só para docs-as-code.** O fluxo inteiro
    depende de pull request, CI, GitHub Actions e Vale. POPs e procedimentos de processo
    costumam viver em Confluence, SharePoint ou num sistema de gestão da qualidade. Não há
    fluxo equivalente nem lugar para guardar o registro da revisão (requisito de informação
    documentada, ISO 9001 §7.5), nem prazo de retenção.
    **Correção:** acrescentar §4.5 "Documentos fora do Git": o revisor preenche uma tabela de
    revisão (mesmos campos do comentário do PR), anexada à versão do documento; o linter roda
    sobre a exportação em Markdown; retenção do registro = vida do documento + 1 ano.

11. **[IMPORTANTE] 05:§3.2 l. 170 e §3.3 l. 199 — referência cruzada errada.** "atingem as
    metas da fase Piloto (ver 5.7)" e "metas da fase Expansão ... (ver 5.7)": §5.7 é
    "Métricas complementares"; as metas estão em §5.8. São exatamente os critérios de saída de
    fase. **Correção:** trocar "5.7" por "5.8" nas duas linhas.

12. **[IMPORTANTE] 05:§4.3 × §4.2 — S1 inclui defeito que o checklist exclui.** §4.3 dá como
    exemplo de S1 "Comando incorreto", mas §4.2 diz "O checklist PTS-BR verifica a linguagem. A
    exatidão técnica (comandos e valores testados ...) fica com a revisão técnica" e o
    CHANGELOG removeu CK-9.2 (comandos testados). O revisor PTS-BR não sabe se deve ou não
    reprovar por comando incorreto. **Correção:** trocar o exemplo por "Comando com dois
    significados possíveis" e acrescentar: "Um comando incorreto é defeito da revisão técnica,
    fora da escala S1-S3."

13. **[IMPORTANTE] 05:§3.2 × §6.6 — linha de base exige ferramenta que não existe.** O critério
    de entrada do Piloto exige linha de base M1 a M5 em 20 documentos. M2 e M4 dependem do
    `metricas.py`, descrito (§6.6) mas não entregue, sem dono e sem prazo; M3 e M5 de
    documentos legados exigem revisar 20 documentos com o checklist antes de qualquer
    treinamento terminar. **Correção:** acrescentar critério de entrada "o `metricas.py` e o
    pacote de regras Vale estão publicados com testes `deve_alertar`/`nao_deve_alertar`" e
    definir a linha de base de M3/M5 como "revisão de 20 documentos legados pelos revisores
    fundadores, com o checklist".

14. **[MENOR] 05:§7 — PMR sem formulário, SLA nem critério.** PMR aparece em §1, na RACI, na
    calibração (§9.3) e nos riscos (§10), mas só tem "Use o mesmo registro, com prefixo PMR".
    **Correção:** acrescentar §7.7 com formulário (regra, problema, 2 exemplos reais, proposta,
    impacto MAJOR/MINOR/PATCH) e SLA (triagem 5 dias úteis, decisão 20 dias úteis).

15. **[MENOR] 05:§7.3 "Uso provisório" × §4.3.** A palavra pendente vale como exceção S2, mas
    num passo irreversível ela sobe para S1, que "nunca tem exceção"; o pedido urgente só cobre
    "aviso de segurança ou a correção de um incidente". **Correção:** estender o pedido urgente
    a "passo com ação irreversível".

16. **[MENOR] 01:§8.2 e §8.5 × 05:§4.3.** 01 manda classificar cada problema como "violação de
    regra, palavra fora do dicionário ou pedido de termo novo" (taxonomia diferente de S1-S3) e
    diz que "Um desvio de uma regra precisa de um registro com ... o nome do aprovador", mas S3
    não precisa de exceção em 05. **Correção:** em 01, remeter só a 05 §4.3 e remover a
    taxonomia paralela.

17. **[MENOR] README, CHANGELOG, 05 §8.4 — identificação de versão inconsistente.** README e 05
    dizem "Versão 1.0"; o CHANGELOG só tem `[1.0.0-rc1]`; 05 §8.1 exige MAJOR.MINOR.PATCH; o
    cabeçalho dos documentos usa `pts-br: "1.0"`. O critério de entrada do Piloto ("A versão
    1.0 da especificação está publicada") não é verificável. **Correção:** publicar a entrada
    `[1.0.0]` no CHANGELOG, usar "1.0.0" em todos os cabeçalhos e definir em §8.4 que o
    documento declara MAJOR.MINOR.

18. **[MENOR] 05:§4.2 — CK-5.4 marcada só "H", mas R5.4 tem `[lint]`; o critério "Versão do
    PTS-BR declarada" (§4.4) não tem item de checklist.** **Correção:** CK-5.4 → "L+H";
    acrescentar CK-0.1 "O cabeçalho declara `pts-br`?" com verificação L.

## O que levaria a nota a ≥ 8

1. Resolver os dois bloqueantes: cláusula de revisores fundadores (item 1) e marca `[lint]`
   ligada a regras Vale realmente publicadas, com 01 §8.2 corrigido (item 2).
2. Aplicar o próprio dicionário à prosa de 01, 02 e 05, com o script de vazamento como gate de
   release (item 3). Hoje o padrão não passa no próprio CK-1.1.
3. Tornar a Seção 5 utilizável para POP: executor, decisões com todas as saídas, registro
   gerado, prazos; vocabulário de processos em 03/04; Exemplo 7 completo e sem alterar o prazo
   de negócio (itens 4 e 5).
4. Fechar o ciclo de auditoria e métricas: registro com estado do desvio, protocolo do teste de
   compreensão, critério da auditoria com ação corretiva e auditor independente, referências
   "5.7" → "5.8", SLA × semver (itens 6, 8, 9, 11).
5. Descrever o fluxo real de manutenção do dicionário (`d*.txt` → `build.py` → 03 → regra Vale)
   e um fluxo para documentos fora do Git (itens 7 e 10).

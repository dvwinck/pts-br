# Decisões para a revisão da rodada 4 (vinculantes)

Rodada 3: processos 7,8 · tecnologia 8,2 · desenvolvimento 7,9 · documentação 7,9 → média 7,95 (meta ≥ 8).
Avaliações: `reviews/round-3/*.md`. DECISOES-R2 e R3 continuam válidos onde este arquivo não muda nada.
Mesma propriedade de arquivos da rodada 3 (A: 01/02 · B: fontes do 03 + 04 · C: 05, README, CHANGELOG,
tools exceto build.py · D: 06). Depois: varredura final.

## Decisões
G1. **Sentido, não só forma (documentação).** Cada palavra do texto normativo usa o sentido aprovado.
    B decide e corrige as definições citadas em `round-3/documentacao.md` (NOVO, FORMA, HORA, USO, DAR ×
    ATRIBUIR, GRAVE, MAIOR/MENOR, ABERTURA × ABRIR e as outras 12), escolhendo o sentido que o texto já
    usa quando ele for válido para um texto técnico (menos reescrita). Regras fixas:
    - "execute o passo" → "faça o passo" (EXECUTAR = programa, comando, script).
    - "pode" = capacidade ou permissão; possibilidade → reescrever ("talvez" não é aprovado: use
      "Se X, …" ou dê o valor/condição).
    - HORA = momento do dia ("às 14:00 UTC-03:00"); duração usa o símbolo "h".
    - O CHANGELOG descreve o USO final como ele ficar no 03.
    A, C e D corrigem os ~45 usos fora do sentido nos próprios arquivos (lista em `round-3/documentacao.md`).
G2. **Medição honesta.** `--lista-branca` conta o termo composto do 04 como unidade (não aceita as partes
    soltas fora do termo). CHANGELOG e 05 dizem que a lista branca verifica a forma, não o sentido, e
    que o sentido é item do revisor. A tabela de níveis do 02 R7.1 e do 03 D8 tem o MESMO texto (copie a
    do 02; a regra do RPO tem uma só leitura).
G3. **Ex9 e operações (D, A).** Ex9: `pg_dump` do estado atual antes de `pg_restore --clean`; backup
    escolhido pela hora anterior à migração com defeito (não pela hora da detecção); verificação na tabela
    afetada; `pg_restore --list` antes; checagem e encerramento de outras sessões; `ANALYZE` depois; cada
    saída de falha diz o estado do serviço (parado) e escala para outra equipe definida; comandos rodam de
    um host de administração (bastion), não do servidor de backup, com credencial de menor privilégio.
    `.pgpass` com permissão 600 (Ex2, Ex5, Ex9). R7.9 sem `PGPASSWORD`. R7.8 ganha tabela "opção de alvo
    por ferramenta" (kubectl `--context`, helm `--kube-context`, psql `--host`/`--dbname`, aws `--profile`,
    terraform workspace). Ex1: `kubectl auth can-i patch`. Nova R5.13 "Inclua o procedimento de reversão
    em todo procedimento que muda produção" (A) + item no checklist (C). D inclui um Ex10 curto de
    comunicado de incidente (status page) se couber com qualidade.
G4. **Fluxo de aprovação (C).** Estado `EXCECAO-PEDIDA` e procedimento "Decidir uma exceção S2" antes do
    resultado; todos os POP do 05 seguem R5.10–R5.12: retorno ao passo de revisão depois de "Reprovado",
    saída "sem resposta no prazo" em toda espera, PMD "Pendente" com a issue aberta, procedimento do
    redator para corrigir desvios, procedimento do aprovador no §4.5. M1/M2 com registro durável por
    documento (o CI executa `--metricas` e grava os campos; uma palavra conta uma vez). Estado "obsoleta"
    real nas fontes e no build (B implementa no build.py; C usa no gerador e no 05). Caminho de publicação
    para mudanças no 04. Qualificação de revisor de equipe nova na Expansão (mentoria por revisor
    qualificado). Anexo A coerente com o critério do Piloto. Licença: CC BY 4.0 decidida (não "sugerida");
    a tag `v1.0.0` é criada na publicação (dizer isso, não afirmar que existe).
G5. **Automação para equipes e UX (C).** Dizer que as regras atuais NÃO foram testadas no Vale (apenas a
    versão da rodada 2); `--config <.vale.ini>` lido pelo Python (MinAlertLevel, pastas, BasedOnStyles);
    `--glossario <arquivo>` para o glossário do projeto; `--mensagens <arquivo.json|.po>` que extrai as
    strings de UI e aplica uma regra `Mensagens` (plural com "(s)", placeholder posicional `%s`/`{0}`,
    "com sucesso!", "Erro desconhecido", ponto de exclamação) com testes.
G6. **Vocabulário de interface (B).** PERFIL (s) aprovado no 04 NT-05 = página ou dados da conta de um
    usuário; "perfil de acesso" continua não aprovado. SETA (tecla/ícone) e RODA (do mouse) aprovados no
    04 NT-06; o gerador não gera forma não aprovada que seja igual a uma palavra aprovada (C). BUSCA (s) =
    campo ou ação de procurar na interface. Inclua as palavras de interface ausentes listadas em
    `round-3/desenvolvimento.md` (convite, lápis, etc.).

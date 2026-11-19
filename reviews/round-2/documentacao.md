---
lente: documentacao
rodada: 2
notas: {correcao: 7.5, completude: 7, aplicabilidade: 7.5, coerencia: 6.5, valor: 8.5}
nota_final: 7.4
---

Método: leitura integral de README, 01, 02 (as 81 regras e a tabela-resumo), 06 (exemplos 1, 2, 4,
5, 6, 7 e 8; o 3 por amostra) e CHANGELOG; 04 nas seções 1, 2, 3 (NT-18 a NT-25), 4.1, 4.2.A–B,
5.5, 6.1, 6.2 e 6.3; 05 por busca dirigida. 03: extração das 878 entradas por script, amostra
estratificada de 84 entradas (3 aprovadas e 1 não aprovada por letra, semente 2026), as 89
entradas novas desde a rodada 1 e cerca de 120 entradas consultadas pelo nome. Scripts em
`scratchpad/r2doc/`: `parse_dic.py` (tabela do 03 → JSON), `lex.py` (léxico: aprovadas do 03 +
nomes e verbos técnicos do 04 + NT-25 + metalinguagem do 01 §11.2), `lexcheck.py`/`absent.py`
(palavras não aprovadas e palavras ausentes do 03 e do 04 no texto normativo, com exclusão de
código, aspas, negrito, blocos "Não aprovado", textos "Antes" e colunas de tabela ignoradas),
`gram.py` (padrões de R1.10, R3.1, R3.7, R3.8, R4.3, R8.3, R8.4, R9.4), `dicscan.py` (regras
aplicadas às colunas de significado e de exemplo do 03), `sentlen.py` (R4.2). O
`check_spec.py --spec` mostra 0 alertas; o meu verificador mostra o que o linter não procura.

## Status dos problemas da rodada 1

| # | Problema da rodada 1 | Status | Evidência |
|---|---|---|---|
| 1 | 6 contradições 02 × 03 | **Resolvido** | ABAIXO/ACIMA aprovados só para o elemento adjacente (03 L279, L290) e R9.4 alinhada; "a seguir" não aprovada nos 2 arquivos. FICAR = "Começar a estar em um estado novo" (03 L676) e R3.9 aprova FICAR. PODER = "capacidade ou permissão" (03 L967), contraexemplos corrigidos. R4.3 sem "haver" ("O log tem 3 erros."). ATENÇÃO/CUIDADO do 03 começam pela instrução (L362, L488). R10.4: "O sistema não gravou o pedido." |
| 2 | Texto da especificação fora do PTS-BR | **Parcialmente resolvido** | As palavras da lista "Não aprovada" sumiram do texto normativo ("só", "esse", "Rode", "1.000", "o leitor executa"): `check_spec.py --spec` = 0 e o meu `lexcheck.py` também acha só menções. A metalinguagem foi declarada (01 §11.2 e 04 NT-25). Mas ficam ~400 palavras gerais ausentes do 03 e do 04 (D9: "não é aprovada"), 31 números por extenso, 7 usos de "acima/abaixo" para comparar valores, ponto e vírgula no 04 e outros desvios (problemas 1 e 5 abaixo). |
| 3 | 14 entradas com 2 significados | **Resolvido** | REDEFINIR, HORA, LINHA, SUPORTE, USO, NOVO, FORA DE, VER, TEMPO, ÚNICO e TER têm 1 definição; `build` (processo) e `artefato` (resultado) separados no 04 L764/L781; CLICAR "em um botão" (04 §4.2.A). PEDIDO virou "Mensagem ou registro em que uma pessoa pede algo [...] por exemplo um acesso ou uma compra" (03 L944): aceitável, mas "registro" na definição cria o problema 3 abaixo. |
| 4 | Homografia "para" (PARAR × preposição) | **Resolvido** | R1.10 nova, com 3 saídas de reescrita e o "Aprovado" "Quando a fila fica cheia, o serviço para."; nota em 03 D6. |
| 5 | Justificativa errada do subjuntivo; casos sem forma | **Resolvido (a regra)** | R3.2 e 01 §5.2 trazem as 3 formas (futuro do subjuntivo, "quando" + presente, "se" + pretérito perfeito), o infinitivo flexionado depois de "até"/"antes de" e a justificativa correta ("As 3 formas são corretas na norma"). Os exemplos do próprio pacote não seguem a divisão (problema 4 abaixo). |
| 6 | Estado de versão anterior | **Resolvido** | R3.1: "escreva a versão como sujeito, no presente"; R3.1 e 06 ex. 6 usam "A versão 2.9.4 envia [...] 2 vezes". |
| 7 | Palavras básicas ausentes; vocabulário pequeno | **Parcialmente resolvido** | Entraram NADA, TUDO, QUEM, SIM, PRÓPRIO, PEQUENO, JUNTO, DIZER, SIGNIFICAR, CONHECER, SOLTAR, NINGUÉM, ALGO e as não aprovadas desejar, cadastrar, estabelecer, principalmente, demais, ele, terceiro, mencionar, tornar-se, ocasionar (562 aprovadas, eram 494). Ainda ausentes: "dentro (de)" (24 usos no texto, inclusive em R1.1), "pergunta" (22 usos, R7.1 e R10.6), "coisa" (usada nas definições de NADA, ALGO, TUDO), "perto", "volta", "meio", "começo", "além de", "difícil". |
| 8 | Exemplos do 03 com número/unidade por extenso | **Resolvido** | `dicscan.py`: 0 números por extenso e 0 unidades por extenso nas colunas de exemplo; RESTAURAR usa "backup de 2026-11-17"; `build.py` L302–L312 verifica R8.4 e parte de R9.4. |
| 9 | Crase incompleta | **Resolvido** | R1.6: horas ("à 01:00"), "à direita/à esquerda", sem crase antes de verbo, masculino, literal e "partir". |
| 10 | R8.5 ISO × "UTC-3" | **Resolvido** | "09:30 UTC-03:00" em R8.5, 01 §5 e 06. |
| 11 | Heurística de R4.5 | **Resolvido** | Lista fechada: "impossível", "incomum", "inválido", "indisponível", "incorreto". |
| 12 | 4 desvios no 06 | **Resolvido** | (a) "5 dias úteis ou mais"; (b) "Reverter o deploy" é um procedimento com fim em cada saída; (c) a tabela do ex. 4 põe a causa em outra frase; (d) o dado de 100 000 CPF está no Contexto do ex. 8. |
| 13 | R5.6 sem substantivo de classe; R6.3 sem ENQUANTO/NEM | **Resolvido** | "Instale a ferramenta `kubectl`"; R6.3 lista "nem" e "enquanto". |
| 14 | Definições circulares; exemplo de D2 | **Resolvido** | TER "Conter algo como parte ou como característica"; SER "Indicar a identidade [...]"; D2 tem "O sistema vai enviar um e-mail quando o build terminar." |

Resumo: 12 resolvidos, 2 parcialmente resolvidos (2 e 7), 0 não resolvidos.

## Pontos fortes (até 5)

1. **As contradições da rodada 1 foram todas resolvidas, e a solução é linguisticamente boa.**
   R3.2 agora descreve a gramática real do português (3 formas corretas, uma para cada tipo de
   condição) e resolve "até que"/"antes que" com o infinitivo flexionado ("Antes de os testes
   terminarem", sem a contração, como pede a norma). R1.10 trata a homografia "para" com
   saídas concretas. R3.9 com FICAR para mudança de estado é uma decisão melhor que a proibição
   anterior: é o verbo que o leitor brasileiro usa.
2. **R7.1 virou um procedimento de decisão verificável.** As 3 perguntas em ordem, com
   "Use o nível da primeira resposta 'sim'", e a definição de "recuperação conhecida" (backup,
   reprocessamento, nova indexação, rollback, volta automática) dão o mesmo nível a redatores
   diferentes. A nota de R7.5 ("ATENÇÃO, não PERIGO: [...] a duração é conhecida e o sistema
   volta de forma automática") ensina o critério.
3. **As regras novas de processo e de desenvolvimento têm formato fixo e exemplos completos.**
   R5.10–R5.12 (bloco Responsável/Entrada/Gatilho e prazo, saídas com destino, frase
   "Registro:"), R7.8 (passo que mostra o alvo + opção explícita `--context`), R7.9 (prompt,
   variável do cofre, arquivo com permissão) e R10.9–R10.10 (validação, `aria-label`, ajuda de
   CLI no presente da 3ª pessoa, log no pretérito perfeito) vão além do ASD-STE100 e são o
   que uma equipe brasileira de software precisa.
4. **O 06 é material de treinamento de alto nível.** O ex. 1 verifica o cluster com
   `kubectl cluster-info --context` antes do deploy, registra o `REVISION` para o rollback e
   fecha cada saída; o ex. 2 separa `pg_cancel_backend` e `pg_terminate_backend` com um aviso
   para cada um; o ex. 7 dá 1 procedimento por responsável, com prazo e registro na tabela de
   abertura. Os 3 textos seguem as regras novas e são tecnicamente corretos.
5. **A frase está sob controle.** O `sentlen.py` contou ~2 640 frases em prosa (README, 01, 02,
   04, 05, 06); fora das tabelas, só 3 passam do limite de R4.2 (02 L1122 com 26 palavras;
   README L58 e 05 L945 com 21 palavras em passo). O 03 deixou de ter números e unidades por
   extenso, e o `build.py` passou a verificar os exemplos.

## Problemas (ordenados por impacto)

1. **[BLOQUEANTE] CHANGELOG "Corrigido" e 01 §11.1 — a autoconformidade foi medida só contra a
   lista de palavras "Não aprovada"; as palavras ausentes do 03 e do 04 não foram verificadas.**
   O CHANGELOG diz: "o README, o 01, o 02, o 04, o 05 e os textos PTS-BR do 06 usam apenas
   palavras aprovadas". Mas o 03, regra D9, diz: "Se uma palavra geral não estiver neste
   dicionário, a palavra não é aprovada", e o `PalavrasNaoAprovadas.yml` é uma lista negra de
   316 entradas. O `absent.py` (com morfologia, NT-25 e a metalinguagem de 01 §11.2 aceitas)
   encontrou cerca de 1 180 ocorrências de cerca de 480 palavras ausentes (por amostra de 60,
   ~15% são falsos positivos de flexão): 05 = 504, 02 = 391, 01 = 172, 06 = 72, README = 26,
   04 = 17. Palavras gerais confirmadas, todas ausentes do 03 e do 04: "citar", "valer",
   "escopo", "fase", "piloto", "trecho", "pergunta", "base", "meio", "fonte", "característica",
   "relação", "obrigação", "resto", "admitir", "facilitar", "obrigar", "frequente", "regular",
   "explícito", "concreto", "direto", "vago", "difícil", "inteiro", "comercial", "negócio",
   "interpretação", "correção", "tradutor", "notificação", "pouco", "expressão", "afirmação",
   "hipótese", "treinamento", "amostra", "adoção", "compreensão", "típico", "princípio",
   "dentro", "volta". Exemplos no texto normativo: R1.1 "As palavras dentro de literais"
   (02 L35); R2.4 "O nome curto mantém as frases dentro dos limites" (02 L275); 01 L15 "uma
   única interpretação"; 01 L23 "os requisitos de negócio". **Correção:** (a) adicione ao
   `check_spec.py --spec` um modo de lista branca (léxico = aprovadas do 03 + 04 + NT-25, com
   regras de flexão) e trate cada ausência como alerta; (b) para cada palavra com 5 ou mais
   ocorrências, decida: entrada aprovada no 03 (DENTRO DE, PERGUNTA, FASE, BASE, FONTE,
   TRECHO, CITAR, VALER, FREQUENTE, EXPLÍCITO, CONCRETO, DIRETO, TREINAMENTO, AMOSTRA,
   PRINCÍPIO), termo do NT-25 (hipótese, afirmação, expressão, interpretação) ou reescrita;
   (c) reescreva a frase do CHANGELOG como "não usam palavras da lista 'Não aprovada' do 03"
   até o item (a) mostrar 0.

2. **[IMPORTANTE] 03 — 12 exemplos e 1 definição violam regras do 02.** O `build.py` verifica
   R8.4 e parte de R9.4, mas não R3.5, R6.4 nem a lista completa de R9.4. Casos verificados:
   - R3.5 (verbo-suporte, regra `[vale]`): `FINAL (adj)` "Faça a verificação final." (é o
     próprio "Não aprovado" de 03 §4, "Faça a verificação da porta"); `BLOQUEIO (s)` "o sistema
     faz o bloqueio da conta" (BLOQUEAR é aprovado; e a definição "Estado de um item [...]"
     não corresponde ao exemplo, que usa a ação).
   - R6.4 (palavra vaga sem valor): `VÁRIOS (pron)` "Mais de 2, sem número exato" e "O log tem
     vários erros de conexão."; `GRANDE (adj)` "Arquivos grandes demoram mais para copiar.";
     `PEQUENO (adj)` "Use um disco pequeno no ambiente de teste."; `RÁPIDO (adj)` "A consulta
     nova é mais rápida."; `BAIXO (adj)` "O espaço livre em disco está baixo." R6.4 proíbe
     "vários", "grande", "pequeno" e "rápido" sem um valor.
   - R9.4 (data de leitura): `ATUAL (adj)` "Verifique a versão atual do agente." (R9.4 lista "a
     versão atual"); `ÚLTIMO (adj)` "Instale a última versão estável."; `AGORA (adv)` "O
     serviço agora usa a porta 8443."
   - R3.2 (comportamento regular = "quando" + presente): `SUCESSO (s)` "O comando retorna o
     código 0 se a operação tiver sucesso."; `METADE (s)` "O cluster perde metade da
     capacidade se um nó parar."
   - Definição incorreta: `FAZER (v)` "Terminar uma ação ou uma tarefa". "Faça um backup" não
     significa "termine um backup". FAZER significa "realizar uma ação". (Este erro já existia
     na rodada 1 e eu não o vi.)
   **Correção:** FAZER = "Produzir um resultado com uma ação. Use apenas quando não existe um
   verbo mais específico."; FINAL → "Verifique o resultado final."; BLOQUEIO → "Depois de 5
   senhas incorretas, o sistema bloqueia a conta. O bloqueio dura 30 min." (definição: "Estado
   de um item bloqueado"); VÁRIOS → defina com a condição de uso ("Use apenas com um número na
   mesma frase") e troque o exemplo por "O log tem 12 erros de conexão em 5 min."; GRANDE/
   PEQUENO/BAIXO/RÁPIDO → exemplos com valor ("Use um disco pequeno, de 20 GB, no ambiente de
   teste"); ATUAL → "Verifique a versão do agente instalado."; ÚLTIMO → "Repita o último
   passo."; AGORA → "Aguarde. Agora, execute o passo 4." ou marque como não aprovada com
   referência a R9.4; SUCESSO/METADE → "quando". No `build.py`, adicione: verbo-suporte com
   "-ção/-mento/-agem/-eio" depois de "faz/faça/realiza/efetua", as palavras vagas de R6.4 sem
   algarismo na frase e "atual/última/agora/nova" à regra de R9.4.

3. **[IMPORTANTE] 01 §9, 02 R5.12, 04 L914 e L632 — "registro" tem 2 significados, e
   "executar" volta a ter o significado que P1 proíbe.**
   - 04, glossário (L914): "registro | NT-15 | Uma linha de uma tabela de banco de dados.", e a
     nota de `registry` (L632): "'Registro' é uma linha de tabela". Mas 01 §9 define
     "Registro | Um documento ou um conjunto de dados que uma etapa gera como evidência", R5.12
     cria o formato "Registro: a aprovação do gestor, no histórico do chamado.", NT-20 lista
     "Registros: chamado, issue, incidente [...]", `evidência` (04 L829) é "Registro que mostra
     que uma etapa [...] aconteceu", e `ADR` (04 §6.1) é "Registro de uma decisão". R5.9 mistura
     os 2: "Se o procedimento alterar um sistema, um registro ou o estado de um pedido". É a
     violação de P1 mais visível do pacote, porque R5.12 é uma regra nova.
   - P1 (01 L89): "O PTS-BR não usa 'executar' com o significado 'fazer uma tarefa'". O 03
     define `RESPONSÁVEL (s)` como "Pessoa ou equipe que executa uma etapa de um processo ou um
     procedimento" (L1088); o 04 repete em NT-19 (L215); `TAREFA (s)` tem o exemplo "O agendador
     executa a tarefa a cada hora"; 05 L1234 "executar o procedimento no ambiente de teste". O 01
     §9 e R5.10 usam a forma certa: "A pessoa ou a equipe que faz uma etapa".
   **Correção:** no 04, renomeie o NT-15 para "linha (de tabela)" e use "registro" apenas como
   artefato de processo (NT-20), com a definição de 01 §9; em `ADR` use "Documento de uma
   decisão"; em R5.9 escreva "um sistema, um dado ou o estado de um pedido". Em RESPONSÁVEL
   (03 e 04 NT-19) e em 05 L1234 troque "executa/executar" por "faz/fazer" ou "segue/seguir".

4. **[IMPORTANTE] R3.2 × 06 e 03 — os exemplos do pacote não seguem a divisão de R3.2.** R3.2
   diz: comportamento regular, em texto descritivo = "quando" + presente do indicativo. Os
   exemplos usam o futuro do subjuntivo para comportamento regular: 06 L249 "O Grafana envia o
   alerta `DBLatenciaAlta` quando o p99 for maior que 500 ms"; 06 L253 "Se uma consulta demorar
   mais de 3 s, a API de catálogo retorna o código de status `504`"; 06 L959 e L970 "A função
   retorna o valor `True` se o número for válido"; a tabela "Mudanças" do ex. 8 cita R3.2 para
   esta forma; 03 SUCESSO e METADE (problema 2). Um revisor que aplica R3.2 marca o exemplo
   como erro; um redator que copia o exemplo desobedece a regra. As 2 formas são corretas na
   norma, por isso o problema é de aplicabilidade, não de gramática. **Correção:** escolha um
   lado. Proposta, mais natural e mais fácil de verificar: em R3.2 e 01 §5.2, aceite "se" ou
   "quando" + futuro do subjuntivo também para o comportamento regular, e mantenha "quando" +
   presente como forma alternativa; ou corrija os 6 exemplos ("quando o p99 é maior que 500
   ms", "quando o número é válido"). Atualize também 04 VT3 (L295), que ainda diz apenas
   "Futuro do subjuntivo depois de 'se' e 'quando'".

5. **[IMPORTANTE] 04, 05, 06 e README — desvios das regras `[revisor]` no texto normativo.** O
   `gram.py` encontrou, fora de exemplos "Não aprovado" e de colunas "Trecho original":
   - R8.4 (algarismos): 31 números por extenso (sem contar "dois-pontos" e a menção "mil" de R8.4). README L6 "O PTS-BR tem duas partes"; 05 L114
     "Três restrições", L154 "três fases", L213 "Três a cinco equipes", L470 "três
     resultados", L572 "dois momentos", L670 "As duas ferramentas", L699, L718, L804, L829,
     L1032, L1037, L1141, L1172, L1241; 06 L588 (Contexto) "duas partes de procedimentos"; "zero" em 01 L359 e 05
     L205, L238, L474, L475, L818, L886, L1115, L1116, L1146.
   - R9.4 ("acima/abaixo" para comparar valores): 05 L207 "M6 acima de 20%", L267 "Amostra
     abaixo do critério", L449 "Frase acima do limite", L476 "exceções acima do limite", L646
     "30% abaixo da linha de base", L1148 "Um aluno abaixo do critério", L1204 "M5 acima da
     meta". O 03 usa "O uso de CPU está abaixo de 50%" como "Não aprovado".
   - R8.3 (ponto e vírgula): 04 L213–L216, L260, L299–L300, L472–L473, L535, L990.
   - R3.8 ("poder" para possibilidade): 05 L161 "se um erro de leitura pode causar dano", 05
     L448 "O desvio pode causar uma ação incorreta", 01 L362 "O texto pode precisar de uma
     palavra".
   - R3.1 (pretérito imperfeito): 05 L820 "os 87 casos anteriores estavam corretos".
   - Concordância de gênero: 02 L1016 "Desativar [...] o MFA"; 04 §6.1 dá o gênero "a" e o 03
     escreve "Ative a MFA".
   **Correção:** algarismos ("2 partes", "3 fases", "0 alertas", "3 a 5 equipes");
   "maior que/menor que" ("M6 maior que 20%", "Frase com mais palavras que o limite");
   ponto final ou lista no lugar de ";" no 04; "O desvio causa uma ação incorreta [...] quando
   o leitor segue o texto"; "os 87 casos anteriores passaram no Vale 3.27.0" → "tiveram o
   resultado correto"; "a MFA". Estenda o `check_spec.py --spec` a números por extenso, ";" e
   "acima/abaixo de" + número.

6. **[IMPORTANTE] 02 R7.1 × 06 ex. 2 — o mesmo tipo de consequência recebe 2 níveis.** A tabela de
   R7.1 classifica pela ação: "ATENÇÃO | [...] | Reiniciar um serviço de produção". As
   perguntas de R7.1 classificam pela consequência. O 06 L340 tem "**ATENÇÃO:** Reinicie apenas
   a API de catálogo [...]. O comando substitui os 6 pods [...], um pod de cada vez. Durante
   aproximadamente 2 min, a API de catálogo responde em até 2 s, em vez de 200 ms." A
   consequência é uma degradação de desempenho, que a pergunta 3 de R7.1 classifica como
   CUIDADO. R7.5 dá exatamente CUIDADO para a mesma consequência: "Por 15 min, a API responde
   em até 2 s, em vez de 200 ms." O objetivo de D5 era o mesmo nível para o mesmo risco.
   **Correção:** na coluna "Exemplos de TI" de R7.1, escreva consequências, não ações:
   "Reiniciar um serviço de produção com indisponibilidade total por 5 min" (ATENÇÃO) e
   "Reiniciar os pods um de cada vez, com latência maior por 2 min" (CUIDADO). No 06 L340, use
   CUIDADO, ou acrescente a consequência que justifica ATENÇÃO.

7. **[IMPORTANTE] 03 D6 e 02 R1.3 — "Esta é a única exceção à regra" é falso; o pacote tem
   vários homógrafos de classe.** D6 diz que apenas "a" e "que" têm 2 classes. Mas o vocabulário
   aprovado produz homógrafos inevitáveis entre substantivo e forma verbal: `FALHA (s)` × "o
   deploy falha" (FALHAR), `TESTE (s)` × "Teste a restauração" (TESTAR), `LIMITE (s)` ×
   "Limite o número de conexões" (LIMITAR, e o título de R5.7 "Limite o tamanho"), `ENTRE
   (prep)` × "Entre no portal" (ENTRAR), `CONTA` × CONTAR (já em D11), "para" × PARAR (R1.10).
   CONECTAR também tem 2 regências ("Também pronominal") e o "se" pronominal não tem entrada
   (`SE (conj)` é apenas conjunção). D7 também dá 2 significados a ENTRADA, EXCEÇÃO, PROCESSO e
   TABELA. Um revisor que aplica R1.3 ao pé da letra marca "O deploy falha" como erro de
   classe. **Correção:** reescreva D6 como regra geral: "Uma forma de um verbo aprovado pode
   ser igual a uma palavra aprovada de outra classe. Esta igualdade é aprovada. A estrutura da
   frase mostra a classe. A regra R1.10 trata o único caso em que a estrutura não mostra a
   classe." Liste os pares de risco (para/PARAR, entre/ENTRAR, falha/FALHAR, teste/TESTAR,
   limite/LIMITAR, conta/CONTAR); adicione `SE (pron)` apenas para os verbos pronominais
   aprovados; troque "única exceção" em R1.3 e em P1 por uma referência a D6 e D7.

8. **[MENOR] 01 §11.2 × 04 NT-25 — 2 listas de metalinguagem com escopos diferentes.** O 01 diz
   que estas palavras são aprovadas "apenas no texto da especificação e nos materiais de
   treinamento"; o NT-25 aceita também "um guia de estilo ou um comentário de revisão". As
   listas diferem: o 01 tem "sentido", "referente", "enunciado", "violação", "severidade",
   "concordância", "apóstrofo", "reticências", "mantenedor", "auditor", "autor da ação"; o
   NT-25 não tem estas palavras. "Sentido" ao lado de "significado" é um par de sinônimos que
   P2 proíbe. Termos que o 02 usa e que nenhuma das 2 listas tem: "átono", "mesóclise",
   "ênclise", "oração subordinada", "pretérito imperfeito", "gerundismo", "voz passiva
   sintética". **Correção:** mantenha uma lista (o NT-25), faça o 01 §11.2 apontar para o
   NT-25, remova "sentido" e adicione os 7 termos.

9. **[MENOR] R3.1 e tabela-resumo — a lista de formas não cobre o infinitivo depois de verbo
   modal e de preposição.** R3.1 diz "Use apenas estas formas" e permite o infinitivo "nas
   construções que as regras R3.3, R3.6 e R5.1 permitem" (passiva, gerúndio, título). As frases
   "Você pode cancelar a operação" (03 PODER), "vão precisar entrar" (R7.2) e "Reinicie o
   serviço para limpar o cache" (R3.2) usam o infinitivo impessoal fora destas construções. A
   tabela-resumo de R3.1 também omite o futuro do subjuntivo. **Correção:** adicione a R3.1
   "Infinitivo depois de PODER, DEVER, PRECISAR (de), IR e de uma preposição ('para limpar',
   'antes de fechar')" e escreva na tabela-resumo "[...] imperativo, futuro do subjuntivo em
   condições e infinitivo".

10. **[MENOR] 06 — 4 desvios pontuais.** (a) Ex. 1, "Reverter o deploy", passo 1: a lista do
    espaço reservado `<numero-do-deploy>` não tem a frase que R8.9 exige ("Substitua cada espaço
    reservado, com os sinais `<` e `>`"); o ex. 2 tem o mesmo desvio com `<pid>`. (b) Ex. 7,
    "Pedir o acesso", passo 5: "Depois de 2 chamados recusados, envie o número do chamado ao
    gestor da equipe de segurança." não tem destino (R5.11); adicione "Este procedimento
    termina neste passo." (c) Ex. 2 L333 "informe o gerente de incidente que você vai
    reiniciar": com a oração como objeto, a regência normativa é "informar algo a alguém":
    "informe ao gerente de incidente que você vai reiniciar os pods da API de catálogo". (d) Ex. 7 alterna
    "pedido de acesso" (título "Analisar o pedido de acesso", "2 dias úteis depois do pedido")
    e "chamado" para o mesmo item (R1.4); R5.10/R5.12 do 02 fazem o mesmo ("o pedido de acesso
    que o solicitante cria no portal de chamados" × "no histórico do chamado"). Use "chamado"
    para o item e "pedido" apenas no nome do modelo.

11. **[MENOR] Coerência de cabeçalhos e contagens.** README L6 "O PTS-BR tem duas partes"
    (regras e dicionário) × 01 L17 "O PTS-BR tem 3 componentes" (regras, dicionário, termos
    técnicos). 06 L5 "Versão 1.0" × "Versão 1.0.0" nos outros arquivos. README "Versão atual:
    **1.0.0**" usa a expressão que R9.4 proíbe. `NOTA (s)` (03 L880) tem 2 significados ("Texto
    curto com uma informação adicional. Também é palavra de sinalização"), contra D8 ("aprovadas
    apenas como palavras de sinalização"). R8.3 "Use o token, o certificado ou os 2." é
    estranho em português; `AMBOS` é aprovado: "ou ambos". `SOLTAR` (03 L1143): "solte o botão
    do mouse na área **Anexos**" — o objeto que o leitor solta na área é o arquivo: "Arraste o
    arquivo até a área **Anexos** e solte o botão do mouse." **Correção:** as 6 substituições
    citadas.

## O que levaria a nota a ≥ 8

1. **Medir a autoconformidade com lista branca (problema 1).** Um modo `--spec --lista-branca`
   no `check_spec.py`, com o léxico do 03 + 04 + NT-25, e a decisão para cada palavra ausente
   com 5 ou mais ocorrências (cerca de 60 palavras: entrada nova no 03, termo do NT-25 ou
   reescrita). Com menos de 50 ocorrências ausentes no texto normativo, Coerência sobe para 8.
2. **Limpar o 03 contra o 02 (problema 2)** e estender o `build.py` a R3.5, R6.4 e à lista
   completa de R9.4. São 13 entradas. Este item e o 3 sobem Correção para 8,5.
3. **Dar 1 significado a "registro" e corrigir EXECUTAR em RESPONSÁVEL (problema 3).**
4. **Fechar as 2 inconsistências de aplicação (problemas 4 e 6):** uma forma de condição para
   comportamento regular que os exemplos seguem, e exemplos de R7.1 por consequência. Este item
   e o 5 (D6 geral) sobem Aplicabilidade para 8,5.
5. **Aplicar as regras `[revisor]` ao próprio texto (problema 5):** algarismos, "maior que/menor
   que", sem ";" no 04, sem "pode causar", "a MFA". São cerca de 60 ocorrências mecânicas.

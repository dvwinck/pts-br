---
lente: documentacao
rodada: 1
notas: {correcao: 6, completude: 6, aplicabilidade: 7, coerencia: 5, valor: 7.5}
nota_final: 6.3
---

Método: leitura integral de README, 01, 02, 05 (partes), 06 e CHANGELOG; 03 por busca e
amostragem estratificada (82 entradas sorteadas, ao menos 3 aprovadas e 1 não aprovada por
letra, mais cerca de 60 entradas consultadas pelo nome); 04 nas seções 1, 2, 4.2, 5 e 6.
Scripts em `scratchpad/` (`parse_dic.py`, `lex.py`, `check_text.py`, `sentlen.py`): extração
das 792 entradas do 03, busca de formas flexionadas das 298 palavras não aprovadas no texto
corrido de 01/02/04/05/README (fora de código, aspas, tabelas de exemplo e blocos
"Não aprovado"), lista de palavras ausentes do 03 e do 04, contagem de palavras por frase.

## Pontos fortes (até 5)

1. **As decisões gramaticais tratam problemas reais do português, não traduzem o STE.**
   "Vai" + infinitivo no lugar do futuro simples (01 §5.1), a nota que identifica o
   imperativo de "você" com o presente do subjuntivo (01 §5.2), a proibição da mesóclise e da
   ênclise com a próclise permitida só depois de sujeito explícito (R3.7), "haver" impessoal no
   singular e "Foi identificado 3 falhas" (R4.3), "o mesmo" anafórico (R1.8), gerundismo
   (R3.6) e "onde" relativo genérico (R1.9) estão corretos e são os erros que um revisor de
   pt-BR encontra todo dia.
2. **A estrutura é equivalente à do ASD-STE100.** As 73 regras cobrem as 9 seções do STE
   (palavras, cadeias nominais, verbos, frases, procedimentos, descrição, avisos, pontuação,
   práticas) com ID, enunciado, justificativa, verificação e par de exemplos. A seção 10
   (R10.4–R10.8: mensagens de erro, rótulos no infinitivo, mensagens de sucesso com particípio,
   variáveis sem concordância com o valor, plural pelo sistema de tradução) vai além do STE e é
   de alto valor para documentação de software.
3. **As "fronteiras de significado" do 03 §3 e a tabela de verbos-suporte do 03 §4** são o
   melhor material de terminologia do pacote. REMOVER/EXCLUIR/LIMPAR/DESCARTAR,
   VERIFICAR/ANALISAR/TESTAR/REVISAR e COPIAR/MOVER/ENVIAR/ENCAMINHAR resolvem dúvidas reais
   com um critério verificável.
4. **As frases da especificação são curtas.** O script contou 1 686 frases no texto corrido
   de 01, 02, 04, 05 e README; só 19 (1,1%) têm mais de 25 palavras. 05 tem 0.
5. **Os exemplos de 06 são realistas e tecnicamente certos.** `pg_cancel_backend` antes de
   `pg_terminate_backend` com aviso entre os dois, `helm rollback` no ramo de timeout,
   `psql -c "\dt"` com a saída real "Did not find any relations.", opções longas do `curl`,
   espaço reservado `<pid>` explicado depois do bloco. A tabela "Mudanças" liga cada correção
   a uma regra, o que torna o arquivo um bom material de treinamento.

## Problemas (ordenados por impacto)

1. **[BLOQUEANTE] 02 × 03 — o dicionário contradiz as regras em pelo menos 6 pontos.** Um
   revisor não consegue decidir qual arquivo segue. Casos verificados:
   - **R9.4 × ABAIXO/ACIMA/SEGUIR.** R9.4: "Não use 'acima', 'abaixo' [...]. Exceção: use
     'a seguir'". O 03 aprova `ABAIXO (adv)` com o exemplo "A tabela abaixo mostra os códigos
     de erro", `ACIMA (adv)` com "O passo acima cria o usuário" (é o próprio "Não aprovado" de
     R9.4) e, em `SEGUIR (v)`, marca como errado "Veja a lista a seguir. (Use: Veja a lista
     abaixo.)". A entrada `seguinte (adj)` também manda usar ABAIXO.
     **Correção:** em 03, mude ABAIXO e ACIMA para "Não aprovada — use A SEGUIR ou o número
     da seção" (mantenha só o sentido físico "abaixo de 50%" → MENOR QUE, que já existe);
     crie `A SEGUIR (adv)`; inverta o contraexemplo de SEGUIR.
   - **R3.9 × FICAR.** R3.9 proíbe "ficar" como verbo de ligação ("O status fica verde
     depois do deploy" é "Não aprovado"). O 03 aprova `FICAR (v)` "Passar a ter um estado"
     com o exemplo "O indicador fica verde quando o serviço está ativo", e usa a mesma
     construção em `QUANDO` ("Quando o disco fica cheio"), `VISÍVEL` ("fica visível") e nas
     definições de 03 §3.3 e §3.5 ("fica disponível", "O item fica visível").
     **Correção:** decida um lado. Proposta: restrinja FICAR a lugar ("O arquivo fica na pasta
     `/etc`"), troque os 5 exemplos por ESTAR ou por "passa a" (crie `PASSAR A (v aux)`), e
     reescreva as definições de ABRIR/FECHAR, APARECER e PUBLICAR com ESTAR.
   - **R3.8 × PODER/DEVER.** R3.8: "Use 'poder' só para capacidade ou permissão [...]. Não use
     'poder' para uma possibilidade incerta ('pode ocorrer')". O 03 define PODER como "Ter a
     possibilidade de fazer algo", 03 §3.8 diz "PODER: possibilidade", e dois contraexemplos
     corrigem para possibilidade incerta: `PODER` "(Use: O serviço pode parar.)" e `DEVER`
     "(Use: O erro pode ser do cache.)". `DANO` usa "Um corte de energia pode causar dano".
     **Correção:** PODER = "Ter a capacidade ou a permissão de fazer algo"; os dois
     contraexemplos passam a "O serviço para quando a fila tem mais de 10 000 mensagens" e
     "A causa do erro é o cache. (Verifique com o comando X.)".
   - **R4.3 × haver.** R4.3 aprova "há" ("exceto com 'há' no sentido de 'existir'", "Há 3
     erros.") e R7.1 usa "não há como recuperar". O 03 marca `haver (v)` como não aprovada
     (use EXISTIR ou TER). **Correção:** mantenha o 03 e reescreva R4.3: "Use EXISTIR ou TER:
     'O log tem 3 erros.'"; reescreva R7.1 como "Sem backup, a equipe não pode recuperar os
     endereços antigos."
   - **R7.3 × exemplos das palavras de sinalização.** `ATENÇÃO (s)`: "**ATENÇÃO:** Este comando
     exclui todos os dados da tabela." e `CUIDADO (s)`: "**CUIDADO:** O comando reinicia todos
     os pods do namespace." Os dois começam pelo risco, não pelo comando (R7.3). O segundo
     também está no nível errado: R7.1 classifica "Reiniciar um serviço de produção" como
     ATENÇÃO. **Correção:** use avisos completos de R7.2/R7.5 como exemplo, ou um exemplo só
     com o comando ("**CUIDADO:** Feche o editor depois de salvar o arquivo.").
   - **R1.2 × R10.4.** R1.2 diz que SALVAR é ação do usuário e que a ação do sistema é
     GRAVAR. O exemplo PTS-BR de R10.4 é "O sistema não salvou o pedido." (06, exemplo 4, usa
     certo: "O sistema não gravou"). **Correção:** "O sistema não gravou o pedido."

2. **[BLOQUEANTE] 01 §11 — "O próprio texto da especificação segue o PTS-BR" é falso.**
   O script encontrou palavras que o 03 marca como "Não aprovada" no texto corrido:
   - "só" (use APENAS): 88 vezes (01: 9, 02: 60, 05: 16, README: 3), inclusive em 15
     títulos de regra ("R1.1 Use só palavras aprovadas", "R3.9 Use só 'ser' e 'estar'").
   - "esse/essa/esses/essas/desses" (use ESTE): 01 l. 21, 62, 162, 166, 170, 174, 178, 180,
     192, 194; 02 l. 42, 44, 60, 64, 228, 277, 313, 331, 415 e outras.
   - "exige" (01 l. 178; 02 l. 279, 536), "muda" (01 l. 23; 02 l. 110, 600), "consegue"
     (01 l. 133; 02 l. 22, 1320), "modifica" (02 l. 198, título de R2.2), "elimina",
     "esconde", "deixa", "conforme" (título de R8.2, 05 ×8), "caso", "motivo", "por isso"
     (02 l. 1054; 03 l. 202), "muito" (05 ×8).
   - "Rode o linter" (README l. 43; 05 l. 235): é exatamente o "Não aprovado" de R1.1
     ("Rode o script de migração"). 05 l. 252: "O revisor pode subir a severidade" — "subir" é
     a outra palavra do mesmo exemplo de R1.1.
   - "1.000" com ponto de milhar: 11 vezes em 05 (§4.4, §5), contra R8.4 ("10 000").
   - EXECUTAR no sentido de "fazer uma tarefa", que P1 proíbe com estas palavras: "o leitor
     executa" (01 l. 103, 348; 02 l. 299, 313, 548, 580, 598, 725, 1155) e "O gestor executa
     este procedimento" (06 l. 568, 579).
   - Palavras ausentes do 03 e do 04 nos exemplos PTS-BR de 02: "Cadastre a chave SSH" (R3.5;
     CADASTRAR não existe), "O reinício para todos os pods" (R7.5; "reinício" é derivado sem
     entrada, contra D4), "esgota a memória" (R7.6), "A causa do erro é desconhecida" (R10.5).
   - Parênteses de inserção, que R8.3 limita a sigla, conversão de unidade e referência: 63
     ocorrências com 3 ou mais palavras em 02 (ex.: R10.1 "(botão, menu, guia, campo, caixa de
     seleção, janela)").
   **Correção:** (a) rode no CI um verificador igual ao `check_text.py` sobre 01–06 e trate
   cada ocorrência como erro de build; (b) substituições mecânicas: só→apenas, esse→este,
   exige→precisa de, muda→altera, consegue→pode, conforme→de acordo com, "Rode"→"Execute",
   "subir"→"aumentar", "1.000"→"1 000", "o leitor executa"→"o leitor faz" (FAZER) ou "segue";
   (c) declare em 01 §11 um glossário de metalinguagem (palavra, frase, verbo, substantivo,
   leitor, redator, significado, exceção), porque estas palavras não estão no 03 nem no 04 e
   aparecem centenas de vezes.

3. **[IMPORTANTE] 03 — "uma palavra, um significado" falha em pelo menos 14 entradas.** Com
   ";" ou "ou" a definição dá dois sentidos: `REDEFINIR` ("Voltar um valor ao valor padrão
   ou definir um valor novo"), `FICAR` (estado ou lugar), `HORA` ("Período de 60 minutos;
   momento do dia"), `LINHA` (série horizontal; série de caracteres), `SUPORTE` (ajuda; a
   equipe), `USO` (ação; quantidade), `NOVO` (não existia; substitui), `FORA DE`, `VER`
   ("Perceber com os olhos; ler"), `TEMPO`, `ÚNICO` ("Que existe apenas um; sem igual" — o
   exemplo "Cada pedido tem um ID único" usa um terceiro sentido, "distinto"), `build` (04 §6:
   "Processo [...]; também o artefato"). O caso mais grave é `PEDIDO`: definido como "Ação de
   pedir algo; o que uma pessoa pede", mas usado em todo o pacote como pedido de compra ("o
   número do pedido", banco `pedidos`, "API de pedidos", "Cada pedido tem um ID único"). Em 04
   §4.2, CLICAR é "Pressionar o botão do mouse sobre um botão", com SOBRE em sentido espacial,
   mas `SOBRE (prep)` é aprovado só como "Que tem como assunto".
   **Correção:** uma definição por entrada; para PEDIDO, aprove "pedido = solicitação" no 03 e
   registre "pedido (de compra)" no glossário do projeto do exemplo, ou use "solicitação" no
   sentido geral; para ÚNICO, defina "Que não tem outro igual no mesmo conjunto"; separe
   `build (o processo)` de `artefato`; aprove SOBRE também como posição ou troque "sobre um
   botão" por "em um botão".

4. **[IMPORTANTE] 03 D6 — falta tratar a homografia de forma "para" (PARAR, 3ª pessoa) ×
   "para" (preposição).** É a ambiguidade mais frequente do português técnico, e a própria
   especificação cai nela: R7.5 "O reinício para todos os pods por 5 a 10 min" (lê-se "o
   reinício destinado a todos os pods"); R7.6 "esgota a memória do servidor e para o banco
   `pedidos`"; `QUANDO` "o serviço para". **Correção:** adicione a regra D12: "Não escreva
   'para' (PARAR) antes de artigo ou substantivo. Escreva o sujeito no plural ('os pods param')
   ou use 'para de' + infinitivo ('o banco para de responder')." O linter de R1.3 detecta
   "para" + artigo depois de um sujeito no singular.

5. **[IMPORTANTE] R3.2 e 01 §5.2 — a justificativa do subjuntivo é linguisticamente
   incorreta, e a regra deixa casos sem solução.** "A forma com indicativo ('Se o teste
   falha, volte ao passo 2') [...] o leitor nativo vê essa forma como um erro" não é verdade:
   "se" + presente do indicativo é gramatical para condição real ou habitual, e o 03 usa esta
   forma ("Quando o disco fica cheio, o serviço para", "Este erro acontece quando o disco está
   cheio"). A regra também não resolve: (a) condição sobre fato passado ("Se o deploy falhou,
   ..." exige "tiver falhado", futuro composto, não aprovado); (b) "até que" / "antes que" +
   presente do subjuntivo ("Aguarde até que o status seja `Ready`"); (c) o infinitivo
   flexionado ("Aguarde até os pods iniciarem"), que é a saída natural de (b) e não aparece em
   R3.1. **Correção:** reescreva R3.2: "Em procedimentos, use 'se'/'quando' + futuro do
   subjuntivo. Em texto descritivo, para um comportamento regular, use 'quando' + presente do
   indicativo. Para um fato passado, use 'se' + pretérito perfeito ('Se o comando retornou o
   código 1')." Adicione a R3.1 o infinitivo flexionado depois de preposição ("até os pods
   iniciarem", "antes de os testes terminarem") e remova a frase sobre o leitor nativo.

6. **[IMPORTANTE] R3.1 — proibir o pretérito imperfeito sem dar a forma para o estado de
   uma versão anterior produz frases enganosas.** O exemplo PTS-BR "Na versão 2.3, o sistema
   envia duas notificações por pedido" usa o presente para um defeito passado e "duas" por
   extenso (R8.4). 06, exemplo 6, repete o padrão ("Na versão 2.9.4, a API envia o webhook [...]
   2 vezes"). Um leitor de notas de versão entende "envia" como comportamento atual.
   **Correção:** defina a forma: "Para o comportamento de uma versão anterior, escreva a
   versão como sujeito, no presente: 'A versão 2.3 envia 2 notificações por pedido. A versão
   2.4 corrige este defeito.'" Corrija "duas" → "2".

7. **[IMPORTANTE] 03 — faltam palavras gerais que todo texto técnico precisa, e o
   vocabulário é pequeno para um equivalente do STE.** O 03 tem 494 aprovadas e 298 não
   aprovadas; o ASD-STE100 tem perto de 900 aprovadas e mais entradas não aprovadas que
   aprovadas. Ausentes do 03 e do 04 (verificado por script): nada (R4.5 aprova "não ...
   nada"), tudo, quem, sim, próprio, pequeno (GRANDE é aprovada), junto, perto, objeto, ponto,
   dizer, significar, conhecer, desejar, lembrar, soltar (a definição de ARRASTAR usa "sem
   soltar o botão"), cadastrar (exemplo de R3.5), estabelecer, principalmente, demais. "ele" é
   não aprovada, mas R1.8 cita "ele" como pronome que o redator pode usar sem ambiguidade.
   Faltam também os ordinais além de PRIMEIRO (o 03 manda "o passo 2", mas não diz o que
   fazer com "segunda tentativa", "terceiro nível").
   **Correção:** inclua estas entradas (aprovadas ou não aprovadas com alternativa); amplie as
   não aprovadas com os verbos mais frequentes em documentação brasileira (desejar,
   cadastrar, mencionar, estabelecer, tornar-se, ocasionar); em R1.8, troque "ele" por "este".

8. **[IMPORTANTE] 03 e CHANGELOG — os exemplos do dicionário ainda violam R8.4.** O CHANGELOG
   diz que corrigiu os números por extenso em TER e COLETAR, mas 15 exemplos PTS-BR continuam
   com número por extenso: ETAPA ("quatro etapas"), OPÇÃO ("três opções"), SISTEMA, MODO
   ("dois modos"), PROCESSO ("duas etapas"), CONDIÇÃO, IGUAL, COMPARAR, ATIVAR, APROVAÇÃO e as
   alternativas de haver ("três réplicas", "duas opções"), possuir, idêntico, isto é, a saber.
   25 exemplos escrevem a unidade por extenso ("30 segundos", "60 segundos"), mas R8.4 pede o
   símbolo ("2,5 s"). Os exemplos `RESTAURAR` ("backup de ontem") usam uma palavra de data
   relativa que R9.4 proíbe. **Correção:** adicione ao `tools/build.py` as verificações de
   número por extenso, unidade por extenso e palavras de R9.4 nas colunas de exemplo.

9. **[MENOR] R1.6 — a regra da crase está incompleta e tem um erro.** "Não use crase [...]
   antes de 'uma'" está errado para horas ("à 01:00", "à uma hora"). A regra não cobre as
   locuções adverbiais femininas que o próprio dicionário torna frequentes ("à direita", "à
   esquerda", com DIREITO/ESQUERDO aprovados) nem "àquele/àquela". **Correção:** "Use crase
   (1) antes de palavra feminina com artigo, (2) antes de horas ('às 02:00', 'à 01:00'),
   (3) em 'à direita' e 'à esquerda'. Não use crase antes de verbo, palavra masculina,
   literal, 'partir' e 'uma' numeral fora de horas."

10. **[MENOR] R8.5 — o título diz ISO 8601, mas os exemplos usam "UTC-3".** O deslocamento
    ISO é "-03:00". **Correção:** "09:30 (UTC−03:00)" ou mude o título para "data ISO 8601 e
    hora de 24 horas com o fuso".

11. **[MENOR] R4.5 — a heurística do linter ("não" + palavra com prefixo "in-", "im-",
    "des-") gera falsos positivos nas proibições legítimas** "Não instale", "Não inicie",
    "Não desligue o servidor" (o exemplo de R5.2). **Correção:** detecte "não" + adjetivo de
    uma lista (impossível, incomum, inválido, indisponível, incorreto).

12. **[MENOR] 06 — quatro desvios em exemplos que são, no geral, bons.** (a) Exemplo 7:
    "5 dias úteis" virou "1 semana", uma alteração de conteúdo (01 §1: "O PTS-BR não muda o
    conteúdo técnico"); use "5 dias úteis ou mais". (b) Exemplo 1, passo 7: o ramo "reverta o
    deploy" não diz o passo seguinte; adicione "Informe o responsável pela versão. Este
    procedimento termina neste passo.", como no passo 4. (c) Exemplo 4, tabela "Mudanças":
    "A causa na mesma frase" contradiz R10.4, que pede a causa em frase própria. (d) Exemplo 8:
    "valida 100 000 números de CPF em aproximadamente 1 s" é um dado que o "Antes" e o
    "Contexto" não têm; escreva o dado no Contexto.

13. **[MENOR] 02 — exemplos PTS-BR que violam outra regra do mesmo arquivo.** R5.6: "Instale
    o `kubectl`" sem substantivo de classe (R1.5); use "a ferramenta `kubectl`", como em 06.
    R6.3 lista os conectores aprovados, mas omite ENQUANTO e NEM, que o 03 aprova.

14. **[MENOR] 03 — definições circulares e definições com palavras fora do 03.** TER "Ter a
    posse de algo", PODER "Ter a possibilidade", SER "Ter uma identidade". FICAR usa "Passar a
    ter" (PASSAR não está no 03). D2 explica "vai" + infinitivo, mas o exemplo de D2 ("Se o
    teste falhar, pare o deploy. Quando o build terminar, execute os testes.") não tem esta
    forma. **Correção:** defina TER como "Possuir algo ou conter algo como parte" (com
    "possuir" só na metalinguagem) ou por exemplo; troque o exemplo de D2 por "O sistema vai
    enviar um e-mail."

## O que levaria a nota a ≥ 8

1. Eliminar as 6 contradições do problema 1 (ABAIXO/ACIMA/SEGUIR × R9.4, FICAR × R3.9,
   PODER/DEVER × R3.8, haver × R4.3, exemplos de ATENÇÃO/CUIDADO × R7.3, "salvou" × R1.2).
   Sozinho, este item sobe Correção e Aplicabilidade para 8.
2. Fazer o texto da especificação passar no próprio verificador léxico (problema 2), com o
   verificador no CI e um glossário de metalinguagem declarado. Este item sobe Coerência
   para 8.
3. Corrigir as 14 entradas com dois significados, com prioridade para PEDIDO, ÚNICO e FICAR,
   e criar a regra D12 sobre "para" (PARAR × preposição) (problemas 3 e 4).
4. Reescrever R3.2 e R3.1 com as formas para fato passado, comportamento regular, "até" +
   infinitivo flexionado e estado de versão anterior (problemas 5 e 6).
5. Incluir no 03 as cerca de 20 palavras gerais ausentes do problema 7 e estender o
   `build.py` às verificações do problema 8.

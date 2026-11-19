---
lente: desenvolvimento
rodada: 2
notas: {correcao: 7.5, completude: 7.5, aplicabilidade: 7.5, coerencia: 8.0, valor: 8.0}
nota_final: 7.7
---

Verificações feitas nesta rodada (scripts no scratchpad da sessão):
- `python3 build.py` (sem `PROBLEM`), `python3 check_spec.py --teste` (95/95 casos; 06: "Antes" 102
  alertas, "PTS-BR" 0), `python3 check_spec.py --spec` (0 alertas) e
  `python3 gerar_regras_dicionario.py --verificar` (OK, 313 entradas).
- `adversarial.py`: 119 frases de dev e de UX contra o motor Python. Resultado: 21 falsos
  positivos e 17 falsos negativos. Parte dos FP é uma decisão de vocabulário, não um erro do linter
  ("Habilite", "Dispare", "Troque" são não aprovadas no 03).
- `estrang.py`: as 32 formas da tabela de 04 §5.4 (verbos com radical estrangeiro).
- `aspas.py` e `frases.py`: o `--spec` sem a isenção das aspas, para achar desvios escondidos.
- `msgs.py`: as mensagens de interface entre crases nos exemplos PTS-BR do 02.
- O Vale não está instalado. O download do binário do Vale foi bloqueado pela permissão da
  sessão. Li o código-fonte do Vale v3.27.0: o `go.mod` usa `jdkato/regexp2`, e
  `internal/regex.Compile` usa `regexp2.RE2`. Este modo aceita lookbehind e `\p{L}`. Portanto os
  padrões devem compilar. A execução real não foi verificada (ver problema 3).

## Status dos problemas da rodada 1

Resultado: 14 resolvidos, 2 parcialmente resolvidos, 0 não resolvidos.

| # R1 | Problema | Status | Evidência |
|---|---|---|---|
| 1 | CI não funciona (repositório de regras fora do runner, `StylesPath`, permissões) | **Parcial** | No repositório da especificação o workflow está coerente: `StylesPath = .` relativo ao `.vale.ini`, Vale 3.27.0 fixado (a versão existe no GitHub), `permissions` com `pull-requests: write` e `checks: write`, nota sobre forks. Para a equipe, a distribuição continua por cópia: `check_spec.py` tem `BASE/tools/vale` fixo, `--teste` lê `BASE/06-exemplos.md` e o job `regras` precisa do 03. Não existe pacote versionado nem `vale sync` (ver problema 2). |
| 2 | Marca `[lint]` promete demais; R10.1 × 05 §6.7 | **Resolvido** | 11 `[vale]`, 70 `[revisor]`; cada `[vale]` tem uma "Verificação" que diz o que a ferramenta não faz. R10.1 agora diz "O revisor compara". 05 §6.3 tem a tabela regra → arquivo → limitação. Resíduo: R4.3 tem `[vale]`, mas o padrão principal (ordem e concordância) é do revisor; o Vale cobre apenas "haver". |
| 3 | Padrões do Vale com erros (RE2, quebra de linha, R1.8, "permissão", flexões, `FraseLonga` em `error`) | **Resolvido** | O texto sobre RE2 saiu do 05. `\s+` em todos os padrões: "Realize a\ninstalação" alerta. "a mesma retorna" e "utilizam o mesmo irão" alertam. "o mesmo e-mail" não alerta. "Dá as permissões" não alerta. "Apaguei"/"apagando" e "Time Machine" estão nos testes. Todas as regras em `warning`. Resíduo: a contagem fiel a R4.2 não existe (05 §5.1 admite 2 diferenças). Os FP novos estão no problema 9. |
| 4 | O texto normativo não segue o dicionário | **Resolvido** | `--spec` mostra 0 alertas. Sem a isenção das aspas, os 170 alertas de 01, 02, 04 e 05 são todos menções metalinguísticas ("Não use 'o qual'"). As mensagens entre crases dos exemplos PTS-BR de R10 também passam sem alerta. |
| 5 | ABAIXO × R9.4 | **Resolvido** | 03: ABAIXO = "Imediatamente depois do texto atual"; R9.4 e D2 iguais; Ex3 usa "a tabela abaixo" para a tabela adjacente. |
| 6 | PASSAR com sentido de argumento | **Resolvido** | 04 §4.2 D: "Fornecer um argumento a uma função, a um método, a um comando ou a um endpoint"; "Todos os testes passaram" → "tiveram sucesso". |
| 7 | registry = repositório; commit = "registro" | **Resolvido** | 04 §5.5: `registry` Manter; "repositório" sem complemento = Git; commit = "Conjunto de alterações que o Git grava em um repositório…". |
| 8 | Vocabulário de API e Ex3 sem resposta nem objeto de erro | **Resolvido** | Glossário: cabeçalho, corpo, código de status, parâmetro de consulta, paginação, campo (JSON incluído), limite de taxa; IDEMPOTENTE no 03; `payload` restrito a mensagem e evento. Ex3 tem cabeçalhos, tabela do corpo, exemplo `201` e "Corpo de erro" com `codigo`, `mensagem`, `erros`. Resíduo no problema 16 (tipos JSON). |
| 9 | R8.9: `<` `>` no shell, detecção de maiúsculas | **Resolvido** | "Antes da lista, escreva que o leitor também substitui os sinais `<` e `>`"; justificativa com redirecionamento; verificação limitada a `bash`, `sh` e `console`, pelo revisor. |
| 10 | "O sistema" como sujeito fixo em R10.4 | **Resolvido** | R10.4: "Use o objeto afetado como sujeito". Ex4 segue. Ver problema 6 (R10.5 e Ex4 criaram outra contradição). |
| 11 | Textos de dev e de UX fora das regras | **Parcial** | 01 §2.1 tem "Textos de desenvolvimento"; 01 §2.2 justifica a exclusão de comentários internos e do título do commit; R10.9 (validação, placeholder, texto alternativo, `aria-label`) e R10.10 (PR, commit, log, CLI, docstring). Faltam o estado vazio e o tamanho do texto na interface (ver problema 13). |
| 12 | Títulos internos em negrito nos exemplos | **Resolvido** | Ex3, Ex6 e Ex8 usam `####` e `#####`. |
| 13 | Ex8 promete CNPJ; bloco sem linguagem | **Resolvido** | Seção "Validar um número de CNPJ"; dígitos conferidos: `11.222.333/0001-81` válido, `11222333000100` inválido; CPF `123.456.789-09` válido, `12345678900` inválido. Blocos com `console` (ver problema 16 sobre `console` sem prompt). |
| 14 | `files: docs` não verifica o README | **Resolvido** | `files` lista o README e os 6 arquivos da especificação. |
| 15 | Terminologia instável (release, semver, `{count}`, R10.2) | **Resolvido** | 01 §2.1 "Notas de versão"; `MAJOR.MINOR.PATCH` em 04, 05 e README; `{quantidade}` em R10.8; R10.2: "Um item de uma lista da interface é um rótulo: escreva o item em negrito". |
| 16 | "Vá para o branch"; "por um tempo" no stash | **Resolvido** | 04 §4.2 E: "Execute o comando `git switch main` para usar o branch `main`." e "para armazenar as alterações locais sem commit". |

## Pontos fortes (até 5)

1. **Automação honesta e testável.** O 05 §6.3 tem uma linha por regra Vale, com a coluna
   "Limitação conhecida". O `check_spec.py` lê os mesmos YAML do Vale. Os 95 casos e os textos
   "Antes"/"PTS-BR" do 06 formam um teste de regressão (102 alertas contra 0). O CI confere com
   `--verificar` se a regra de palavras corresponde ao 03. Para um time de docs-as-code, este é o
   padrão certo: regra, caso de teste e fonte única.
2. **O Ex3 é uma referência de API utilizável.** Ele tem cabeçalhos em lista, uma tabela do
   corpo com tipo e obrigatoriedade, uma tabela de códigos de status com o corpo de cada resposta,
   um exemplo de `201` e o contrato do corpo de erro ("Use este campo no código da aplicação
   cliente"). As decisões de vocabulário seguem o MDN em português (corpo, cabeçalho, código de
   status, parâmetro de consulta).
3. **A Seção 10 agora atende UX writers e devs.** R10.4 com o objeto como sujeito ("O arquivo
   {nome_arquivo} tem mais de 25 MB. Envie um arquivo com até 25 MB.") e R10.9 com validação,
   placeholder, texto alternativo e `aria-label`. R10.10 dá um formato a PR, log, ajuda de CLI e
   docstring. 01 §2.2 justifica bem a exclusão dos comentários internos.
4. **Verbos de controle de versão e de deploy naturais e fechados.** 04 §4.2 E/F e §5.4:
   "Mescle o branch", "Crie um commit", "Envie os commits para o repositório remoto", "Execute o
   deploy", "Reverta o deploy", "Aplique o commit `a1b2c3d` no branch `main`". Cada verbo
   proibido tem uma forma aprovada.
5. **Exemplos tecnicamente corretos.** O Ex1 verifica o contexto com `kubectl cluster-info
   --context prod-sa-east-1` antes do `helm upgrade` (R7.8) e pede o Git 2.23 por causa do `git
   switch`. O Ex6 separa as alterações incompatíveis e dá o procedimento de migração. O Ex8
   documenta cada função com entrada, saída e exceção.

## Problemas (ordenados por impacto)

1. [IMPORTANTE] 04-termos-tecnicos.md:5.4 + tools/gerar_regras_dicionario.py — **o linter não
   encontra os verbos com radical estrangeiro, o desvio mais frequente em texto de dev.** Das 32
   formas da tabela de 04 §5.4, o linter encontra apenas 7 (setar, startar, resetar, deletar,
   checar, customizar e uma forma com "ele"). Ele não encontra "Deployei a versão nova.",
   "Commite as alterações.", "Mergeie o branch.", "Builde a imagem.", "Logue no portal.",
   "Dropei a tabela", "Debugue o código", "Dê push no branch" nem "O pipeline está deployando.".
   Motivo: o gerador lê apenas as entradas "Não aprovada" do 03, e estes verbos estão apenas no
   04. O próprio 04 §5.4, justificativa 5, diz: "Um linter verifica um critério simples
   ('nenhum verbo com radical estrangeiro')". — Correção: o gerador também lê a coluna "Não
   aprovado" da tabela de 04 §5.4 e gera as flexões com a ortografia do radical (deploye,
   deployei, commite, mergeie, logue, plugue, pingue, debugue, rebaseie). Adicione "dar push" e
   "dar pull" como locuções. Adicione estes 6 casos a
   `tools/vale/testes/PalavrasNaoAprovadas/deve_alertar.md`. Depois, a coluna "Linter" de CK-1.5
   pode deixar de dizer "(apenas os verbos do 03)", e R1.7 pode receber a marca `[vale]`.

2. [IMPORTANTE] 05-governanca.md:6.5, 6.7, 8.3, 8.4 + tools/check_spec.py — **a integração numa
   equipe continua por cópia de arquivos, sem versão.** O 05 §6.5 manda copiar `tools/vale/` para
   `.vale/`. Nesta estrutura o `check_spec.py` falha: `ESTILOS = BASE / "tools" / "vale"` é fixo,
   e o script não tem uma opção para a pasta das regras. O `--teste` lê `BASE/06-exemplos.md`, e
   o job `regras` do workflow precisa do 03 e do gerador. Um documento declara `pts-br: "1.0"`
   (8.4), mas a equipe não tem como fixar as regras na versão 1.0. A transição MAJOR (8.3: "O
   revisor aceita a versão anterior e a versão nova") exige 2 conjuntos de regras, e uma cópia
   tem apenas um. — Correção: publique em cada versão um arquivo `PTSBR-1.0.0.zip` (pasta
   `PTSBR/` e `config/vocabularies/`) como asset do release. No `.vale.ini` das equipes, use
   `Packages = https://<host>/pts-br/releases/download/v1.0.0/PTSBR-1.0.0.zip` e execute
   `vale sync` no CI. Adicione ao `check_spec.py` a opção `--estilos CAMINHO`, com o valor padrão
   lido do `StylesPath` do `.vale.ini`. Separe um workflow `tools/ci/docs-lint-equipe.yml` apenas
   com o job `lint` e o `vale sync`.

3. [IMPORTANTE] 05-governanca.md:6.6 e 8.5 + CHANGELOG.md — **a versão 1.0.0 foi publicada sem o
   critério de publicação do próprio 05.** O critério 4 de 8.5 exige `check_spec.py --teste`
   "com o motor Python e com o Vale". O 05 §6.6 diz: "Os 8 casos novos […] ainda não têm um
   resultado com o Vale. O mantenedor executa os testes com o Vale antes de publicar a versão
   1.0.0". O CHANGELOG e o README declaram a 1.0.0 publicada em 2026-11-18. A frase "Com o
   Vale 3.27.0, os 87 casos anteriores estavam corretos" não tem um registro no repositório. Não
   consegui confirmar: o Vale não está instalado, e a leitura do código do Vale mostra apenas
   que os padrões devem compilar. Também existem diferenças de motor que os testes não cobrem: o
   Vale aplica o `Vocab` às regras `substitution`, mas não às regras `existence` com `nonword`. —
   Correção: execute o job `regras` uma vez e grave a saída em
   `tools/vale/testes/resultado-vale-3.27.0.txt` (data, versão, número de casos). Até isto,
   chame a versão de `1.0.0-rc2` ou retire a frase sobre os 87 casos.

4. [IMPORTANTE] tools/ci/docs-lint.yml:job `lint` — **no repositório da especificação, o Vale
   comenta centenas de falsos positivos.** O Vale não tem as isenções do `--spec`: exemplos "Não
   aprovado", menções entre aspas, textos "Antes" e tabelas "Mudanças". O motor Python sem
   `--spec`, que se aproxima do Vale, dá 482 alertas: 214 no 02, 186 no 06, 35 no 05, 27 no 04 e
   20 no 01. O 02 e o 06 não têm nenhum comentário `<!-- vale off -->`. Com `filter_mode: added`,
   cada PR que altera um exemplo recebe comentários do reviewdog que o revisor precisa descartar,
   e isto contamina a métrica M6. O gatilho `workflow_dispatch` também executa o job `lint`, mas
   o reporter `github-pr-review` precisa de um pull request. — Correção: no repositório da
   especificação, troque o job `lint` por `python3 tools/check_spec.py --spec --falhar` nos
   arquivos alterados. Outra opção: adicione ao `.vale.ini` `BlockIgnores = (?m)^\*\*Não
   aprovado:\*\*.*$` e coloque `<!-- vale off -->`/`<!-- vale on -->` em volta das seções
   "Antes" e "Mudanças" do 06. Adicione `if: github.event_name == 'pull_request'` ao job `lint`.

5. [IMPORTANTE] 02-regras.md:R10.8 — **o exemplo PTS-BR de plural tem um defeito de i18n.** O
   texto é "2 formas no sistema de tradução: `1 arquivo excluído.` e `{quantidade} arquivos
   excluídos.`". No CLDR, a categoria `one` do português (pt) vale para i = 0..1. Com 0
   arquivos, o ICU, o i18next e o gettext com regras CLDR escolhem a forma `one`, e o usuário vê
   "1 arquivo excluído.". O número fixo na forma `one` é um erro clássico de localização. —
   Correção: no PTS-BR, escreva `{quantidade, plural, =0 {Nenhum arquivo excluído.} one {#
   arquivo excluído.} other {# arquivos excluídos.}}`. No enunciado, adicione: "Escreva a
   variável também na forma do singular. Não escreva o número 1 no texto. Se o sistema de
   tradução tiver uma forma para o zero, escreva a forma para o zero."

6. [IMPORTANTE] 06-exemplos.md:Exemplo 4 × 02-regras.md:R10.4–R10.6 — **os exemplos de mensagem
   contradizem as regras da própria Seção 10.**
   - R10.5: "Se o sistema não conhecer a causa, não escreva a parte 2 da regra R10.4 e escreva
     uma ação." O Ex4 escreve a frase de causa "A causa do erro não está identificada.", e a
     tabela "Mudanças" troca "Erro desconhecido." por esta frase. É o mesmo "erro desconhecido"
     com outras palavras.
   - R10.4 manda usar o objeto afetado como sujeito. O PTS-BR de R10.5 é "O sistema não carregou
     o painel.", mas "O painel não carregou." é uma frase na voz ativa com o objeto como sujeito.
   - O mesmo diálogo tem 2 sujeitos: R10.6 "O sistema também vai excluir todos os deploys do
     projeto." e Ex4 "Você também vai excluir os arquivos e os deploys do projeto."
   — Correção: no Ex4, escreva "As alterações do projeto {nome_projeto} não estão gravadas. Tente
   de novo depois de 5 min. Se o erro acontecer de novo, envie o código PRJ-500 à equipe de
   suporte." e corrija a linha "Erro desconhecido." da tabela "Mudanças". Em R10.5, escreva "O
   painel não carregou. Atualize a página. […]". Escolha um sujeito para a consequência no
   diálogo e use o mesmo sujeito em R10.6 e no Ex4.

7. [IMPORTANTE] 02-regras.md:R10.10 — **a regra de log leva o dev a um antipadrão, e a regra de
   commit contradiz o escopo.**
   - "Mensagem de log […]: uma frase com o evento no pretérito perfeito, o objeto e os valores
     com a unidade." Com os valores no texto, cada mensagem é diferente. As ferramentas de log
     (Datadog, Sentry, Loki) agrupam os eventos pelo texto da mensagem. A prática de log
     estruturado é uma mensagem fixa com os valores em campos. O exemplo PTS-BR também tem 2
     frases, contra "uma frase": `A conexão com o banco pedidos falhou depois de 5 s. Tentativa 2
     de 3.`
   - "O título [do commit] segue a convenção do repositório e tem no máximo 72 caracteres." O 01
     §2.2 diz que o título do commit está fora do escopo. A convenção do Git é de 50 caracteres
     no título e de 72 caracteres por linha no corpo.
   — Correção: "Mensagem de log: uma frase fixa no pretérito perfeito, sem valores variáveis.
   Escreva os valores em campos estruturados, com a unidade no nome do campo." Exemplo:
   `A conexão com o banco falhou.` e os campos `banco=pedidos duracao_ms=5000 tentativa=2
   tentativas_max=3`. Para o commit: "O corpo tem linhas de até 72 caracteres." Retire o limite do
   título ou mova este limite para o 01 §2.2, como convenção do Git.

8. [MENOR] 06-exemplos.md:Exemplo 3 × 02-regras.md:R7.9 — R7.9 justifica a regra assim: "outros
   usuários do host podem ver o argumento na lista de processos". O Ex3 usa `--header
   "Authorization: Bearer $API_TOKEN"`. O shell expande a variável, e o token fica nos argumentos
   do `curl`, visível no comando `ps`. O aviso PERIGO fala apenas do histórico. — Correção: use um
   arquivo de cabeçalho com permissão 600, `--header @cabecalho-auth.txt` (curl 7.55 ou mais
   novo), e explique o arquivo na lista depois do bloco. Outra opção: em R7.9, diga que a variável
   de ambiente protege o histórico, mas não protege a lista de processos.

9. [MENOR] tools/vale/PTSBR/*.yml — **falsos positivos encontrados com frases de dev.**
   - `OndeRelativo`: "Abra o arquivo onde a configuração fica.", "o repositório onde",
     "No ambiente onde" e "Onde fica o arquivo de configuração?" (pergunta). A lista de lugares
     não tem arquivo, repositório, ambiente, página, tela, tabela, banco, namespace, nó,
     contêiner nem rede.
   - `VerboSuporte`: "O sistema dá a mensagem de erro", "Faça o documento de arquitetura" e "Dê
     o argumento `--force`". Os sufixos "-agem" e "-mento" também encontram substantivos que não
     são derivados de um verbo.
   - `OMesmo`: "O resultado é o mesmo." e "O comportamento é o mesmo em todos os nós.". "é o
     mesmo que" gera 2 alertas, de `OMesmo` e de `PalavrasNaoAprovadas`.
   - `FuturoSimples`: "Ceará". `Unidades`: "às 14h" recebe a sugestão "'10 min'", mas R8.5 pede
     "14:00".
   — Correção: adicione à lista de `OndeRelativo` os nomes de NT-04, NT-12 e NT-13 e exclua
   "Onde" no início de uma frase que termina com "?". No lookahead negativo de `VerboSuporte`,
   adicione `mensag|imag|document|argument|element|segment|instrument`. Exclua "ceará" em
   `FuturoSimples`. Crie um padrão de hora (`\d{1,2}h(?!\p{L})` depois de "às") com a mensagem
   de R8.5. Adicione cada frase deste item ao `nao_deve_alertar.md` da regra.

10. [MENOR] tools/vale/PTSBR/SeparadorMilhar.yml e Unidades.yml — **falsos negativos em casos que
    o 02 cita.** "O valor é R$ 1.500,00." não alerta: o lookahead `(?![.,]?\p{N})` rejeita a
    vírgula decimal. "O arquivo tem 10 KB." e "A rede tem 100 Mbps." não alertam, mas R8.4 diz
    "Não use 'Mbps', 'KB'". — Correção: em `SeparadorMilhar`, use `(?!\.?\p{N})` e aceite
    `,\p{N}+` depois do grupo. Em `Unidades`, padrão 2, adicione `KB|Mbps|Gbps|kbps` com `\s*`.
    Em R8.4, adicione o formato de moeda: "R$ 1 500,00" no texto e o valor em centavos, como
    inteiro, nos campos de API.

11. [MENOR] tools/vale/.vale.ini, FraseLonga.yml, check_spec.py — **os 2 motores dão resultados
    diferentes para R4.2 no mesmo arquivo.** O Vale aplica 20 palavras por pasta (seção
    `[docs/{procedimentos,runbooks}/**/*.md]`). O `check_spec.py` não lê o `.vale.ini` e aplica 20
    palavras a itens de lista numerada em qualquer pasta. O comentário de `FraseLonga.yml` diz que
    o Vale conta "**Salvar alterações**" como 2 palavras. O 05 §6.3 diz que o Vale "não conta o
    negrito" (`IgnoredScopes = strong`). Cada regra de frase longa tem apenas 2 casos de teste. —
    Correção: alinhe o comentário com o 05 §6.3. Adicione ao `check_spec.py` a opção
    `--limite-frase pasta`, que lê as seções do `.vale.ini`. Adicione 6 casos por regra, com
    código em linha, negrito e "10 GB" perto do limite.

12. [MENOR] tools/ — **a pasta tem scripts de trabalho que o 05 §6.2 não lista.** `check04.py`,
    `check_a.py`, `cobertura.py`, `fix1.py`, `fmt.py`, `naousadas.py` e `__pycache__/`. Três
    scripts têm o caminho absoluto `/Users/<usuário>/...`. O `cobertura.py` ainda procura a
    marca `[lint]`, e o `fix1.py` reescreve o texto do 03. Uma publicação CC BY com caminhos
    pessoais e scripts de correção única confunde quem contribui. — Correção: apague estes
    scripts ou mova os scripts para `tools/dev/`, com caminhos relativos a `__file__`. Adicione
    um `.gitignore` com `__pycache__/`.

13. [MENOR] 02-regras.md:Seção 10 — **faltam 3 textos que todo UX writer escreve.** Não existe
    regra para o texto de um link ("clique aqui", "este link"; WCAG 2.4.4). Não existe regra para
    o estado vazio de uma lista ou de uma tela. Não existe regra para o tamanho do texto (truncar
    um rótulo; o texto traduzido com mais caracteres). — Correção: em R10.9, adicione "Texto de
    link: escreva o destino ('Leia a seção 4.2 do guia de instalação'). Não use 'clique aqui' nem
    'este link'." Adicione R10.11 "Escreva o estado vazio com o motivo e uma ação", com o par
    `Nada aqui.` → `Este projeto não tem deploys. Clique em **Executar deploy** para criar o
    primeiro deploy.` Na mesma regra, escreva: "Não escreva um rótulo que precisa de um tamanho
    fixo na tela."

14. [MENOR] 02-regras.md:R8.5 — "09:30 UTC-03:00" não é uma notação da ISO 8601, e a
    justificativa diz "O deslocamento com horas e minutos é a forma da ISO 8601". Na ISO 8601 o
    deslocamento vem colado à hora (`09:30-03:00`), e "Z" indica o UTC. — Correção: "Em prosa,
    escreva a hora e o fuso: '09:30 UTC-03:00'. Em literais de API e de log, use a RFC 3339:
    `2026-12-05T02:00:00-03:00`." Corrija a justificativa.

15. [MENOR] 05-governanca.md:8.1 — o PATCH inclui "Alterar o nível de uma regra do linter".
    Nas fases Expansão e Padrão (`fail_on_error: true`), uma regra que passa a `error` bloqueia
    o merge de PRs que antes passavam. Para quem consome as regras, esta mudança é incompatível.
    — Correção: classifique a mudança de uma regra para `error` como MINOR, com uma entrada
    "Alterado (linter)" no CHANGELOG. Outra opção: dê às regras Vale uma versão própria
    (problema 2).

16. [MENOR] Consistência de formato e de vocabulário de dev.
    - Ex3: o tipo de `erros` é "lista", mas o 04 §5.5 decide "array | Manter". O glossário não
      tem os tipos JSON que a coluna "Tipo" precisa: booleano, inteiro, número, nulo.
    - R10.4 a R10.9 e o Ex4 escrevem as mensagens de interface em código. A tabela de R8.8 diz
      "Aspas duplas: Mensagem completa que o sistema mostra". Escreva em R8.8 que o texto de uma
      mensagem no arquivo de tradução é um literal (código) e que a mensagem citada num documento
      fica entre aspas.
    - R5.8, R8.9, Ex1 e Ex8 usam blocos ```` ```console ```` sem prompt. O realce `console` é para
      uma sessão com prompt e saída. Como R5.8 proíbe o prompt, use ```` ```shell ````. R5.8
      também não diz como quebrar um comando longo: o `curl` do Ex3 tem uma linha de cerca de 200
      caracteres. Adicione "Quebre um comando longo com `\` no fim da linha, uma opção por linha."
    - O 03 diz "versão 1.0". Os outros arquivos dizem "1.0.0".

## O que levaria a nota a ≥ 8 (se < 8) ou a 9 (se ≥ 8)

1. **Fechar a lacuna principal do linter para devs (problemas 1, 9, 10):** gerar a regra de
   palavras também da tabela de 04 §5.4, corrigir os FP e FN deste parecer e adicionar as frases
   de `adversarial.py` aos `testes/`. Isto leva Aplicabilidade a 8,5 e dá ao `[vale]` de R1.1
   uma cobertura real em texto de dev.
2. **Provar e distribuir a automação (problemas 2, 3, 4):** uma execução registrada do Vale
   3.27.0 com os 95 casos; um pacote `PTSBR-<versão>.zip` com `Packages` e `vale sync`;
   `--estilos` no `check_spec.py`; o job `lint` da especificação sem ruído. Isto leva Correção e
   Aplicabilidade a 8 ou mais e torna verdadeiro o critério 4 de 05 §8.5.
3. **Corrigir os 3 defeitos de domínio da Seção 10 (problemas 5, 6, 7):** o plural com a forma
   `one` do CLDR, o Ex4 alinhado com R10.5, e o log com uma mensagem fixa e os valores em campos.
   São mudanças pequenas no texto, e a Seção 10 é a parte que devs e UX writers usam. Isto leva
   Correção e Valor a 8,5.

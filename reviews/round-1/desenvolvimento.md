---
lente: desenvolvimento
rodada: 1
notas: {correcao: 6.5, completude: 6.5, aplicabilidade: 7.0, coerencia: 6.0, valor: 7.5}
nota_final: 6.7
---

Verificações objetivas feitas com scripts (sem Vale instalado na máquina; os padrões
do 05 §6.3 foram traduzidos para Python `re`, com `\p{L}` → `[^\W\d_]`):
- `scratchpad/check_vocab.py`: procura as entradas "Não aprovada" do 03 nas Seções 8 e 10
  do 02 e nos blocos PTS-BR do 06.
- `scratchpad/test_vale.py`: roda as regras do Vale contra os textos "Antes" (devem
  alertar) e "PTS-BR" (não devem alertar) do 06, mais casos dirigidos.
- Contagem de palavras por frase nos blocos PTS-BR do 06 com o token de `FraseLonga.yml`.

## Pontos fortes (até 5)

1. **Verbos de controle de versão e a tabela de 04 §5.4 ("deployar" → "Execute o deploy").**
   "Crie um commit", "Mescle o branch", "Envie os commits para o repositório remoto",
   "Faça o rebase do branch" são formas que um dev brasileiro lê sem estranhar; "mesclar"
   é o termo da interface pt-BR do GitHub. A proibição total de verbos com radical
   estrangeiro (commitar, setar, buildar) tem justificativa técnica boa (conjugação
   instável, verificável por regex) e uma alternativa para cada caso.
2. **R10.8 (variáveis em textos de interface)** é a melhor regra de i18n do pacote: proíbe
   `%s`/`{0}`, proíbe artigo concordando com variável ("O {0} foi excluído" → "O pasta foi
   excluído") e manda usar as formas de plural do sistema de tradução em vez de "(s)".
   É exatamente o que um time de front-end precisa.
3. **R10.4–R10.6 e o Exemplo 4.** Estrutura "o que aconteceu / causa / o que fazer /
   código" e diálogos com rótulos que repetem a ação ("[Revogar token] [Cancelar]") seguem
   a prática de Material, Fluent e Apple HIG. O Exemplo 4 corrige "Ops!", "Algo deu
   errado :(" e "[Sim] [Não]" de forma convincente.
4. **Os exemplos cumprem R4.2.** Medido: nos 8 blocos PTS-BR do 06 só 2 frases passam de
   20 tokens (Ex2: 22, frase descritiva; Ex8: 21, descritiva) e nenhuma passa de 25. O
   README do Exemplo 8 está correto até no dado: `123.456.789-09` e `12345678909` são CPFs
   válidos e `12345678900` é inválido (dígitos verificadores conferidos).
5. **Docs-as-code pensado desde o início:** repositório de regras com `testes/deve_alertar.md`
   e `nao_deve_alertar.md` por regra, regra de dicionário gerada do 03 ("o dicionário é a
   única fonte"), `filter_mode: added` na fase Expansão e extração das mensagens de
   interface de JSON/YAML/`.po` para o linter (05 §6.5).

## Problemas (ordenados por impacto)

1. [BLOQUEANTE] 05-governanca.md:6.5 — **o workflow de CI não funciona como está.** O passo
   `pip install -r pts-br-regras/scripts/requirements.txt` usa a pasta `pts-br-regras/`, mas
   o job só faz `actions/checkout@v4` do repositório da documentação; o repositório de
   regras (05 §6.2) nunca chega ao runner. O mesmo vale para o Vale: `.vale.ini` aponta
   `StylesPath = estilos`, que não existe no repositório da equipe. — Correção: no
   `.vale.ini` das equipes, use `Packages = https://<host>/pts-br-regras/releases/download/v1.0.x/PTSBR.zip`
   e um passo `vale sync` antes do lint (ou um segundo `actions/checkout@v4` com
   `repository: <org>/pts-br-regras` e `path: pts-br-regras`). Acrescente
   `permissions: {contents: read, pull-requests: write}`, que o reporter
   `github-pr-review` precisa, e diga que PRs de fork não recebem comentários.

2. [BLOQUEANTE] 02-regras.md:Tabela-resumo + 05-governanca.md:6.2/6.7 — **a marca `[lint]`
   promete o que a automação não entrega.** 54 de 73 regras têm `[lint]`, mas o 05 §6.2
   lista só 7 arquivos de regra. Várias marcações são inviáveis com Vale (regex sem
   morfologia): R4.3 (sujeito antes do verbo e concordância), R5.2 (imperativo), R5.4,
   R6.6, R7.3 (ordem comando-risco-consequência), R7.6 (consequência concreta), R1.6 (crase
   exige gênero), R3.1/R3.2 (tempos e modos). Há contradição direta: R10.1 diz "O linter
   compara cada texto em negrito com o catálogo de textos da interface", e 05 §6.7 diz "Só
   um humano verifica [...] Se o rótulo citado é igual ao rótulo da interface (CK-10.1)".
   O catálogo de interface também não existe em nenhuma parte da automação. — Correção:
   troque `[lint]` por uma marca de ferramenta: `[vale]` (regex de precisão alta),
   `[script]` (contagem estrutural: R5.3, R5.7, R6.2, R8.9 em blocos de código, R10.8 em
   arquivos de tradução), `[LT]` (LanguageTool pt-BR: R1.6, R3.1, R3.2, R4.3) e `[revisor]`.
   Acrescente ao 05 §6.2 uma tabela regra → arquivo → estado (implementada/planejada).
   Retire `[lint]` de R10.1 e R10.2 até existir o catálogo; se existir, gere um
   `accept.txt`/regra `existence` a partir dos arquivos de tradução.

3. [IMPORTANTE] 05-governanca.md:6.3 — **padrões do Vale com erros verificáveis.**
   - "O Vale usa a sintaxe [...] do Go (RE2), com lookahead e lookbehind" é contraditório:
     RE2 não tem lookaround. O Vale compila as regras com `regexp2` (semântica .NET). Nessa
     semântica `\w` já é Unicode, então a justificativa de `nonword` + `(?<!\p{L})` precisa
     ser confirmada com um teste, não afirmada. Corrija o texto para "regexp2 (sintaxe .NET)"
     e coloque o caso "índice"/"já" no `testes/`.
   - **Quebra de linha:** os padrões usam espaço literal. "realize a\ninstalação" (parágrafo
     com quebra suave, como no próprio 05) não gera alerta no teste; na mesma linha gera.
     Correção: troque cada `' '` por `\s+` em `VerboSuporte.yml`, `OMesmo.yml` e
     `Gerundismo.yml`.
   - **R1.8 falha nos casos do próprio 06:** "As integrações que utilizam o mesmo irão
     parar" (Ex4 Antes) e "a mesma retorna True" (Ex8 Antes) **não** geram alerta, porque
     "irão" e "retorna" não estão na lista de verbos. Falso positivo em PTS-BR aprovado:
     "Já existe um usuário com o mesmo e-mail" (Ex3) alerta em `'o mesmo e'`, porque o
     hífen satisfaz `(?!\p{L})`. Correção: use `(?![\p{L}-])` e troque a lista fechada de
     verbos por "mesm[oa]s? seguido de palavra que não é substantivo do glossário", ou
     baixe a regra para `suggestion`.
   - `VerboSuporte.yml` alerta "Dá as permissões do perfil de acesso" no PTS-BR do Ex7
     ("permissão" termina em "-são"). Correção: exclua "permissão|versão|sessão|extensão"
     com lookahead negativo.
   - `PalavrasNaoAprovadas.yml`: "apaguei" e "apagando" não geram alerta (a lista de
     flexões não tem 1ª pessoa nem gerúndio); `time` gera alerta em "Time Machine".
     Correção: o gerador deve criar todas as flexões dos tempos aprovados e não aprovados
     (R3.1) e respeitar o `accept.txt` de nomes próprios.
   - `FraseLonga.yml` com `level: error` contradiz o próprio 05 §6.4 (`error` só com
     falso positivo ≤ 5% medido) e a contagem difere de R4.2: o token conta "10 GB" e
     "**Salvar alterações**" como 2 palavras, e o código em linha que o Vale ignora conta
     0. Correção: `level: warning` até a medição M6; mova a contagem fiel a R4.2 para o
     `metricas.py`.

4. [IMPORTANTE] 02-regras.md (todas as seções) — **o texto normativo não segue o próprio
   dicionário.** "só" está "Não aprovada (Use: APENAS)" no 03, mas aparece 77 vezes no 02,
   inclusive em 14 títulos de regra ("R1.1 Use só palavras aprovadas", "R8.6 Use
   maiúsculas só no início", "R7.2 Use NOTA só para"). Nas Seções 8 e 10: "conforme"
   (título de R8.2 e R10.2; use DE ACORDO COM), "Acrescente" (R8.7, R10.6; use
   ADICIONAR), "o usuário consegue executar" (R10.4; "conseguir" não é aprovada),
   "deixa o usuário sem uma saída" (R10.4), "por isso" (R8.4), "esse nome" (R8.6),
   "inserir", "elimina", "observar" (R8.3, R8.8). O CHANGELOG diz que um script comparou
   só os exemplos. — Correção: estenda o teste de vazamento de `tools/build.py` aos
   títulos, enunciados e justificativas de 01, 02, 04, 05 e README, e corrija os casos
   (por exemplo, "R1.1 Use apenas palavras aprovadas e termos técnicos").

5. [IMPORTANTE] 03-dicionario.md:ABAIXO e `seguinte` × 02-regras.md:R9.4 — o 03 aprova
   ABAIXO com o exemplo "A tabela abaixo mostra os códigos de erro" e manda trocar
   "seguinte" por "abaixo" ("Execute o comando abaixo"); R9.4 proíbe "acima", "abaixo" e
   "seguinte". O Ex3 usa "os campos da tabela a seguir". — Correção: limite ABAIXO ao
   significado de posição física na tela ("o campo abaixo do logotipo") e troque os dois
   exemplos por "A tabela 3 mostra os códigos de erro" e "Execute o comando do passo 2".

6. [IMPORTANTE] 04-termos-tecnicos.md:4.2 I (PASSAR) — "Passe o parâmetro `id`. (Use:
   Envie o parâmetro `id`.)" está errado para devs: em uma chamada de função não há envio;
   "passar um argumento" é o termo de qualquer documentação de linguagem em pt-BR. "Enviar"
   serve só para requisição HTTP. — Correção: acrescente a PASSAR o significado técnico
   "Dar um valor a uma função, a um método ou a um comando no momento da chamada" ("Passe
   o argumento `timeout` para a função `conectar()`") e mantenha "Envie o parâmetro" só
   para requisições. Mova "O uso de CPU passou de 90%" para a coluna de uso não técnico.

7. [IMPORTANTE] 04-termos-tecnicos.md:5.5 e 6 — **um nome para dois conceitos de dev.**
   "registry → repositório" e o glossário define repositório como "Local que armazena
   código, pacotes ou imagens". No mesmo texto o leitor vê "Envie os commits para o
   repositório remoto" (Git) e "o repositório de imagens" (registry), o que viola P2/R1.4.
   Na mesma tabela, "registro" é "uma linha de uma tabela de banco de dados", mas a
   definição de "commit" começa com "Registro de um conjunto de alterações". —
   Correção: decisão **Manter** para "registry" ("o registry de imagens", "o registry
   npm"), e reescreva a definição de commit: "Conjunto de alterações que o Git grava em um
   repositório, com um autor, uma data e uma mensagem."

8. [IMPORTANTE] 04-termos-tecnicos.md:6 + 06-exemplos.md:Exemplo 3 — **falta o vocabulário
   de documentação de API.** "campo" está no glossário só como elemento de interface
   (NT-05), mas o Ex3 usa "campo" para propriedade JSON (`nome`, `email`). Não há
   entradas para cabeçalho (header), corpo da requisição (body), código de status HTTP,
   parâmetro de consulta (query string), paginação, limite de requisições (rate limit),
   idempotência, SDK e CLI. O Ex3 usa "Código HTTP" e "Payload", e o 01 §2.1 promete
   "Documentação de API [...] códigos de erro". — Correção: acrescente ao glossário
   "campo (de um objeto JSON)" como segundo significado com categoria NT-10 (ou o termo
   "propriedade"), "cabeçalho", "corpo", "código de status", "parâmetro de consulta",
   "limite de requisições" e "idempotente". No Ex3, acrescente um "Exemplo de resposta"
   com o JSON do `201` e o formato do objeto de erro do `400`; "Uma mensagem de erro"
   (linhas `401` e `409`) contradiz R6.4 e não diz ao dev qual campo ler.

9. [IMPORTANTE] 02-regras.md:R8.9 — o formato `<nome-do-servidor>` é bom para texto, mas
   em bloco de shell `<` e `>` são redirecionamento: `ssh -i <arquivo-da-chave>
   <usuario>@<servidor>` colado sem substituição dá "no such file or directory" ou, com
   `>`, **cria/sobrescreve** um arquivo. A verificação "detecta, dentro de blocos de
   código, palavras em maiúsculas sem definição" também alerta em SQL (`DROP TABLE`),
   em cabeçalhos HTTP e em variáveis de ambiente como `PORT`; e o Vale ignora blocos de
   código por padrão. — Correção: acrescente à regra "Substitua também os sinais `<` e
   `>`" na lista de explicação; restrinja a detecção de maiúsculas a blocos com
   linguagem `bash`/`sh`/`console`; diga que a verificação usa `scope: raw` no Vale ou o
   `metricas.py`.

10. [IMPORTANTE] 02-regras.md:R10.4 + 06-exemplos.md:Exemplo 4 — **"O sistema" como sujeito
    fixo deixa as mensagens robóticas** e mais longas: "O sistema não gravou as alterações
    do projeto. O sistema não identificou a causa do erro. Tente de novo [...]" Para UX
    writing, o sujeito natural é o objeto afetado. — Correção: no enunciado de R10.4,
    escreva "Use o objeto afetado como sujeito. Use 'o sistema' como sujeito apenas se
    o objeto não puder ser o sujeito em voz ativa." Exemplo para o Ex4: "O arquivo
    {nome_arquivo} tem mais de 25 MB. Envie um arquivo com até 25 MB." (2 frases em vez
    de 3, sem "O sistema recusou").

11. [IMPORTANTE] 01-introducao.md:2.1 — **textos de dev comuns ficam sem regra.** O escopo
    não cita mensagens de commit, descrições de pull request, saída e `--help` de CLI,
    mensagens de log e docstrings; a Seção 10 não trata de texto alternativo de imagem,
    `aria-label`, dica de campo (placeholder), mensagem de validação de campo ("O campo
    **E-mail** é obrigatório"), estado vazio nem do aumento de tamanho do texto na
    tradução. — Correção: acrescente ao 01 §2.1 a linha "Textos de desenvolvimento:
    descrição de pull request, ajuda de CLI, mensagens de log para operadores", e
    acrescente à Seção 10 uma regra R10.9 "Escreva textos de acessibilidade e de
    validação de campo" com 2 pares Não aprovado/PTS-BR.

12. [MENOR] 06-exemplos.md:Exemplos 3, 6 e 8 — os títulos internos estão em negrito
    ("**Autenticação**", "**Requisitos**", "**Instalar a biblioteca**"). R8.8 aprova
    negrito só para elemento de interface e palavra de sinalização. Num README real, isso
    também tira os títulos do escopo `heading` do Vale (R8.1, R8.6). — Correção: use
    títulos Markdown (`###`) dentro dos exemplos.

13. [MENOR] 06-exemplos.md:Exemplo 8 — o resumo promete CNPJ ("valida e formata números do
    [...] CNPJ"), mas o README só documenta funções de CPF (R9.5). O bloco
    `pip install brvalida` não tem linguagem (`console`/`bash`), e os blocos Python têm. —
    Correção: acrescente "Validar um número de CNPJ" ou retire o CNPJ do resumo; use
    ```` ```console ```` nos comandos.

14. [MENOR] 05-governanca.md:6.5 — `paths` inclui `'**/*.md'`, mas `files: docs` faz o
    Vale ler só `docs/`: um PR que altera só o `README.md` da raiz (o caso do Ex8) roda o
    workflow e não verifica nada. — Correção: `files: '["docs", "README.md"]'` ou
    `files: .` com `[*.md]` no `.vale.ini`.

15. [MENOR] Terminologia instável: 01 §2.1 diz "Notas de release", mas 04 §5.5 decide
    "release → versão" e "release notes → notas de versão". O glossário define
    versionamento semântico como "MAIOR.MENOR.CORREÇÃO"; o README e o 05 §8 usam
    "MAJOR.MINOR.PATCH". R10.8 mistura `{nome_arquivo}` e `{count}` como nomes de
    variável. R10.2 escreve a opção de lista como código (`sa-east-1`), mas R10.1 manda
    escrever o rótulo do elemento em negrito. — Correção: "Notas de versão" no 01; uma
    só grafia de semver (proposta: MAJOR.MINOR.PATCH como literal, em código); `{quantidade}`
    em R10.8; decida em R10.2 se um valor visível numa lista é rótulo (negrito) ou valor
    (código) e escreva a decisão no enunciado.

16. [MENOR] 04-termos-tecnicos.md:4.2 E — "Vá para o branch `main`" (checkout/switch) usa IR,
    cujo único significado é "mover para outro lugar"; um branch não é lugar, e o dev
    estranha a frase. "Execute o comando `git stash` para armazenar as alterações locais
    por um tempo" tem "por um tempo", que é vago (R6.4). — Correção: "Troque para o branch
    `main` com o comando `git switch main`" (adicionar TROCAR a 4.2 E, se não for
    aprovada no 03) e "Guarde as alterações locais na pilha de stash com o comando `git
    stash`", ou apenas "Execute o comando `git stash`".

## O que levaria a nota a ≥ 8 (se < 8) ou a 9 (se ≥ 8)

1. **Automação honesta e executável (problemas 1, 2, 3, 14):** CI que roda num repositório
   limpo (`Packages` + `vale sync`, permissões); marca de ferramenta por regra no lugar de
   `[lint]`; os 7 YAML corrigidos (`\s+`, hífen em R1.8, flexões no gerador,
   `FraseLonga` em `warning`) e um `testes/` que já contenha os casos deste parecer,
   inclusive os "Antes" do 06 como `deve_alertar.md`. Só isso leva Aplicabilidade e
   Correção a 8.
2. **Passada de conformidade no próprio texto (problemas 4, 5, 15):** rodar o detector de
   palavras não aprovadas em títulos e enunciados e fechar a contradição ABAIXO × R9.4.
   Leva Coerência a 8.
3. **Vocabulário e exemplos de dev (problemas 6, 7, 8, 10, 11):** PASSAR com sentido de
   argumento, registry separado de repositório, glossário de API (cabeçalho, corpo,
   código de status, campo JSON), resposta e objeto de erro no Ex3 e uma regra para
   validação de campo e acessibilidade. Leva Completude e Valor a 8 ou mais.

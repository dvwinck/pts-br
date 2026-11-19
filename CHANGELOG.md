# Changelog do PTS-BR

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · **Versões**

Este arquivo segue o formato de [`05-governanca.md`](05-governanca.md), [seção 8.2](05-governanca.md#82-changelog).

## [1.0.0] - 2026-11-18

Revisões 2, 3 e 4 da especificação. As alterações aplicam as decisões D1 a D16 de
`reviews/DECISOES-R2.md`, E1 a E13 de `reviews/DECISOES-R3.md` e G1 a G6 de
`reviews/DECISOES-R4.md`. Esta versão não tem PMD nem PMR. O linter em Python
([`tools/check_spec.py`](https://github.com/dvwinck/pts-br/blob/main/tools/check_spec.py)) é o motor de referência desta versão ([`05-governanca.md`](05-governanca.md), [seção 6.1](05-governanca.md#61-ferramentas-desta-versão)).

A tag `v1.0.0` ainda não existe: o mantenedor cria a tag no commit da publicação
([`05-governanca.md`](05-governanca.md), [seção 8.5](05-governanca.md#85-critérios-para-publicar-uma-versão), critério 9). Os números abaixo são os números da última
verificação antes da publicação (2026-11-18). O mantenedor executa os comandos de novo no
commit da tag e atualiza os números.

### Resultado dos critérios de publicação (`05-governanca.md`, seção 8.5)
1. `python3 tools/build.py`: nenhuma linha `PROBLEM`. 723 aprovadas, 362 não aprovadas, 0 obsoletas.
2. `python3 tools/build.py --render`: o resultado é igual ao [`03-dicionario.md`](03-dicionario.md).
3. `python3 tools/gerar_regras_dicionario.py --verificar`: OK, 421 entradas, 0 palavras obsoletas.
4. `python3 tools/check_spec.py --teste` (motor Python): 160 testes de regra corretos. Os
   textos "Antes" dos 10 exemplos do 06 geram 122 alertas, e os textos "PTS-BR" geram 0
   alertas. As 24 frases da lista branca e os 13 testes das opções de equipe (`--config`,
   `--glossario`, `--mensagens`, `--metricas`) estão corretos.
   **As regras atuais não foram testadas no Vale.** A revisão 2 testou com o Vale 3.27.0
   uma versão anterior das regras (87 testes), e 8 dos 13 arquivos de regra mudaram depois.
   O registro `tools/vale/testes/resultado-vale-3.27.0.txt` ainda não existe. O teste das
   regras atuais com o Vale é um critério de entrada do Piloto ([`05-governanca.md`](05-governanca.md), seção
   3.2), não um critério desta versão (decisão E8).
5. `python3 tools/check_spec.py --spec --falhar`: 0 alertas.
6. `python3 tools/check_spec.py --lista-branca --spec --meta 1`: 62 de 74 430 palavras fora
   da lista branca (0,08%), 36 palavras diferentes. Por arquivo: README 0,22%, 01 0%, 02 0%,
   03 0,06%, 04 0,34%, 05 0,03%, 06 0%. Desde a revisão 4, um termo composto do 04 ("banco
   de dados", "roda do mouse") e uma locução do 03 são unidades: a lista branca não aceita a
   parte do termo fora do termo. Por isso, o número é maior que o número da revisão 3
   (19 palavras).
   **A lista branca verifica a forma da palavra, não o significado.** O significado é um
   item do revisor (CK-1.2). A revisão 4 corrigiu os usos fora do significado que a
   avaliação de documentação da rodada 3 listou (decisão G1), com uma leitura humana, não
   com uma ferramenta.
   Decisão do mantenedor para as palavras fora:
   - Nomes próprios em minúsculas ou em inglês: "asd" (ASD-STE100), "and" e "of" (nome
     oficial da ASD no README), "mdn" (MDN Web Docs), "abnt" e "nbr" (norma), "js",
     "martins" e "icmc-usp" (referência bibliográfica do 05, seção 5.6) e "governança"
     (título do arquivo 05).
   - "cobrança": parte do termo "serviço de cobrança", o exemplo de glossário do projeto
     do 04, seção 7. A própria linha define o termo.
   - "eletricidade", "força", "humano", "luz" e "som": palavras das definições de ENERGIA,
     PRESSIONAR, PESSOA e SINAL no 03. Estas palavras não têm um equivalente aprovado com
     o significado da definição. Estas palavras ficam apenas nas definições.
   - As outras palavras do 03 e do 04 ("nuvem", "virtual", "dono", "assinatura") são partes
     de termos compostos usadas fora do termo, nos títulos das categorias e nas definições.
     O mantenedor decide cada palavra no próximo PMD do 03 ou do 04.
7. Cada regra nova tem um item na lista de verificação ([`05-governanca.md`](05-governanca.md), [seção 4.2](05-governanca.md#42-lista-de-verificação-do-revisor)).
   [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) tem o item CK-5.11.
8. Esta entrada tem as seções da seção 8.2.
9. A tag `v1.0.0`: o mantenedor cria a tag na publicação.

### Licença
- CC BY 4.0, decidida para a versão 1.0.0 (README, seção "Licença").

### Adicionado
- Revisão 4 (decisões G1 a G6):
  - 05, seção 4.1 (G4): estado `EXCECAO-PEDIDA` e procedimento "Decidir uma exceção S2". O resultado "Aprovado com exceções" tem agora um caminho no fluxo. Procedimentos novos "Corrigir os desvios da revisão" (redator) e "Decidir um conflito de revisão" (mantenedor, prazo de 5 dias úteis). Cada espera tem a saída "sem resposta no prazo", cada volta tem o número máximo de vezes, e o fim de um procedimento usa o destino "Este procedimento termina neste passo." de [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor).
  - 05, seção 4.5 (G4): procedimentos do redator, do revisor e do aprovador fora do Git, com o pedido de exceção e o cálculo de M1 e M2.
  - 05, seção 4.1 e Anexo C (G4): linha `[METRICAS]` com `M1-sub`, `M2-sub`, `M1-pub` e `M2-pub`. O comentário de resultado é o registro permanente de M1 e M2. O pipeline de equipe executa `--metricas` e mostra a linha no resumo do job.
  - 05, seção 9.5 (G4): o primeiro revisor de uma equipe nova na Expansão faz a trilha sem os 5 documentos, com um revisor responsável que revisa de novo as 5 primeiras revisões.
  - 05, seção 4.2: CK-5.11 para [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor). CK-7.6 pede o passo que mostra o alvo com a opção de alvo do comando ([R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor)). CK-7.5 tem a exceção do negrito de [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor).
  - 05, seção 2.1: regra 4, "O aprovador de um documento não é o redator do documento". No mínimo 2 aprovadores.
  - `tools/check_spec.py --config ARQUIVO` (G5): lê um `.vale.ini` (MinAlertLevel, StylesPath, seções de pastas, BasedOnStyles e `PTSBR.<Regra>`), como o Vale. O caminho do documento é comparado a partir da pasta do `.vale.ini`, também com um caminho completo.
  - `tools/check_spec.py --glossario ARQUIVO` (G5): o glossário do projeto (04, seção 7). A coluna "Termo" entra na lista branca e em M2. A coluna "Sinônimos não aprovados" gera a regra `GlossarioProjeto`.
  - `tools/check_spec.py --mensagens` (G5): lê arquivos de tradução JSON (plano ou com níveis) e gettext `.po`/`.pot` e aplica a regra nova [`tools/vale/PTSBR/Mensagens.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/vale/PTSBR/Mensagens.yml) ([R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor), [R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor), [R10.8](02-regras.md#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor)): "(s)", variável por posição, artigo antes de variável, "com sucesso", mensagens gerais, interjeições e ponto de exclamação. Cada alerta mostra a chave ou a linha da mensagem. 19 testes da regra e 13 testes das opções de equipe no `--teste`.
  - [`tools/gerar_regras_dicionario.py`](https://github.com/dvwinck/pts-br/blob/main/tools/gerar_regras_dicionario.py) (G4): gera `PalavrasObsoletas.yml` (nível `suggestion`) e os testes da regra a partir das entradas "Obsoleta" do 03. Nesta versão, o 03 não tem palavras obsoletas, e a regra não existe.
- 02, revisões 2 e 3: 8 regras novas.
  - [R1.10](02-regras.md#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor): não use a forma "para" do verbo PARAR se a frase também tiver a leitura de preposição (D4).
  - [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor): escreva o responsável do procedimento e de cada etapa (D14).
  - [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor): escreva cada ponto de decisão com todas as saídas (D14).
  - [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor): escreva o registro que a etapa gera (D14).
  - [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor): identifique o ambiente antes de um comando que altera ou exclui dados (D5, E5).
  - [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor): não coloque segredos na linha de comando nem no texto (D5).
  - [R10.9](02-regras.md#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor): escreva textos de validação, de acessibilidade, de link e de estado vazio com a ação.
  - [R10.10](02-regras.md#r1010-escreva-textos-de-desenvolvimento-com-um-formato-fixo-revisor): escreva textos de desenvolvimento com um formato fixo (D14).
- 02, revisão 4: [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor), "Escreva um procedimento para reverter cada alteração do ambiente de produção". A especificação tem agora 82 regras.
- 02: cada regra tem a marca `[vale]` ou `[revisor]` no título e na tabela-resumo. 12 regras têm a marca `[vale]` ([R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) passou a `[vale]` na revisão 4). 70 regras têm a marca `[revisor]` (D13).
- 03: 723 palavras aprovadas e 362 palavras não aprovadas. Vocabulário novo de API, de operação, de segurança e de processo (D12).
- 04: tabela de 86 siglas de uso geral (seção 6.1). A regra [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) isenta estas siglas (D8).
- 04: glossário-base com 270 termos (seção 6.2), 146 decisões sobre termos em inglês (seção 5.5) e 25 categorias de nomes técnicos ([NT-01](04-termos-tecnicos.md#nt-01-produtos-softwares-e-serviços-externos) a [NT-25](04-termos-tecnicos.md#nt-25-termos-de-linguagem-e-de-redação)).
- 05 (D15): cláusula de revisores fundadores (seção 9.4) e fluxo para documentos fora do Git (seção 4.5). Instrumentos de medição (seção 5.2). Prazos de PMD e período de transição (seções 7.4 e 8.3).
- [`tools/vale/PTSBR/`](https://github.com/dvwinck/pts-br/tree/main/tools/vale/PTSBR): 14 regras Vale reais (a regra `Mensagens` é da revisão 4), com casos de teste em [`tools/vale/testes/`](https://github.com/dvwinck/pts-br/tree/main/tools/vale/testes) (D16).
- [`tools/check_spec.py`](https://github.com/dvwinck/pts-br/blob/main/tools/check_spec.py): linter em Python com as mesmas regras do Vale. Modos `--spec`, `--teste`, `--metricas` e `--lista-branca`. Opções `--regras`, `--dicionario`, `--termos` e `--limite-frase pasta` para os repositórios de equipe (E10).
- [`tools/lista_branca.py`](https://github.com/dvwinck/pts-br/blob/main/tools/lista_branca.py): as formas válidas das palavras aprovadas do 03, dos termos do 04, da metalinguagem do 01 (seção 11.2) e das contrações. Verbos com as formas dos tempos aprovados e uma tabela de verbos irregulares. Siglas definidas no próprio documento (E1).
- [`tools/gerar_regras_dicionario.py`](https://github.com/dvwinck/pts-br/blob/main/tools/gerar_regras_dicionario.py): gera `PalavrasNaoAprovadas.yml` a partir do 03 e das tabelas 5.4 e 6.3 do 04. A regra encontra "deployei", "commite", "mergeie", "builde", "logue" e "dê push" (E9).
- [`tools/ci/docs-lint.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint.yml): pipeline do repositório da especificação. [`tools/ci/docs-lint-equipe.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint-equipe.yml): pipeline de um repositório de equipe, com as regras de uma versão fixa (E10). Os 2 pipelines dão ao token apenas `contents: read` e usam `actions/checkout@v5` (Node 24). Esta versão não verificou o hash do commit desta tag: o comentário de cada pipeline e o 05, seção 6.7, pedem o hash antes do uso em produção. O passo do Vale compara o hash SHA-256 do pacote com a lista de hashes da página de versões do Vale.
- [`tools/vale/testes/`](https://github.com/dvwinck/pts-br/tree/main/tools/vale/testes): 160 testes de regra (`check_spec.py --teste`). A revisão 2 tinha 87 testes. Os testes novos têm: verbos com radical estrangeiro, falsos positivos ("o arquivo onde", "é o mesmo", "dá a mensagem", "Ceará"), "10 KB", "100 Mbps", "R$ 1.500,00" e frases longas com código e negrito.
- 05: auditoria das decisões do mantenedor (seção 3.5), procedimentos com o bloco de [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) e as linhas "Registro:" (seções 4.1, 4.5 e 7.3), linha `[LINTER]` com os alertas de cada regra (M6) e colunas de data e de prioridade no registro de decisões (M7) (E11).

### Alterado
- Revisão 4:
  - [`tools/lista_branca.py`](https://github.com/dvwinck/pts-br/blob/main/tools/lista_branca.py) (G2): um termo composto do 04 e uma locução do 03 são unidades. A lista branca não aceita a parte do termo fora do termo ("o ponto de decisão" não vale por causa de "ponto de exclamação"). O plural de "-ção" e "-são" é "-ções" e "-sões" ("publicaçãos" não é gerado). Um substantivo não recebe feminino. Uma entrada "Obsoleta" do 03 continua válida.
  - `tools/check_spec.py --metricas` (G4): M2 conta cada palavra 1 vez. Uma palavra que o linter e a lista branca mostram na mesma linha conta 1 vez. Um tempo verbal não aprovado de um verbo aprovado ("enviava") é um desvio de CK-3.1, e M2 não conta este desvio. M2 não conta as tabelas.
  - [`tools/gerar_regras_dicionario.py`](https://github.com/dvwinck/pts-br/blob/main/tools/gerar_regras_dicionario.py) (G6): a regra não tem as formas iguais a uma palavra aprovada do 03 ou do 04 ("seta", "busca", "perfil"). Uma forma dentro de um termo composto aprovado não gera alerta ("roda do mouse"). O plural de "-il", "-el" e "-ol" está correto ("perfis").
  - [`tools/ci/docs-lint-equipe.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint-equipe.yml) (G5): o código 2 do Vale (erro de configuração ou de regra) falha o job também no Piloto. O passo Python usa `--config` e `--limite-frase auto`. Variáveis `GLOSSARIO` e `MENSAGENS`. Passo "Métricas M1 e M2" no resumo do job. Um item de `DOCS` que não existe não para o job, e a lista branca não bloqueia. Instrução para um repositório da especificação privado (`PTSBR_TOKEN`).
  - [`tools/ci/docs-lint.yml`](https://github.com/dvwinck/pts-br/blob/main/tools/ci/docs-lint.yml): os critérios 1 e 2 da seção 8.5 (`build.py` e `build.py --render` igual ao 03). O job `vale` grava a saída no arquivo de registro.
  - [`tools/vale/.vale.ini`](https://github.com/dvwinck/pts-br/blob/main/tools/vale/.vale.ini): `PTSBR.Mensagens = NO` nos arquivos Markdown.
  - 05, seções 3.2 e 3.3: o critério "por documento" usa M1 e M2 na submissão. A tag `v1.0.0` é um critério de entrada do Piloto. Anexo A: com 5 a 9 leitores, **Melhor ou igual** cumpre o critério do Piloto, e **Pior** passa a **Inconclusivo**.
  - 05, seção 3.4: a amostra mensal tem os documentos publicados no mês (no máximo 10), sem repetir um documento sem alteração.
  - 05, seções 5.7 e 5.9: M5 (duração) é a mediana da fase. Prazo do revisor: 3 dias úteis na primeira revisão e 2 dias úteis depois de uma correção.
  - 05, seção 7.3: "Pendente" aguarda 10 dias úteis. A publicação inclui as alterações do 04, as palavras obsoletas (estado `O`), os critérios da seção 8.5 e o aviso às equipes. Triagem urgente em 1 dia útil.
  - 05, seções 6.4, 8.3 e 8.4: a alteração para `error` é MINOR porque não altera a conformidade. No fim da transição MAJOR, o mantenedor aplica a seção 6.4. O revisor usa a última PATCH da versão declarada, e `PTSBR_REF` usa a tag desta PATCH.
  - 02 (G1, G2, G3): [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) tem uma tabela com a opção de alvo e o passo de verificação de cada ferramenta (`kubectl`, `helm`, `psql`, `aws`, `terraform`). [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) não usa `PGPASSWORD`: o segredo está em um arquivo com a permissão 600, por exemplo `~/.pgpass`. A tabela de níveis de [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) e a tabela da regra D8 do 03 têm o mesmo texto. Os textos normativos usam as palavras do 03 com o significado aprovado (lista abaixo).
  - 03 e 04 (G1, G6): significados novos ou corrigidos. ALTERAÇÃO no lugar de "mudança", exceto em "solicitação de mudança". ABRIR apenas para um arquivo, uma janela ou uma conexão. Para um chamado, um PMD ou um PMR, use CRIAR. USO é a ação de usar. A quantidade de um recurso que um sistema usa é CONSUMO. HORA é um momento do dia. Para uma duração, use o símbolo "h". ESCRITA é a ação de escrever um texto. Para dados, use GRAVAÇÃO. DAR é o verbo geral. Para uma tarefa, um chamado ou um papel de acesso, use ATRIBUIR. Termos novos no 04, seção 6.2: "banco", "elemento", "endereço", "analista", "provedor de identidade", "perfil", "busca", "seta" e "roda do mouse".
  - 06 (G3): Exemplo 9 com o `pg_dump` do estado atual antes do `pg_restore --clean`, o backup escolhido pela hora de início da migração com defeito, o comando `pg_restore --list`, o comando `ANALYZE` e o host de administração `adm-01`. Exemplos 2, 5 e 9 com o arquivo `~/.pgpass` e a permissão 600. Exemplo 1 com o comando `kubectl auth can-i`. Exemplo 10 novo: comunicados de um incidente na página de status.
  - 05 e README (G1): CRIAR para chamado, PMD, PMR e ação corretiva ("Crie um PMD", "cria uma ação corretiva"). "Atribua a tarefa". "PMD sem decisão". ALTERAÇÃO no lugar de "mudança", exceto nos nomes "pedido de mudança no dicionário" e "pedido de mudança de regra". ESTAR no lugar de FICAR para lugar. "pode" apenas para permissão ou capacidade. A tabela "Alterações" do 06.
- 01, seção 2.1: o escopo tem os procedimentos de processo (POP) e os textos de desenvolvimento (D14).
- 01, seção 8.2: o revisor aplica a lista de verificação inteira. O linter encontra apenas parte dos desvios (D13).
- [R3.9](02-regras.md#r39-use-apenas-ser-estar-e-ficar-como-verbos-de-ligação-revisor): os verbos de ligação aprovados são SER, ESTAR e FICAR (D3).
- [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor): "acima" e "abaixo" apenas para o conteúdo imediatamente antes ou depois. Para comparar valores, use "maior que" e "menor que" (D2).
- Seção 7: o nível do aviso depende da reversibilidade e da exposição. Os exemplos de [R7.5](02-regras.md#r75-escreva-um-risco-por-aviso-revisor) e de [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) seguem este critério (D5).
- [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale), 03, 04 ([NT-22](04-termos-tecnicos.md#nt-22-unidades-de-medida)) e 05 (D7): símbolo da unidade depois do número. Espaço como separador de milhar. kB = 1 000 B e KiB = 1 024 B.
- [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) e 04 ([NT-24](04-termos-tecnicos.md#nt-24-valores-de-estado-do-sistema)): "estado" em prosa. Um valor de estado de CLI, de API ou de log usa o formato de código. Um valor de estado da interface usa o negrito (D6). O título de [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) usa "significado" no lugar de "função".
- [R1.9](02-regras.md#r19-use-onde-apenas-para-lugar-vale): a verificação descreve a lista de nomes de lugar da regra Vale `OndeRelativo`.
- 04 e 06: "papel de acesso" para RBAC e IAM. "Função" é apenas a função de código. "Perfil de acesso" não é aprovado (D9).
- 04: "registry" é um nome técnico. Um registry contém repositórios de imagens (D10).
- 04: PASSAR tem um significado: fornecer um argumento a uma função, a um comando ou a um endpoint. Para o resultado de um teste, use FALHAR ou SUCESSO (D11).
- 05: a lista de verificação do revisor cobre as 82 regras. A seção 6 descreve apenas as ferramentas que existem.
- 05, seção 4.4: os 3 resultados não têm sobreposição. Um S1 com o estado `CORRIGIDO` não reprova o documento. Um documento sem a versão declarada tem o resultado "Reprovado" (CK-0.1 passa para S2) (E11).
- 05, seção 5.2: M1 e M2 medidos na submissão e na publicação. A meta usa o valor da submissão. M2 conta apenas as palavras confirmadas (E11).
- 05, seções 7.4 e 8.1: um PMD urgente aceito é publicado numa versão PATCH em até 5 dias úteis. A alteração de uma regra do linter para o nível `error` é uma versão MINOR (E11).
- 05, seções 2.1, 3.2 e 9.4: um revisor fundador de outra equipe é o auditor do Piloto. O substituto do mantenedor decide os pedidos do mantenedor. A RACI tem a coluna "Auditor" (E11).
- 05, Anexo A: 3 resultados (**Melhor ou igual**, **Inconclusivo**, **Pior**) e um responsável pelo teste (E11).
- 05: números com algarismos e "maior que" ou "menor que" para comparar valores. "Glossário do projeto" no lugar de "glossário do produto".
- `PalavrasNaoAprovadas`: não alerta "status" em "página de status" (04). A regra lê também a coluna "Formas flexionadas não aprovadas" da tabela 5.4 do 04.
- `PalavrasNaoAprovadas`, `OndeRelativo`, `VerboSuporte`, `OMesmo`, `FuturoSimples`, `Unidades` e `SeparadorMilhar`: falsos positivos e falsos negativos da revisão 2 corrigidos.
- `tools/`: os scripts de trabalho da revisão foram para `reviews/scripts-de-trabalho/`.
- README: contagens reais de regras, de palavras do dicionário, de siglas e de termos do glossário-base.
- 05, README e 03 (revisão 3, varredura final): um termo para cada conceito, com as palavras aprovadas do 03.
  - ADOÇÃO: "fases de adoção" e os títulos das seções 3 e 10 do 05 ("Adoção do PTS-BR em fases", "Riscos da adoção e ações"). A tabela da seção 1 do 05 define "adoção" e "fase de adoção". USO tem apenas o significado do 03: a ação de usar um item, uma regra ou um recurso. A quantidade de um recurso que um sistema usa é CONSUMO.
  - SUBMISSÃO: M1, M2 e M3 "na submissão" e "na publicação" (05, seções 4.1, 5.2, 5.5, 5.8 e 5.9 e Anexo C). A tabela da seção 1 do 05 define "submissão".
  - REPROVAR: o resultado da seção 4.4 do 05 é "Reprovado". RECUSAR continua para um pedido: um PMD, uma exceção ou um chamado.
  - 03: a definição de ADOÇÃO não usa "uso". "isto é" e "ou seja": "divida a frase em 2 frases". "desejar": "a condição exata".
- [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor): a frase da consequência num diálogo de confirmação usa o sujeito de [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor): o objeto afetado ou, como reserva, "o sistema". O Exemplo 4 do 06 segue esta regra.

### Corrigido
- Autoconformidade de forma (D1, E1, G2): o README, o 01, o 02, o 04, o 05 e os textos PTS-BR do 06 não usam as palavras da lista "Não aprovada" do 03 (`check_spec.py --spec`). O modo `--lista-branca` mostra 62 palavras fora da lista branca em 74 430 palavras do texto normativo (0,08%), com os termos compostos como unidades. A lista branca verifica a forma, não o significado. O critério 6 acima mostra o resultado por arquivo.
- 02, 05 e 06: palavras não aprovadas em prosa. Exemplos: "função" com o significado geral, "principalmente", "terceira", "demais", "muitos", "status" e PASSAR com o significado de "ter sucesso".
- Frases com mais de 25 palavras (texto descritivo) ou mais de 20 palavras (procedimento) no 01, no 02, no 04 e no 06.
- `PalavrasNaoAprovadas`: não alerta "status" no nome técnico "código de status" nem um literal em negrito ou em código ([R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor)). O gerador não cria a forma "statuss".
- `check_spec.py --spec`: uma menção entre aspas conta como 1 palavra, e a divisão das frases fica correta.
- 02, seção 7: "A volta automática do sistema" passa a "Quando o sistema volta ao estado anterior de forma automática". "volta" como substantivo não é aprovado. O mesmo no 05 (seção 3) e no Exemplo 7 do 06.
- 06, Exemplo 3: o tipo JSON do campo `erros` é "array" (04, seção 5.5), não "lista".
- 04, seção 6.1: o README e esta entrada têm o número real de siglas da tabela (86).

## [1.0.0-rc1] - 2026-11-18

Revisão editorial de consistência entre os arquivos 01 a 05. Esta versão não
tem PMD nem PMR: as alterações alinham os arquivos às decisões que já existiam.
O arquivo [`06-exemplos.md`](06-exemplos.md) não faz parte desta revisão.

### Adicionado
- Dicionário: `ESPERADO (adj)`, para "o resultado esperado" ([R5.5](02-regras.md#r55-escreva-o-resultado-esperado-em-uma-frase-separada-revisor)). O verbo "esperar" continua não aprovado.
- Dicionário: `time (s)`, não aprovada. Use EQUIPE.
- Dicionário, regra D11: "nós", plural do nome técnico "nó", é aprovado depois de artigo, contração ou número. O pronome "nós" continua não aprovado.
- 04, seção 5.5: decisão "node" → "nó" (Português).
- 05, seção 4.2: coluna "Regras" com os IDs de [`02-regras.md`](02-regras.md) em cada item do checklist. Itens novos para as regras sem item: CK-1.6, CK-2.2, CK-3.5, CK-4.3, CK-5.5, CK-5.6, CK-6.3, CK-6.4, CK-7.4, CK-8.4, CK-9.3, CK-10.4.

### Alterado
- [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor) e princípio P1 (01): registram a exceção de "a" (artigo e preposição) e "que" (pronome e conjunção), com justificativa. A regra D6 do dicionário cita P1 e [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor).
- [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor) e regra D3 do dicionário: o particípio de um verbo aprovado é adjetivo aprovado. O particípio de um verbo não aprovado precisa de entrada própria.
- `IR (v)`, regra D2, [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale) e seção 5.1 (01): IR tem um só significado (mover). "Vai" + infinitivo é uma forma verbal com "ir" auxiliar, não um segundo significado.
- [R9.1](02-regras.md#r91-escreva-para-o-leitor-na-forma-você-revisor), 04 (seção 1) e entrada "nós": o linter detecta "nós" sem artigo, contração ou número antes.
- [R1.2](02-regras.md#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor) e P1 (01): o significado de "executar" segue o dicionário (comando, script, programa ou deploy). O significado de "salvar" segue o verbo técnico de 04, seção 4.2.
- [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale) e [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor): "Faça um backup", como em 03 e em 04, seção 5.5.
- [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor): a exceção vale para as siglas do glossário-base de 04 (seção 6), como na regra T4 de 04.
- [R2.1](02-regras.md#r21-use-no-máximo-3-substantivos-em-uma-cadeia-com-de-revisor) e T7 (04): um termo composto do glossário-base, por exemplo "banco de dados", conta como 1 substantivo nos dois arquivos.
- [R6.3](02-regras.md#r63-use-conectores-simples-revisor): o conector aprovado é "portanto". "Por isso" não é aprovado no dicionário.
- 05: comentários de revisão no formato `[S2][R4.2]`, também no README e em 01, seção 8.2.
- 05, seção 5.1: as regras de contagem de palavras seguem [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale).
- 05, seção 6: as regras do Vale citam o ID da regra ([R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale), [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale)). A regra "o mesmo" cita [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), não a Seção 4. Os padrões usam `nonword: true` com `(?<!\p{L})` e `(?!\p{L})`, porque `\b` do Vale reconhece apenas letras ASCII. Versão do Vale no CI: 3.27.0.
- 05, seção 9.3: módulos da trilha do revisor com os IDs RV1 a RV3, para não confundir com IDs de regra.

### Removido
- 05, seção 4.2: CK-9.1 (título e leitor-alvo) e CK-9.2 (comandos testados). Os dois itens não têm regra em [`02-regras.md`](02-regras.md). A exatidão técnica fica com a revisão técnica (05, seção 2.1).
- 05, seção 4.2: a pergunta "não mostra código de erro sem explicação" de CK-10.3. [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) não tem esta exigência.

### Corrigido
- Exemplos PTS-BR de 01, 02, 04 e 05 com palavras não aprovadas: time, apagar, encerrar, mudar, exigir, esperar, guardar, conseguir, avisar, deixar, esse, por isso, só, errado, incluir, reduzir. Os avisos de [R7.5](02-regras.md#r75-escreva-um-risco-por-aviso-revisor) e [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor) também usavam "desligar" fora do significado aprovado (energia de um equipamento). Um script comparou os exemplos com as entradas "Não aprovada" do dicionário.
- Dicionário: exemplos de `TER (v)` e `COLETAR (v)` com número em algarismos ("3 nós"), conforme [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale).
- [`tools/build.py`](https://github.com/dvwinck/pts-br/blob/main/tools/build.py): a verificação de vazamento compara as palavras com acento. Antes, "nos" (em + os) era igual a "nós".
- 05, seção 5.5: a referência de Martins et al. (1996) marca o número da série como "[conferir]".
- 05, seção 6.7: as referências ao checklist usam os IDs novos.

---

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · **Versões**

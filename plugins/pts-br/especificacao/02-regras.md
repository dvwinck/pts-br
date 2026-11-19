# PTS-BR: Português Técnico Simplificado

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · **02 Regras** · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

## Parte 2: Regras de escrita

Versão 1.0.0, 2026-11-18

Esta parte contém 82 regras em 10 seções. Leia [`01-introducao.md`](01-introducao.md) antes desta parte. A seção 10 de [`01-introducao.md`](01-introducao.md) explica a estrutura de cada regra. A seção 5 de [`01-introducao.md`](01-introducao.md) explica as decisões gramaticais de base.

| Seção | Assunto | Regras |
|---|---|---|
| 1 | Palavras | [R1.1](#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) a [R1.10](#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor) |
| 2 | Cadeias nominais | [R2.1](#r21-use-no-máximo-3-substantivos-em-uma-cadeia-com-de-revisor) a [R2.4](#r24-nomeie-um-conceito-longo-com-um-nome-curto-revisor) |
| 3 | Verbos | [R3.1](#r31-use-apenas-os-tempos-verbais-aprovados-vale) a [R3.10](#r310-use-o-verbo-específico-não-um-verbo-geral-revisor) |
| 4 | Frases | [R4.1](#r41-escreva-uma-instrução-ou-uma-afirmação-por-frase-revisor) a [R4.6](#r46-use-no-máximo-uma-oração-subordinada-por-frase-revisor) |
| 5 | Procedimentos | [R5.1](#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) a [R5.13](#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) |
| 6 | Texto descritivo | [R6.1](#r61-comece-o-parágrafo-com-a-frase-principal-revisor) a [R6.6](#r66-não-escreva-instruções-em-texto-descritivo-revisor) |
| 7 | Avisos de segurança | [R7.1](#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) a [R7.9](#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) |
| 8 | Pontuação e formatação | [R8.1](#r81-termine-as-frases-com-ponto-final-revisor) a [R8.9](#r89-escreva-espaços-reservados-em-um-formato-único-revisor) |
| 9 | Práticas de escrita | [R9.1](#r91-escreva-para-o-leitor-na-forma-você-revisor) a [R9.5](#r95-escreva-listas-completas-revisor) |
| 10 | Interface, mensagens de software e textos de desenvolvimento | [R10.1](#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor) a [R10.10](#r1010-escreva-textos-de-desenvolvimento-com-um-formato-fixo-revisor) |

Cada regra tem uma marca de verificação:

- `[vale]`: o pacote de regras Vale do PTS-BR detecta o padrão principal da regra. O revisor confirma as ocorrências que a ferramenta não decide.
- `[revisor]`: apenas o revisor verifica a regra.

O revisor aplica todas as regras, com e sem a marca `[vale]` ([`01-introducao.md`](01-introducao.md), [seção 8.2](01-introducao.md#82-revisar-um-texto-em-pts-br)). A tabela-resumo no fim desta parte lista todas as regras e as marcas.

---

## Seção 1: Palavras

### R1.1 Use apenas palavras aprovadas e termos técnicos `[vale]`

**Enunciado:** Use apenas palavras aprovadas em [`03-dicionario.md`](03-dicionario.md) e termos de uma categoria de [`04-termos-tecnicos.md`](04-termos-tecnicos.md). As palavras dentro de literais, rótulos de interface e mensagens citadas estão fora desta regra.

**Justificativa:** Um vocabulário fechado permite ao leitor e ao tradutor conhecer todas as palavras do texto.

**Verificação:** O Vale detecta as palavras não aprovadas de [`03-dicionario.md`](03-dicionario.md) e as formas flexionadas destas palavras. O revisor verifica as palavras que não estão no 03 nem no 04.

**Não aprovado:** Rode o script de migração antes de subir a aplicação.

**PTS-BR:** Execute o script de migração antes de iniciar a aplicação.

### R1.2 Use cada palavra apenas com o significado aprovado `[revisor]`

**Enunciado:** Use uma palavra aprovada apenas com o significado que [`03-dicionario.md`](03-dicionario.md) define para a palavra. Se você precisar de outro significado, use a palavra que o dicionário indica para este significado.

**Justificativa:** Com uma palavra de 2 significados, o leitor precisa escolher um significado. O leitor não nativo conhece um significado e aplica este significado em todas as ocorrências.

**Verificação:** O revisor compara o significado de cada verbo e de cada substantivo principal com o significado do dicionário.

**Não aprovado:** Execute a revisão do código antes do merge.

**PTS-BR:** Revise o código antes do merge.

**Não aprovado:** O backup salvou o projeto depois da falha do disco.

**PTS-BR:** A equipe recuperou o projeto com o backup depois da falha do disco.

**Não aprovado:** Atribua a função `cluster-admin` à conta de serviço `deploy`.

**PTS-BR:** Atribua o papel de acesso `cluster-admin` à conta de serviço `deploy`.

Nestes exemplos, "executar" significa "fazer um computador processar um comando, um script, um programa ou um deploy" ([`03-dicionario.md`](03-dicionario.md)). "Salvar" é um verbo técnico de interface e significa "gravar no armazenamento as alterações de um arquivo, de um documento ou de um formulário, por uma ação do usuário" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 4.2](04-termos-tecnicos.md#42-lista-de-verbos-técnicos)). Para a ação do sistema, use "gravar". "Função" é a função de código. "Papel de acesso" é o conjunto de permissões de uma identidade ([`04-termos-tecnicos.md`](04-termos-tecnicos.md)).

### R1.3 Use cada palavra apenas na classe gramatical aprovada `[revisor]`

**Enunciado:** Use uma palavra aprovada apenas na classe gramatical que [`03-dicionario.md`](03-dicionario.md) indica: substantivo, verbo, adjetivo, advérbio, preposição ou conjunção. Não use um particípio como preposição. Não use um adjetivo como substantivo se o dicionário não aprovar esta classe. O particípio de um verbo aprovado é aprovado como adjetivo, com o significado do verbo ("o pacote instalado"). O particípio de um verbo não aprovado precisa de uma entrada própria de adjetivo no dicionário, por exemplo `ESPERADO (adj)` ([`03-dicionario.md`](03-dicionario.md), regra D3).

**Exceção:** Estas formas iguais são aprovadas ([`03-dicionario.md`](03-dicionario.md), regras D6 e D7):

- "a" é artigo e preposição, e "que" é pronome relativo e conjunção. O português não tem outra palavra para estas classes. O artigo está antes de um substantivo feminino, e o pronome "que" tem um substantivo antes.
- Uma forma de um verbo aprovado é igual a uma palavra aprovada de outra classe: "a falha" e "o deploy falha", "o teste" e "Teste a restauração", "o limite" e "Limite o número de conexões". A estrutura da frase mostra a classe.

A regra [R1.10](#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor) é sobre a única forma em que a estrutura da frase não mostra a classe: a forma "para" do verbo PARAR.

**Justificativa:** No português, a mesma forma é substantivo, adjetivo ou particípio de acordo com a frase. Uma classe fixa para cada palavra resolve esta dúvida de leitura.

**Verificação:** O revisor confirma a classe de cada palavra com mais de uma classe possível no dicionário.

**Não aprovado:** Dado o volume de logs, aumente o disco.

**PTS-BR:** O servidor grava 80 GB de logs por dia. Aumente o disco para 500 GB.

**Não aprovado:** Adicione a linha no final do arquivo.

**PTS-BR:** Adicione a linha no fim do arquivo.

Nestes exemplos, "dado" é aprovado apenas como substantivo ("os dados do cliente"), e "final" é aprovado apenas como adjetivo ("a versão final").

### R1.4 Use uma palavra para cada conceito `[revisor]`

**Enunciado:** Para um conceito, use sempre a mesma palavra em todo o documento. Não use 2 sinônimos para o mesmo conceito, por exemplo "pasta" e "diretório", ou "excluir" e "apagar". Use a palavra que [`03-dicionario.md`](03-dicionario.md) aprova para o conceito.

**Justificativa:** O leitor entende uma palavra diferente como um conceito diferente. O tradutor também traduz 2 palavras diferentes de 2 formas.

**Verificação:** O revisor procura no documento os sinônimos, por exemplo "pasta" e "diretório".

**Não aprovado:** Crie o diretório `backup`. Depois, copie os arquivos para a pasta `backup`.

**PTS-BR:** Crie a pasta `backup`. Depois, copie os arquivos para a pasta `backup`.

### R1.5 Escreva os artigos e o substantivo de classe antes de literais `[revisor]`

**Enunciado:** Escreva o artigo antes de cada substantivo comum. Antes de um literal, escreva um substantivo que indica a classe do literal: "o arquivo", "o comando", "a variável", "a ferramenta", "o botão". A preposição faz a contração com o artigo deste substantivo, não com o literal.

**Justificativa:** Em um texto sem artigos, a classe de cada palavra é ambígua. O substantivo de classe define o gênero do artigo e evita contrações com nomes em inglês ou em código.

**Verificação:** O revisor procura uma preposição ou uma contração ("no", "na", "do", "da", "ao", "pelo") imediatamente antes de um literal em formato de código.

**Não aprovado:** Abra arquivo de configuração e altere porta.

**PTS-BR:** Abra o arquivo de configuração. Altere a porta.

**Não aprovado:** Adicione a chave no `settings.json`.

**PTS-BR:** Adicione a chave no arquivo `settings.json`.

### R1.6 Use a crase apenas antes de palavra feminina com artigo e antes de horas `[revisor]`

**Enunciado:** Escreva "à" ou "às" apenas nestas situações:

- A preposição "a" encontra o artigo feminino "a" ou "as": "Conecte o computador à VPN."
- Antes de uma hora: "às 02:00 UTC", "à 01:00 UTC".
- Nas expressões "à direita" e "à esquerda".

Não use crase antes de verbo, de palavra masculina, de literal em formato de código e de "partir". Não use crase antes de "uma", exceto na hora "à 01:00 UTC".

**Justificativa:** Um erro de crase altera a estrutura e o significado da frase.

**Verificação:** O revisor verifica cada "à" e cada "às" e procura a falta de crase antes de palavra feminina com artigo.

**Não aprovado:** Conecte o computador a VPN da empresa.

**PTS-BR:** Conecte o computador à VPN da empresa.

**Não aprovado:** À partir da versão 3.0, o endpoint retorna JSON.

**PTS-BR:** A partir da versão 3.0, o endpoint retorna JSON.

**Não aprovado:** Envie o relatório à `equipe-sre`.

**PTS-BR:** Envie o relatório ao canal `equipe-sre`.

**Não aprovado:** O backup começa as 02:00 UTC.

**PTS-BR:** O backup começa às 02:00 UTC.

### R1.7 Use estrangeirismos apenas da lista de termos técnicos `[vale]`

**Enunciado:** Use uma palavra estrangeira apenas se [`04-termos-tecnicos.md`](04-termos-tecnicos.md) listar a palavra. Use a palavra apenas como substantivo, com o gênero que a lista define. No plural, use a forma do inglês ("commits", "tokens", "proxies"). Não use verbos com radical estrangeiro ("deployar", "commitar", "mergear", "buildar", "startar", "setar", "printar", "upar", "logar"). Para a ação, use um verbo aprovado com o substantivo técnico.

**Justificativa:** Cada termo estrangeiro aumenta o tempo de leitura para um leitor que não lê inglês. Os verbos com radical estrangeiro não têm conjugação estável e não estão no dicionário.

**Verificação:** O Vale detecta os verbos com radical estrangeiro da tabela de [`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 5.4](04-termos-tecnicos.md#54-verbos-com-radical-estrangeiro), e as formas flexionadas destes verbos (regra `PalavrasNaoAprovadas`). O modo `--lista-branca` da ferramenta [`tools/check_spec.py`](https://github.com/dvwinck/pts-br/blob/main/tools/check_spec.py) mostra as outras palavras que não estão no 03 nem no 04. O revisor compara cada palavra estrangeira com a lista de [`04-termos-tecnicos.md`](04-termos-tecnicos.md).

**Não aprovado:** Commite as alterações e sete a variável `PORT`.

**PTS-BR:** Crie um commit com as alterações. Defina a variável `PORT`.

**Não aprovado:** Logue no console da AWS.

**PTS-BR:** Entre no console da AWS.

### R1.8 Não use "o mesmo" como pronome e repita o substantivo se o referente for ambíguo `[vale]`

**Enunciado:** Não use "o mesmo", "a mesma", "os mesmos" ou "as mesmas" no lugar de um substantivo. Para indicar um item do texto, use "este" ou "esta" com o substantivo. Não use "esse", "essa", "isso", "ele", "ela" nem "aquele". Se "este" puder indicar mais de um substantivo, repita o substantivo. Use "seu" e "sua" apenas para o leitor. Para outra pessoa ou outro objeto, repita o substantivo.

**Justificativa:** Com "o mesmo" como pronome, o leitor precisa procurar o referente em frases anteriores. Em português, "seu" indica o leitor ou a pessoa da frase, e o leitor não sabe qual dos 2. O substantivo repetido resolve esta dúvida.

**Verificação:** O Vale detecta "o mesmo", "a mesma", "os mesmos" e "as mesmas" antes de pontuação, de verbo ou de conjunção. A regra [R1.1](#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) detecta "esse", "isso" e "ele". O revisor verifica o referente de cada "este".

**Não aprovado:** Baixe o certificado e instale o mesmo no servidor.

**PTS-BR:** Baixe o certificado. Instale o certificado no servidor.

**Não aprovado:** O cliente envia o token ao servidor. Ele valida a assinatura.

**PTS-BR:** O cliente envia o token ao servidor. O servidor valida o token.

**Não aprovado:** O administrador altera a sua senha.

**PTS-BR:** O administrador altera a senha do usuário.

**Aprovado:** Use a mesma versão em todos os nós.

### R1.9 Use "onde" apenas para lugar `[vale]`

**Enunciado:** Use "onde" apenas para um lugar físico ou um local de armazenamento: pasta, servidor, região, disco. Para situação, tempo, versão, processo ou documento, use "em que" ou escreva a frase de novo sem "onde".

**Justificativa:** "Onde" como pronome relativo geral não mostra como as ideias estão ligadas. O leitor não nativo entende "onde" sempre como lugar.

**Verificação:** O Vale marca "onde" quando a palavra antes de "onde" não está na lista de nomes de lugar da regra. A lista tem estes nomes: "pasta", "servidor", "região", "disco", "máquina", "local", "lugar", "host", "bucket", "cluster", "caminho", "volume" e "zona". O revisor confirma se cada "onde" marcado indica um lugar. O revisor também verifica "onde" depois de um nome de lugar com outras palavras entre o nome e "onde" ("a pasta do projeto onde").

**Não aprovado:** Em cenários onde a fila está cheia, a API retorna o código 503.

**PTS-BR:** Quando a fila está cheia, a API retorna o código 503.

**Não aprovado:** A versão 2.0, onde o endpoint mudou, exige um token novo.

**PTS-BR:** A versão 2.0 alterou o endpoint. Na versão 2.0, o endpoint precisa de um token novo.

**Aprovado:** Abra a pasta onde o agente grava os logs.

### R1.10 Não use a forma "para" do verbo PARAR se a frase também tiver a leitura de preposição `[revisor]`

**Enunciado:** A forma "para" do verbo PARAR, na 3ª pessoa do singular, é igual à preposição "para". Não escreva esta forma do verbo antes de um artigo, de um substantivo, de um número ou de um literal. Escreva a frase de novo com uma destas soluções:

- Escreva o sujeito no plural: "os pods param".
- Escreva "não funciona" ou "não responde".
- Use outra estrutura: "o serviço recusa mensagens novas".

A forma "para" do verbo no fim da frase é aprovada.

**Justificativa:** Antes de um complemento, o leitor lê a forma "para" como preposição, e a frase tem outro significado. O leitor não nativo conhece "para" como preposição antes de conhecer o verbo PARAR.

**Verificação:** O revisor procura "para" entre um sujeito no singular e um artigo, um substantivo, um número ou um literal.

**Não aprovado:** O reinício para todos os pods por 5 min.

**PTS-BR:** Todos os pods param por 5 min quando o cluster reinicia.

**Não aprovado:** Um valor maior que 500 esgota a memória e para o banco `pedidos`.

**PTS-BR:** Com um valor maior que 500, o servidor não tem memória livre. O banco `pedidos` não responde.

**Aprovado:** Quando a fila fica cheia, o serviço para.

---

## Seção 2: Cadeias nominais

Uma cadeia nominal é uma sequência de substantivos ligados pela preposição "de" ou pelas contrações "do", "da", "dos" e "das".

### R2.1 Use no máximo 3 substantivos em uma cadeia com "de" `[revisor]`

**Enunciado:** Uma cadeia nominal tem no máximo 3 substantivos. Um termo técnico composto do glossário-base de [`04-termos-tecnicos.md`](04-termos-tecnicos.md) (seção 6) conta como 1 substantivo, por exemplo "banco de dados". Se uma cadeia tiver 4 ou mais substantivos, escreva a frase de novo com um verbo, com uma oração com "que" ou com 2 frases.

**Justificativa:** Em uma cadeia longa, o leitor não identifica qual substantivo é o núcleo. "O arquivo de configuração do servidor" tem 3 substantivos e é aprovado.

**Verificação:** O revisor conta os substantivos ligados por "de", "do", "da", "dos" e "das" em sequência.

**Não aprovado:** Altere o valor do parâmetro de tempo de expiração da sessão do usuário.

**PTS-BR:** A sessão do usuário expira depois de um tempo fixo. Altere este tempo no parâmetro `session_timeout`.

### R2.2 Escreva o adjetivo imediatamente depois do substantivo `[revisor]`

**Enunciado:** Escreva o adjetivo imediatamente depois do substantivo que o adjetivo descreve. Se o adjetivo puder descrever 2 substantivos da cadeia, escreva a frase de novo.

**Justificativa:** Em "o backup do banco antigo", o leitor não sabe qual item é antigo. Com 2 substantivos do mesmo gênero e do mesmo número, a gramática não resolve esta dúvida.

**Verificação:** O revisor verifica cada adjetivo depois de uma cadeia com 2 ou mais substantivos do mesmo gênero e do mesmo número.

**Não aprovado:** Restaure o backup do servidor antigo.

**PTS-BR:** Restaure o backup de 2026-11-17 do servidor `db-01`.

### R2.3 Não use a ordem do inglês em substantivos compostos `[revisor]`

**Enunciado:** Escreva o núcleo antes do modificador, na ordem do português. Não escreva compostos com a ordem do inglês ("o status code", "a user session"). Exceção: um termo composto que [`04-termos-tecnicos.md`](04-termos-tecnicos.md) mantém em inglês, sem tradução.

**Justificativa:** A ordem do inglês usa 2 gramáticas na mesma expressão. O leitor que não lê inglês não identifica o núcleo.

**Verificação:** O revisor verifica cada sequência de 2 ou mais palavras em inglês que não está na lista de termos técnicos.

**Não aprovado:** Verifique o status code da response.

**PTS-BR:** Verifique o código de status da resposta.

**Não aprovado:** Configure o session timeout.

**PTS-BR:** Configure o tempo limite da sessão.

### R2.4 Nomeie um conceito longo com um nome curto `[revisor]`

**Enunciado:** Se um conceito precisar de mais de 3 substantivos, defina um nome curto na primeira ocorrência do conceito. Use apenas este nome curto nas outras partes do documento.

**Justificativa:** O nome curto mantém as frases dentro dos limites da regra [R4.2](#r42-escreva-frases-dentro-do-limite-de-palavras-vale). Um nome fixo também cumpre a regra [R1.4](#r14-use-uma-palavra-para-cada-conceito-revisor).

**Verificação:** O revisor confirma que o documento define o nome curto antes do primeiro uso e que o documento não usa outras formas do nome.

**Não aprovado:** O serviço de envio de notificações de pagamento por e-mail usa a fila `billing`. Se o notificador de pagamento parar, a fila acumula mensagens.

**PTS-BR:** Neste documento, *serviço de notificação* é o serviço que envia por e-mail as notificações de pagamento. O serviço de notificação usa a fila `billing`. Quando o serviço de notificação não funciona, o número de mensagens da fila aumenta.

---

## Seção 3: Verbos

### R3.1 Use apenas os tempos verbais aprovados `[vale]`

**Enunciado:** Use apenas estas formas verbais:

- Presente do indicativo: "A API retorna um token."
- Pretérito perfeito: "O deploy falhou."
- Futuro com "ir" + infinitivo: "O sistema vai enviar um e-mail." Nesta forma, "ir" é um verbo auxiliar de tempo, no presente ("vai", "vão"). Esta forma não é um significado de `IR (v)`, que significa apenas "mover para outro lugar" ([`03-dicionario.md`](03-dicionario.md), regra D2).
- Imperativo da forma "você": "Reinicie o serviço."
- Futuro do subjuntivo em condições (regra [R3.2](#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor)).
- Infinitivo flexionado depois de uma preposição: "Aguarde até os pods iniciarem.", "Antes de os testes terminarem, não feche o terminal."
- Infinitivo depois de "poder", "dever", "precisar", "ir" e de uma preposição: "Você pode cancelar a operação.", "Reinicie o serviço para limpar o cache."
- Infinitivo, particípio e gerúndio nas construções que as regras [R3.3](#r33-use-a-voz-ativa-revisor), [R3.6](#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale) e [R5.1](#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) permitem.

Não use o futuro do presente simples ("enviará") nem "irá" + infinitivo. Não use o futuro do pretérito ("enviaria", "seria"). Não use o pretérito imperfeito ("enviava") nem o pretérito mais-que-perfeito ("enviara", "tinha enviado").

Para o comportamento de uma versão anterior, escreva a versão como sujeito, no presente: "A versão 2.3 envia 2 notificações por pedido." Não use "o sistema" como sujeito para um comportamento que a versão do documento não tem.

**Justificativa:** Com um número pequeno de formas verbais, a leitura e a verificação são mais simples. A versão como sujeito mostra ao leitor que o comportamento é da versão citada, não da versão do documento. A seção 5.1 de [`01-introducao.md`](01-introducao.md) explica a decisão sobre o futuro simples.

**Verificação:** O Vale detecta as terminações do futuro simples e a sequência "irá" + infinitivo. O revisor verifica o futuro do pretérito, o pretérito imperfeito e o comportamento de versões anteriores.

**Não aprovado:** O backup irá começar às 02:00 UTC.

**PTS-BR:** O backup vai começar às 02:00 UTC.

**Não aprovado:** O sistema enviará um alerta à equipe de plantão.

**PTS-BR:** O sistema vai enviar um alerta à equipe de plantão.

**Não aprovado:** Seria interessante atualizar o driver.

**PTS-BR:** Atualize o driver para a versão 5.2.

**Não aprovado:** Na versão 2.3, o sistema enviava duas notificações por pedido.

**PTS-BR:** A versão 2.3 envia 2 notificações por pedido. A versão 2.4 corrige este defeito.

### R3.2 Use o subjuntivo apenas em condições com "se" ou "quando" `[revisor]`

**Enunciado:** Escolha a forma da condição pelo tipo de condição:

- Instrução ou fato futuro: "se" ou "quando" + futuro do subjuntivo ("Se o teste falhar, volte ao passo 2.").
- Comportamento que o sistema tem sempre, em texto descritivo: "quando" + presente do indicativo ("Quando a fila fica cheia, o serviço recusa mensagens novas.").
- Fato passado que o leitor verifica: "se" + pretérito perfeito ("Se o comando retornou o código 1, leia o log.").
- Condição de uma regra, de um requisito ou de um critério: "se" + futuro do subjuntivo ("Se o documento não declarar a versão, o resultado é Reprovado.").

Depois de "até" e de "antes de", use o infinitivo flexionado (regra [R3.1](#r31-use-apenas-os-tempos-verbais-aprovados-vale)). Não use "caso", "desde que", "a menos que", "para que", "até que", "antes que", "embora" nem "talvez". Não use o imperfeito do subjuntivo ("se fosse"). As formas do imperativo ("Instale", "Não remova") são aprovadas. Estas formas são iguais às formas do presente do subjuntivo.

**Justificativa:** As 3 formas de condição são corretas na norma do português. Uma forma fixa para cada tipo de condição mostra o tipo ao leitor: uma instrução, um comportamento do sistema, um fato passado ou uma regra. As outras formas do subjuntivo indicam hipótese, concessão ou desejo, e um texto técnico não precisa destes significados.

**Verificação:** O revisor procura "caso", "desde que", "a menos que", "para que", "até que", "antes que", "embora", "talvez" e as terminações do imperfeito do subjuntivo ("-sse", "-ssem"). O revisor confirma a forma de cada condição.

**Não aprovado:** Caso o token expire, solicite um token novo.

**PTS-BR:** Se o token expirar, gere um token novo.

**Não aprovado:** Para que o cache seja limpo, reinicie o serviço.

**PTS-BR:** Reinicie o serviço para limpar o cache.

**Não aprovado:** Se o servidor fosse reiniciado, a sessão seria perdida.

**PTS-BR:** Quando o servidor reinicia, o usuário perde a sessão.

Este exemplo descreve um comportamento que o sistema tem sempre. Portanto, a condição usa "quando" + presente do indicativo.

**Não aprovado:** Aguarde até que o pod esteja pronto.

**PTS-BR:** Aguarde até o pod ficar no estado `Running`.

### R3.3 Use a voz ativa `[revisor]`

**Enunciado:** Use a voz ativa. Use a voz passiva com "ser" + particípio apenas em texto descritivo. No texto descritivo, use a voz passiva apenas se o leitor não precisar saber o autor da ação. Não use a voz passiva em procedimentos, avisos e mensagens de erro. A regra [R10.7](#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor) tem uma exceção para mensagens de sucesso.

**Justificativa:** A voz ativa mostra o autor da ação. Em um incidente, o leitor precisa saber se a ação é do sistema, de outro serviço ou do próprio leitor.

**Verificação:** O revisor verifica cada construção "ser" + particípio. O revisor confirma que o texto é descritivo e que o leitor não precisa saber o autor da ação.

**Não aprovado:** O arquivo de log é compactado e os arquivos antigos são removidos.

**PTS-BR:** A ferramenta `logrotate` compacta o arquivo de log 1 vez por dia. A ferramenta `logrotate` exclui os arquivos com mais de 30 dias.

**Aprovado:** Os dados de pagamento são criptografados com AES-256.

### R3.4 Não use a passiva sintética nem o "se" indeterminado `[vale]`

**Enunciado:** Não use verbo + "se" para indicar uma ação sem autor: "Instala-se", "Recomenda-se", "Deve-se", "Verifica-se", "Precisa-se de". Em procedimentos, use o imperativo. Em texto descritivo, escreva o autor da ação como sujeito.

**Justificativa:** A passiva sintética oculta o autor da ação. O leitor não nativo lê este "se" como conjunção de condição ou como pronome reflexivo.

**Verificação:** O Vale detecta verbo + "-se" com hífen. O revisor verifica "se" + verbo sem sujeito no início da frase e confirma os verbos pronominais aprovados.

**Não aprovado:** Recomenda-se reiniciar o serviço depois da atualização.

**PTS-BR:** Reinicie o serviço depois da atualização.

**Não aprovado:** Verifica-se que o certificado expirou.

**PTS-BR:** O certificado expirou.

**Não aprovado:** Precisa-se de permissão de administrador para esta tarefa.

**PTS-BR:** Esta tarefa precisa de permissão de administrador.

### R3.5 Use o verbo, não um verbo-suporte com um substantivo `[vale]`

**Enunciado:** Não use "fazer", "realizar", "efetuar", "proceder a", "promover" ou "dar" com um substantivo que tem o radical de um verbo aprovado. Estes substantivos têm o radical de um verbo aprovado e as terminações "-ção", "-mento" e "-agem". Use o verbo aprovado. Exceção: se o substantivo for um termo técnico sem verbo aprovado ("o deploy", "o backup"), use o verbo que [`04-termos-tecnicos.md`](04-termos-tecnicos.md) indica para este termo ("Execute o deploy.", "Faça um backup.").

**Justificativa:** A nominalização aumenta a frase e oculta a ação em um substantivo. A frase com o verbo é mais curta e cumpre a regra do imperativo ([R5.2](#r52-use-o-imperativo-nos-passos-revisor)).

**Verificação:** O Vale detecta as formas destes verbos seguidas de artigo e de um substantivo com as terminações "-ção", "-mento" ou "-agem". O revisor confirma os termos técnicos sem verbo aprovado.

**Não aprovado:** Realize a instalação do agente.

**PTS-BR:** Instale o agente.

**Não aprovado:** Efetue a configuração da chave SSH.

**PTS-BR:** Configure a chave SSH.

**Não aprovado:** Proceda à reinicialização do servidor.

**PTS-BR:** Reinicie o servidor.

### R3.6 Use o gerúndio apenas para uma ação em andamento `[vale]`

**Enunciado:** Use o gerúndio apenas em "estar" + gerúndio, para uma ação em andamento ("O serviço está processando a fila."), e nas mensagens de andamento (regra [R10.7](#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor)). Não use gerundismo ("vai estar enviando", "vamos estar analisando"). Não use orações de gerúndio ("Clicando em...", "..., gerando um relatório").

**Justificativa:** Uma oração de gerúndio não mostra o sujeito nem a ordem das ações. O gerundismo adiciona 2 verbos e nenhum significado.

**Verificação:** O Vale detecta o gerundismo: "estar" + gerúndio depois de "vai", "vão" ou "vamos". O revisor verifica as orações de gerúndio.

**Não aprovado:** Vamos estar enviando o relatório amanhã.

**PTS-BR:** O sistema vai enviar o relatório em 2026-11-19.

**Não aprovado:** Clicando em **Salvar**, o sistema grava as alterações.

**PTS-BR:** Clique em **Salvar**. O sistema grava as alterações.

**Não aprovado:** O script lê o arquivo, validando cada linha e gerando um relatório.

**PTS-BR:** O script lê o arquivo e valida cada linha. Depois, o script gera um relatório.

### R3.7 Não use pronomes oblíquos átonos nem mesóclise `[vale]`

**Enunciado:** Não use os pronomes oblíquos átonos "o", "a", "os", "as", "lhe", "lhes", nem as formas "-lo", "-la", "-los", "-las", "-no", "-na". Repita o substantivo. Não use mesóclise. Exceção: em um verbo pronominal aprovado ("conectar-se"), escreva o sujeito e depois "se" antes do verbo ("O serviço se conecta ao banco."). Não comece uma frase com um pronome átono.

**Justificativa:** A colocação dos pronomes átonos é diferente na norma gramatical e no uso do Brasil. O substantivo repetido mostra ao leitor não nativo o referente do pronome.

**Verificação:** O Vale detecta a ênclise com hífen e a mesóclise. A regra [R1.1](#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) detecta "lhe". O revisor verifica as frases que começam com pronome átono.

**Não aprovado:** Copie o token e cole-o no campo **Token**.

**PTS-BR:** Copie o token. Cole o token no campo **Token**.

**Não aprovado:** O sistema enviar-lhe-á um código.

**PTS-BR:** O sistema vai enviar um código para você.

**Não aprovado:** Conecta-se ao banco na porta 5432.

**PTS-BR:** O serviço se conecta ao banco na porta 5432.

### R3.8 Use "poder" e "dever" com um único significado `[revisor]`

**Enunciado:** Use "poder" apenas para capacidade ou permissão ("O campo pode ter até 64 caracteres."). Use "dever" apenas para uma obrigação em um requisito ("A senha deve ter 12 caracteres ou mais."). Não use "dever" para probabilidade ou recomendação. Não use "poder" para uma possibilidade ("pode ser que", "pode ocorrer", "você pode querer"). Para um risco, escreva a condição e o efeito: "Quando a fila tem mais de 10 000 mensagens, o serviço recusa mensagens novas."

**Justificativa:** A frase "O job deve terminar em 10 min" tem 2 leituras: uma previsão ou uma obrigação. O leitor não sabe qual significado o autor escolheu.

**Verificação:** O revisor verifica o significado de cada ocorrência de "poder" e "dever".

**Não aprovado:** O job deve terminar em 10 min.

**PTS-BR:** O job termina entre 8 e 10 min depois do início.

**Não aprovado:** Você pode querer limpar o cache.

**PTS-BR:** Se a página mostrar dados antigos, limpe o cache.

**Não aprovado:** Pode ocorrer perda de dados.

**PTS-BR:** O comando exclui todas as linhas da tabela `sessoes`.

### R3.9 Use apenas "ser", "estar" e "ficar" como verbos de ligação `[revisor]`

**Enunciado:** Use "ser" para uma característica fixa, "estar" para um estado em um momento e "ficar" para um estado novo depois de um evento ("O indicador fica verde depois do deploy."). Use "ficar" apenas com este significado. Para um lugar, use "estar" ("O arquivo está na pasta `/etc/app`."). Não use "tornar-se", "permanecer", "continuar", "parecer", "virar", "encontrar-se" e "mostrar-se" como verbos de ligação.

**Justificativa:** Um verbo de ligação para cada tipo de estado mostra ao leitor se o estado é fixo, atual ou novo. "Permanecer" e "continuar" como verbos de ligação têm o significado de "estar". "Parecer" indica uma incerteza, e um texto técnico descreve fatos.

**Verificação:** O revisor procura estes verbos seguidos de adjetivo, de particípio ou de "em" + lugar. O revisor confirma que cada "ficar" indica um estado novo.

**Não aprovado:** O serviço se tornou indisponível depois do deploy.

**PTS-BR:** O serviço ficou indisponível depois do deploy.

**Não aprovado:** O arquivo se encontra na pasta `/etc/app`.

**PTS-BR:** O arquivo está na pasta `/etc/app`.

**Não aprovado:** O pod permanece pendente.

**PTS-BR:** O pod está no estado `Pending` desde 09:30 UTC.

**Não aprovado:** O serviço parece indisponível.

**PTS-BR:** O serviço não responde no endpoint `/health`.

**Aprovado:** O indicador fica verde depois do deploy.

### R3.10 Use o verbo específico, não um verbo geral `[revisor]`

**Enunciado:** Não use "fazer", "dar", "colocar", "botar", "pôr", "pegar", "mexer" e "mandar" se o dicionário tiver um verbo mais específico para a ação. Use "ter" apenas com o significado que [`03-dicionario.md`](03-dicionario.md) define ("A tabela tem 3 colunas."). Não use "ter que" nem "ter de".

**Justificativa:** Com um verbo geral, o leitor não sabe a ação exata. O verbo específico mostra a ação exata e também a ferramenta.

**Verificação:** O revisor procura os verbos gerais da lista e as sequências "ter que" e "ter de".

**Não aprovado:** Coloque a senha no campo **Senha**.

**PTS-BR:** Digite a senha no campo **Senha**.

**Não aprovado:** Dê um restart no pod.

**PTS-BR:** Reinicie o pod.

**Não aprovado:** Você tem que mexer no arquivo `.env`.

**PTS-BR:** Altere o valor de `API_URL` no arquivo `.env`.

---

## Seção 4: Frases

### R4.1 Escreva uma instrução ou uma afirmação por frase `[revisor]`

**Enunciado:** Cada frase contém uma instrução ou uma afirmação principal. Se uma frase tiver 2 ações independentes, escreva 2 frases. Uma frase pode ter mais de um objeto para a mesma ação ("Copie o ID e a chave."). A regra [R5.3](#r53-escreva-uma-instrução-por-passo-revisor) tem uma exceção para 2 ações ao mesmo tempo.

**Justificativa:** Com uma ideia por frase, a leitura e a tradução automática são mais simples. O leitor confirma cada informação antes de continuar.

**Verificação:** O revisor procura frases com 2 verbos principais ligados por "e", "mas", "que" ou vírgula.

**Não aprovado:** Atualize o pacote e reinicie o serviço, que vai recarregar a configuração.

**PTS-BR:** Atualize o pacote. Reinicie o serviço. O serviço vai ler a configuração de novo.

### R4.2 Escreva frases dentro do limite de palavras `[vale]`

**Enunciado:** Uma frase de procedimento tem no máximo 20 palavras. Uma frase de texto descritivo tem no máximo 25 palavras. Conte como 1 palavra: cada literal de código, cada rótulo de interface, cada espaço reservado e cada número com a unidade ("10 GB"). As contrações ("do", "na") e as palavras com hífen contam como 1 palavra.

**Justificativa:** Frases longas aumentam os erros de leitura. Os leitores não nativos têm o maior número de erros. Os limites são valores máximos, não metas.

**Verificação:** O Vale conta as palavras de cada frase e mostra um alerta para cada frase maior que o limite. Em 2 situações, o Vale conta as palavras com outro critério: o número com a unidade e o rótulo com 2 ou mais palavras. O revisor conta de novo as palavras das frases com alerta.

**Não aprovado:**

> 1. Antes de iniciar a atualização do cluster, verifique se todos os nós estão com o status Ready e se não há pods em estado Pending no namespace.

**PTS-BR:**

> 1. Verifique se todos os nós estão no estado `Ready`.
> 2. Verifique se o namespace `pagamentos` não tem pods no estado `Pending`.

### R4.3 Escreva o sujeito antes do verbo e faça a concordância `[vale]`

**Enunciado:** Use a ordem direta: sujeito, verbo, complementos. O verbo está em concordância com o sujeito em número e pessoa. Não use "haver". Para indicar que um item existe, use "ter" com o lugar como sujeito ("O log tem 3 erros.") ou use "existir" ("Existem 3 erros no log."). Com "existir", o sujeito pode estar depois do verbo, e o verbo está em concordância com o sujeito.

**Justificativa:** Com o sujeito depois do verbo, os redatores escrevem a concordância incorreta ("Segue os arquivos"). "Haver" impessoal não tem plural, e os redatores escrevem "houveram". A ordem direta também é mais simples para o leitor não nativo.

**Verificação:** O Vale detecta "há", "houve" e "houveram". O revisor verifica as outras inversões e a concordância, por exemplo "segue", "existe" e "falta" antes de um substantivo no plural.

**Não aprovado:** Segue em anexo os logs do incidente.

**PTS-BR:** Os logs do incidente estão em anexo.

**Não aprovado:** Foi identificado 3 falhas no teste de carga.

**PTS-BR:** O teste de carga mostrou 3 falhas.

**Não aprovado:** Houveram 2 tentativas de acesso negado.

**PTS-BR:** O log mostra 2 tentativas de acesso negado.

**Não aprovado:** Há 3 erros no log.

**PTS-BR:** O log tem 3 erros.

### R4.4 Escreva o sujeito se o texto tiver mais de um autor de ação `[revisor]`

**Enunciado:** Escreva o sujeito de cada frase se o texto anterior tiver 2 ou mais autores de ação possíveis. Um autor de ação é uma pessoa, um sistema, um serviço ou um componente.

**Justificativa:** O português permite uma frase sem sujeito, porque o verbo indica a pessoa. Com 2 sistemas no texto, a forma do verbo não mostra qual sistema faz a ação.

**Verificação:** O revisor verifica cada frase sem sujeito depois de uma frase com 2 ou mais autores de ação.

**Não aprovado:** O agente envia as métricas ao servidor de métricas a cada 60 s. Depois, descarta as métricas antigas.

**PTS-BR:** O agente envia as métricas ao servidor de métricas a cada 60 s. Depois, o servidor de métricas descarta as métricas com mais de 30 dias.

### R4.5 Use no máximo uma negação por frase `[revisor]`

**Enunciado:** Uma frase tem no máximo uma negação. Não use dupla negação com significado afirmativo: "não é impossível", "não deixe de", "não é incomum". A concordância negativa do português ("não ... nenhum", "não ... nunca", "não ... nada") conta como uma negação. Escreva "não" imediatamente antes do verbo.

**Justificativa:** Com 2 negações, o leitor precisa calcular o significado da frase. A concordância negativa é a forma normal do português e não causa esta dúvida.

**Verificação:** O revisor procura "não" + adjetivo com prefixo negativo ("impossível", "incomum", "inválido", "indisponível", "incorreto") e as expressões "não deixe de" e "não é incomum".

**Não aprovado:** Não deixe de validar o certificado.

**PTS-BR:** Valide o certificado.

**Não aprovado:** Não é impossível restaurar o backup.

**PTS-BR:** Você pode restaurar o backup.

**Aprovado:** O comando não altera nenhum arquivo.

### R4.6 Use no máximo uma oração subordinada por frase `[revisor]`

**Enunciado:** Uma frase tem no máximo uma oração subordinada. Nas orações relativas, use "que", "em que" ou "de que". Não use "o qual", "a qual", "os quais", "as quais" nem "cujo".

**Justificativa:** Com 2 ou mais orações subordinadas, a frase tem outras palavras entre o sujeito e o verbo. "O qual" e "cujo" estão em concordância com um substantivo de outra parte da frase e não são comuns na fala.

**Verificação:** O revisor procura "o qual", "a qual", "os quais", "as quais", "cujo" e as formas flexionadas de "cujo". O revisor conta as orações subordinadas de cada frase.

**Não aprovado:** O job, cujo agendamento é definido no arquivo `cron.yaml`, o qual o serviço lê na inicialização, limpa a tabela de sessões.

**PTS-BR:** O arquivo `cron.yaml` define a hora de início do job. O serviço lê o arquivo `cron.yaml` quando inicia. O job limpa a tabela `sessoes`.

---

## Seção 5: Procedimentos

Um procedimento é uma sequência numerada de passos que o leitor segue para obter um resultado. Use as regras [R5.1](#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) a [R5.9](#r59-termine-com-um-passo-de-verificação-revisor) em todos os procedimentos. Use também as regras [R5.10](#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) a [R5.12](#r512-escreva-o-registro-que-a-etapa-gera-revisor) nos procedimentos de processo, por exemplo um procedimento operacional padrão (POP). Um procedimento de processo tem 2 ou mais responsáveis, tem pontos de decisão ou gera registros. Use a regra [R5.13](#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) em todos os procedimentos que alteram o ambiente de produção.

### R5.1 Escreva os passos em uma lista numerada, na ordem de execução `[revisor]`

**Enunciado:** Escreva cada passo como um item de uma lista numerada, na ordem de execução. Escreva o título do procedimento no infinitivo, sem ponto final ("Instalar o agente"). Não escreva um procedimento em forma de parágrafo.

**Justificativa:** A numeração mostra a ordem e permite citar um passo ("Volte ao passo 3."). O título no infinitivo é o nome da tarefa e não é uma ordem.

**Verificação:** O revisor verifica que o título começa com um verbo no infinitivo e que os passos estão em uma lista numerada.

**Não aprovado:**

> Como instalar o agente: primeiro baixe o pacote, depois instale com o dpkg e por fim inicie o serviço.

**PTS-BR:**

> **Instalar o agente**
>
> 1. Baixe o pacote `agente_3.2_amd64.deb`.
> 2. Instale o pacote:
>    ```shell
>    sudo dpkg --install agente_3.2_amd64.deb
>    ```
> 3. Inicie o serviço:
>    ```shell
>    sudo systemctl start agente
>    ```

### R5.2 Use o imperativo nos passos `[revisor]`

**Enunciado:** Comece cada passo com um verbo no imperativo da forma "você" ("Remova", "Instale", "Clique"). Um passo também pode começar com uma condição ou um local antes do imperativo (regra [R5.4](#r54-escreva-a-condição-e-o-local-antes-da-ação-revisor)). Para proibir uma ação, use "Não" + imperativo ("Não desligue o servidor."). Não use o infinitivo como ordem. Não use expressões indiretas: "é necessário", "é preciso", "você deve", "você precisa", "o usuário deve", "deve-se", "favor".

**Justificativa:** O imperativo mostra que a frase é uma ordem para o leitor. O infinitivo e as expressões indiretas não mostram o autor da ação.

**Verificação:** O revisor verifica que o primeiro verbo de cada passo está no imperativo e procura as expressões indiretas da lista.

**Não aprovado:** Remover a versão antiga do pacote.

**PTS-BR:** Remova a versão antiga do pacote.

**Não aprovado:** É necessário reiniciar o serviço.

**PTS-BR:** Reinicie o serviço.

**Não aprovado:** O usuário deve clicar em **Enviar**.

**PTS-BR:** Clique em **Enviar**.

### R5.3 Escreva uma instrução por passo `[revisor]`

**Enunciado:** Cada passo tem um único verbo no imperativo. Exceção: 2 ações que o leitor faz ao mesmo tempo estão no mesmo passo ("Mantenha a tecla **Shift** pressionada e clique em **Reiniciar**.").

**Justificativa:** Com uma instrução por passo, o leitor sabe os passos que terminou e continua no passo correto depois de uma pausa. A exceção existe porque 2 passos separados para 2 ações ao mesmo tempo alteram o resultado.

**Verificação:** O revisor conta os verbos no imperativo de cada passo e confirma as exceções.

**Não aprovado:**

> 1. Abra o terminal, entre na pasta do projeto e execute os testes.

**PTS-BR:**

> 1. Abra o terminal.
> 2. Vá para a pasta do projeto:
>    ```shell
>    cd loja-web
>    ```
> 3. Execute os testes:
>    ```shell
>    npm test
>    ```

**Aprovado:**

> 1. Mantenha a tecla **Shift** pressionada e clique em **Reiniciar**.

### R5.4 Escreva a condição e o local antes da ação `[revisor]`

**Enunciado:** Se uma ação depender de uma condição, escreva a condição antes do imperativo: "Se X, faça Y." Se a ação acontecer em uma tela, um menu ou uma ferramenta específica, escreva o local antes do imperativo: "Na página **Perfil**, clique em **Salvar**." Escreva uma condição explícita, com um valor que o leitor pode verificar. Não use "se necessário", "se for o caso", "quando aplicável" nem "conforme a necessidade".

**Justificativa:** O leitor começa a ação quando lê o verbo. Uma condição depois do verbo chega depois do início da ação. "Se necessário" transfere a decisão para o leitor sem o critério da decisão.

**Verificação:** O revisor procura "se" depois do imperativo na mesma frase e as expressões vagas da lista.

**Não aprovado:** Clique em **Excluir** se o estado do usuário for **Inativo**.

**PTS-BR:** Se o estado do usuário for **Inativo**, clique em **Excluir**.

**Não aprovado:** Se necessário, aumente o limite de memória.

**PTS-BR:** Se o pod reiniciar com o erro `OOMKilled`, aumente o limite de memória para 512 MiB.

**Não aprovado:** Clique em **Salvar** na página **Perfil**.

**PTS-BR:** Na página **Perfil**, clique em **Salvar**.

### R5.5 Escreva o resultado esperado em uma frase separada `[revisor]`

**Enunciado:** Se um passo gerar um resultado visível, escreva o resultado em uma frase separada, depois da instrução. Escreva o resultado no mesmo item da lista, sem número próprio. Use o presente do indicativo. Não escreva a instrução e o resultado na mesma frase.

**Justificativa:** O leitor separa a ação que precisa fazer do resultado que precisa ver. O resultado esperado também permite ao leitor confirmar que o passo funcionou.

**Verificação:** O revisor verifica que a primeira frase de cada passo é uma instrução e que o resultado está em uma frase própria.

**Não aprovado:**

> 3. Clique em **Publicar** e a página vai mostrar a mensagem "Versão publicada.".

**PTS-BR:**

> 3. Clique em **Publicar**.
>
>    A página mostra a mensagem "Versão publicada."

### R5.6 Escreva os pré-requisitos antes do passo 1 `[revisor]`

**Enunciado:** Escreva as condições que o leitor precisa cumprir antes do procedimento em uma seção "Antes de começar", antes do passo 1. As condições são permissões, papéis de acesso, ferramentas, versões e backups. Não escreva pré-requisitos entre os passos.

**Justificativa:** O leitor que encontra um pré-requisito no passo 4 precisa desfazer os passos 1 a 3. A seção "Antes de começar" permite verificar todas as condições antes do passo 1.

**Verificação:** O revisor verifica que nenhum passo contém uma permissão, uma ferramenta ou uma versão que o leitor precisa ter antes do passo 1.

**Não aprovado:**

> 4. Para este passo, você precisa da permissão de administrador do cluster.

**PTS-BR:**

> **Antes de começar**
>
> - Confirme que a sua conta tem o papel de acesso `cluster-admin`.
> - Instale a ferramenta `kubectl` na versão 1.30 ou em uma versão mais nova.

### R5.7 Limite o número de passos e de níveis do procedimento `[revisor]`

**Enunciado:** Um procedimento tem no máximo 10 passos. Se uma tarefa precisar de mais passos, divida a tarefa em procedimentos menores, cada um com um título. Use no máximo um nível de sublista. Use a sublista apenas para alternativas, com uma condição em cada item.

**Justificativa:** Em um procedimento longo, o leitor perde a posição. Com mais de um nível de sublista, o leitor não sabe qual é o próximo passo.

**Verificação:** O revisor conta os passos de cada procedimento e os níveis de cada lista.

**Não aprovado:**

> 5. Configure o banco.
>    1. Se o banco for PostgreSQL:
>       1. Se a versão for 15 ou mais nova, altere o arquivo `pg_hba.conf`.
>       2. Se a versão for 14 ou mais antiga, ...

**PTS-BR:**

> 5. Configure a conexão com o banco:
>    - Se o banco for PostgreSQL, siga o procedimento "Configurar o PostgreSQL".
>    - Se o banco for MySQL, siga o procedimento "Configurar o MySQL".

### R5.8 Escreva os comandos para digitar em blocos de código `[revisor]`

**Enunciado:** Escreva cada comando que o leitor copia em um bloco de código, com um comando por bloco. Use o identificador `shell` no bloco. Não escreva o prompt do terminal ("$", "#", ">"). Não junte 2 comandos com "&&" ou ";" no mesmo bloco. Um pipeline com "|" é 1 comando. Se a ferramenta tiver uma opção longa, use a opção longa: `--namespace`, não `-n`. Se um comando tiver mais de 100 caracteres, escreva uma opção por linha, com `\` no fim de cada linha. Escreva a saída esperada em um bloco separado, depois da frase de resultado. Use código em linha apenas para citar o nome de um comando que o leitor não copia.

**Justificativa:** O bloco de código permite copiar o comando sem erro. O prompt e os comandos com "&&" ou ";" causam erros quando o leitor copia o bloco. A opção longa mostra ao leitor a função da opção sem o manual da ferramenta.

**Verificação:** O revisor procura prompts no início das linhas de blocos de código e os operadores "&&" e ";" entre comandos. O revisor também procura opções curtas que têm uma opção longa e comandos completos em código em linha dentro de passos.

**Não aprovado:** Execute `$ npm install && npm run build` no terminal.

**PTS-BR:**

> 1. Instale as dependências:
>    ```shell
>    npm install
>    ```
> 2. Gere o build:
>    ```shell
>    npm run build
>    ```

### R5.9 Termine com um passo de verificação `[revisor]`

**Enunciado:** Se o procedimento alterar um sistema, um dado ou o estado de um chamado, o último passo verifica o resultado. Exemplos de alteração: um deploy, uma migração, uma configuração, uma permissão, uma aprovação. O passo de verificação diz a ação do leitor e o resultado correto.

**Justificativa:** Sem verificação, o leitor não identifica uma falha que o sistema não mostra. No último passo, o resultado esperado é um teste.

**Verificação:** O revisor confirma que o último passo de cada procedimento com alteração contém uma ação de verificação e um resultado esperado.

**Não aprovado:**

> 4. Aplique o manifesto:
>    ```shell
>    kubectl apply --filename deployment.yaml --context homologacao-sa-east-1 --namespace pagamentos
>    ```
>
> (Fim do procedimento.)

**PTS-BR:**

> 3. Verifique o cluster do contexto `homologacao-sa-east-1`:
>    ```shell
>    kubectl cluster-info --context homologacao-sa-east-1
>    ```
>    A primeira linha da saída mostra o endereço `https://k8s.homologacao.loja.interno:6443`. Se o endereço for outro, não faça o próximo passo. Este procedimento termina neste passo.
> 4. Aplique o manifesto:
>    ```shell
>    kubectl apply --filename deployment.yaml --context homologacao-sa-east-1 --namespace pagamentos
>    ```
> 5. Verifique o estado dos pods:
>    ```shell
>    kubectl get pods --context homologacao-sa-east-1 --namespace pagamentos
>    ```
>    Todos os pods mostram o estado `Running`.

O passo 3 deste exemplo segue a regra [R7.8](#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor): o passo mostra o alvo do comando antes da alteração.

### R5.10 Escreva o responsável do procedimento e de cada etapa `[revisor]`

**Enunciado:** Em um procedimento de processo, escreva este bloco antes da seção "Antes de começar":

- **Responsável:** o responsável que segue o procedimento, com o nome do glossário do projeto.
- **Entrada:** o item que o responsável recebe e o responsável de origem.
- **Gatilho e prazo:** o evento que inicia o procedimento e o prazo, com o número e a unidade. Se o próprio responsável iniciar o procedimento e o processo não tiver um prazo para este procedimento, escreva "Prazo: nenhum."

Um procedimento tem um único responsável. Se uma tarefa tiver 2 ou mais responsáveis, escreva um procedimento para cada responsável. O último passo de cada procedimento diz qual procedimento recebe a saída. Use "responsável" para a pessoa ou a equipe que faz a etapa. Use "cargo" para a posição na empresa. Use "papel de acesso" para as permissões de uma identidade.

**Justificativa:** Em um processo com 2 ou mais responsáveis, o leitor precisa saber o responsável de cada passo e a origem de cada entrada. Um auditor também verifica o responsável de cada etapa.

**Verificação:** O revisor verifica o bloco antes de "Antes de começar" e confirma que cada procedimento tem um único responsável.

**Não aprovado:**

> **Aprovar o acesso ao banco de produção**
>
> 1. O gestor aprova o pedido.
> 2. A equipe de segurança cria o acesso.

**PTS-BR:**

> **Analisar um chamado de acesso ao banco de produção**
>
> - **Responsável:** gestor do solicitante
> - **Entrada:** o chamado com o modelo "Pedido de acesso", que o solicitante cria no portal de chamados
> - **Gatilho e prazo:** um chamado novo com este modelo. Prazo: 2 dias úteis. O prazo começa quando o solicitante cria o chamado.
>
> **Antes de começar**
>
> - Confirme que a sua conta tem o papel de acesso `aprovador` no portal de chamados.
>
> 1. Leia o chamado no portal de chamados.

Os exemplos das regras [R5.11](#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) e [R5.12](#r512-escreva-o-registro-que-a-etapa-gera-revisor) mostram os passos 2 a 4 deste procedimento. A equipe de segurança tem outro procedimento: "Criar o acesso ao banco de produção".

### R5.11 Escreva cada ponto de decisão com todas as saídas `[revisor]`

**Enunciado:** Escreva um ponto de decisão como um passo com uma sublista. Cada item da sublista tem uma condição e uma ação. Escreva um item para cada resultado possível, também para "recusado" e para "sem resposta no prazo". Cada saída termina em um destino explícito:

- Um passo: Vá para o passo 5.
- Outro procedimento: Siga o procedimento "Criar o acesso ao banco de produção".
- O fim deste procedimento, com o processo ainda em andamento: Este procedimento termina neste passo. Escreva também a pessoa ou o procedimento que continua o processo: Informe o gerente de incidente com a saída do comando.
- O fim do processo: O processo termina neste passo.

Use "O processo termina neste passo." apenas quando nenhuma pessoa precisa fazer outra ação no processo. Se uma saída voltar a um passo anterior, escreva "Volte ao passo 3.", o número máximo de vezes e a saída depois deste número.

**Justificativa:** Em uma decisão sem todas as saídas, o leitor não tem instrução para um dos resultados. Sem um número máximo de vezes, o leitor repete o passo sem fim.

**Verificação:** O revisor verifica que cada ponto de decisão tem um item para cada resultado e que cada item termina em um destino.

**Não aprovado:**

> 2. Analise o chamado e aprove o chamado se estiver tudo certo.

**PTS-BR:**

> 2. Compare o chamado com a política de acesso:
>    - Se o chamado cumprir a política, vá para o passo 3.
>    - Se o chamado não cumprir a política, recuse o chamado com a causa no campo **Comentário**. Registro: a recusa e a causa, no histórico do chamado. O processo termina neste passo.
>    - Se o chamado não tiver o nome do banco, peça o nome do banco ao solicitante no chamado. Quando o solicitante responder, repita este passo. Depois de 2 vezes, ou sem resposta em 2 dias úteis, recuse o chamado. Registro: a recusa, no histórico do chamado. O processo termina neste passo.

### R5.12 Escreva o registro que a etapa gera `[revisor]`

**Enunciado:** Se um passo gerar um registro, escreva o registro em uma frase própria que começa com "Registro:". Um registro documenta uma ação, um resultado ou um evento ([`01-introducao.md`](01-introducao.md), [seção 9](01-introducao.md#9-definições)). A frase diz o nome do registro e o lugar que armazena o registro. O nome do registro é um artefato do glossário do projeto ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo)), por exemplo um chamado, uma aprovação ou um relatório. Escreva a frase de registro depois da frase de resultado (regra [R5.5](#r55-escreva-o-resultado-esperado-em-uma-frase-separada-revisor)).

**Justificativa:** Uma auditoria verifica os registros de cada etapa. Com a frase de registro no procedimento, o auditor sabe qual registro procurar, e o responsável sabe qual registro gerar.

**Verificação:** O revisor verifica que cada passo que gera uma aprovação, uma recusa ou um documento tem a frase "Registro:".

**Não aprovado:**

> 3. Aprove o chamado.

**PTS-BR:**

> 3. Clique em **Aprovar**.
>
>    O portal envia o chamado à equipe de segurança.
>
>    Registro: a aprovação do gestor, no histórico do chamado.
> 4. Verifique o estado do chamado no portal de chamados.
>
>    O estado do chamado é **Aprovado**. A equipe de segurança recebe o chamado no procedimento "Criar o acesso ao banco de produção".

O procedimento altera o estado do chamado. Portanto, o passo 4 verifica o estado (regra [R5.9](#r59-termine-com-um-passo-de-verificação-revisor)). O passo 4 também diz qual procedimento recebe a saída (regra [R5.10](#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor)).

### R5.13 Escreva um procedimento para reverter cada alteração do ambiente de produção `[revisor]`

**Enunciado:** Se um procedimento alterar o ambiente de produção, escreva também um procedimento que reverte a alteração. O procedimento de rollback tem o mesmo nível de detalhe: título, "Antes de começar", passos, avisos e passo de verificação (regra [R5.9](#r59-termine-com-um-passo-de-verificação-revisor)). Cada saída de falha do procedimento principal diz em qual condição o leitor segue o procedimento de rollback. Se a alteração for irreversível, escreva esta informação antes do passo 1. Escreva também o plano da equipe para voltar ao estado anterior, por exemplo restaurar um backup feito antes do passo 1. Escreva também um aviso para esta alteração (regra [R7.1](#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor)).

**Justificativa:** Durante um incidente, o leitor precisa voltar ao estado anterior em poucos minutos. Sem um procedimento escrito, o leitor cria os passos do rollback durante o incidente, sem revisão e sem teste.

**Verificação:** O revisor procura cada procedimento que altera o ambiente de produção. O revisor confirma que o documento tem um procedimento de rollback para cada um destes procedimentos. Para uma alteração irreversível, o revisor confirma a frase sobre a alteração e o plano da equipe.

**Não aprovado:**

> 4. Execute o deploy da versão 2.4.0 no contexto `prod-sa-east-1`.
> 5. Verifique os pods. Se algum pod falhar, faça o rollback.

**PTS-BR:**

> 5. Verifique o estado do deploy:
>    ```shell
>    kubectl rollout status deployment/api-pedidos --context prod-sa-east-1 --namespace pedidos --timeout 5m
>    ```
>    - Se a saída mostrar a mensagem `successfully rolled out`, vá para o passo 6.
>    - Se a saída mostrar outra mensagem, siga o procedimento "Reverter o deploy do serviço `api-pedidos`".
>
> **Reverter o deploy do serviço `api-pedidos`**
>
> **Antes de começar**
>
> - Confirme que a sua conta tem o papel de acesso `deployer` no namespace `pedidos`.
>
> 1. Verifique o cluster do contexto `prod-sa-east-1`:
>    ```shell
>    kubectl cluster-info --context prod-sa-east-1
>    ```
>    A primeira linha da saída mostra o endereço `https://k8s.prod.loja.interno:6443`. Se o endereço for outro, informe o gerente de incidente. Este procedimento termina neste passo.
>
> **ATENÇÃO:** Informe o gerente de incidente antes do passo 2. O comando `helm rollback` substitui os pods do serviço `api-pedidos`. Por até 5 min, a API recusa até 10% das requisições.
>
> 2. Reverta o serviço para a revisão anterior:
>    ```shell
>    helm rollback api-pedidos --kube-context prod-sa-east-1 --namespace pedidos --wait --timeout 5m
>    ```
>    Sem o número de uma revisão, o comando reverte o serviço para a revisão anterior.
> 3. Verifique a versão da imagem do serviço:
>    ```shell
>    kubectl get deployment api-pedidos \
>      --context prod-sa-east-1 \
>      --namespace pedidos \
>      --output jsonpath='{.spec.template.spec.containers[0].image}'
>    ```
>    A saída termina em `:2.3.0`, a versão antes do deploy. Se a saída mostrar outra versão, informe o gerente de incidente com a saída do comando. Este procedimento termina neste passo.

**Aprovado:**

> A migração `0042` exclui a coluna `endereco_antigo` da tabela `clientes`. Esta alteração é irreversível. Plano para voltar ao estado anterior: a equipe restaura o backup do passo 1 com o procedimento "Restaurar o banco `pedidos`".

---

## Seção 6: Texto descritivo

Um texto descritivo explica como um sistema funciona, o que um componente faz ou por que uma decisão existe. Um texto descritivo não contém instruções.

### R6.1 Comece o parágrafo com a frase principal `[revisor]`

**Enunciado:** A primeira frase de cada parágrafo diz o assunto principal do parágrafo. As outras frases dão detalhes, causas ou exemplos sobre este assunto.

**Justificativa:** Um leitor que lê apenas a primeira frase de cada parágrafo entende a estrutura do texto. Este tipo de leitura é comum durante um incidente.

**Verificação:** O revisor confirma que a primeira frase de cada parágrafo diz o assunto das outras frases.

**Não aprovado:** Depois de 3 tentativas, a aplicação cliente aguarda 30 s. Se a API retornar o código 429, a aplicação cliente também aguarda. A aplicação cliente repete as requisições com falha.

**PTS-BR:** A aplicação cliente repete as requisições com falha. Depois de 3 tentativas, a aplicação cliente aguarda 30 s. Quando a API retorna o código 429, a aplicação cliente aguarda o tempo do cabeçalho `Retry-After`.

### R6.2 Escreva parágrafos com no máximo 6 frases e um assunto `[revisor]`

**Enunciado:** Um parágrafo tem no máximo 6 frases. Cada parágrafo tem um único assunto. Para um assunto novo, comece outro parágrafo.

**Justificativa:** Parágrafos curtos mostram a estrutura do texto. Com parágrafos curtos, o leitor encontra uma informação em menos tempo.

**Verificação:** O revisor conta as frases de cada parágrafo e verifica o assunto.

**Não aprovado:** A API usa OAuth 2.0. O token expira em 1 h. O limite é 1 000 requisições por minuto. Se o cliente passar do limite, a API retorna o código 429.

**PTS-BR:**

> A API usa OAuth 2.0 para autenticação. O token expira em 1 h.
>
> A API aceita até 1 000 requisições por minuto de cada aplicação cliente. Quando uma aplicação cliente envia mais requisições, a API retorna o código 429.

### R6.3 Use conectores simples `[revisor]`

**Enunciado:** Para ligar ideias, use apenas estes conectores: "e", "ou", "mas", "nem", "porque", "portanto", "se", "quando", "enquanto", "depois", "antes", "para" + infinitivo, "por exemplo". Não use conectores formais: "haja vista", "outrossim", "destarte", "porquanto", "conquanto", "não obstante", "mediante", "visto que", "uma vez que", "tendo em vista".

**Justificativa:** Os conectores formais não são comuns na fala, e os leitores não nativos não conhecem estes conectores. "Uma vez que" tem 2 significados, causa e tempo, e o leitor não sabe qual significado o autor escolheu.

**Verificação:** O revisor procura os conectores não aprovados. A regra [R1.1](#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) detecta os conectores que [`03-dicionario.md`](03-dicionario.md) lista como não aprovados.

**Não aprovado:** Haja vista que o token expira em 1 h, outrossim recomenda-se renovar o mesmo.

**PTS-BR:** O token expira em 1 h. Portanto, a aplicação cliente gera um token novo a cada 50 min.

**Não aprovado:** Uma vez que o deploy termina, o cache é limpo.

**PTS-BR:** Quando o deploy termina, o pipeline limpa o cache.

### R6.4 Escreva valores, não palavras vagas `[revisor]`

**Enunciado:** Escreva números, limites, nomes e unidades no lugar de palavras vagas. Não use "rápido", "lento", "muito", "pouco", "vários", "alguns", "bastante", "frequentemente", "às vezes", "grande" e "pequeno" sem um valor. "Rápido", "lento", "vários", "grande" e "pequeno" são aprovados em [`03-dicionario.md`](03-dicionario.md), mas o valor precisa estar na mesma frase ("um disco pequeno, de 20 GB"). Se o valor existir, escreva o valor. Se você não tiver um valor exato, escreva uma faixa ("entre 5 e 10 min").

**Justificativa:** Uma palavra vaga tem um valor diferente para cada leitor. Um número permite ao leitor comparar o comportamento real com o comportamento esperado.

**Verificação:** O revisor procura as palavras vagas da lista sem um número na mesma frase.

**Não aprovado:** A API responde rapidamente e aceita muitas requisições.

**PTS-BR:** A API responde em menos de 200 ms e aceita até 1 000 requisições por segundo.

**Não aprovado:** O backup demora bastante.

**PTS-BR:** O backup demora entre 40 e 60 min.

**Aprovado:** Use um disco pequeno, de 20 GB, no ambiente de teste.

### R6.5 Use listas e tabelas para itens paralelos `[revisor]`

**Enunciado:** Se o texto tiver 3 ou mais itens do mesmo tipo, use uma lista. Se cada item tiver 2 ou mais informações, use uma tabela. Use uma lista numerada apenas para uma sequência. Escreva todos os itens com a mesma estrutura gramatical. Escreva uma frase de introdução antes da lista ou da tabela.

**Justificativa:** A lista mostra a quantidade de itens e permite comparar os itens. Com a mesma estrutura em todos os itens, o leitor não procura diferenças que não existem.

**Verificação:** O revisor procura frases com 3 ou mais itens separados por vírgula e verifica a estrutura dos itens de cada lista.

**Não aprovado:** A API aceita JSON, XML e CSV, sendo que o JSON é o padrão, o XML está obsoleto e o CSV só funciona para exportação.

**PTS-BR:** A API aceita 3 formatos:

| Formato | Estado | Uso |
|---|---|---|
| JSON | Padrão | Leitura e gravação |
| XML | Obsoleto | Leitura e gravação |
| CSV | Ativo | Apenas para exportar dados |

### R6.6 Não escreva instruções em texto descritivo `[revisor]`

**Enunciado:** Não escreva ordens, recomendações ou obrigações para o leitor em um texto descritivo. Escreva a instrução em um procedimento. Se a instrução evitar um risco, escreva a instrução em um aviso (seção 7). No texto descritivo, escreva apenas o nome do procedimento.

**Justificativa:** O leitor que procura o que fazer lê os procedimentos e não lê toda a descrição. Este leitor não vê uma instrução dentro de uma descrição.

**Verificação:** O revisor procura verbos no imperativo e expressões de recomendação ("é recomendável", "recomendamos", "o ideal é") em parágrafos fora de procedimentos.

**Não aprovado:** O cache armazena as respostas por 10 min, e é recomendável limpar o cache depois de cada deploy.

**PTS-BR:** O cache armazena as respostas por 10 min. O procedimento "Limpar o cache" explica como limpar o cache depois de um deploy.

---

## Seção 7: Avisos de segurança

Um aviso informa o leitor sobre um risco antes da ação que causa o risco. Em software, o risco afeta dados, sistemas, credenciais, custos ou pessoas. O nível do aviso depende da consequência mais grave da ação, não da ação.

### R7.1 Use o nível de aviso da consequência mais grave `[revisor]`

**Enunciado:** Escolha a palavra de sinalização pela consequência mais grave da ação, não pela ação. Responda a estas 3 perguntas, nesta ordem. Use o nível da primeira resposta "sim".

1. A consequência é um dano sem recuperação? Use PERIGO. Um dano sem recuperação é uma destas consequências:
   - Uma perda de dados sem cópia no backup. Um backup tem apenas os dados gravados até o momento do backup. Os dados gravados depois do último backup não têm recuperação. Esta perda é um dano sem recuperação também quando a perda está dentro do RPO, a perda máxima de dados que a empresa aceita.
   - Dados expostos a pessoas sem permissão, por exemplo com um controle de segurança desativado.
   - Uma credencial exposta.
   - Um risco para pessoas.
2. A consequência é uma destas? Use ATENÇÃO.
   - Uma indisponibilidade parcial ou total com recuperação conhecida. Em uma recuperação conhecida, a equipe restaura um backup, executa um rollback ou processa os dados de novo. Quando o sistema volta ao estado anterior automaticamente, a recuperação também é conhecida.
   - Uma exclusão de dados com cópia completa no backup: a equipe restaura todos os dados excluídos.
   - Um custo não planejado maior que o limite da equipe. O glossário do projeto define este limite, por exemplo R$ 1 000 por mês.
3. A consequência é um desempenho menor sem perda de funcionalidade, um retrabalho ou um dano menor? Use CUIDADO. Uma latência maior é um desempenho menor. Um custo não planejado menor que o limite da equipe é um dano menor.

Use NOTA apenas para uma informação sem risco (regra [R7.2](#r72-use-nota-apenas-para-informação-sem-risco-revisor)). Não use outras palavras de sinalização, como "IMPORTANTE", "ALERTA", "AVISO" ou "OBSERVAÇÃO".

Os exemplos desta tabela escrevem a ação e a consequência. A mesma ação com outra consequência tem outro nível.

| Palavra de sinalização | Consequência | Exemplos de TI |
|---|---|---|
| **PERIGO** | Dano sem recuperação. Perda de dados sem cópia no backup, também dentro do RPO. Dados expostos a pessoas sem permissão. Credencial exposta. Risco para pessoas. | Excluir o banco `pedidos` de produção: os pedidos gravados depois do último backup não têm recuperação. Publicar uma chave privada em um repositório: a credencial fica exposta. Desativar a verificação TLS, a MFA ou o log de auditoria: os dados ficam expostos a pessoas sem permissão. Atribuir o papel de acesso de administrador a uma conta de serviço: a conta pode ler e alterar os dados de todos os clientes. Configurar um bucket com acesso público: os arquivos ficam expostos a qualquer pessoa. Permitir o acesso da internet a uma porta com a origem `0.0.0.0/0`: o serviço fica exposto a qualquer pessoa. Excluir uma chave de criptografia: os dados criptografados com esta chave não têm recuperação. |
| **ATENÇÃO** | Indisponibilidade parcial ou total com recuperação conhecida. Exclusão de dados com cópia completa no backup. Custo não planejado maior que o limite da equipe. | Reiniciar um serviço de produção: o serviço fica indisponível por 5 min e volta automaticamente. Excluir os índices do Elasticsearch: os clientes não podem procurar produtos até a equipe indexar os dados de novo. Alterar o endereço IP de um nome DNS: até o fim do TTL de 1 h, os clientes com o cache antigo recebem erros. Excluir a tabela `eventos_2025`, que nenhum processo altera depois do backup: a equipe restaura a tabela com o backup. Aumentar um cluster para 20 nós: o custo da conta aumenta em R$ 15 000 por mês. O limite da equipe é R$ 1 000 por mês. |
| **CUIDADO** | Desempenho menor sem perda de funcionalidade. Retrabalho. Dano menor, por exemplo um custo não planejado menor que o limite da equipe. | Reiniciar os pods de um serviço um de cada vez: por 2 min, a API responde em até 2 s, em vez de 200 ms. Limpar o cache da API: por 15 min, a API responde em até 2 s, em vez de 200 ms. Fechar o editor sem salvar: o leitor escreve as alterações de novo. |
| **NOTA** | Nenhum risco. Uma informação que ajuda o leitor no passo (regra [R7.2](#r72-use-nota-apenas-para-informação-sem-risco-revisor)). | Um comportamento esperado, uma referência a outro documento. |

**Justificativa:** Um nível fixo para cada tipo de consequência permite ao leitor avaliar o risco pela palavra de sinalização. As 3 perguntas dão o mesmo nível à mesma consequência em textos de redatores diferentes. Depois de avisos com o nível incorreto, o leitor não lê os avisos.

**Verificação:** O revisor responde às 3 perguntas do enunciado para cada aviso e compara a resposta com a palavra de sinalização. O revisor também compara os avisos do documento: a mesma consequência tem o mesmo nível.

**Não aprovado:**

> **IMPORTANTE:** Cuidado ao executar a migração em produção.

**PTS-BR:**

> **PERIGO:** Faça um backup do banco `pedidos` antes da migração. A migração exclui a coluna `endereco_antigo`. Sem um backup feito imediatamente antes da migração, a equipe não pode recuperar os endereços antigos.

### R7.2 Use NOTA apenas para informação sem risco `[revisor]`

**Enunciado:** Use NOTA para uma informação que ajuda o leitor e que não tem risco. Uma NOTA não descreve um dano, uma perda ou uma falha. Se a informação tiver um risco, use PERIGO, ATENÇÃO ou CUIDADO. O texto de uma NOTA segue as regras da seção 6.

**Justificativa:** Uma NOTA com um risco oculta o risco em um formato que o leitor associa a uma informação opcional.

**Verificação:** O revisor verifica que nenhuma NOTA descreve uma perda, uma falha ou uma indisponibilidade.

**Não aprovado:**

> **NOTA:** Este comando exclui todas as linhas da tabela `sessoes`.

**PTS-BR:**

> **CUIDADO:** Execute este comando entre 22:00 e 06:00 UTC-03:00. O comando exclui todas as linhas da tabela `sessoes`. Todos os usuários conectados vão precisar entrar no sistema de novo.

O nível é CUIDADO: a consequência é um retrabalho para os usuários, e o sistema continua disponível (regra [R7.1](#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor)).

**Aprovado:**

> **NOTA:** O comando `kubectl rollout status` mostra o estado do deploy em tempo real.

### R7.3 Escreva o aviso na ordem instrução, risco, consequência `[revisor]`

**Enunciado:** Um aviso de PERIGO, ATENÇÃO ou CUIDADO tem 3 partes, nesta ordem, cada parte em uma frase:

1. Instrução: uma ação específica, no imperativo, que evita o risco.
2. Risco: o que a ação perigosa faz ao sistema.
3. Consequência: o efeito sobre os dados, o serviço, as pessoas ou os custos.

A instrução é uma ação específica. Não use instruções gerais: "Tenha cuidado", "Preste atenção", "Fique atento", "Atenção ao".

**Justificativa:** O leitor que lê apenas a primeira frase já sabe como evitar o risco. O risco e a consequência explicam por que a instrução é importante.

**Verificação:** O revisor verifica que a primeira frase do aviso começa com um imperativo ou com "Não" + imperativo. O revisor procura as instruções gerais da lista e verifica a ordem do risco e da consequência.

**Não aprovado:**

> **PERIGO:** Tenha cuidado com o arquivo `.env`, pois ele contém informações sensíveis que podem vazar.

**PTS-BR:**

> **PERIGO:** Não envie o arquivo `.env` ao repositório Git. O arquivo `.env` contém as credenciais do banco de produção. Qualquer pessoa com acesso ao repositório vai poder ler e alterar os dados dos clientes.

### R7.4 Escreva o aviso antes da ação perigosa `[revisor]`

**Enunciado:** Escreva o aviso imediatamente antes do passo com o risco. Se o risco existir em todo o procedimento, escreva o aviso antes do passo 1. Não escreva o aviso dentro da frase do passo nem depois do passo.

**Justificativa:** O leitor começa a ação quando lê o verbo. Um aviso depois do passo chega depois da ação.

**Verificação:** O revisor verifica que cada aviso está antes do passo com o risco.

**Não aprovado:**

> 3. Execute o script `limpar_base.sh`.
>
>    **PERIGO:** o script exclui todas as tabelas.

**PTS-BR:**

> 2. Verifique o servidor e o banco do comando:
>    ```shell
>    psql --host db-homologacao.loja.interno --dbname loja_homologacao \
>      --command "SELECT current_database();"
>    ```
>    A saída mostra o valor `loja_homologacao`. Se a conexão falhar ou se a saída mostrar outro valor, não faça o passo 3. Este procedimento termina neste passo.
>
> **PERIGO:** Faça o passo 3 apenas no banco `loja_homologacao`. O script `limpar_base.sh` exclui todas as tabelas do banco conectado. Em produção, o script exclui os dados de todos os clientes, também os dados de depois do último backup.
>
> 3. Execute o script no banco `loja_homologacao`:
>    ```shell
>    ./limpar_base.sh --host db-homologacao.loja.interno --dbname loja_homologacao
>    ```

### R7.5 Escreva um risco por aviso `[revisor]`

**Enunciado:** Cada aviso tem um único risco. Se uma ação tiver 2 riscos, escreva 2 avisos, do mais grave para o menos grave.

**Justificativa:** Um aviso com 2 ou mais riscos é longo, e o leitor lê apenas o primeiro risco.

**Verificação:** O revisor verifica que cada aviso tem uma frase de risco e uma frase de consequência.

**Não aprovado:**

> **ATENÇÃO:** Ao reiniciar o cluster, os pods ficam indisponíveis, o cache é perdido, as filas podem acumular mensagens e as credenciais temporárias expiram.

**PTS-BR:**

> **ATENÇÃO:** Reinicie o cluster apenas na janela de manutenção. Todos os pods param por 5 a 10 min quando o cluster reinicia. Durante este tempo, os clientes não podem acessar o site `loja-web`.

> **CUIDADO:** Informe a equipe de suporte antes de reiniciar o cluster. O cluster limpa o cache da API quando reinicia. Por 15 min, a API responde em até 2 s, em vez de 200 ms.

O primeiro aviso é ATENÇÃO, não PERIGO: o site fica indisponível, mas a duração é conhecida e o sistema volta automaticamente. O segundo aviso é CUIDADO: a API tem uma latência maior, mas todas as funcionalidades do site continuam disponíveis (regra [R7.1](#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor)).

### R7.6 Escreva a consequência com o objeto e o efeito `[revisor]`

**Enunciado:** A frase de consequência diz o objeto afetado e o efeito. O objeto afetado é um banco, um serviço, um ambiente, uma conta ou um dado. Não use consequências vagas: "pode causar problemas", "pode gerar erros", "comportamento inesperado", "danos ao sistema", "pode afetar".

**Justificativa:** Uma consequência vaga não permite ao leitor avaliar o risco. O leitor não lê os avisos que não dizem o efeito da ação.

**Verificação:** O revisor procura as expressões vagas da lista dentro de avisos e confirma que a consequência diz o objeto afetado e o efeito.

**Não aprovado:**

> **ATENÇÃO:** Não altere esta configuração, pois isso pode causar problemas no sistema.

**PTS-BR:**

> **ATENÇÃO:** Altere o valor de `max_connections` em produção apenas com a aprovação da equipe de banco de dados. O banco reserva memória para cada conexão. Com um valor maior que 500, o banco `pedidos` não responde. O banco volta quando a equipe restaura o valor de `max_connections`.

### R7.7 Marque o aviso apenas com a palavra de sinalização `[revisor]`

**Enunciado:** Escreva a palavra de sinalização em maiúsculas e em negrito, seguida de dois-pontos. A palavra de sinalização inicia um bloco separado do texto: um bloco de citação ou um componente de aviso. Escreva as outras partes do aviso em texto normal, com frases completas. Exceção: os nomes de elementos de interface e os valores de estado dentro do aviso seguem as regras [R8.8](#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) e [R10.1](#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor). Não use maiúsculas nem pontos de exclamação como ênfase em outros lugares do documento.

**Justificativa:** Um formato fixo permite ao leitor encontrar os avisos em uma leitura rápida da página. Uma ênfase fora deste formato diminui o efeito dos avisos.

**Verificação:** O revisor verifica o formato da palavra de sinalização. O revisor também procura palavras com todas as letras em maiúsculas que não são siglas nem palavras de sinalização.

**Não aprovado:**

> NUNCA execute este comando em PRODUÇÃO!!!

**PTS-BR:**

> **ATENÇÃO:** Execute este comando apenas no ambiente `homologacao`. O comando exclui todos os índices do Elasticsearch. Em produção, os clientes não podem procurar produtos no site por até 6 h, até a equipe indexar os produtos de novo.

### R7.8 Identifique o ambiente antes de um comando que altera ou exclui dados `[revisor]`

**Enunciado:** Antes de um passo que altera ou exclui dados, recursos ou configurações, escreva um passo de verificação. Este passo mostra o alvo do comando e o resultado esperado. O alvo é o ambiente, o cluster, o servidor, a conta, a região ou o banco. Escreva o nome do ambiente no aviso e no comando. No comando, use a opção explícita que define o alvo. Não dependa do alvo padrão do terminal. Esta tabela mostra a opção de alvo e o passo de verificação de cada ferramenta:

| Ferramenta | Opção de alvo | Passo de verificação |
|---|---|---|
| `kubectl` | `--context` e `--namespace` | `kubectl cluster-info --context <contexto>`. A primeira linha da saída mostra o endereço do cluster. Um comando `kubectl get` mostra que o objeto existe, mas não mostra qual cluster responde. |
| `helm` | `--kube-context` e `--namespace`. O Helm não tem a opção `--context`. | `kubectl cluster-info --context <contexto>`, com o mesmo nome de contexto. |
| `psql`, `pg_dump`, `pg_restore` | `--host` e `--dbname` | `psql --host <servidor> --dbname <banco> --command "SELECT current_database();"`. A saída mostra o nome do banco. |
| `aws` | `--profile` e `--region` | `aws sts get-caller-identity --profile <profile>`. A saída mostra o número da conta. |
| `terraform` | O Terraform não tem uma opção de alvo em cada comando. O comando `terraform workspace select` e o backend definem o alvo. | `terraform workspace show`. A saída mostra o nome do alvo. |

**Justificativa:** Um terminal conectado ao ambiente incorreto é uma causa comum de perda de dados em produção. O passo de verificação mostra o alvo real antes da ação, e a opção explícita impede a execução no alvo padrão.

**Verificação:** O revisor verifica que cada passo que altera ou exclui dados tem, antes, um passo que mostra o alvo, com o comando da tabela. O revisor confirma que o passo de verificação e o comando usam o mesmo alvo explícito. O revisor verifica que o aviso e o comando têm o nome do ambiente.

O passo de verificação usa a mesma opção de alvo que o comando. O comando `kubectl config current-context` mostra apenas o contexto padrão do terminal e não verifica um comando com a opção `--context`.

**Não aprovado:**

> **PERIGO:** Confirme que você está em homologação.
>
> 4. Exclua o namespace:
>    ```shell
>    kubectl delete namespace pedidos --context homologacao-sa-east-1
>    ```

**PTS-BR:**

> 3. Verifique o cluster do contexto `homologacao-sa-east-1`:
>    ```shell
>    kubectl cluster-info --context homologacao-sa-east-1
>    ```
>    A primeira linha da saída mostra o endereço `https://k8s.homologacao.loja.interno:6443`. Se o endereço for outro, não faça o próximo passo. Este procedimento termina neste passo.
>
> **PERIGO:** Faça o passo 4 apenas no contexto `homologacao-sa-east-1`. O comando exclui o namespace `pedidos` e todos os dados do namespace. Em produção, o sistema perde os pedidos dos clientes sem recuperação.
>
> 4. Exclua o namespace:
>    ```shell
>    kubectl delete namespace pedidos --context homologacao-sa-east-1
>    ```

### R7.9 Não coloque segredos na linha de comando nem no texto `[revisor]`

**Enunciado:** Não escreva o valor real de um segredo no documento: senha, token, chave privada ou chave de API. Use um espaço reservado (regra [R8.9](#r89-escreva-espaços-reservados-em-um-formato-único-revisor)). Não escreva um segredo como argumento de um comando, também na forma de uma variável de ambiente (`"$API_TOKEN"`). O shell grava o comando no histórico. Antes de executar o comando, o shell substitui a variável pelo valor. Outros usuários do mesmo computador podem ver este valor na lista de processos (`ps`). Use uma destas formas:

- O prompt da ferramenta, que lê o segredo sem mostrar o segredo na tela.
- Um arquivo de configuração ou de senhas com a permissão 600, que apenas o seu usuário pode ler, por exemplo o arquivo `~/.pgpass` do `psql`. O `psql` não lê o arquivo `~/.pgpass` com outra permissão. Verifique a permissão com o comando `ls -l ~/.pgpass`: a saída começa com `-rw-------`.
- A entrada padrão de um comando interno do shell: `printf 'Authorization: Bearer %s\n' "$API_TOKEN" | curl --header @- https://api.loja.com.br/v1/pedidos`. O comando `printf` é interno do shell e não aparece na lista de processos. O cofre de segredos define a variável `API_TOKEN`.

Não use uma variável de ambiente que contém o segredo e que a ferramenta lê, por exemplo `PGPASSWORD`. Em um sistema operacional que mostra o ambiente dos processos a outros usuários, estes usuários veem o segredo. A documentação do PostgreSQL não recomenda a variável `PGPASSWORD`. Use uma variável de ambiente com um segredo apenas se a ferramenta não tiver um prompt nem um arquivo de senhas.

Em imagens da tela, logs e chamados, mascare o segredo ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), verbo MASCARAR).

**Justificativa:** Um segredo no histórico do shell, na lista de processos, em um log ou em um chamado é uma credencial exposta. Qualquer pessoa com acesso ao computador, ao log ou ao chamado pode usar a credencial.

**Verificação:** O revisor procura senhas, tokens e chaves em comandos, em exemplos de saída e em imagens da tela. O revisor também procura opções de senha com valor, por exemplo `-p<senha>` e `--password=`, e variáveis de segredo em argumentos, por exemplo `--header "Authorization: Bearer $API_TOKEN"`.

**Não aprovado:**

> 2. Conecte o terminal ao banco:
>    ```shell
>    mysql --host db-prod.loja.interno --user admin --password=S3nhaForte
>    ```

**PTS-BR:**

> **PERIGO:** Não escreva a senha no comando. O shell grava o comando no histórico do usuário. Qualquer pessoa com acesso ao computador pode ler a senha do banco de produção.
>
> 2. Conecte o terminal ao banco:
>    ```shell
>    mysql --host db-prod.loja.interno --user admin --password
>    ```
>    O comando pede a senha. Digite a senha do item `mysql-prod-admin` do cofre de segredos.

**Não aprovado:**

> ```shell
> curl --fail --header "Authorization: Bearer $API_TOKEN" https://api.loja.com.br/v1/pedidos
> ```

**PTS-BR:**

> ```shell
> printf 'Authorization: Bearer %s\n' "$API_TOKEN" \
>   | curl --fail --header @- https://api.loja.com.br/v1/pedidos
> ```
>
> O comando `printf` envia o cabeçalho ao `curl` pela entrada padrão. O valor do token não aparece na lista de processos. A opção `--header @-` precisa da ferramenta `curl` na versão 7.55 ou em uma versão mais nova.

---

## Seção 8: Pontuação e formatação

### R8.1 Termine as frases com ponto final `[revisor]`

**Enunciado:** Termine cada frase com ponto final, também nos passos de procedimento e nos itens de lista que são frases. Não use ponto final em títulos, em tabelas, nos valores que não são frases, e em itens de lista que não são frases. Não use ponto de exclamação. Use ponto de interrogação apenas em perguntas de diálogos de interface (regra [R10.6](#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor)) e em uma lista de perguntas e respostas.

**Justificativa:** O ponto final marca o fim de uma instrução e permite à ferramenta contar as frases e as palavras. O ponto de exclamação adiciona emoção e nenhuma informação.

**Verificação:** O revisor verifica o último caractere de cada frase, de cada passo e de cada título.

**Não aprovado:** 2. Clique em **Salvar**

**PTS-BR:** 2. Clique em **Salvar**.

**Não aprovado:** `## Como configurar o proxy.`

**PTS-BR:** `## Configurar o proxy`

### R8.2 Use a vírgula de acordo com a estrutura da frase `[revisor]`

**Enunciado:** Não escreva vírgula entre o sujeito e o verbo, nem entre o verbo e o complemento. Escreva vírgula depois de uma condição ou de um local no início da frase: "Se o teste falhar, volte ao passo 2." e "Na página **Perfil**, clique em **Salvar**."

**Justificativa:** A vírgula entre o sujeito e o verbo separa partes que o leitor precisa ler juntas. A vírgula depois da condição mostra o início da ação.

**Verificação:** O revisor procura a falta de vírgula depois de uma oração com "se" ou "quando" no início da frase. O revisor também procura a vírgula entre o sujeito e o verbo.

**Não aprovado:** O servidor de autenticação, valida o token.

**PTS-BR:** O servidor de autenticação valida o token.

**Não aprovado:** Se o teste falhar volte ao passo 2.

**PTS-BR:** Se o teste falhar, volte ao passo 2.

### R8.3 Não use ponto e vírgula, barra entre palavras nem inserções `[revisor]`

**Enunciado:** Não use ponto e vírgula. Não use barra entre palavras ("e/ou", "usuário/senha", "ativar/desativar"). Não use parênteses nem travessões para adicionar uma informação dentro da frase. Use parênteses apenas nestas situações:

- Uma sigla na primeira ocorrência (regra [R8.7](#r87-defina-as-siglas-na-primeira-ocorrência-revisor)).
- O valor em outra unidade.
- Uma referência a uma regra, a uma seção ou a um arquivo.
- Um exemplo curto entre aspas ou em formato de código, imediatamente depois da palavra que o exemplo mostra.

**Justificativa:** Estes sinais juntam ideias que o leitor precisa separar. Com "e/ou" e com a barra, o leitor precisa decidir se o texto indica "e" ou "ou".

**Verificação:** O revisor procura ponto e vírgula, barra entre 2 palavras fora de literais, travessões e parênteses com mais de 4 palavras.

**Não aprovado:** Configure a porta (use 8080, ou 8443 se o TLS estiver ativo; a porta 80 não funciona) e reinicie o serviço.

**PTS-BR:** Se o TLS estiver ativo, configure a porta 8443. Se o TLS não estiver ativo, configure a porta 8080.

**Não aprovado:** Use o token e/ou o certificado.

**PTS-BR:** Use o token, o certificado ou ambos.

### R8.4 Escreva números e unidades em um formato fixo `[vale]`

**Enunciado:**

- Escreva todas as quantidades em algarismos ("3 servidores"). Exceção: "um" e "uma" como artigo. Uma frequência também é uma quantidade: "1 vez por dia", não "uma vez por dia".
- No texto, use vírgula como separador decimal ("2,5 s"). Em literais de código, valores de configuração e números de versão, use o formato original (`timeout: 2.5`, versão 2.5.1).
- Em quantidades com 4 ou mais algarismos antes da vírgula, use um espaço como separador de milhar ("10 000"). Não use ponto como separador de milhar. Identificadores não têm separador: portas, anos e códigos ("porta 8080").
- Depois de um número, escreva o símbolo da unidade, não o nome da unidade: "10 min", "1 h", "30 s", "512 MB". Escreva um espaço entre o número e o símbolo. Exceção: o símbolo "%" não tem espaço antes ("99,9%").
- Use os símbolos do Sistema Internacional de Unidades (SI) e da Comissão Eletrotécnica Internacional (IEC). Os símbolos são: ms, s, min, h, kB, MB, GB, TB, KiB, MiB, GiB, TiB. O prefixo "k" é minúsculo. Os prefixos "M", "G" e "T" são maiúsculos.
- Nos prefixos decimais, 1 kB = 1 000 B. Nos prefixos binários, 1 KiB = 1 024 B. O símbolo do byte é B. Use o prefixo que o sistema configura ou mostra. Os limites de memória de contêiner usam o prefixo binário: `512Mi` é 512 MiB.
- Para a quantidade de dados por segundo, use bit/s com prefixo: kbit/s, Mbit/s, Gbit/s. Não use "Mbps", "KB", "Gb" no lugar de "GB" nem abreviaturas fora do SI ("seg", "mins", "hrs").
- Para dias, semanas, meses e anos, escreva a palavra: "5 dias úteis", "2 semanas".

**Justificativa:** O ponto é o separador de milhar no Brasil e o separador decimal em inglês. Portanto, "1.000" tem 2 leituras: "mil" ou "um". O espaço é a recomendação do SI e tem uma única leitura nas 2 línguas. O símbolo da unidade tem a mesma forma em todas as línguas.

**Verificação:** O Vale detecta o ponto entre grupos de 3 algarismos fora de literais e o nome da unidade depois de um número ("10 minutos"). O revisor verifica os números por extenso, o espaço antes do símbolo e os prefixos.

**Não aprovado:** O limite é de dez mil requisições e o timeout é 2.5seg.

**PTS-BR:** O limite é 10 000 requisições por minuto. O tempo limite da requisição é 2,5 s.

**Não aprovado:** O backup tem 2.000 megabytes e demora 40 minutos.

**PTS-BR:** O backup tem 2 000 MB e demora 40 min.

### R8.5 Escreva datas no formato ISO 8601 e horas com o fuso horário `[revisor]`

**Enunciado:** Escreva as datas no formato AAAA-MM-DD ("2026-11-18"). Escreva as horas no formato de 24 h, com 2 algarismos para a hora e 2 para os minutos ("09:30"). Em prosa, escreva o fuso horário depois da hora: "UTC" ou "UTC" com o deslocamento no formato `+HH:MM` ou `-HH:MM` ("09:30 UTC", "09:30 UTC-03:00"). Em literais de API, de log e de configuração, use o formato da RFC 3339, com o deslocamento junto da hora: `2026-12-05T02:00:00-03:00` ou `2026-12-05T05:00:00Z`. Em uma linha do tempo de incidente, use UTC. Não escreva datas nos formatos DD/MM ou MM/DD. Exceção: um texto de interface mostra a data no formato da língua do usuário.

A palavra "hora" indica um momento do dia. Para uma duração, escreva o número e o símbolo "h" (regra [R8.4](#r84-escreva-números-e-unidades-em-um-formato-fixo-vale)): "Aguarde 1 h."

**Justificativa:** O formato DD/MM/AAAA e o formato MM/DD/AAAA dos Estados Unidos são iguais nos dias de 1 a 12. O formato AAAA-MM-DD tem uma única leitura e é o formato dos logs e das APIs. Uma hora sem fuso horário tem uma leitura diferente em cada fuso horário. A RFC 3339 é uma forma da ISO 8601 que as APIs e os logs usam.

**Verificação:** O revisor procura datas com barras, horas sem minutos ("2h") e horas sem fuso horário.

**Não aprovado:** A manutenção vai acontecer dia 5/12 às 2h.

**PTS-BR:** A manutenção começa em 2026-12-05, às 02:00 UTC-03:00.

### R8.6 Use maiúsculas apenas no início das frases e em nomes próprios `[revisor]`

**Enunciado:** Use letra maiúscula apenas no início de frases, títulos e itens de lista, e em nomes próprios. Em títulos, use maiúscula apenas na primeira palavra e nos nomes próprios. Escreva os nomes de produtos e de empresas com a grafia da empresa do produto ("GitHub", "macOS", "PostgreSQL"). Não use maiúscula em substantivos comuns, nos meses e nos dias da semana. A regra [R10.1](#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor) tem prioridade para rótulos de interface.

**Justificativa:** Em português, a letra maiúscula marca um nome próprio. Uma maiúscula em um substantivo comum faz o leitor procurar um produto ou um componente com este nome.

**Verificação:** O revisor procura palavras com maiúscula dentro da frase que não estão na lista de nomes próprios e de termos técnicos. O revisor verifica a grafia dos nomes de produtos.

**Não aprovado:** O Usuário envia o Formulário para o Servidor.

**PTS-BR:** O usuário envia o formulário para o servidor.

**Não aprovado:** Instale o Github CLI no MacOS.

**PTS-BR:** Instale o GitHub CLI no macOS.

### R8.7 Defina as siglas na primeira ocorrência `[revisor]`

**Enunciado:** Na primeira ocorrência de uma sigla em um documento, escreva a forma por extenso e depois a sigla entre parênteses. Nas outras ocorrências, use apenas a sigla. Exceção: uma sigla do glossário-base ou da tabela de siglas de uso geral de [`04-termos-tecnicos.md`](04-termos-tecnicos.md) não precisa de definição. Escreva a sigla com as maiúsculas do padrão técnico. No plural, adicione "s" minúsculo, sem apóstrofo ("APIs", "IDs"). O gênero da sigla é o gênero do substantivo principal da forma por extenso em português ("a API": a interface).

**Justificativa:** Uma sigla sem definição é uma palavra desconhecida para um leitor novo. O leitor de TI lê as siglas de uso geral, como HTTP e JSON, sem a forma por extenso. O apóstrofo no plural é uma forma do inglês e não existe no português.

**Verificação:** O revisor procura as siglas sem definição antes do primeiro uso que não estão na tabela de siglas de uso geral. O revisor também procura siglas com apóstrofo.

**Não aprovado:** Configure o IdP da empresa no portal.

**PTS-BR:** Configure o provedor de identidade (IdP) da empresa no portal.

**Não aprovado:** Liste as API's do projeto.

**PTS-BR:** Liste as APIs do projeto.

**Aprovado:** A API retorna um objeto JSON no corpo da resposta HTTP.

### R8.8 Use cada formato tipográfico com um único significado `[revisor]`

**Enunciado:** Use os formatos tipográficos apenas com os significados desta tabela. Não use negrito, itálico ou aspas como ênfase.

| Formato | Significado | Exemplo |
|---|---|---|
| Negrito | Nome de um elemento de interface. Valor de estado que a interface mostra. Palavra de sinalização de um aviso. | Clique em **Salvar**. O estado do usuário é **Inativo**. |
| Código | Texto literal que o leitor digita ou que o sistema lê: comando, arquivo, pasta, variável, valor, código de erro, endpoint. Valor de estado que uma CLI, uma API ou um log mostra. | Defina a variável `PORT`. O pod está no estado `Running`. |
| Aspas duplas | Mensagem completa que o sistema mostra, citada em um documento. | A tela mostra a mensagem "Arquivo salvo." |
| Itálico | Um termo na ocorrência em que o texto define o termo. | Um *nó* é um servidor do cluster. |

O texto de uma mensagem em um arquivo de tradução ou no código é um literal: use o formato de código (regras [R10.4](#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) a [R10.9](#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor)). Use as aspas duplas para uma mensagem completa que um documento cita como resultado de um passo. Para uma parte de uma mensagem de CLI ou de log que o leitor procura na saída, use o formato de código ("A saída mostra a mensagem `successfully rolled out`.").

Em prosa, use "estado" para a condição de um sistema ou de um componente. Use "status" apenas dentro de um literal, de um rótulo ou de um termo técnico do glossário, por exemplo "código de status".

**Justificativa:** Cada formato diz ao leitor o que fazer com o texto: clicar, digitar, ler ou conhecer um termo. Um formato com 2 significados não mostra esta informação.

**Verificação:** O revisor compara o texto em negrito com a interface e o texto em código com os literais do sistema. O revisor verifica as aspas e o itálico.

**Não aprovado:** Clique no botão "Salvar" e defina a variável **PORT** com o valor 8080.

**PTS-BR:** Clique em **Salvar**. Defina o valor `8080` na variável `PORT`.

### R8.9 Escreva espaços reservados em um formato único `[revisor]`

**Enunciado:** Escreva um espaço reservado entre os sinais `<` e `>`, em português, com letras minúsculas, sem acentos e com hífen entre as palavras: `<nome-do-servidor>`. Depois do bloco de código, explique cada espaço reservado em uma lista. Antes da lista, escreva que o leitor também substitui os sinais `<` e `>`. Não use outros formatos: `HOST`, `{{host}}`, `[host]`, `SEU_HOST`, `xxx`. Uma variável de ambiente que o leitor usa sem alteração (`$HOME`) é um literal, não um espaço reservado. Esta regra é para o texto que o leitor digita ou copia. As variáveis de um arquivo de tradução seguem a regra [R10.8](#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor) e o formato do sistema de tradução (`{nome_arquivo}`).

**Justificativa:** Um formato único mostra ao leitor o que copiar sem alteração e o que substituir. No shell, os sinais `<` e `>` enviam a entrada ou a saída de um comando para um arquivo. Um espaço reservado que o leitor não substituiu gera um erro ou grava sobre um arquivo.

**Verificação:** O revisor procura, nos blocos de shell (`shell`, `bash`, `sh`, `console`), palavras em maiúsculas sem definição, a sequência "{{", colchetes e a sequência "xxx". O revisor verifica que cada espaço reservado está na lista depois do bloco.

**Não aprovado:** Execute `ssh user@HOST -i YOUR_KEY`.

**PTS-BR:**

> Execute o comando:
>
> ```shell
> ssh -i <arquivo-da-chave> <usuario>@<servidor>
> ```
>
> Substitua cada espaço reservado, com os sinais `<` e `>`:
>
> - `<arquivo-da-chave>`: o caminho do arquivo da chave privada.
> - `<usuario>`: o seu nome de usuário no servidor.
> - `<servidor>`: o endereço IP ou o nome do servidor.

---

## Seção 9: Práticas de escrita

### R9.1 Escreva para o leitor na forma "você" `[revisor]`

**Enunciado:** Escreva as instruções no imperativo da forma "você", sem pronome. Escreva o pronome "você" apenas em texto descritivo, se a frase precisar de um sujeito. Não use "tu", "o senhor", "a senhora", o pronome "nós", "a gente" nem "vamos" + infinitivo. "Nós", plural do nome técnico "nó", é aprovado: escreva um artigo, uma contração ou um número antes deste plural ("os nós", "3 nós") ([`03-dicionario.md`](03-dicionario.md), regra D11). Não use "o usuário deve" em uma ordem ao leitor. Use "o usuário" apenas para uma pessoa que não é o leitor, por exemplo o cliente de uma aplicação.

**Justificativa:** Uma forma de tratamento fixa mostra ao leitor que a instrução é para o leitor. "Nós" e "vamos" não mostram o autor da ação.

**Verificação:** O revisor procura "tu", "o senhor", "a senhora", "nós" sem artigo, contração ou número antes, "a gente", "vamos" + infinitivo, verbos na primeira pessoa do plural e "o usuário deve".

**Não aprovado:** Agora vamos configurar o proxy.

**PTS-BR:** Configure o proxy.

**Não aprovado:** O usuário deve informar a senha do banco.

**PTS-BR:** Digite a senha do banco.

**Não aprovado:** Tu podes alterar a porta no arquivo `.env`.

**PTS-BR:** Você pode alterar a porta no arquivo `.env`.

### R9.2 Não use linguagem figurada, gíria nem personificação `[revisor]`

**Enunciado:** Não use expressões idiomáticas, gírias, regionalismos, metáforas nem personificação de sistemas ("o sistema quer", "o servidor não gosta", "o script sabe"). Descreva a ação ou o estado real. Nomes de comandos, como `kill`, são literais e estão fora desta regra.

**Justificativa:** O leitor não nativo lê a expressão figurada palavra por palavra e entende outro significado. A tradução automática tem o mesmo erro.

**Verificação:** O revisor procura expressões figuradas e gírias. O revisor também procura os verbos "querer", "gostar", "saber" e "achar" com um sistema como sujeito.

**Não aprovado:** Mate o processo e dê um up no serviço.

**PTS-BR:** Pare o processo. Inicie o serviço.

**Não aprovado:** O servidor caiu e a fila está bombando.

**PTS-BR:** O servidor está indisponível. A fila tem 50 000 mensagens.

**Não aprovado:** O sistema não gosta de arquivos grandes.

**PTS-BR:** O sistema não aceita arquivos com mais de 10 MB.

### R9.3 Não use palavras vazias, de julgamento ou de cortesia `[revisor]`

**Enunciado:** Não use "simplesmente", "basta", "fácil", "facilmente", "obviamente", "claramente", "é claro que", "naturalmente", "rapidinho", "por favor", "favor" nem "gentileza".

**Justificativa:** Estas palavras não adicionam informação. Se o passo falhar, "basta" e "fácil" dizem ao leitor que o erro é do leitor.

**Verificação:** O revisor procura as palavras da lista. A regra [R1.1](#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) detecta as palavras da lista que [`03-dicionario.md`](03-dicionario.md) marca como não aprovadas.

**Não aprovado:** Basta clicar em **Salvar**.

**PTS-BR:** Clique em **Salvar**.

**Não aprovado:** Por favor, aguarde a conclusão do processo.

**PTS-BR:** Aguarde o fim do processo.

**Não aprovado:** Obviamente, o token precisa ser válido.

**PTS-BR:** Use um token válido.

### R9.4 Escreva referências estáveis `[revisor]`

**Enunciado:** Para citar outra parte do documento, use o número ou o título da seção, do passo, da imagem ou da tabela: "a tabela 3", "o passo 4". Use "acima" e "abaixo" apenas para o elemento imediatamente antes ou depois do texto, na mesma página ou na mesma tela: "Execute o comando abaixo." Não use "acima" e "abaixo" para comparar valores. Para comparar valores, use "maior que" e "menor que". Não use "anterior", "seguinte", "a seguir" nem "como vimos" para citar uma parte do documento. Não use palavras que dependem da data de publicação do texto: "atualmente", "hoje", "recentemente", "em breve", "a nova versão", "a versão atual do produto". Não use "novo" e "antigo" para comparar com a data do texto. Escreva a versão ou a data. Use "atual" e "agora" apenas para o momento em que o leitor segue o procedimento ou vê a interface: "o contexto atual do terminal".

**Justificativa:** A posição de um elemento que não está ao lado do texto depende da formatação da página. Esta posição não tem significado em um leitor de tela. Com o elemento imediatamente ao lado do texto, "acima" e "abaixo" não têm esta dúvida. Uma palavra como "novo" é falsa depois da próxima versão do produto. O momento em que o leitor segue o procedimento não depende da versão do produto.

**Verificação:** O revisor procura as palavras da lista. O revisor confirma que cada "acima" e cada "abaixo" indica um elemento imediatamente ao lado do texto.

**Não aprovado:** Use o comando da seção anterior para reiniciar o serviço.

**PTS-BR:** Use o comando do passo 3 para reiniciar o serviço.

**Não aprovado:** A latência está acima do limite.

**PTS-BR:** A latência é maior que o limite de 200 ms.

**Não aprovado:** A nova tela de login aceita MFA.

**PTS-BR:** Na versão 4.2, a tela de login aceita MFA.

**Aprovado:** Execute o comando abaixo.

Neste exemplo, o bloco de código está imediatamente depois da frase.

**Aprovado:** Aguarde até o pod ficar no estado `Running`. Agora, faça o passo 5.

Neste exemplo, "agora" indica o momento em que o leitor segue o procedimento.

### R9.5 Escreva listas completas `[revisor]`

**Enunciado:** Escreva todos os itens de uma lista que o leitor usa em uma ação. Não use "etc.", "entre outros", "e assim por diante" nem reticências no fim de uma lista. Se a lista completa estiver em outro lugar, escreva a referência à lista.

**Justificativa:** O leitor não sabe quais itens o "etc." indica. Em uma configuração, um item que falta causa um erro.

**Verificação:** O revisor procura as expressões da lista e reticências no fim de uma lista.

**Não aprovado:** Configure as variáveis `DB_HOST`, `DB_PORT` etc.

**PTS-BR:**

> Configure estas 4 variáveis:
>
> - `DB_HOST`
> - `DB_PORT`
> - `DB_USER`
> - `DB_PASSWORD`

**Não aprovado:** O agente coleta métricas de CPU, memória, entre outras.

**PTS-BR:** O agente coleta as métricas da tabela "Métricas do agente".

---

## Seção 10: Interface, mensagens de software e textos de desenvolvimento

As regras desta seção são sobre 3 tipos de texto:

- A documentação que cita a interface: regras [R10.1](#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor) a [R10.3](#r103-escreva-caminhos-de-menu-e-teclas-em-um-formato-fixo-revisor).
- Os textos da própria interface: regras [R10.4](#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) a [R10.9](#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor).
- Os textos de desenvolvimento: regra [R10.10](#r1010-escreva-textos-de-desenvolvimento-com-um-formato-fixo-revisor).

### R10.1 Escreva o nome exato do elemento de interface em negrito `[revisor]`

**Enunciado:** Escreva o nome de um elemento de interface em negrito, com o texto exato do rótulo: as mesmas letras, maiúsculas, acentos e pontuação. Os elementos de interface são botões, menus, guias, campos, caixas de seleção, janelas e itens de lista. Se a interface estiver em inglês, escreva o rótulo em inglês. Se o elemento não tiver rótulo, descreva o elemento pela ação do elemento e pela posição ("o ícone de lápis ao lado do nome do projeto"). Esta regra tem prioridade sobre a regra [R8.6](#r86-use-maiúsculas-apenas-no-início-das-frases-e-em-nomes-próprios-revisor).

**Justificativa:** O leitor procura na tela o texto que lê no documento. Uma diferença de uma letra ou uma tradução do rótulo faz o leitor procurar um elemento que não existe.

**Verificação:** O revisor compara cada texto em negrito com a interface ou com os arquivos de tradução da interface.

**Não aprovado:** Clique no botão salvar alterações.

**PTS-BR:** Clique em **Salvar alterações**.

**Não aprovado:** Com a interface em inglês: Clique em **Implantar**.

**PTS-BR:** Clique em **Deploy**.

### R10.2 Use o verbo do tipo de elemento `[revisor]`

**Enunciado:** Use o verbo da tabela para cada tipo de elemento. Escreva o tipo do elemento depois do verbo apenas se 2 elementos da mesma tela tiverem o mesmo rótulo. Um item de uma lista da interface é um rótulo: escreva o item em negrito (regra [R10.1](#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor)).

| Elemento | Verbo |
|---|---|
| Botão, link, ícone, guia | clicar em. Em uma tela que o usuário toca: tocar em. |
| Item de lista, opção de um menu, botão de opção | selecionar |
| Caixa de seleção | marcar, desmarcar |
| Interruptor | ativar, desativar |
| Campo de texto | digitar ... em |
| Uma tecla, ou 2 ou mais teclas ao mesmo tempo | pressionar |
| Arquivo, janela ou item que o leitor move | arrastar |

**Justificativa:** Um verbo fixo para cada tipo de elemento mostra ao leitor a ação física exata.

**Verificação:** O revisor compara o verbo com o tipo do elemento na tela.

**Não aprovado:** Clique na caixa **Lembrar de mim**.

**PTS-BR:** Marque **Lembrar de mim**.

**Não aprovado:** Escolha a região na lista **Região**.

**PTS-BR:** Selecione **sa-east-1** na lista **Região**.

### R10.3 Escreva caminhos de menu e teclas em um formato fixo `[revisor]`

**Enunciado:** Em um caminho de menu, escreva cada item em negrito e separe os itens com " > ": **Configurações** > **Segurança** > **Tokens**. Escreva o nome de uma tecla em negrito, com o texto do teclado: **Enter**, **Esc**, **Ctrl**. Para 2 ou mais teclas ao mesmo tempo, junte as teclas com "+", sem espaços: **Ctrl+Shift+P**.

**Justificativa:** Um formato fixo mostra o caminho em uma linha. O leitor segue o caminho sem dúvida.

**Verificação:** O revisor verifica o separador " > ", o negrito de cada item e o formato das teclas.

**Não aprovado:** Vá em Configurações, depois em Segurança e depois em Tokens.

**PTS-BR:** Selecione **Configurações** > **Segurança** > **Tokens**.

**Não aprovado:** Aperte control + shift + p.

**PTS-BR:** Pressione **Ctrl+Shift+P**.

### R10.4 Escreva a mensagem de erro com o que aconteceu e o que fazer `[revisor]`

**Enunciado:** Uma mensagem de erro tem esta estrutura, com no máximo 4 frases:

1. O que aconteceu: uma frase no pretérito perfeito ou no presente. Use o objeto afetado como sujeito, na voz ativa ou com "estar" + particípio ("O pedido não está gravado."). Use "o sistema" como sujeito apenas se as 2 formas não tiverem o objeto afetado como sujeito.
2. A causa: uma frase. Escreva a causa apenas se o sistema conhecer a causa.
3. O que fazer: uma ou 2 frases no imperativo, com uma ação que o usuário pode fazer.
4. O código do erro, no fim, para a equipe de suporte. Esta parte é opcional.

Se a causa for uma característica do objeto afetado, a parte 1 e a parte 2 podem estar na mesma frase ("O arquivo tem mais de 25 MB.").

**Justificativa:** Uma mensagem apenas com o que aconteceu não diz ao usuário como continuar. O objeto afetado como sujeito gera uma mensagem mais curta e mostra ao usuário o item com o problema.

**Verificação:** O revisor verifica que cada mensagem de erro tem a parte 1 e a parte 3 e confirma o sujeito da parte 1.

**Não aprovado:** `Não foi possível enviar o arquivo.`

**PTS-BR:** `O arquivo {nome_arquivo} tem mais de 25 MB. Envie um arquivo com até 25 MB.`

**Não aprovado:** `Erro 500. Falha na operação.`

**PTS-BR:** `O pedido não está gravado. O servidor de pagamentos não respondeu. Tente de novo em 5 min. Se o erro continuar, envie o código PAG-503-17 à equipe de suporte.`

No segundo exemplo, o pedido é o objeto afetado. Na voz ativa, o sujeito de "gravar" é o sistema, não o pedido. Portanto, a frase usa "estar" + particípio, com o pedido como sujeito.

### R10.5 Escreva mensagens de erro sem humor e sem culpa `[revisor]`

**Enunciado:** Não use humor, interjeições ("Ops", "Opa", "Ué"), pontos de exclamação nem frases que dizem que o erro é do usuário ("Você digitou errado", "ação inválida do usuário"). Não use apenas uma mensagem geral: "Algo deu errado", "Erro desconhecido", "Falha na operação". Se o sistema não conhecer a causa, não escreva a parte 2 da regra [R10.4](#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) e escreva uma ação.

**Justificativa:** O usuário que perdeu trabalho não aceita humor em uma mensagem de erro. Uma frase que diz que o erro é do usuário não ajuda o usuário a corrigir o problema.

**Verificação:** O revisor procura as interjeições, os pontos de exclamação e as frases da lista.

**Não aprovado:** `Ops! Você digitou a senha errada!`

**PTS-BR:** `O e-mail ou a senha estão incorretos. Digite o e-mail e a senha de novo.`

**Não aprovado:** `Algo deu errado.`

**PTS-BR:** `O painel não está disponível. Atualize a página. Se o erro continuar, envie o código DASH-000 à equipe de suporte.`

Neste exemplo, o sistema não conhece a causa. A mensagem não tem a parte 2 da regra [R10.4](#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) e não tem uma frase que diz que a causa não está identificada.

### R10.6 Escreva rótulos de botão e diálogos de confirmação com o verbo da ação `[revisor]`

**Enunciado:** Escreva o rótulo de um botão de ação no infinitivo. Adicione o objeto se o verbo sem o objeto for ambíguo: "Salvar", "Excluir projeto", "Enviar convite". Em um diálogo de confirmação, escreva uma pergunta com a ação e o objeto, e uma frase com a consequência. Na frase da consequência, use o sujeito da regra [R10.4](#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor): o objeto afetado. Se a voz ativa e "estar" + particípio não tiverem o objeto afetado como sujeito, use "o sistema". Use rótulos de botão que repetem a ação. Não use "Sim", "Não" e "OK" em diálogos de confirmação. Verifique que a interface mostra o rótulo completo com 30% de caracteres a mais: a tradução para outra língua aumenta o rótulo. Esta regra é uma exceção à regra [R5.2](#r52-use-o-imperativo-nos-passos-revisor): um rótulo é o nome de uma ação na interface, não uma instrução da documentação.

**Justificativa:** O infinitivo é o padrão dos rótulos de botão em português do Brasil nos sistemas operacionais e nas aplicações web. Com "Sim" e "Não", o usuário precisa ler a pergunta de novo antes de decidir.

**Verificação:** O revisor verifica que os rótulos de botão começam com um verbo no infinitivo e procura "Sim", "Não" e "OK" em diálogos de confirmação.

**Não aprovado:**

> Tem certeza? Deseja continuar?
>
> [Sim] [Não]

**PTS-BR:**

> Excluir o projeto `loja-web`? O sistema também vai excluir todos os deploys do projeto.
>
> [Excluir projeto] [Cancelar]

### R10.7 Escreva mensagens de andamento e de sucesso curtas `[revisor]`

**Enunciado:** Uma mensagem de sucesso confirma o resultado em até 6 palavras, sem ponto de exclamação e sem "com sucesso". Na mensagem de sucesso, a forma curta "substantivo + particípio" é aprovada ("Arquivo salvo."). Uma mensagem de andamento de uma ação usa o gerúndio e reticências ("Enviando arquivos…"). Esta regra é uma exceção às regras [R3.3](#r33-use-a-voz-ativa-revisor) e [R3.6](#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), apenas para mensagens de interface.

**Justificativa:** O usuário lê uma mensagem de andamento em menos de 2 s, e a forma curta é o padrão das interfaces em português. A exceção é apenas para estas mensagens, porque a tela mostra o contexto da ação.

**Verificação:** O revisor conta as palavras das mensagens de sucesso e procura pontos de exclamação e a expressão "com sucesso".

**Não aprovado:** `O arquivo foi salvo com sucesso!`

**PTS-BR:** `Arquivo salvo.`

**Não aprovado:** `Aguarde enquanto estamos processando a sua solicitação...`

**PTS-BR:** `Processando o pagamento…`

### R10.8 Escreva textos com variáveis que funcionam com qualquer valor `[revisor]`

**Enunciado:** Nos textos de interface com variáveis:

- Use variáveis com nome (`{nome_arquivo}`). Não use variáveis por posição (`%s`, `{0}`).
- Não escreva um artigo ou um adjetivo em concordância com o valor de uma variável. Escreva um substantivo fixo antes da variável ou escreva a variável depois de dois-pontos.
- Para quantidades, escreva no sistema de tradução 3 formas: para 0 itens, para 1 item e para mais de 1 item. Não use "(s)" nem "(es)".
- Escreva a variável também na forma para 1 item. Não escreva o número 1 como texto fixo. No português do Brasil, a categoria `one` das regras de plural do Unicode também recebe o valor 0. Sem a forma para 0 itens, o usuário vê "0 arquivo excluído.".
- Se o sistema de tradução não tiver uma forma para 0 itens, crie uma chave separada para 0 itens e escolha a chave no código. Por exemplo, as ferramentas `gettext` e Android não têm uma forma para 0 itens no português.

**Justificativa:** A variável recebe valores masculinos, femininos, no singular e no plural, e o texto não conhece o valor. Um texto que funciona apenas com um gênero ou um número mostra erros de concordância para o usuário.

**Verificação:** O revisor procura nos arquivos de tradução as variáveis por posição, as sequências "(s)" e "(es)" e um artigo imediatamente antes de uma variável.

**Não aprovado:** `O {0} foi excluído.` Com o valor "pasta", o usuário vê "O pasta foi excluído."

**PTS-BR:** `Item excluído: {nome_item}.`

**Não aprovado:** `{quantidade} arquivo(s) excluído(s).`

**PTS-BR:** 3 formas no sistema de tradução, no formato `MessageFormat`:

```text
{quantidade, plural, =0 {Nenhum arquivo excluído.} one {# arquivo excluído.} other {# arquivos excluídos.}}
```

O usuário vê "Nenhum arquivo excluído.", "1 arquivo excluído." e, por exemplo, "12 arquivos excluídos."

### R10.9 Escreva textos de validação, de acessibilidade, de link e de estado vazio com a ação `[revisor]`

**Enunciado:** Nos textos de validação de campo, de acessibilidade, de link e de estado vazio:

- Mensagem de validação: diga o valor que o usuário precisa digitar e o formato aceito. Escreva a mensagem ao lado do campo. Não use "inválido" sem o formato.
- Texto de exemplo dentro de um campo (placeholder): escreva apenas um exemplo de valor. Escreva a instrução no rótulo ou no texto de ajuda, porque o texto de exemplo não está visível depois do primeiro caractere.
- Texto alternativo de uma imagem: diga o conteúdo ou o objetivo da imagem em até 2 frases. Não comece com "Imagem de". Para uma imagem sem informação, use um texto alternativo vazio.
- Rótulo de acessibilidade de um botão sem texto, por exemplo `aria-label`: use a forma da regra [R10.6](#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) ("Excluir projeto").
- Texto de um link: escreva o destino do link ("Leia a seção 4.2 do guia de instalação."). Não use "clique aqui", "aqui" nem "este link" como texto do link.
- Estado vazio de uma lista ou de uma tela: escreva a causa da lista vazia e uma ação ("Este projeto não tem deploys. Clique em **Executar deploy** para criar o primeiro deploy.").
- Estado vazio de uma lista com um filtro: escreva o filtro e a ação que limpa o filtro ("Nenhum projeto com o estado **Arquivado**. Clique em **Limpar filtro**.").

**Justificativa:** Um leitor de tela lê o texto alternativo e o rótulo de acessibilidade em vez da imagem e do ícone. Um leitor de tela também lê a lista dos links de uma página sem o texto ao lado. Nesta lista, "clique aqui" não diz o destino. Uma mensagem de validação com o formato permite ao usuário corrigir o valor na primeira tentativa. Um estado vazio com uma ação mostra ao usuário o próximo passo.

**Verificação:** Nos arquivos de tradução e no código da interface, o revisor verifica as mensagens de validação, os textos alternativos e os textos `aria-label`. O revisor também verifica os textos de link e os estados vazios.

**Não aprovado:** `E-mail inválido.`

**PTS-BR:** `Digite o e-mail no formato nome@empresa.com.br.`

**Não aprovado:** Texto alternativo: `Imagem do gráfico de CPU`

**PTS-BR:** Texto alternativo: `Consumo de CPU do nó db-01 entre 09:00 e 10:00 UTC. O valor máximo é 95%, às 09:40 UTC.`

**Não aprovado:** Estado vazio: `Nada aqui.`

**PTS-BR:** Estado vazio: `Este projeto não tem deploys. Clique em Executar deploy para criar o primeiro deploy.`

### R10.10 Escreva textos de desenvolvimento com um formato fixo `[revisor]`

**Enunciado:** Os textos de desenvolvimento do escopo ([`01-introducao.md`](01-introducao.md), [seção 2.1](01-introducao.md#21-textos-no-escopo)) seguem as regras das seções 1 a 9, com estes formatos:

- Descrição de pull request: 3 seções, nesta ordem: "O que altera", "Por que" e "Como testar". A seção "Como testar" é um procedimento (seção 5).
- Mensagem de commit: o corpo diz a causa da alteração em texto descritivo (seção 6). Cada linha do corpo tem no máximo 72 caracteres. O título está fora do escopo ([`01-introducao.md`](01-introducao.md), [seção 2.2](01-introducao.md#22-textos-fora-do-escopo)).
- Mensagem de log para a equipe de operação: uma frase fixa, com o evento no pretérito perfeito e o objeto. Não escreva valores variáveis no texto da mensagem. Escreva os valores em campos, no formato chave=valor ou JSON, com a unidade no nome do campo (`duracao_ms`). Os nomes dos campos, como `level` e `error_code`, são literais.
- Ajuda de CLI: a descrição de um comando ou de uma opção começa com um verbo no presente, na 3ª pessoa do singular ("Exclui o cache local."). Escreva a unidade e o valor padrão.
- Documentação de API pública no código-fonte: texto descritivo (seção 6). Descreva os parâmetros, o valor que a função retorna e as exceções que a função lança.
- Mensagem de erro de uma API ou de uma exceção para o desenvolvedor: o campo ou o argumento, a causa e o formato aceito (`O campo email não tem o caractere @. Formato aceito: nome@empresa.com.br.`).

**Justificativa:** A equipe de operação lê os logs, a ajuda de CLI e as descrições de pull request durante um incidente ou uma revisão. Um formato fixo permite encontrar a informação sem ler todo o texto. As ferramentas de log agrupam os eventos pelo texto da mensagem. Com uma mensagem fixa, a ferramenta conta os eventos do mesmo tipo, e a equipe procura um valor pelo campo.

**Verificação:** O revisor verifica as seções da descrição de pull request, as unidades e os valores padrão da ajuda de CLI. O revisor também verifica o tempo verbal das mensagens de log e da ajuda de CLI. Nas mensagens de log, o revisor procura valores variáveis no texto.

**Não aprovado:** Mensagem de log: `Erro!!! conexão falhou, tentando de novo...`

**PTS-BR:** Mensagem de log: `A conexão com o banco falhou.` Campos: `banco=pedidos duracao_ms=5000 tentativa=2 tentativas_max=3`

**Não aprovado:** Ajuda de CLI: `--timeout    timeout da conexão`

**PTS-BR:** Ajuda de CLI: `--timeout    Define o tempo limite da conexão, em segundos. Valor padrão: 30.`

---

## Tabela-resumo

| ID | Enunciado curto | Marca |
|---|---|---|
| [R1.1](#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Use apenas palavras aprovadas e termos técnicos. | `[vale]` |
| [R1.2](#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor) | Use cada palavra apenas com o significado aprovado. | `[revisor]` |
| [R1.3](#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor) | Use cada palavra apenas na classe gramatical aprovada. | `[revisor]` |
| [R1.4](#r14-use-uma-palavra-para-cada-conceito-revisor) | Use uma palavra para cada conceito. | `[revisor]` |
| [R1.5](#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | Escreva os artigos e o substantivo de classe antes de literais. | `[revisor]` |
| [R1.6](#r16-use-a-crase-apenas-antes-de-palavra-feminina-com-artigo-e-antes-de-horas-revisor) | Use a crase apenas antes de palavra feminina com artigo e antes de horas. | `[revisor]` |
| [R1.7](#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | Use estrangeirismos apenas da lista de termos técnicos. Não use verbos com radical estrangeiro. | `[vale]` |
| [R1.8](#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) | Não use "o mesmo" como pronome. Use "este" e repita o substantivo se o referente for ambíguo. | `[vale]` |
| [R1.9](#r19-use-onde-apenas-para-lugar-vale) | Use "onde" apenas para lugar. | `[vale]` |
| [R1.10](#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor) | Não use a forma "para" do verbo PARAR se a frase também tiver a leitura de preposição. | `[revisor]` |
| [R2.1](#r21-use-no-máximo-3-substantivos-em-uma-cadeia-com-de-revisor) | Use no máximo 3 substantivos em uma cadeia com "de". | `[revisor]` |
| [R2.2](#r22-escreva-o-adjetivo-imediatamente-depois-do-substantivo-revisor) | Escreva o adjetivo imediatamente depois do substantivo. | `[revisor]` |
| [R2.3](#r23-não-use-a-ordem-do-inglês-em-substantivos-compostos-revisor) | Não use a ordem do inglês em substantivos compostos. | `[revisor]` |
| [R2.4](#r24-nomeie-um-conceito-longo-com-um-nome-curto-revisor) | Nomeie um conceito longo com um nome curto. | `[revisor]` |
| [R3.1](#r31-use-apenas-os-tempos-verbais-aprovados-vale) | Use apenas presente, pretérito perfeito, "vai" + infinitivo, imperativo, futuro do subjuntivo em condições e infinitivo. | `[vale]` |
| [R3.2](#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | Use o subjuntivo apenas em condições. Escolha a forma da condição pelo tipo de condição. | `[revisor]` |
| [R3.3](#r33-use-a-voz-ativa-revisor) | Use a voz ativa. Voz passiva apenas em texto descritivo, sem autor necessário. | `[revisor]` |
| [R3.4](#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale) | Não use a passiva sintética nem o "se" indeterminado. | `[vale]` |
| [R3.5](#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale) | Use o verbo, não um verbo-suporte com um substantivo. | `[vale]` |
| [R3.6](#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale) | Use o gerúndio apenas para uma ação em andamento. Sem gerundismo. | `[vale]` |
| [R3.7](#r37-não-use-pronomes-oblíquos-átonos-nem-mesóclise-vale) | Não use pronomes oblíquos átonos nem mesóclise. | `[vale]` |
| [R3.8](#r38-use-poder-e-dever-com-um-único-significado-revisor) | Use "poder" e "dever" com um único significado. | `[revisor]` |
| [R3.9](#r39-use-apenas-ser-estar-e-ficar-como-verbos-de-ligação-revisor) | Use apenas "ser", "estar" e "ficar" como verbos de ligação. | `[revisor]` |
| [R3.10](#r310-use-o-verbo-específico-não-um-verbo-geral-revisor) | Use o verbo específico, não um verbo geral. | `[revisor]` |
| [R4.1](#r41-escreva-uma-instrução-ou-uma-afirmação-por-frase-revisor) | Escreva uma instrução ou uma afirmação por frase. | `[revisor]` |
| [R4.2](#r42-escreva-frases-dentro-do-limite-de-palavras-vale) | Máximo de 20 palavras por frase de procedimento e 25 por frase descritiva. | `[vale]` |
| [R4.3](#r43-escreva-o-sujeito-antes-do-verbo-e-faça-a-concordância-vale) | Escreva o sujeito antes do verbo e faça a concordância. Sem "haver". | `[vale]` |
| [R4.4](#r44-escreva-o-sujeito-se-o-texto-tiver-mais-de-um-autor-de-ação-revisor) | Escreva o sujeito se o texto tiver mais de um autor de ação. | `[revisor]` |
| [R4.5](#r45-use-no-máximo-uma-negação-por-frase-revisor) | Use no máximo uma negação por frase. | `[revisor]` |
| [R4.6](#r46-use-no-máximo-uma-oração-subordinada-por-frase-revisor) | Use no máximo uma oração subordinada por frase. Sem "o qual" e "cujo". | `[revisor]` |
| [R5.1](#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) | Escreva os passos em uma lista numerada, na ordem de execução. Título no infinitivo. | `[revisor]` |
| [R5.2](#r52-use-o-imperativo-nos-passos-revisor) | Use o imperativo nos passos. Sem infinitivo e sem expressões indiretas. | `[revisor]` |
| [R5.3](#r53-escreva-uma-instrução-por-passo-revisor) | Escreva uma instrução por passo. | `[revisor]` |
| [R5.4](#r54-escreva-a-condição-e-o-local-antes-da-ação-revisor) | Escreva a condição e o local antes da ação. Sem "se necessário". | `[revisor]` |
| [R5.5](#r55-escreva-o-resultado-esperado-em-uma-frase-separada-revisor) | Escreva o resultado esperado em uma frase separada. | `[revisor]` |
| [R5.6](#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor) | Escreva os pré-requisitos antes do passo 1. | `[revisor]` |
| [R5.7](#r57-limite-o-número-de-passos-e-de-níveis-do-procedimento-revisor) | Máximo de 10 passos por procedimento e um nível de sublista. | `[revisor]` |
| [R5.8](#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | Escreva os comandos para digitar em blocos de código, com as opções longas. | `[revisor]` |
| [R5.9](#r59-termine-com-um-passo-de-verificação-revisor) | Termine com um passo de verificação. | `[revisor]` |
| [R5.10](#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | Escreva o responsável do procedimento e de cada etapa. | `[revisor]` |
| [R5.11](#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Escreva cada ponto de decisão com todas as saídas. | `[revisor]` |
| [R5.12](#r512-escreva-o-registro-que-a-etapa-gera-revisor) | Escreva o registro que a etapa gera. | `[revisor]` |
| [R5.13](#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) | Escreva um procedimento para reverter cada alteração do ambiente de produção. | `[revisor]` |
| [R6.1](#r61-comece-o-parágrafo-com-a-frase-principal-revisor) | Comece o parágrafo com a frase principal. | `[revisor]` |
| [R6.2](#r62-escreva-parágrafos-com-no-máximo-6-frases-e-um-assunto-revisor) | Escreva parágrafos com no máximo 6 frases e um assunto. | `[revisor]` |
| [R6.3](#r63-use-conectores-simples-revisor) | Use conectores simples. | `[revisor]` |
| [R6.4](#r64-escreva-valores-não-palavras-vagas-revisor) | Escreva valores, não palavras vagas. | `[revisor]` |
| [R6.5](#r65-use-listas-e-tabelas-para-itens-paralelos-revisor) | Use listas e tabelas para itens paralelos. | `[revisor]` |
| [R6.6](#r66-não-escreva-instruções-em-texto-descritivo-revisor) | Não escreva instruções em texto descritivo. | `[revisor]` |
| [R7.1](#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) | Use o nível de aviso da consequência mais grave, não da ação. | `[revisor]` |
| [R7.2](#r72-use-nota-apenas-para-informação-sem-risco-revisor) | Use NOTA apenas para informação sem risco. | `[revisor]` |
| [R7.3](#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor) | Escreva o aviso na ordem instrução, risco, consequência. | `[revisor]` |
| [R7.4](#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | Escreva o aviso antes da ação perigosa. | `[revisor]` |
| [R7.5](#r75-escreva-um-risco-por-aviso-revisor) | Escreva um risco por aviso. | `[revisor]` |
| [R7.6](#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor) | Escreva a consequência com o objeto e o efeito. | `[revisor]` |
| [R7.7](#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | Marque o aviso apenas com a palavra de sinalização. | `[revisor]` |
| [R7.8](#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) | Identifique o ambiente antes de um comando que altera ou exclui dados. | `[revisor]` |
| [R7.9](#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) | Não coloque segredos na linha de comando nem no texto. | `[revisor]` |
| [R8.1](#r81-termine-as-frases-com-ponto-final-revisor) | Termine as frases com ponto final. Sem ponto de exclamação. | `[revisor]` |
| [R8.2](#r82-use-a-vírgula-de-acordo-com-a-estrutura-da-frase-revisor) | Use a vírgula de acordo com a estrutura da frase. | `[revisor]` |
| [R8.3](#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor) | Não use ponto e vírgula, barra entre palavras nem inserções. | `[revisor]` |
| [R8.4](#r84-escreva-números-e-unidades-em-um-formato-fixo-vale) | Escreva números e unidades em um formato fixo. | `[vale]` |
| [R8.5](#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor) | Escreva datas no formato ISO 8601 e horas com o fuso horário. | `[revisor]` |
| [R8.6](#r86-use-maiúsculas-apenas-no-início-das-frases-e-em-nomes-próprios-revisor) | Use maiúsculas apenas no início das frases e em nomes próprios. | `[revisor]` |
| [R8.7](#r87-defina-as-siglas-na-primeira-ocorrência-revisor) | Defina as siglas na primeira ocorrência, exceto as siglas de uso geral. | `[revisor]` |
| [R8.8](#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) | Use cada formato tipográfico com um único significado. | `[revisor]` |
| [R8.9](#r89-escreva-espaços-reservados-em-um-formato-único-revisor) | Escreva espaços reservados em um formato único. | `[revisor]` |
| [R9.1](#r91-escreva-para-o-leitor-na-forma-você-revisor) | Escreva para o leitor na forma "você". | `[revisor]` |
| [R9.2](#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor) | Não use linguagem figurada, gíria nem personificação. | `[revisor]` |
| [R9.3](#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor) | Não use palavras vazias, de julgamento ou de cortesia. | `[revisor]` |
| [R9.4](#r94-escreva-referências-estáveis-revisor) | Escreva referências estáveis. "Acima" e "abaixo" apenas para o elemento ao lado. | `[revisor]` |
| [R9.5](#r95-escreva-listas-completas-revisor) | Escreva listas completas. Sem "etc.". | `[revisor]` |
| [R10.1](#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor) | Escreva o nome exato do elemento de interface em negrito. | `[revisor]` |
| [R10.2](#r102-use-o-verbo-do-tipo-de-elemento-revisor) | Use o verbo do tipo de elemento. | `[revisor]` |
| [R10.3](#r103-escreva-caminhos-de-menu-e-teclas-em-um-formato-fixo-revisor) | Escreva caminhos de menu e teclas em um formato fixo. | `[revisor]` |
| [R10.4](#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) | Escreva a mensagem de erro com o que aconteceu e o que fazer. | `[revisor]` |
| [R10.5](#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor) | Escreva mensagens de erro sem humor e sem culpa. | `[revisor]` |
| [R10.6](#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) | Escreva rótulos de botão e diálogos de confirmação com o verbo da ação. | `[revisor]` |
| [R10.7](#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor) | Escreva mensagens de andamento e de sucesso curtas. | `[revisor]` |
| [R10.8](#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor) | Escreva textos com variáveis que funcionam com qualquer valor. | `[revisor]` |
| [R10.9](#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor) | Escreva textos de validação, de acessibilidade, de link e de estado vazio com a ação. | `[revisor]` |
| [R10.10](#r1010-escreva-textos-de-desenvolvimento-com-um-formato-fixo-revisor) | Escreva textos de desenvolvimento com um formato fixo. | `[revisor]` |

Total: 82 regras. 12 regras com a marca `[vale]`. 70 regras com a marca `[revisor]`. O revisor verifica as 82 regras.

---

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · **02 Regras** · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

<!-- rodape -->
Feito com ❤️ em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Nenhum direito reservado.

# PTS-BR: Português Técnico Simplificado

<!-- nav -->
[Início](README.md) · **01 Introdução** · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

## Parte 1: Introdução

Versão 1.0.0, 2026-11-18

> **Aviso sobre o ASD-STE100**
>
> O PTS-BR usa a estrutura do ASD-STE100 ("Simplified Technical English") como modelo. O ASD-STE100 é uma especificação da ASD ("AeroSpace and Defence Industries Association of Europe"). O PTS-BR não é uma tradução oficial do ASD-STE100. A ASD não aprovou o PTS-BR. As regras e o dicionário do PTS-BR são textos originais, escritos para a gramática do português do Brasil. Nenhuma parte do PTS-BR copia o texto do ASD-STE100.

---

## 1. O que é o PTS-BR

O PTS-BR é uma linguagem controlada para documentação técnica em português do Brasil. Uma linguagem controlada limita o vocabulário e a gramática de uma língua natural. O objetivo do PTS-BR é um texto técnico com um único significado para todos os leitores.

O PTS-BR tem 3 componentes:

- As regras de escrita, em [`02-regras.md`](02-regras.md). As 82 regras são sobre palavras, frases, procedimentos, avisos, formatação, textos de interface e textos de desenvolvimento.
- O dicionário controlado, em [`03-dicionario.md`](03-dicionario.md). O dicionário lista as palavras do vocabulário geral. Cada palavra é aprovada ou não aprovada e tem uma classe gramatical e um significado. Cada palavra não aprovada tem uma alternativa aprovada.
- Os termos técnicos, em [`04-termos-tecnicos.md`](04-termos-tecnicos.md). Este arquivo define as categorias de nomes e de verbos técnicos e a política de estrangeirismos. Este arquivo também tem o glossário-base de TI e a tabela de siglas de uso geral.

O PTS-BR altera as palavras e a estrutura das frases do texto. O PTS-BR não altera o conteúdo técnico nem os requisitos do texto. O texto PTS-BR mantém cada prazo, cada valor e cada condição do texto original.

---

## 2. Escopo

### 2.1 Textos no escopo

Use o PTS-BR nestes tipos de texto de software, de processos e de TI:

| Tipo de texto | Exemplos |
|---|---|
| Manuais e guias | Guia de instalação, manual do administrador, guia do usuário |
| Procedimentos de operação | Runbooks, procedimentos de deploy, procedimentos de recuperação de desastre |
| Procedimentos de processo | Procedimento operacional padrão (POP), instrução de trabalho, fluxo de aprovação, procedimento de auditoria |
| Documentação de API | Descrição de endpoints, parâmetros, códigos de erro, exemplos de requisição e de resposta |
| Textos de interface | Mensagens de erro, diálogos de confirmação, rótulos de botão, textos de ajuda, mensagens de validação, textos de acessibilidade |
| Textos de desenvolvimento | Descrição de pull request, corpo da mensagem de commit, ajuda de CLI, mensagens de log de operação, documentação de API pública no código-fonte |
| Notas de versão | Alterações, defeitos corrigidos, problemas conhecidos |
| Instruções de segurança | Avisos, procedimentos com credenciais, regras de acesso a produção |

Os procedimentos de processo também seguem as regras [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) a [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor). Os procedimentos que alteram o ambiente de produção também seguem a regra [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor). Os textos de desenvolvimento também seguem a regra [R10.10](02-regras.md#r1010-escreva-textos-de-desenvolvimento-com-um-formato-fixo-revisor).

### 2.2 Textos fora do escopo

O PTS-BR não é para estes textos:

- Textos de marketing e textos de vendas.
- Textos jurídicos: contratos, termos de uso e políticas de privacidade.
- Textos acadêmicos e artigos de opinião.
- Código-fonte e comentários internos de código. O leitor de um comentário interno é o desenvolvedor do código, e o desenvolvedor altera o comentário com o código. O PTS-BR não é obrigatório nestes comentários. A documentação de uma API pública no código-fonte está no escopo (seção 2.1).
- O título da mensagem de commit. O título segue o padrão do repositório, por exemplo o padrão "Conventional Commits". Algumas ferramentas leem o título automaticamente.
- Conversa em chat e e-mail pessoal.

### 2.3 Conteúdo que o PTS-BR não altera

Em um texto no escopo, o PTS-BR não altera estes conteúdos:

- Literais: comandos, código, nomes de arquivo, variáveis, valores de configuração e códigos de erro.
- Nomes próprios de produtos, empresas e serviços.
- Rótulos de interface. O documento cita o rótulo exato, também se o rótulo não seguir o PTS-BR.
- Mensagens de outros sistemas, citadas sem alteração.
- Textos com uma redação fixa que uma lei ou um contrato define.

As regras de palavras e de frases não verificam o texto dentro destes conteúdos.

---

## 3. Público

| Público | Resultado do PTS-BR para este público |
|---|---|
| Redatores técnicos e desenvolvedores que escrevem documentação em português | Regras com um critério de verificação fixo e um vocabulário fechado. O redator não precisa decidir a forma de cada frase. |
| Responsáveis por processos e auditores | Procedimentos com um responsável, com todas as saídas de cada decisão e com o registro de cada etapa. |
| Leitores nativos sem prática de leitura técnica | Frases curtas, uma palavra para cada conceito e uma estrutura fixa. |
| Leitores não nativos com espanhol ou inglês como primeira língua | Um vocabulário pequeno, formas verbais regulares e nenhuma expressão idiomática. |
| Ferramentas: linter e tradução automática | Regras com padrões que uma ferramenta encontra e um dicionário em formato de tabela. |

---

## 4. Princípios

Os princípios explicam o objetivo das regras. Se uma regra não existir para uma situação de escrita, aplique o princípio mais próximo da situação.

### P1. Uma palavra, um significado, uma classe gramatical

Este é o princípio central do PTS-BR. Cada palavra aprovada tem um único significado e uma única classe gramatical. Por exemplo, o PTS-BR usa "executar" apenas com o significado "fazer um computador processar um comando, um script, um programa ou um deploy". O PTS-BR não usa "executar" com o significado "fazer uma tarefa".

O princípio tem 2 exceções, que [`03-dicionario.md`](03-dicionario.md) (regras D6 e D7) e a regra [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor) definem:

- "A" (artigo e preposição) e "que" (pronome relativo e conjunção) têm 2 classes aprovadas. O português não tem outra palavra para estas classes.
- Uma forma de um verbo aprovado é igual a uma palavra aprovada de outra classe: "a falha" e "o deploy falha". A estrutura da frase mostra a classe.

O futuro com "vai" + infinitivo não é uma exceção. Nesta forma, "ir" é um verbo auxiliar de tempo, e `IR (v)` tem um único significado ([`03-dicionario.md`](03-dicionario.md), regra D2). A forma "para" do verbo PARAR é igual à preposição "para". A regra [R1.10](02-regras.md#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor) resolve esta ambiguidade.

Regras: [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.2](02-regras.md#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor), [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor), [R1.10](02-regras.md#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor).

### P2. Um conceito, uma palavra

O P2 é o princípio P1 visto do conceito. Para cada conceito, o texto usa sempre a mesma palavra. O redator não substitui "pasta" por "diretório" em outra parte do texto. O leitor entende uma palavra diferente como um conceito diferente.

Regras: [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor), [R2.4](02-regras.md#r24-nomeie-um-conceito-longo-com-um-nome-curto-revisor).

### P3. Frases curtas, uma ideia por frase

Uma frase de procedimento tem no máximo 20 palavras. Uma frase descritiva tem no máximo 25 palavras. Um parágrafo tem no máximo 6 frases. Cada frase contém uma instrução ou uma afirmação.

Regras: [R4.1](02-regras.md#r41-escreva-uma-instrução-ou-uma-afirmação-por-frase-revisor), [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale), [R6.2](02-regras.md#r62-escreva-parágrafos-com-no-máximo-6-frases-e-um-assunto-revisor).

### P4. Voz ativa e sujeito explícito

O leitor precisa saber o autor de cada ação: o próprio leitor, o sistema, outro componente ou outro responsável. A voz ativa e o sujeito explícito mostram o autor da ação.

Regras: [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale), [R4.4](02-regras.md#r44-escreva-o-sujeito-se-o-texto-tiver-mais-de-um-autor-de-ação-revisor), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor).

### P5. Imperativo nas instruções

Uma instrução usa o imperativo da forma "você": "Remova", "Instale", "Clique". O imperativo mostra que a frase é uma ordem para o leitor.

Regras: [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor), [R5.3](02-regras.md#r53-escreva-uma-instrução-por-passo-revisor).

### P6. Ordem direta e estrutura fixa

O PTS-BR usa a ordem sujeito, verbo, complementos. A condição está antes da ação. Nos avisos, a instrução está antes do risco. Em um ponto de decisão, cada saída tem um destino. O leitor encontra cada tipo de informação no lugar esperado.

Regras: [R4.3](02-regras.md#r43-escreva-o-sujeito-antes-do-verbo-e-faça-a-concordância-vale), [R5.4](02-regras.md#r54-escreva-a-condição-e-o-local-antes-da-ação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor).

### P7. Informação exata

O texto usa números, unidades, nomes exatos e rótulos exatos. Uma palavra vaga como "rápido" tem um valor diferente para cada leitor.

Regras: [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale), [R10.1](02-regras.md#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor).

### P8. Segurança antes da ação

O leitor recebe o aviso antes da ação que causa o risco. O nível do aviso depende da consequência mais grave da ação, não da ação. Os níveis são para um dano sem recuperação, para uma indisponibilidade com recuperação conhecida e para um desempenho menor. Cada procedimento que altera o ambiente de produção tem um procedimento para reverter a alteração.

Regras: [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) e seção 7 de [`02-regras.md`](02-regras.md).

### P9. Regras com verificação

Um revisor pode verificar cada regra com um critério fixo. A marca de cada regra mostra o tipo de verificação:

- `[vale]`: o pacote de regras Vale do PTS-BR detecta o padrão principal da regra. O revisor confirma as ocorrências que a ferramenta não decide.
- `[revisor]`: apenas o revisor verifica a regra.

A ferramenta verifica uma parte das regras antes do revisor. A ferramenta não substitui o revisor.

### P10. Responsável e registro em cada etapa

Em um procedimento de processo, o leitor sabe o responsável de cada etapa, as saídas de cada decisão e o registro que cada etapa gera. Um auditor pode verificar cada etapa com estas informações.

Regras: [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor).

---

## 5. Decisões de base sobre a língua

A tabela mostra as decisões gramaticais do PTS-BR. As seções 5.1 a 5.5 explicam as decisões principais.

| Assunto | Decisão do PTS-BR | Regras |
|---|---|---|
| Forma de tratamento | "Você" implícito. Não use "tu", "o senhor", o pronome "nós" nem "o usuário deve". | [R9.1](02-regras.md#r91-escreva-para-o-leitor-na-forma-você-revisor) |
| Instruções | Imperativo da forma "você". Infinitivo apenas em títulos de procedimento e em rótulos de botão. | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor), [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) |
| Voz | Voz ativa. Voz passiva com "ser" apenas em texto descritivo, se o leitor não precisar saber o autor da ação. Passiva sintética proibida. | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale) |
| Tempos verbais | Presente, pretérito perfeito, "vai" + infinitivo, imperativo, futuro do subjuntivo em condições, infinitivo depois de verbo auxiliar ou de preposição e infinitivo flexionado depois de preposição. | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale) |
| Futuro do presente simples | Não aprovado. | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale) |
| Condições | "Se" ou "quando" + futuro do subjuntivo para uma instrução ou um fato futuro. "Quando" + presente do indicativo para um comportamento que o sistema tem sempre. "Se" + pretérito perfeito para um fato passado. "Se" + futuro do subjuntivo para a condição de uma regra, de um requisito ou de um critério. | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) |
| Gerúndio | Apenas "estar" + gerúndio e mensagens de andamento. Gerundismo proibido. | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor) |
| Verbos de ligação | "Ser", "estar" e "ficar". "Ficar" indica um estado novo depois de um evento. | [R3.9](02-regras.md#r39-use-apenas-ser-estar-e-ficar-como-verbos-de-ligação-revisor) |
| Pronomes átonos | Não aprovados. Mesóclise proibida. Exceção: o "se" de verbo pronominal, antes do verbo. | [R3.7](02-regras.md#r37-não-use-pronomes-oblíquos-átonos-nem-mesóclise-vale) |
| Referência a um item do texto | "Este" ou "esta" com o substantivo. Não use "esse", "isso", "ele" nem "o mesmo" como pronome. | [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) |
| Limites | 20 palavras por frase de procedimento. 25 palavras por frase descritiva. 6 frases por parágrafo. 3 substantivos por cadeia com "de". 10 passos por procedimento. | [R2.1](02-regras.md#r21-use-no-máximo-3-substantivos-em-uma-cadeia-com-de-revisor), [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale), [R5.7](02-regras.md#r57-limite-o-número-de-passos-e-de-níveis-do-procedimento-revisor), [R6.2](02-regras.md#r62-escreva-parágrafos-com-no-máximo-6-frases-e-um-assunto-revisor) |
| Estrangeirismos | Apenas substantivos da lista de [`04-termos-tecnicos.md`](04-termos-tecnicos.md). Nenhum verbo com radical estrangeiro. | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) |
| Números e unidades | Algarismos, vírgula como separador decimal, espaço como separador de milhar e símbolo da unidade depois do número ("10 min", "512 MB"). | [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale) |
| Datas e horas | Data no formato ISO 8601 (AAAA-MM-DD), formato de 24 h e fuso horário ("09:30 UTC-03:00"). | [R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor) |
| Siglas | Definição na primeira ocorrência, exceto as siglas do glossário-base e da tabela de siglas de uso geral de [`04-termos-tecnicos.md`](04-termos-tecnicos.md). | [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) |

### 5.1 Futuro do presente simples: não aprovado

**Decisão:** O PTS-BR não aprova o futuro do presente simples ("enviará", "fará"). Para o futuro, use "vai" + infinitivo ("vai enviar"). Nesta forma, "ir" é um verbo auxiliar de tempo, não o verbo `IR (v)`, que significa "mover para outro lugar" ([`03-dicionario.md`](03-dicionario.md), regra D2). O PTS-BR também não aprova "irá" + infinitivo nem o futuro do pretérito ("enviaria", "seria").

**Justificativa:**

- O princípio P2 pede uma forma para cada significado. 2 formas de futuro com o mesmo significado não cumprem este princípio.
- "Vai" + infinitivo é a forma de futuro mais comum no português do Brasil, na fala e na escrita.
- Na forma com "vai", o verbo principal está no infinitivo. O infinitivo é a forma que o dicionário registra.
- O leitor não precisa conhecer as formas irregulares do futuro simples ("fará", "dirá", "trará", "porá").
- A estrutura é igual à estrutura do espanhol "va a" + infinitivo e do inglês "going to". Os leitores não nativos do público conhecem esta estrutura.
- O futuro simples permite a mesóclise ("enviar-lhe-á"). O PTS-BR proíbe a mesóclise.
- O futuro do pretérito indica possibilidade ou cortesia. Uma instrução técnica não precisa de possibilidade nem de cortesia.

**Custo da decisão:** Para alguns redatores, "vai" + infinitivo é uma forma informal. No PTS-BR, a leitura simples tem prioridade sobre a forma mais formal. A forma com "vai" também adiciona 1 palavra à frase.

### 5.2 Subjuntivo e condições

**Decisão:** O PTS-BR aprova 3 formas de condição. Esta tabela mostra a forma de cada tipo de condição:

| Tipo de condição | Forma | Exemplo |
|---|---|---|
| Instrução ou fato futuro | "se" ou "quando" + futuro do subjuntivo | "Se o teste falhar, volte ao passo 2." |
| Comportamento que o sistema tem sempre, em texto descritivo | "quando" + presente do indicativo | "Quando a fila fica cheia, o serviço recusa mensagens novas." |
| Fato passado que o leitor verifica | "se" + pretérito perfeito | "Se o comando retornou o código 1, leia o log." |
| Condição de uma regra, de um requisito ou de um critério | "se" + futuro do subjuntivo | "Se o documento não declarar a versão, o resultado é Reprovado." |

Depois de "até" e de "antes de", use o infinitivo flexionado: "Aguarde até os pods ficarem no estado `Running`." O PTS-BR não aprova as outras formas do subjuntivo.

**Justificativa:**

- As 3 formas são corretas na norma do português. Uma condição sobre um fato também aceita o presente do indicativo. O PTS-BR escolhe uma forma para cada tipo de condição, e o leitor identifica o tipo de condição pela forma do verbo.
- O futuro do subjuntivo é a forma mais comum nas instruções em português.
- O infinitivo flexionado substitui "até que" e "antes que" + presente do subjuntivo com uma forma mais simples.
- As outras formas do subjuntivo indicam possibilidade, concessão, dúvida ou desejo. Um texto técnico não precisa destes significados.

**Formas não aprovadas e alternativas:**

| Não aprovado | Alternativa PTS-BR |
|---|---|
| "Caso o token expire" | "Se o token expirar" |
| "Para que o cache seja limpo, reinicie o serviço." | "Reinicie o serviço para limpar o cache." |
| "Embora o teste passe, ..." | 2 frases com "mas". |
| "Talvez o servidor não responda." | Um fato que o leitor pode verificar: "O servidor não respondeu em 30 s." |
| "Se o servidor fosse reiniciado" | "Se o servidor reiniciar" |
| "Aguarde até que o pod esteja pronto." | "Aguarde até o pod ficar no estado `Running`." |
| "Se o deploy tiver falhado" | "Se o deploy falhou" |

**Nota sobre o imperativo:** As formas do imperativo de "você" ("Instale", "Não remova") são iguais às formas do presente do subjuntivo. O PTS-BR aprova estas formas como imperativo. As regras do subjuntivo não proíbem estas formas.

**Custo da decisão:** Os verbos irregulares têm formas próprias no futuro do subjuntivo ("fizer", "tiver", "puder", "vier"). O PTS-BR aceita este custo, porque estas formas são comuns e o leitor nativo conhece todas as formas.

### 5.3 Pronomes átonos e mesóclise

**Decisão:** O PTS-BR não aprova os pronomes oblíquos átonos ("o", "a", "lhe", "-lo", "-la"). Repita o substantivo. O PTS-BR proíbe a mesóclise. Exceção: em verbos pronominais do dicionário ("conectar-se"), escreva o sujeito e depois o "se" antes do verbo: "O serviço se conecta ao banco."

**Justificativa:** A colocação dos pronomes átonos é diferente na norma gramatical e no uso do Brasil. O substantivo repetido resolve a dúvida e mostra ao leitor não nativo o referente do pronome. A próclise com sujeito explícito é a forma mais comum no português do Brasil, e as gramáticas brasileiras aceitam esta forma.

### 5.4 Estrangeirismos

**Decisão:** O PTS-BR aceita uma palavra estrangeira apenas se a palavra cumprir estes 4 critérios:

1. A palavra é o nome de um objeto ou de um conceito técnico de TI. A palavra não é o nome de uma ação ou de uma qualidade geral.
2. O português não tem um termo com o mesmo significado e com uso estável em TI.
3. A palavra é comum na documentação técnica em português e nas ferramentas do leitor.
4. [`04-termos-tecnicos.md`](04-termos-tecnicos.md) lista a palavra, com o gênero e a definição.

**Regras derivadas:**

- O PTS-BR aceita estrangeirismos apenas como substantivos e como nomes técnicos: "o commit", "o deploy", "o token", "o endpoint".
- O PTS-BR não aceita verbos com radical estrangeiro ("deployar", "commitar", "setar", "logar"). Para a ação, use um verbo aprovado com o substantivo técnico: "Crie um commit.", "Execute o deploy.", "Defina a variável.", "Entre no portal."
- O PTS-BR não aceita um estrangeirismo se o português tiver uma palavra com o mesmo significado e com uso estável. Exemplos: "feature" (use "funcionalidade"), "setup" (use "configuração"), "default" (use "padrão"), "request" (use "requisição").
- Escreva o estrangeirismo aprovado sem itálico e sem aspas, como uma palavra do texto. Um literal de código está sempre em formato de código.
- No plural, use a forma do inglês: "os commits", "os tokens", "os proxies".
- Use o gênero que [`04-termos-tecnicos.md`](04-termos-tecnicos.md) define para cada termo.

**Exemplo de decisão, "deploy":** O PTS-BR mantém "deploy" como substantivo técnico. O termo "implantação" não tem um uso estável em TI, e o leitor lê "implantação" como "implementação". Para a ação, use "executar o deploy". Não use "deployar" nem "fazer o deploy".

**Fonte da lista:** A lista completa dos estrangeirismos aprovados está em [`04-termos-tecnicos.md`](04-termos-tecnicos.md). Esta seção define os critérios. Se esta seção e a lista tiverem um conflito sobre um termo específico, a lista tem prioridade.

### 5.5 Limites

O PTS-BR usa os limites da tabela de decisões. Os limites são valores máximos, não metas. Uma frase de 8 palavras é melhor que uma frase de 20 palavras com o mesmo conteúdo. A regra [R4.2](02-regras.md#r42-escreva-frases-dentro-do-limite-de-palavras-vale) explica como contar as palavras.

---

## 6. Vocabulário geral controlado e termos técnicos

O PTS-BR tem um controle diferente para cada um destes 2 tipos de palavra.

### 6.1 Vocabulário geral controlado

O vocabulário geral contém as palavras comuns a todas as áreas. Exemplos: verbos de ação ("abrir", "remover", "verificar"), substantivos gerais ("erro", "valor", "passo"), adjetivos, advérbios, preposições e conjunções.

[`03-dicionario.md`](03-dicionario.md) controla o vocabulário geral. O dicionário é uma lista fechada. Se uma palavra geral não estiver no dicionário, a palavra não é aprovada. Cada entrada do dicionário tem estas informações:

- A decisão: aprovada ou não aprovada.
- A classe gramatical.
- O significado aprovado.
- Um exemplo em PTS-BR.
- Para uma palavra não aprovada, a alternativa aprovada.

Os arquivos [`tools/d1.txt`](https://github.com/dvwinck/pts-br/blob/main/tools/d1.txt), [`tools/d2.txt`](https://github.com/dvwinck/pts-br/blob/main/tools/d2.txt) e [`tools/d3.txt`](https://github.com/dvwinck/pts-br/blob/main/tools/d3.txt) são a fonte do dicionário. O script [`tools/build.py`](https://github.com/dvwinck/pts-br/blob/main/tools/build.py) gera [`03-dicionario.md`](03-dicionario.md) com estes arquivos.

### 6.2 Termos técnicos

Os termos técnicos são os nomes de objetos, de conceitos e de ações específicos de TI ou de um projeto. [`04-termos-tecnicos.md`](04-termos-tecnicos.md) define as categorias de termos técnicos. A lista abaixo mostra exemplos de categorias. O arquivo [`04-termos-tecnicos.md`](04-termos-tecnicos.md) é a fonte oficial.

- Nomes de produtos e componentes: "PostgreSQL", "o serviço de pagamentos".
- Conceitos de TI: "token", "endpoint", "commit", "cache", "cluster".
- Protocolos, formatos e padrões: "HTTP", "JSON", "OAuth 2.0".
- Elementos de interface: "botão", "campo", "caixa de seleção".
- Verbos técnicos: verbos de ação específicos de TI, como "compilar" e "criptografar".

O redator pode usar um termo técnico se o termo pertencer a uma categoria de [`04-termos-tecnicos.md`](04-termos-tecnicos.md). Cada projeto tem um glossário com os nomes do projeto: componentes, responsáveis, papéis de acesso, telas e ambientes. O glossário do projeto segue as mesmas regras: um termo, um significado.

[`04-termos-tecnicos.md`](04-termos-tecnicos.md) também tem a tabela de siglas de uso geral. Estas siglas não precisam de definição no texto (regra [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor)).

### 6.3 Como classificar uma palavra

Para cada palavra do texto, faça estas perguntas, nesta ordem:

1. A palavra é um literal, por exemplo um código, um rótulo de interface ou um nome de produto? Se for, mantenha a palavra sem alteração. Use o formato da regra [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor).
2. A palavra está em uma categoria de [`04-termos-tecnicos.md`](04-termos-tecnicos.md), por exemplo um objeto, um conceito ou uma ação de TI? Se estiver, use a palavra como termo técnico.
3. Nas outras situações, a palavra é vocabulário geral. Procure a palavra em [`03-dicionario.md`](03-dicionario.md). Use a palavra apenas se a palavra for aprovada.

Um termo técnico não autoriza uma palavra geral não aprovada. Por exemplo, "feature" não é um termo técnico aceito, porque o português tem "funcionalidade".

### 6.4 Comparação

| Característica | Vocabulário geral controlado | Termos técnicos |
|---|---|---|
| Fonte | [`03-dicionario.md`](03-dicionario.md) | [`04-termos-tecnicos.md`](04-termos-tecnicos.md) e glossário do projeto |
| Tipo de controle | Lista fechada de palavras | Categorias e lista de referência |
| Quem adiciona uma palavra | O processo da seção 7 de [`05-governanca.md`](05-governanca.md) | O projeto, dentro das categorias |
| Significado | Um significado por palavra, em todos os projetos | Um significado por termo, dentro do projeto |
| Classe gramatical | A classe que o dicionário define | Substantivos e verbos técnicos |
| Exemplo | "remover" (v): o item sai de um lugar | "o token", "criptografar" |

---

## 7. Estrutura da especificação

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Índice da especificação |
| [`01-introducao.md`](#) | Escopo, princípios, decisões de base e uso da especificação |
| [`02-regras.md`](02-regras.md) | Regras de escrita numeradas, com exemplos e tabela-resumo |
| [`03-dicionario.md`](03-dicionario.md) | Dicionário controlado do vocabulário geral |
| [`04-termos-tecnicos.md`](04-termos-tecnicos.md) | Categorias de termos técnicos, política de estrangeirismos, glossário-base de TI e siglas de uso geral |
| [`05-governanca.md`](05-governanca.md) | Adoção, verificação de conformidade, ferramentas, manutenção do dicionário e versões |
| [`06-exemplos.md`](06-exemplos.md) | Textos completos antes e depois da aplicação do PTS-BR |
| `tools/` | Fontes do dicionário, regras Vale do PTS-BR e scripts de verificação |

Se 2 arquivos tiverem um conflito, use esta ordem de prioridade:

1. Para o vocabulário, [`03-dicionario.md`](03-dicionario.md) tem prioridade. O vocabulário são as palavras aprovadas e os significados.
2. Para a gramática e a estrutura do texto, [`02-regras.md`](02-regras.md) tem prioridade.
3. Para um termo técnico ou uma sigla, [`04-termos-tecnicos.md`](04-termos-tecnicos.md) tem prioridade sobre esta introdução.

---

## 8. Como usar o PTS-BR

### 8.1 Escrever um texto em PTS-BR

1. Identifique o tipo de texto: procedimento de operação ou de processo, texto descritivo, aviso, texto de interface ou de desenvolvimento.
2. Leia as regras de [`02-regras.md`](02-regras.md) para este tipo de texto.

   Use as seções 1, 2, 3, 4, 8 e 9 em todos os tipos de texto.
3. Escreva o texto.
4. Verifique cada palavra geral em [`03-dicionario.md`](03-dicionario.md).
5. Verifique cada termo técnico e cada sigla em [`04-termos-tecnicos.md`](04-termos-tecnicos.md) e no glossário do projeto.
6. Execute a ferramenta de verificação do PTS-BR no texto ([`05-governanca.md`](05-governanca.md), [seção 6](05-governanca.md#6-ferramentas-de-verificação)).

   A ferramenta mostra o ID da regra de cada alerta.
7. Corrija cada alerta. Para um alerta que a ferramenta não decide, confirme a regra no texto de [`02-regras.md`](02-regras.md).
8. Se uma regra impedir uma informação necessária, escreva a justificativa no pedido de revisão. O revisor pede a exceção ao aprovador ([`05-governanca.md`](05-governanca.md), [seção 4.1](05-governanca.md#41-fluxo-de-revisão-de-um-documento-no-git)).
9. Envie o texto para revisão.

### 8.2 Revisar um texto em PTS-BR

- Aplique toda a lista de verificação do revisor ([`05-governanca.md`](05-governanca.md), [seção 4.2](05-governanca.md#42-lista-de-verificação-do-revisor)) em cada revisão. A ferramenta de verificação verifica apenas uma parte da lista antes do revisor. Um texto com 0 alertas da ferramenta também precisa da revisão completa.
- Escreva a severidade do desvio e o ID da regra em cada comentário. Exemplo: `[S2][R3.4] Passiva sintética.` As severidades S1, S2 e S3 estão em [`05-governanca.md`](05-governanca.md), [seção 4.3](05-governanca.md#43-níveis-de-severidade-do-desvio).
- Verifique os avisos de segurança (seção 7 de [`02-regras.md`](02-regras.md)) e os procedimentos de rollback (regra [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor)) em todas as revisões.
- Se o texto precisar de uma palavra ou de um termo novo, envie um PMD, um pedido para alterar o dicionário. Uma palavra nova não está no 03 nem no 04. O processo está em [`05-governanca.md`](05-governanca.md), [seção 7](05-governanca.md#7-manutenção-do-dicionário-e-das-regras).

### 8.3 Ferramentas

- A marca `[vale]` indica uma regra com uma regra Vale no pacote PTS-BR. A ferramenta detecta o padrão principal da regra. O revisor confirma as ocorrências que a ferramenta não decide.
- A marca `[revisor]` indica uma regra que apenas o revisor verifica.
- A ferramenta mostra o ID da regra, a linha e o texto de cada alerta.
- A ferramenta não verifica o texto dentro de literais, rótulos de interface e mensagens citadas.
- A ferramenta não altera avisos de segurança automaticamente. Uma pessoa revisa cada alteração em um aviso.

### 8.4 Se o dicionário não tiver uma palavra para a ideia

Escreva a ideia com palavras aprovadas, em uma frase a mais se for necessário. Não crie um sinônimo local. Se o problema acontecer com frequência, envie um PMD de acordo com [`05-governanca.md`](05-governanca.md), [seção 7](05-governanca.md#7-manutenção-do-dicionário-e-das-regras).

### 8.5 Prioridade entre regras

Se 2 regras tiverem um conflito, aplique esta ordem de prioridade:

1. Conteúdo técnico correto: o texto descreve o sistema real.
2. Segurança: as regras da seção 7 de [`02-regras.md`](02-regras.md).
3. As outras regras do PTS-BR.
4. O guia de estilo do projeto.

O registro de um desvio e a aprovação de uma exceção seguem [`05-governanca.md`](05-governanca.md), seções 4.3 e 4.4.

---

## 9. Definições

| Termo | Definição |
|---|---|
| Procedimento | Uma sequência numerada de passos que o leitor segue para obter um resultado. |
| Procedimento de processo | Um procedimento com 2 ou mais responsáveis, com pontos de decisão ou com registros, por exemplo um procedimento operacional padrão (POP). |
| Procedimento operacional padrão | Um procedimento de processo que a empresa aprova como o padrão para uma tarefa. A sigla é POP. |
| Passo | Um item de um procedimento. Um passo contém uma instrução. |
| Instrução | Uma frase no imperativo que diz uma ação ao leitor. |
| Comando | Um texto que o leitor digita em um terminal ou que um programa executa. Um comando é um literal. |
| Responsável | A pessoa ou a equipe que faz uma etapa de um processo. |
| Ponto de decisão | Um passo com 2 ou mais saídas. Cada saída tem uma condição e um destino. |
| Registro | Um texto ou um conjunto de dados que documenta uma ação, um resultado ou um evento. Exemplos: a aprovação em um chamado, a frase "Registro:" de um POP, uma entrada de log. Para a linha de uma tabela de banco de dados, use "linha" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md)). |
| Texto descritivo | Um texto que explica como um sistema funciona ou por que uma decisão existe. Um texto descritivo não contém instruções. |
| Aviso | Um bloco que informa o leitor sobre um risco antes da ação que causa o risco. |
| Palavra de sinalização | A palavra que inicia um aviso ou uma nota: PERIGO, ATENÇÃO, CUIDADO ou NOTA. |
| Literal | Um texto que o leitor copia ou que o sistema lê sem alteração: comando, código, nome de arquivo, variável, valor. |
| Rótulo | O texto de um elemento de interface: botão, campo, menu, guia. |
| Espaço reservado | Um texto em um comando ou em um exemplo que o leitor substitui por um valor real. |
| Cadeia nominal | Uma sequência de substantivos ligados pela preposição "de" ou pelas contrações "do", "da", "dos" e "das". |
| Termo técnico | Um substantivo ou um verbo de uma categoria de [`04-termos-tecnicos.md`](04-termos-tecnicos.md). |
| Linter | Uma ferramenta que verifica um texto automaticamente e mostra os alertas das regras. O PTS-BR usa o Vale. |
| Texto normativo | O texto das regras, dos princípios, das definições e das justificativas desta especificação, sem os exemplos "Não aprovado". |

---

## 10. Como ler as regras

Cada regra de [`02-regras.md`](02-regras.md) tem esta estrutura:

- Um ID no formato "R" + número da seção + número da regra. Exemplo: [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale) é a regra 4 da seção 3.
- Um título curto e a marca de verificação: `[vale]` ou `[revisor]` (seção 8.3).
- **Enunciado:** a regra completa, em frases que um revisor pode verificar.
- **Justificativa:** por que a regra existe, em 1 ou 2 frases.
- **Verificação:** o que o revisor ou a ferramenta verifica.
- Pelo menos 2 exemplos: um exemplo **Não aprovado** e um exemplo **PTS-BR**.
- Em algumas regras, um exemplo **Aprovado** mostra um uso aprovado. Este exemplo mostra ao revisor que o uso não é uma violação.

Cada exemplo "Não aprovado" mostra a violação de uma regra. Se um exemplo "Não aprovado" também tiver uma violação de outra regra, esta violação não é o assunto do exemplo.

Nenhuma versão altera o número de uma regra. Uma regra nova recebe o próximo número da seção.

---

## 11. Formatos desta especificação

Esta especificação usa os formatos da regra [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) e mais 2 formatos:

- O negrito também marca os rótulos da estrutura das regras: **Enunciado**, **Justificativa**, **Verificação**, **Não aprovado**, **PTS-BR** e **Aprovado**.
- As aspas também marcam uma palavra que o texto mostra como exemplo: a palavra "executar".

### 11.1 Autoconformidade

O texto normativo desta especificação segue o PTS-BR. O texto normativo tem 3 exceções:

- Os exemplos "Não aprovado".
- Os blocos de código.
- A menção metalinguística: uma palavra entre aspas ou em formato de código, quando o texto fala da palavra.

No texto normativo, uma palavra está aprovada se for de uma destas listas ([`03-dicionario.md`](03-dicionario.md), regra D9):

1. Uma forma flexionada de uma entrada aprovada de [`03-dicionario.md`](03-dicionario.md).
2. Um nome técnico, um termo do glossário-base ou uma sigla de [`04-termos-tecnicos.md`](04-termos-tecnicos.md).
3. Uma palavra da tabela da seção 11.2 ou um termo de linguagem de [`04-termos-tecnicos.md`](04-termos-tecnicos.md) ([NT-25](04-termos-tecnicos.md#nt-25-termos-de-linguagem-e-de-redação)).
4. Um artigo, uma preposição, uma contração ou uma conjunção aprovados em [`03-dicionario.md`](03-dicionario.md).

Os termos da tabela da seção 9 e da tabela da seção 1 de [`05-governanca.md`](05-governanca.md) também estão aprovados no texto da especificação. Estas tabelas são o glossário do projeto desta especificação.

Antes de cada versão, o mantenedor executa a ferramenta `check_spec.py --spec --lista-branca` ([`05-governanca.md`](05-governanca.md), [seção 8](05-governanca.md#8-versões-da-especificação)). A ferramenta mostra cada palavra do texto normativo que não está nas 4 listas e a porcentagem destas palavras.

### 11.2 Vocabulário de metalinguagem

Para descrever a língua, os tipos de texto e o processo de escrita, a especificação usa as palavras desta tabela. A especificação também usa os termos de linguagem de [`04-termos-tecnicos.md`](04-termos-tecnicos.md) ([NT-25](04-termos-tecnicos.md#nt-25-termos-de-linguagem-e-de-redação)). Estas palavras estão aprovadas apenas em um texto sobre a escrita. Exemplos: esta especificação, um treinamento do PTS-BR, um guia de estilo e um comentário de revisão. Os documentos dos projetos não usam estas palavras como vocabulário geral. Uma palavra desta tabela tem um único significado: o significado de metalinguagem. A tabela não tem as palavras de metalinguagem que são entradas de [`03-dicionario.md`](03-dicionario.md). Use estas palavras apenas com o significado do dicionário. Estas palavras são: AMBÍGUO, CONTRATO, DÚVIDA, ESCOPO, ESCRITA, EXCEÇÃO, EXEMPLO, HIPÓTESE, JUSTIFICATIVA, OBRIGAÇÃO, REGRA, SEÇÃO e VERIFICAÇÃO.

| Grupo | Palavras |
|---|---|
| Classes e partes da frase | palavra, frase, oração, oração subordinada, oração relativa, parágrafo, verbo, substantivo, adjetivo, advérbio, pronome, pronome átono |
| Classes e partes da frase | pronome reflexivo, artigo, preposição, conjunção, conector, interjeição, contração, sujeito, sujeito explícito, sujeito implícito, complemento, modificador, construção |
| Classes e partes da frase | cadeia, composto, descritivo, gramatical, feminino, masculino, impessoal, indeterminado, irregular, pronome oblíquo átono |
| Classes e partes da frase | concordância, concordância negativa, ordem direta, inversão, colocação, próclise, ênclise, mesóclise, classe, classe gramatical |
| Formas verbais | infinitivo, infinitivo flexionado, imperativo, indicativo, subjuntivo, particípio, gerúndio, gerundismo, pretérito, pretérito imperfeito, pretérito mais-que-perfeito, imperfeito, futuro do presente |
| Formas verbais | futuro do pretérito, futuro do subjuntivo, passiva sintética, "se" indeterminado, verbo de ligação, verbo pronominal, verbo impessoal, verbo regular |
| Formas verbais | tempo verbal, forma verbal, voz, voz ativa, voz passiva |
| Formas verbais | verbo irregular, nominalização, forma de tratamento, singular, plural, gênero |
| Sinais e formatos | sigla, crase, vírgula, hífen, travessão, parênteses, colchetes, apóstrofo, reticências, ponto de exclamação, ponto de interrogação, formatação, formato tipográfico |
| Sinais e formatos | pontuação, barra, separador, separador decimal, separador de milhar |
| Sinais e formatos | ênfase, inserção, bloco de citação, lista numerada, sublista, numeração, maiúsculo, minúsculo, por extenso, introdução, tabela-resumo |
| Significado | significado, sinônimo, referente, ambiguidade, linguagem controlada, língua natural, linguagem figurada, expressão, expressão idiomática, metáfora, personificação, regionalismo, afirmação |
| Significado | afirmativo, negação, dupla negação, negativo, concessão, desejo, cortesia, humor, julgamento, emoção, recomendação, possibilidade, probabilidade, previsão |
| Significado | figurado |
| Significado | incerteza, forma informal, fala, paralelo, culpa, expressão indireta |
| Tipos de texto | mensagem de andamento, mensagem de sucesso, mensagem de validação, diálogo de confirmação, texto alternativo, texto de acessibilidade |
| Tipos de texto | texto de validação, diálogo, termo de linguagem |
| Tipos de texto | rótulo de acessibilidade, texto de link, estado vazio, texto de marketing, texto de vendas, texto jurídico |
| Tipos de texto | termos de uso, política de privacidade, texto acadêmico, artigo de opinião, conversa em chat, e-mail pessoal |
| Pessoas | leitor, leitor não nativo, redator, revisor, aprovador, mantenedor, auditor, tradutor, autor da ação |
| Texto da especificação | enunciado, marca, texto normativo, autoconformidade, metalinguagem, metalinguística, estrangeirismo, violação, desvio, severidade |

---

## 12. Limites do PTS-BR

- O PTS-BR não verifica se o conteúdo técnico do texto está correto. O texto também precisa de uma revisão técnica.
- A versão 1.0.0 não tem um teste com leitores reais. Os testes com leitores do público estão no processo de adoção ([`05-governanca.md`](05-governanca.md), [seção 3](05-governanca.md#3-adoção-do-pts-br-em-fases)).
- O vocabulário de [`03-dicionario.md`](03-dicionario.md) é menor que o vocabulário do ASD-STE100. Os PMD aumentam o dicionário a cada versão.
- O PTS-BR não é uma norma da Associação Brasileira de Normas Técnicas (ABNT) nem de outra organização de normas.
- O PTS-BR usa a norma do português do Brasil. O PTS-BR não é para o português de Portugal.
- O PTS-BR não substitui o guia de estilo de cada projeto. O guia do projeto tem as regras para os assuntos que o PTS-BR não tem.

---

<!-- nav -->
[Início](README.md) · **01 Introdução** · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

<!-- rodape -->
Feito com ❤️ em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Nenhum direito reservado.

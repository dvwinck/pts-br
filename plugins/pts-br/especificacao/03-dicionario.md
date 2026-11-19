# 03 — Dicionário controlado

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · **03 Dicionário** · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

PTS-BR — Português Técnico Simplificado, versão 1.0.0, 2026-11-18.
A estrutura do PTS-BR segue a estrutura do ASD-STE100. O PTS-BR não é uma tradução oficial do ASD-STE100, e a ASD não aprovou o PTS-BR.

Este arquivo controla o **vocabulário geral** do PTS-BR. Os nomes técnicos e os verbos técnicos estão em `04-termos-tecnicos.md`.

Conteúdo: 723 palavras aprovadas, 362 palavras não aprovadas com alternativa e 0 palavras obsoletas.

## Sumário

1. [Como ler uma entrada](#1-como-ler-uma-entrada)
2. [Regras de uso do dicionário](#2-regras-de-uso-do-dicionário)
3. [Fronteiras de significado](#3-fronteiras-de-significado)
4. [Verbos-suporte e locuções](#4-verbos-suporte-e-locuções)
5. [Número de entradas](#5-número-de-entradas)
6. Dicionário: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [Z](#z)

---

## 1. Como ler uma entrada

Cada linha das tabelas é uma entrada do dicionário. As entradas estão em ordem alfabética, sem os acentos.

| Coluna | Palavra aprovada | Palavra não aprovada | Palavra obsoleta |
|---|---|---|---|
| Palavra (classe) | A palavra em MAIÚSCULAS e a classe gramatical. Exemplo: `REMOVER (v)`. | A palavra em minúsculas e a classe gramatical. Exemplo: `realizar (v)`. | A palavra em MAIÚSCULAS e a classe gramatical. |
| Decisão | "Aprovada". | "Não aprovada". | "Obsoleta". |
| Significado aprovado / Alternativa | O único significado aprovado. | "Use:" e a alternativa aprovada em MAIÚSCULAS. Se a alternativa for uma frase nova, a coluna começa com "Reescreva:". | "Use:", a palavra aprovada que substitui a palavra obsoleta e a versão MAJOR que exclui a palavra. |
| Exemplo PTS-BR | Uma frase em PTS-BR com o significado aprovado. | A frase da coluna "Não aprovado", escrita de novo em PTS-BR. | A frase da coluna "Não aprovado", escrita de novo com a palavra que substitui a palavra obsoleta. |
| Não aprovado | Um uso da palavra fora do significado aprovado, com a forma correta entre parênteses. Um travessão (—) indica que a entrada não tem exemplo de uso incorreto. | A frase com a palavra não aprovada. | A frase com a palavra obsoleta. |

Na coluna "Significado aprovado / Alternativa", o sinal ";" separa 2 alternativas: "Use: MANUAL (adj); MANUALMENTE (adv)". Neste lugar, o sinal ";" é um separador de dados, não um sinal de pontuação de uma frase (02-regras.md, R8.3).

**Palavra obsoleta.** Uma palavra obsoleta é uma palavra aprovada que a próxima versão MAJOR vai excluir (05-governanca.md, seção 8.1). Um texto com uma palavra obsoleta continua em conformidade até esta versão MAJOR. Em um texto novo ou em um texto que você altera, use a palavra que substitui a palavra obsoleta. A versão MINOR que marca a palavra como obsoleta altera a decisão da entrada de "Aprovada" para "Obsoleta". A versão MAJOR remove a entrada ou altera a decisão para "Não aprovada". Na fonte do dicionário (`tools/d*.txt`), a entrada obsoleta tem o estado `O` (05-governanca.md, seção 7).

### 1.1 Classes gramaticais

| Código | Classe | Nota |
|---|---|---|
| `v` | verbo | A entrada é o infinitivo. O exemplo usa o imperativo (procedimento) ou o presente (descrição). |
| `s` | substantivo | A entrada está no singular, exceto quando o uso normal é no plural. |
| `adj` | adjetivo | A entrada está no masculino singular. |
| `adv` | advérbio | Contém também as locuções adverbiais aprovadas, por exemplo `DE NOVO` e `POR EXEMPLO`. |
| `prep` | preposição | Contém também as locuções prepositivas aprovadas, por exemplo `ANTES DE` e `POR CAUSA DE`. |
| `conj` | conjunção | — |
| `pron` | pronome | Contém também os pronomes indefinidos e os pronomes demonstrativos. |
| `art` | artigo | — |
| `num` | numeral | Para quantidades, use algarismos (02-regras.md, R8.4). |
| `loc` | locução | Apenas em palavras não aprovadas: um grupo de palavras que o PTS-BR não aprova como unidade. |
| `abrev` | abreviatura | Apenas em palavras não aprovadas. |

---

## 2. Regras de uso do dicionário

**D1. Um significado, uma classe.** Use a palavra aprovada apenas com a classe e com o significado da entrada. Uma palavra aprovada com outro significado é uma palavra não aprovada.

> Não aprovado: Atualize a equipe sobre o incidente.
> PTS-BR: Informe a equipe sobre o incidente.

**D2. Formas flexionadas.** Você pode usar o plural, o feminino e as formas verbais dos tempos aprovados (01-introducao.md, seção 5). As contrações de uma preposição aprovada com um artigo aprovado também são aprovadas: "do", "na", "pelo", "à", "num".

O futuro com "vai" + infinitivo (02-regras.md, R3.1) é uma forma verbal, como as terminações dos tempos aprovados. Nesta forma, "ir" é um verbo auxiliar de tempo: "ir" está no presente ("vai", "vão") e o verbo principal está no infinitivo. Esta forma não é um segundo significado de `IR (v)`. `IR (v)` tem apenas 1 significado: mover para outro lugar. O leitor separa as 2 formas pela estrutura: "vai" + infinitivo é futuro, "ir" + "para" + lugar indica um destino.

> PTS-BR: O sistema vai enviar um e-mail quando o build terminar.

**D3. Particípio.** Você pode usar o particípio de um verbo aprovado como adjetivo, com o significado do verbo: "o pacote instalado", "a porta bloqueada", "o arquivo excluído". O particípio de um verbo não aprovado não é aprovado, exceto se o particípio tiver uma entrada própria como adjetivo: `ESPERADO (adj)`. Não use um particípio como preposição ("Dado o volume..."). A regra R1.3 de `02-regras.md` aplica esta regra.

**D4. Palavras derivadas.** Uma palavra derivada de uma palavra aprovada não é aprovada de forma automática. Use a palavra derivada apenas se a palavra derivada tiver uma entrada própria.

> `EXCLUSÃO (s)` tem entrada. Você pode usar "a exclusão do projeto".
> "reinicialização" não tem entrada. Escreva "Reinicie o servidor", não "Faça a reinicialização do servidor".

**D5. Palavra não aprovada.** Use a alternativa da entrada. Se a alternativa começar com "Reescreva:", escreva uma frase nova: remova a palavra, divida a frase em 2 frases ou escreva o sujeito real.

**D6. Homógrafos.** Um homógrafo é uma forma escrita que é igual em 2 palavras de classes diferentes. O PTS-BR aprova 2 tipos de homógrafo:

1. **Entradas com 2 classes.** 2 palavras têm 2 entradas aprovadas, porque o português não tem outra palavra para estas classes. As entradas são `A (art)` e `A (prep)`, e `QUE (pron)` e `QUE (conj)`. Sem estas palavras, o texto não é gramatical. As palavras ao lado mostram a classe: o artigo "a" está antes de um substantivo feminino, e o "que" pronome tem um substantivo antes. O "se" de um verbo pronominal aprovado ("o serviço se conecta") é parte da forma do verbo (02-regras.md, R3.7), não outra classe de `SE (conj)`.
2. **Forma de um verbo igual a outra palavra aprovada.** Algumas formas de verbos aprovados são iguais a uma palavra aprovada de outra classe. Este tipo de homógrafo é aprovado. A estrutura da frase mostra a classe. Exemplos:
   - "a falha" (FALHA) e "o deploy falha" (FALHAR).
   - "o teste" (TESTE) e "Teste a restauração" (TESTAR).
   - "o limite" (LIMITE) e "Limite o número de conexões" (LIMITAR).
   - "entre 1 e 100" (ENTRE) e "Entre no portal" (ENTRAR).
   - "a conta" (nome técnico) e "o script conta as linhas" (CONTAR, regra D11).

Algumas formas de verbos não aprovados também são iguais a uma palavra aprovada. A palavra aprovada continua aprovada, apenas com a sua classe e com o seu significado. Exemplos: "a busca" (nome técnico, NT-05) e "Busque o termo no log" ("buscar", não aprovada). "a seta" (nome técnico, NT-06) e "Sete a variável" ("setar", não aprovada). "a roda do mouse" (nome técnico, NT-06) e "Rode os testes" ("rodar", não aprovada).

A estrutura da frase não mostra a classe apenas em 1 situação: a forma "para" de PARAR e a preposição PARA (ver abaixo e `02-regras.md`, R1.10). `01-introducao.md` (princípio P1) e `02-regras.md` (regra R1.3) aplicam esta regra. Os pronomes oblíquos "o", "a" e "lhe" não são aprovados (01-introducao.md, seção 5.3).

**"Para", forma de PARAR.** A forma "para" de `PARAR (v)` (3ª pessoa do singular) é igual à preposição `PARA (prep)`. Não escreva a forma "para" de PARAR se a frase também tiver uma leitura com a preposição. Escreva o sujeito no plural, use "não funciona" ou escreva outra estrutura (02-regras.md, Seção 1).

> Não aprovado: O reinício para todos os pods.
> PTS-BR: O comando reinicia todos os pods. Os pods não respondem por 5 min.

**D7. Palavras gerais que também são nomes técnicos.** `ENTRADA (s)`, `EXCEÇÃO (s)`, `FORMA (s)`, `LINHA (s)`, `PROCESSO (s)` e `TABELA (s)` têm um significado geral neste dicionário e um significado técnico em `04-termos-tecnicos.md`. Use o significado técnico apenas em um texto sobre a categoria técnica. Escreva o tipo ou o literal com o nome técnico: "a exceção `TimeoutError`", "o processo `nginx`", "a tabela `pedidos` do banco", "a linha 42 da tabela `clientes`", "a entrada do dicionário", "a forma flexionada". `FORMA (s)` tem o significado geral "modo" ("de forma automática"). O significado técnico de "forma" é a forma escrita de uma palavra (NT-25), apenas em um texto sobre a escrita: "a forma 'para' de PARAR". Para o texto que documenta uma ação, um resultado ou um evento, use `REGISTRO (s)`, não "linha" nem "evidência". "Função" é apenas um nome técnico (função de código, `04-termos-tecnicos.md`, NT-03). Para o objetivo de um componente, use `OBJETIVO (s)`. Para um conjunto de permissões, use o nome técnico "papel de acesso".

**D8. Palavras de sinalização.** `PERIGO`, `ATENÇÃO`, `CUIDADO` e `NOTA` são aprovadas apenas como palavras de sinalização. A seção 7 de `02-regras.md` define o nível de risco de cada uma. Escolha o nível pela consequência, não pela ação. Para classificar uma consequência, responda às 3 perguntas da regra R7.1. A tabela abaixo tem o mesmo texto da tabela de R7.1:

| Palavra de sinalização | Consequência | Exemplos de TI |
|---|---|---|
| **PERIGO** | Dano sem recuperação. Perda de dados sem cópia no backup, também dentro do RPO. Dados expostos a pessoas sem permissão. Credencial exposta. Risco para pessoas. | Excluir o banco `pedidos` de produção: os pedidos gravados depois do último backup não têm recuperação. Publicar uma chave privada em um repositório: a credencial fica exposta. Desativar a verificação TLS, a MFA ou o log de auditoria: os dados ficam expostos a pessoas sem permissão. Atribuir o papel de acesso de administrador a uma conta de serviço: a conta pode ler e alterar os dados de todos os clientes. Configurar um bucket com acesso público: os arquivos ficam expostos a qualquer pessoa. Permitir o acesso da internet a uma porta com a origem `0.0.0.0/0`: o serviço fica exposto a qualquer pessoa. Excluir uma chave de criptografia: os dados criptografados com esta chave não têm recuperação. |
| **ATENÇÃO** | Indisponibilidade parcial ou total com recuperação conhecida. Exclusão de dados com cópia completa no backup. Custo não planejado maior que o limite da equipe. | Reiniciar um serviço de produção: o serviço fica indisponível por 5 min e volta automaticamente. Excluir os índices do Elasticsearch: os clientes não podem procurar produtos até a equipe indexar os dados de novo. Alterar o endereço IP de um nome DNS: até o fim do TTL de 1 h, os clientes com o cache antigo recebem erros. Excluir a tabela `eventos_2025`, que nenhum processo altera depois do backup: a equipe restaura a tabela com o backup. Aumentar um cluster para 20 nós: o custo da conta aumenta em R$ 15 000 por mês. O limite da equipe é R$ 1 000 por mês. |
| **CUIDADO** | Desempenho menor sem perda de funcionalidade. Retrabalho. Dano menor, por exemplo um custo não planejado menor que o limite da equipe. | Reiniciar os pods de um serviço um de cada vez: por 2 min, a API responde em até 2 s, em vez de 200 ms. Limpar o cache da API: por 15 min, a API responde em até 2 s, em vez de 200 ms. Fechar o editor sem salvar: o leitor escreve as alterações de novo. |
| **NOTA** | Nenhum risco. Uma informação que ajuda o leitor no passo (regra R7.2). | Um comportamento esperado, uma referência a outro documento. |

A mesma consequência tem sempre o mesmo nível. Os exemplos das entradas PERIGO, ATENÇÃO e CUIDADO seguem esta tabela.

**D9. Palavra ausente.** Uma palavra de um texto em PTS-BR é aprovada apenas se for 1 destes itens:

1. Uma forma flexionada de uma entrada aprovada deste dicionário (D2, D3).
2. Um nome técnico, um termo do glossário-base, uma sigla ou um verbo técnico de `04-termos-tecnicos.md`.
3. Uma palavra da lista de metalinguagem de `01-introducao.md`, seção 11.2, apenas em um texto sobre a escrita.
4. Um literal (código, rótulo, mensagem, nome de produto), com o formato da regra R8.8.

Se uma palavra geral não estiver neste dicionário, a palavra não é aprovada. Procure primeiro uma palavra aprovada com o mesmo significado. Se nenhuma palavra tiver o significado correto, envie um PMD (05-governanca.md, seção 7). O modo `--lista-branca` do script `check_spec.py` verifica esta regra (05-governanca.md, seção 6).

**D10. Uso pelo linter.** O script `gerar_regras_dicionario.py` (05-governanca.md, seção 6) lê as entradas não aprovadas e as entradas obsoletas deste arquivo. Não altere a ordem nem o nome das colunas sem atualizar o script.

**D11. Nomes técnicos com a forma de outra palavra.** O pronome "nós" não é aprovado (02-regras.md, R9.1). "Nós", plural do nome técnico "nó" (04-termos-tecnicos.md, NT-12), é aprovado. Escreva sempre um artigo, uma contração ou um número antes deste plural: "os nós", "dos nós", "3 nós". O pronome não tem estas palavras antes. O nome técnico "conta" (04-termos-tecnicos.md, NT-16) tem a mesma forma do verbo `CONTAR (v)` ("O script conta as linhas"). Escreva sempre um artigo, uma contração ou um pronome antes do nome técnico: "a conta", "da conta", "sua conta". O linter usa estas diferenças.

> Não aprovado: Nós reiniciamos os nós do cluster.
> PTS-BR: A equipe de plataforma reiniciou os nós do cluster.

---

## 3. Fronteiras de significado

O português técnico tem grupos de palavras com significados semelhantes. O PTS-BR aprova 1 palavra para cada significado e define a fronteira de significado entre as palavras do grupo. Use esta seção quando você tiver dúvida entre 2 palavras aprovadas.

### 3.1 Remover, excluir e voltar

| Palavra | Use quando | Exemplo PTS-BR |
|---|---|---|
| REMOVER | O item sai de um lugar, de um grupo ou de um sistema. REMOVER não diz que o item não existe mais. | Remova o usuário do grupo `admin`. |
| EXCLUIR | O item não existe mais. Sem backup, você não pode recuperar o item. | Exclua o bucket de teste. |
| LIMPAR | Você remove o conteúdo, mas o item que contém o conteúdo continua a existir. | Limpe o cache. Limpe o campo **Nome**. |
| DESCARTAR | Você não aplica alterações que ainda não salvou. | Descarte as alterações locais. |
| DESFAZER | Você cancela o efeito da última ação. | Desfaça a última alteração. |
| RESTAURAR | Você volta um sistema ou dados a um estado anterior com uma cópia. | Restaure o banco com o backup de 2026-11-17. |
| RECUPERAR | Você obtém de novo um item perdido ou excluído. | Recupere o arquivo da lixeira. |

Não aprovadas neste grupo: "apagar", "deletar", "eliminar", "retirar", "tirar", "suprimir", "zerar".

### 3.2 Verificar e analisar

| Palavra | Use quando | Exemplo PTS-BR |
|---|---|---|
| VERIFICAR | O resultado é "sim" ou "não": uma condição é verdadeira ou um valor está correto. | Verifique se a porta 443 está aberta. |
| ANALISAR | Você precisa entender o conteúdo ou a causa de algo. | Analise o log para encontrar a causa da falha. |
| COMPARAR | Você procura as diferenças entre 2 ou mais itens. | Compare os 2 arquivos de configuração. |
| TESTAR | Você usa o item em condições controladas para saber se o item funciona. | Teste a restauração do backup. |
| REVISAR | Você lê um texto ou um código para encontrar e corrigir erros. | Revise o código antes do merge. |
| MONITORAR | Você vê os dados de um sistema durante um período. | Monitore o consumo de CPU por 10 min. |
| AVALIAR | Você decide o valor, a qualidade ou o efeito de algo com critérios. | Avalie o impacto da alteração. |

Não aprovadas neste grupo: "checar", "conferir", "averiguar", "certificar-se", "assegurar", "garantir", "constatar", "examinar", "inspecionar", "acompanhar", "observar".

### 3.3 Funcionar e parar

| Palavra | Use quando | Exemplo PTS-BR |
|---|---|---|
| LIGAR / DESLIGAR | Você liga ou desliga a energia de um equipamento físico. | Desligue o servidor antes de substituir o disco. |
| INICIAR / PARAR | Um agente faz um processo, um serviço ou um programa começar a funcionar ou parar. | Inicie o serviço `nginx`. Pare o worker. |
| REINICIAR | Você para e inicia de novo. | Reinicie o servidor de aplicação. |
| ATIVAR / DESATIVAR | Uma funcionalidade ou uma opção começa ou para de funcionar e continua neste estado. | Ative a MFA. |
| COMEÇAR / TERMINAR | Um evento acontece pela primeira vez ou chega ao fim. Não indica quem faz a ação. | A janela de deploy começa às 22:00 UTC-03:00. |
| ABRIR / FECHAR | Um arquivo, uma janela ou uma conexão fica disponível ou não fica mais disponível. | Feche a conexão depois da consulta. |
| PAUSAR | Você para a operação por um tempo e pode continuar depois. | Pause a sincronização. |
| CANCELAR | Você para a operação antes do fim e não aplica o resultado. | Cancele a cópia. |

Não aprovadas neste grupo: "acionar", "habilitar", "desabilitar", "startar", "subir", "levantar", "derrubar", "matar", "cessar", "interromper", "encerrar", "finalizar", "concluir", "completar", "abortar", "resetar".

### 3.4 Alterar

| Palavra | Use quando | Exemplo PTS-BR |
|---|---|---|
| ALTERAR | Você dá outro conteúdo, outra estrutura ou outro valor a algo. É o verbo geral. | Altere a senha do usuário `root`. |
| AJUSTAR | Você altera um valor em uma quantidade pequena, para obter o resultado correto. | Ajuste o tempo limite para 60 s. |
| CONFIGURAR | Você define as opções de um sistema para um uso. | Configure o proxy. |
| DEFINIR | Você dá um valor específico a um item. | Defina a variável `PORT` como `8080`. |
| REDEFINIR | Você define de novo um valor que já tem um valor, por exemplo com o valor padrão. | Redefina a senha do usuário. |
| PERSONALIZAR | Você altera algo para as necessidades de uma pessoa ou de uma equipe. | Personalize as colunas do painel. |
| SUBSTITUIR | Você coloca um item no lugar de outro item. | Substitua o certificado antigo. |
| ATUALIZAR | Você substitui por uma versão mais nova ou por dados mais novos. | Atualize o pacote `openssl`. |

Não aprovadas neste grupo: "modificar", "mudar", "trocar", "adequar", "adaptar", "setar", "parametrizar", "customizar", "mexer", "manipular".

### 3.5 Mostrar e informar

| Palavra | Sujeito comum | Exemplo PTS-BR |
|---|---|---|
| MOSTRAR | Um sistema ou um documento faz algo ficar visível. | A tela mostra o estado da cópia. |
| APARECER | O item fica visível. | A mensagem aparece na parte superior da página. |
| VER | Uma pessoa vê ou lê algo. | Veja a tabela 2. |
| INDICAR | Um sinal ou um valor dá uma informação. | O código 0 indica sucesso. |
| INFORMAR | Uma pessoa ou um sistema dá uma informação a outra pessoa ou a outro sistema. | Informe o número do pedido ao suporte. |

Não aprovadas neste grupo: "exibir", "apresentar", "visualizar", "demonstrar", "evidenciar", "comunicar", "notificar", "reportar", "avisar", "alertar".

### 3.6 Erro, falha, defeito e problema

| Palavra | Significado | Exemplo PTS-BR |
|---|---|---|
| ERRO | Uma ação ou um resultado incorreto. | O comando retorna o erro 403. |
| FALHA | Um sistema ou um componente não funciona corretamente. | Uma falha no disco parou o banco de dados. |
| DEFEITO | A causa no código ou no projeto. | Esta versão corrige o defeito do login. |
| PROBLEMA | Uma condição que impede o resultado esperado. É a palavra geral. | Descreva o problema no chamado. |

"Incidente" é um nome técnico (04-termos-tecnicos.md). Não aprovadas neste grupo: "pane", "questão".

### 3.7 Mover dados e itens

| Palavra | Use quando | Exemplo PTS-BR |
|---|---|---|
| COPIAR | O original continua no lugar original. | Copie o arquivo para `/backup`. |
| MOVER | O original sai do lugar original. | Mova o log para `/var/archive`. |
| ENVIAR | Dados, uma mensagem ou um arquivo vão para um destino. | Envie o relatório para a equipe. |
| ENCAMINHAR | Você envia para outro destino algo que você recebeu. | Encaminhe o incidente para a equipe de banco de dados. |
| TRANSFERIR | Outra pessoa ou outra conta recebe a responsabilidade pelo item. | Transfira o repositório para a organização. |
| PUBLICAR | Um conteúdo, um pacote ou uma versão fica disponível para outras pessoas. | Publique o pacote no registry do `npm`. |

Não aprovadas neste grupo: "mandar", "jogar", "subir", "disponibilizar".

### 3.8 Outras fronteiras

| Palavras | Fronteira de significado |
|---|---|
| ACESSAR / ENTRAR | ACESSAR: usar um sistema ou um recurso com permissão. ENTRAR: começar uma sessão com as suas credenciais. |
| ESCOLHER / "selecionar" | ESCOLHER: decidir entre opções. "Selecionar" é um verbo técnico de interface (04-termos-tecnicos.md): marcar um item na tela. |
| PRESSIONAR / "clicar" | PRESSIONAR: tecla ou botão físico. "Clicar" é um verbo técnico de interface: botão na tela. |
| DAR / ATRIBUIR | DAR é o verbo geral: uma pessoa ou um item recebe algo, por exemplo uma permissão, um acesso ou uma informação. ATRIBUIR: uma pessoa, uma equipe ou uma conta fica com uma tarefa, um chamado ou um papel de acesso. Para um nome, use NOMEAR. Para um valor, use DEFINIR. |
| DEVER / PRECISAR / PODER | DEVER: um requisito obrigatório. PRECISAR: a necessidade de um recurso. PODER: a capacidade ou a permissão. Em procedimentos, use o imperativo, não DEVER. Para um evento que não acontece sempre, escreva o fato e a condição do evento: "O serviço falha quando o disco está cheio." |
| AGUARDAR / "esperar" | AGUARDAR tem apenas 1 significado. "Esperar" tem também os significados de "prever" e de "precisar". Portanto, "esperar" não é aprovado. |
| ATUAL / AGORA | ATUAL é adjetivo. AGORA é advérbio. Use as 2 palavras apenas para o momento em que o leitor faz o procedimento ou vê a interface, nunca para a data de publicação do texto (02-regras.md, R9.4): "Registre o valor atual do campo **Limite**." "Atualmente", "corrente", "recente" e "nova versão" não são aprovados. |
| PORQUE / PORTANTO | PORQUE indica a causa. PORTANTO indica a consequência. "Como" com o significado de causa, "pois", "visto que" e "uma vez que" não são aprovados. |

---

## 4. Verbos-suporte e locuções

Um verbo-suporte não tem um significado específico. O significado está no substantivo depois do verbo. O PTS-BR substitui o verbo-suporte e o substantivo por um verbo específico.

| Não aprovado | PTS-BR |
|---|---|
| Realize a instalação do agente. | Instale o agente. |
| Efetue a cópia dos dados. | Copie os dados. |
| Proceda à exclusão dos snapshots. | Exclua os snapshots. |
| Providencie a atualização do certificado. | Atualize o certificado. |
| Execute a revisão do código. | Revise o código. |
| Faça a verificação da porta. | Verifique a porta. |
| Dê início à sincronização. | Inicie a sincronização. |
| Faça uso do modo seguro. | Use o modo seguro. |

`FAZER (v)` é aprovado, mas apenas quando não existe um verbo mais específico: "Faça um backup do banco". `EXECUTAR (v)` é aprovado apenas para comandos, scripts, programas e deploys.

As locuções da tabela abaixo não são aprovadas. Cada locução tem uma entrada própria no dicionário.

| Tipo | Locuções não aprovadas | Alternativa |
|---|---|---|
| Objetivo | "a fim de", "com o objetivo de", "com o intuito de", "no sentido de", "visando", "de forma a", "para que" | PARA |
| Causa | "devido a", "em virtude de", "em razão de", "haja vista", "visto que", "já que", "uma vez que", "dado que", "tendo em vista" | PORQUE, POR CAUSA DE |
| Consequência | "destarte", "dessa forma", "assim sendo", "sendo assim", "por conseguinte", "consequentemente", "com isso", "por isso", "logo" | PORTANTO |
| Diferença | "porém", "contudo", "todavia", "entretanto", "no entanto", "não obstante", "embora", "ainda que" | MAS |
| Assunto | "a nível de", "em nível de", "com relação a", "em relação a", "no que tange a", "no que diz respeito a", "acerca de", "a respeito de", "referente a", "relativo a" | SOBRE, EM |
| Forma | "através de", "por meio de", "por intermédio de", "mediante", "via", "junto a" | COM, POR |
| Condição | "caso", "desde que", "a menos que", "mesmo que" | SE |
| Referência | "o mesmo", "o qual", "cujo", "tal", "referido", "supracitado", "mencionado" | ESTE, QUE, ou repita o substantivo |
---

## 5. Número de entradas

| Classe | Aprovadas | Obsoletas | Não aprovadas |
|---|---|---|---|
| v | 205 | 0 | 156 |
| s | 298 | 0 | 32 |
| adj | 138 | 0 | 31 |
| adv | 25 | 0 | 45 |
| prep | 24 | 0 | 5 |
| conj | 10 | 0 | 11 |
| pron | 19 | 0 | 17 |
| art | 3 | 0 | 0 |
| num | 1 | 0 | 1 |
| loc | 0 | 0 | 63 |
| abrev | 0 | 0 | 1 |
| **Total** | **723** | **0** | **362** |

---


## A

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| A (art) | Aprovada | Artigo definido feminino. Indica um item conhecido ou que o texto já indicou. | Abra a pasta de logs. | — |
| A (prep) | Aprovada | Indica o destino ou o objeto indireto de um verbo. | Envie o relatório à equipe de suporte. | — |
| a fim de (loc) | Não aprovada | Use: PARA (prep) | Reinicie o serviço para aplicar a configuração. | Reinicie o serviço a fim de aplicar a configuração. |
| a fim de que (loc) | Não aprovada | Use: PARA (prep) | Pare o job para liberar a fila. | Pare o job a fim de que a fila seja liberada. |
| a gente (pron) | Não aprovada | Reescreva: escreva o sujeito real | A equipe de plataforma mantém este serviço. | A gente mantém este serviço. |
| à mão (loc) | Não aprovada | Use: MANUAL (adj); MANUALMENTE (adv) | Edite o arquivo de forma manual. | Edite o arquivo à mão. |
| a menos que (loc) | Não aprovada | Use: SE (conj) — com NÃO | Se o teste não falhar, execute o deploy. | Execute o deploy, a menos que o teste falhe. |
| a nível de (loc) | Não aprovada | Use: EM (prep) — ou remova a locução | O erro acontece no banco de dados. | O erro acontece a nível de banco de dados. |
| A PARTIR DE (prep) | Aprovada | Indica o ponto de início no tempo ou em uma sequência de versões. | A opção `--json` está disponível a partir da versão 2.3. | Gere o relatório a partir dos logs. (Use: Gere o relatório com os dados dos logs.) |
| a respeito de (loc) | Não aprovada | Use: SOBRE (prep) | Leia a seção sobre limites de uso. | Leia a seção a respeito de limites de uso. |
| a saber (loc) | Não aprovada | Reescreva: use dois-pontos e uma lista | O pacote tem 2 componentes: o agente e o worker. | O pacote tem dois componentes, a saber, o agente e o coletor. |
| a seguir (loc) | Não aprovada | Use: ABAIXO (adv) | Execute o comando abaixo. | Execute o comando a seguir. |
| aba (s) | Não aprovada | Reescreva: use o nome técnico "guia" (04-termos-tecnicos.md, NT-05) | Clique na guia **Logs**. | Clique na aba **Logs**. |
| ABAIXO (adv) | Aprovada | Imediatamente depois do texto atual, na mesma página ou na mesma tela. Para um conteúdo em outro lugar do documento, escreva o número da seção, da tabela ou do passo. | O bloco de código abaixo mostra a saída do comando. | O consumo de CPU está abaixo de 50%. (Use: O consumo de CPU é menor que 50%.) / Veja a lista abaixo, na seção 9. (Use: Veja a lista da seção 9.) |
| ABERTO (adj) | Aprovada | Que permite acesso, conexão ou alteração. | Verifique se a porta 443 está aberta. | O desvio S1 está aberto. (Use: O desvio S1 ainda não tem correção.) |
| abertura (s) | Não aprovada | Use: CRIAÇÃO (s) | A data de criação do chamado é 2026-11-17. | A data de abertura do chamado é 2026-11-17. |
| abortar (v) | Não aprovada | Use: CANCELAR (v); PARAR (v) | Cancele a operação. | Aborte a operação. |
| ABRIR (v) | Aprovada | Fazer um arquivo, uma janela ou uma conexão ficar disponível para uso. | Abra o arquivo `config.yaml`. | Abra um chamado no portal. (Use: Crie um chamado no portal.) |
| AÇÃO (s) | Aprovada | Algo que uma pessoa ou um sistema faz. | O log registra cada ação do administrador. | — |
| acarretar (v) | Não aprovada | Use: CAUSAR (v) | Esta alteração causa a perda da sessão. | Esta alteração acarreta a perda da sessão. |
| ACEITAR (v) | Aprovada | Receber algo como válido ou permitido. | O servidor aceita apenas conexões TLS 1.3. | — |
| acerca de (prep) | Não aprovada | Use: SOBRE (prep) | Este documento tem informações sobre a API. | Este documento contém informações acerca da API. |
| ACESSAR (v) | Aprovada | Entrar em um sistema, em um recurso ou em um conjunto de dados com permissão. | Acesse o portal com a sua conta. | Acesse o link abaixo. (Use: Clique no link abaixo.) |
| ACESSO (s) | Aprovada | Possibilidade de entrar em um sistema ou de usar um recurso. | O grupo de suporte tem acesso de leitura ao banco. | — |
| achar (v) | Não aprovada | Use: ENCONTRAR (v) | Encontre o PID do processo. | Ache o PID do processo. |
| ACIMA (adv) | Aprovada | Imediatamente antes do texto atual, na mesma página ou na mesma tela. Para um conteúdo em outro lugar do documento, escreva o número da seção, da tabela ou do passo. | A tabela acima mostra os códigos de erro. | A latência está acima do limite. (Use: A latência é maior que o limite.) / Use o comando acima, do procedimento de instalação. (Use: Use o comando do passo 3 do procedimento de instalação.) |
| acionar (v) | Não aprovada | Use: ATIVAR (v); PRESSIONAR (v); ENVIAR (v) — para chamar uma pessoa, envie um alerta | Ative o modo de manutenção. / Envie um alerta ao analista de plantão. | Acione o modo de manutenção. / Acione o plantão. |
| acompanhar (v) | Não aprovada | Use: MONITORAR (v) | Monitore o consumo de memória durante a migração. | Acompanhe o consumo de memória durante a migração. |
| ACONTECER (v) | Aprovada | Começar a existir como evento em um momento. | O erro acontece apenas no ambiente de produção. | — |
| acrescentar (v) | Não aprovada | Use: ADICIONAR (v) | Adicione o parâmetro `--verbose`. | Acrescente o parâmetro `--verbose`. |
| adaptar (v) | Não aprovada | Use: ALTERAR (v) | Altere o script para a versão 3 da API. | Adapte o script à nova versão da API. |
| ademais (adv) | Não aprovada | Use: TAMBÉM (adv) | O script também cria a pasta de logs. | Ademais, o script cria a pasta de logs. |
| adequadamente (adv) | Não aprovada | Use: CORRETAMENTE (adv) | Verifique se o certificado está instalado corretamente. | Verifique se o certificado está adequadamente instalado. |
| adequar (v) | Não aprovada | Use: ALTERAR (v) | Altere o arquivo para o formato novo. | Adeque o arquivo ao novo formato. |
| ADIAR (v) | Aprovada | Alterar a data de uma ação ou de um evento para uma data depois da data planejada. | O gestor adiou a janela de manutenção para 2026-12-10. | — |
| adicionalmente (adv) | Não aprovada | Use: TAMBÉM (adv) | A versão 2 também aceita YAML. | Adicionalmente, a versão 2 aceita YAML. |
| ADICIONAR (v) | Aprovada | Colocar um item a mais em um conjunto, em uma lista ou em um sistema. | Adicione o usuário ao grupo `admin`. | — |
| admitir (v) | Não aprovada | Use: ACEITAR (v) | O campo aceita apenas números. | O campo admite apenas números. |
| ADOÇÃO (s) | Aprovada | Processo em que uma equipe ou uma empresa começa a usar uma ferramenta, um padrão ou um processo e chega ao uso regular. | A adoção do Kubernetes pela equipe começa em 2027. | — |
| adotar (v) | Não aprovada | Use: USAR (v) | A equipe usa o PTS-BR em todos os runbooks. | A equipe adota o PTS-BR em todos os runbooks. |
| adquirir (v) | Não aprovada | Use: OBTER (v) | Obtenha uma licença no portal do fornecedor. | Adquira uma licença no portal do fornecedor. |
| AFETAR (v) | Aprovada | Causar um efeito em um item, em um sistema ou em uma pessoa. | A falha afeta todos os clientes da região `sa-east-1`. | — |
| AGENDAR (v) | Aprovada | Definir a data e a hora em que uma tarefa vai acontecer. | Agende o backup para as 02:00 UTC-03:00. | — |
| AGORA (adv) | Aprovada | No momento em que o leitor faz o passo ou vê a interface. Não use para uma alteração de uma versão (02-regras.md, R9.4). | Aguarde 2 min. Agora, faça o passo 4. | O serviço agora usa a porta 8443. (Use: A partir da versão 3.0, o serviço usa a porta 8443.) |
| AGRUPAR (v) | Aprovada | Colocar itens em grupos de acordo com uma característica comum. | Agrupe os alertas por serviço. | — |
| AGUARDAR (v) | Aprovada | Não fazer uma ação até um evento acontecer ou até o fim de um tempo definido. | Aguarde 30 s. | — |
| AINDA (adv) | Aprovada | Até este momento. | O pacote ainda não está instalado. | — |
| ainda que (loc) | Não aprovada | Use: MAS (conj) | O teste falhou, mas o pipeline continuou. | Ainda que o teste tenha falhado, o pipeline continuou. |
| AJUDA (s) | Aprovada | Informação ou suporte para fazer uma tarefa. | Para obter ajuda, digite `--help`. | — |
| AJUDAR (v) | Aprovada | Dar a uma pessoa a informação ou a ação de que a pessoa precisa para fazer uma tarefa. | A mensagem de erro ajuda o usuário a corrigir o campo. | — |
| AJUSTAR (v) | Aprovada | Alterar um valor um pouco para obter o resultado correto. | Ajuste o tempo limite para 60 s. | Ajuste o código para a nova API. (Use: Altere o código para a versão 2 da API.) |
| alavancar (v) | Não aprovada | Use: USAR (v) | Use o cache para diminuir a latência. | Alavanque o cache para diminuir a latência. |
| alcançar (v) | Não aprovada | Use: CHEGAR (v) | O consumo de disco chega a 90%. | O consumo de disco alcança 90%. |
| ALEATÓRIO (adj) | Aprovada | Escolhido sem uma ordem e sem um critério. | Escolha uma amostra aleatória de 10 chamados do mês. | — |
| além de (loc) | Não aprovada | Use: E (conj); TAMBÉM (adv) | O script cria o usuário e configura as permissões. | Além de criar o usuário, o script configura as permissões. |
| além disso (loc) | Não aprovada | Use: TAMBÉM (adv) | O instalador também configura o firewall. | Além disso, o instalador configura o firewall. |
| ALERTA (s) | Aprovada | Mensagem automática que informa uma condição fora do normal. | O sistema de monitoramento envia um alerta quando o consumo de CPU é maior que 90%. | — |
| alertar (v) | Não aprovada | Use: INFORMAR (v) | Informe a equipe de plantão. | Alerte a equipe de plantão. |
| ALGO (pron) | Aprovada | Um item, uma ação ou um evento que a frase não define. | Se algo falhar, veja o log. | — |
| ALGUM (pron) | Aprovada | Um ou mais itens, sem indicar qual. | Se algum teste falhar, pare o deploy. | — |
| alinhar (v) | Não aprovada | Use: INFORMAR (v); DECIDIR (v) | Informe a equipe de produto sobre a data da versão. | Alinhe com a equipe de produto a data da versão. |
| ALTERAÇÃO (s) | Aprovada | Resultado da ação de alterar um item. | Registre cada alteração no changelog. | — |
| ALTERAR (v) | Aprovada | Dar outro conteúdo, outra estrutura ou outro valor a algo. | Altere a senha do usuário `root`. | — |
| ALTERNAR (v) | Aprovada | Ir de um estado para outro estado e depois voltar ao primeiro estado. | Alterne entre o modo local e o modo remoto. | — |
| ALTERNATIVA (s) | Aprovada | Outra opção que você pode usar no lugar da primeira opção. | Se a porta 8080 não estiver livre, use a alternativa: a porta 8081. | — |
| ALTO (adj) | Aprovada | Com valor maior que o normal ou que o limite. Escreva o valor (02-regras.md, R6.4). | A latência está alta: 2 s, com o limite de 500 ms. | — |
| AMARELO (adj) | Aprovada | Da cor amarela. Em painéis, indica um estado de aviso. | O ícone amarelo indica um consumo de disco maior que 80%. | — |
| AMBÍGUO (adj) | Aprovada | Que tem 2 ou mais significados possíveis. | O nome do campo `valor` é ambíguo. Use o nome `valor_total`. | — |
| AMBOS (pron) | Aprovada | Os 2 itens. | Ambos os servidores usam a mesma versão. | — |
| AMOSTRA (s) | Aprovada | Parte de um conjunto que a equipe analisa para conhecer o conjunto. | Analise uma amostra de 100 requisições do log. | — |
| ANALISAR (v) | Aprovada | Ver ou ler em detalhe para entender o conteúdo ou a causa de algo. | Analise o log para encontrar a causa da falha. | Analise se a porta está aberta. (Use: Verifique se a porta está aberta.) |
| ANÁLISE (s) | Aprovada | Ação de ler e avaliar um item para entender o conteúdo ou a causa de algo. | A análise do log mostra 3 erros de conexão. | — |
| análogo (adj) | Não aprovada | Use: SEMELHANTE (adj) | O erro é semelhante ao erro do chamado anterior. | O erro é análogo ao do chamado anterior. |
| ANEXAR (v) | Aprovada | Juntar um arquivo a uma mensagem, a um chamado ou a um documento. | Anexe o log ao chamado. | — |
| ANEXO (s) | Aprovada | Arquivo que está junto a uma mensagem, a um chamado ou a um documento. | O anexo tem o log completo. | — |
| ANO (s) | Aprovada | Período de 12 meses. | O sistema mantém os logs de auditoria por 5 anos. | — |
| ANTERIOR (adj) | Aprovada | Que está antes na ordem ou no tempo. | Volte para a versão anterior. | — |
| anteriormente (adv) | Não aprovada | Use: ANTES (adv) | A versão 1.9 usa o valor padrão 30. | Anteriormente, o valor padrão era 30. |
| ANTES (adv) | Aprovada | Em um momento anterior. | Faça um backup antes. | — |
| ANTES DE (prep) | Aprovada | Em um momento anterior a outro momento ou a outro evento. | Pare o serviço antes da atualização. | — |
| antes que (loc) | Não aprovada | Use: ANTES DE (prep) | Faça um backup antes da migração. | Faça um backup antes que a migração comece. |
| ANTIGO (adj) | Aprovada | Que um item mais novo substituiu ou que existe antes dos outros itens. | Exclua as imagens antigas do repositório de imagens. | — |
| ANUAL (adj) | Aprovada | Que acontece 1 vez por ano. | A auditoria anual verifica os acessos ao banco de produção. | — |
| ao acaso (loc) | Não aprovada | Use: ALEATÓRIO (adj) | Escolha uma amostra aleatória de 10 chamados. | Escolha 10 chamados ao acaso. |
| aonde (adv) | Não aprovada | Use: ONDE (adv) | Informe a pasta onde o script grava o log. | Informe a pasta aonde o script grava o log. |
| apagar (v) | Não aprovada | Use: EXCLUIR (v); LIMPAR (v) | Exclua o arquivo temporário. / Limpe o campo **Nome**. | Apague o arquivo temporário. / Apague o campo **Nome**. |
| APARECER (v) | Aprovada | Ficar visível na tela ou em um resultado. | A mensagem de erro aparece na parte superior da página. | — |
| APENAS (adv) | Aprovada | Não mais que o item ou a quantidade que a frase indica. | Apenas administradores podem excluir projetos. | — |
| APLICAR (v) | Aprovada | Fazer uma configuração, uma alteração ou uma regra começar a ter efeito. | Aplique a política de senha a todos os usuários. | Aplique um questionário à equipe. (Use: Envie o formulário à equipe.) |
| após (prep) | Não aprovada | Use: DEPOIS DE (prep) | Reinicie o serviço depois da atualização. | Reinicie o serviço após a atualização. |
| APRENDER (v) | Aprovada | Obter um conhecimento novo. | Na análise pós-incidente, a equipe registra o que aprendeu com o incidente. | — |
| apresentar (v) | Não aprovada | Use: MOSTRAR (v) | A tela mostra o estado do pedido. | A tela apresenta o status do pedido. |
| APROVAÇÃO (s) | Aprovada | Permissão formal para uma tarefa continuar. | A alteração precisa da aprovação de 2 revisores. | — |
| APROVAR (v) | Aprovada | Dar permissão formal para algo continuar. | O revisor aprova o pull request. | — |
| APROXIMADAMENTE (adv) | Aprovada | Com um valor perto de um número, mas não exato. | A migração demora aproximadamente 20 min. | — |
| aquele (pron) | Não aprovada | Use: ESTE (pron) — ou repita o substantivo | Compare o arquivo novo com o arquivo antigo. Mantenha o arquivo antigo. | Compare o arquivo novo com o antigo e mantenha aquele. |
| aqui (adv) | Não aprovada | Use: ESTE (pron); PASSO (s) | Neste passo, o script cria a pasta. | Aqui, o script cria a pasta. |
| aquilo (pron) | Não aprovada | Use: ESTE (pron) — com o substantivo | Este erro acontece quando o token não é válido. | Aquilo acontece quando o token é inválido. |
| ÁREA (s) | Aprovada | Parte definida de uma tela, de um sistema ou de uma organização. | A área de mensagens está no canto superior direito. | — |
| ARMAZENAR (v) | Aprovada | Manter dados em um lugar para usar depois. | O banco armazena os dados de sessão por 24 h. | — |
| ARQUIVAR (v) | Aprovada | Mover itens que não estão em uso para um lugar de armazenamento de longo prazo. | Arquive os projetos que não têm alterações nos últimos 12 meses. | — |
| ARREDONDAR (v) | Aprovada | Alterar um número para o valor mais próximo com menos algarismos depois da vírgula. | Arredonde o valor 2,46 s para 2,5 s. | — |
| assegurar (v) | Não aprovada | Use: VERIFICAR (v) | Verifique se o serviço está ativo. | Assegure que o serviço esteja ativo. |
| ASSIM (adv) | Aprovada | Da forma que o texto mostra. | Escreva o comando assim: `git log --oneline`. | Assim, o sistema fica seguro. (Use: Portanto, o sistema fica seguro.) |
| assim que (loc) | Não aprovada | Use: QUANDO (conj); DEPOIS DE (prep) | Quando a cópia terminar, feche o terminal. | Assim que a cópia terminar, feche o terminal. |
| assim sendo (loc) | Não aprovada | Use: PORTANTO (conj) | O disco está cheio. Portanto, o serviço parou. | O disco está cheio. Assim sendo, o serviço parou. |
| ASSOCIAR (v) | Aprovada | Criar uma relação entre 2 itens. | Associe o endereço IP ao balanceador de carga. | — |
| ASSUNTO (s) | Aprovada | O que um texto, uma mensagem ou uma reunião descreve. | Escreva o número do chamado no assunto do e-mail. | — |
| ATA (s) | Aprovada | Documento com as decisões e as tarefas de uma reunião. | Anexe a ata da reunião ao chamado. | — |
| ATÉ (prep) | Aprovada | Indica o limite de tempo, de espaço ou de quantidade. | Aguarde até o fim da sincronização. | — |
| ATENÇÃO (s) | Aprovada | Palavra de sinalização de aviso. Use apenas da forma que 02-regras.md, seção 7, define. | **ATENÇÃO:** Execute a migração apenas na janela de manutenção. A migração bloqueia a tabela `pedidos` por 10 min. Durante este tempo, os clientes não podem criar pedidos. | Atenção para o prazo. (Use: O prazo é 2026-12-10.) |
| atender (v) | Não aprovada | Use: SEGUIR (v); RESPONDER (v) | O código segue a norma interna. | O código atende à norma interna. |
| atentar (v) | Não aprovada | Use: LER (v); VERIFICAR (v) | Leia os avisos antes de continuar. | Atente para os avisos antes de continuar. |
| atingir (v) | Não aprovada | Use: CHEGAR (v) | A fila chega a 10 000 mensagens. | A fila atinge 10 000 mensagens. |
| ATIVAR (v) | Aprovada | Fazer uma funcionalidade ou uma opção começar a funcionar e continuar neste estado. | Ative a MFA na sua conta. | Ative o servidor. (Use: Ligue o servidor.) |
| ATIVIDADE (s) | Aprovada | Trabalho ou ação que acontece durante um período. | O painel mostra a atividade dos últimos 7 dias. | — |
| ATIVO (adj) | Aprovada | Que está em funcionamento ou em uso. | Mostre apenas os usuários ativos. | — |
| ATRASO (s) | Aprovada | Tempo a mais que o tempo planejado. | O atraso na fila é de 5 min. | — |
| através de (loc) | Não aprovada | Use: COM (prep); POR (prep) | Envie o arquivo com o comando `scp`. | Envie o arquivo através do comando `scp`. |
| ATRIBUIR (v) | Aprovada | Fazer uma tarefa, um chamado ou um papel de acesso ser de uma pessoa, de uma equipe ou de uma conta. | Atribua o chamado ao analista de plantão. | Atribua o valor `8080` à variável `PORT`. (Use: Defina a variável `PORT` como `8080`.) |
| ATUAL (adj) | Aprovada | Que existe ou que é válido no momento em que o leitor faz o procedimento ou vê a interface. Não use para a data de publicação do texto (02-regras.md, R9.4). | Antes da alteração, registre o valor atual do campo **Limite**. | A versão atual corrige o defeito. (Use: A versão 2.4.1 corrige o defeito.) |
| ATUALIZAÇÃO (s) | Aprovada | Ação de substituir um item por uma versão mais nova ou por dados mais novos. | A atualização demora 10 min. | — |
| ATUALIZAR (v) | Aprovada | Substituir por uma versão mais nova ou por dados mais novos. | Atualize o pacote `openssl`. | Atualize a equipe sobre o incidente. (Use: Informe a equipe sobre o incidente.) |
| atualmente (adv) | Não aprovada | Reescreva: escreva a versão ou a data (02-regras.md, R9.4) | A partir da versão 3.0, o serviço usa a porta 8080. | Atualmente, o serviço usa a porta 8080. |
| AUMENTAR (v) | Aprovada | Fazer ficar maior em quantidade, em tamanho ou em valor. | Aumente o limite de memória para 2 GB. | — |
| AUSENTE (adj) | Aprovada | Que não está em um lugar, em uma lista ou em um conjunto. | O campo `email` está ausente na resposta da API. | — |
| AUTOMATICAMENTE (adv) | Aprovada | Sem a ação de uma pessoa. | O sistema exclui os arquivos temporários automaticamente. | — |
| AUTOMÁTICO (adj) | Aprovada | Que funciona sem a ação de uma pessoa. | O backup automático começa às 02:00 UTC-03:00. | — |
| AUTOR (s) | Aprovada | Pessoa que criou um texto, um commit ou um comentário. | O autor do commit responde aos comentários da revisão. | — |
| AVALIAR (v) | Aprovada | Decidir o valor, a qualidade ou o efeito de algo com critérios definidos. | Avalie o impacto da alteração antes da aprovação. | — |
| averiguar (v) | Não aprovada | Use: VERIFICAR (v) | Verifique se o backup terminou. | Averigue se o backup foi concluído. |
| avisar (v) | Não aprovada | Use: INFORMAR (v) | Informe o cliente sobre a janela de manutenção. | Avise o cliente sobre a janela de manutenção. |
| AVISO (s) | Aprovada | Texto que informa um risco ou uma condição importante. | Leia o aviso antes de continuar. | — |

## B

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| BAIXO (adj) | Aprovada | Com valor menor que o normal ou que o limite. Escreva o valor (02-regras.md, R6.4). | O espaço livre em disco está baixo: 5%. | — |
| BASE (s) | Aprovada | Item que outro item usa como ponto de início ou como referência. | A imagem `python:3.12-slim` é a base da imagem da API. | — |
| basicamente (adv) | Não aprovada | Reescreva: remova a palavra | O script copia os arquivos. | Basicamente, o script copia os arquivos. |
| bem (adv) | Não aprovada | Use: CORRETAMENTE (adv) | O serviço funciona corretamente. | O serviço funciona bem. |
| bem como (loc) | Não aprovada | Use: E (conj) | Instale o agente e o worker. | Instale o agente, bem como o worker. |
| BLOQUEAR (v) | Aprovada | Impedir o acesso a algo ou o uso de algo. | Bloqueie a porta 23 no firewall. | O processo bloqueou. (Use: O processo parou de responder.) |
| BLOQUEIO (s) | Aprovada | Estado de um item bloqueado. | Depois de 5 senhas incorretas, o sistema bloqueia a conta. O bloqueio termina depois de 30 min. | O sistema faz o bloqueio da conta. (Use: O sistema bloqueia a conta.) |
| botar (v) | Não aprovada | Use: COLOCAR (v) | Coloque o arquivo na pasta `config`. | Bote o arquivo na pasta config. |
| BRASILEIRO (adj) | Aprovada | Do Brasil. | O CPF é um número brasileiro. | — |
| buscar (v) | Não aprovada | Use: PROCURAR (v); OBTER (v) | Procure o termo "timeout" no log. / A aplicação cliente obtém os dados da API. | Busque o termo "timeout" no log. / A aplicação cliente busca os dados da API. |

## C

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| CADA (pron) | Aprovada | Todos os itens de um grupo, um por um. | Teste cada endpoint. | — |
| cadastrar (v) | Não aprovada | Use: REGISTRAR (v); ADICIONAR (v) | Adicione a chave SSH à sua conta. | Cadastre a chave SSH na sua conta. |
| CADASTRO (s) | Aprovada | Conjunto dos dados de uma pessoa ou de um item que um sistema registra. | Atualize o cadastro do cliente com o e-mail novo. | — |
| cair (v) | Não aprovada | Use: PARAR (v); INDISPONÍVEL (adj) | O servidor parou às 14:00 UTC-03:00. / O site está indisponível. | O servidor caiu às 14h. / O site caiu. |
| CALCULAR (v) | Aprovada | Obter um valor com uma operação de números, por exemplo uma soma. | Calcule o espaço necessário para o backup. | — |
| CÁLCULO (s) | Aprovada | Operação que obtém um valor a partir de outros valores. | O cálculo da disponibilidade usa os minutos de indisponibilidade do mês. | — |
| CALENDÁRIO (s) | Aprovada | Lista dos dias de um período com os eventos e os dias de trabalho. | O calendário da empresa define os dias úteis. | — |
| CAMADA (s) | Aprovada | Parte de um sistema que está sobre outra parte e que tem um objetivo próprio. | A camada de cache responde a 80% das requisições. | — |
| CAMINHO (s) | Aprovada | Sequência de pontos, de pastas ou de passos de um início até um fim. | Escreva o caminho completo do arquivo: `/etc/app/config.yaml`. | — |
| CANAL (s) | Aprovada | Ferramenta ou lugar em que um grupo de pessoas recebe mensagens, por exemplo um canal do Slack. | Envie o aviso de manutenção ao canal `#incidentes`. | — |
| CANCELAR (v) | Aprovada | Parar uma operação antes do fim, sem aplicar o resultado. | Cancele o upload. | — |
| CANTO (s) | Aprovada | Parte de uma tela, de uma janela ou de uma página entre 2 lados, por exemplo o canto superior direito. | O ícone de ajuda está no canto superior direito. | — |
| CAPACIDADE (s) | Aprovada | Quantidade máxima que um sistema ou um componente aceita. | A capacidade do disco é de 500 GB. | — |
| CARACTERE (s) | Aprovada | Uma letra, um número, um sinal de pontuação ou um símbolo. | A senha precisa ter 12 caracteres ou mais. | — |
| CARACTERÍSTICA (s) | Aprovada | Qualidade que identifica um item ou que separa um item de outros itens. | O tipo de disco é uma característica da instância. | — |
| CARGA (s) | Aprovada | Quantidade de requisições ou de trabalho que um sistema recebe em um período. | A carga da API é de 2 000 requisições por segundo às 20:00 UTC-03:00. | — |
| CARGO (s) | Aprovada | Posição de uma pessoa na estrutura de uma empresa. | O formulário pede o nome e o cargo do solicitante. | — |
| CARREGAR (v) | Aprovada | Colocar dados ou código na memória para uso. | O navegador carrega a página em 2 s. | Carregue o arquivo no portal. (Use: Envie o arquivo para o portal.) |
| caso (conj) | Não aprovada | Use: SE (conj) | Se o teste falhar, pare o deploy. | Caso o teste falhe, pare o deploy. |
| CATÁLOGO (s) | Aprovada | Lista organizada dos produtos ou dos serviços que uma empresa vende. | A API de catálogo retorna os produtos do catálogo da loja. | — |
| CAUSA (s) | Aprovada | Fato ou condição que faz um evento acontecer. | Encontre a causa da falha. | — |
| CAUSAR (v) | Aprovada | Fazer um evento ou uma condição acontecer. | Uma senha incorreta causa o bloqueio da conta. | — |
| CÉLULA (s) | Aprovada | Parte de uma tabela que contém 1 valor, em 1 linha e em 1 coluna. | Não use células vazias na tabela. Escreva um travessão (—) na célula. | — |
| CENÁRIO (s) | Aprovada | Conjunto de condições para um teste ou para uma situação de operação. | Teste o cenário em que a rede falha. | — |
| CENTRAL (adj) | Aprovada | Que controla as outras partes de um sistema. | O kernel é a parte central do sistema operacional. | — |
| CENTRO (s) | Aprovada | Ponto ou área no meio de algo. | A mensagem aparece no centro da tela. | — |
| cerca de (loc) | Não aprovada | Use: APROXIMADAMENTE (adv) | A cópia demora aproximadamente 5 min. | A cópia leva cerca de 5 minutos. |
| certificar-se (v) | Não aprovada | Use: VERIFICAR (v) | Verifique se o serviço está ativo. | Certifique-se de que o serviço está ativo. |
| certo (adj) | Não aprovada | Use: CORRETO (adj) | Use a versão correta do driver. | Use a versão certa do driver. |
| cessar (v) | Não aprovada | Use: PARAR (v) | O serviço para de enviar métricas. | O serviço cessa o envio de métricas. |
| checar (v) | Não aprovada | Use: VERIFICAR (v) | Verifique o estado do pod. | Cheque o status do pod. |
| CHEGAR (v) | Aprovada | Começar a estar em um lugar, em um valor ou em um momento. | O consumo de disco chega a 90%. | — |
| CHEIO (adj) | Aprovada | Sem espaço livre. | O disco está cheio. | — |
| CICLO (s) | Aprovada | Sequência de etapas que acontece de novo, sempre na mesma ordem. | Cada ciclo de backup tem 1 backup completo e 6 backups incrementais. | — |
| CITAR (v) | Aprovada | Escrever no texto o nome, o número ou as palavras de outro item. | Cite o número do chamado na mensagem do commit. | — |
| CLASSIFICAR (v) | Aprovada | Colocar um item em um grupo de acordo com um critério. | Classifique o incidente como SEV2. | — |
| COBRIR (v) | Aprovada | Ter uma situação, um item ou um risco dentro do escopo de um teste, de uma licença ou de um contrato. | Os testes cobrem as 3 saídas da função `validar_cpf()`. | — |
| coisa (s) | Não aprovada | Use: ITEM (s) | Remova os itens da pasta `tmp`. | Remova as coisas da pasta `tmp`. |
| COLETAR (v) | Aprovada | Obter dados de uma ou mais fontes e juntar os dados em um lugar. | Colete os logs dos 3 nós. | — |
| COLOCAR (v) | Aprovada | Fazer um item estar em um lugar. | Coloque o arquivo `.env` na pasta principal do projeto. | — |
| COLUNA (s) | Aprovada | Série vertical de itens em uma tabela. | A coluna **Estado** mostra o resultado de cada teste. | — |
| COM (prep) | Aprovada | Indica o que está junto ou o que uma pessoa ou um sistema usa em uma ação. | Inicie o contêiner com a opção `-d`. | — |
| com isso (loc) | Não aprovada | Use: PORTANTO (conj) | O cache está vazio. Portanto, a primeira consulta demora 2 s. | O cache está vazio; com isso, a primeira consulta é lenta. |
| com o intuito de (loc) | Não aprovada | Use: PARA (prep) | Ative o log de depuração para analisar a falha. | Ative o log de depuração com o intuito de analisar a falha. |
| com o objetivo de (loc) | Não aprovada | Use: PARA (prep) | Crie um índice para diminuir o tempo da consulta. | Crie um índice com o objetivo de reduzir o tempo da consulta. |
| com relação a (loc) | Não aprovada | Use: SOBRE (prep) | Leia as notas sobre a migração. | Leia as notas com relação à migração. |
| combinação (s) | Não aprovada | Reescreva: escreva os itens. Para teclas, escreva "as teclas" e o nome de cada tecla (04-termos-tecnicos.md, NT-06) | Pressione as teclas **Ctrl+C**. | Pressione a combinação de teclas **Ctrl+C**. |
| combinar (v) | Não aprovada | Use: JUNTAR (v) | Junte os 2 arquivos de configuração. | Combine os 2 arquivos de configuração. |
| COMEÇAR (v) | Aprovada | Ter início em um momento. | A janela de deploy começa às 22:00 UTC-03:00. | Comece o serviço. (Use: Inicie o serviço.) |
| começo (s) | Não aprovada | Use: INÍCIO (s) | Leia o procedimento do início ao fim. | Leia o procedimento do começo ao fim. |
| COMENTAR (v) | Aprovada | Escrever um comentário sobre um item. | Comente o pull request com as alterações necessárias. | — |
| COMENTÁRIO (s) | Aprovada | Texto que uma pessoa adiciona a um documento, a um chamado ou a uma revisão. | Responda a cada comentário da revisão. | — |
| COMERCIAL (adj) | Aprovada | Que é sobre a venda de produtos ou de serviços. | A equipe comercial informa os clientes sobre a manutenção. | — |
| COMO (prep) | Aprovada | Com a identidade ou com o formato de. | Execute o script como administrador. / Salve o relatório como CSV. | Como o disco está cheio, o serviço parou. (Use: O serviço parou porque o disco está cheio.) |
| COMPARAR (v) | Aprovada | Ver 2 ou mais itens em detalhe para encontrar as diferenças. | Compare os 2 arquivos de configuração. | — |
| COMPARTILHAR (v) | Aprovada | Dar acesso a um item para outras pessoas. | Compartilhe o painel com a equipe de suporte. | — |
| COMPATIBILIDADE (s) | Aprovada | Qualidade de 2 itens que funcionam juntos sem erro. | Verifique a compatibilidade do driver com o kernel 6.8. | — |
| COMPATÍVEL (adj) | Aprovada | Que funciona corretamente com outro item. | A versão 3.2 é compatível com Python 3.12. | — |
| completar (v) | Não aprovada | Use: TERMINAR (v) | Termine a instalação. | Complete a instalação. |
| COMPLETO (adj) | Aprovada | Que tem todas as partes. | Faça um backup completo. | — |
| COMPONENTE (s) | Aprovada | Parte de um sistema com um objetivo próprio. | Atualize cada componente do cluster. | — |
| COMPORTAMENTO (s) | Aprovada | Forma em que um sistema responde a uma ação ou a uma condição. | A versão 2.4 altera o comportamento do botão **Salvar**. | — |
| COMPRA (s) | Aprovada | Ação de obter um produto pelo pagamento de um valor. | O gestor aprovou a compra. | — |
| COMUM (adj) | Aprovada | Que acontece com frequência ou que vários itens têm. | A seção 5 descreve os erros comuns. | — |
| COMUNICADO (s) | Aprovada | Texto curto que uma empresa ou uma equipe envia a um grupo de pessoas para informar um fato. | Publique o comunicado do incidente no portal de suporte a cada 30 min. | — |
| comunicar (v) | Não aprovada | Use: INFORMAR (v) | Informe a falha ao gerente de incidente. | Comunique a falha ao gerente de incidente. |
| conceder (v) | Não aprovada | Use: DAR (v) | Dê permissão de leitura ao grupo `auditoria`. | Conceda permissão de leitura ao grupo `auditoria`. |
| concluir (v) | Não aprovada | Use: TERMINAR (v) | Termine a configuração do agente. | Conclua a configuração do agente. |
| concreto (adj) | Não aprovada | Use: ESPECÍFICO (adj) | Escreva uma consequência específica: o cliente perde o pedido. | Escreva uma consequência concreta. |
| CONDIÇÃO (s) | Aprovada | Estado que precisa existir para algo acontecer. | A regra tem 2 condições. | — |
| CONECTAR (v) | Aprovada | Criar um caminho entre 2 itens para enviar e receber dados ou energia. Também é verbo pronominal, com "se" antes do verbo (02-regras.md, R3.7): "o serviço se conecta ao banco". | Conecte a aplicação cliente ao banco de dados. | — |
| CONEXÃO (s) | Aprovada | Caminho que permite enviar e receber dados entre 2 itens. | A conexão com o banco falhou. | — |
| conferir (v) | Não aprovada | Use: VERIFICAR (v); COMPARAR (v) | Verifique o hash do arquivo. / Compare o hash com o valor publicado. | Confira o hash do arquivo. |
| confidencial (adj) | Não aprovada | Use: SECRETO (adj) | O token é secreto. | O token é confidencial. |
| CONFIGURAÇÃO (s) | Aprovada | Conjunto de opções que definem como um sistema funciona. | Faça uma cópia da configuração atual. | — |
| CONFIGURAR (v) | Aprovada | Definir as opções de um sistema para um uso específico. | Configure o proxy no arquivo `.npmrc`. | — |
| CONFIRMAR (v) | Aprovada | Informar ou mostrar que algo está correto, ou aprovar que uma ação continue. | Clique em **OK** para confirmar a exclusão. | Confirme as alterações no Git. (Use: Crie um commit.) |
| CONFLITO (s) | Aprovada | Condição em que 2 regras, 2 alterações ou 2 valores não podem ser verdadeiros ao mesmo tempo. | Resolva o conflito de merge no arquivo `app.py`. | — |
| conforme (conj) | Não aprovada | Use: DE ACORDO COM (prep); QUANDO (conj) | Configure o firewall de acordo com a política. / Quando a fila aumentar, adicione workers. | Configure o firewall conforme a política. / Conforme a fila aumenta, adicione workers. |
| CONFUNDIR (v) | Aprovada | Usar ou entender um item no lugar de outro item, por erro. | O leitor confunde os 2 ambientes quando os 2 ambientes têm o mesmo nome. | — |
| CONHECER (v) | Aprovada | Ter informação sobre um item ou ter usado um item antes. | O analista de plantão conhece o procedimento de rollback. | — |
| CONHECIMENTO (s) | Aprovada | Informação que uma pessoa sabe e que usa em um trabalho. | O runbook não precisa de conhecimento do código da aplicação. | — |
| CONJUNTO (s) | Aprovada | Grupo de itens que você usa ou analisa como uma unidade. | O conjunto de testes tem 120 testes. | — |
| conseguir (v) | Não aprovada | Use: PODER (v); OBTER (v) | Se você não puder acessar o portal, peça ajuda ao suporte. | Caso não consiga acessar o painel, solicite ajuda ao suporte. |
| CONSEQUÊNCIA (s) | Aprovada | Resultado de uma ação ou de um evento. | Leia as consequências da exclusão antes de confirmar. | — |
| consequentemente (adv) | Não aprovada | Use: PORTANTO (conj) | O token não é válido. Portanto, a API retorna 401. | O token é inválido; consequentemente, a API retorna 401. |
| consertar (v) | Não aprovada | Use: CORRIGIR (v); REPARAR (v) | Corrija o script de backup. | Conserte o script de backup. |
| considerar (v) | Não aprovada | Reescreva: reescreva com USAR (v), CONTAR (v) ou AVALIAR (v) | O cálculo usa apenas os dias úteis. | O cálculo considera apenas os dias úteis. |
| constar (v) | Não aprovada | Use: ESTAR (v) | O endereço IP está na lista de bloqueio. | O endereço IP consta na lista de bloqueio. |
| constatar (v) | Não aprovada | Use: ENCONTRAR (v); VERIFICAR (v) | A equipe encontrou um erro no módulo de pagamento. | A equipe constatou um erro no módulo de impostos. |
| CONSUMIR (v) | Aprovada | Usar um recurso, que fica menos disponível para outros usos. | O processo consome 2 GB de memória. | — |
| CONSUMO (s) | Aprovada | Quantidade de um recurso que um sistema usa, por exemplo CPU, memória, disco ou rede. | O consumo de memória do pod é 900 MiB. | — |
| CONTAR (v) | Aprovada | Obter o número de itens. | Conte as linhas do arquivo com o comando `wc -l`. | — |
| CONTATO (s) | Aprovada | Dados que permitem enviar uma mensagem a uma pessoa, por exemplo o e-mail. | Escreva o contato da equipe de suporte no runbook. | — |
| CONTER (v) | Aprovada | Ter um item como parte do conteúdo. | O arquivo contém as chaves públicas. | — |
| CONTEÚDO (s) | Aprovada | O que está dentro de algo. | Copie o conteúdo do arquivo. | — |
| CONTINUAR (v) | Aprovada | Fazer algo sem parar ou depois de uma pausa. | Clique em **Próximo** para continuar. | — |
| CONTRA (prep) | Aprovada | Indica o item de que uma ação protege, ou o item que uma ação tenta impedir. | Proteja o servidor contra acesso sem autorização. | — |
| CONTRATO (s) | Aprovada | Documento formal em que 2 ou mais partes definem o que cada parte faz e recebe. | O contrato define o SLA de 99,9% para a API. | — |
| CONTROLAR (v) | Aprovada | Fazer algo funcionar da forma que você define. | O agendador controla a ordem dos jobs. | — |
| contudo (conj) | Não aprovada | Use: MAS (conj) | O build terminou, mas a cobertura de testes diminuiu. | O build terminou; contudo, a cobertura de testes diminuiu. |
| CONVENÇÃO (s) | Aprovada | Regra que uma equipe ou um grupo de pessoas aceita e segue, mas que não é uma norma oficial. | Siga a convenção de nomes do repositório para o nome do branch. | — |
| CONVERSÃO (s) | Aprovada | Ação de converter um item para outro formato, para outra unidade ou para outro tipo. | A conversão do arquivo CSV para o formato JSON demora 2 min. | — |
| CONVERTER (v) | Aprovada | Alterar dados de um formato para outro formato. | Converta o arquivo CSV para JSON. | — |
| CONVIDAR (v) | Aprovada | Enviar um convite a uma pessoa. | Convide o analista para o projeto **Pagamentos**. | — |
| CONVITE (s) | Aprovada | Mensagem com um link que dá a uma pessoa o acesso a uma equipe, a um projeto ou a uma reunião. | Envie um convite ao e-mail do colaborador novo. | — |
| CÓPIA (s) | Aprovada | Item igual a outro item. | Mantenha uma cópia do arquivo original. | — |
| COPIAR (v) | Aprovada | Fazer um item igual a outro item, sem remover o original. | Copie o arquivo para a pasta `/backup`. | — |
| COR (s) | Aprovada | Qualidade que uma pessoa vê em um item, por exemplo verde, amarelo ou vermelho. | Não use apenas a cor para indicar um estado. Escreva também o nome do estado. | — |
| CORREÇÃO (s) | Aprovada | Alteração que remove um erro ou um defeito. | A versão 2.4.1 tem a correção do defeito do login. | — |
| corrente (adj) | Não aprovada | Use: ATUAL (adj) | Registre o valor atual do campo **Limite**. | Registre o valor corrente do campo **Limite**. |
| CORRESPONDER (v) | Aprovada | Ser igual a outro item ou ter uma relação definida com outro item. | Cada linha do arquivo corresponde a 1 pedido. | — |
| CORRETAMENTE (adv) | Aprovada | Sem erro. | O serviço funciona corretamente. | — |
| CORRETO (adj) | Aprovada | Sem erro e de acordo com o requisito. | Digite a senha correta. | — |
| CORRIGIR (v) | Aprovada | Fazer um defeito ou um dado incorreto ficar correto. | Esta versão corrige o erro de login. | — |
| CRIAÇÃO (s) | Aprovada | Ação de criar um item. | O campo `data_criacao` contém a data de criação do pedido. | — |
| CRIAR (v) | Aprovada | Fazer existir um item novo. | Crie um usuário para o serviço. | — |
| CRITÉRIO (s) | Aprovada | Regra que você usa para decidir ou para avaliar algo. | O critério de aceite é: a API responde em menos de 200 ms. | — |
| CRÍTICO (adj) | Aprovada | Que, quando falha, faz um serviço parar ou causa uma perda de dados. | Aplique os patches críticos primeiro. | — |
| crucial (adj) | Não aprovada | Use: IMPORTANTE (adj); NECESSÁRIO (adj) | Este passo é necessário. | Este passo é crucial. |
| CUIDADO (s) | Aprovada | Palavra de sinalização de aviso. Use apenas da forma que 02-regras.md, seção 7, define. | **CUIDADO:** Feche o arquivo `config.yaml` no editor antes de executar o script. O script sobrescreve o arquivo `config.yaml`. Você perde as alterações que não salvou no editor. | Tenha cuidado com o arquivo. (Use: Não altere o arquivo.) |
| cujo (pron) | Não aprovada | Use: COM (prep) — ou reescreva a frase | Exclua os arquivos com data anterior a 2024-01-01. | Exclua os arquivos cuja data é anterior a 2024-01-01. |
| CUMPRIR (v) | Aprovada | Fazer o que uma regra, um prazo ou um requisito define. | O texto cumpre a regra R4.2. | — |
| CURTO (adj) | Aprovada | Com tamanho ou duração menor que o normal. | Use nomes curtos para as variáveis. | — |
| CUSTO (s) | Aprovada | Valor em dinheiro ou em recursos que algo usa. | O painel mostra o custo de cada conta por mês. | — |
| customizar (v) | Não aprovada | Use: PERSONALIZAR (v) | Personalize as colunas do painel. | Customize as colunas do painel. |

## D

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| DADO (s) | Aprovada | Informação que um sistema armazena ou processa. Use em geral no plural. | Faça um backup dos dados antes da migração. | Dado que o disco está cheio, o serviço parou. (Use: O serviço parou porque o disco está cheio.) |
| dado que (loc) | Não aprovada | Use: PORQUE (conj) | O serviço parou porque o disco está cheio. | Dado que o disco está cheio, o serviço parou. |
| DANIFICADO (adj) | Aprovada | Que tem um dano e não funciona corretamente. | Substitua o disco danificado. | — |
| DANO (s) | Aprovada | Alteração no hardware ou nos dados que faz um item não funcionar corretamente. | Uma falha de energia durante uma operação de escrita causa dano ao disco. | — |
| DAR (v) | Aprovada | Fazer uma pessoa ou um item receber algo. Para uma tarefa, um chamado ou um papel de acesso, use ATRIBUIR. Para um nome, use NOMEAR. | Dê permissão de escrita ao grupo `deploy`. | Dê um restart no serviço. (Use: Reinicie o serviço.) / Dê o chamado ao analista de plantão. (Use: Atribua o chamado ao analista de plantão.) |
| dar continuidade (loc) | Não aprovada | Use: CONTINUAR (v) | Continue a migração depois da aprovação. | Dê continuidade à migração após a aprovação. |
| dar início a (loc) | Não aprovada | Use: INICIAR (v); COMEÇAR (v) | Inicie a sincronização. / A sincronização começa às 03:00 UTC-03:00. | Dê início à sincronização. |
| DATA (s) | Aprovada | Dia, mês e ano. | Digite a data no formato AAAA-MM-DD. | — |
| DE (prep) | Aprovada | Indica a origem, o dono, o conteúdo ou a parte. | Copie o arquivo do servidor de origem. | — |
| DE ACORDO COM (prep) | Aprovada | Da forma que uma regra, um documento ou um valor define. | Configure o firewall de acordo com a política de segurança. | — |
| de forma a (loc) | Não aprovada | Use: PARA (prep) | Configure o cache para diminuir a latência. | Configure o cache de forma a reduzir a latência. |
| de modo que (loc) | Não aprovada | Use: PARA (prep); PORTANTO (conj) | Configure o alerta para enviar um e-mail à equipe. | Configure o alerta de modo que a equipe receba um e-mail. |
| DE NOVO (adv) | Aprovada | Mais uma vez. | Execute o teste de novo. | — |
| DECIDIR (v) | Aprovada | Escolher o que fazer depois de uma análise. | O gerente de incidente decide se a equipe reverte o deploy. | — |
| DECISÃO (s) | Aprovada | Escolha que uma pessoa ou uma equipe faz depois de uma análise. | Registre a decisão no ADR. | — |
| DEFEITO (s) | Aprovada | Erro no código ou no projeto que causa um funcionamento incorreto. | Registre o defeito no rastreador de issues. | — |
| DEFINIR (v) | Aprovada | Dar um valor ou um significado específico a algo. | Defina a variável `PORT` como `8080`. | — |
| deixar (v) | Não aprovada | Use: PERMITIR (v); MANTER (v) | Mantenha o servidor ligado. / O firewall permite a conexão. | Deixe o servidor ligado. / O firewall deixa passar a conexão. |
| dele (pron) | Não aprovada | Reescreva: repita o substantivo | Abra o projeto e verifique o arquivo `README` do projeto. | Abra o projeto e verifique o `README` dele. |
| deletar (v) | Não aprovada | Use: EXCLUIR (v) | Exclua o branch depois do merge. | Delete o branch após o merge. |
| demais (pron) | Não aprovada | Use: OUTRO (pron) | Os outros serviços continuam ativos. | Os demais serviços continuam ativos. |
| demandar (v) | Não aprovada | Use: PRECISAR (v) | A migração precisa de uma janela de manutenção. | A migração demanda uma janela de manutenção. |
| demonstrar (v) | Não aprovada | Use: MOSTRAR (v) | O gráfico mostra que a latência aumentou. | O gráfico demonstra o aumento da latência. |
| DEMORAR (v) | Aprovada | Precisar de um tempo para terminar. | A cópia demora 10 min. | — |
| dentre (prep) | Não aprovada | Use: ENTRE (prep) | Escolha uma região entre as regiões disponíveis. | Escolha uma região dentre as disponíveis. |
| DENTRO DE (prep) | Aprovada | Na parte interna de. | O arquivo de configuração está dentro do contêiner. | Responda dentro de 15 minutos. (Use: Responda em até 15 min.) |
| departamento (s) | Não aprovada | Use: SETOR (s) | O setor de compras aprova o pedido. | O departamento de compras aprova o pedido. |
| DEPENDER (v) | Aprovada | Precisar de outro item para funcionar ou para acontecer. | O serviço de pedidos depende do serviço de pagamento. | — |
| DEPOIS (adv) | Aprovada | Em um momento que começa no fim de outra ação ou de outro evento. | Salve o arquivo. Depois, feche o editor. | — |
| DEPOIS DE (prep) | Aprovada | Em um momento que começa no fim do momento ou do evento indicado. | Teste a aplicação depois do deploy. | — |
| derrubar (v) | Não aprovada | Use: PARAR (v) | Pare o serviço antes da manutenção. | Derrube o serviço antes da manutenção. |
| desabilitar (v) | Não aprovada | Use: DESATIVAR (v) | Desative o login com senha. | Desabilite o login com senha. |
| DESATIVAR (v) | Aprovada | Fazer uma funcionalidade ou uma opção parar de funcionar e continuar neste estado. | Desative a conta do usuário `jsilva`. | — |
| DESBLOQUEAR (v) | Aprovada | Permitir de novo o acesso a algo ou o uso de algo. | Desbloqueie a conta do usuário. | — |
| DESCARTAR (v) | Aprovada | Não aplicar alterações e voltar à última versão que você salvou. | Descarte as alterações locais. | Descarte os discos antigos. (Use: Remova os discos antigos do data center.) |
| descobrir (v) | Não aprovada | Use: ENCONTRAR (v); SABER (v) | Encontre a causa do erro. / Para saber a versão, execute `app --version`. | Descubra a causa do erro. |
| DESCONECTAR (v) | Aprovada | Separar 2 itens conectados. | Desconecte o disco externo. | — |
| DESCONHECIDO (adj) | Aprovada | Que ninguém sabe ou identificou. | A causa do erro é desconhecida. | — |
| DESCREVER (v) | Aprovada | Informar como algo é ou como algo funciona. | Esta seção descreve o fluxo de autenticação. | — |
| DESCRIÇÃO (s) | Aprovada | Texto que informa como algo é ou como algo funciona. | Escreva uma descrição curta do problema. | — |
| DESDE (prep) | Aprovada | Do ponto de início no passado até agora. | O serviço está ativo desde as 08:00 UTC-03:00. | — |
| desde que (loc) | Não aprovada | Use: SE (conj) | Se o teste não falhar, execute o deploy. | Execute o deploy, desde que o teste passe. |
| desejar (v) | Não aprovada | Use: PRECISAR (v) — ou escreva a condição exata | Se você precisar de um relatório em PDF, clique em **Exportar**. | Se desejar um relatório em PDF, clique em **Exportar**. |
| desempenhar (v) | Não aprovada | Use: FAZER (v) — ou verbo específico | O agente coleta as métricas. | O agente desempenha a coleta de métricas. |
| DESEMPENHO (s) | Aprovada | Velocidade e consumo de recursos de um sistema quando o sistema faz uma tarefa. | Esta versão melhora o desempenho do login. | — |
| DESFAZER (v) | Aprovada | Cancelar o efeito de uma ação anterior. | Desfaça a última alteração. | — |
| DESLIGAR (v) | Aprovada | Fazer a energia parar de chegar a um equipamento. | Desligue o servidor antes de substituir o disco. | Desligue o modo de depuração. (Use: Desative o modo de depuração.) |
| dessa forma (loc) | Não aprovada | Use: ASSIM (adv); PORTANTO (conj) | Os dados estão no cache. Portanto, as próximas consultas demoram 5 ms. | Os dados ficam no cache. Dessa forma, a segunda consulta é rápida. |
| destarte (adv) | Não aprovada | Use: PORTANTO (conj) | A chave não é válida. Portanto, a API recusa a requisição. | A chave é inválida. Destarte, a API recusa a requisição. |
| DESTINATÁRIO (s) | Aprovada | Pessoa, equipe ou sistema que recebe uma mensagem. | Adicione a equipe de banco de dados aos destinatários do alerta. | — |
| DESTINO (s) | Aprovada | Lugar ou sistema para onde algo vai. | Informe a pasta de destino. | — |
| DESTRUTIVO (adj) | Aprovada | Que exclui ou altera dados, e não é possível desfazer a alteração sem um backup. | Antes de um comando destrutivo, verifique o alvo do comando. | — |
| DETALHE (s) | Aprovada | Uma pequena parte de uma informação. | Clique em **Detalhes** para ver o log completo. | — |
| DETECTAR (v) | Aprovada | Encontrar um item ou uma condição, em geral de forma automática. | O agente de segurança detecta a vulnerabilidade na imagem. | — |
| DEVER (v) | Aprovada | Precisar fazer algo por causa de uma regra ou de um requisito. Use para requisitos, não para passos de procedimento. | A senha deve ter 12 caracteres ou mais. | O erro deve ser do cache. (Use: Verifique se a causa do erro é o cache.) |
| devidamente (adv) | Não aprovada | Use: CORRETAMENTE (adv) | Verifique se o agente está configurado corretamente. | Verifique se o agente está devidamente configurado. |
| devido a (loc) | Não aprovada | Use: POR CAUSA DE (prep) | O deploy falhou por causa de um teste. | O deploy falhou devido a um teste. |
| DEVOLVER (v) | Aprovada | Enviar um item de novo para a pessoa ou para a equipe que enviou o item. | Se o chamado não tiver a aprovação do gestor, devolva o chamado ao solicitante. | — |
| DIA (s) | Aprovada | Período de 24 h. | O sistema mantém os logs por 30 dias. | — |
| DIAGNÓSTICO (s) | Aprovada | Análise que identifica a causa de um problema. | Registre o resultado do diagnóstico no incidente. | — |
| DIÁRIO (adj) | Aprovada | Que acontece 1 vez por dia. | O backup diário começa às 02:00 UTC-03:00. | — |
| DIFERENÇA (s) | Aprovada | O que faz 2 itens não serem iguais. | O comando `diff` mostra a diferença entre os arquivos. | — |
| DIFERENTE (adj) | Aprovada | Que não é igual. | Use uma senha diferente para cada conta. | — |
| DIFÍCIL (adj) | Aprovada | Que precisa de mais esforço, de mais tempo ou de mais conhecimento que o normal. | Uma frase com 3 condições é difícil de ler. | — |
| DIFICULDADE (s) | Aprovada | Condição que faz uma tarefa ser difícil. | Registre no chamado as dificuldades do procedimento. | — |
| DIMINUIR (v) | Aprovada | Fazer ficar menor em quantidade, em tamanho ou em valor. | Diminua o número de workers para 4. | — |
| DINHEIRO (s) | Aprovada | Valor em uma moeda, por exemplo em reais. | Um pagamento duplicado é uma perda de dinheiro para o cliente. | — |
| DIREÇÃO (s) | Aprovada | Caminho de um lado para outro lado, por exemplo da esquerda para a direita. | A seta indica a direção da ordem: do valor menor para o valor maior. | — |
| DIREITO (adj) | Aprovada | Do lado direito. | Clique no ícone no canto superior direito. | — |
| DIRETO (adj) | Aprovada | Sem um passo, uma pessoa ou um sistema entre a origem e o destino. | O serviço tem uma conexão direta com o banco de dados. | — |
| disparar (v) | Não aprovada | Use: INICIAR (v); ENVIAR (v) | O commit inicia o pipeline. / O sistema envia um e-mail. | O commit dispara o pipeline. / O sistema dispara um e-mail. |
| disponibilizar (v) | Não aprovada | Use: PUBLICAR (v); DAR (v) | Publique a documentação no portal. | Disponibilize a documentação no portal. |
| DISPONÍVEL (adj) | Aprovada | Que é possível usar ou obter no momento em que o leitor precisa do item. | A versão 4.1 está disponível na página de versões. | — |
| dispor de (loc) | Não aprovada | Use: TER (v) | O servidor tem 64 GB de memória. | O servidor dispõe de 64 GB de memória. |
| distinto (adj) | Não aprovada | Use: DIFERENTE (adj) | Use contas diferentes para teste e produção. | Use contas distintas para teste e produção. |
| DISTRIBUIR (v) | Aprovada | Dividir itens ou trabalho entre 2 ou mais destinos. | O balanceador de carga distribui as requisições entre 3 servidores. | — |
| diversos (pron) | Não aprovada | Use: VÁRIOS (pron) | O log tem vários erros: 12 erros em 5 min. | O log possui diversos erros. |
| DIVIDIR (v) | Aprovada | Separar em 2 ou mais partes. | Divida o arquivo em partes de 100 MB. | — |
| DIZER (v) | Aprovada | Ter um conteúdo escrito. O sujeito é um texto, uma regra ou um log. | O log diz que a conexão falhou. | Diga o prazo ao cliente. (Use: Informe o prazo ao cliente.) |
| DOBRO (s) | Aprovada | Quantidade 2 vezes maior que outra quantidade. | Configure o tempo limite com o dobro do p99: 600 ms. | — |
| DOCUMENTAÇÃO (s) | Aprovada | Conjunto dos documentos sobre um produto, um sistema ou um processo. | Publique a documentação no portal. | — |
| DOCUMENTAR (v) | Aprovada | Registrar informações em um texto. | Documente cada passo da recuperação. | — |
| DOCUMENTO (s) | Aprovada | Texto ou arquivo com informações registradas. | Anexe o documento ao chamado. | — |
| DOMINGO (s) | Aprovada | Dia da semana antes da segunda-feira. | A janela de manutenção é no domingo, das 02:00 às 04:00 UTC-03:00. | — |
| DUPLICADO (adj) | Aprovada | Que existe 2 ou mais vezes no mesmo lugar. | Exclua as linhas duplicadas da tabela `clientes`. | — |
| DURAÇÃO (s) | Aprovada | Tempo entre o início e o fim de algo. | A duração máxima da sessão é 8 h. | — |
| DURANTE (prep) | Aprovada | No período de. | Não desligue o equipamento durante a atualização. | — |
| DÚVIDA (s) | Aprovada | Condição em que uma pessoa não sabe se um fato é verdadeiro ou se uma decisão está correta. | Se você tiver dúvida sobre o nível do aviso, use o nível mais alto. | — |

## E

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| E (conj) | Aprovada | Liga palavras ou frases do mesmo tipo. | Pare e inicie o serviço. | — |
| e/ou (conj) | Não aprovada | Use: OU (conj); E (conj) — escolha um | Use o arquivo `.yaml` ou o arquivo `.json`. | Use o arquivo `.yaml` e/ou `.json`. |
| EFEITO (s) | Aprovada | Resultado de uma ação ou de uma alteração. | A alteração tem efeito depois que você reinicia o serviço. | — |
| efetivamente (adv) | Não aprovada | Reescreva: remova a palavra | O cache diminui a latência. | O cache efetivamente reduz a latência. |
| efetivar (v) | Não aprovada | Use: APLICAR (v) | Aplique as alterações. | Efetive as alterações. |
| efetuar (v) | Não aprovada | Use: FAZER (v) — ou verbo específico | Copie os dados para o bucket de backup. | Efetue a cópia dos dados para o bucket de backup. |
| EFICÁCIA (s) | Aprovada | Capacidade de uma ação de obter o resultado planejado. | Verifique a eficácia da ação corretiva na próxima auditoria. | — |
| elaborar (v) | Não aprovada | Use: CRIAR (v); ESCREVER (v) | Escreva o plano de rollback. | Elabore o plano de rollback. |
| ele (pron) | Não aprovada | Use: ESTE (pron) — ou repita o substantivo | Reinicie o serviço. O serviço volta em 10 s. | Reinicie o serviço. Ele volta em 10 segundos. |
| eliminar (v) | Não aprovada | Use: EXCLUIR (v); REMOVER (v) | Exclua os registros iguais. | Elimine os registros duplicados. |
| EM (prep) | Aprovada | Indica lugar, tempo ou estado. | Salve o arquivo em `/etc/app`. | — |
| EM ANDAMENTO (adv) | Aprovada | Depois do início e antes do fim. Use depois de ESTAR. | O deploy está em andamento. Aguarde o fim do deploy. | — |
| em nível de (loc) | Não aprovada | Use: EM (prep) — ou remova a locução | Configure o limite no projeto. | Configure o limite em nível de projeto. |
| em razão de (loc) | Não aprovada | Use: POR CAUSA DE (prep) | O job parou por causa de um erro de memória. | O job parou em razão de um erro de memória. |
| em relação a (loc) | Não aprovada | Use: SOBRE (prep); COMPARAR (v) | Comparada com a versão 1, a versão 2 usa 30% menos memória. | Em relação à versão 1, a versão 2 usa 30% menos memória. |
| EM VEZ DE (prep) | Aprovada | No lugar de. | Use HTTPS em vez de HTTP. | — |
| em virtude de (loc) | Não aprovada | Use: POR CAUSA DE (prep) | A API responde em 3 s por causa do número de requisições. | A API está lenta em virtude do volume de requisições. |
| embora (conj) | Não aprovada | Use: MAS (conj) | O build terminou, mas o tempo de execução aumentou. | Embora o build tenha terminado, o tempo de execução aumentou. |
| empregar (v) | Não aprovada | Use: USAR (v) | Use o modo de leitura. | Empregue o modo somente leitura. |
| EMPRESA (s) | Aprovada | Organização que vende produtos ou serviços. | A empresa mantém os dados dos clientes em data centers do Brasil. | — |
| ENCAMINHAMENTO (s) | Aprovada | Ação de encaminhar um item para outra pessoa ou para outra equipe. | O runbook define o encaminhamento do incidente para a equipe de banco de dados. | — |
| ENCAMINHAR (v) | Aprovada | Enviar algo que você recebeu para outra pessoa, outra equipe ou outro sistema. | Encaminhe o incidente para a equipe de banco de dados. | — |
| encerrar (v) | Não aprovada | Use: TERMINAR (v); PARAR (v); FECHAR (v) | Feche a sessão. / Pare o processo. | Encerre a sessão. / Encerre o processo. |
| ENCONTRAR (v) | Aprovada | Saber onde algo está ou qual é a causa de algo, depois de procurar. | Encontre o processo que usa a porta 80. | — |
| endereçar (v) | Não aprovada | Use: RESOLVER (v) | Resolva os comentários da revisão. | Enderece os comentários do review. |
| ENERGIA (s) | Aprovada | Eletricidade que faz um equipamento funcionar. | Desligue a energia antes de abrir o rack. | — |
| ENGENHARIA (s) | Aprovada | Área de uma empresa que planeja, cria e mantém os produtos de software. | A equipe de engenharia corrige o defeito. | — |
| ENQUANTO (conj) | Aprovada | Durante o tempo em que. | Não feche o terminal enquanto a cópia está em execução. | — |
| então (adv) | Não aprovada | Use: PORTANTO (conj); DEPOIS (adv) | O certificado não é válido. Portanto, o navegador mostra um aviso. | O certificado é inválido, então o navegador mostra um aviso. |
| ENTENDER (v) | Aprovada | Saber o significado ou a causa de algo. | Leia o log para entender a falha. | — |
| ENTRADA (s) | Aprovada | Dados, um documento ou um item que um sistema ou uma etapa de um processo recebe para processar. Para a entrada do dicionário, use o nome técnico (04-termos-tecnicos.md, NT-25). | O script valida cada entrada. / A entrada da etapa 2 é o pedido aprovado. | — |
| ENTRAR (v) | Aprovada | Começar uma sessão em um sistema com as suas credenciais. | Entre no portal com a sua conta da empresa. | Entre na pasta `/etc`. (Use: Vá para a pasta `/etc`.) |
| ENTRE (prep) | Aprovada | No espaço ou no intervalo que separa 2 itens. | Use um valor entre 1 e 100. | — |
| entretanto (conj) | Não aprovada | Use: MAS (conj) | O build terminou, mas o relatório da cobertura de testes não apareceu. | O build terminou; entretanto, o relatório da cobertura de testes não apareceu. |
| ENVIAR (v) | Aprovada | Fazer dados, uma mensagem ou um arquivo ir para um destino. | Envie o relatório para o e-mail da equipe. | — |
| ENVIO (s) | Aprovada | Ação de enviar dados, uma mensagem ou um arquivo. | O envio do relatório acontece às 08:00 UTC. | — |
| EQUIPAMENTO (s) | Aprovada | Item físico de hardware, por exemplo um servidor, um switch ou um disco. | Desligue o equipamento antes da manutenção. | — |
| EQUIPE (s) | Aprovada | Grupo de pessoas que fazem as mesmas tarefas ou que têm o mesmo objetivo. | A equipe de plantão recebe o alerta. | — |
| equivalente (adj) | Não aprovada | Use: IGUAL (adj) | O valor `1024 MiB` é igual ao valor `1 GiB`. | O valor `1024 MiB` é equivalente ao valor `1 GiB`. |
| errado (adj) | Não aprovada | Use: INCORRETO (adj) | O valor da variável está incorreto. | O valor da variável está errado. |
| ERRO (s) | Aprovada | Ação ou resultado incorreto. | O comando retorna o erro 403. | — |
| esclarecer (v) | Não aprovada | Use: EXPLICAR (v) | Explique a causa do erro no chamado. | Esclareça a causa do erro no chamado. |
| ESCOLHER (v) | Aprovada | Decidir qual item usar entre 2 ou mais opções. | Escolha a região `sa-east-1`. | — |
| esconder (v) | Não aprovada | Use: OCULTAR (v) | Oculte as colunas sem dados. | Esconda as colunas sem dados. |
| ESCOPO (s) | Aprovada | Conjunto dos itens que um projeto, um documento, uma regra ou uma permissão contém ou afeta. | O escopo do token permite apenas a leitura do repositório. | — |
| ESCREVER (v) | Aprovada | Colocar palavras ou caracteres em um texto ou em um arquivo. | Escreva a causa do incidente no relatório. | — |
| ESCRITA (s) | Aprovada | Ação de escrever um texto. Para dados, use GRAVAÇÃO (s) ou os nomes técnicos "operação de escrita" e "permissão de escrita" (04-termos-tecnicos.md). | Revise a escrita do runbook com outro redator antes da aprovação. | A escrita no disco falhou. (Use: A gravação no disco falhou.) |
| ESFORÇO (s) | Aprovada | Quantidade de trabalho que uma tarefa precisa. | Estime o esforço da migração em dias úteis. | — |
| esgotar (v) | Não aprovada | Reescreva: escreva o valor do recurso | O processo usa 100% da memória do servidor. | O processo esgota a memória do servidor. |
| ESPAÇO (s) | Aprovada | Quantidade de memória ou de disco livre para uso. | Libere espaço em disco. | — |
| ESPECÍFICO (adj) | Aprovada | Que é apenas para um item ou para uma condição. | Use uma tag específica para cada versão. | — |
| ESPERADO (adj) | Aprovada | Que é o resultado correto de uma ação, de acordo com o procedimento ou o requisito. Adjetivo com entrada própria (regra D3). | O resultado esperado é o estado `Running`. | — |
| esperar (v) | Não aprovada | Use: AGUARDAR (v); ACEITAR (v); PRECISAR (v) | Aguarde a resposta do servidor. / O campo aceita apenas números. | Espere a resposta do servidor. / O campo espera um número. |
| ESQUERDO (adj) | Aprovada | Do lado esquerdo. | O menu está no lado esquerdo da tela. | — |
| esse (pron) | Não aprovada | Use: ESTE (pron) | Execute este comando. | Execute esse comando. |
| essencial (adj) | Não aprovada | Use: NECESSÁRIO (adj) | O certificado é necessário para a conexão. | O certificado é essencial para a conexão. |
| estabelecer (v) | Não aprovada | Use: DEFINIR (v); CRIAR (v) | Defina um prazo para corrigir o defeito. / A aplicação cliente cria uma conexão com o servidor. | Estabeleça um prazo para a correção. / A aplicação cliente estabelece uma conexão com o servidor. |
| ESTADO (s) | Aprovada | Condição de um sistema ou de um componente em um momento. Em prosa, use ESTADO, não "status". | O comando `systemctl status nginx` mostra o estado `active`. | O status do serviço é Ativo. (Use: O estado do serviço é **Ativo**.) |
| ESTAR (v) | Aprovada | Ter um estado ou uma posição em um momento. | O serviço está ativo. | O sistema vai estar enviando o e-mail. (Use: O sistema vai enviar o e-mail.) |
| ESTÁVEL (adj) | Aprovada | Que não tem alterações frequentes. | Use a versão estável do pacote. | — |
| ESTE (pron) | Aprovada | Indica o item de que o texto fala agora. | Este comando exclui todos os registros. | — |
| ESTIMAR (v) | Aprovada | Calcular um valor antes de saber o valor real. | Estime o tempo da migração. | — |
| ESTIMATIVA (s) | Aprovada | Valor que uma pessoa calcula antes de saber o valor real. | A estimativa da migração é de 3 dias úteis. | — |
| estipular (v) | Não aprovada | Use: DEFINIR (v) | Defina um prazo para a tarefa. | Estipule um prazo para a tarefa. |
| ESTOQUE (s) | Aprovada | Quantidade de um produto que a empresa tem para vender. | A API de estoque retorna 0 quando o produto não está disponível. | — |
| ESTRANGEIRO (adj) | Aprovada | Que é de outro país ou de outra língua. | O PTS-BR não aprova verbos com radical estrangeiro. | — |
| ESTRUTURA (s) | Aprovada | Organização das partes de um item. | O documento mostra a estrutura do repositório. | — |
| ESTRUTURADO (adj) | Aprovada | Que tem um formato fixo de campos e de valores que um programa lê. | Escreva os valores do log em campos estruturados: `banco=pedidos duracao_ms=5000`. | — |
| ETAPA (s) | Aprovada | Parte de um processo, com início e fim definidos. | O pipeline tem 4 etapas. | — |
| etc. (abrev) | Não aprovada | Use: POR EXEMPLO (adv) — ou escreva a lista completa | O agente coleta métricas, por exemplo CPU e memória. | O agente coleta CPU, memória etc. |
| EVENTO (s) | Aprovada | Algo que acontece em um momento e que um sistema pode registrar. | O sistema registra cada evento de login. | — |
| eventualmente (adv) | Não aprovada | Reescreva: escreva a condição e o efeito (02-regras.md, R3.8) | Quando a fila tem mais de 10 000 mensagens, o job falha por tempo limite. | Eventualmente, o job falha por timeout. |
| evidência (s) | Não aprovada | Use: REGISTRO (s) | Anexe ao chamado o registro do teste. | Anexe ao chamado a evidência do teste. |
| evidenciar (v) | Não aprovada | Use: MOSTRAR (v) | O log mostra o erro de conexão. | O log evidencia o erro de conexão. |
| EVITAR (v) | Aprovada | Fazer uma ação para que um evento não aconteça. | Para evitar perda de dados, faça um backup. | — |
| examinar (v) | Não aprovada | Use: ANALISAR (v); VERIFICAR (v) | Analise o dump de memória. | Examine o dump de memória. |
| EXATIDÃO (s) | Aprovada | Qualidade de um valor exato. | Verifique a exatidão do valor total do pedido. | — |
| EXATO (adj) | Aprovada | Sem diferença do valor correto. | Copie o comando exato. | — |
| EXCEÇÃO (s) | Aprovada | Condição em que uma regra não se aplica. Para a exceção de código, use o nome técnico (04-termos-tecnicos.md). | Esta regra tem uma exceção: os literais. | — |
| EXCETO (prep) | Aprovada | Sem contar o item que a frase indica. | Pare todos os serviços, exceto o banco de dados. | — |
| EXCLUIR (v) | Aprovada | Fazer um item não existir mais. O item não volta a existir sem um backup. | Exclua os snapshots com mais de 30 dias. | Exclua o usuário do grupo. (Use: Remova o usuário do grupo.) |
| EXCLUSÃO (s) | Aprovada | Ação de excluir um item. | A exclusão do projeto é permanente. | — |
| exclusivamente (adv) | Não aprovada | Use: APENAS (adv) | A API aceita apenas HTTPS. | A API aceita exclusivamente HTTPS. |
| EXECUÇÃO (s) | Aprovada | Período em que um computador processa um programa ou um comando. | Não altere o arquivo durante a execução do script. | — |
| EXECUTAR (v) | Aprovada | Fazer um computador processar um comando, um script, um programa ou um deploy. | Execute o script `install.sh`. / Execute o deploy. | Execute a revisão do código. (Use: Revise o código.) |
| EXEMPLO (s) | Aprovada | Item que mostra como algo é ou como algo funciona. | O exemplo abaixo mostra uma requisição `GET`. | — |
| exibir (v) | Não aprovada | Use: MOSTRAR (v) | A página mostra os últimos 50 eventos. | A página exibe os últimos 50 eventos. |
| exigir (v) | Não aprovada | Use: PRECISAR (v); DEVER (v) | O acesso ao portal precisa de MFA. | O acesso ao portal exige MFA. |
| EXISTIR (v) | Aprovada | Estar em um lugar ou em um sistema. | Se o arquivo não existir, crie o arquivo. | — |
| experimentar (v) | Não aprovada | Use: TESTAR (v) | Teste a nova configuração no ambiente de homologação. | Experimente a nova configuração em staging. |
| EXPLICAR (v) | Aprovada | Informar a causa ou o funcionamento de algo para uma pessoa entender. | Esta seção explica o modelo de permissões. | — |
| EXPLÍCITO (adj) | Aprovada | Que o texto ou o comando escreve, em vez de usar um valor padrão. | Use a opção `--context` explícita em cada comando `kubectl`. | — |
| EXPOR (v) | Aprovada | Fazer um dado, uma credencial ou um serviço ficar disponível para pessoas ou para sistemas sem permissão. | Um bucket público expõe os dados dos clientes na internet. | — |
| EXPOSIÇÃO (s) | Aprovada | Estado de um dado, de uma credencial ou de um serviço que pessoas sem permissão podem acessar. | A exposição de uma credencial é um incidente de segurança. | — |
| expressar (v) | Não aprovada | Use: INDICAR (v) | O código 0 indica sucesso. | O código 0 expressa sucesso. |
| EXTERNO (adj) | Aprovada | Que está fora de um sistema ou de uma organização. | Não use serviços externos sem aprovação. | — |
| EXTRAIR (v) | Aprovada | Copiar uma parte de um texto, de um arquivo ou de um conjunto de dados para outro lugar. | O script extrai as linhas de erro do log para o arquivo `erros.txt`. | — |

## F

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| FABRICANTE (s) | Aprovada | Empresa que cria e vende um equipamento ou um software. | Instale o driver do fabricante do disco. | — |
| facilitar (v) | Não aprovada | Reescreva: escreva o efeito com um valor | Com o índice, a consulta demora 40 ms em vez de 900 ms. | O índice facilita a consulta. |
| facilmente (adv) | Não aprovada | Reescreva: remova a palavra | Restaure o backup com o comando `restore`. | Restaure facilmente o backup com o comando `restore`. |
| FAIXA (s) | Aprovada | Conjunto de valores entre um valor mínimo e um valor máximo. | Use uma porta da faixa 8000 a 8999. | — |
| FALHA (s) | Aprovada | Condição em que um sistema ou um componente não funciona corretamente. | Uma falha no disco parou o banco de dados. | — |
| FALHAR (v) | Aprovada | Não ter sucesso em uma ação, em uma operação ou em um teste. | Se o teste falhar, pare o deploy. | — |
| FALSO (adj) | Aprovada | Que não é verdadeiro. | O alerta é falso. O serviço está ativo. | — |
| FALTAR (v) | Aprovada | Não existir ou não estar no lugar em que precisa estar. | Falta o arquivo `config.yaml` na pasta `/etc/app`. | — |
| FASE (s) | Aprovada | Parte de um processo ou de um projeto, com início e fim definidos. | A migração tem 3 fases. A fase 2 copia os dados. | — |
| FATO (s) | Aprovada | Informação que uma pessoa pode verificar. | Escreva o fato: o serviço não respondeu em 30 s. | — |
| favor (s) | Não aprovada | Reescreva: use o imperativo | Reinicie o servidor. | Favor reiniciar o servidor. |
| FAZER (v) | Aprovada | Criar um resultado com uma ação. Use apenas quando não existe um verbo mais específico. | Faça um backup do banco. | Faça a verificação do arquivo. (Use: Verifique o arquivo.) |
| fazer com que (loc) | Não aprovada | Use: CAUSAR (v) — ou verbo específico | O erro de memória reinicia o pod. | O erro de memória faz com que o pod reinicie. |
| fazer uso de (loc) | Não aprovada | Use: USAR (v) | Use o modo seguro. | Faça uso do modo seguro. |
| FECHADO (adj) | Aprovada | Que não permite acesso, conexão ou alteração. | A porta 22 está fechada para a internet. | — |
| FECHAR (v) | Aprovada | Fazer um arquivo, uma janela ou uma conexão parar de estar disponível. | Feche a conexão depois da consulta. | — |
| FERIADO (s) | Aprovada | Dia em que a empresa não funciona por causa de uma data oficial. | O prazo de 5 dias úteis não conta os feriados. | — |
| FERRAMENTA (s) | Aprovada | Programa ou objeto que você usa para fazer uma tarefa. | Use a ferramenta de migração do fornecedor. | — |
| FICAR (v) | Aprovada | Começar a estar em um estado novo. Use como verbo de ligação apenas para um estado novo, depois de um evento. | O ícone fica verde quando o serviço inicia. | O arquivo fica na pasta `/etc/app`. (Use: O arquivo está na pasta `/etc/app`.) / O serviço fica ativo das 22:00 às 06:00. (Use: O serviço está ativo das 22:00 às 06:00 UTC-03:00.) |
| FIGURA (s) | Aprovada | Imagem ou gráfico de um documento, com um número e uma legenda. | A figura 2 mostra a arquitetura do serviço. | — |
| FILTRAR (v) | Aprovada | Mostrar ou manter apenas os itens que estão de acordo com uma condição. | Filtre os logs por nível de erro. | — |
| FIM (s) | Aprovada | Último ponto de algo. | Leia o resumo no fim da página. | — |
| FINAL (adj) | Aprovada | Que é o último de uma sequência. | Verifique o resultado final do pipeline. | Faça a verificação final. (Use: Verifique o resultado final.) |
| finalidade (s) | Não aprovada | Use: OBJETIVO (s) | O objetivo do script é limpar o cache. | A finalidade do script é limpar o cache. |
| finalizar (v) | Não aprovada | Use: TERMINAR (v); PARAR (v) | Termine a instalação. / Pare o processo. | Finalize a instalação. / Finalize o processo. |
| finalmente (adv) | Não aprovada | Use: DEPOIS (adv) — ou remova | Depois, reinicie o serviço. | Finalmente, reinicie o serviço. |
| FÍSICO (adj) | Aprovada | Que é um objeto real, não um software. | Desligue o servidor físico antes de substituir o disco. | — |
| FIXAR (v) | Aprovada | Definir uma versão ou um valor que o sistema não altera de forma automática. | Fixe a versão do Vale em 3.27.0 no arquivo do workflow. | — |
| FIXO (adj) | Aprovada | Que tem sempre o mesmo valor ou a mesma posição. | Use um endereço IP fixo para o servidor de banco. | — |
| FLUXO (s) | Aprovada | Sequência de passos ou de dados, do início ao fim. | A seção 3 descreve o fluxo de autenticação. | — |
| FONTE (s) | Aprovada | Documento ou arquivo que contém a informação original ou o texto original. | Escreva a fonte de cada dado do relatório. | — |
| FORA DE (prep) | Aprovada | Na parte externa de um lugar, de um grupo ou de um sistema. | Não armazene senhas fora do cofre de segredos. | — |
| FORMA (s) | Aprovada | Modo como uma ação acontece ou como um item funciona. Para a forma escrita de uma palavra, ver a regra D7. | O pipeline executa os testes de forma automática a cada commit. | A forma da resposta está na seção 4. (Use: A estrutura da resposta está na seção 4.) |
| FORMAL (adj) | Aprovada | Que segue um processo definido e que tem um registro escrito. | A alteração precisa de uma aprovação formal. | — |
| FORMATO (s) | Aprovada | Estrutura e regras de organização de dados. | Use o formato ISO 8601 para datas. | — |
| FÓRMULA (s) | Aprovada | Regra com números e operações que calcula um valor a partir de outros valores. | A fórmula da taxa de erro é: erros / requisições × 100. | — |
| FORNECEDOR (s) | Aprovada | Empresa que vende um produto ou um serviço a outra empresa. | Peça a licença ao fornecedor. | — |
| FORNECER (v) | Aprovada | Dar algo que outra pessoa ou outro sistema precisa. | O provedor de nuvem fornece um certificado para o domínio. | — |
| FOTO (s) | Aprovada | Imagem de uma pessoa, de um lugar ou de um item, em um arquivo. | Altere a foto do seu perfil. | — |
| FREQUÊNCIA (s) | Aprovada | Número de vezes que um evento acontece em um período. | Defina a frequência do backup: 1 vez por dia. | — |
| FREQUENTE (adj) | Aprovada | Que acontece 2 ou mais vezes em um período curto. Escreva a frequência com um número (02-regras.md, R6.4). | O erro 503 é frequente: 40 vezes em 1 h. | O erro é frequente. (Use: O erro acontece 40 vezes em 1 h.) |
| frequentemente (adv) | Não aprovada | Reescreva: dê a frequência exata | O job falha 3 vezes por semana. | O job falha frequentemente. |
| FUNCIONALIDADE (s) | Aprovada | Uma capacidade que um software dá ao usuário. | A versão 2.4 tem uma funcionalidade nova: exportar o relatório em PDF. | — |
| FUNCIONAMENTO (s) | Aprovada | Forma como um item funciona. | Esta seção explica o funcionamento do cache. | — |
| FUNCIONAR (v) | Aprovada | Fazer o trabalho esperado. | O backup funciona corretamente. | — |
| fundamental (adj) | Não aprovada | Use: NECESSÁRIO (adj); IMPORTANTE (adj) | O backup é necessário antes da migração. | O backup é fundamental antes da migração. |

## G

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| garantir (v) | Não aprovada | Use: VERIFICAR (v) | Verifique se o backup terminou antes de continuar. | Garanta que o backup tenha terminado antes de prosseguir. |
| genérico (adj) | Não aprovada | Reescreva: reescreva com NÃO (adv) e ESPECÍFICO (adj), ou escreva o nome do item | A mensagem "Erro" não é específica. Escreva a causa e a ação. | A mensagem "Erro" é genérica. |
| GERAL (adj) | Aprovada | Que se aplica a todos os itens ou à maioria dos itens de um grupo. | A seção 2 tem as regras gerais. | — |
| geralmente (adv) | Não aprovada | Use: APROXIMADAMENTE (adv) — ou dê a frequência | O job demora aproximadamente 5 min. | Geralmente, o job demora 5 minutos. |
| GERAR (v) | Aprovada | Fazer existir algo como resultado de um processo. | O pipeline gera um relatório da cobertura de testes. | — |
| GERENCIAR (v) | Aprovada | Controlar a criação, a alteração e a exclusão de itens. | Use o console para gerenciar os usuários. | — |
| gestão (s) | Não aprovada | Reescreva: reescreva com GERENCIAR (v) | A equipe de plataforma gerencia os acessos. | A gestão dos acessos é da equipe de plataforma. |
| GRÁFICO (s) | Aprovada | Imagem que mostra dados com linhas, barras ou áreas. | O gráfico mostra a latência média de cada período de 1 h. | — |
| GRANDE (adj) | Aprovada | Com tamanho ou quantidade maior que o normal. Escreva o valor (02-regras.md, R6.4). | Um arquivo grande, com mais de 10 GB, demora mais de 1 h para copiar. | Arquivos grandes demoram mais para copiar. (Use: Um arquivo de 10 GB demora 1 h para copiar.) |
| GRAVAÇÃO (s) | Aprovada | Ação de gravar dados. | A gravação dos eventos no disco local demora 2 ms. | — |
| GRAVAR (v) | Aprovada | Colocar dados em um disco, em um arquivo ou em um banco de dados, para usar os dados depois. | O agente grava os eventos no disco local. | — |
| GRAVE (adj) | Aprovada | Que faz um serviço parar, que causa uma perda de dados ou que causa um dano a pessoas. | Uma falha grave parou o serviço de pagamento. | — |
| GRUPO (s) | Aprovada | Conjunto de itens ou de pessoas com uma característica comum. | Adicione o usuário ao grupo `devops`. | — |
| guardar (v) | Não aprovada | Use: ARMAZENAR (v); MANTER (v) | Armazene o token no cofre de segredos. | Guarde o token no cofre de segredos. |

## H

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| habilitar (v) | Não aprovada | Use: ATIVAR (v) | Ative o log de auditoria. | Habilite o log de auditoria. |
| haja vista (loc) | Não aprovada | Use: PORQUE (conj) | O job parou porque a fila está vazia. | O job parou, haja vista que a fila está vazia. |
| haver (v) | Não aprovada | Use: EXISTIR (v); TER (v) | O cluster tem 3 réplicas. / Existem 2 opções. | Há três réplicas no cluster. / Há duas opções. |
| HIPÓTESE (s) | Aprovada | Causa possível que a equipe ainda não confirmou. | A hipótese da equipe é: o cache tem dados antigos. Teste a hipótese. | — |
| HISTÓRICO (s) | Aprovada | Lista de eventos ou de alterações em ordem de tempo. | O histórico mostra todas as alterações do arquivo. | — |
| HORA (s) | Aprovada | Momento do dia, no formato `HH:MM` e com o fuso horário (02-regras.md, R8.5). Para uma duração, escreva o número e o símbolo h (R8.4). | Registre a hora do início do incidente: 14:10 UTC-03:00. | O agendador executa o job a cada hora. (Use: O agendador executa o job a cada 1 h.) / Aguarde 1 hora. (Use: Aguarde 1 h.) |
| HORIZONTAL (adj) | Aprovada | Na direção da esquerda para a direita, ou da direita para a esquerda. | Role a tabela na direção horizontal para ver as outras colunas. | — |

## I

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| IDEIA (s) | Aprovada | Plano ou proposta que uma pessoa tem. | Descreva a ideia no chamado. | — |
| IDEMPOTENTE (adj) | Aprovada | Que tem o mesmo resultado se você executar a operação 1 vez ou mais vezes. | O endpoint `PUT /v1/pedidos/{id}` é idempotente. | — |
| idêntico (adj) | Não aprovada | Use: IGUAL (adj) | Os 2 arquivos são iguais. | Os dois arquivos são idênticos. |
| IDENTIFICAR (v) | Aprovada | Saber ou mostrar qual é um item. | Identifique o processo que usa mais memória. | — |
| IDIOMA (s) | Aprovada | Língua de uma interface, de um documento ou de um conteúdo, por exemplo o português ou o inglês. | Altere o idioma da interface para **English**. | — |
| IGNORAR (v) | Aprovada | Não processar um item, por causa de uma regra ou de uma decisão. | O linter ignora o texto dentro de um bloco de código. | — |
| IGUAL (adj) | Aprovada | Com o mesmo valor ou o mesmo conteúdo. | Os 2 hashes são iguais. | — |
| IMEDIATAMENTE (adv) | Aprovada | Sem aguardar. | Revogue a chave imediatamente. | — |
| impactar (v) | Não aprovada | Use: AFETAR (v) | A falha afeta os pagamentos. | A falha impacta os pagamentos. |
| IMPACTO (s) | Aprovada | Efeito de uma alteração ou de uma falha em um sistema ou nas pessoas. | Descreva o impacto da falha para os clientes. | — |
| IMPEDIR (v) | Aprovada | Não permitir que algo aconteça. | O bloqueio impede o acesso ao banco. | — |
| IMPLÍCITO (adj) | Aprovada | Que o texto ou o comando não escreve. O leitor ou o sistema usa um valor que o texto não mostra. | O comando usa o contexto implícito do terminal. Escreva a opção `--context`. | — |
| IMPORTANTE (adj) | Aprovada | Que tem um efeito grande no resultado. | Leia as informações importantes antes de começar. | — |
| imprescindível (adj) | Não aprovada | Use: NECESSÁRIO (adj) | A chave de API é necessária para a requisição. | A chave de API é imprescindível para a requisição. |
| IMPRIMIR (v) | Aprovada | Gerar uma cópia em papel. | Imprima a lista de verificação do deploy. | O script imprime o resultado. (Use: O script mostra o resultado na saída padrão.) |
| INATIVO (adj) | Aprovada | Que não está em funcionamento ou em uso. | Desative as contas inativas. | — |
| incluir (v) | Não aprovada | Use: ADICIONAR (v); CONTER (v) | Adicione o usuário à lista. / O pacote contém o driver. | Inclua o usuário na lista. / O pacote inclui o driver. |
| inclusão (s) | Não aprovada | Use: ADICIONAR (v) | Adicione o usuário ao grupo `deploy`. | Faça a inclusão do usuário no grupo `deploy`. |
| INCOMPATÍVEL (adj) | Aprovada | Que não funciona corretamente com outro item. | A versão 1.8 é incompatível com o esquema da versão 2. | — |
| INCOMPLETO (adj) | Aprovada | Que não tem todas as partes. | O arquivo de backup está incompleto. Gere o backup de novo. | — |
| INCORRETO (adj) | Aprovada | Que não está correto. | A senha está incorreta. | — |
| INDEPENDENTE (adj) | Aprovada | Que não depende de outro item. | Cada microsserviço tem um deploy independente. | — |
| INDICAR (v) | Aprovada | Mostrar um valor ou uma condição. | O código 0 indica sucesso. | — |
| INDIRETO (adj) | Aprovada | Com 1 ou mais passos, pessoas ou sistemas entre a origem e o destino. | A aplicação tem uma dependência indireta da biblioteca `openssl`. | — |
| INDISPONÍVEL (adj) | Aprovada | Que não é possível usar ou obter agora. | O serviço está indisponível desde as 14:00 UTC-03:00. | — |
| INFERIOR (adj) | Aprovada | Que está na parte de baixo. | O botão **Salvar** está no canto inferior direito. | — |
| INFORMAÇÃO (s) | Aprovada | Conteúdo que uma pessoa ou um sistema dá a outra pessoa ou a outro sistema. | Esta seção tem informações sobre limites de uso. | — |
| INFORMAR (v) | Aprovada | Dar uma informação a uma pessoa ou a um sistema. | Informe o número do pedido ao suporte. | — |
| INICIAL (adj) | Aprovada | Que existe ou que acontece no início. | Altere a senha inicial no primeiro login. | — |
| inicialmente (adv) | Não aprovada | Use: PRIMEIRO (num) | Primeiro, faça um backup. | Inicialmente, faça um backup. |
| INICIAR (v) | Aprovada | Fazer um processo, um serviço ou um programa começar a funcionar. | Inicie o serviço `nginx`. | O deploy inicia às 22h. (Use: O deploy começa às 22:00 UTC-03:00.) |
| INÍCIO (s) | Aprovada | Primeiro ponto de algo. | Volte ao início do procedimento. | — |
| inserir (v) | Não aprovada | Use: COLOCAR (v); ADICIONAR (v) — para texto, use o verbo técnico digitar | Coloque o pendrive na porta USB. / Adicione uma linha ao arquivo. | Insira o pendrive na porta USB. / Insira uma linha no arquivo. |
| inspecionar (v) | Não aprovada | Use: ANALISAR (v); VERIFICAR (v) | Analise os cabeçalhos da resposta. | Inspecione os cabeçalhos da resposta. |
| INSTALAÇÃO (s) | Aprovada | Ação de instalar ou o resultado desta ação. | A instalação precisa de acesso à internet. | — |
| INSTALAR (v) | Aprovada | Colocar um programa ou um equipamento em um sistema e preparar o item para uso. | Instale o agente de monitoramento. | — |
| INSTÁVEL (adj) | Aprovada | Que tem resultados ou estados diferentes sem uma causa conhecida. | O teste `test_login` é instável: o teste falha 1 vez a cada 20 execuções. | — |
| INSTRUÇÃO (s) | Aprovada | Frase no imperativo que informa uma ação ao leitor. Para o texto que o leitor digita no terminal, use o nome técnico "comando" (04-termos-tecnicos.md). | Siga as instruções do arquivo `README.md`. | Execute a instrução `kubectl apply`. (Use: Execute o comando `kubectl apply`.) |
| INTERAÇÃO (s) | Aprovada | Ação de uma pessoa com um elemento de interface. | O painel registra cada interação do usuário com o formulário. | — |
| INTERNO (adj) | Aprovada | Que está dentro de um sistema ou de uma organização. | Use o servidor DNS interno. | — |
| interpretação (s) | Não aprovada | Reescreva: reescreva com ENTENDER (v) | O leitor entende a frase de uma única forma. | A frase tem uma única interpretação. |
| interpretar (v) | Não aprovada | Use: ENTENDER (v) | O leitor entende a mensagem sem ajuda. | O leitor interpreta a mensagem sem ajuda. |
| interromper (v) | Não aprovada | Use: PARAR (v); PAUSAR (v) | Pare a sincronização. | Interrompa a sincronização. |
| interrupção (s) | Não aprovada | Reescreva: reescreva com PARAR (v), ou use o nome técnico "indisponibilidade" | O serviço de pagamentos parou por 12 min. | A interrupção do serviço de pagamentos durou 12 min. |
| INTERVALO (s) | Aprovada | Tempo entre 2 eventos. | Defina um intervalo de 30 s entre as tentativas. | — |
| INVÁLIDO (adj) | Aprovada | Que não está de acordo com as regras e que o sistema não aceita. | A API retorna o código 400 se o JSON for inválido. | — |
| invisível (adj) | Não aprovada | Reescreva: reescreva com NÃO (adv) e VISÍVEL (adj) | O campo não está visível para o usuário. | O campo está invisível para o usuário. |
| IR (v) | Aprovada | Mover para outro lugar, também na interface ou no sistema de arquivos. Nota: "vai" + infinitivo é o futuro aprovado (02-regras.md, R3.1), uma forma verbal e não outro significado de IR (regra D2). | Vá para a pasta `/var/log`. | O script irá criar a tabela. (Use: O script vai criar a tabela.) |
| IRREVERSÍVEL (adj) | Aprovada | Que não é possível desfazer. | A exclusão do bucket é irreversível. | — |
| isso (pron) | Não aprovada | Use: ESTE (pron) — com o substantivo | Este erro acontece quando o disco está cheio. | Isso acontece quando o disco está cheio. |
| isto é (loc) | Não aprovada | Reescreva: divida a frase em 2 frases | O job é idempotente. O agendador pode executar o job 2 vezes sem erro. | O job é idempotente, isto é, pode rodar duas vezes sem erro. |
| ITEM (s) | Aprovada | Cada uma das partes de uma lista ou de um conjunto. | Escolha um item da lista. | — |

## J

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| JÁ (adv) | Aprovada | Antes deste momento. | O pacote já está instalado. | — |
| já que (loc) | Não aprovada | Use: PORQUE (conj) | O build falhou porque uma dependência não está instalada. | Já que falta uma dependência, o build falhou. |
| jogar (v) | Não aprovada | Use: COLOCAR (v); MOVER (v) | Mova o arquivo para a pasta `/tmp`. | Jogue o arquivo na pasta `/tmp`. |
| JUNTAR (v) | Aprovada | Colocar 2 ou mais itens no mesmo lugar ou no mesmo conjunto. | Junte os arquivos de log em um arquivo ZIP. | — |
| JUNTO (adj) | Aprovada | Que funciona ou está com outro item ao mesmo tempo. | Os 3 nós funcionam juntos como um sistema. | — |
| junto a (loc) | Não aprovada | Use: COM (prep) | Verifique o prazo com o fornecedor. | Verifique o prazo junto ao fornecedor. |
| JURÍDICO (adj) | Aprovada | Que é sobre leis, contratos ou normas oficiais. | A equipe jurídica aprova o texto do contrato. | — |
| JUSTIFICAR (v) | Aprovada | Explicar por que uma decisão ou uma ação é necessária. | Justifique a exceção no chamado. | — |
| JUSTIFICATIVA (s) | Aprovada | Texto que explica por que uma decisão ou uma ação é necessária. | Escreva a justificativa da alteração na solicitação de mudança. | — |

## L

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| LADO (s) | Aprovada | Uma das partes de algo, à direita ou à esquerda. | O menu está no lado esquerdo da tela. | — |
| LEGADO (adj) | Aprovada | Que é de uma versão ou de uma tecnologia anterior, e que a empresa ainda usa. | O sistema legado de pedidos usa o Java 8. | — |
| LEITURA (s) | Aprovada | Ação de obter dados ou de ler um texto. | O grupo `auditoria` tem permissão de leitura. | — |
| lembrar (v) | Não aprovada | Reescreva: escreva a ação no imperativo | Salve o arquivo antes de fechar o editor. | Lembre-se de salvar o arquivo antes de fechar o editor. |
| LENTO (adj) | Aprovada | Que precisa de mais tempo que o normal. Escreva o valor (02-regras.md, R6.4). | A consulta está lenta: 8 s, em vez de 200 ms. | — |
| LER (v) | Aprovada | Obter o conteúdo de um texto ou de uma fonte de dados. | Leia o arquivo `README`. / O serviço lê a configuração no início. | — |
| levantar (v) | Não aprovada | Use: IDENTIFICAR (v); INICIAR (v) | Identifique os requisitos. / Inicie o serviço. | Levante os requisitos. / Levante o serviço. |
| levar (v) | Não aprovada | Use: DEMORAR (v); MOVER (v) | A cópia demora 10 min. | A cópia leva 10 minutos. |
| lhe (pron) | Não aprovada | Use: VOCÊ (pron) — ou reescreva | Com esta opção, você pode filtrar os logs. | Esta opção lhe permite filtrar os logs. |
| LIBERAR (v) | Aprovada | Fazer um recurso ficar disponível de novo. | Libere espaço em disco. | Libere a versão para produção. (Use: Execute o deploy da versão em produção.) |
| LIGAR (v) | Aprovada | Fornecer energia a um equipamento para que o equipamento comece a funcionar. | Ligue o servidor. | Ligue o modo de depuração. (Use: Ative o modo de depuração.) |
| LIMITAR (v) | Aprovada | Definir um valor máximo para algo. | Limite o número de conexões a 100. | — |
| LIMITE (s) | Aprovada | Valor máximo ou mínimo permitido. | O limite é de 100 requisições por minuto. | — |
| LIMPAR (v) | Aprovada | Remover o conteúdo de um campo, de um cache ou de uma área, sem excluir o item. | Limpe o cache do navegador. | — |
| LINHA (s) | Aprovada | Série horizontal de itens ou de caracteres em uma tabela, em um arquivo ou em uma tela. | Adicione uma linha ao arquivo `hosts`. | — |
| LISTA (s) | Aprovada | Série de itens, um depois do outro. | A lista mostra todos os usuários ativos. | — |
| LISTAR (v) | Aprovada | Mostrar itens em uma lista. | Liste os contêineres em execução. | — |
| LIVRE (adj) | Aprovada | Que não está em uso e que você pode usar. | Verifique o espaço livre em disco. | — |
| LOCAL (adj) | Aprovada | Que está no seu computador ou na sua rede, não em um sistema remoto. | Faça o teste no ambiente local. | — |
| localizar (v) | Não aprovada | Use: ENCONTRAR (v) | Encontre o arquivo de configuração. | Localize o arquivo de configuração. |
| logo (conj) | Não aprovada | Use: PORTANTO (conj) | A fila está cheia. Portanto, os serviços não enviam mais mensagens para a fila. | A fila está cheia, logo o produtor para de enviar. |
| logo que (loc) | Não aprovada | Use: QUANDO (conj) | Quando o build terminar, execute os testes. | Logo que o build terminar, execute os testes. |
| LOJA (s) | Aprovada | Site ou lugar em que uma empresa vende produtos aos clientes. | A loja recebe 2 000 pedidos por dia. | — |
| LONGO (adj) | Aprovada | Com tamanho ou duração maior que o normal. | Divida as frases longas. | — |
| LOTE (s) | Aprovada | Grupo de itens que um sistema processa juntos, em 1 operação. | O job processa os pedidos em lotes de 500 pedidos. | — |
| LUGAR (s) | Aprovada | Ponto ou área onde algo está. | Mantenha o backup em um lugar seguro. | — |

## M

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| MAIOR (adj) | Aprovada | Com mais tamanho, mais quantidade ou mais valor que outro item. | Use um valor maior que 0. | — |
| MAIORIA (s) | Aprovada | A parte maior de um grupo. | A maioria dos erros acontece no módulo de pagamento. | — |
| MAIS (adv) | Aprovada | Em quantidade ou em nível maior. | Adicione mais memória ao nó. | — |
| mandar (v) | Não aprovada | Use: ENVIAR (v) | Envie o log para o suporte. | Mande o log para o suporte. |
| manipular (v) | Não aprovada | Use: ALTERAR (v); USAR (v) | Não altere o arquivo `package-lock.json`. | Não manipule o arquivo `package-lock.json`. |
| MANTER (v) | Aprovada | Fazer algo continuar no mesmo estado ou no mesmo lugar. | Mantenha o servidor ligado durante a cópia. | — |
| MANUAL (adj) | Aprovada | Que uma pessoa faz, sem automação. | A aprovação é manual. | — |
| MANUALMENTE (adv) | Aprovada | Por uma pessoa, sem automação. | Execute o script manualmente. | — |
| MANUTENÇÃO (s) | Aprovada | Trabalho que mantém um sistema funcionando corretamente. | Ative o modo de manutenção antes da migração. | — |
| MARCAR (v) | Aprovada | Colocar um sinal em um item para identificar o item. | Marque o chamado como resolvido. | — |
| MAS (conj) | Aprovada | Indica uma diferença ou um limite ao texto anterior. | O serviço inicia, mas não responde na porta 80. | — |
| matar (v) | Não aprovada | Use: PARAR (v) | Pare o processo com o comando `kill`. | Mate o processo. |
| MATERIAL (s) | Aprovada | Documento ou arquivo que uma pessoa usa para aprender ou para fazer uma tarefa. | Envie o material do treinamento aos participantes. | — |
| MÁXIMO (adj) | Aprovada | O maior valor permitido ou possível. | O tamanho máximo do arquivo é 10 MB. | — |
| mediante (prep) | Não aprovada | Use: COM (prep); DEPOIS DE (prep) | Acesse o sistema com o token. / Execute o deploy depois da aprovação. | Acesse o sistema mediante token. / Execute o deploy mediante aprovação. |
| MEDIDA (s) | Aprovada | Valor que você obtém quando mede algo. | Registre a medida de latência antes da alteração. | — |
| MÉDIO (adj) | Aprovada | Que é a soma dos valores dividida pelo número de valores. | O tempo médio de resposta é 120 ms. | — |
| MEDIR (v) | Aprovada | Obter um valor, por exemplo um tempo ou um tamanho, com uma ferramenta. | Meça o tempo de resposta da API. | — |
| MEIO (s) | Aprovada | Ponto ou parte entre o início e o fim. | Não escreva uma nota no meio de um passo. | — |
| MELHOR (adj) | Aprovada | Que tem mais qualidade que os outros itens de um grupo. | Compare os 2 planos e escolha o melhor. | — |
| MELHORAR (v) | Aprovada | Fazer algo ficar melhor. | Esta versão melhora o desempenho do login. | — |
| MEMBRO (s) | Aprovada | Pessoa ou conta de uma equipe, de um grupo ou de um projeto. | Adicione o analista como membro do projeto. | — |
| mencionado (adj) | Não aprovada | Use: ESTE (pron) | Execute este comando. | Execute o comando mencionado. |
| mencionar (v) | Não aprovada | Use: INFORMAR (v); ESCREVER (v) | Escreva o número do chamado no e-mail. | Mencione o número do chamado no e-mail. |
| MENOR (adj) | Aprovada | Com menos tamanho, menos quantidade ou menos valor que outro item. | Use um valor menor que 1000. | — |
| MENOS (adv) | Aprovada | Em quantidade ou em nível menor. | O índice novo usa menos memória. | — |
| MENSAGEM (s) | Aprovada | Texto que um sistema ou uma pessoa envia ou mostra. | A mensagem de erro mostra o código 500. | — |
| MENSAL (adj) | Aprovada | Que acontece 1 vez por mês. | O relatório mensal mostra a disponibilidade de cada serviço. | — |
| MÊS (s) | Aprovada | Cada um dos 12 períodos de um ano. | O sistema gera o relatório de custo 1 vez por mês. | — |
| MESMO (adj) | Aprovada | Que não é diferente de outro item. | Use a mesma versão em todos os nós. | Abra o arquivo e altere o mesmo. (Use: Abra o arquivo e altere o arquivo.) |
| mesmo que (loc) | Não aprovada | Use: MAS (conj); SE (conj) | O teste falhou, mas o pipeline continuou. | Mesmo que o teste falhe, o pipeline continua. |
| METADE (s) | Aprovada | Uma de 2 partes iguais. | O cluster tem 2 nós. Quando 1 nó falha, o cluster perde metade da capacidade. | — |
| mexer (v) | Não aprovada | Use: ALTERAR (v) | Não altere a configuração do proxy. | Não mexa na configuração do proxy. |
| MÍNIMO (adj) | Aprovada | O menor valor permitido ou possível. | O valor mínimo é 1. | — |
| MINUTO (s) | Aprovada | Período de 60 s. Símbolo depois de um número: min. | O agendador executa o job a cada minuto. | Aguarde 5 minutos. (Use: Aguarde 5 min.) |
| mitigar (v) | Não aprovada | Use: DIMINUIR (v) | Aplique o patch para diminuir o risco. | Aplique o patch para mitigar o risco. |
| MODELO (s) | Aprovada | Estrutura padrão que você usa para criar itens iguais. | Use o modelo de runbook da equipe. | — |
| modificar (v) | Não aprovada | Use: ALTERAR (v) | Altere o arquivo de configuração. | Modifique o arquivo de configuração. |
| MODO (s) | Aprovada | Estado de funcionamento que um usuário ou uma configuração escolhe para um sistema. | O agente tem 2 modos: local e remoto. | — |
| MOEDA (s) | Aprovada | Unidade dos preços e dos pagamentos de um país, por exemplo o real (R$). | Escreva o valor com o símbolo da moeda: R$ 1 500,00. | — |
| MOMENTO (s) | Aprovada | Ponto específico no tempo. | Você pode cancelar a operação a qualquer momento. | — |
| MONITORAMENTO (s) | Aprovada | Ação de monitorar um sistema, sem parar, para encontrar alterações ou problemas. | O monitoramento mostra o consumo de CPU de cada nó. | — |
| MONITORAR (v) | Aprovada | Ver os dados de um sistema durante um tempo para encontrar alterações ou problemas. | Monitore o consumo de CPU por 10 min. | — |
| MOSTRAR (v) | Aprovada | Fazer algo ficar visível para uma pessoa. | A tela mostra o estado da cópia. | — |
| motivo (s) | Não aprovada | Use: CAUSA (s) | Descreva a causa da falha. | Descreva o motivo da falha. |
| MOVER (v) | Aprovada | Fazer um item ir de um lugar para outro. O item não está mais no lugar original. | Mova o log para `/var/archive`. | — |
| mudar (v) | Não aprovada | Use: ALTERAR (v); MOVER (v) | Altere a porta para 8080. / Mova o arquivo para outra pasta. | Mude a porta para 8080. / Mude o arquivo de pasta. |
| muito (adv) | Não aprovada | Reescreva: dê o valor exato; MAIS (adv) | A consulta demora 30 s. | A consulta demora muito. |
| MULTIPLICAR (v) | Aprovada | Calcular o resultado de um número vezes outro número. | Para obter a memória total, multiplique por 8 GiB o número dos nós do cluster. | — |

## N

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| NADA (pron) | Aprovada | Nenhum item. Use com NÃO antes do verbo. | O comando não retorna nada. | — |
| NÃO (adv) | Aprovada | Indica negação. | Não desligue o servidor. | — |
| não obstante (loc) | Não aprovada | Use: MAS (conj) | A migração terminou, mas 3 tabelas têm erros. | Não obstante a migração ter terminado, 3 tabelas têm erros. |
| NATIVO (adj) | Aprovada | Que tem a língua do texto como primeira língua. | O leitor nativo conhece os verbos do português. | — |
| necessariamente (adv) | Não aprovada | Use: DEVER (v) — ou remova | O nome deve começar com uma letra. | O nome necessariamente começa com uma letra. |
| NECESSÁRIO (adj) | Aprovada | Que precisa existir ou acontecer para obter um resultado. | Instale as dependências necessárias. | — |
| NECESSIDADE (s) | Aprovada | O que uma pessoa ou um sistema precisa. | Descreva a necessidade do cliente no chamado. | — |
| necessitar (v) | Não aprovada | Use: PRECISAR (v) | O build precisa do Node.js 20. | O build necessita do Node.js 20. |
| NEGÓCIO (s) | Aprovada | Atividade de uma empresa para vender produtos ou serviços aos clientes. | O requisito de negócio é: o cliente cancela o pedido em até 7 dias. | — |
| NEM (conj) | Aprovada | E também não. | Não pare nem reinicie o banco durante o backup. | — |
| NENHUM (pron) | Aprovada | Nem um único item. | Nenhum teste falhou. | — |
| NINGUÉM (pron) | Aprovada | Nenhuma pessoa. | Ninguém pode alterar o log de auditoria. | — |
| NÍVEL (s) | Aprovada | Posição em uma escala. | Defina o nível de log como `INFO`. | — |
| no entanto (loc) | Não aprovada | Use: MAS (conj) | O serviço respondeu, mas a latência aumentou. | O serviço respondeu. No entanto, a latência aumentou. |
| no que diz respeito a (loc) | Não aprovada | Use: SOBRE (prep) | Esta seção tem as regras sobre senhas. | No que diz respeito a senhas, esta seção tem as regras. |
| no que tange a (loc) | Não aprovada | Use: SOBRE (prep) | Leia a política sobre retenção de dados. | Leia a política no que tange à retenção de dados. |
| no sentido de (loc) | Não aprovada | Use: PARA (prep) | A equipe analisa o log para corrigir o defeito. | A equipe trabalha no sentido de corrigir o defeito. |
| NOME (s) | Aprovada | Palavra ou conjunto de caracteres que identifica um item. | Digite o nome do bucket. | — |
| NOMEAR (v) | Aprovada | Dar um nome a um item. | Nomeie o arquivo de backup com a data: `backup-2026-11-17.sql`. | — |
| NORMA (s) | Aprovada | Documento com regras obrigatórias. | O código segue a norma interna de segurança. | — |
| NORMAL (adj) | Aprovada | De acordo com o estado comum de um sistema. | O consumo de memória está normal: 60%. | — |
| normalmente (adv) | Não aprovada | Use: APROXIMADAMENTE (adv) — ou dê a frequência | O build demora aproximadamente 8 min. | Normalmente, o build demora 8 minutos. |
| nós (pron) | Não aprovada | Reescreva: escreva o sujeito real. Nota: "nós", plural do nome técnico "nó" (04-termos-tecnicos.md, NT-12), é permitido depois de um artigo, de uma contração ou de um número (regra D11). | A equipe de segurança recomenda a versão 2.4. | Nós recomendamos a versão LTS. |
| NOTA (s) | Aprovada | Palavra de sinalização de uma informação a mais, que não é um aviso. Use apenas da forma que 02-regras.md, seção 7, define. | **NOTA:** O comando não altera os dados. | — |
| notificar (v) | Não aprovada | Use: INFORMAR (v); ENVIAR (v) | O sistema envia um e-mail ao responsável. | O sistema notifica o responsável. |
| novamente (adv) | Não aprovada | Use: DE NOVO (adv) | Execute o teste de novo. | Execute o teste novamente. |
| NOVO (adj) | Aprovada | Que começa a existir, a funcionar ou a ser usado depois de outro item ou depois de um evento. Não use para comparar um item com a data do texto (02-regras.md, R9.4). | Crie um token novo. / O Python 3.12 é mais novo que o Python 3.9. | A nova versão corrige o defeito. (Use: A versão 2.4 corrige o defeito.) |
| NUMERADO (adj) | Aprovada | Que tem um número de ordem em cada item. | Escreva os passos em uma lista numerada. | — |
| NÚMERO (s) | Aprovada | Valor que indica uma quantidade ou uma posição. | Informe o número da versão. | — |
| NUNCA (adv) | Aprovada | Em nenhum momento. | Nunca armazene senhas em texto simples. | — |

## O

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| O (art) | Aprovada | Artigo definido masculino. Indica um item conhecido ou que o texto já indicou. | Abra o terminal. | Remova-o. (Use: Remova o arquivo.) |
| o mesmo (pron) | Não aprovada | Use: ESTE (pron) — ou repita o substantivo | Abra o arquivo. Altere a porta no arquivo. | Abra o arquivo e altere a porta no mesmo. |
| o qual (pron) | Não aprovada | Use: QUE (pron) | O servidor que recebe a requisição grava o log. | O servidor, o qual recebe a requisição, grava o log. |
| o senhor (pron) | Não aprovada | Use: VOCÊ (pron) — ou use o imperativo | Você pode cancelar a assinatura no portal. | O senhor pode cancelar a assinatura no portal. |
| objetivar (v) | Não aprovada | Use: OBJETIVO (s) | O objetivo do script é limpar os logs antigos. | O script objetiva limpar os logs antigos. |
| OBJETIVO (s) | Aprovada | Resultado que uma ação ou um processo precisa obter. | O objetivo deste runbook é restaurar o serviço. | — |
| OBRIGAÇÃO (s) | Aprovada | Ação que uma pessoa ou uma empresa deve fazer por causa de uma regra, de uma lei ou de um contrato. | A LGPD cria obrigações para a empresa que processa dados pessoais. | — |
| obrigar (v) | Não aprovada | Use: DEVER (v) | O redator deve escrever a unidade depois de cada número. | A regra obriga o redator a escrever a unidade depois de cada número. |
| obrigatoriamente (adv) | Não aprovada | Use: DEVER (v); OBRIGATÓRIO (adj) | O token deve estar no cabeçalho. / O cabeçalho `Authorization` é obrigatório. | O token obrigatoriamente vai no cabeçalho. |
| OBRIGATÓRIO (adj) | Aprovada | Que você precisa fazer ou usar. | O campo **E-mail** é obrigatório. | — |
| observação (s) | Não aprovada | Use: NOTA (s) | **NOTA:** O limite se aplica a cada usuário. | Observação: o limite vale por usuário. |
| observar (v) | Não aprovada | Use: VER (v); ANALISAR (v) — para "Observe que", use NOTA | Veja a tabela 3. / Analise o gráfico de latência. | Observe a tabela 3. / Observe que o limite é diário. |
| OBSOLETO (adj) | Aprovada | Que ainda existe, mas que não tem mais suporte e que você não deve usar. | A versão 1 da API é obsoleta. Use a versão 2. | — |
| OBTER (v) | Aprovada | Começar a ter algo. | Obtenha o token na página de configurações. | — |
| ocasionar (v) | Não aprovada | Use: CAUSAR (v) | A atualização causa a perda da sessão. | A atualização ocasiona a perda da sessão. |
| OCORRÊNCIA (s) | Aprovada | Cada vez que uma palavra, um termo ou um evento aparece. | Escreva o nome completo da sigla na primeira ocorrência. | — |
| ocorrer (v) | Não aprovada | Use: ACONTECER (v) | O erro acontece às 03:00 UTC-03:00. | O erro ocorre às 03:00. |
| OCULTAR (v) | Aprovada | Fazer algo não estar visível. | Oculte as colunas sem dados. | — |
| OCUPAR (v) | Aprovada | Usar um espaço de memória ou de disco. | O índice ocupa 4 GB. | — |
| OFICIAL (adj) | Aprovada | Que a organização responsável publica ou aprova. | Use a grafia oficial do nome do produto. | — |
| omitir (v) | Não aprovada | Reescreva: reescreva com NÃO (adv) e ESCREVER (v) | Não escreva a senha no chamado. | Omita a senha no chamado. |
| ONDE (adv) | Aprovada | Em que lugar (uma pasta, um servidor ou uma tela). | Escolha a pasta onde o instalador cria os arquivos. | Um cenário onde a rede falha. (Use: Um cenário em que a rede falha.) |
| OPÇÃO (s) | Aprovada | Um dos itens que o usuário pode escolher. | O comando tem 3 opções. | — |
| OPCIONAL (adj) | Aprovada | Que não é obrigatório. | Este passo é opcional. | — |
| OPERAÇÃO (s) | Aprovada | Ação que um sistema faz. | A operação de cópia demora 10 min. | — |
| operacionalizar (v) | Não aprovada | Use: FAZER (v) — ou verbo específico | Configure o processo de backup. | Operacionalize o processo de backup. |
| operar (v) | Não aprovada | Use: USAR (v); CONTROLAR (v) | Use o console para controlar o cluster. | Opere o cluster pelo console. |
| OPINIÃO (s) | Aprovada | O que uma pessoa diz sobre a qualidade de um item, com os próprios critérios. | O questionário registra a opinião de cada participante sobre o treinamento. | — |
| ORDEM (s) | Aprovada | Sequência em que itens ou ações acontecem. | Execute os scripts na ordem abaixo. | O gerente deu a ordem de parar o serviço. (Use: O gerente decidiu parar o serviço.) |
| ORDENAR (v) | Aprovada | Colocar itens em uma ordem definida. | Ordene a lista por data. | O gerente ordenou o rollback. (Use: O gerente decidiu reverter o deploy.) |
| ORGANIZAÇÃO (s) | Aprovada | Grupo de pessoas com estrutura e objetivo comuns, por exemplo uma empresa. | Transfira o repositório para a organização. | — |
| ORGANIZAR (v) | Aprovada | Colocar itens em uma ordem ou em uma estrutura. | Organize os arquivos por projeto. | — |
| ORIGEM (s) | Aprovada | Lugar ou sistema em que um dado, uma requisição ou um item começa. | Verifique o endereço IP de origem. | — |
| ORIGINAL (adj) | Aprovada | Que existe antes de uma cópia ou de uma alteração. | Copie o arquivo. O arquivo original continua na pasta `/etc`. | — |
| otimizar (v) | Não aprovada | Use: MELHORAR (v) | Crie um índice para melhorar a consulta. | Crie um índice para otimizar a consulta. |
| OU (conj) | Aprovada | Indica uma alternativa entre itens. | Use o arquivo `.yaml` ou o arquivo `.json`. | — |
| ou seja (loc) | Não aprovada | Reescreva: divida a frase em 2 frases | O tempo limite é 30 s. Depois deste tempo, a aplicação cliente cancela a requisição. | O timeout é de 30 segundos, ou seja, a aplicação cliente desiste depois disso. |
| OUTRO (pron) | Aprovada | Diferente do item de que o texto fala. | Use outro nome de usuário. | — |
| outrossim (adv) | Não aprovada | Use: TAMBÉM (adv) | O script também atualiza o índice. | Outrossim, o script atualiza o índice. |

## P

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| PADRÃO (s) | Aprovada | Valor ou modelo que um sistema usa quando ninguém define outro. | O valor padrão é 30 s. | Siga o padrão da empresa. (Use: Siga a norma da empresa.) |
| PAGAMENTO (s) | Aprovada | Transferência de dinheiro de um cliente para uma empresa. | O serviço de pagamento confirma cada pagamento em até 2 s. | — |
| PAÍS (s) | Aprovada | Área com leis próprias, por exemplo o Brasil. | A LGPD protege os dados pessoais das pessoas no país. | — |
| pane (s) | Não aprovada | Use: FALHA (s) | Uma falha no roteador parou a rede. | Uma pane no roteador derrubou a rede. |
| PARA (prep) | Aprovada | Indica destino, objetivo ou limite de tempo. | Envie o log para o suporte. | — |
| para que (loc) | Não aprovada | Use: PARA (prep) | Reinicie o serviço para aplicar a alteração. | Reinicie o serviço para que a alteração seja aplicada. |
| parametrizar (v) | Não aprovada | Use: CONFIGURAR (v) | Configure o job com as variáveis de ambiente. | Parametrize o job com as variáveis de ambiente. |
| PARAR (v) | Aprovada | Fazer um processo, um serviço ou um equipamento não funcionar mais. | Pare o serviço antes do backup. | — |
| PARCIAL (adj) | Aprovada | Que tem apenas uma parte. | O backup parcial tem apenas o banco de usuários. | — |
| parcialmente (adv) | Não aprovada | Use: PARCIAL (adj) | O deploy teve um resultado parcial: 2 de 3 nós. | O deploy funcionou parcialmente. |
| PARTE (s) | Aprovada | Um dos itens menores que, juntos, são um item completo. | A primeira parte do guia descreve a instalação. | — |
| PARTICIPANTE (s) | Aprovada | Pessoa que faz parte de uma reunião, de um treinamento ou da resposta a um incidente. | Registre os participantes da reunião na ata. | — |
| PASSO (s) | Aprovada | Uma instrução numerada de um procedimento. | Repita o passo 3. | — |
| PAUSAR (v) | Aprovada | Parar uma operação por um tempo, com a possibilidade de continuar depois. | Pause a sincronização. | — |
| PEDIDO (s) | Aprovada | Mensagem em que uma pessoa pede algo a outra pessoa, a uma equipe ou a um sistema, por exemplo uma compra. Para um pedido de suporte ou de acesso em um sistema de chamados, use o nome técnico "chamado" (04-termos-tecnicos.md, NT-20). | Cada pedido de compra tem um número. | O pedido de acesso precisa da aprovação do gestor. (Use: O chamado de acesso precisa da aprovação do gestor.) |
| PEDIR (v) | Aprovada | Informar a uma pessoa ou a um sistema que você precisa de algo. | Peça acesso ao administrador. | — |
| pegar (v) | Não aprovada | Use: OBTER (v); COPIAR (v) | Obtenha o token no portal. | Pegue o token no portal. |
| PENDENTE (adj) | Aprovada | Que ainda não terminou ou que ainda não tem resposta. | O pedido está pendente. | — |
| PEQUENO (adj) | Aprovada | Com tamanho ou quantidade menor que o normal. Escreva o valor (02-regras.md, R6.4). | Use um disco pequeno, de 20 GB, no ambiente de teste. | Use um disco pequeno. (Use: Use um disco de 20 GB.) |
| PERDA (s) | Aprovada | Condição de não ter mais algo. | Este comando causa a perda dos dados da tabela `sessoes`. | — |
| PERDER (v) | Aprovada | Não ter mais algo. | Se você fechar o editor, você perde as alterações que não salvou. | — |
| perfil de acesso (loc) | Não aprovada | Reescreva: use o nome técnico "papel de acesso" (04-termos-tecnicos.md, NT-16) | Atribua ao usuário o papel de acesso `leitura`. | Atribua ao usuário o perfil de acesso `leitura`. |
| PERGUNTA (s) | Aprovada | Frase que pede uma informação. | Responda às perguntas do formulário de acesso. | — |
| PERGUNTAR (v) | Aprovada | Pedir uma informação a uma pessoa. | Pergunte ao solicitante o número do pedido. | — |
| PERIGO (s) | Aprovada | Palavra de sinalização de aviso. Use apenas da forma que 02-regras.md, seção 7, define. | **PERIGO:** Não escreva a senha do banco de produção no chamado. Todas as pessoas com acesso ao chamado podem ler a senha e acessar os dados dos clientes. | Perigo de lentidão no sistema. (Use: **CUIDADO:** e a consequência com o valor.) |
| PERIGOSO (adj) | Aprovada | Que tem risco de dano ou de perda. | Não execute comandos perigosos em produção sem aprovação. | — |
| PERÍODO (s) | Aprovada | Tempo entre 2 momentos. | Escolha o período do relatório. | — |
| permanecer (v) | Não aprovada | Use: CONTINUAR (v); ESTAR (v) | O serviço continua ativo. | O serviço permanece ativo. |
| PERMANENTE (adj) | Aprovada | Que continua a existir sem limite de tempo. | A exclusão é permanente. | — |
| PERMISSÃO (s) | Aprovada | Direito de acessar ou de alterar um item. | O usuário não tem permissão de escrita. | — |
| PERMITIR (v) | Aprovada | Dar a possibilidade ou o direito de fazer algo. | A regra permite tráfego na porta 443. | — |
| PERSONALIZAR (v) | Aprovada | Alterar algo para as necessidades de uma pessoa ou de uma equipe. | Personalize as colunas do painel. | — |
| PERTENCER (v) | Aprovada | Ser parte de um grupo ou de um conjunto. | O usuário pertence ao grupo `admin`. | — |
| pertinente (adj) | Não aprovada | Use: IMPORTANTE (adj) | Anexe os logs importantes ao chamado. | Anexe os logs pertinentes ao chamado. |
| PERTO DE (prep) | Aprovada | Com uma diferença pequena de um valor ou de um lugar. Escreva o valor (02-regras.md, R6.4). | O consumo de disco está perto do limite: 88%, com o limite de 90%. | — |
| pesquisa (s) | Não aprovada | Reescreva: na interface, use o nome técnico "busca" (04-termos-tecnicos.md, NT-05). Para perguntas a um grupo de pessoas, use QUESTIONÁRIO (s) | Digite o número do pedido no campo de busca. | Digite o número do pedido no campo de pesquisa. |
| pesquisar (v) | Não aprovada | Use: PROCURAR (v) | Procure o ID do pedido no log. | Pesquise o ID do pedido no log. |
| PESSOA (s) | Aprovada | Ser humano. | Uma pessoa precisa aprovar a alteração. | — |
| PESSOAL (adj) | Aprovada | Que é de uma pessoa ou que identifica uma pessoa. | Não use a sua conta pessoal para acessar o banco de produção. | — |
| PICO (s) | Aprovada | Valor máximo de uma métrica em um período. | O pico de tráfego é de 3 000 requisições por segundo, às 20:00 UTC-03:00. | — |
| PLANEJAR (v) | Aprovada | Decidir antes o que fazer e como fazer. | Planeje a janela de manutenção com a equipe. | — |
| PLANILHA (s) | Aprovada | Arquivo com dados em linhas, em colunas e com fórmulas, por exemplo um arquivo do Excel. | Exporte o relatório para uma planilha. | — |
| PLANO (s) | Aprovada | Lista de ações que você decide fazer, em uma ordem. | Escreva o plano de rollback antes do deploy. | — |
| plantonista (s) | Não aprovada | Reescreva: use o nome técnico "analista de plantão" (04-termos-tecnicos.md, NT-19) | Envie um alerta ao analista de plantão. | Acione o plantonista. |
| PODER (v) | Aprovada | Ter a capacidade ou a permissão de fazer algo. | Você pode cancelar a operação a qualquer momento. | O serviço pode falhar. (Use: O serviço falha quando o disco está cheio.) / O serviço poderá parar. (Use: O serviço vai parar às 22:00 UTC-03:00.) |
| pois (conj) | Não aprovada | Use: PORQUE (conj) | Reinicie o pod, porque a equipe alterou a configuração. | Reinicie o pod, pois a configuração mudou. |
| POR (prep) | Aprovada | Indica o caminho, o item que uma ação usa ou a quantidade em cada unidade. | O limite é de 100 requisições por minuto. | — |
| POR CAUSA DE (prep) | Aprovada | Indica a causa de algo. | A fila parou por causa de um erro de permissão. | — |
| por conseguinte (loc) | Não aprovada | Use: PORTANTO (conj) | O certificado não é válido. Portanto, a conexão falha. | O certificado é inválido e, por conseguinte, a conexão falha. |
| POR EXEMPLO (adv) | Aprovada | Indica um item que mostra a regra geral. | Use um formato de texto, por exemplo JSON ou YAML. | — |
| por favor (loc) | Não aprovada | Reescreva: remova (use o imperativo) | Digite a senha. | Por favor, digite a senha. |
| por intermédio de (loc) | Não aprovada | Use: COM (prep) | Envie o arquivo com o comando `sftp`. | Envie o arquivo por intermédio do comando `sftp`. |
| por isso (loc) | Não aprovada | Use: PORTANTO (conj) | O cache está cheio. Portanto, a latência aumentou. | O cache está cheio, por isso a latência aumentou. |
| por meio de (loc) | Não aprovada | Use: COM (prep); POR (prep) | Acesse o banco com a VPN. | Acesse o banco por meio da VPN. |
| PORCENTAGEM (s) | Aprovada | Valor em partes de 100. | O painel mostra a porcentagem de requisições com erro. | — |
| porém (conj) | Não aprovada | Use: MAS (conj) | O pod inicia, mas não fica pronto. | O pod inicia; porém, não fica pronto. |
| porquanto (conj) | Não aprovada | Use: PORQUE (conj) | O deploy parou porque o teste falhou. | O deploy parou, porquanto o teste falhou. |
| PORQUE (conj) | Aprovada | Indica a causa. | O serviço parou porque o disco está cheio. | — |
| PORTANTO (conj) | Aprovada | Indica uma consequência do texto anterior. | O disco está cheio. Portanto, o serviço parou. | — |
| POSIÇÃO (s) | Aprovada | Lugar de um item em relação a outros itens. | Altere a posição da coluna na tabela. | — |
| posicionar (v) | Não aprovada | Use: COLOCAR (v) | Clique no campo **Nome**. | Posicione o cursor no campo **Nome**. |
| possibilitar (v) | Não aprovada | Use: PERMITIR (v) | A opção `--force` permite sobrescrever o arquivo. | A opção `--force` possibilita sobrescrever o arquivo. |
| POSSÍVEL (adj) | Aprovada | Que acontece ou existe em 1 condição ou mais. | Teste todas as entradas possíveis. | — |
| possivelmente (adv) | Não aprovada | Reescreva: escreva o fato que você verificou ou o passo que verifica a causa | Verifique se a causa da falha é o cache. | Possivelmente, a falha é do cache. |
| possuir (v) | Não aprovada | Use: TER (v) | A conta tem 2 usuários administradores. | A conta possui dois usuários administradores. |
| posterior (adj) | Não aprovada | Use: PRÓXIMO (adj); DEPOIS (adv) | A próxima versão vai remover este parâmetro. | Uma versão posterior removerá este parâmetro. |
| posteriormente (adv) | Não aprovada | Use: DEPOIS (adv) | Depois, revise o log. | Posteriormente, revise o log. |
| POUCO (pron) | Aprovada | Uma quantidade pequena de itens. Escreva o número (02-regras.md, R6.4). | Poucos pedidos falharam: 3 de 10 000. | Poucos pedidos falharam. (Use: 3 de 10 000 pedidos falharam.) |
| PRÁTICA (s) | Aprovada | Forma de trabalho que uma equipe usa de forma regular. | A revisão de código é uma prática da equipe. | — |
| praticamente (adv) | Não aprovada | Use: APROXIMADAMENTE (adv) — ou dê o valor exato | O disco está 98% cheio. | O disco está praticamente cheio. |
| PRAZO (s) | Aprovada | Data ou tempo máximo para terminar algo. | O prazo para responder ao pedido é 5 dias úteis. | — |
| PRÉ-REQUISITO (s) | Aprovada | Condição que precisa ser verdadeira antes do início de um procedimento. | Pré-requisito: o usuário tem o papel de acesso `cluster-admin`. | — |
| precedência (s) | Não aprovada | Use: PRIORIDADE (s) | A variável de ambiente tem prioridade sobre o arquivo de configuração. | A variável de ambiente tem precedência sobre o arquivo de configuração. |
| PRECISAR (v) | Aprovada | Ter necessidade de algo. | O instalador precisa de acesso à internet. | — |
| PREÇO (s) | Aprovada | Valor de um produto ou de um serviço para o cliente. | O campo `preco` contém o preço do produto. | — |
| PREENCHER (v) | Aprovada | Colocar dados em todos os campos de um formulário. | Preencha o formulário de pedido de acesso. | — |
| PREFERIDO (adj) | Aprovada | Que a regra ou a equipe escolhe entre 2 ou mais opções. | Use o termo preferido da lista. | — |
| PREPARAR (v) | Aprovada | Fazer o que é necessário antes de uma tarefa. | Prepare o ambiente de teste. | — |
| PRESSIONAR (v) | Aprovada | Aplicar força a uma tecla ou a um botão físico. | Pressione **Enter**. | — |
| previamente (adv) | Não aprovada | Use: ANTES (adv) | Crie o usuário antes. | Crie previamente o usuário. |
| prévio (adj) | Não aprovada | Use: ANTERIOR (adj) | Restaure a configuração anterior. | Restaure a configuração prévia. |
| PREVISÍVEL (adj) | Aprovada | Que acontece da forma esperada, e que o leitor pode saber antes. | O tempo do backup é previsível: 40 min a cada execução. | — |
| previsto (adj) | Não aprovada | Use: PLANEJAR (v) | A equipe planejou a migração para 2026-12-10. | A migração está prevista para 2026-12-10. |
| primeiramente (adv) | Não aprovada | Use: PRIMEIRO (num) | Primeiro, pare o serviço. | Primeiramente, pare o serviço. |
| PRIMEIRO (num) | Aprovada | Que está antes de todos os outros na ordem. | O primeiro passo é fazer um backup. | — |
| PRINCIPAL (adj) | Aprovada | Mais importante entre vários itens. | O arquivo principal da configuração é `config.yaml`. | — |
| principalmente (adv) | Não aprovada | Reescreva: escreva a condição exata | O erro acontece quando o disco está cheio. | O erro acontece principalmente quando o disco está cheio. |
| PRIORIDADE (s) | Aprovada | Nível que define a ordem das tarefas. | Defina a prioridade do chamado. | — |
| PRIORIZAR (v) | Aprovada | Decidir a ordem das tarefas de acordo com o impacto e com o prazo. | Priorize os defeitos críticos. | — |
| PRIVADO (adj) | Aprovada | Que apenas pessoas ou sistemas autorizados podem acessar. | Use uma sub-rede privada para o banco. | — |
| PROBLEMA (s) | Aprovada | Condição que impede o funcionamento correto ou o resultado esperado. | Descreva o problema no chamado. | — |
| proceder (v) | Não aprovada | Use: FAZER (v); CONTINUAR (v) | Continue com o passo 4. | Proceda ao passo 4. |
| PROCEDIMENTO (s) | Aprovada | Série de passos para fazer uma tarefa. | Siga este procedimento para restaurar o banco. | — |
| PROCESSAR (v) | Aprovada | Executar operações com dados para obter um resultado. | O worker processa 100 mensagens por segundo. | — |
| PROCESSO (s) | Aprovada | Série de atividades que gera um resultado a partir de uma entrada. Para o processo do sistema operacional, use o nome técnico (04-termos-tecnicos.md). | O processo de aprovação tem 2 etapas. | — |
| PROCURAR (v) | Aprovada | Tentar encontrar algo. | Procure a mensagem "timeout" no log. | — |
| produzir (v) | Não aprovada | Use: GERAR (v) | O job gera um arquivo CSV. | O job produz um arquivo CSV. |
| PROGRESSO (s) | Aprovada | Parte de uma tarefa que já terminou, como porcentagem do total. | A barra mostra o progresso da cópia: 45%. | — |
| PROIBIR (v) | Aprovada | Não permitir uma ação com uma regra. | A política proíbe senhas com menos de 12 caracteres. | — |
| PROJETO (s) | Aprovada | Trabalho com um objetivo e um prazo definidos, com os arquivos e os recursos deste trabalho. | Organize os arquivos por projeto. | — |
| PRONTO (adj) | Aprovada | Que pode começar o trabalho. | O nó está pronto. O cluster pode enviar pods para o nó. | — |
| propiciar (v) | Não aprovada | Use: PERMITIR (v) | O cache permite respostas em menos de 10 ms. | O cache propicia respostas em menos de 10 ms. |
| propósito (s) | Não aprovada | Use: OBJETIVO (s) | O objetivo deste teste é medir a latência. | O propósito deste teste é medir a latência. |
| PROPOSTA (s) | Aprovada | Texto que descreve uma solução ou uma alteração para outras pessoas decidirem. | Envie a proposta de alteração ao aprovador. | — |
| PRÓPRIO (adj) | Aprovada | Que pertence ao item de que a frase fala. | Cada serviço tem um banco de dados próprio. | — |
| prosseguir (v) | Não aprovada | Use: CONTINUAR (v) | Clique em **Próximo** para continuar. | Clique em **Próximo** para prosseguir. |
| PROTEÇÃO (s) | Aprovada | Ação ou item que protege um sistema, um dado ou uma pessoa. | A proteção do bucket bloqueia o acesso público. | — |
| PROTEGER (v) | Aprovada | Impedir dano, perda ou acesso sem autorização. | Proteja a chave privada com uma senha. | — |
| provavelmente (adv) | Não aprovada | Reescreva: escreva o fato que você verificou ou o passo que verifica a causa | Verifique se a causa do erro é o DNS. | O erro provavelmente é do DNS. |
| prover (v) | Não aprovada | Use: FORNECER (v) | O serviço fornece tokens para as aplicações cliente. | O serviço provê tokens para as aplicações cliente. |
| providenciar (v) | Não aprovada | Use: FAZER (v); OBTER (v); PREPARAR (v) | Obtenha as credenciais de acesso. / Prepare o ambiente. | Providencie as credenciais de acesso. / Providencie o ambiente. |
| provisório (adj) | Não aprovada | Use: TEMPORÁRIO (adj) | Use a senha temporária apenas no primeiro login. | Use a senha provisória apenas no primeiro login. |
| PRÓXIMO (adj) | Aprovada | Que está imediatamente depois na ordem. | Vá para o próximo passo. | O servidor fica próximo ao roteador. (Use: O servidor está ao lado do roteador.) |
| PUBLICAR (v) | Aprovada | Fazer um conteúdo, um pacote ou uma versão ficar disponível para outras pessoas. | Publique o pacote no registry do `npm`. | — |
| PÚBLICO (adj) | Aprovada | Que qualquer pessoa ou qualquer sistema pode acessar. | Não coloque dados pessoais em um bucket público. | — |
| puxar (v) | Não aprovada | Use: OBTER (v) | Obtenha os dados da API. | Puxe os dados da API. |

## Q

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| QUAL (pron) | Aprovada | Indica uma pergunta sobre um item de um grupo. | Verifique qual versão está instalada. | — |
| QUALIDADE (s) | Aprovada | Nível em que um item está de acordo com os requisitos. | A revisão melhora a qualidade do código. | — |
| QUALQUER (pron) | Aprovada | Um item, sem importar qual. | Você pode usar qualquer porta livre. | — |
| QUANDO (conj) | Aprovada | No momento em que. | Quando o disco fica cheio, o serviço não grava os logs. / Quando o build terminar, execute os testes. | — |
| QUANTIDADE (s) | Aprovada | Número ou volume de itens. | Informe a quantidade de réplicas. | — |
| QUARTA-FEIRA (s) | Aprovada | Dia da semana depois da terça-feira. | O aprovador analisa as solicitações de mudança na quarta-feira. | — |
| quase (adv) | Não aprovada | Use: APROXIMADAMENTE (adv) | A fila tem aproximadamente 10 000 mensagens. | A fila tem quase 10 000 mensagens. |
| QUE (conj) | Aprovada | Liga uma frase a verbos como mostrar, indicar e informar. | O log mostra que a conexão falhou. | É necessário que você reinicie o serviço. (Use: Reinicie o serviço.) |
| QUE (pron) | Aprovada | Pronome relativo. Liga uma frase ao substantivo anterior. | Remova o arquivo que o script criou. | — |
| QUEM (pron) | Aprovada | Pronome relativo para uma pessoa ou para uma equipe. | Informe quem executou o deploy. | — |
| questão (s) | Não aprovada | Use: PROBLEMA (s) | Existe um problema no servidor de e-mail. | Há uma questão com o servidor de e-mail. |
| QUESTIONÁRIO (s) | Aprovada | Lista de perguntas que um grupo de pessoas responde. | Cada participante responde ao questionário depois do treinamento. | — |
| QUINTA-FEIRA (s) | Aprovada | Dia da semana depois da quarta-feira. | O backup completo começa na quinta-feira às 01:00 UTC-03:00. | — |

## R

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| rapidamente (adv) | Não aprovada | Use: RÁPIDO (adj); IMEDIATAMENTE (adv) | Com o índice novo, a consulta é mais rápida: 40 ms em vez de 900 ms. | Com o índice novo, a consulta executa rapidamente. |
| RÁPIDO (adj) | Aprovada | Que precisa de pouco tempo. Escreva o valor (02-regras.md, R6.4). | Com o índice, a consulta é mais rápida: 40 ms em vez de 900 ms. | A consulta nova é mais rápida. (Use: A consulta demora 40 ms em vez de 900 ms.) |
| raro (adj) | Não aprovada | Reescreva: dê a frequência exata | O erro acontece 1 vez por mês. | O erro é raro. |
| RASCUNHO (s) | Aprovada | Versão de um texto, de um documento ou de uma mensagem que o autor ainda não publicou nem enviou. | Salve a mensagem como rascunho. | — |
| razão (s) | Não aprovada | Use: CAUSA (s) | Descreva a causa do rollback. | Descreva a razão do rollback. |
| REAL (adj) | Aprovada | Que existe de fato e não é simulado. | Não use dados reais no ambiente de teste. | — |
| realizar (v) | Não aprovada | Use: FAZER (v) — ou verbo específico | Teste a restauração do backup. | Realize o teste de restauração do backup. |
| realmente (adv) | Não aprovada | Reescreva: remova a palavra | O cache diminui a carga do banco. | O cache realmente reduz a carga do banco. |
| recarregar (v) | Não aprovada | Use: ATUALIZAR (v) | Atualize a página. | Recarregue a página. |
| RECEBER (v) | Aprovada | Começar a ter algo que outra pessoa ou outro sistema envia. | O servidor recebe a requisição na porta 443. | — |
| recente (adj) | Não aprovada | Reescreva: escreva a data ou o número da versão (02-regras.md, R9.4) | A versão 2.4 corrige o defeito. | A versão mais recente corrige o defeito. |
| RECOMENDAR (v) | Aprovada | Informar que uma opção é a melhor. | A equipe de segurança recomenda chaves SSH do tipo Ed25519. | — |
| reconhecer (v) | Não aprovada | Use: IDENTIFICAR (v) | O linter identifica as formas do verbo. | O linter reconhece as formas do verbo. |
| RECUPERAÇÃO (s) | Aprovada | Ação de recuperar dados, um item ou o funcionamento de um serviço depois de uma perda ou de uma falha. | A recuperação do serviço de pedidos demorou 40 min. | — |
| RECUPERAR (v) | Aprovada | Ter de novo algo perdido ou excluído. | Recupere o arquivo da lixeira. | — |
| RECUSAR (v) | Aprovada | Não aceitar. | O servidor recusa a conexão. | — |
| REDEFINIR (v) | Aprovada | Definir de novo um valor que já tem um valor, por exemplo com o valor padrão. | Redefina a senha do usuário. / Redefina as configurações com os valores padrão. | — |
| reduzir (v) | Não aprovada | Use: DIMINUIR (v) | Diminua o tamanho da imagem. | Reduza o tamanho da imagem. |
| REESCREVER (v) | Aprovada | Escrever de novo um texto, com outras palavras ou com outra estrutura. | Reescreva a mensagem de erro com a ação que o usuário faz. | — |
| REFERÊNCIA (s) | Aprovada | Nome ou número de outro documento, de outra seção ou de outro item que o texto indica. | A referência completa da API está no anexo B. | — |
| referente a (loc) | Não aprovada | Use: SOBRE (prep) | Leia a nota sobre a versão 3. | Leia a nota referente à versão 3. |
| referido (adj) | Não aprovada | Use: ESTE (pron) | Remova este arquivo. | Remova o referido arquivo. |
| REGISTRAR (v) | Aprovada | Gravar uma informação para usar depois. | O sistema registra cada tentativa de login. | — |
| REGISTRO (s) | Aprovada | Texto ou dado que documenta uma ação, um resultado ou um evento. | Anexe ao chamado o registro da aprovação do gestor. | Exclua o registro 42 da tabela `clientes`. (Use: Exclua a linha 42 da tabela `clientes`.) |
| REGRA (s) | Aprovada | Instrução que define o que é permitido ou obrigatório. | Crie uma regra de firewall para a porta 22. | — |
| REGULAR (adj) | Aprovada | Que acontece sempre da mesma forma, nas mesmas condições. | O comportamento regular do job é: o job termina em 5 min. | — |
| REINICIAR (v) | Aprovada | Parar e iniciar de novo. | Reinicie o servidor de aplicação. | — |
| reinício (s) | Não aprovada | Use: REINICIAR (v) | O comando reinicia todos os pods. Os pods não respondem por 5 min. | O reinício dos pods demora 5 min. |
| reiterar (v) | Não aprovada | Use: REPETIR (v) | Repita o pedido ao fornecedor. | Reitere o pedido ao fornecedor. |
| rejeitar (v) | Não aprovada | Use: RECUSAR (v) | O aprovador recusa o chamado sem a justificativa. | O aprovador rejeita o chamado sem a justificativa. |
| RELAÇÃO (s) | Aprovada | Dependência, ordem ou causa entre 2 ou mais itens. | Descreva a relação entre o alerta e o incidente. | — |
| relativo a (loc) | Não aprovada | Use: SOBRE (prep) | Leia as instruções sobre o firewall. | Leia as instruções relativas ao firewall. |
| RELATÓRIO (s) | Aprovada | Documento que mostra resultados ou dados de um período. | Envie o relatório do incidente em até 48 h. | — |
| relevante (adj) | Não aprovada | Use: IMPORTANTE (adj) | Registre as informações importantes no chamado. | Registre as informações relevantes no chamado. |
| RELÓGIO (s) | Aprovada | Componente ou programa que mantém a data e a hora de um sistema. | Sincronize o relógio do servidor com o NTP. | — |
| REMETENTE (s) | Aprovada | Pessoa ou sistema que envia uma mensagem. | O remetente do alerta é o endereço `alertas@exemplo.com.br`. | — |
| remoção (s) | Não aprovada | Use: REMOVER (v) | Remova o usuário do grupo `admin`. | Faça a remoção do usuário do grupo `admin`. |
| REMOTO (adj) | Aprovada | Que está em outro computador ou em outra rede. | Conecte ao servidor remoto com SSH. | — |
| REMOVER (v) | Aprovada | Fazer um item sair de um lugar, de um grupo ou de um sistema. REMOVER não diz que o item não existe mais (para este significado, use EXCLUIR). | Remova o usuário do grupo `admin`. | Remova o banco de teste. (Use: Exclua o banco de teste.) |
| RENOMEAR (v) | Aprovada | Dar outro nome a um item. | Renomeie o arquivo para `config.old`. | — |
| RENOVAR (v) | Aprovada | Dar a um certificado, a uma licença ou a um token um período de validade novo. | Renove o certificado TLS 30 dias antes do fim da validade. | — |
| REPARAR (v) | Aprovada | Fazer um equipamento danificado funcionar de novo. | O fornecedor repara o disco danificado. | — |
| REPETIR (v) | Aprovada | Fazer de novo. | Repita os passos 2 a 4. | — |
| reportar (v) | Não aprovada | Use: INFORMAR (v) | Informe o defeito no rastreador de issues. | Reporte o defeito no rastreador de issues. |
| representar (v) | Não aprovada | Use: INDICAR (v) | O ícone vermelho indica um serviço com falha. | O ícone vermelho representa um serviço com falha. |
| reprocessamento (s) | Não aprovada | Use: REPROCESSAR (v) | Reprocesse as mensagens da fila de erros. | Faça o reprocessamento das mensagens da fila de erros. |
| REPROCESSAR (v) | Aprovada | Processar de novo dados que o sistema já processou. | Reprocesse as mensagens da fila de erros depois da correção. | — |
| REPRODUZIR (v) | Aprovada | Fazer um erro acontecer de novo para analisar o erro. | Reproduza o erro no ambiente de teste. | — |
| REPROVAR (v) | Aprovada | Decidir que um documento, um código ou uma versão não cumpre os critérios de uma revisão. | O revisor reprova o documento com um desvio S1 sem correção. | — |
| requerer (v) | Não aprovada | Use: PRECISAR (v) | A instalação precisa de permissão de administrador. | A instalação requer permissão de administrador. |
| requisitar (v) | Não aprovada | Use: PEDIR (v) | Peça uma conta de serviço à equipe de plataforma. | Requisite uma conta de serviço à equipe de plataforma. |
| REQUISITO (s) | Aprovada | Condição obrigatória para um sistema, uma tarefa ou uma instalação. | Leia os requisitos de hardware na tabela 2. | — |
| RESERVAR (v) | Aprovada | Separar um recurso para usar depois. | Reserve 20% do disco para os logs. | — |
| resetar (v) | Não aprovada | Use: REDEFINIR (v); REINICIAR (v) | Redefina a senha. / Reinicie o roteador. | Resete a senha. / Resete o roteador. |
| RESOLUÇÃO (s) | Aprovada | Ação de resolver um problema ou um incidente. | Registre a hora da resolução do incidente em UTC. | — |
| RESOLVER (v) | Aprovada | Fazer um problema não existir mais. | Este patch resolve o erro de memória. | — |
| respectivamente (adv) | Não aprovada | Reescreva: reescreva em frases separadas | Defina A como 1. Defina B como 2. | Defina A e B como 1 e 2, respectivamente. |
| RESPONDER (v) | Aprovada | Dar uma resposta a uma pergunta, a uma mensagem ou a uma requisição. | A API responde em menos de 200 ms. | — |
| RESPONSABILIDADE (s) | Aprovada | Tarefa ou resultado que uma pessoa ou uma equipe precisa fazer ou obter. | A responsabilidade do revisor é verificar o texto. | — |
| RESPONSÁVEL (s) | Aprovada | Pessoa ou equipe que faz uma etapa de um processo ou de um procedimento. | O responsável pela etapa 3 é a equipe de banco de dados. | O responsável pelo sistema. (Use: O dono do produto.) |
| RESPOSTA (s) | Aprovada | O que um sistema ou uma pessoa envia depois de receber uma pergunta ou uma requisição. | A resposta tem o código 200. | — |
| ressaltar (v) | Não aprovada | Reescreva: use NOTA (s) | **NOTA:** O backup não contém os logs. | Vale ressaltar que o backup não contém os logs. |
| RESTAURAÇÃO (s) | Aprovada | Ação de restaurar um sistema ou um conjunto de dados. | Teste a restauração do backup 1 vez por mês. | — |
| RESTAURAR (v) | Aprovada | Fazer um sistema ou um conjunto de dados voltar a um estado anterior com uma cópia. | Restaure o banco com o backup de 2026-11-17. | — |
| resto (s) | Não aprovada | Use: OUTRO (pron) | Copie o arquivo 1. Depois, copie os outros arquivos. | Copie o arquivo 1. Depois, copie o resto. |
| RESTRIÇÃO (s) | Aprovada | Regra que limita o que uma pessoa ou um sistema pode fazer. | A política tem uma restrição: a conta de serviço não exclui dados. | — |
| RESULTADO (s) | Aprovada | O que uma ação ou um processo gera. | Compare o resultado com a tabela 3. | — |
| RESUMO (s) | Aprovada | Texto curto com as informações principais. | Escreva um resumo do incidente. | — |
| retirar (v) | Não aprovada | Use: REMOVER (v) | Remova o nó do balanceador de carga. | Retire o nó do balanceador de carga. |
| retorno (s) | Não aprovada | Use: RESPOSTA (s) | Aguarde a resposta do suporte. | Aguarde o retorno do suporte. |
| RETRABALHO (s) | Aprovada | Trabalho que uma pessoa precisa fazer de novo por causa de um erro. | Um requisito incompleto causa retrabalho. | — |
| REUNIÃO (s) | Aprovada | Evento com 2 ou mais pessoas para decidir ou para informar algo. | Informe o assunto na reunião. | — |
| reversibilidade (s) | Não aprovada | Reescreva: reescreva com REVERSÍVEL (adj) | A alteração é reversível? | Qual é a reversibilidade da alteração? |
| REVERSÍVEL (adj) | Aprovada | Que é possível desfazer com um procedimento conhecido. | O deploy é reversível: reverta o deploy com o comando `helm rollback`. | — |
| REVISÃO (s) | Aprovada | Leitura ou análise de algo para encontrar e corrigir erros. | A revisão do código é obrigatória. | — |
| REVISAR (v) | Aprovada | Ler ou analisar algo para encontrar e corrigir erros. | Revise o código antes do merge. | — |
| RISCO (s) | Aprovada | Possibilidade de dano, perda ou falha. | Este comando tem risco de perda de dados. | — |
| rodar (v) | Não aprovada | Use: EXECUTAR (v) | Execute os testes. | Rode os testes. |

## S

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| SÁBADO (s) | Aprovada | Dia da semana depois da sexta-feira. | O analista de plantão responde aos alertas no sábado. | — |
| SABER (v) | Aprovada | Ter uma informação. | Para saber a versão, execute `app --version`. | — |
| SAÍDA (s) | Aprovada | Dados, um documento ou um item que um sistema ou uma etapa de um processo gera como resultado. | Redirecione a saída para um arquivo. / A saída da etapa 2 é o relatório aprovado. | — |
| SAIR (v) | Aprovada | Terminar uma sessão ou fechar um programa. | Saia do portal. / Saia do editor. | — |
| sanar (v) | Não aprovada | Use: RESOLVER (v); CORRIGIR (v) | Resolva o problema de rede. | Sane o problema de rede. |
| SE (conj) | Aprovada | Indica uma condição. | Se o teste falhar, não execute o deploy. | Instala-se o pacote. (Use: Instale o pacote.) |
| SEÇÃO (s) | Aprovada | Parte numerada de um documento. | Leia a seção 3. | — |
| SECRETO (adj) | Aprovada | Que apenas as pessoas ou os sistemas com permissão podem saber. | A chave privada é secreta. | — |
| seguinte (adj) | Não aprovada | Use: PRÓXIMO (adj); ABAIXO (adv) | Execute o comando abaixo. / Vá para o próximo passo. | Execute o seguinte comando. |
| SEGUIR (v) | Aprovada | Fazer uma ação de acordo com uma regra, uma instrução ou uma ordem. | Siga as instruções na tela. | Veja a lista a seguir. (Use: Veja a lista abaixo.) |
| SEGUNDA-FEIRA (s) | Aprovada | Dia da semana depois do domingo. | O relatório semanal chega na segunda-feira às 09:00 UTC-03:00. | — |
| SEGUNDO (s) | Aprovada | Unidade de tempo. Símbolo depois de um número: s. Um minuto tem 60 s. | O sistema mede a latência a cada segundo. | O tempo limite é de 30 segundos. (Use: O tempo limite é 30 s.) / Segundo a documentação, o limite é 10. (Use: De acordo com a documentação, o limite é 10.) / o segundo passo (Use: o passo 2) |
| SEGURANÇA (s) | Aprovada | Proteção contra dano, perda ou acesso sem autorização. | Leia as instruções de segurança. | — |
| SEGURO (adj) | Aprovada | Protegido contra dano, perda ou acesso sem autorização. | Armazene a senha em um lugar seguro. | Você está seguro da alteração? (Use: Confirme a alteração.) |
| SEM (prep) | Aprovada | Indica que um item não faz parte da ação ou do conjunto. | Execute o comando sem a opção `-f`. | — |
| SEMANA (s) | Aprovada | Período de 7 dias. | A equipe revisa os alertas 1 vez por semana. | — |
| SEMANAL (adj) | Aprovada | Que acontece 1 vez por semana. | O backup semanal começa no domingo às 01:00 UTC-03:00. | — |
| SEMELHANTE (adj) | Aprovada | Que tem poucas diferenças de outro item. | O erro é semelhante ao erro do chamado anterior. | — |
| SEMPRE (adv) | Aprovada | Em todas as situações ou em todos os momentos. | Sempre faça um backup antes de uma migração. | — |
| sendo assim (loc) | Não aprovada | Use: PORTANTO (conj) | A réplica secundária tem um atraso de 30 s. Portanto, leia os dados da réplica primária. | A réplica está atrasada. Sendo assim, leia do primário. |
| SEPARAR (v) | Aprovada | Colocar itens em grupos diferentes. | Separe os logs por serviço. | — |
| SEQUÊNCIA (s) | Aprovada | Série de itens ou de ações em uma ordem. | Execute os comandos nesta sequência. | — |
| SER (v) | Aprovada | Indicar a identidade, uma característica fixa ou o valor de um item. | O valor padrão é 30. | A tabela será criada pelo script. (Use: O script vai criar a tabela.) |
| SÉRIE (s) | Aprovada | Conjunto de itens do mesmo tipo, um depois do outro. | O script executa uma série de testes. | — |
| servir (v) | Não aprovada | Reescreva: reescreva com PARA (prep) ou com USAR (v) | Use o arquivo `values-prod.yaml` para o ambiente de produção. | O arquivo `values-prod.yaml` serve para o ambiente de produção. |
| setar (v) | Não aprovada | Use: DEFINIR (v); CONFIGURAR (v) | Defina a variável `NODE_ENV` como `production`. | Sete a variável `NODE_ENV` para production. |
| SETOR (s) | Aprovada | Parte de uma empresa com um objetivo e com um gestor próprios, por exemplo o setor de compras. | O setor de compras aprova o pedido. | — |
| SEU (pron) | Aprovada | Que pertence a você, o leitor. | Digite a sua senha. | O serviço e seu arquivo de log. (Use: O serviço e o arquivo de log do serviço.) |
| SEXTA-FEIRA (s) | Aprovada | Dia da semana depois da quinta-feira. | Não execute deploys em produção na sexta-feira depois das 15:00 UTC-03:00. | — |
| SIGNIFICAR (v) | Aprovada | Ter um significado. O sujeito é uma palavra, uma sigla ou um termo. | A sigla "RTO" significa "objetivo de tempo de recuperação". | O código 0 significa sucesso. (Use: O código 0 indica sucesso.) |
| SIM (adv) | Aprovada | Indica uma resposta afirmativa. | Se a resposta for sim, vá para o passo 4. | — |
| SÍMBOLO (s) | Aprovada | Sinal gráfico que indica um item, uma unidade ou uma operação. | O símbolo # indica um comentário. | — |
| similar (adj) | Não aprovada | Use: SEMELHANTE (adj) | Use uma configuração semelhante à configuração de produção. | Use uma configuração similar à de produção. |
| SIMPLES (adj) | Aprovada | Que tem poucas partes ou poucos passos. | Use frases simples. | — |
| simplesmente (adv) | Não aprovada | Reescreva: remova a palavra | Execute o instalador. | Simplesmente execute o instalador. |
| SIMULAR (v) | Aprovada | Fazer um sistema funcionar como em uma condição real, sem esta condição real. | Simule uma falha de rede no ambiente de teste. | — |
| SINAL (s) | Aprovada | Marca, som ou luz que dá uma informação. | O sinal verde indica que o nó está pronto. | — |
| SISTEMA (s) | Aprovada | Conjunto de componentes que funcionam juntos com um objetivo. | O sistema de pagamento tem 3 serviços. | — |
| SITUAÇÃO (s) | Aprovada | Conjunto dos fatos e das condições de um momento. | Descreva a situação do incidente na primeira mensagem. | — |
| só (adv) | Não aprovada | Use: APENAS (adv) | Apenas o dono do repositório pode excluir o repositório. | Só o dono pode excluir o repositório. |
| SOBRE (prep) | Aprovada | Que tem como assunto. | Este guia tem informações sobre a API de pagamentos. | — |
| solicitar (v) | Não aprovada | Use: PEDIR (v) | Peça acesso ao banco de produção. | Solicite acesso ao banco de produção. |
| SOLTAR (v) | Aprovada | Parar de pressionar um botão ou uma tecla. | Arraste o arquivo até a área **Anexos** e solte o botão do mouse. | — |
| SOLUÇÃO (s) | Aprovada | Ação que resolve um problema. | Descreva a solução no chamado. | — |
| SOMAR (v) | Aprovada | Calcular o total de 2 ou mais números. | Some os minutos de indisponibilidade de cada incidente do mês. | — |
| somente (adv) | Não aprovada | Use: APENAS (adv) | O endpoint aceita apenas o método `POST`. | O endpoint aceita somente POST. |
| startar (v) | Não aprovada | Use: INICIAR (v) | Inicie o worker. | Starte o worker. |
| status (s) | Não aprovada | Use: ESTADO (s) — "status" apenas em literais e no nome técnico "código de status" (04-termos-tecnicos.md) | Verifique o estado do pod. | Verifique o status do pod. |
| subir (v) | Não aprovada | Use: INICIAR (v); ENVIAR (v) — para colocar uma versão em um ambiente, use "executar o deploy" | Inicie o contêiner. / Envie o arquivo para o bucket. | Suba o contêiner. / Suba o arquivo para o bucket. |
| SUBMISSÃO (s) | Aprovada | Primeiro envio de um documento ou de um código para uma revisão. | O linter verifica o documento na submissão do pull request. | — |
| subsequente (adj) | Não aprovada | Use: PRÓXIMO (adj) | O próximo passo cria o índice. | O passo subsequente cria o índice. |
| SUBSTITUIR (v) | Aprovada | Colocar um item no lugar de outro item. | Substitua o certificado antigo. | — |
| SUCESSO (s) | Aprovada | Resultado correto e completo de uma operação. | O comando retorna o código 0 quando a operação tem sucesso. | — |
| SUFICIENTE (adj) | Aprovada | Na quantidade necessária. | Verifique se o disco tem espaço suficiente. | — |
| sugerir (v) | Não aprovada | Use: RECOMENDAR (v) | A ferramenta recomenda um índice para a consulta. | A ferramenta sugere um índice para a consulta. |
| SUPERIOR (adj) | Aprovada | Que está na parte mais alta de uma tela, de uma página ou de um item. | O menu está na parte superior da tela. | — |
| suportar (v) | Não aprovada | Use: ACEITAR (v); COMPATÍVEL (adj) | A API aceita JSON. / O agente é compatível com o Windows Server 2022. | A API suporta JSON. / O agente suporta Windows Server 2022. |
| SUPORTE (s) | Aprovada | Equipe que ajuda os usuários a resolver problemas técnicos. | Envie o log para o suporte. | O sistema dá suporte a arquivos PDF. (Use: O sistema aceita arquivos PDF.) |
| supracitado (adj) | Não aprovada | Use: ESTE (pron) | Execute este script. | Execute o script supracitado. |
| suprimir (v) | Não aprovada | Use: REMOVER (v); OCULTAR (v) | Remova os dados pessoais do log. / Oculte os avisos. | Suprima os dados pessoais do log. / Suprima os avisos. |

## T

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| TABELA (s) | Aprovada | Dados organizados em linhas e colunas em um documento. Para a tabela de banco de dados, use o nome técnico (04-termos-tecnicos.md). | A tabela 2 mostra os limites de cada plano. | — |
| tais como (loc) | Não aprovada | Use: POR EXEMPLO (adv) | Use uma ferramenta de pacotes, por exemplo `npm` ou `pnpm`. | Use um gerenciador de pacotes, tais como npm ou pnpm. |
| tal (pron) | Não aprovada | Use: ESTE (pron) | Se este erro aparecer, reinicie o agente. | Caso tal erro apareça, reinicie o agente. |
| TAMANHO (s) | Aprovada | Medida do espaço que algo ocupa. | O tamanho máximo do arquivo é 50 MB. | — |
| TAMBÉM (adv) | Aprovada | Indica um item a mais, depois de outros itens que o texto já informou. | O pacote também instala a ferramenta de linha de comando. | — |
| TAREFA (s) | Aprovada | Trabalho que uma pessoa ou um sistema precisa fazer. | Atribua a tarefa ao analista de plantão. | — |
| TÉCNICO (adj) | Aprovada | Que é sobre tecnologia ou sobre o funcionamento de um sistema. | A seção 4 tem os detalhes técnicos. | — |
| TECNOLOGIA (s) | Aprovada | Conjunto de ferramentas e de conhecimentos de uma área, por exemplo de TI. | A equipe avalia a tecnologia antes da compra. | — |
| tema (s) | Não aprovada | Use: ASSUNTO (s) | O assunto da reunião é a migração do banco. | O tema da reunião é a migração do banco. |
| TEMPO (s) | Aprovada | Duração de um evento ou de uma ação. | O tempo de resposta é 200 ms. | — |
| temporariamente (adv) | Não aprovada | Use: TEMPORÁRIO (adj) | Use uma senha temporária. | Use uma senha válida temporariamente. |
| TEMPORÁRIO (adj) | Aprovada | Que existe apenas durante um período limitado. | Exclua os arquivos temporários. | — |
| TENDÊNCIA (s) | Aprovada | Forma como um valor aumenta ou diminui durante um período. | O gráfico mostra a tendência do consumo de disco: 2% a mais por semana. | — |
| tendo em vista (loc) | Não aprovada | Use: PORQUE (conj) | Pare a sincronização, porque o disco de destino está cheio. | Tendo em vista que o disco de destino está cheio, pare a sincronização. |
| TENTAR (v) | Aprovada | Fazer algo sem saber se o resultado vai ser o resultado esperado. | Tente a conexão de novo. | — |
| TENTATIVA (s) | Aprovada | Ação de tentar algo. | A aplicação cliente faz 3 tentativas de conexão. | — |
| TER (v) | Aprovada | Conter algo como parte ou como característica. | O cluster tem 3 nós. | Você tem que reiniciar o serviço. (Use: Reinicie o serviço.) |
| TERÇA-FEIRA (s) | Aprovada | Dia da semana depois da segunda-feira. | A janela de manutenção começa na terça-feira às 22:00 UTC-03:00. | — |
| terceiro (num) | Não aprovada | Reescreva: use o número: "o passo 3", "a tentativa 3" | Repita o passo 3. | Repita o terceiro passo. |
| TERMINAR (v) | Aprovada | Chegar ao fim ou fazer algo chegar ao fim. | A cópia termina em 10 min. | — |
| TESTAR (v) | Aprovada | Usar um item em condições controladas para saber se o item funciona. | Teste a restauração do backup. | — |
| TESTE (s) | Aprovada | Procedimento que mostra se algo funciona. | Execute os testes antes do merge. | — |
| TEXTO (s) | Aprovada | Conjunto de palavras escritas. | Escreva o texto da mensagem de erro em PTS-BR. | — |
| time (s) | Não aprovada | Use: EQUIPE (s) | A equipe de plantão recebe o alerta. | O time de plantão recebe o alerta. |
| típico (adj) | Não aprovada | Use: COMUM (adj) | O código de erro mais comum é `401`. | O código de erro típico é `401`. |
| TIPO (s) | Aprovada | Grupo de itens com as mesmas características. | Escolha o tipo de instância. | — |
| tirar (v) | Não aprovada | Use: REMOVER (v) | Remova o nó do cluster. | Tire o nó do cluster. |
| TÍTULO (s) | Aprovada | Nome de um documento, de uma seção ou de uma janela. | Use um título curto para o chamado. | — |
| todavia (conj) | Não aprovada | Use: MAS (conj) | O backup terminou, mas o tamanho é menor que o normal. | O backup terminou; todavia, o tamanho é menor que o normal. |
| TODO (pron) | Aprovada | O conjunto completo, sem exceção. | Pare todos os serviços. | — |
| tornar-se (v) | Não aprovada | Use: FICAR (v) | O certificado fica inválido em 2026-12-01. | O certificado se torna inválido em 2026-12-01. |
| TOTAL (adj) | Aprovada | Que contém todas as partes. | O uso total de disco é 80%. | — |
| totalmente (adv) | Não aprovada | Use: COMPLETO (adj) | A migração está completa. | A migração está totalmente concluída. |
| TRABALHO (s) | Aprovada | Atividade que uma pessoa, uma equipe ou um sistema faz para obter um resultado. | O worker obtém o trabalho da fila. | — |
| TRADUZIR (v) | Aprovada | Escrever um texto em outra língua com o mesmo significado. | Não traduza as mensagens do sistema. | — |
| TRANSFERÊNCIA (s) | Aprovada | Ação de transferir um item. | A transferência do repositório demora 1 min. | — |
| TRANSFERIR (v) | Aprovada | Fazer outra pessoa ou outra conta ficar responsável por um item. | Transfira o repositório para a organização. | — |
| transformar (v) | Não aprovada | Use: CONVERTER (v) | Converta o arquivo para o formato JSON. | Transforme o arquivo em JSON. |
| TRANSIÇÃO (s) | Aprovada | Período em que um sistema, uma versão ou um processo antigo e um novo funcionam ao mesmo tempo. | Durante a transição, os 2 sistemas recebem os pedidos. | — |
| transmitir (v) | Não aprovada | Use: ENVIAR (v) | O servidor envia os dados para a aplicação cliente. | O servidor transmite os dados para a aplicação cliente. |
| tratativa (s) | Não aprovada | Use: AÇÃO (s); SOLUÇÃO (s) | Registre as ações no chamado. | Registre as tratativas no chamado. |
| TRECHO (s) | Aprovada | Parte de um texto, de um código ou de um log. | Copie o trecho do log com o erro para o chamado. | — |
| TREINAMENTO (s) | Aprovada | Atividade em que uma pessoa aprende um trabalho ou uma ferramenta. | O treinamento de segurança é obrigatório para os colaboradores novos. | — |
| TREINAR (v) | Aprovada | Fazer uma pessoa aprender um trabalho ou uma ferramenta. | Treine o analista de plantão novo com o runbook do serviço. | — |
| TRIAGEM (s) | Aprovada | Primeira análise de um chamado ou de um incidente, para definir a prioridade e o responsável. | Na triagem, o analista de plantão define a severidade do incidente. | — |
| TRIMESTRAL (adj) | Aprovada | Que acontece 1 vez por trimestre. | A revisão trimestral dos acessos é obrigatória. | — |
| TRIMESTRE (s) | Aprovada | Período de 3 meses. | A equipe revisa os acessos 1 vez por trimestre. | — |
| trocar (v) | Não aprovada | Use: SUBSTITUIR (v); ALTERAR (v) | Substitua o disco. / Altere a senha. | Troque o disco. / Troque a senha. |
| tu (pron) | Não aprovada | Use: VOCÊ (pron) — ou use o imperativo | Abra o terminal. | Abre o terminal. |
| TUDO (pron) | Aprovada | Todos os itens de um conjunto. | O backup copia tudo da pasta `/data`. | — |

## U

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| ÚLTIMO (adj) | Aprovada | Que está depois de todos os outros, em uma sequência que o texto define. | Desfaça a última alteração. | Instale a última versão estável. (Use: Instale a versão 2.4.1.) |
| UM (art) | Aprovada | Artigo indefinido. Indica um item não específico. Para quantidade, use o algarismo (1). | Crie um usuário. | — |
| uma vez que (loc) | Não aprovada | Use: PORQUE (conj); DEPOIS DE (prep) | O job falhou porque a credencial não é válida. | O job falhou, uma vez que a credencial é inválida. |
| unicamente (adv) | Não aprovada | Use: APENAS (adv) | Use a conta `root` apenas durante um incidente. | Use a conta root unicamente para emergências. |
| ÚNICO (adj) | Aprovada | Que não tem outro igual no mesmo conjunto. | Cada pedido tem um ID único. | — |
| UNIDADE (s) | Aprovada | Quantidade padrão de uma medida. | Informe o tamanho com a unidade, por exemplo 512 MB. | — |
| URGÊNCIA (s) | Aprovada | Necessidade de fazer uma ação em um prazo curto. | A solicitação de mudança tem um destes valores de urgência: normal ou urgente. | — |
| URGENTE (adj) | Aprovada | Que precisa de uma ação imediatamente. | Os incidentes SEV1 são urgentes. | — |
| USAR (v) | Aprovada | Fazer algo funcionar para um objetivo. | Use a opção `--dry-run` para testar. | — |
| USO (s) | Aprovada | Ação de usar um item, uma regra ou um recurso. Para a quantidade de um recurso que um sistema usa, use CONSUMO (s). | Esta seção explica o uso da opção `--dry-run`. | O uso de CPU é 90%. (Use: O consumo de CPU é 90%.) / O uso do comando é simples. (Use: O comando é simples.) |
| utilizar (v) | Não aprovada | Use: USAR (v) | Use o arquivo de exemplo. | Utilize o arquivo de exemplo. |

## V

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| VAGO (adj) | Aprovada | Que não tem um valor ou um significado exato. | A frase "O sistema está lento" é vaga. Escreva o tempo: "A consulta demora 8 s". | — |
| VALER (v) | Aprovada | Ter validade em um período, em uma situação ou em um lugar. | O token vale por 1 h. | — |
| VALIDADE (s) | Aprovada | Período em que algo é válido. | A validade do certificado é de 90 dias. | — |
| VÁLIDO (adj) | Aprovada | Que está de acordo com as regras e que o sistema aceita. | O token é válido por 1 h. | — |
| VALOR (s) | Aprovada | Número, texto ou dado de uma variável, de um campo ou de uma medida. | Defina o valor da variável `TIMEOUT`. | — |
| VARIAR (v) | Aprovada | Ter valores diferentes em momentos ou em situações diferentes. | A latência varia entre 80 ms e 120 ms. | — |
| VÁRIOS (pron) | Aprovada | Mais de 2. Se você sabe o número, escreva o número (02-regras.md, R6.4). | O log tem vários erros de conexão: 12 erros em 5 min. | O log tem vários erros. (Use: O log tem 12 erros de conexão em 5 min.) |
| VAZIO (adj) | Aprovada | Sem conteúdo. | O campo **Nome** está vazio. | — |
| VELOCIDADE (s) | Aprovada | Quantidade de dados ou de ações por unidade de tempo. | A velocidade de cópia é de 100 MB/s. | — |
| VENDER (v) | Aprovada | Dar um produto, ou o uso de um produto, a um cliente pelo pagamento de um valor. | O provedor de nuvem vende o armazenamento por GB. | — |
| VER (v) | Aprovada | Ler uma informação ou identificar um item em uma tela, em um documento ou em um equipamento. | Veja a tabela 2. | Veja se o serviço está ativo. (Use: Verifique se o serviço está ativo.) |
| VERDADEIRO (adj) | Aprovada | Que está de acordo com os fatos. | Se a condição for verdadeira, o pipeline executa o job `deploy`. | — |
| VERDE (adj) | Aprovada | Da cor verde. Em painéis, indica um estado normal. | O ícone verde indica que o serviço está ativo. | — |
| VERIFICAÇÃO (s) | Aprovada | Ação que mostra se uma condição é verdadeira ou se um valor está correto. | A verificação de integridade falhou. | — |
| VERIFICAR (v) | Aprovada | Ver ou medir algo para saber se uma condição é verdadeira ou se um valor está correto. | Verifique se a porta 443 está aberta. | Verifique o log para entender a falha. (Use: Analise o log para entender a falha.) |
| VERMELHO (adj) | Aprovada | Da cor vermelha. Em painéis, indica um estado de erro. | O ícone vermelho indica que o serviço está parado. | — |
| VERSÃO (s) | Aprovada | Estado identificado de um software ou de um documento em um momento. | Atualize para a versão 2.4. | — |
| VERTICAL (adj) | Aprovada | Na direção da parte superior para a parte inferior, ou da parte inferior para a parte superior. | Role a página na direção vertical até a seção **Pagamentos**. | — |
| VEZ (s) | Aprovada | Cada ocorrência de um evento em uma sequência. | A aplicação cliente tenta a conexão 3 vezes. | — |
| via (prep) | Não aprovada | Use: POR (prep); COM (prep) | Acesse o servidor com SSH. | Acesse o servidor via SSH. |
| viabilizar (v) | Não aprovada | Use: PERMITIR (v) | O token permite o acesso à API. | O token viabiliza o acesso à API. |
| viável (adj) | Não aprovada | Use: POSSÍVEL (adj) | A migração em 1 fim de semana é possível. | A migração em 1 fim de semana é viável. |
| VÍDEO (s) | Aprovada | Arquivo com uma sequência de imagens que um programa mostra em ordem. | O vídeo do treinamento tem 20 min. | — |
| vincular (v) | Não aprovada | Use: ASSOCIAR (v) | Associe o domínio ao certificado. | Vincule o domínio ao certificado. |
| visando (v) | Não aprovada | Use: PARA (prep) | Crie réplicas para aumentar a disponibilidade. | Crie réplicas visando aumentar a disponibilidade. |
| VISÍVEL (adj) | Aprovada | Que uma pessoa pode ver. | O botão **Excluir** está visível apenas para administradores. | — |
| visto que (loc) | Não aprovada | Use: PORQUE (conj) | O pod reinicia porque não tem memória livre. | O pod reinicia, visto que a memória se esgota. |
| visualizar (v) | Não aprovada | Use: VER (v); MOSTRAR (v) | Veja os logs no painel. / O painel mostra os logs. | Visualize os logs no painel. |
| VOCÊ (pron) | Aprovada | A pessoa que lê o texto. | Você pode cancelar o processo a qualquer momento. | O usuário deve clicar em Salvar. (Use: Clique em **Salvar**.) |
| VOLTAR (v) | Aprovada | Ir de novo para um lugar ou para um estado anterior. | Volte para a tela anterior. | Volte o deploy. (Use: Reverta o deploy.) |

## Z

| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
|---|---|---|---|---|
| zerar (v) | Não aprovada | Use: REDEFINIR (v); LIMPAR (v) | Redefina a variável `contador` para `0`. | Zere o contador. |

---

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · **03 Dicionário** · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

<!-- rodape -->
Feito com ❤️ em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Alguns direitos reservados.

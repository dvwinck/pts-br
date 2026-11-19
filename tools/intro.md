# 03 — Dicionário controlado

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · **03 Dicionário** · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

PTS-BR — Português Técnico Simplificado, versão 1.0.0, 2026-11-18.
A estrutura do PTS-BR segue a estrutura do ASD-STE100. O PTS-BR não é uma tradução oficial do ASD-STE100, e a ASD não aprovou o PTS-BR.

Este arquivo controla o **vocabulário geral** do PTS-BR. Os nomes técnicos e os verbos técnicos estão em `04-termos-tecnicos.md`.

Conteúdo: {{NA}} palavras aprovadas, {{NN}} palavras não aprovadas com alternativa e {{NO}} palavras obsoletas.

## Sumário

1. [Como ler uma entrada](#1-como-ler-uma-entrada)
2. [Regras de uso do dicionário](#2-regras-de-uso-do-dicionário)
3. [Fronteiras de significado](#3-fronteiras-de-significado)
4. [Verbos-suporte e locuções](#4-verbos-suporte-e-locuções)
5. [Número de entradas](#5-número-de-entradas)
6. Dicionário: {{LETRAS}}

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

{{TABELA_CLASSES}}

---


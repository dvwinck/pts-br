# Guia rápido do PTS-BR 1.0.0

Este guia é um resumo da especificação PTS-BR para as skills do plugin. Os textos completos estão na
pasta `especificacao/`, ao lado deste arquivo:

| Arquivo | Conteúdo |
|---|---|
| `especificacao/02-regras.md` | As 82 regras, cada uma com enunciado, justificativa, verificação e exemplos. |
| `especificacao/03-dicionario.md` | 723 palavras aprovadas (1 significado cada) e 362 não aprovadas (com a alternativa). |
| `especificacao/04-termos-tecnicos.md` | Nomes técnicos (NT-01 a NT-25), 86 siglas de uso geral, glossário e política de termos em inglês. |
| `especificacao/05-governanca.md` | Lista de verificação do revisor (seção 4.2), severidades (4.3) e critério de aprovação (4.4). |
| `especificacao/06-exemplos.md` | 10 textos completos antes e depois. Os exemplos 2 e 9 são modelos de runbook. |

Se este guia e a especificação tiverem um conflito, a especificação tem prioridade.

## 1. O que o PTS-BR controla

O PTS-BR controla o texto em português para o leitor: frases, palavras, procedimentos, avisos e
mensagens. O PTS-BR não altera:

- código, comandos, saídas de terminal, nomes de arquivos, identificadores e valores;
- rótulos de interface e mensagens do sistema citados de forma literal;
- citações e nomes próprios.

## 2. Decisões de base

| Assunto | Decisão |
|---|---|
| Tratamento | "Você" implícito. Nunca "tu", "o senhor" ou "o usuário deve". |
| Passos de procedimento | Imperativo afirmativo: "Remova", "Execute", "Clique". O infinitivo aparece apenas em títulos ("Instalar o agente") e rótulos de botão. |
| Voz | Ativa. Sem passiva sintética ("Instala-se") e sem "se" indeterminado. |
| Tempos verbais | Presente, pretérito perfeito, imperativo, infinitivo e futuro com "vai" + infinitivo. Sem futuro simples ("será") e sem "irá" + infinitivo. |
| Subjuntivo | Apenas em condições com "se" ou "quando" + futuro do subjuntivo ("Se o pod estiver no estado `Pending`, …"). |
| Pronomes | Sem pronome átono e sem mesóclise. Repita o substantivo. Sem "o mesmo" como pronome. |
| Gerúndio | Apenas para ação em andamento. Sem gerundismo ("vamos estar enviando"). |
| Tamanho | Frase de procedimento: até 20 palavras. Frase descritiva: até 25 palavras. Parágrafo: até 6 frases e 1 assunto. |
| Cadeias com "de" | No máximo 3 substantivos: "o arquivo de configuração do servidor". |
| Vocabulário | 1 palavra = 1 significado = 1 classe gramatical. Use apenas palavras aprovadas no 03 e termos técnicos do 04. |
| Termos em inglês | Apenas os termos da lista do 04. Nunca verbos com radical estrangeiro (deployar, commitar, buildar, logar). |

## 3. As 82 regras

A marca `[vale]` indica que o linter encontra parte dos desvios. O revisor verifica todas as regras.

### Seção 1: Palavras
- R1.1 Use apenas palavras aprovadas e termos técnicos. `[vale]`
- R1.2 Use cada palavra apenas com o significado aprovado.
- R1.3 Use cada palavra apenas na classe gramatical aprovada.
- R1.4 Use uma palavra para cada conceito.
- R1.5 Escreva os artigos e o substantivo de classe antes de literais ("o arquivo `settings.json`").
- R1.6 Use a crase apenas antes de palavra feminina com artigo e antes de horas.
- R1.7 Use estrangeirismos apenas da lista de termos técnicos. Não use verbos com radical estrangeiro. `[vale]`
- R1.8 Não use "o mesmo" como pronome. Use "este" e repita o substantivo se o referente for ambíguo. `[vale]`
- R1.9 Use "onde" apenas para lugar. `[vale]`
- R1.10 Não use a forma "para" do verbo PARAR se a frase também tiver a leitura de preposição.

### Seção 2: Cadeias nominais
- R2.1 Use no máximo 3 substantivos em uma cadeia com "de".
- R2.2 Escreva o adjetivo imediatamente depois do substantivo.
- R2.3 Não use a ordem do inglês em substantivos compostos.
- R2.4 Nomeie um conceito longo com um nome curto.

### Seção 3: Verbos
- R3.1 Use apenas presente, pretérito perfeito, "vai" + infinitivo, imperativo, futuro do subjuntivo em condições e infinitivo. `[vale]`
- R3.2 Use o subjuntivo apenas em condições. Escolha a forma da condição pelo tipo de condição.
- R3.3 Use a voz ativa. Voz passiva apenas em texto descritivo, sem autor necessário.
- R3.4 Não use a passiva sintética nem o "se" indeterminado. `[vale]`
- R3.5 Use o verbo, não um verbo-suporte com um substantivo ("Verifique", não "Faça a verificação"). `[vale]`
- R3.6 Use o gerúndio apenas para uma ação em andamento. Sem gerundismo. `[vale]`
- R3.7 Não use pronomes oblíquos átonos nem mesóclise. `[vale]`
- R3.8 Use "poder" e "dever" com um único significado ("pode" = capacidade ou permissão).
- R3.9 Use apenas "ser", "estar" e "ficar" como verbos de ligação.
- R3.10 Use o verbo específico, não um verbo geral.

### Seção 4: Frases
- R4.1 Escreva uma instrução ou uma afirmação por frase.
- R4.2 Máximo de 20 palavras por frase de procedimento e 25 por frase descritiva. `[vale]`
- R4.3 Escreva o sujeito antes do verbo e faça a concordância. Sem "haver". `[vale]`
- R4.4 Escreva o sujeito se o texto tiver mais de um autor de ação.
- R4.5 Use no máximo uma negação por frase.
- R4.6 Use no máximo uma oração subordinada por frase. Sem "o qual" e "cujo".

### Seção 5: Procedimentos
- R5.1 Escreva os passos em uma lista numerada, na ordem de execução. Título no infinitivo.
- R5.2 Use o imperativo nos passos. Sem infinitivo e sem expressões indiretas.
- R5.3 Escreva uma instrução por passo.
- R5.4 Escreva a condição e o local antes da ação. Sem "se necessário".
- R5.5 Escreva o resultado esperado em uma frase separada.
- R5.6 Escreva os pré-requisitos antes do passo 1 ("Antes de começar").
- R5.7 Máximo de 10 passos por procedimento e um nível de sublista.
- R5.8 Escreva os comandos para digitar em blocos de código, com as opções longas (`--namespace`, não `-n`).
- R5.9 Termine com um passo de verificação.
- R5.10 Escreva o responsável do procedimento e de cada etapa.
- R5.11 Escreva cada ponto de decisão com todas as saídas.
- R5.12 Escreva o registro que a etapa gera.
- R5.13 Escreva um procedimento para reverter cada alteração do ambiente de produção.

### Seção 6: Texto descritivo
- R6.1 Comece o parágrafo com a frase principal.
- R6.2 Escreva parágrafos com no máximo 6 frases e um assunto.
- R6.3 Use conectores simples.
- R6.4 Escreva valores, não palavras vagas ("em até 5 min", não "rapidamente").
- R6.5 Use listas e tabelas para itens paralelos.
- R6.6 Não escreva instruções em texto descritivo.

### Seção 7: Avisos de segurança
- R7.1 Use o nível de aviso da consequência mais grave, não da ação (tabela da seção 4 deste guia).
- R7.2 Use NOTA apenas para informação sem risco.
- R7.3 Escreva o aviso na ordem instrução, risco, consequência.
- R7.4 Escreva o aviso antes da ação perigosa.
- R7.5 Escreva um risco por aviso.
- R7.6 Escreva a consequência com o objeto e o efeito.
- R7.7 Marque o aviso apenas com a palavra de sinalização.
- R7.8 Identifique o ambiente antes de um comando que altera ou exclui dados (`--context`, `--kube-context`, `--host`, `--profile`).
- R7.9 Não coloque segredos na linha de comando nem no texto.

### Seção 8: Pontuação e formatação
- R8.1 Termine as frases com ponto final. Sem ponto de exclamação.
- R8.2 Use a vírgula de acordo com a estrutura da frase.
- R8.3 Não use ponto e vírgula, barra entre palavras nem inserções.
- R8.4 Escreva números e unidades em um formato fixo. `[vale]`
- R8.5 Escreva datas no formato ISO 8601 e horas com o fuso horário.
- R8.6 Use maiúsculas apenas no início das frases e em nomes próprios.
- R8.7 Defina as siglas na primeira ocorrência, exceto as siglas de uso geral do 04.
- R8.8 Use cada formato tipográfico com um único significado.
- R8.9 Escreva espaços reservados em um formato único: `<nome-do-servidor>`.

### Seção 9: Práticas de escrita
- R9.1 Escreva para o leitor na forma "você".
- R9.2 Não use linguagem figurada, gíria nem personificação.
- R9.3 Não use palavras vazias, de julgamento ou de cortesia ("simplesmente", "fácil", "por favor").
- R9.4 Escreva referências estáveis. "Acima" e "abaixo" apenas para o elemento ao lado.
- R9.5 Escreva listas completas. Sem "etc.".

### Seção 10: Interface, mensagens e textos de desenvolvimento
- R10.1 Escreva o nome exato do elemento de interface em negrito.
- R10.2 Use o verbo do tipo de elemento (clique em botão, selecione opção, digite em campo).
- R10.3 Escreva caminhos de menu e teclas em um formato fixo.
- R10.4 Escreva a mensagem de erro com o que aconteceu e o que fazer.
- R10.5 Escreva mensagens de erro sem humor e sem culpa.
- R10.6 Escreva rótulos de botão e diálogos de confirmação com o verbo da ação.
- R10.7 Escreva mensagens de andamento e de sucesso curtas.
- R10.8 Escreva textos com variáveis que funcionam com qualquer valor (texto para 0, 1 e 2 ou mais).
- R10.9 Escreva textos de validação, de acessibilidade, de link e de estado vazio com a ação.
- R10.10 Escreva textos de desenvolvimento (commit, pull request, log, comentário) com um formato fixo.

## 4. Níveis de aviso (R7.1)

| Palavra | Consequência mais grave |
|---|---|
| **PERIGO** | Dano sem recuperação: perda de dados sem cópia no backup (também dentro do RPO), dados expostos a pessoas sem permissão, credencial exposta, risco para pessoas. |
| **ATENÇÃO** | Indisponibilidade parcial ou total com recuperação conhecida, exclusão de dados com cópia completa no backup, custo não planejado maior que o limite da equipe. |
| **CUIDADO** | Desempenho menor sem perda de funcionalidade, retrabalho, dano menor. |
| **NOTA** | Nenhum risco. Uma informação que ajuda o leitor no passo. |

Formato: um bloco de citação antes do passo, com a palavra em negrito e a ordem instrução, risco
e consequência:

```markdown
> **PERIGO:** Execute o script `limpar_base.sh` apenas no banco `clientes_hml`. O script exclui
> todas as tabelas do banco. No banco de produção, a equipe perde os dados gravados depois do
> último backup.
```

## 5. Estrutura de um procedimento

1. Título no infinitivo: `### Reiniciar o serviço pagamentos`.
2. Responsável e registro, em procedimentos de processo (R5.10, R5.12).
3. **Antes de começar:** permissões, ferramentas com a versão e o alvo (cluster, banco, conta).
4. Passos numerados, 1 instrução por passo, no máximo 10 passos.
5. Comando em bloco de código logo depois do passo, com as opções longas e o alvo explícito.
6. Resultado esperado em uma frase separada.
7. Cada ponto de decisão com todas as saídas: "Se …, vá para o passo 6. Se …, este procedimento
   termina neste passo: envie o incidente à equipe de banco de dados."
8. Último passo: a verificação.
9. Em produção: o procedimento de reversão, ou a frase que diz que a alteração não tem reversão e
   o plano.

## 6. Números, datas e formatos

- Número com símbolo da unidade: `10 min`, `1 h`, `512 MB`. Separador de milhar com espaço
  (`10 000`) e vírgula decimal (`2,5`). `1 kB` = `1 000 B` e `1 KiB` = `1 024 B`.
- Frequência: `1 vez por dia`.
- Data ISO 8601 (`2026-11-18`). Hora com o fuso horário: `às 14:00 UTC-03:00`.
- Literal (comando, arquivo, valor, saída) em formato de código. Rótulo de interface em
  **negrito**. Valor de estado: em código quando vem de CLI, API ou log (`Running`); em negrito
  quando é rótulo de interface.
- Espaço reservado: `<nome-do-servidor>` (minúsculas, sem acento, com hífen). Depois do bloco de
  código, explique cada espaço reservado.
- Documento novo: declare a versão no cabeçalho, `pts-br: "1.0"`.

## 7. Substituições frequentes

| Não aprovado | Use |
|---|---|
| realizar, efetuar | fazer, ou o verbo específico |
| utilizar | usar |
| rodar | executar |
| deletar, apagar | excluir (ou limpar, para um campo) |
| checar, assegurar, garantir | verificar |
| setar | definir, configurar |
| startar, subir (um serviço) | iniciar |
| resetar, zerar | redefinir, reiniciar, limpar |
| abortar | cancelar, parar |
| visualizar | ver, mostrar |
| possuir | ter |
| necessitar | precisar |
| solicitar | pedir |
| disponibilizar | publicar |
| pegar | obter, copiar |
| através de | com, por |
| devido a | por causa de |
| caso (conjunção) | se |
| diversos | vários |
| só | apenas |
| status (na prosa) | estado |
| evidência | registro |
| há, houve | existir, ter ("O log tem 3 erros.") |
| será, irá executar | vai ser, vai executar |
| simplesmente, basicamente, facilmente | remova a palavra |
| por favor, favor | use o imperativo |

Para qualquer outra palavra, consulte o dicionário:

```shell
grep -i "^| <palavra> (" especificacao/03-dicionario.md
grep -i "<termo>" especificacao/04-termos-tecnicos.md
```

## 8. Linter

O linter em Python 3.9 ou mais novo não precisa de instalação:

```shell
python3 especificacao/tools/check_spec.py <arquivo.md>
python3 especificacao/tools/check_spec.py --lista-branca <arquivo.md>
python3 especificacao/tools/check_spec.py --mensagens <arquivo.json|arquivo.po>
```

O linter verifica a forma. O significado (R1.2) e as regras `[revisor]` precisam de leitura humana
ou do modelo.

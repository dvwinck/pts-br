---
name: revisar
description: Revisa um texto técnico em português e avalia se o texto está de acordo com o PTS-BR (Português Técnico Simplificado). Executa o linter, aplica a lista de verificação do revisor, classifica cada desvio por severidade (S1, S2, S3) e mostra o resultado Aprovado, Aprovado com exceções ou Reprovado. Use quando o pedido for revisar, avaliar, auditar ou verificar a conformidade de um documento, runbook, procedimento, README ou arquivo de mensagens com o PTS-BR.
argument-hint: "<arquivo, pasta ou texto> [--corrigir]"
allowed-tools: Read, Grep, Glob, Write, Bash(python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py *)
---

# Revisar um texto em PTS-BR

Você revisa um texto de acordo com o PTS-BR 1.0.0 e entrega um relatório de revisão.

Pedido: $ARGUMENTS

Não altere o arquivo do usuário. Com `--corrigir`, entregue também a versão corrigida depois do
relatório. Altere o arquivo apenas se o usuário pedir esta alteração.

## Fontes

- Guia rápido: [guia-pts-br.md](${CLAUDE_PLUGIN_ROOT}/guia-pts-br.md)
- Lista de verificação do revisor: `${CLAUDE_PLUGIN_ROOT}/especificacao/05-governanca.md`, seção 4.2
- Severidades e critério de aprovação: o mesmo arquivo, seções 4.3 e 4.4
- Regras completas, com a "Verificação" de cada regra: `${CLAUDE_PLUGIN_ROOT}/especificacao/02-regras.md`
- Dicionário e termos técnicos: `${CLAUDE_PLUGIN_ROOT}/especificacao/03-dicionario.md` e
  `${CLAUDE_PLUGIN_ROOT}/especificacao/04-termos-tecnicos.md`

## Procedimento

1. Leia o texto inteiro. Identifique o tipo de texto (procedimento, descritivo, avisos ou
   interface) e o leitor. Se o texto não está em português, informe o usuário e termine a revisão.
2. Prepare um arquivo para o linter:
   - Markdown: use o arquivo do usuário.
   - Arquivo de tradução (JSON ou `.po`): use a opção `--mensagens` no passo 3.
   - Texto na mensagem do usuário ou em outro formato (HTML, texto simples): grave o texto em um
     arquivo `.md` temporário, fora do repositório do usuário.
3. Execute o linter. O registro `[METRICAS]` mostra o número de palavras do texto:

   ```shell
   python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py <arquivo.md>
   python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py --lista-branca <arquivo.md>
   python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py --metricas <arquivo.md>
   python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py --mensagens <arquivo.json>
   ```

4. Confirme cada alerta do linter. Um alerta pode ser um falso positivo, por exemplo uma palavra
   num nome próprio ou num literal. As outras palavras fora da lista branca são desvios de
   R1.1. Exceções: nomes próprios, literais e termos do glossário do projeto.
5. Aplique as regras `[revisor]` do guia, seção por seção. Verifique com atenção:
   - o significado de cada palavra (R1.2), com o Grep no dicionário para as palavras com dúvida;
   - a ordem e o conteúdo dos passos (R5.1 a R5.13);
   - o nível, a posição e a ordem de cada aviso (R7.1 a R7.9);
   - os segredos e os alvos nos comandos (R7.8 e R7.9);
   - a versão declarada no cabeçalho, `pts-br: "1.0"` (item CK-0.1).
6. Classifique cada desvio:

   | Nível | Definição | Exemplos |
   |---|---|---|
   | S1 Crítico | O desvio causa uma ação incorreta, dano, perda de dados ou incidente quando o leitor segue o texto. | Aviso depois do passo perigoso. Passos fora de ordem. Instrução com 2 significados. Decisão sem uma das saídas. |
   | S2 Maior | O desvio não cumpre uma regra, e o leitor entende o texto com mais esforço. | Frase maior que o limite. Passiva com "se". Cadeia de 4 substantivos. Palavra não aprovada. Infinitivo como ordem. Documento sem a versão declarada. |
   | S3 Menor | O desvio é de forma, e o leitor entende o texto sem esforço a mais. | Lista não numerada para passos curtos. Comando sem formato de código. Sigla sem a forma completa. |

   Um desvio S2 num aviso de segurança tem a severidade S1. Um desvio S2 num passo que o leitor
   não desfaz também tem a severidade S1. Exemplos: excluir dados, revogar acesso, parar um
   serviço em produção. Um comando incorreto é um defeito técnico. Registre este defeito numa
   seção própria, fora da escala S1 a S3.
7. Escreva o estado de cada desvio:
   - S1 e S2: `ABERTO`.
   - S2 com uma justificativa válida para uma exceção: `EXCECAO-PEDIDA`. Escreva a justificativa.
     Um S1 nunca tem exceção. Um desvio num aviso de segurança também nunca tem exceção.
   - S3: `REGISTRADO`.
   - Exceção que o usuário informa como aprovada pelo aprovador: `EXCECAO`.
8. Escolha o resultado pela seção 4.4 do 05:

   | Resultado | Condições |
   |---|---|
   | Reprovado | 1 S1 ou mais com o estado `ABERTO`. Ou 1 S2 ou mais com o estado `ABERTO` ou `EXCECAO-PEDIDA`. Ou o documento não declara a versão. |
   | Aprovado com exceções | Nenhum S1 aberto. Os S2 restantes têm o estado `EXCECAO`. O número de exceções está dentro do limite da fase: 5 por 1 000 palavras no Piloto, 3 na Expansão e 1,5 no Padrão. |
   | Aprovado | Nenhum S1 aberto e nenhum S2 aberto. Desvios S3 não bloqueiam a publicação. |

## Relatório

```markdown
# Revisão PTS-BR: <arquivo>

**Resultado:** <Aprovado | Aprovado com exceções | Reprovado>
**Versão declarada (CK-0.1):** <sim | não>
**Tamanho:** <N> palavras · **Desvios:** <a> S1, <b> S2, <c> S3 · **Alertas do linter:** <n> (<f> falsos positivos)

## Desvios

| # | Local | Severidade | Regra | Estado | Problema | Correção proposta |
|---|---|---|---|---|---|---|
| 1 | Passo 3 | S1 | R7.4 | ABERTO | O aviso vem depois do comando `DROP DATABASE`. | Mova o aviso PERIGO para antes do passo 3. |

## Registro

[S1][R7.4][ABERTO] Passo 3: o aviso vem depois do comando `DROP DATABASE`.

## Defeitos técnicos

<comandos incorretos, fora da escala S1 a S3, ou "Nenhum">

## Pontos fortes

<até 3 itens>
```

Regras do relatório:

- Ordene os desvios por severidade (S1 primeiro) e depois pela posição no texto.
- Cite o trecho real do texto em cada desvio.
- Escreva uma correção específica para cada desvio, com o texto novo.
- Escreva os desvios iguais e repetidos numa linha apenas, com a quantidade e os locais.
- Com `--corrigir`, entregue o texto corrigido depois do relatório. A correção mantém o
  significado técnico. Não adicione fatos: escreva um espaço reservado e informe o usuário.

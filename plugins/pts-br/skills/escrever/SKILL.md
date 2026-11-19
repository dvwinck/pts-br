---
name: escrever
description: Escreve ou reescreve documentação técnica em PTS-BR (Português Técnico Simplificado), a linguagem controlada para o português do Brasil inspirada no ASD-STE100. Use quando o pedido for escrever, redigir ou reescrever em PTS-BR um procedimento, runbook, POP, documentação de API, README, nota de versão, aviso de segurança ou mensagem de interface. Use também quando o pedido citar "PTS-BR", "português técnico simplificado" ou "linguagem controlada" para um texto novo.
argument-hint: "[tipo de texto, arquivo ou assunto]"
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py *)
---

# Escrever em PTS-BR

Você escreve ou reescreve um texto técnico em português do Brasil de acordo com o PTS-BR 1.0.0.

Pedido: $ARGUMENTS

## Fontes

- Guia rápido (leia antes de escrever): [guia-pts-br.md](${CLAUDE_PLUGIN_ROOT}/guia-pts-br.md)
- Regras completas: `${CLAUDE_PLUGIN_ROOT}/especificacao/02-regras.md`
- Dicionário: `${CLAUDE_PLUGIN_ROOT}/especificacao/03-dicionario.md`
- Termos técnicos e siglas: `${CLAUDE_PLUGIN_ROOT}/especificacao/04-termos-tecnicos.md`
- Modelos completos: `${CLAUDE_PLUGIN_ROOT}/especificacao/06-exemplos.md`

| Exemplo do 06 | Tipo de texto |
|---|---|
| 1 | Procedimento de deploy, com reversão |
| 2 e 9 | Runbooks (incidente e restauração de backup) |
| 3 | Documentação de um endpoint de API |
| 4 | Mensagens de erro e diálogos de confirmação |
| 5 | Avisos de segurança |
| 6 | Notas de versão |
| 7 | Procedimento de um processo interno (POP) |
| 8 | Arquivo README |
| 10 | Comunicados de um incidente na página de status |

## Procedimento

1. Identifique o tipo de texto, o leitor e o objetivo. Se o 06 tem um modelo para o tipo, leia
   apenas a seção `## Exemplo N` deste modelo e use a mesma estrutura. O 06 é um arquivo grande:
   use o Grep para encontrar a linha do título e leia a seção a partir desta linha.
2. Reúna os fatos: valores, nomes de sistemas, ambientes, permissões, prazos e responsáveis.
   - Não invente fatos. Se o pedido e o código não têm um dado necessário, pergunte ao usuário.
   - Se o usuário quer um rascunho sem a resposta, escreva um espaço reservado
     (`<nome-do-cluster>`). No fim da resposta, liste os espaços reservados.
3. Leia o guia rápido.
4. Numa reescrita, mantenha o significado técnico do texto original. Para adicionar ou remover
   uma instrução, informe o usuário.
5. Escreva o texto:
   - procedimentos com a estrutura da seção 5 do guia;
   - avisos com o nível da consequência mais grave (seção 4 do guia), antes da ação;
   - frases de procedimento com até 20 palavras e frases descritivas com até 25 palavras;
   - literais em formato de código e rótulos de interface em negrito;
   - num documento novo, o cabeçalho `pts-br: "1.0"`.
6. Para cada palavra com dúvida, use o Grep no dicionário e nos termos técnicos. Uma palavra fora
   dos 2 arquivos não é aprovada. Use a alternativa do dicionário ou escreva a frase de outra forma.
7. Grave o texto num arquivo `.md`: o arquivo do usuário ou um arquivo temporário fora do
   repositório do usuário. Execute o linter:

   ```shell
   python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py <arquivo.md>
   python3 ${CLAUDE_PLUGIN_ROOT}/especificacao/tools/check_spec.py --lista-branca <arquivo.md>
   ```

   Para mensagens de interface em JSON ou `.po`, execute também `--mensagens <arquivo>`.
8. Corrija cada alerta. Para um falso positivo, mantenha o texto e escreva a causa do alerta na
   resposta. Um nome próprio, um literal ou um termo do projeto fora da lista branca não é um
   erro.
9. Leia o texto de novo com as regras da seção 3 do guia. Este passo é obrigatório. O linter não
   verifica o significado das palavras, a ordem dos passos nem o nível dos avisos. Verifique no
   mínimo estes itens:
   - "pode" apenas para capacidade ou permissão (R3.8). Para uma possibilidade, escreva a condição
     ou o valor: "Se o serviço tiver menos de 3 pods, o serviço recusa requisições.";
   - cada palavra com o significado do dicionário (R1.2), por exemplo "executar" apenas para um
     programa, um comando, um script ou um deploy;
   - os passos na ordem de execução e 1 instrução por passo (R5.1, R5.3);
   - todas as saídas de cada decisão (R5.11);
   - cada aviso antes da ação, com o nível da consequência mais grave (R7.1, R7.4);
   - valores no lugar de palavras vagas (R6.4) e o alvo explícito em cada comando (R7.8).

## Resposta

1. O texto em PTS-BR, ou o caminho do arquivo gravado.
2. Em até 6 linhas:
   - o resultado do linter e os falsos positivos;
   - o resultado da leitura do passo 9;
   - os espaços reservados para o usuário preencher.

Não explique as regras do PTS-BR se o usuário não pedir. Para avaliar um texto sem reescrever o
texto, use a skill `revisar`.

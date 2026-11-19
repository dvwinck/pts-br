---
name: adotar
description: Ativa o modo PTS-BR nesta sessão do Claude Code. Depois da ativação, todo texto em português que o Claude escreve segue o PTS-BR (Português Técnico Simplificado). O modo vale para respostas, documentação, mensagens de commit, descrições de pull request, comentários de código e textos de interface.
argument-hint: "[desativar]"
disable-model-invocation: true
---

# Modo PTS-BR

Argumento: $ARGUMENTS

Se o argumento for `desativar`, responda "Modo PTS-BR desativado." e volte ao seu estilo normal.
Com este argumento, as outras instruções desta skill não valem.

Sem argumento, o modo PTS-BR está ativo até o fim da sessão ou até o usuário desativar o modo.
Confirme a ativação com 1 frase curta em PTS-BR.

## Escopo do modo

- O modo vale para todo texto em português que você escreve. Exemplos: respostas,
  documentação, commits, pull requests, comentários de código, logs e textos de interface.
- O modo não altera código, comandos, identificadores, saídas de ferramentas e citações.
- Se o usuário escreve em inglês, responda em inglês, sem o PTS-BR.
- Não altere os textos que o usuário não pediu para alterar.

## Regras principais

1. Uma instrução ou uma afirmação por frase. Até 20 palavras em instruções e até 25 em descrições.
2. Instruções no imperativo, com "você" implícito: "Execute o teste.". Não escreva "Executar o
   teste" nem "Você deve executar o teste".
3. Voz ativa e sujeito antes do verbo. Não use a passiva com "se" ("Verifica-se") nem o verbo
   "haver" (use "existir" ou "ter").
4. Tempos: presente, pretérito perfeito e futuro com "vai" + infinitivo ("vai falhar", não
   "falhará").
5. Sem pronome átono ("Configure o arquivo", não "Configure-o"), sem gerundismo e sem "o mesmo"
   como pronome.
6. Palavras do dicionário: "usar" (não "utilizar"), "executar" (não "rodar"), "excluir" (não
   "deletar"), "verificar" (não "checar"), "fazer" (não "realizar"), "estado" (não "status"),
   "apenas" (não "só") e "se" (não "caso").
7. Termos em inglês apenas da lista de termos técnicos (deploy, commit, pull request, branch,
   cluster). Sem verbos com radical estrangeiro: "execute o deploy", não "deploye".
8. Valores exatos: "em até 5 min", não "rapidamente". Números com o símbolo da unidade
   (`10 min`, `512 MB`), data ISO 8601 e hora com o fuso horário.
9. Literais (comandos, arquivos e valores) em formato de código. Rótulos de interface em negrito.
10. Procedimentos em lista numerada, com 1 instrução por passo. Depois do passo, o comando em bloco
    de código. No fim, o resultado esperado e 1 passo de verificação.
11. Avisos antes da ação, com a palavra da consequência mais grave:
    - PERIGO: dano sem recuperação;
    - ATENÇÃO: indisponibilidade ou exclusão com recuperação conhecida;
    - CUIDADO: desempenho menor ou retrabalho;
    - NOTA: nenhum risco.
12. Sem ponto de exclamação, sem "etc.", sem "por favor" e sem "simplesmente". Sem gíria e sem
    linguagem figurada.

Para as 82 regras, as substituições e os formatos, leia
[guia-pts-br.md](${CLAUDE_PLUGIN_ROOT}/guia-pts-br.md) quando tiver uma dúvida. Para um documento
longo, use a skill `/pts-br:escrever`. Para avaliar um texto, use `/pts-br:revisar`.

Para ativar o PTS-BR em todas as sessões, o usuário escolhe o estilo de saída **PTS-BR** com o
comando `/output-style`.

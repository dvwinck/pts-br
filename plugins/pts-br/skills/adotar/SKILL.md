---
name: adotar
description: Ativa o modo PTS-BR nesta sessão do Claude Code. Depois da ativação, o texto em português que o Claude escreve segue o PTS-BR (Português Técnico Simplificado). O modo vale para respostas, documentação, comentários de código e textos de interface. O modo não vale para commits, pull requests, logs e textos do usuário com frases em inglês.
argument-hint: "[desativar]"
disable-model-invocation: true
allowed-tools: Read
---

# Modo PTS-BR

Argumento: $ARGUMENTS

Se o argumento for `desativar`, responda "Modo PTS-BR desativado." e volte ao seu estilo normal.
Com este argumento, as outras instruções desta skill não valem.

Sem argumento:

1. Leia o arquivo `${CLAUDE_PLUGIN_ROOT}/output-styles/pts-br.md`. O arquivo tem o escopo e as
   regras do PTS-BR. O estilo de saída **PTS-BR** usa o mesmo arquivo.
2. Siga as seções "Escopo do estilo" e "Regras" deste arquivo até o fim da sessão ou até o usuário
   desativar o modo. Neste modo, a palavra "estilo" do arquivo significa "modo".
3. Confirme a ativação com 1 frase curta em PTS-BR.

Para as 82 regras, as substituições e os formatos, leia
[guia-pts-br.md](${CLAUDE_PLUGIN_ROOT}/guia-pts-br.md) quando tiver uma dúvida. Para um documento
longo, use a skill `/pts-br:escrever`. Para avaliar um texto, use `/pts-br:revisar`.

Para ativar o PTS-BR em todas as sessões, o usuário escolhe o estilo de saída **PTS-BR** com o
comando `/output-style`.

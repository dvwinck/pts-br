# Plugin PTS-BR para o Claude Code

Este plugin aplica o PTS-BR 1.0.0, o Português Técnico Simplificado, no Claude Code. O PTS-BR é
uma linguagem controlada para documentação técnica em português do Brasil, inspirada na estrutura
do ASD-STE100. Especificação completa: <https://dvwinck.github.io/pts-br/>.

## Instalar

No Claude Code:

```text
/plugin marketplace add dvwinck/pts-br
/plugin install pts-br@pts-br
```

Ou no terminal:

```shell
claude plugin marketplace add dvwinck/pts-br
claude plugin install pts-br@pts-br
```

Reinicie a sessão depois da instalação. O linter do plugin precisa do Python 3.9 ou de uma
versão mais nova.

## Conteúdo

| Item | Comando | Função |
|---|---|---|
| Skill `escrever` | `/pts-br:escrever <assunto ou arquivo>` | Escreve ou reescreve um texto técnico em PTS-BR. O Claude consulta o dicionário e os modelos do 06. Antes da resposta, o Claude executa o linter. |
| Skill `revisar` | `/pts-br:revisar <arquivo> [--corrigir]` | Avalia a conformidade de um texto. O Claude executa o linter, aplica a lista de verificação do revisor e classifica os desvios (S1, S2, S3). O resultado é Aprovado, Aprovado com exceções ou Reprovado. |
| Skill `adotar` | `/pts-br:adotar` (ou `/pts-br:adotar desativar`) | Ativa o PTS-BR em todo texto em português que o Claude escreve nesta sessão: respostas, documentação, commits, pull requests e comentários. |
| Estilo de saída `PTS-BR` | `/output-style` e escolha **PTS-BR** | Ativa o PTS-BR em todas as sessões. O estilo mantém as instruções de engenharia de software do Claude Code. |

O Claude também usa as skills `escrever` e `revisar` sem o comando, quando o pedido fala de
PTS-BR. A skill `adotar` funciona apenas com o comando.

## Arquivos

| Pasta ou arquivo | Conteúdo |
|---|---|
| `guia-pts-br.md` | Guia rápido: decisões de base, as 82 regras, níveis de aviso, formatos e substituições frequentes. |
| `especificacao/` | Cópia da especificação (partes 01 a 06), do linter (`tools/check_spec.py`) e das regras Vale. |
| `skills/` | As skills `escrever`, `revisar` e `adotar`. |
| `output-styles/pts-br.md` | O estilo de saída. |

A pasta `especificacao/` é uma cópia gerada. Não altere esta pasta. Para atualizar a cópia, na
raiz do repositório, execute:

```shell
python3 tools/sincronizar_plugin.py
```

O pipeline do site executa `python3 tools/sincronizar_plugin.py --verificar` e falha se a cópia
estiver desatualizada.

## Limites

- O linter verifica a forma das palavras e parte das regras. O significado das palavras (R1.2) e
  as regras `[revisor]` dependem da leitura do modelo, que pode errar. Para documentos de
  produção, mantenha a revisão humana de `05-governanca.md`, seção 4.
- As regras desta versão ainda não têm resultado com o Vale. O linter em Python é a referência.

## Licença

CC BY 4.0, como a especificação. Veja `especificacao/LICENSE`.

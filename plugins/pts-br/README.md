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
| Skill `revisar` | `/pts-br:revisar <arquivo> [--fase piloto\|expansao\|padrao] [--corrigir]` | Avalia a conformidade de um texto. O Claude executa o linter, aplica a lista de verificação do revisor e classifica os desvios (S1, S2, S3). O resultado é Aprovado, Aprovado com exceções ou Reprovado. Com exceções aprovadas, o resultado depende da fase de adoção. |
| Skill `adotar` | `/pts-br:adotar` (ou `/pts-br:adotar desativar`) | Ativa o PTS-BR no texto em português que o Claude escreve nesta sessão: respostas, documentação, comentários de código e textos de interface. O PTS-BR não vale para commits, pull requests, logs e textos do usuário com frases em inglês. |
| Estilo de saída `PTS-BR` | `/output-style` e escolha **PTS-BR** | Ativa o PTS-BR em todas as sessões, com o mesmo escopo da skill `adotar`. O estilo mantém as instruções de engenharia de software do Claude Code. |

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

## Versões

| Versão | Data | Alterações |
|---|---|---|
| 2.0.0 | 2026-11-19 | O PTS-BR não vale mais para commits, pull requests e logs. O PTS-BR também não vale para textos do usuário com frases em português e em inglês. A especificação continua na versão 1.0.0. |
| 1.0.0 | 2026-11-19 | Primeira versão do plugin, com a especificação 1.0.0. |

## Licença

CC BY 4.0, como a especificação. Veja `especificacao/LICENSE`.

---

<!-- rodape -->
Feito com ❤️ em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Alguns direitos reservados.

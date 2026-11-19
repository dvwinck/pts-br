# Política de segurança

## Versões com correções de segurança

| Versão | Correções de segurança |
|---|---|
| 1.0.x | Sim |
| Antes de 1.0.0 | Não |

O escopo desta política é o código do repositório:

- O linter e os scripts da pasta `tools/`.
- Os pipelines da pasta `.github/workflows/`.
- O plugin da pasta `plugins/pts-br/`.

## Como informar uma vulnerabilidade

Não crie uma issue pública para uma vulnerabilidade.

1. Abra a página [Security](https://github.com/dvwinck/pts-br/security) do repositório.
2. Clique em "Report a vulnerability".
3. Escreva a descrição, os passos para reproduzir o problema e o impacto.
4. Envie o relatório.

O relatório é privado. Apenas o mantenedor e você leem o relatório.

## Prazos

| Etapa | Prazo |
|---|---|
| Resposta inicial | 5 dias úteis depois do relatório |
| Decisão sobre o relatório | 10 dias úteis depois da resposta inicial |
| Correção de uma vulnerabilidade confirmada | Versão PATCH, no menor prazo possível |

O mantenedor informa o resultado no relatório. Se você quiser, o aviso de segurança publicado tem o seu nome.

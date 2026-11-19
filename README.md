# PTS-BR — Português Técnico Simplificado

<!-- nav -->
**Início** · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

Versão 1.0.0 (2026-11-18)

Versão HTML: <https://dvwinck.github.io/pts-br/>

O PTS-BR é uma linguagem controlada para documentação técnica em português do
Brasil. O PTS-BR tem 3 partes:
- **Regras de escrita:** como escrever palavras, verbos, frases, procedimentos e avisos.
- **Dicionário controlado:** palavras aprovadas, cada uma com um significado, e
  palavras não aprovadas, cada uma com uma alternativa.
- **Termos técnicos:** os nomes técnicos, os verbos técnicos e a política de termos em inglês.

O objetivo é um texto que o leitor entende numa leitura. O leitor-alvo também
tem pessoas com pouca leitura técnica. O leitor-alvo também tem leitores não
nativos de português.

O escopo é a documentação de software, de processos e de tecnologia. Exemplos:
- Manuais, runbooks e procedimentos de operação.
- Procedimentos de processos da empresa (POP).
- Documentação de API, mensagens de interface e notas de versão.
- Avisos de segurança.
O [`01-introducao.md`](01-introducao.md) define o escopo completo.

> **Aviso.** O PTS-BR usa a estrutura do ASD-STE100 ("Simplified Technical English")
> como modelo. O PTS-BR não é uma tradução oficial do ASD-STE100. A ASD ("AeroSpace and Defence
> Industries Association of Europe") não aprovou o PTS-BR. As regras são originais e seguem a gramática do português.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [01-introducao.md](01-introducao.md) | Escopo, princípios, modo de uso e diferença entre termos técnicos e vocabulário geral. |
| [02-regras.md](02-regras.md) | 82 regras de escrita nas Seções 1 a 10, com justificativa e exemplos "Não aprovado" e "PTS-BR". 12 regras têm a marca `[vale]` (o linter encontra parte dos desvios). 70 regras têm a marca `[revisor]`. |
| [03-dicionario.md](03-dicionario.md) | Dicionário controlado: 723 palavras aprovadas, cada uma com um significado, e 362 palavras não aprovadas, cada uma com uma alternativa. Nesta versão, nenhuma palavra tem o estado "Obsoleta". Arquivo gerado (ver `tools/`). |
| [04-termos-tecnicos.md](04-termos-tecnicos.md) | Nomes técnicos em 25 categorias ([NT-01](04-termos-tecnicos.md#nt-01-produtos-softwares-e-serviços-externos) a [NT-25](04-termos-tecnicos.md#nt-25-termos-de-linguagem-e-de-redação)), verbos técnicos permitidos e política de termos em inglês. Tabela de 86 siglas de uso geral, glossário-base de TI com 270 termos e 146 decisões sobre termos em inglês. |
| [05-governanca.md](05-governanca.md) | Papéis, adoção em fases, lista de verificação do revisor, métricas, linter, manutenção do dicionário, versões e treinamento. |
| [06-exemplos.md](06-exemplos.md) | 10 textos completos antes e depois. Exemplos 1 a 5: procedimento, runbook, API, mensagens de erro e avisos de segurança. Exemplos 6 a 10: notas de versão, POP, `README.md`, restauração de um backup e comunicados de um incidente. 2 modelos de runbook. |
| [CHANGELOG.md](CHANGELOG.md) | Alterações de cada versão. |
| [`tools/`](https://github.com/dvwinck/pts-br/tree/main/tools) | Linter (regras Vale e `check_spec.py`), lista branca (`lista_branca.py`), testes das regras, arquivos de origem e script do dicionário, 2 pipelines. O linter também lê o `.vale.ini` da equipe (`--config`), o glossário do projeto (`--glossario`) e os arquivos de tradução JSON e `.po` (`--mensagens`). O [`05-governanca.md`](05-governanca.md), [seção 6](05-governanca.md#6-ferramentas-de-verificação), descreve cada arquivo. |

## Como começar

### Para o redator

1. Leia o [`01-introducao.md`](01-introducao.md).
2. Leia as Seções 5 e 7 do [`02-regras.md`](02-regras.md) se você escreve procedimentos ou avisos.
3. Compare um texto antes e depois no [`06-exemplos.md`](06-exemplos.md).
4. Escreva o documento. Declare a versão no cabeçalho: `pts-br: "1.0"`.
5. Procure cada palavra no [`03-dicionario.md`](03-dicionario.md) e no [`04-termos-tecnicos.md`](04-termos-tecnicos.md) se você não souber a decisão da palavra.
6. Execute o linter no documento. Com o Python 3.9 ou mais novo, o linter não
   precisa de instalação:

   ```shell
   python3 tools/check_spec.py docs/meu-documento.md
   ```

   Com o glossário do projeto, use também `--glossario docs/glossario.md`. O linter em
   Python é a referência da versão 1.0.0. As regras desta versão ainda não têm resultado
   com o Vale ([`05-governanca.md`](05-governanca.md), [seção 6.6](05-governanca.md#66-testes-das-regras)). Com o Vale 3.27.0 instalado, use também:

   ```shell
   vale --config tools/vale/.vale.ini docs/meu-documento.md
   ```
7. Mostre as palavras sem entrada no 03 e no 04:

   ```shell
   python3 tools/check_spec.py --lista-branca docs/meu-documento.md
   ```
8. Para mensagens de interface, verifique o arquivo de tradução (JSON ou `.po`):

   ```shell
   python3 tools/check_spec.py --mensagens locales/pt-BR.json
   ```
9. Corrija cada alerta, ou escreva a justificativa no pedido de revisão.
10. Peça a revisão PTS-BR: crie o pull request, ou use o procedimento para documentos fora
    do Git ([`05-governanca.md`](05-governanca.md), [seção 4.5](05-governanca.md#45-documentos-fora-do-git)).
11. Se nenhuma palavra aprovada tiver o significado correto, envie um PMD
    ([`05-governanca.md`](05-governanca.md), [seção 7](05-governanca.md#7-manutenção-do-dicionário-e-das-regras)).

### Para o revisor

1. Faça a trilha do redator e a trilha do revisor ([`05-governanca.md`](05-governanca.md), [seção 9](05-governanca.md#9-treinamento)).
2. Aplique a lista de verificação do [`05-governanca.md`](05-governanca.md), [seção 4.2](05-governanca.md#42-lista-de-verificação-do-revisor), em cada revisão.
   O linter encontra parte dos desvios. O revisor verifica todos os itens.
3. Classifique cada desvio como S1, S2 ou S3 (seção 4.3).
4. Registre cada desvio com o formato `[S2][R4.2][ABERTO] <descrição>`: a severidade do
   desvio, o ID da regra e o estado (seção 4.1).
5. Calcule M1 e as palavras de M2. Confirme cada palavra de M2:

   ```shell
   python3 tools/check_spec.py --metricas docs/meu-documento.md
   ```
6. Peça ao aprovador cada exceção S2 necessária, com o estado `EXCECAO-PEDIDA` (seção 4.1).
7. Registre o resultado com o critério de aprovação (seção 4.4) e o tempo de revisão em
   minutos. Registre também a linha `[METRICAS]` e a linha `[LINTER]` (seção 4.1).
8. Se uma regra tiver 2 significados possíveis, consulte o mantenedor.

### Para o mantenedor

Antes de publicar uma versão, execute estes comandos e registre o resultado de cada
comando na entrada da versão do [`CHANGELOG.md`](CHANGELOG.md) ([`05-governanca.md`](05-governanca.md), [seção 8.5](05-governanca.md#85-critérios-para-publicar-uma-versão)).

1. Verifique os arquivos de origem do dicionário:

   ```shell
   python3 tools/build.py
   ```
2. Gere o 03:

   ```shell
   python3 tools/build.py --render 03-dicionario.md
   ```
3. Confirme que a regra Vale de palavras não aprovadas é igual ao 03 e ao 04:

   ```shell
   python3 tools/gerar_regras_dicionario.py --verificar
   ```
4. Teste as regras com os testes, com o 06 e com as frases da lista branca:

   ```shell
   python3 tools/check_spec.py --teste
   ```
5. Verifique o texto da especificação com as regras do linter:

   ```shell
   python3 tools/check_spec.py --spec --falhar
   ```
6. Verifique o texto da especificação com a lista branca (no máximo 1% de palavras sem aprovação):

   ```shell
   python3 tools/check_spec.py --lista-branca --spec --meta 1
   ```

7. Confirme os critérios de [`05-governanca.md`](05-governanca.md), [seção 8.5](05-governanca.md#85-critérios-para-publicar-uma-versão). Crie a tag `v1.0.0` no commit
   da publicação.

O linter em Python é a referência da versão 1.0.0. As regras da versão 1.0.0 ainda não
têm resultado com o Vale. O teste das regras com o Vale é um critério de entrada do Piloto
([`05-governanca.md`](05-governanca.md), seções 3.2 e 6.6). A lista branca verifica a forma das palavras, não o
significado: o revisor verifica o significado.

## Versão

- Versão da especificação: **1.0.0** (2026-11-18). Um documento declara apenas
  `MAJOR.MINOR` (`pts-br: "1.0"`).
- A especificação usa versões `MAJOR.MINOR.PATCH`. O [`05-governanca.md`](05-governanca.md), [seção 8](05-governanca.md#8-versões-da-especificação),
  define o critério de cada tipo de versão.
- O [`CHANGELOG.md`](CHANGELOG.md) registra as alterações de cada versão.
- O mantenedor cria a tag `v1.0.0` no repositório da especificação na publicação da
  versão 1.0.0. A tag é a versão das regras que o pipeline de uma equipe usa (`PTSBR_REF`).

## Licença

Licença: [`CC BY 4.0`](https://creativecommons.org/licenses/by/4.0/deed.pt_BR) ("Creative Commons Atribuição 4.0 Internacional").
Esta é a licença decidida para a versão 1.0.0.

Com esta licença, você pode copiar, alterar e distribuir o PTS-BR, também para
uso comercial. Escreva a origem do texto e indique as alterações.

A licença cobre apenas o texto do PTS-BR. O ASD-STE100 tem uma licença da ASD.

---

<!-- nav -->
**Início** · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

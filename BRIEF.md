# Briefing — PTS-BR: Português Técnico Simplificado (inspirado no ASD-STE100)

## Objetivo
Criar uma especificação de linguagem controlada para português do Brasil, equivalente em
função ao ASD-STE100 (Simplified Technical English): um conjunto de **regras de escrita** +
um **dicionário controlado** (palavras aprovadas e não aprovadas com alternativas), para
documentação técnica de **software, processos e tecnologia** (manuais, runbooks, procedimentos
operacionais, docs de API, mensagens de UI, notas de release, instruções de segurança).

## Nome e status
- Nome: **PTS-BR — Português Técnico Simplificado** (versão 1.0, 2026-11-18).
- Declarar no início: "inspirado na estrutura do ASD-STE100; não é tradução oficial nem
  endossado pela ASD". Não copiar texto do ASD-STE100 literalmente — redigir regras originais,
  adaptadas à gramática do português.

## Público
1. Redatores técnicos e desenvolvedores que escrevem docs em pt-BR.
2. Leitores: falantes nativos com pouca leitura técnica e não nativos (espanhol, inglês).
3. Ferramentas: regras devem ser verificáveis por revisor humano e, quando possível, por linter.

## Decisões linguísticas fixas (todos os agentes seguem)
- Procedimentos: **imperativo afirmativo na 3ª pessoa (você)** — "Remova", "Instale", "Clique".
  Não usar infinitivo como ordem ("Remover a tampa") em passos de procedimento. Infinitivo é
  permitido só em títulos de procedimento ("Instalar o agente").
- Tratamento: **você** implícito. Nunca "tu", "o senhor", "o usuário deve".
- Voz ativa; voz passiva só em texto descritivo quando o agente é desconhecido/irrelevante.
  Proibir passiva sintética com "se" ("Instala-se", "Verifica-se").
- Colocação pronominal: evitar clíticos. Proibir mesóclise. Preferir repetir o substantivo.
- Sem gerundismo ("vamos estar enviando") e sem gerúndio encadeado.
- Tempos verbais aprovados: presente, pretérito perfeito, futuro com "vai + infinitivo"
  (decidir no texto se o futuro do presente simples também é aceito — justificar).
  Subjuntivo: só em condicionais com "se" + futuro do subjuntivo, quando inevitável — o
  documento deve decidir e justificar.
- Limites: procedimento ≤ 20 palavras por frase; descritivo ≤ 25 palavras; parágrafo ≤ 6 frases.
- Cadeias nominais com "de": máximo 3 substantivos encadeados ("o arquivo de configuração do
  servidor" ok; mais que isso, reescrever).
- Uma palavra = um significado = uma classe gramatical (princípio central do STE).
- Estrangeirismos de TI: regra explícita (quando manter em inglês — nomes técnicos consagrados
  como "deploy"? decidir: o documento deve definir política e lista).

## Arquivos (todos na raiz do repositório)
- `01-introducao.md` — escopo, princípios, como usar, termos técnicos vs vocabulário geral.
- `02-regras.md` — regras de escrita numeradas (R1.1, R1.2…), cada uma com: enunciado,
  justificativa curta, exemplo **Não aprovado** / **PTS-BR** (pares de exemplo de software/TI).
  Seções: 1 Palavras · 2 Cadeias nominais · 3 Verbos · 4 Frases · 5 Procedimentos ·
  6 Texto descritivo · 7 Avisos de segurança (PERIGO/ATENÇÃO/CUIDADO) · 8 Pontuação e
  formatação · 9 Práticas de escrita · 10 Interface e mensagens de software.
- `03-dicionario.md` — dicionário controlado em tabelas Markdown:
  | Palavra (classe) | Status | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |
  Ordem alfabética. Palavras aprovadas em MAIÚSCULAS na coluna 1 (ex.: `REMOVER (v)`),
  não aprovadas em minúsculas com a alternativa aprovada.
- `04-termos-tecnicos.md` — categorias de nomes técnicos e verbos técnicos permitidos
  (equivalente às "technical names/verbs" do STE), política de anglicismos, glossário-base de TI.
- `05-governanca.md` — processo de adoção, verificação de conformidade (checklist, métricas,
  linter), manutenção do dicionário (pedido de inclusão de palavra), versionamento.
- `06-exemplos.md` — textos completos antes/depois (procedimento de deploy, runbook de
  incidente, descrição de API, mensagem de erro, aviso de segurança, nota de release).
- `README.md` — índice.
- `reviews/round-N/<especialista>.md` — avaliações.

## Formato
Markdown, pt-BR, sem emojis. Exemplos sempre do domínio de software/processos/TI.
O próprio texto da especificação deve, sempre que possível, seguir o PTS-BR.

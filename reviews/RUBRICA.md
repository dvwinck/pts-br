# Rubrica de avaliação — PTS-BR

Cada especialista avalia o pacote inteiro (`README.md`, `01` a `06`) pela própria lente e
dá nota de 0 a 10 em 5 critérios. A nota do especialista é a média dos 5 critérios.
Meta: média das 4 notas de especialista **≥ 8,0**.

## Critérios comuns (todas as lentes)
1. **Correção** — regras e entradas corretas para o pt-BR e para o domínio; sem contradição
   entre arquivos (regras × dicionário × termos técnicos × exemplos × governança).
2. **Completude** — cobre o que um padrão equivalente ao ASD-STE100 precisa cobrir para
   o uso real da lente avaliada.
3. **Aplicabilidade** — um redator ou revisor consegue aplicar sem ambiguidade; regras verificáveis.
4. **Coerência interna e consistência** — o próprio texto segue o PTS-BR; terminologia estável;
   referências cruzadas certas.
5. **Valor para a lente** — utilidade concreta para o domínio do especialista.

## Escala
- 9–10: pronto para publicação; ajustes cosméticos.
- 8: bom; poucos problemas menores, nenhum bloqueante.
- 6–7: utilizável com correções relevantes.
- ≤ 5: problemas estruturais.

## Formato do arquivo de avaliação (`reviews/round-N/<lente>.md`)
```
---
lente: <processos|tecnologia|desenvolvimento|documentacao>
rodada: N
notas: {correcao: X, completude: X, aplicabilidade: X, coerencia: X, valor: X}
nota_final: X.X
---
## Pontos fortes (até 5)
## Problemas (ordenados por impacto)
Cada item: [BLOQUEANTE|IMPORTANTE|MENOR] arquivo:seção — problema — correção concreta proposta.
## O que levaria a nota a ≥ 8 (se < 8) ou a 9 (se ≥ 8)
```
Seja exigente e específico. Cite trechos reais. Não proponha correção vaga.

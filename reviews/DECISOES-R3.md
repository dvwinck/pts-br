# Decisões para a revisão da rodada 3 (vinculantes)

Rodada 2: processos 7,4 · tecnologia 7,9 · desenvolvimento 7,7 · documentação 7,4 → média 7,6 (meta ≥ 8).
Avaliações: `reviews/round-2/*.md`. DECISOES-R2 continua válido onde este arquivo não muda nada.

## Propriedade dos arquivos (fase 1, em paralelo)
- A: `01-introducao.md`, `02-regras.md`.
- B: fontes do 03 em `tools/` (d1–d3.txt, intro.md, build.py) e `04-termos-tecnicos.md`.
- C: `05-governanca.md`, `README.md`, `CHANGELOG.md`, `tools/*.py` exceto build.py, `tools/vale/**`, `tools/ci/**`.
- D: `06-exemplos.md`.
- Fase 2: varredura final (todos os arquivos) com a ferramenta de lista branca.

## Decisões
E1. **Autoconformidade por lista branca (D9 do 03).** Uma palavra do texto normativo é válida se for
    (a) forma flexionada de entrada aprovada no 03, (b) nome técnico, termo do glossário ou sigla do 04,
    (c) palavra da lista de metalinguagem do 01 §11.2, ou (d) palavra funcional aprovada. C cria
    `tools/lista_branca.py` (gera formas: conjugação regular -ar/-er/-ir nas formas aprovadas + tabela de
    irregulares; plural e gênero de substantivos e adjetivos) e o modo `check_spec.py --lista-branca`.
    B adiciona ao 03 as palavras gerais AUSENTES mais frequentes (um sentido cada), usando a lista do
    avaliador (`scratchpad/r2doc/`). Meta da fase 2: ≤ 1% de palavras do texto normativo fora da lista
    branca, todas justificadas. O CHANGELOG só afirma o que o modo `--lista-branca` comprova.
E2. **Registro × evidência × linha.** REGISTRO (s) = texto ou dado que documenta uma ação, um resultado
    ou um evento (registro de conformidade, linha "Registro:" de POP, entrada de log). A linha de uma
    tabela de banco de dados = LINHA (termo técnico no 04, NT-15). "evidência" passa a não aprovada →
    REGISTRO. RESPONSÁVEL (s) = pessoa ou equipe que faz uma etapa (sem "executa").
E3. **Níveis de aviso por consequência, não por ação (R7.1).**
    PERIGO: dano irreversível — perda de dados fora da cobertura do backup (RPO), exposição de dados a
    pessoas sem permissão, credencial exposta, risco a pessoas.
    ATENÇÃO: indisponibilidade parcial ou total com recuperação conhecida; perda de dados coberta pelo
    backup dentro do RPO; custo financeiro não planejado.
    CUIDADO: degradação sem perda de função (ex.: latência maior), retrabalho, dano menor.
    Todos os exemplos (02 R7.x, 03, 04, 06) seguem esta tabela; a mesma consequência tem o mesmo nível.
E4. **Segredos em comandos (R7.9, Ex3):** a variável expandida em argumento aparece em `ps`. Padrão
    aprovado: `printf 'Authorization: Bearer %s\n' "$API_TOKEN" | curl --header @- ...` (printf é
    comando interno do shell) ou arquivo de configuração com permissão 600. Nunca `-H "...$API_TOKEN"`.
E5. **Contexto do cluster (R7.8):** todo comando `kubectl`/`helm` de exemplo em 02 e 06 usa
    `--context`/`--kube-context` explícito. Exemplos de R5.9 e R7.8 incluídos.
E6. **Datas e quantidades relativas (R9.4, R6.4):** proibidas as palavras relativas à data de
    publicação ("recentemente", "atualmente", "nova versão"). ATUAL e AGORA são aprovados apenas em
    relação ao momento em que o leitor faz o procedimento ou vê a interface. VÁRIOS, GRANDE, PEQUENO,
    RÁPIDO: aprovados, mas R6.4 exige o valor quando ele existe; os exemplos do 03 mostram o valor.
E7. **Seção 10:** R10.8 trata zero, um e mais de um ("Nenhum arquivo excluído." / "1 arquivo
    excluído." / "{quantidade} arquivos excluídos."). R10.10 (logs): mensagem fixa e legível + valores em
    campos estruturados (chave=valor ou JSON), não interpolados no texto. Ex4 do 06 segue R10.5.
E8. **Vale:** o executável baixado não pode ser executado nesta sessão. O motor Python
    (`check_spec.py`) é a referência normativa da versão 1.0.0. A suíte com o Vale 3.27.0 rodou com os
    87 casos da rodada 2; os casos novos ainda não. Isso fica declarado no 05 e no CHANGELOG, e "rodar a
    suíte completa com o Vale" vira critério de entrada do Piloto (não de publicação da 1.0.0).
E9. **Linter e 04 §5.4:** o gerador também lê a tabela de verbos com radical estrangeiro do 04 §5.4 e
    os termos "não aprovados" do 04 §6.3. Casos de teste para deployar, commitar, mergear, buildar, logar.
E10. **Empacotamento:** `check_spec.py` aceita `--regras <pasta>` e `--dicionario <arquivo>`; o job de
    CI para repositórios de equipe não depende da estrutura de pastas da especificação; a isenção
    `--spec` vale apenas para a própria especificação.
E11. **Governança (C), itens de `round-2/processos.md`:** estados de aprovação sem sobreposição;
    S1 corrigido antes da aprovação não reprova; documento sem versão declarada tem resultado definido;
    M1/M2 medidos na submissão E na publicação (dizer qual vale para a meta); registro com os campos que
    M6/M7 precisam (datas, urgência, alertas por regra); fluxos de §4.1, §4.5 e §7.3 seguem R5.10–R5.12
    (bloco de responsável, todas as saídas de decisão, linhas "Registro:"); auditor no Piloto possível;
    auditoria das decisões do mantenedor definida; PMD urgente publicado em PATCH em até 5 dias úteis.
E12. **03 × 02 (B):** corrija as 13 entradas citadas em `round-2/documentacao.md` (ex.: "Faça a
    verificação final" → "Verifique…"; definição de FAZER) e acrescente ao build.py verificações para
    verbo-suporte e palavras vagas sem valor nos exemplos.
E13. **Defeitos técnicos do 06 (D), itens de `round-2/tecnologia.md`:** `pg_read_all_stats` (ou
    `pg_monitor`) no "Antes de começar" do Ex2; `helm upgrade` com `--values <arquivo de produção>` e
    verificação de revisão com estado `deployed`; Ex7 com destino para toda saída; condições conforme
    R3.2; níveis conforme E3.

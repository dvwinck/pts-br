# Decisões para a revisão da rodada 2 (vinculantes)

Rodada 1: processos 6,0 · desenvolvimento 6,7 · tecnologia 6,8 · documentação 6,3 → média 6,45.
Avaliações completas em `reviews/round-1/*.md`. Estas decisões resolvem os conflitos entre
arquivos. Elas prevalecem sobre qualquer texto atual da especificação.

## Precedência
1. Este arquivo.
2. Vocabulário (quais palavras e sentidos são aprovados): o 03 prevalece. Gramática e estrutura: o 02 prevalece.
3. IDs de regra existentes NÃO mudam de número. Regra nova entra no fim da seção (ex.: R5.10).

## Propriedade dos arquivos (cada agente edita só os seus)
- Agente A (linguística/documentação): `01-introducao.md`, `02-regras.md`.
- Agente B (tecnologia/dev, vocabulário): fontes do 03 em `tools/` (regenerar o 03) e `04-termos-tecnicos.md`.
- Agente C (processos/automação): `05-governanca.md`, `README.md`, `tools/vale/**`, `tools/check_spec.py`, `.github/workflows/` de exemplo dentro de `tools/ci/`.
- Agente D (exemplos/SRE): `06-exemplos.md`.
- Depois: agente de varredura final (todos os arquivos) + `CHANGELOG.md`.

## Decisões de conteúdo
D1. **Autoconformidade.** O texto normativo (README, 01, 02, 04, 05, 06-PTS-BR) usa apenas palavras
    aprovadas no 03 ou nomes técnicos do 04. Exceções: exemplos "Não aprovado", blocos de código,
    menção metalinguística (a palavra entre aspas ou em `código` quando o texto fala dela).
    "só" → APENAS. "Rode" → EXECUTE. "esse/essa/isso" → ESTE/ESTA/ISTO conforme o 03. Sem "há" (use EXISTIR/TER).
D2. **acima/abaixo:** aprovados (03) só para posição na mesma página ou tela. R9.4 muda: permite
    "acima/abaixo" para conteúdo adjacente; exige referência explícita ("a Tabela 3", "o passo 4") para
    conteúdo distante; proíbe para comparação de valores (use "maior que/menor que").
D3. **FICAR:** aprovado com um significado: "passar a um estado". R3.9 muda: verbos de ligação
    aprovados = SER, ESTAR, FICAR (mudança de estado). Proibidos como ligação: tornar-se, permanecer,
    continuar, parecer, virar.
D4. **"para" (PARAR × preposição):** regra nova no 02 (fim da Seção 1): não use a forma "para" do
    verbo PARAR quando a frase também admite leitura de preposição; reescreva (sujeito no plural,
    "não funciona", ou outra estrutura). Nota correspondente em D6 do 03.
D5. **Avisos (Seção 7):** nível escolhido por (a) reversibilidade e (b) exposição:
    PERIGO = dano irreversível ou risco a pessoas/dados pessoais/credenciais/segurança;
    ATENÇÃO = dano reversível ao sistema ou indisponibilidade com recuperação conhecida;
    CUIDADO = degradação, retrabalho ou dano menor. Corrija os exemplos R7.5/R7.7 com esse critério.
    Regras novas: R7.8 "Identifique o ambiente antes de um comando destrutivo" (nome do ambiente no
    aviso e no comando); R7.9 "Não coloque segredos na linha de comando nem no texto".
D6. **status/estado:** em prosa, ESTADO. Valores literais de estado mostrados pelo sistema: em
    formato de código quando vêm de CLI/API/log (`Running`), em **negrito** quando são rótulo de UI
    (R8.8). NT-24 alinha com isto.
D7. **Unidades e números:** símbolo com número sempre ("10 min", "1 h", "512 MB"); kB = 1000 bytes,
    KiB = 1024 (SI/IEC); MB, GB, TB maiúsculos; separador de milhar = espaço ("10 000"); decimal =
    vírgula. Corrija 03 (fontes), 04 NT-22 e 05 ("1.000" → "1 000").
D8. **Siglas:** o 04 ganha uma "Tabela de siglas de uso geral" (40–60 siglas: HTTP, HTTPS, JSON, YAML,
    XML, CSV, PDF, UTC, ID, CPU, RAM, SSD, TLS, SSH, SQL, TCP, UDP, REST, SDK, CLI, UI, CD, MFA, SSO,
    RBAC, IAM, RPO, RTO, MTTR, TI, LGPD, CPF, CNPJ, PR, etc.). R8.7 isenta as siglas desta tabela.
D9. **Acesso e papéis:** "papel de acesso" = role de RBAC/IAM; "função" = apenas função de código;
    "responsável" = pessoa ou equipe que executa uma etapa de processo; "cargo" = posição na empresa.
    "perfil de acesso" e "função" (no sentido de acesso) são não aprovados.
D10. **registry:** mantém "registry" (nome técnico, inglês). Um registry contém "repositórios de imagens".
    "Repositório" sozinho = repositório Git. Corrija a definição no glossário.
D11. **PASSAR:** verbo técnico com um sentido: "fornecer um argumento a uma função, comando ou
    endpoint" ("Passe o parâmetro `id`"). ENVIAR = transmitir dados por rede.
D12. **Vocabulário a adicionar (B):** API: cabeçalho, corpo (da requisição/resposta), código de
    status (HTTP), campo, parâmetro de consulta, payload (decidir), paginação. Operação/segurança:
    serviço, conta, conta de serviço, cofre de segredos, failover, RPO, RTO, MTTR, papel de acesso.
    Processo: dia útil, prazo, solicitante, aprovador, responsável, evidência, etapa, entrada, saída.
    Corrija as ~14 entradas do 03 com dois sentidos listadas em `round-1/documentacao.md`.
D13. **Marcas de automação no 02:** substitua `[lint]` por `[vale]` ou `[revisor]`. Marque `[vale]`
    APENAS para regras destes comportamentos, que o agente C vai implementar como regras Vale reais:
    palavras não aprovadas (lista gerada do 03), passiva sintética com "se", verbos-suporte, "o mesmo",
    frase longa (procedimento e descritivo), gerundismo, futuro simples e "irá"+infinitivo,
    mesóclise/ênclise, "onde" relativo, ponto como separador de milhar, unidade por extenso depois de
    número, "há". Todas as outras regras: `[revisor]`. A tabela-resumo mostra a marca.
    01 §8.2 muda: o revisor aplica o checklist inteiro; o linter apenas antecipa parte dele.
D14. **Procedimentos de processo (POP):** regras novas no 02, Seção 5: R5.10 responsável por
    procedimento ou por etapa; R5.11 ponto de decisão com todas as saídas; R5.12 registro/evidência
    que a etapa gera. 01 §2.1 inclui POP e processos de negócio no escopo. Avalie também os textos
    de desenvolvimento citados em `round-1/desenvolvimento.md` item 11 (mensagens de commit, descrição
    de PR, comentários de código): inclua no escopo com regra curta ou exclua com justificativa.
D15. **Governança (C):** cláusula de revisores fundadores (resolve o impasse de partida); SLA × versionamento;
    instrumentos de medição definidos (o `tools/check_spec.py` é a ferramenta de linha de base);
    fluxo para quem não usa docs-as-code (Confluence/Google Docs); demais itens de `round-1/processos.md`.
D16. **Linter real (C):** regras Vale em arquivos YAML de verdade em `tools/vale/PTSBR/`, com `\s+`
    entre palavras, limites de palavra com `(?<![\p{L}-])` e `(?![\p{L}-])`, e testes: os textos
    "Antes" do 06 devem gerar alertas e os textos PTS-BR do 06 não. Se o Vale não puder ser instalado,
    implemente os mesmos padrões em `tools/check_spec.py` (Python) e rode os testes com ele. O 05
    descreve o que existe de fato, sem prometer mais.

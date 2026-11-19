---
lente: tecnologia
rodada: 2
notas: {correcao: 7.5, completude: 7.5, aplicabilidade: 8, coerencia: 8, valor: 8.5}
nota_final: 7.9
---

Verificações feitas com scripts, sem alterar a especificação:
- `<pasta-de-trabalho-local>/siglas_r2.py`: siglas sem definição no README, no 01, no 02, no 04, no 05 e nos textos PTS-BR do 06, comparadas com a tabela 6.1 e com o glossário-base.
- Buscas com `grep`: unidades por extenso, ponto como separador de milhar, "KB", "Mbps", horas sem fuso horário, "status", "checklist" e "lista de verificação", "painel", "agente" e "deployment".
- `python3 tools/check_spec.py --spec`: o resultado foi "Total: 0 alerta(s)".
- Contagem das tabelas 6.1 (58 siglas) e 6.2 (220 termos). As contagens são iguais às do README.

## Status dos problemas da rodada 1

| # | Problema da rodada 1 | Status | Evidência |
|---|---|---|---|
| 1 | Fronteira PERIGO × ATENÇÃO contraditória (R7.1 × R7.5 × R7.7) | **Resolvido** (o conflito citado) | R7.1 tem agora 3 perguntas em ordem (reversibilidade e exposição). R7.5 explica: "O primeiro aviso é ATENÇÃO, não PERIGO: [...] a duração é conhecida e o sistema volta de forma automática". O exemplo do Elasticsearch em R7.7 mudou para ATENÇÃO e está na tabela ("que a equipe pode gerar de novo"). As correções criaram outras inconsistências de classificação (ver o problema novo 1). |
| 2 | R8.7 inaplicável a um documento de TI (só 9 siglas isentas) | **Resolvido** | 04 §6.1 tem 58 siglas (HTTP, JSON, TLS, SSH, SQL, CPU, ID, UTC, MFA, RBAC, IAM, RPO, RTO, MTTR...). R8.7 isenta a tabela. `siglas_r2.py` não mostra nenhuma sigla sem definição nos 8 textos PTS-BR do 06. A exceção é `HEAD` no Ex1, que é a saída literal do Git. |
| 3 | Faltam termos de operação e de segurança no glossário | **Resolvido**, com 3 lacunas pequenas | O glossário tem agora serviço, conta, conta de serviço, cofre de segredos, certificado, rastro, percentil, failover, réplica primária e réplica secundária, recuperação de desastre, retenção, privilégio mínimo, shell, terminal, kernel, observabilidade, limite de taxa, cota, incidente de segurança, vazamento de dados, IOPS e largura de banda. Ainda faltam "chave SSH" (aparece apenas na lista de exemplos de NT-16), "root" e "superusuário", e `sudo` (02:R5.1 usa `sudo`). |
| 4 | Vocabulário de acesso instável (papel × função × perfil) | **Resolvido** | "papel de acesso" (NT-16), "papel" (NT-19) e "função" apenas para código, com uma nota em cada entrada. R5.6: "o papel de acesso `cluster-admin`". Ex7: "Papéis de acesso por cargo". 04 §6.3 não aprova "perfil de acesso". |
| 5 | "status" em prosa no 02 | **Resolvido** | `grep status 02-regras.md` encontra a palavra apenas em literais (`kubectl rollout status`), em "código de status", em exemplos "Não aprovado" e na regra R8.8. R8.8 e NT-24 têm o mesmo formato: código para CLI, API e log, e negrito para a interface. |
| 6 | "registry → repositório" tecnicamente errado | **Resolvido** | 04 §5.5: "registry, Manter [...] Um registry contém repositórios de imagens". O glossário define "repositório" como repositório Git. Sobrou uma inconsistência no 03 (problema novo 9). |
| 7 | Unidades contraditórias (KB, bit/s, prefixo binário, unidade por extenso, "1.000", ISO 8601) | **Resolvido** | R8.4 e NT-22 têm o mesmo texto: kB minúsculo, bit/s, a escolha do prefixo pelo sistema, `512Mi` = 512 MiB e o símbolo depois do número. `grep` não encontra unidade por extenso depois de número, a não ser em exemplos "Não aprovado" (e "DIA: Período de 24 horas", no 03). R8.5 aceita "UTC-03:00" e exige UTC na linha do tempo de um incidente. Ainda existem horas sem fuso horário (problema novo 8). |
| 8 | Seção 7 não cobre alvo do comando, segredos e riscos de TI | **Resolvido** | R7.8 (alvo explícito com `--context`, `--profile` ou `--namespace`) e R7.9 (segredos fora da linha de comando) são regras novas. A tabela de R7.1 tem os riscos pedidos: TLS e MFA desativados, papel de administrador, bucket público, `0.0.0.0/0`, chave de criptografia e o TTL do DNS. R7.9 tem um defeito técnico novo (problema novo 3). |
| 9 | Ex2 inutilizável sem correções | **Resolvido** | O Ex2 tem a seção "Antes de começar" com `~/.pgpass`, `pg_signal_backend` e `kubectl auth can-i patch deployments/api-catalogo`. Os filtros `backend_type = 'client backend'` e `usename = 'api_catalogo'` aparecem também nos comandos de cancelamento. O aviso ATENÇÃO está antes de `pg_cancel_backend`. O passo 2 repete o comando. O texto diz "A API de catálogo retorna um erro". O Ex2 tem um defeito novo de privilégio (problema novo 2). |
| 10 | Ex1: fluxo do rollback incompleto, estados do pipeline, `curl` sem `--fail` | **Resolvido** | O Ex1 tem agora o procedimento "Reverter o deploy", com registro, verificação e fim em cada saída. O passo 4 tem uma saída para cada estado: **Queued** e **In progress** (com o limite de 30 min) e "outro valor". O comando usa `curl --fail --silent --show-error --max-time 10`. O Ex1 tem imprecisões novas de Helm (problema novo 4). |
| 11 | Estrangeirismos sem decisão (gateway, throughput, serverless, console, deployment, SDK, QA, chart, header, body, payload) | **Resolvido** | Todos têm uma decisão no §5.5 ou uma sigla no §6.1. ESCALAR: "Escale o objeto `Deployment` `api`". "payload" fica restrito a mensagem, evento e webhook. "corpo" e "cabeçalho" estão no glossário. |
| 12 | Polissemias (painel, instância, agente, operador) | **Resolvido** | painel: "Para a interface que gerencia um serviço, use 'console' ou 'portal'". A entrada "instância" exige o tipo. As 14 ocorrências de "agente" no 02 são o programa. "operador (LGPD)" está em NT-23. Existem polissemias novas em "servidor" e "repositório" (problema novo 9). |
| 13 | Terminologia diferente entre arquivos (release notes, checklist, MAJOR.MINOR.PATCH) | **Parcialmente resolvido** | "Notas de release" não aparece mais. MAJOR.MINOR.PATCH é igual em 04, 05 e README. A decisão de "checklist" agora contradiz o uso real (problema novo 7). |
| 14 | GMUD, RDM, plantonista e acionar sem alternativa | **Resolvido** | 04 §6.3: "GMUD, RDM → solicitação de mudança" e "plantonista → analista de plantão". 03, "acionar": "para chamar uma pessoa, envie um alerta". |
| 15 | Falta modelo de runbook e tipos de texto de operação (restauração, DR, pós-incidente, comunicado) | **Parcialmente resolvido** | O Ex2 tem uma estrutura que pode servir de modelo: Alerta, Impacto, Procedimentos, Antes de começar, Encaminhar e Resolver. Mas nenhuma regra ou seção declara esta estrutura como modelo. O 06 continua com 8 exemplos e não tem restauração de backup, DR, análise pós-incidente nem comunicado de incidente (problema novo 5). |

Resumo: **13 de 15 resolvidos**, 2 parcialmente resolvidos (13 e 15) e 0 não resolvidos. O item 3 conta como resolvido, com as lacunas pequenas no problema novo 13.

## Pontos fortes (até 5)

1. **A Seção 7 ficou operacional.** R7.8 exige um passo que mostra o alvo e a opção explícita no comando: "Não dependa do alvo padrão do terminal". R7.9 trata o histórico do shell, a lista de processos, as capturas de tela e os chamados. A tabela de R7.1 cobre os riscos reais de nuvem e de segurança: `0.0.0.0/0`, bucket público, exclusão de uma chave de criptografia e TTL do DNS. Poucos guias corporativos em pt-BR têm este nível.
2. **Os Exemplos 1, 2 e 5 seguem as práticas de SRE.** O Ex1 registra o `REVISION` do Helm antes do upgrade para usar no rollback e mostra o alvo com `kubectl cluster-info --context prod-sa-east-1`. No Ex2, `kubectl auth can-i patch deployments/api-catalogo` testa exatamente o verbo de `rollout restart`. O Ex5 usa `\conninfo` antes de um script destrutivo e passa `--host` e `--dbname` explícitos. Cada ponto de decisão tem todas as saídas, e um runbook não volta para trás sem um limite.
3. **A tabela de 58 siglas de uso geral com gênero e categoria (04 §6.1)** resolve um ponto fraco do STE em contexto de TI. O leitor não precisa da forma por extenso de HTTP, JSON ou TLS, e as siglas de domínio (IdP, MTBF) continuam com definição obrigatória. O 06 está conforme sem exceções.
4. **A política de estrangeirismos é defensável e confere com as interfaces pt-BR reais.** Alguns exemplos: "limite de taxa" (console do GCP), "conta de serviço" (GCP e Azure), "verificação de integridade" (AWS), "sem servidor" (AWS), "rastro" (OpenTelemetry pt-BR), "corpo" e "cabeçalho" (MDN). A seção 6.3 lista os termos que as equipes usam e que o PTS-BR não aprova (GMUD, RDM, KPI, plantonista, "código HTTP"), com a alternativa de cada um.
5. **Unidades e datas sem ambiguidade.** Um único texto em R8.4 e em NT-22 define kB/KiB, bit/s, o espaço como separador de milhar e "`512Mi` é 512 MiB". R8.5 exige UTC na linha do tempo de um incidente. Os 3 arquivos (02, 03 e 04) estão alinhados.

## Problemas (ordenados por impacto)

1. **[IMPORTANTE] 02-regras.md:R7.1 × R7.5 × 06:Ex2 e Ex5: o critério dos avisos ainda dá níveis diferentes para a mesma consequência.** Os exemplos da tabela descrevem ações. As 3 perguntas descrevem consequências. Os dois métodos dão resultados diferentes:
   - A mesma consequência tem 2 níveis. R7.5 classifica como **CUIDADO** "Por 15 min, a API responde em até 2 s, em vez de 200 ms". O Ex2, procedimento 3, classifica como **ATENÇÃO** "Durante aproximadamente 2 min, a API de catálogo responde em até 2 s, em vez de 200 ms". Pela pergunta 3, as duas consequências são "degradação do desempenho". A justificativa do Ex2 ("o comando reinicia um serviço de produção") é uma ação, não uma consequência.
   - A pergunta 1 contradiz a tabela. A pergunta 1 diz "A consequência afeta [...] dados pessoais [...]? O dano é irreversível [...]? Se uma das respostas for 'sim', use PERIGO". A linha ATENÇÃO da tabela diz "Perda de dados com backup disponível. Custo não planejado". Um banco de clientes sempre tem dados pessoais, e um custo gasto é irreversível. Portanto, pela pergunta 1, as 2 linhas são PERIGO.
   - O Ex5 classifica a exclusão do banco `clientes` como PERIGO, "sem forma de recuperar todos os dados", mesmo com o backup diário. Com este raciocínio, "Perda de dados com backup disponível" nunca é ATENÇÃO, porque um backup sempre tem uma janela de perda (RPO).

   **Correção:**
   - Na pergunta 1, troque "afeta [...] dados pessoais, credenciais" por "expõe dados pessoais ou credenciais a pessoas sem permissão, ou desativa um controle de segurança".
   - Adicione à pergunta 2: "Uma perda de dados é reversível apenas se o backup tiver todos os dados até o momento da ação (backup imediatamente antes do passo ou recuperação até um ponto no tempo). Se o backup não tiver os dados de depois do último backup, use PERIGO."
   - Mova "Custo não planejado" para uma pergunta explícita ou para CUIDADO e dê um valor de referência.
   - Escreva no enunciado: "Classifique pela consequência, não pela ação. Os exemplos da tabela supõem a consequência mais comum da ação."
   - No Ex2, procedimento 3, use CUIDADO (latência de 2 s, abaixo do tempo limite de 3 s, sem erro) ou altere a consequência para uma consequência de ATENÇÃO.

2. **[IMPORTANTE] 06-exemplos.md:Ex2, "Antes de começar" e procedimento 1, passo 2: o usuário `sre` não vê as consultas que o runbook filtra.** No PostgreSQL, uma conta sem `pg_read_all_stats` (ou `pg_monitor`) que não é superusuário recebe NULL nas colunas `state` e `query_start` das sessões de outros usuários. A coluna `query` mostra `<insufficient privilege>`. O filtro `usename = 'api_catalogo' AND state = 'active' AND now() - query_start > ...` então retorna 0 linhas mesmo durante o incidente. O passo 5 manda o leitor para o procedimento 3 ou 4 e pula o cancelamento. O contexto dá ao `sre` apenas `pg_signal_backend`. **Correção:** no contexto e em "Antes de começar", escreva "O usuário `sre` tem os papéis de acesso `pg_signal_backend` e `pg_read_all_stats`". Adicione a verificação `psql ... --command "SELECT pg_has_role('sre', 'pg_read_all_stats', 'MEMBER');"`, com o resultado `t`.

3. **[IMPORTANTE] 02:R7.9 × 06:Ex3: a variável de ambiente expandida em um argumento continua visível na lista de processos.** R7.9 justifica a regra com "outros usuários do host podem ver o argumento na lista de processos" e aprova "Uma variável de ambiente que o cofre de segredos define". O Ex3 mostra `curl ... --header "Authorization: Bearer $API_TOKEN"`. O shell expande `$API_TOKEN` antes de executar o `curl`, e o valor do token aparece em `ps` e em `/proc/<pid>/cmdline` durante a requisição. O exemplo resolve o histórico, mas não resolve o risco que a regra nomeia. **Correção:** em R7.9, troque o item por "Uma variável de ambiente que a ferramenta lê de forma direta (por exemplo `PGPASSWORD`, `AWS_SECRET_ACCESS_KEY`). Não escreva a variável em um argumento (`$TOKEN`)". Adicione o item "A opção da ferramenta que lê o segredo de um arquivo, por exemplo `curl --header @<arquivo-do-cabecalho>`". No Ex3, use `--header @/run/secrets/api-header` ou explique o limite na NOTA.

4. **[IMPORTANTE] 06-exemplos.md:Ex1: 3 imprecisões de Helm no procedimento de referência.**
   - (a) `helm upgrade loja-web ./chart ... --set image.tag=v2.8.0` não passa um arquivo de valores. No Helm 3, o upgrade sem `--values` nem `--reuse-values` usa apenas o `values.yaml` do chart e o `--set`. Os valores de produção do release anterior (réplicas, recursos, host do ingress) voltam ao padrão do chart.
   - (b) `helm history --max 1` mostra a última revisão, e esta revisão pode ter o estado `failed`. O rollback para uma revisão `failed` não restaura a versão boa.
   - (c) `kubectl auth can-i update deployments` não prova a permissão do Helm, que também grava os Secrets do release no namespace.

   **Correção:**
   - (a) Use `--values chart/values-prod.yaml` e escreva o arquivo no contexto.
   - (b) Escreva no passo 2: "A coluna `STATUS` mostra `deployed`. Registre o número desta linha".
   - (c) Adicione `kubectl auth can-i create secrets --context prod-sa-east-1 --namespace loja` à seção "Antes de começar".

5. **[IMPORTANTE] 02 §5 × 06: falta o modelo de runbook e faltam os textos de recuperação (pendente da rodada 1, item 15).** As equipes de operação escrevem 4 textos sob pressão e nenhum tem regra ou exemplo:
   - restauração de backup;
   - recuperação de desastre;
   - análise pós-incidente;
   - comunicado de incidente para clientes ou para a página de status.

   O 05 §3.1 põe os runbooks como o 2º tipo do Piloto, mas o redator só tem o Ex2 como referência implícita. Também falta uma regra que exija um procedimento de reversão em uma mudança de produção, como o Ex1 faz. **Correção:**
   - Adicione a regra R5.13, "Um procedimento que altera produção tem um procedimento de reversão com o mesmo nível de detalhe".
   - Adicione ao 06 uma subseção "Modelo de runbook", com as seções fixas do Ex2: Alerta, Impacto, Antes de começar, Diagnóstico, Mitigação, Encaminhamento, Resolução e Verificação.
   - Adicione o Exemplo 9, "Restaurar o banco `pedidos` com o backup", com um aviso PERIGO de alvo (R7.8), a janela de perda (RPO) e a verificação da contagem de registros.
   - Adicione o Exemplo 10, "Comunicado de incidente", com o impacto, o horário em UTC-03:00 e a próxima atualização.

6. **[IMPORTANTE] 02:R5.9 e R7.8: os exemplos PTS-BR das regras contradizem R7.8.**
   - O exemplo PTS-BR de R5.9 ensina `kubectl apply -f deployment.yaml` e `kubectl get pods -n pagamentos` sem `--context` e sem passo de alvo. O exemplo altera uma configuração, que é exatamente o caso de R7.8 ("altera ou exclui dados, recursos ou configurações [...] Não dependa do alvo padrão"). O exemplo também usa `-n`, mas o Ex1 corrige "-n loja" para "A opção longa: `--namespace loja`".
   - O exemplo PTS-BR de R7.8 verifica `kubectl config current-context`, mas o comando destrutivo usa `--context homologacao-sa-east-1`. O passo verifica o contexto padrão, e o comando não usa o contexto padrão. O Ex1 faz a verificação certa: `kubectl cluster-info --context prod-sa-east-1`, comparado com a URL esperada.

   **Correção:**
   - Em R5.9, escreva `kubectl apply -f deployment.yaml --context homologacao-sa-east-1 --namespace pagamentos` e adicione um passo de alvo antes.
   - Em R7.8, troque o passo 3 por `kubectl cluster-info --context homologacao-sa-east-1`, com a URL esperada.
   - Decida em R5.8 a regra das opções curtas e longas. Proposta: "Use a opção longa quando a ferramenta tiver uma".

7. **[MENOR] 04:§5.5 "checklist" × 01, 05 e README: a decisão contradiz o uso.** O §5.5 diz "checklist | Ambos | **checklist**; lista de verificação [...] A especificação usa 'checklist'". O 05 usa "lista de verificação" 15 vezes e "checklist" nenhuma vez. O 01 e o README também usam "lista de verificação". Pela legenda "Ambos", o termo preferido em negrito é o principal. **Correção:** troque o preferido para "**lista de verificação**; checklist" e altere a nota para "A especificação usa 'lista de verificação'".

8. **[MENOR] 03 e 02: horas sem fuso horário contra R8.5.** Exemplos aprovados escrevem a hora sem fuso horário. 03, linhas 140, 404, 436, 505, 538, 676, 722, 746, 752, 905 e 967: "O servidor parou às 14:00", "O serviço está indisponível desde as 14:00" e "O deploy começa às 22:00". 02:R1.6 (linhas 120 e 123) e R10.9 (linha 1687) têm o mesmo problema. Em incidentes, o fuso horário é o dado que causa confusão. Também: 03, "DIA: Período de 24 horas" deve ser "24 h". **Correção:** acrescente "UTC-03:00" ou "UTC" em todos os exemplos. Adicione à regra Vale de R8.4 o padrão `\b\d{2}:\d{2}\b(?!\s*UTC)` com o nível `warning`.

9. **[MENOR] 04:§6.2 × 03: polissemias novas.**
   - "servidor" tem 2 sentidos na mesma entrada: "Computador ou programa que recebe requisições".
   - "host" ("Computador ou máquina virtual que executa um serviço") repete o 1º sentido de "servidor".
   - "repositório" é definido como apenas Git, mas o 03 (DISPONÍVEL) diz "A versão 4.1 está disponível no repositório". Neste exemplo, a palavra é um repositório de pacotes. Em operação, "repositório `apt`/`yum`/Maven" é comum.

   **Correção:**
   - Em "servidor", deixe apenas o sentido de equipamento ou VM. Para o programa, use "serviço" ou "aplicação".
   - Em "host", escreva "Use 'host' apenas em literais e em nomes de campos; em prosa, use 'servidor'". Outra opção é remover uma das 2 entradas.
   - Adicione "repositório de pacotes (o), NT-17" e corrija o exemplo de DISPONÍVEL.

10. **[MENOR] 04:NT-14: "Libere a porta 443 no firewall" usa LIBERAR fora do significado aprovado.** No 03, LIBERAR é "Fazer um recurso ficar disponível de novo" ("Libere espaço em disco"). O próprio 03 tem PERMITIR: "A regra permite tráfego na porta 443". **Correção:** escreva "Crie uma regra no firewall que permite o tráfego na porta 443 a partir do endereço `10.0.0.12`". Escreva "a partir do" porque a frase atual também não diz se `10.0.0.12` é a origem ou o destino.

11. **[MENOR] 02:R7.2: "O comando exclui a tabela `sessoes`" descreve um `DROP`, mas a consequência descreve um `TRUNCATE`.** Uma aplicação sem a tabela `sessoes` não aceita nenhum login, e esta consequência é uma indisponibilidade, não um "entrar no sistema de novo". O 04 tem o verbo TRUNCAR: "Excluir todos os registros de uma tabela do banco, sem excluir a tabela". **Correção:** escreva "O comando exclui todos os registros da tabela `sessoes`" e confirme o nível com as 3 perguntas de R7.1.

12. **[MENOR] 04:NT-12: "Remova o nó 3 do cluster antes da manutenção" ensina a ação errada.** Antes de uma manutenção, a equipe drena o nó (`kubectl drain`) e marca o nó como não programável (`kubectl cordon`). Remover o nó (`kubectl delete node`) é outra operação. **Correção:** escreva "Antes da manutenção, execute o comando `kubectl drain` no nó 3". Adicione ao §5.5 "drain → Manter como literal (comando)" ou crie um verbo técnico DRENAR com o significado "mover as cargas de um nó para outros nós antes de uma manutenção".

13. **[MENOR] 04:§6.1: faltam siglas de infraestrutura e de segurança.** Para uma equipe de infraestrutura, de suporte ou de segurança, estas siglas são diárias e não estão na tabela: LDAP, AD, SAML, OIDC, DHCP, NTP, LAN, WAN, VLAN, WAF, DDoS, SIEM, RAID e EDR. Com R8.7, cada runbook de rede ou de identidade precisa da forma por extenso de cada uma. O glossário também não tem "chave SSH", "root" e "superusuário", e "dados pessoais sensíveis" (LGPD, art. 5º, II) também falta. **Correção:** adicione estas siglas e estes termos ao §6.1 e ao §6.2, com gênero e categoria. Exemplos: "o LDAP (NT-09)", "o WAF (NT-14)", "o SIEM (NT-01)".

14. **[MENOR] 04:§6.2 "severidade" × 05 §4.3: uma palavra com 2 escalas.** O glossário define "severidade" como "Nível do impacto de um incidente ou de um defeito, por exemplo SEV1 a SEV4". O 05 usa "severidade" para os desvios de redação S1 a S3. Um revisor de um runbook usa as 2 escalas no mesmo documento. Também: CK-7.2 (05) diz "Cada aviso tem comando, risco e consequência", mas R7.3 diz "instrução", e o glossário reserva "comando" para o texto digitado no terminal ("Para uma frase no imperativo, use INSTRUÇÃO"). **Correção:** no 05, chame os níveis de desvio de "gravidade do desvio (S1 a S3)" ou escreva "severidade do desvio" em todas as ocorrências. Em CK-7.2, troque "comando" por "instrução".

15. **[MENOR] tools/ci/docs-lint.yml: o workflow de exemplo não segue o privilégio mínimo do próprio PTS-BR.**
    - As permissões `pull-requests: write` e `checks: write` valem para o workflow inteiro. Com isso, também o job `regras` recebe as 2 permissões, e este job executa o Python do próprio pull request (`tools/check_spec.py`). Em um PR de um branch do mesmo repositório, o token tem escrita.
    - O passo "Instalar o Vale" usa `curl ... | tar` sem verificar o SHA-256 da versão.
    - A ação de terceiros `errata-ai/vale-action@v2` usa uma tag, não o SHA de um commit.

    **Correção:** escreva `permissions: contents: read` no nível do workflow e `pull-requests: write` apenas no job `lint`. Baixe o arquivo `vale_..._checksums.txt` e verifique o arquivo com `sha256sum --check`. Fixe as ações pelo SHA do commit, com a versão em um comentário.

16. **[MENOR] 06:Ex7: a senha temporária vai para o gestor, sem troca obrigatória.** O PERIGO do passo 6 trata o canal (o cofre de segredos), mas o gestor fica com a senha de todos os sistemas do colaborador novo. O procedimento também não exige a troca da senha no primeiro login. No Microsoft Entra ID, a prática é a opção "Exigir que o usuário altere a senha no próximo login" ou um passe de acesso temporário. **Correção:** no passo 2, adicione "Marque a opção **Exigir alteração da senha no próximo login**". Na verificação (passo 8), confirme a opção.

## O que levaria a nota a ≥ 8

1. Em R7.1, troque "afeta dados pessoais" por "expõe [...] a pessoas sem permissão" e defina "perda com backup" pela cobertura do backup (RPO). Escreva "classifique pela consequência, não pela ação". Depois, alinhe o Ex2, procedimento 3, com o exemplo de CUIDADO de R7.5 (problema 1). Com isto, CK-7.1 (S1) tem uma resposta única.
2. Corrija os 3 defeitos técnicos dos exemplos que uma equipe de operação vai copiar: `pg_read_all_stats` no Ex2 (problema 2), o segredo em um argumento em R7.9 e no Ex3 (problema 3), e `--values` mais a revisão `deployed` no Ex1 (problema 4).
3. Alinhe os exemplos PTS-BR de R5.9 e de R7.8 com R7.8: alvo explícito e verificação do mesmo contexto que o comando usa (problema 6).

## O que levaria a nota a 9 (depois dos itens acima)

4. Adicione o modelo de runbook, a regra R5.13 (reversão obrigatória) e os exemplos de restauração e de comunicado de incidente (problema 5).
5. Corrija os itens menores de consistência: "checklist" (7), fuso horário nos exemplos (8), "servidor", "host" e "repositório" (9), LIBERAR (10), TRUNCAR em R7.2 (11) e o nó drenado (12). Depois, complete as siglas de infraestrutura (13).

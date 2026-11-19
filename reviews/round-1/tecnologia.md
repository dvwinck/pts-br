---
lente: tecnologia
rodada: 1
notas: {correcao: 7, completude: 6, aplicabilidade: 7, coerencia: 6.5, valor: 7.5}
nota_final: 6.8
---

Verificações objetivas feitas com scripts em
`<pasta-de-trabalho-local>/check_ti.py`
(conflitos 03 × 04, termos "Português" do 04 §5.5 usados em prosa, unidades, palavras do 06 sem entrada, cobertura de termos de TI)
e `siglas.py` (siglas do 06 × glossário-base × R8.7). Nenhum arquivo da especificação foi alterado.

## Pontos fortes (até 5)

1. **Proibição de verbos com radical estrangeiro (04 §5.4), com alternativa para cada um.** A tabela cobre o jargão real das equipes brasileiras ("deployar", "commitar", "setar", "dropar", "tunar", "shippar"). A regra é binária e o linter consegue verificar. É a decisão de maior impacto prático do pacote.
2. **Critérios E1–E5 com teste de uso estável (04 §5.2).** O teste se baseia na interface pt-BR da ferramenta, em norma ABNT ou na tradução oficial ISO. A maioria das decisões bate com o uso no Brasil: "plantão" (on-call), "chamado" (ticket), "navegador" e "tempo limite" (timeout) em português. "deploy", "commit", "branch", "pipeline", "bucket" e "payload" ficam em inglês. A rejeição de "implantação" tem justificativa explícita: a confusão com "implementação".
3. **Verbos técnicos com a coluna "Uso não técnico" (04 §4.2).** ESCALAR (capacidade) × "encaminhar" (incidente), REVERTER para rollback, REVOGAR, ROTACIONAR, TRUNCAR e MASCARAR têm limites claros. No 03, as fronteiras RESTAURAR × RECUPERAR, PARAR × DESLIGAR e LIMPAR × EXCLUIR resolvem ambiguidades que causam incidentes. As saídas para "derrubar", "matar" e "subir" também resolvem ambiguidades desse tipo.
4. **Estrutura dos avisos (R7.3 a R7.6) e prioridade de adoção (05 §3.1).** O aviso segue a ordem comando, risco, consequência. A consequência precisa ser concreta, e o PERIGO cobre a exposição de credenciais e de dados pessoais. A fase piloto começa por avisos e runbooks. A severidade sobe de S2 para S1 em um passo irreversível (05 §4.3). Para operações, esta é a ordem certa.
5. **Regras de procedimento prontas para operação.** R5.8 proíbe o prompt e o `&&`. R8.9 define o espaço reservado `<nome>` e a explicação depois do bloco. R5.9 exige um passo final de verificação, e R5.4 proíbe "se necessário". O Exemplo 1 aplica bem estas regras: a mensagem exata do `kubectl rollout status` e a opção `--timeout 10m` substituem "leva alguns minutos".

## Problemas (ordenados por impacto)

1. **[BLOQUEANTE] 02-regras.md:R7.1 × R7.5 × R7.7: a fronteira entre PERIGO e ATENÇÃO se contradiz nos próprios exemplos.** A tabela põe "indisponibilidade total de um sistema de produção" em PERIGO e "indisponibilidade parcial ou temporária" em ATENÇÃO. O exemplo de R7.5 ("O reinício para todos os pods por 5 a 10 min. Durante este tempo, os clientes não podem acessar a loja.") descreve uma indisponibilidade total e temporária e usa ATENÇÃO. O exemplo de R7.7 ("O comando exclui todos os índices do Elasticsearch... os clientes não podem procurar produtos na loja por até 6 h") descreve uma indisponibilidade parcial, temporária e recuperável por reindexação, mas usa PERIGO. CK-7.1 só tem verificação humana (05 §6.7), e os avisos são o primeiro tipo de documento do piloto. Com estes exemplos, cada revisor classifica de um jeito. **Correção:** troque a tabela por uma decisão em dois eixos. (a) Reversibilidade: "sem procedimento de recuperação documentado" = PERIGO; "recuperação com backup, reprocessamento ou reindexação" = ATENÇÃO; "recuperação imediata pelo próprio leitor" = CUIDADO. (b) Exposição: credencial, dado pessoal ou acesso público = sempre PERIGO. Escreva também: "Uma indisponibilidade total com duração conhecida e retorno automático é ATENÇÃO." Depois, altere o exemplo de R7.7 para ATENÇÃO ou troque a consequência por uma perda sem recuperação.

2. **[IMPORTANTE] 02-regras.md:R8.7 × 04-termos-tecnicos.md:§6 × 06-exemplos.md: a regra das siglas não serve para um documento de TI.** O glossário-base tem só 9 siglas: API, CI, DNS, IP, SLA, SLI, SLO, URL e VPN. R8.7 `[lint]` exige a forma por extenso de todas as outras siglas. O próprio 06 viola a regra: o Ex2 escreve "código HTTP `500`", o Ex3 escreve "objeto JSON" e "códigos HTTP", o Ex1 escreve "UTC-3" e o Ex7 escreve "ID", tudo sem definição. Ao mesmo tempo, NT-09 e NT-10 mandam "Use a sigla oficial" sem exigir a definição. Com o linter ativo, cada runbook gera alertas para HTTP, JSON, CPU, SSH, TLS e SQL, e o revisor aprende a ignorar o alerta. **Correção:** adicione ao 04 §6 a tabela "Siglas de uso geral, sem definição": HTTP, HTTPS, TLS, SSH, TCP, UDP, JSON, YAML, CSV, XML, SQL, CPU, RAM, GPU, ID, UTC, PDF, USB, SSD e HTML. Altere a exceção de R8.7: "uma sigla do glossário-base, desta tabela ou das categorias NT-09, NT-10 e NT-22 não precisa de definição". Mantenha a definição obrigatória para SSO, IdP, RBAC, IAM, MTTR, RPO, RTO e GMUD.

3. **[IMPORTANTE] 04-termos-tecnicos.md:§6: faltam termos centrais de operação e de segurança no glossário-base.** O script mostrou que os textos normativos usam estas palavras sem entrada no 03 nem no 04:
   - "serviço": 30 ocorrências no 02;
   - "conta";
   - "papel";
   - "cofre de segredos": 9 ocorrências no 02, 04 e 06, e é o exemplo de NT-16;
   - "certificado": o glossário só tem "certificado digital";
   - "rastros": aparece em INSTRUMENTAR;
   - "percentil" e RPO, RTO e MTTR: aparecem nos exemplos de NT-21 e não têm definição;
   - "vulnerabilidade" e "dados pessoais": aparecem na tabela de R7.1.

   Faltam também termos que uma equipe de operação usa todos os dias: failover, réplica primária e réplica secundária, recuperação de desastre, restauração, retenção, conta de serviço, privilégio mínimo, chave SSH, `root` e `sudo` (R5.1 usa `sudo`), shell, terminal, kernel, observabilidade, alerta (só no 03), limite de taxa (rate limit), cota, incidente de segurança, vazamento de dados, IOPS e largura de banda. **Correção:** adicione ao §6 uma entrada para cada um destes termos, com gênero, categoria e definição. Para os termos em inglês, adicione a decisão no §5.5: "failover" Manter (E4); "rate limit" Português, "limite de taxa" (E3); "service account" Português, "conta de serviço" (E3, interface pt-BR do GCP e do Azure).

4. **[IMPORTANTE] 02:R5.6 × 04:NT-16 × NT-19 × 06:Ex3 e Ex7: o vocabulário de acesso não é estável (P2).** O mesmo conceito, "role" em RBAC e IAM, aparece com três palavras. O Ex3 diz "use o nome técnico 'papel' (NT-16)". R5.6 diz "Confirme que a sua conta tem a função `cluster-admin`". O Ex7 usa "perfil de acesso". "Função" também é o nome técnico de código (03, D7). "Papel" também nomeia a responsabilidade de uma pessoa no processo (NT-19, "Papéis e funções de pessoas"). As consoles em pt-BR (AWS IAM, Azure RBAC) mostram "Função" para role. **Correção:** crie a entrada "papel de acesso (o), NT-16: conjunto de permissões que um sistema atribui a uma identidade". Escreva a nota: "Se a interface mostrar **Função**, o rótulo é literal (E1)." Altere R5.6 para "o papel de acesso `cluster-admin`". Mantenha "papel" sem qualificador só para NT-19.

5. **[IMPORTANTE] 02-regras.md (várias regras) × 04:§5.5 e NT-24 × 06: "status" é proibido em prosa, mas 02 usa a palavra em prosa.** O §5.5 decide "status → estado (Português)" e "'Status' apenas em literais". O 02 usa "status" em prosa PTS-BR em mais de 15 linhas, por exemplo:
   - R5.4: "Se o status do usuário for **Inativo**";
   - R5.9: "Verifique o status dos pods" e "Todos os pods mostram o status `Running`";
   - R4.2: "têm o status `Ready`";
   - R2.3: "Verifique o código de status da resposta";
   - R10.7, no título: "mensagens de status".

   O 06 segue a decisão ("Todos os pods mostram o estado "Running""). Além disso, R5.9 escreve o valor em código, e NT-24 e o 06 escrevem o valor entre aspas. **Correção:** substitua "status" por "estado" nestes exemplos de 02. Escreva os valores de estado entre aspas, como NT-24 manda ("o estado "Running""). Em R2.3, use "Verifique o código HTTP da resposta", como NT-08 já faz. Altere o título de R10.7 para "mensagens de andamento e de sucesso".

6. **[IMPORTANTE] 04:§5.5 "registry → repositório": a decisão contém um erro técnico.** Na OCI e no Docker, um registry (`ghcr.io`, Amazon ECR) contém repositórios (`org/loja-web`). Com a decisão atual, "registry", "repository" de imagens e repositório Git têm o mesmo nome. A definição do glossário reforça a mistura: "repositório: local que armazena código, pacotes ou imagens". Com isso, "Envie a imagem para o repositório" fica ambíguo. "Registro" também não serve, porque o glossário já define "registro" como uma linha de tabela. **Correção:** mude a decisão para "registry, Manter (o), E4". Defina o termo como "serviço que armazena repositórios de imagens de contêiner ou de pacotes". Mantenha "repositório de imagens" para o repositório dentro do registry.

7. **[IMPORTANTE] 02:R8.4 e R8.5 × 04:NT-22 × 03 × 05: as unidades se contradizem e há lacunas.**
   - NT-22 lista "KB". R8.4 lista "kB", e a IEC 80000-13, que o próprio NT-22 cita, usa o "k" minúsculo.
   - NT-22 lista "Mbit/s", mas R8.4 não tem unidades de bit. R8.4 proíbe só "Gb para gigabyte" e não diz como escrever a taxa de um link.
   - Nenhuma regra diz quando usar prefixo binário ou decimal. R8.4 usa "16 GB", e R5.4 e NT-22 usam "512 MiB".
   - O 03 escreve a unidade por extenso depois de um número em 40 exemplos ("Monitore o uso de CPU por 10 minutos", "Aguarde 30 segundos"). O 04 faz o mesmo em T4 ("25 minutos") e em EXPIRAR ("1 hora"). O 02 e o 06 usam o símbolo ("10 min").
   - O 05 usa "1.000" 11 vezes, e R8.4 proíbe o ponto como separador de milhar.
   - R8.5 diz "ISO 8601", mas o formato aprovado "09:30 UTC-3" não é ISO. A forma ISO é "09:30-03:00".

   **Correção:**
   - (a) No NT-22, troque "KB" por "kB".
   - (b) Em R8.4, adicione: "Para taxa de dados, use bit/s com prefixo (Mbit/s, Gbit/s). Não use Mbps nem Gb."
   - (c) Adicione: "Use o prefixo da unidade que o sistema configura ou mostra. Memória e limites de contêiner usam o prefixo binário (MiB, GiB)."
   - (d) Adicione: "Depois de um número, escreva o símbolo, não o nome da unidade." Corrija os exemplos do 03, do 04 e do 05.
   - (e) Em R8.5, escreva "formato derivado da ISO 8601" ou aprove "-03:00". Recomende UTC para a linha do tempo de um incidente.

8. **[IMPORTANTE] 02-regras.md:Seção 7: a seção não cobre riscos frequentes de TI.**
   - Nenhuma regra manda mostrar o alvo de um comando destrutivo: o contexto do cluster, o host, a conta ou a região. O exemplo de R7.4 ("Confirme que o terminal está conectado ao banco de homologação") não diz como confirmar.
   - Nenhuma regra trata de segredos em comandos: a senha como argumento, o histórico do shell, a captura de tela, o log ou o chamado. NT-16 só proíbe o valor real no documento.
   - A tabela de R7.1 não tem exemplos para estes riscos: desativar um controle de segurança (verificação TLS, MFA, log de auditoria), dar privilégio de administrador, deixar um recurso público (bucket público, regra `0.0.0.0/0`), excluir uma chave de criptografia (perda definitiva dos dados cifrados) e alterar um registro DNS (o rollback depende do TTL).
   - O exemplo "Alterar uma regra de firewall" está em ATENÇÃO de forma genérica, mas abrir uma porta para a internet é PERIGO.

   **Correção:**
   - (a) Crie a regra R7.8: "Antes de um passo que altera produção, escreva um passo que mostra o alvo e o resultado esperado." Exemplo: `kubectl config current-context` → `prod-sa-east-1`.
   - (b) Crie a regra R7.9: "Não escreva um segredo em um argumento de comando. Leia o segredo do cofre ou de uma variável de ambiente." Exemplo de aviso PERIGO: "Não digite a senha no comando. O shell grava o comando no histórico..."
   - (c) Adicione os 5 riscos acima à coluna "Exemplos de TI" de R7.1.

9. **[IMPORTANTE] 06-exemplos.md:Exemplo 2 (runbook): uma equipe de operação não usaria este runbook sem correções.**
   - (a) O runbook não tem a seção "Antes de começar" (R5.6). Faltam o acesso `psql` ao `catalogo-db-01` como `sre`, o local da credencial, a permissão no namespace `catalogo` e o acesso ao PagerDuty.
   - (b) O passo 1 de "Diminuir a latência" cancela "cada consulta do passo 3" sem aviso. O `pg_cancel_backend` também devolve um erro à aplicação. A consulta do passo 3 não filtra `backend_type`, e por isso pode cancelar o autovacuum, um `pg_dump` de backup ou uma migração. O aviso só existe para `pg_terminate_backend`, o que viola R7.4.
   - (c) O aviso diz "O cliente da API de catálogo recebe o código HTTP `500`". Pelo glossário, "cliente" é uma pessoa ou uma empresa, e o programa é a "aplicação cliente".
   - (d) O passo 2 diz "Se uma consulta continuar ativa depois de 1 min", mas não dá o comando que verifica isso.

   **Correção:**
   - Adicione a seção "Antes de começar" com estes 4 itens.
   - Adicione `AND backend_type = 'client backend'` à consulta e exclua o usuário de backup.
   - Escreva um aviso ATENÇÃO antes do passo 1, com a consequência "a requisição da aplicação cliente termina com erro".
   - Troque "o cliente" por "a aplicação cliente".
   - No passo 2, repita o comando do passo 3 da análise.

10. **[IMPORTANTE] 06-exemplos.md:Exemplo 1: o fluxo do rollback está incompleto.** Depois de `helm rollback`, no passo 7, o texto não diz o que fazer. O leitor segue para os passos 8 e 9 e "verifica" a versão antiga como se o deploy tivesse sucesso. O passo 4 só trata "Success" e "Failure", mas o GitHub Actions também mostra "In progress" e "Cancelled", o que viola R9.5. Além disso, `curl --silent` devolve o código de saída 0 com um HTTP 500, e a verificação fica fraca. **Correção:** no ramo do rollback, escreva "Verifique o estado dos pods (passo 8). Este procedimento termina neste passo. Registre um incidente com a saída do passo 7." No passo 4, escreva "Se o estado não for "Success", ...". No passo 9, use `curl --fail --silent ...`.

11. **[MENOR] 04:§5.1 × 02:R1.7: há termos em inglês sem decisão no §5.5, nos próprios textos normativos.** O §5.1 diz que o PTS-BR aceita um estrangeirismo "apenas se a palavra estiver na lista da seção 5.5". Estes termos não estão na lista:
    - "gateway": está no glossário-base, mas não no §5.5;
    - "throughput": NT-21;
    - "serverless": NT-13;
    - "console": no exemplo PTS-BR de R1.7, "Entre no console da AWS";
    - "deployment": "Escale o deployment para 6 réplicas" (ESCALAR). É um objeto do Kubernetes e deve ser um literal;
    - "SDK" e "QA": nos exemplos de INSTRUMENTAR e HOMOLOGAR;
    - "chart": Helm.

    O Ex3 também usa "cabeçalho" sem entrada. "Payload" ficou com o corpo da requisição HTTP, mas a MDN em pt-BR usa "corpo". **Correção:** adicione ao §5.5 "gateway, Manter (o)", "throughput, Português, vazão" e "console, Manter (o)". No exemplo de ESCALAR, escreva "Escale o objeto `Deployment` `api` para 6 réplicas". Adicione "header → cabeçalho" e "body → corpo (E3, MDN pt-BR)". Restrinja "payload" a mensagens, eventos e webhooks.

12. **[MENOR] 04:§6 × 03: há polissemias de TI que violam P1.**
    - "Painel": o glossário define "painel" como dashboard (NT-05). O 03 usa "Obtenha o token no painel" e "Acesse o painel" no sentido de portal ou console. RECOLHER usa "Recolha o painel lateral" no sentido de área da tela.
    - "Instância": o glossário define uma máquina virtual de nuvem, mas INSTANCIAR cria o objeto de uma classe, e as equipes também falam em "instância do banco".
    - "Agente": o glossário define um programa (NT-12). O 02 usa "agente" no sentido gramatical (R3.3, R4.4) e chama o `logrotate` de agente.
    - "Operador": NT-19 usa a palavra para uma pessoa, e a LGPD usa a mesma palavra para outra figura jurídica.

    **Correção:** use "portal" ou "console" para a interface de administração e "área" para a parte da tela. Escreva "instância de banco" e "instância de máquina virtual" e limite a entrada atual. Use "sujeito" no texto gramatical do 02. Adicione a nota "operador (LGPD) é literal de norma (NT-23)".

13. **[MENOR] 01, 04, 05 e README: a terminologia não é a mesma nos arquivos.** O 01 §2.1 usa "Notas de release", mas o §5.5 decide "notas de versão". O 05 e o README usam "checklist" 15 vezes, mas o §5.5 decide "lista de verificação". O glossário de 04 escreve "MAIOR.MENOR.CORREÇÃO", e o README e o 05 §8.1 escrevem "MAJOR.MINOR.PATCH". **Correção:** escolha uma forma para cada termo e aplique a forma em todos os arquivos. Se o 05 continuar com "checklist", mude a decisão do §5.5 para "Ambos".

14. **[MENOR] 04:§5.5 e §7: faltam os termos do dia a dia das equipes brasileiras como sinônimos não aprovados.** "GMUD" e "RDM" só aparecem na tabela de mudanças do Ex1. "Plantonista" também. "Acionar o plantão" não tem alternativa: 03 manda trocar "acionar" por ATIVAR ou PRESSIONAR, e nenhuma das duas serve para chamar uma pessoa. **Correção:** adicione ao §5.5 ou ao 03:
    - "GMUD, RDM → solicitação de mudança";
    - "plantonista → analista de plantão";
    - "acionar (uma pessoa) → Envie um alerta ao analista de plantão no <ferramenta>".

15. **[MENOR] 06-exemplos.md: falta um modelo de runbook e faltam tipos de texto de operação.** O 06 não tem um modelo com seções fixas: alerta, impacto, diagnóstico, mitigação, encaminhamento, verificação e rollback. Também não tem exemplos de restauração de backup ou de recuperação de desastre, de análise pós-incidente e de comunicado de incidente para a página de status. São textos que a equipe escreve sob pressão. **Correção:** adicione o Exemplo 9, "Restaurar o banco `pedidos` com o backup", com um aviso PERIGO para o alvo. Adicione também um modelo de runbook em uma subseção do 02 §5 ou do 06.

## O que levaria a nota a ≥ 8

1. Na Seção 7, troque a tabela de R7.1 pelo critério de reversibilidade e exposição do problema 1. Corrija os exemplos de R7.5 e R7.7. Adicione R7.8 (alvo do comando), R7.9 (segredos em comandos) e os riscos de TI do problema 8.
2. Adicione ao 04 §6 a tabela de siglas de uso geral e altere a exceção de R8.7 (problema 2). Depois disso, o 06 fica conforme sem exceções.
3. Complete o glossário-base com os cerca de 40 termos dos problemas 3 e 4. Inclua "papel de acesso", "cofre de segredos", "serviço" e "conta". Corrija "registry" (problema 6).
4. Unifique "status" e "estado", os formatos de unidade, o "kB" e o separador de milhar no 02, 03, 04 e 05 (problemas 5, 7 e 13). Rode de novo o script `check_ti.py`: as seções B e C devem mostrar zero ocorrências fora das tabelas de decisão.
5. Corrija os Exemplos 1 e 2 (problemas 9 e 10). Assim, o 06 serve como referência de runbook para uma equipe de operação.

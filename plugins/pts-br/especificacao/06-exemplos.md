# PTS-BR: Português Técnico Simplificado

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · **06 Exemplos** · [Versões](CHANGELOG.md)

## Parte 6: Exemplos

Versão 1.0.0, 2026-11-18

Esta parte contém 10 textos completos em 2 formas: a forma comum e a forma PTS-BR. Leia [`01-introducao.md`](01-introducao.md) e [`02-regras.md`](02-regras.md) antes desta parte.

| Número | Exemplo | Tipo de texto |
|---|---|---|
| 1 | Deploy de uma aplicação | Procedimento |
| 2 | Latência alta em um banco de dados | Runbook de incidente |
| 3 | Endpoint `POST /v1/usuarios` | Documentação de API |
| 4 | Mensagens de erro e diálogos de confirmação | Textos de interface |
| 5 | Exclusão de dados e cópia de um token | Avisos de segurança |
| 6 | Versão 3.0.0 da API de pedidos | Notas de versão |
| 7 | Acesso de um colaborador novo | Procedimento de um processo interno |
| 8 | Biblioteca `brvalida` | Arquivo `README.md` |
| 9 | Restauração do banco `pedidos` com um backup | Runbook de restauração |
| 10 | Comunicados de um incidente na página de status | Comunicado de incidente |

Cada exemplo tem 4 partes:

1. Contexto: o tipo de texto, o leitor e todos os dados do texto PTS-BR que o texto "Antes" não mostra.
2. Antes: o texto na forma comum em equipes do Brasil.
3. PTS-BR: o texto "Antes" na forma PTS-BR, de acordo com [`02-regras.md`](02-regras.md), [`03-dicionario.md`](03-dicionario.md) e [`04-termos-tecnicos.md`](04-termos-tecnicos.md).
4. Alterações: uma tabela com as partes principais do texto "Antes", o ID da regra e a forma PTS-BR.

Os textos "Antes" e a coluna "Trecho original" são as únicas partes deste arquivo fora do PTS-BR. Os nomes de sistemas, de servidores e de valores são exemplos. O domínio `exemplo.com.br` não é um domínio real.

Nos textos PTS-BR, os títulos do documento de exemplo são títulos Markdown (`####` e `#####`). Os avisos são blocos com o sinal `>` no início da linha, dentro do exemplo ([R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor)).

Os exemplos 2 e 9 são modelos de runbook:

- Um runbook de incidente (exemplo 2) tem estas seções, nesta ordem: "Alerta", "Impacto", "Procedimentos" e "Antes de começar". Depois, o runbook tem os procedimentos que analisam e resolvem o problema, "Encaminhar o incidente" e "Resolver o incidente".
- Um runbook de restauração (exemplo 9) tem estas seções, nesta ordem: o bloco da regra [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor), "Objetivos de recuperação", "Procedimentos" e "Antes de começar". Depois, o runbook tem os procedimentos. Os procedimentos verificam o backup antes da restauração e verificam os dados e o serviço depois da restauração. O runbook também tem um procedimento de rollback (regra [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor)).

Os avisos dos exemplos usam os níveis da regra [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), pela consequência. A mesma consequência tem o mesmo nível em todos os exemplos:

| Consequência | Nível | Exemplos |
|---|---|---|
| Perda dos dados de depois do último backup. Uma credencial visível para outras pessoas. | PERIGO | 3, 5, 7 e 9 |
| Indisponibilidade ou perda de função, parcial ou total, com recuperação conhecida | ATENÇÃO | 1, 2, 6 e 9 |
| Latência maior, sem erros. Uma tarefa que o leitor faz de novo. | CUIDADO | 2 e 5 |

---

## Exemplo 1: Procedimento de deploy de uma aplicação web

Contexto: a equipe de operação executa o deploy da aplicação `loja-web` no cluster de produção `prod-sa-east-1` com o Helm. Estes dados não estão no texto "Antes":

- A solicitação de mudança da versão 2.8.0 é a `MUD-4512`. A solicitação de mudança tem o nome do responsável pela versão.
- O papel de acesso `deployer` dá a permissão de deploy no namespace `loja`. O Helm 3 altera os objetos `Deployment` com o verbo `patch` da API do Kubernetes.
- O Helm grava cada deploy em um objeto `Secret` do namespace. Portanto, o papel de acesso `deployer` tem os verbos `list`, `create` e `update` para os objetos `Secret`.
- O arquivo `chart/values-prod.yaml` do repositório tem os valores de produção do chart: o número de réplicas, os recursos e o host da aplicação. Sem este arquivo, o comando `helm upgrade` usa os valores padrão do chart.
- O histórico do Helm mostra o estado de cada deploy na coluna `STATUS`. Apenas o deploy em uso tem o estado `deployed`. Um deploy com falha tem o estado `failed`.
- O deploy substitui os pods em 3 a 5 min. Durante este tempo, a aplicação recusa aproximadamente 10% das requisições.
- A equipe de operação executa deploys em produção apenas entre 22:00 e 06:00 UTC-03:00.
- O pipeline do GitHub Actions gera a imagem da tag. A página **Actions** mostra um destes estados: **Queued**, **In progress**, **Success**, **Failure**, **Cancelled** ou **Skipped**.

### Antes

> **Como fazer o deploy da loja-web em produção.**
>
> Antes de tudo é necessário ter acesso ao cluster de prod e a GMUD aprovada.
>
> 1. Fazer o checkout na main e dar um pull pra pegar as últimas alterações.
> 2. Checar se a tag da release foi criada (ex: v2.8.0), caso não tenha sido criada deve-se criar a mesma.
> 3. Verificar se o pipeline está verde, se estiver vermelho não prossiga com o deploy e avise o responsável pela release.
> 4. Setar o contexto do kubectl para o cluster de produção.
> 5. Rodar o helm upgrade passando a tag da imagem: `$ helm upgrade loja-web ./chart -n loja --set image.tag=v2.8.0`
> 6. Ficar acompanhando o rollout até que todos os pods subam, o que normalmente leva alguns minutos.
> 7. Caso o rollout demore muito, deverá ser feito o rollback da aplicação.
> 8. Após isso, validar se a aplicação está respondendo normalmente no /health.
>
> Obs.: o deploy derruba os pods, então vai estar ocorrendo indisponibilidade parcial durante alguns minutos. Recomenda-se fazer fora do horário de pico!

### PTS-BR

> #### Executar o deploy da aplicação `loja-web` em produção
>
> Este documento tem 3 procedimentos: "Preparar o deploy", "Executar o deploy" e "Reverter o deploy".
>
> ##### Antes de começar
>
> - Confirme que a solicitação de mudança `MUD-4512` da versão 2.8.0 tem o estado **Aprovada**.
> - Identifique o responsável pela versão 2.8.0 na solicitação de mudança `MUD-4512`.
> - Confirme que a sua conta pode criar um incidente no PagerDuty.
> - Instale estas 3 ferramentas:
>   - o Git 2.23 ou uma versão mais nova
>   - a ferramenta `kubectl` 1.30 ou uma versão mais nova
>   - a ferramenta `helm` 3.14 ou uma versão mais nova
> - Confirme que a sua conta tem o papel de acesso `deployer` no namespace `loja` do cluster `prod-sa-east-1`:
>   ```shell
>   kubectl auth can-i patch deployments --context prod-sa-east-1 --namespace loja
>   ```
>   O comando mostra a resposta `yes`.
> - Confirme que a sua conta pode criar os objetos `Secret` do Helm no namespace `loja`:
>   ```shell
>   kubectl auth can-i create secrets --context prod-sa-east-1 --namespace loja
>   ```
>   O comando mostra a resposta `yes`.
>
> ##### Preparar o deploy
>
> 1. Na pasta do repositório `loja-web`, obtenha as tags do repositório remoto:
>    ```shell
>    git fetch --tags origin
>    ```
> 2. Verifique se a tag `v2.8.0` existe:
>    ```shell
>    git tag --list v2.8.0
>    ```
>    - Se o comando mostrar a tag `v2.8.0`, vá para o passo 3.
>    - Se o comando não mostrar nenhuma tag, siga o procedimento "Criar a tag de uma versão" antes do passo 3.
> 3. Atualize a pasta local para a tag `v2.8.0`:
>    ```shell
>    git switch --detach v2.8.0
>    ```
>    O comando mostra a mensagem "HEAD is now at" e o commit da tag `v2.8.0`.
> 4. Na página **Actions** do repositório `loja-web`, verifique o estado do pipeline da tag `v2.8.0`:
>    - Se o estado for **Success**, siga o procedimento "Executar o deploy".
>    - Se o estado for **Queued** ou **In progress** por menos de 30 min, repita o passo 4 depois de 5 min.
>    - Se o estado for **Queued** ou **In progress** por 30 min ou mais, informe o responsável pela versão. Este procedimento termina neste passo.
>    - Se o estado for outro valor, informe o responsável pela versão. Este procedimento termina neste passo.
>
> ##### Executar o deploy
>
> 1. Verifique a URL do cluster `prod-sa-east-1`:
>    ```shell
>    kubectl cluster-info --context prod-sa-east-1
>    ```
>    O comando mostra a URL do cluster de produção:
>    ```text
>    Kubernetes control plane is running at https://k8s.prod-sa-east-1.exemplo.com.br
>    ```
>    - Se o comando mostrar a URL `https://k8s.prod-sa-east-1.exemplo.com.br`, vá para o passo 2.
>    - Se o comando mostrar outra URL, informe o responsável pela versão. Este procedimento termina neste passo.
> 2. Obtenha os últimos deploys da aplicação `loja-web` no histórico do Helm:
>    ```shell
>    helm history loja-web --kube-context prod-sa-east-1 --namespace loja --max 10
>    ```
>    O comando mostra uma linha para cada deploy. A coluna `STATUS` mostra o valor `deployed` na linha do deploy em uso.
>
>    - Se uma linha mostrar o valor `deployed`, vá para o passo 3.
>    - Se nenhuma linha mostrar o valor `deployed`, informe o responsável pela versão. Este procedimento termina neste passo.
> 3. Na solicitação de mudança `MUD-4512`, registre o número da coluna `REVISION` da linha `deployed`, por exemplo `41`.
>
>    Registro: o número do deploy em uso, na solicitação de mudança `MUD-4512`.
>
> > **ATENÇÃO:** Execute o deploy apenas entre 22:00 e 06:00 UTC-03:00. O deploy substitui todos os pods da aplicação `loja-web` no cluster de produção `prod-sa-east-1`. Durante 3 a 5 min, a aplicação recusa aproximadamente 10% das requisições dos clientes.
>
> 4. Execute o deploy da versão 2.8.0 no cluster `prod-sa-east-1`, com os valores de produção:
>    ```shell
>    helm upgrade loja-web ./chart \
>      --kube-context prod-sa-east-1 \
>      --namespace loja \
>      --values ./chart/values-prod.yaml \
>      --set image.tag=v2.8.0
>    ```
>    O comando mostra esta mensagem:
>    ```text
>    Release "loja-web" has been upgraded. Happy Helming!
>    ```
> 5. Verifique o estado do deploy novo no histórico do Helm:
>    ```shell
>    helm history loja-web --kube-context prod-sa-east-1 --namespace loja --max 1
>    ```
>    - Se a coluna `STATUS` mostrar o valor `deployed`, vá para o passo 6.
>    - Se a coluna `STATUS` mostrar outro valor, siga o procedimento "Reverter o deploy".
> 6. Monitore o deploy:
>    ```shell
>    kubectl rollout status deployment/loja-web --context prod-sa-east-1 --namespace loja --timeout 10m
>    ```
>    A mensagem "successfully rolled out" indica o fim do deploy. A mensagem "timed out waiting for the condition" indica que os pods novos não iniciaram em 10 min.
>
>    - Se o comando mostrar a mensagem "successfully rolled out", vá para o passo 7.
>    - Se o comando mostrar outra mensagem, siga o procedimento "Reverter o deploy".
> 7. Verifique o estado dos pods:
>    ```shell
>    kubectl get pods \
>      --context prod-sa-east-1 \
>      --namespace loja \
>      --selector app.kubernetes.io/name=loja-web
>    ```
>    - Se a coluna `STATUS` mostrar o valor `Running` em todos os pods, vá para o passo 8.
>    - Se um pod mostrar outro valor na coluna `STATUS`, siga o procedimento "Reverter o deploy".
> 8. Teste o endpoint `/health` da aplicação:
>    ```shell
>    curl --fail --silent --show-error --max-time 10 https://loja.exemplo.com.br/health
>    ```
>    Com a opção `--fail`, o comando mostra um erro quando a resposta tem um código de status `4xx` ou `5xx`.
>
>    - Se o comando mostrar o texto `{"status":"ok"}`, altere o estado da solicitação de mudança `MUD-4512` para **Executada**. O processo termina neste passo.
>    - Se o comando mostrar um erro, siga o procedimento "Reverter o deploy".
>
> ##### Reverter o deploy
>
> ###### Antes de começar
>
> - Confirme que a solicitação de mudança `MUD-4512` tem o número do deploy em uso do passo 3 de "Executar o deploy".
>
> ###### Procedimento
>
> > **ATENÇÃO:** Reverta o deploy apenas no cluster `prod-sa-east-1` e no namespace `loja`. O rollback substitui todos os pods da aplicação `loja-web`. Durante 3 a 5 min, a aplicação recusa aproximadamente 10% das requisições dos clientes.
>
> 1. Reverta o deploy para o número do passo 3 de "Executar o deploy":
>    ```shell
>    helm rollback loja-web <numero-do-deploy> \
>      --kube-context prod-sa-east-1 \
>      --namespace loja \
>      --wait \
>      --timeout 10m
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<numero-do-deploy>`: o número da coluna `REVISION` na solicitação de mudança `MUD-4512`, por exemplo `41`.
>
>    - Se o comando mostrar a mensagem "Rollback was a success! Happy Helming!", vá para o passo 2.
>    - Se o comando mostrar outra mensagem, crie um incidente no PagerDuty para a equipe da aplicação `loja-web`. Este procedimento termina neste passo.
> 2. Copie para a solicitação de mudança `MUD-4512` a saída do passo de "Executar o deploy" que mostrou o erro.
>
>    Registro: a saída do erro, na solicitação de mudança `MUD-4512`.
> 3. Informe o responsável pela versão sobre o rollback, com o número da solicitação de mudança `MUD-4512`.
> 4. Verifique o estado dos pods:
>    ```shell
>    kubectl get pods \
>      --context prod-sa-east-1 \
>      --namespace loja \
>      --selector app.kubernetes.io/name=loja-web
>    ```
>    - Se a coluna `STATUS` mostrar o valor `Running` em todos os pods, vá para o passo 5.
>    - Se um pod mostrar outro valor, crie um incidente no PagerDuty para a equipe da aplicação `loja-web`. Este procedimento termina neste passo.
> 5. Teste o endpoint `/health` da aplicação:
>    ```shell
>    curl --fail --silent --show-error --max-time 10 https://loja.exemplo.com.br/health
>    ```
>    - Se o comando mostrar o texto `{"status":"ok"}`, altere o estado da solicitação de mudança `MUD-4512` para **Revertida**. O processo termina neste passo.
>    - Se o comando mostrar um erro, crie um incidente no PagerDuty para a equipe da aplicação `loja-web`. Este procedimento termina neste passo.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Como fazer o deploy da loja-web em produção. | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | Título no infinitivo, sem ponto final: "Executar o deploy da aplicação `loja-web` em produção" |
| fazer o deploy | [R3.10](02-regras.md#r310-use-o-verbo-específico-não-um-verbo-geral-revisor) | "Executar o deploy" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 4.2](04-termos-tecnicos.md#42-lista-de-verbos-técnicos).F) |
| Antes de tudo é necessário ter acesso | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor) | Seção "Antes de começar", com um item para cada condição: a solicitação de mudança, o responsável, as ferramentas e o papel de acesso |
| ter acesso ao cluster | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | O papel de acesso `deployer` e 2 comandos `kubectl auth can-i`, com o resultado `yes`. Um comando verifica o verbo `patch` dos objetos `Deployment`: o Helm 3 usa este verbo, não o verbo `update`. O outro comando verifica os objetos `Secret` do Helm. O Contexto tem os outros verbos do papel de acesso. |
| GMUD | [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor), [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | "a solicitação de mudança `MUD-4512`" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [NT-20](04-termos-tecnicos.md#nt-20-artefatos-de-processo)) |
| prod | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) | O nome exato do cluster, `prod-sa-east-1`, no aviso e em cada comando (opções `--context` e `--kube-context`) |
| Fazer o checkout na main e dar um pull | [R5.3](02-regras.md#r53-escreva-uma-instrução-por-passo-revisor), [R3.10](02-regras.md#r310-use-o-verbo-específico-não-um-verbo-geral-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Passo 1: "obtenha as tags do repositório remoto". Passo 3: "Atualize a pasta local para a tag `v2.8.0`". Os arquivos do deploy são os arquivos da tag `v2.8.0`. |
| pra pegar as últimas alterações | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | Remova estas palavras. A tag `v2.8.0` identifica a versão. |
| Checar se a tag da release foi criada | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | "Verifique se a tag `v2.8.0` existe" |
| (ex: v2.8.0) | [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor) | O valor exato no passo: a tag `v2.8.0` |
| caso não tenha sido criada | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | "Se o comando não mostrar nenhuma tag" |
| deve-se criar a mesma | [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale), [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) | O imperativo e o nome do procedimento: siga o procedimento "Criar a tag de uma versão" |
| se estiver vermelho não prossiga | [R5.4](02-regras.md#r54-escreva-a-condição-e-o-local-antes-da-ação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Uma condição para cada estado do pipeline, antes da ação |
| está verde | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) | O rótulo exato do estado, em negrito: **Success** |
| (sem os estados **Queued**, **In progress**, **Cancelled** e **Skipped**) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Uma saída para cada estado. Para **Queued** e **In progress**, o passo 4 tem um limite de 30 min. |
| avise | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "informe" |
| Setar o contexto do kubectl | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) | Passo 1 de "Executar o deploy": o comando `kubectl cluster-info` mostra a URL do cluster antes do deploy. Cada comando tem o nome do cluster na opção `--context` ou `--kube-context`. |
| Rodar o helm upgrade | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | "Execute o deploy da versão 2.8.0 no cluster `prod-sa-east-1`, com os valores de produção" e o comando em um bloco de código |
| (o comando `helm upgrade` sem arquivo de valores) | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | A opção `--values ./chart/values-prod.yaml`. Sem esta opção, o deploy usa os valores padrão do chart para o número de réplicas e os recursos. |
| `helm upgrade ... -n loja --set image.tag=v2.8.0` em uma linha | [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | O comando tem mais de 100 caracteres: uma opção por linha, com `\` no fim da linha |
| `$ helm upgrade ...` em código em linha | [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | Bloco de código sem o sinal `$`. A saída do comando está em outro bloco de código. |
| -n loja | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | A opção longa: `--namespace loja` |
| (sem o registro do deploy atual) | [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passos 2 e 3: o número da coluna `REVISION` da linha com o estado `deployed`, na solicitação de mudança, com a frase "Registro:". Depois de um deploy com falha, a última linha do histórico tem o estado `failed`. Um rollback para este número não volta à versão em uso. O rollback usa o número da linha `deployed`. |
| (sem verificação do Helm depois do deploy) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passo 5: o comando `helm history --max 1` mostra o estado do deploy novo. Uma saída para `deployed` e uma saída para outro valor. |
| Ficar acompanhando o rollout | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Monitore o deploy" |
| até que todos os pods subam | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | As mensagens exatas do comando e o significado de cada mensagem |
| normalmente leva alguns minutos | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale) | Tempo limite de 10 min, na opção `--timeout 10m` |
| Caso o rollout demore muito | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "Se o comando mostrar outra mensagem" |
| deverá ser feito o rollback da aplicação | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) | Outro procedimento: "Reverter o deploy" (verbo técnico REVERTER), com o mesmo nível de detalhe do deploy |
| (sem as ações depois do rollback) | [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor), [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | Procedimento "Reverter o deploy", com o fim do procedimento em cada saída. O procedimento tem uma saída para o rollback com falha, o registro do erro e a informação ao responsável pela versão. Depois, o procedimento verifica os pods e o endpoint. |
| (o número do deploy sem explicação) | [R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor) | A frase "Substitua o espaço reservado, com os sinais `<` e `>`" e a lista depois do bloco de código |
| Após isso, validar | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor) | Passo 8: "Teste o endpoint `/health`" |
| está respondendo normalmente | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Resultado exato: o texto `{"status":"ok"}`. A opção `--fail` mostra um erro para o código de status `4xx` ou `5xx`. |
| Obs.: o deploy derruba os pods | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor), [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | Aviso ATENÇÃO antes do passo 4 de "Executar o deploy". A consequência é uma indisponibilidade parcial com recuperação conhecida: o fim do deploy ou o rollback ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 2). |
| (rollback sem aviso) | [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) | Aviso ATENÇÃO antes do passo 1 de "Reverter o deploy". O rollback também substitui os pods: a consequência e o nível são os mesmos do aviso do deploy. |
| vai estar ocorrendo | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale) | Verbo no presente: "a aplicação recusa" |
| indisponibilidade parcial durante alguns minutos | [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "Durante 3 a 5 min, a aplicação recusa aproximadamente 10% das requisições dos clientes." |
| Recomenda-se fazer fora do horário de pico! | [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale), [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor), [R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor) | Instrução do aviso: "Execute o deploy apenas entre 22:00 e 06:00 UTC-03:00." |

---

## Exemplo 2: Runbook de incidente com latência alta no banco de dados

Contexto: o analista de plantão recebe o alerta `DBLatenciaAlta` do banco `catalogo`, um banco PostgreSQL 16 no servidor `catalogo-db-01` do ambiente de produção. Estes dados não estão no texto "Antes":

- O serviço `api-catalogo` usa o banco `catalogo` com o usuário `api_catalogo`. O serviço tem 6 pods no namespace `catalogo` do cluster `prod-sa-east-1`.
- O serviço `api-catalogo` tem um tempo limite de 3 s para cada consulta. Sem o alerta, o serviço responde em até 200 ms.
- O limite do servidor `catalogo-db-01` é 200 conexões (parâmetro `max_connections`). O limite conta as conexões de todos os bancos de dados do servidor.
- O usuário `sre` do banco tem os papéis de acesso `pg_signal_backend` e `pg_read_all_stats`. A senha do usuário `sre` está no cofre de segredos, no item `catalogo-db-01/sre`.
- Sem o papel de acesso `pg_read_all_stats`, o PostgreSQL mostra ao usuário `sre` o valor `NULL` nas colunas `state` e `query_start` das sessões de outros usuários. Com este valor, a consulta do procedimento 1 não mostra nenhuma linha durante o incidente.
- A equipe de banco de dados recebe os incidentes pelo PagerDuty. O PagerDuty mostra um destes estados: **Triggered**, **Acknowledged** ou **Resolved**.
- A equipe encaminha um incidente depois de 30 min sem solução. A equipe também encaminha um incidente com mais de 5% de respostas com o código de status `5xx`.

### Antes

> **Runbook - Latência alta no banco catalogo**
>
> Quando o alerta disparar, o plantonista deverá logar no Grafana e checar o dashboard do Postgres. Verifica-se primeiro se há queries travadas através da pg_stat_activity e, caso existam queries rodando há muito tempo, as mesmas devem ser killadas. Se o pool de conexões estiver estourado, dar um restart nos pods da API. Se mesmo assim a latência não normalizar, escalar para o time de DBA e acionar o gerente de incidente.
>
> Obs: cuidado com o terminate, pode causar problemas.

### PTS-BR

> #### Runbook: latência alta no banco `catalogo`
>
> ##### Alerta
>
> O Grafana mede o percentil 99 (p99) da latência das consultas do banco `catalogo`. O Grafana envia o alerta `DBLatenciaAlta` quando o p99 fica maior que 500 ms durante 5 min.
>
> ##### Impacto
>
> O serviço `api-catalogo` usa o banco `catalogo` no servidor `catalogo-db-01` do ambiente de produção. O serviço tem um tempo limite de 3 s para cada consulta. Quando uma consulta demora mais de 3 s, o serviço `api-catalogo` retorna o código de status `504`.
>
> ##### Procedimentos
>
> O runbook tem 5 procedimentos:
>
> 1. "Analisar a latência"
> 2. "Cancelar as consultas longas"
> 3. "Reiniciar os pods do serviço `api-catalogo`"
> 4. "Encaminhar o incidente"
> 5. "Resolver o incidente"
>
> ##### Antes de começar
>
> - Confirme que o arquivo `~/.pgpass` contém a senha do usuário `sre` do servidor `catalogo-db-01`. A senha está no cofre de segredos, no item `catalogo-db-01/sre`.
> - Confirme que apenas o seu usuário pode ler e alterar o arquivo `~/.pgpass`:
>   ```shell
>   ls -l ~/.pgpass
>   ```
>   A primeira coluna da saída mostra o valor `-rw-------`. Com outra permissão, o comando `psql` não lê o arquivo e pede a senha.
>   - Se a primeira coluna mostrar outro valor, altere a permissão do arquivo para 600:
>     ```shell
>     chmod 600 ~/.pgpass
>     ```
> - Confirme que o usuário `sre` tem os papéis de acesso `pg_signal_backend` e `pg_read_all_stats`:
>   ```shell
>   psql --host catalogo-db-01 \
>     --username sre \
>     --dbname catalogo \
>     --command "SELECT pg_has_role('sre', 'pg_signal_backend', 'MEMBER') AS sinal, \
>       pg_has_role('sre', 'pg_read_all_stats', 'MEMBER') AS estatisticas;"
>   ```
>   O comando mostra o valor `t` nas 2 colunas:
>   ```text
>    sinal | estatisticas
>   -------+--------------
>    t     | t
>   (1 row)
>   ```
>   Sem o papel de acesso `pg_read_all_stats`, o passo 2 do procedimento 1 não mostra as consultas do usuário `api_catalogo`.
> - Confirme que a sua conta pode reiniciar o serviço `api-catalogo` no cluster `prod-sa-east-1`:
>   ```shell
>   kubectl auth can-i patch deployments/api-catalogo --context prod-sa-east-1 --namespace catalogo
>   ```
>   O comando mostra a resposta `yes`.
> - Confirme que a sua conta tem acesso ao PagerDuty e ao painel **PostgreSQL - catalogo** do Grafana.
> - Instale estas 2 ferramentas:
>   - a ferramenta `psql` 16 ou uma versão mais nova
>   - a ferramenta `kubectl` 1.30 ou uma versão mais nova
>
> ##### Procedimento 1: Analisar a latência
>
> 1. No Grafana, abra o painel **PostgreSQL - catalogo**.
>
>    O painel mostra o p99 da latência e o número de conexões do banco `catalogo`.
> 2. Liste as consultas do usuário `api_catalogo` com mais de 1 min de duração:
>    ```shell
>    psql --host catalogo-db-01 \
>      --username sre \
>      --dbname catalogo \
>      --command "SELECT pid, now() - query_start AS duracao, left(query, 80) AS consulta \
>        FROM pg_stat_activity \
>        WHERE backend_type = 'client backend' AND usename = 'api_catalogo' \
>        AND state = 'active' AND now() - query_start > interval '1 minute' \
>        ORDER BY duracao DESC;"
>    ```
>    O comando mostra uma linha para cada consulta ativa do usuário `api_catalogo` com mais de 1 min de duração. A condição `usename` exclui as consultas de outros usuários, por exemplo o usuário de backup e o usuário de réplica. A condição `backend_type` exclui os processos internos do PostgreSQL.
> 3. Conte as conexões de clientes com o servidor `catalogo-db-01`:
>    ```shell
>    psql --host catalogo-db-01 \
>      --username sre \
>      --dbname catalogo \
>      --command "SELECT count(*) FROM pg_stat_activity WHERE backend_type = 'client backend';"
>    ```
>    O comando mostra o número de conexões de clientes com todos os bancos de dados do servidor. O limite do servidor é 200 conexões.
> 4. No incidente do PagerDuty, registre a saída dos passos 2 e 3.
>
>    Registro: a saída dos passos 2 e 3, no incidente do PagerDuty.
> 5. Escolha o procedimento de acordo com a saída dos passos 2 e 3:
>    - Se o passo 2 mostrar uma ou mais consultas, siga o procedimento 2.
>    - Se o passo 2 não mostrar consultas e o passo 3 mostrar mais de 180 conexões, siga o procedimento 3.
>    - Se o passo 2 não mostrar consultas e o passo 3 mostrar até 180 conexões, siga o procedimento 4.
>
> ##### Procedimento 2: Cancelar as consultas longas
>
> Este procedimento não tem rollback. O PostgreSQL desfaz as alterações de cada consulta cancelada, e os dados continuam no estado de antes da consulta.
>
> > **ATENÇÃO:** Cancele apenas as consultas do usuário `api_catalogo` no servidor `catalogo-db-01`. A função `pg_cancel_backend` cancela a consulta e desfaz as alterações da consulta. O serviço `api-catalogo` retorna um erro para a requisição da consulta cancelada.
>
> 1. Para cada linha da saída do passo 2 do procedimento 1, cancele a consulta:
>    ```shell
>    psql --host catalogo-db-01 \
>      --username sre \
>      --dbname catalogo \
>      --command "SELECT pg_cancel_backend(pid) FROM pg_stat_activity \
>        WHERE pid = <pid> AND usename = 'api_catalogo';"
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<pid>`: o valor da coluna `pid` da linha.
>
>    O comando mostra o valor `t` na coluna `pg_cancel_backend`. O valor `t` indica que o PostgreSQL vai cancelar a consulta. Quando a consulta do `<pid>` não é do usuário `api_catalogo`, o comando não mostra nenhuma linha.
> 2. Depois de 1 min, liste de novo as consultas longas:
>    ```shell
>    psql --host catalogo-db-01 \
>      --username sre \
>      --dbname catalogo \
>      --command "SELECT pid, now() - query_start AS duracao, left(query, 80) AS consulta \
>        FROM pg_stat_activity \
>        WHERE backend_type = 'client backend' AND usename = 'api_catalogo' \
>        AND state = 'active' AND now() - query_start > interval '1 minute' \
>        ORDER BY duracao DESC;"
>    ```
>    - Se o comando não mostrar nenhuma linha, vá para o passo 4.
>    - Se o comando mostrar uma ou mais linhas, vá para o passo 3.
>
> > **ATENÇÃO:** Feche apenas as conexões das linhas do passo 2. A função `pg_terminate_backend` fecha a conexão e desfaz a transação da conexão. O serviço `api-catalogo` perde a conexão e retorna o código de status `500` para as requisições desta conexão.
>
> 3. Para cada linha da saída do passo 2, feche a conexão da consulta:
>    ```shell
>    psql --host catalogo-db-01 \
>      --username sre \
>      --dbname catalogo \
>      --command "SELECT pg_terminate_backend(pid) FROM pg_stat_activity \
>        WHERE pid = <pid> AND usename = 'api_catalogo';"
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<pid>`: o valor da coluna `pid` da linha.
>
>    O comando mostra o valor `t` na coluna `pg_terminate_backend`.
> 4. Depois de 5 min, verifique o p99 da latência no painel **PostgreSQL - catalogo**:
>    - Se o p99 for menor que 500 ms, siga o procedimento 5.
>    - Se o p99 for 500 ms ou mais, siga o procedimento 4.
>
> ##### Procedimento 3: Reiniciar os pods do serviço `api-catalogo`
>
> Este procedimento não tem rollback. O comando `kubectl rollout restart` cria pods novos com a mesma configuração do serviço.
>
> 1. No incidente do PagerDuty, informe ao gerente de incidente que você vai reiniciar os pods do serviço `api-catalogo`.
> 2. Verifique a URL do cluster `prod-sa-east-1`:
>    ```shell
>    kubectl cluster-info --context prod-sa-east-1
>    ```
>    - Se o comando mostrar a URL `https://k8s.prod-sa-east-1.exemplo.com.br`, vá para o passo 3.
>    - Se o comando mostrar outra URL, siga o procedimento 4.
> 3. Verifique o serviço `api-catalogo` no cluster `prod-sa-east-1`:
>    ```shell
>    kubectl get deployment api-catalogo --context prod-sa-east-1 --namespace catalogo
>    ```
>    - Se a coluna `NAME` mostrar o valor `api-catalogo`, vá para o passo 4.
>    - Se o comando mostrar a mensagem `NotFound`, siga o procedimento 4.
>
> > **CUIDADO:** Reinicie apenas o serviço `api-catalogo` do cluster `prod-sa-east-1`. O comando substitui os 6 pods do serviço, um pod de cada vez. Durante aproximadamente 2 min, o serviço responde em até 2 s, em vez de 200 ms.
>
> 4. Reinicie os pods do serviço `api-catalogo`:
>    ```shell
>    kubectl rollout restart deployment/api-catalogo --context prod-sa-east-1 --namespace catalogo
>    ```
>    O comando mostra a mensagem "deployment.apps/api-catalogo restarted".
> 5. Monitore os pods novos:
>    ```shell
>    kubectl rollout status deployment/api-catalogo \
>      --context prod-sa-east-1 \
>      --namespace catalogo \
>      --timeout 5m
>    ```
>    - Se o comando mostrar a mensagem "successfully rolled out", vá para o passo 6.
>    - Se o comando mostrar outra mensagem, siga o procedimento 4.
> 6. Depois de 5 min, verifique o p99 da latência no painel **PostgreSQL - catalogo**:
>    - Se o p99 for menor que 500 ms, siga o procedimento 5.
>    - Se o p99 for 500 ms ou mais, siga o procedimento 4.
>
> ##### Procedimento 4: Encaminhar o incidente
>
> Siga este procedimento se uma destas 3 condições for verdadeira:
>
> - Um passo dos procedimentos 1, 2 ou 3 indica este procedimento.
> - O incidente tem 30 min ou mais de duração, e o p99 da latência é 500 ms ou mais.
> - Durante 5 min, mais de 5% das respostas do serviço `api-catalogo` têm um código de status `5xx`.
>
> 1. No PagerDuty, encaminhe o incidente para a equipe de banco de dados.
> 2. No incidente, registre o valor do p99 e as ações dos procedimentos 1, 2 e 3.
>
>    Registro: o valor do p99 e as ações, no incidente do PagerDuty.
> 3. No PagerDuty, adicione o gerente de incidente ao incidente.
> 4. Depois de 10 min, verifique o estado do incidente no PagerDuty:
>    - Se o estado for **Acknowledged**, a equipe de banco de dados é responsável pelo incidente. Este procedimento termina neste passo.
>    - Se o estado for **Triggered**, informe o gerente de incidente. O gerente de incidente é responsável pelo incidente. Este procedimento termina neste passo.
>    - Se o estado for **Resolved**, o processo termina neste passo.
>
> ##### Procedimento 5: Resolver o incidente
>
> 1. No incidente do PagerDuty, registre as ações e o resultado de cada procedimento.
>
>    Registro: as ações e o resultado de cada procedimento, no incidente do PagerDuty.
> 2. Depois de 15 min, verifique o estado do alerta `DBLatenciaAlta` no Grafana:
>    - Se o alerta mostrar o estado **Normal**, altere o estado do incidente para **Resolved** no PagerDuty. O processo termina neste passo.
>    - Se o alerta mostrar outro estado, siga o procedimento 4.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| no banco catalogo | [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor), [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) | "no banco `catalogo`" |
| Quando o alerta disparar | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R4.4](02-regras.md#r44-escreva-o-sujeito-se-o-texto-tiver-mais-de-um-autor-de-ação-revisor), [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | Seção "Alerta", com o agente como sujeito e o critério do alerta. O comportamento do sistema usa "quando" e o presente: "quando o p99 fica maior que 500 ms". |
| (sem o impacto do alerta) | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | Seção "Impacto", com o ambiente e o efeito: "Quando uma consulta demora mais de 3 s, o serviço `api-catalogo` retorna o código de status `504`." |
| (sem acessos e ferramentas) | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) | Seção "Antes de começar": a senha no arquivo `~/.pgpass` e no cofre de segredos, os papéis de acesso, o PagerDuty, o Grafana e as ferramentas. A senha não aparece em nenhum comando. |
| (arquivo `~/.pgpass` sem verificação da permissão) | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor), [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | O comando `ls -l ~/.pgpass`, a saída esperada `-rw-------` e o comando `chmod 600` para outra saída. Com outra permissão, o comando `psql` não lê o arquivo, e o analista de plantão digita a senha durante o incidente. |
| (sem os papéis de acesso do usuário `sre`) | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Os papéis de acesso `pg_signal_backend` e `pg_read_all_stats`, com o comando `pg_has_role` e o resultado `t`. O papel `pg_signal_backend` permite cancelar as consultas. O papel `pg_read_all_stats` permite ler as colunas `state`, `query_start` e `query` das sessões de outros usuários. |
| o plantonista | [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | O nome do glossário-base: "o analista de plantão" |
| deverá logar no Grafana | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor) | Passo 1 do procedimento 1: "No Grafana, abra o painel **PostgreSQL - catalogo**." |
| checar o dashboard do Postgres | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R10.1](02-regras.md#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor) | "o painel **PostgreSQL - catalogo**" |
| Verifica-se primeiro | [R3.4](02-regras.md#r34-não-use-a-passiva-sintética-nem-o-se-indeterminado-vale) | Imperativo: "Liste" |
| se há queries travadas | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor) | "as consultas do usuário `api_catalogo` com mais de 1 min de duração" |
| através da pg_stat_activity | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | O comando completo em um bloco de código, com uma opção por linha |
| caso existam queries rodando há muito tempo | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "com mais de 1 min de duração" |
| (consulta sem filtro de usuário) | [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | As condições `usename = 'api_catalogo'` e `backend_type = 'client backend'`. Os comandos dos passos 1 e 3 do procedimento 2 repetem a condição `usename`. |
| as mesmas devem ser killadas | [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | Procedimento 2: "cancele a consulta" (função `pg_cancel_backend`) |
| (cancelamento sem aviso) | [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) | Aviso ATENÇÃO antes do passo 1 do procedimento 2, com o usuário e o servidor. A consequência é uma indisponibilidade parcial com recuperação conhecida: um erro para as requisições das consultas canceladas ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 2). |
| (`<pid>` sem explicação) | [R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor) | A frase "Substitua o espaço reservado, com os sinais `<` e `>`" e a lista depois do bloco de código |
| Se o pool de conexões estiver estourado | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "Se o passo 2 não mostrar consultas e o passo 3 mostrar mais de 180 conexões". O limite de conexões é do servidor (`max_connections`), não do banco. Portanto, o passo 3 conta as conexões de clientes com todos os bancos de dados do servidor. |
| dar um restart nos pods da API | [R3.10](02-regras.md#r310-use-o-verbo-específico-não-um-verbo-geral-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor) | Procedimento 3: "Reinicie os pods do serviço `api-catalogo`" |
| (reinício dos pods sem aviso) | [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor) | Passos 2 e 3 do procedimento 3: o comando `kubectl cluster-info` mostra a URL do cluster, e o comando `kubectl get` mostra o serviço no cluster `prod-sa-east-1`. Cada passo tem uma saída para cada resultado. Depois, um aviso CUIDADO com o nome do cluster. A consequência é uma latência de até 2 s, menor que o tempo limite de 3 s. O serviço não retorna erros e não perde nenhuma função ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 3). A regra [R7.5](02-regras.md#r75-escreva-um-risco-por-aviso-revisor) dá o mesmo nível para a mesma consequência. |
| (sem o resultado do reinício) | [R5.5](02-regras.md#r55-escreva-o-resultado-esperado-em-uma-frase-separada-revisor) | Passo 4: a mensagem do comando, "deployment.apps/api-catalogo restarted" |
| Se mesmo assim a latência não normalizar | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Se o p99 for 500 ms ou mais" |
| escalar para o time de DBA | [R1.2](02-regras.md#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) | "encaminhe o incidente para a equipe de banco de dados". ESCALAR é um verbo técnico apenas para capacidade. |
| (sem critério de encaminhamento) | [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | 3 condições com valores: 30 min de incidente, p99 de 500 ms ou mais, mais de 5% de respostas `5xx` |
| acionar o gerente de incidente | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "adicione o gerente de incidente ao incidente" |
| (sem rollback) | [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) | Antes do passo 1 dos procedimentos 2 e 3, uma frase diz por que o procedimento não tem rollback. Os 2 procedimentos têm um aviso antes da alteração. |
| (sem o fim do runbook) | [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | Cada saída termina em um passo, em outro procedimento, no fim do procedimento com a pessoa que recebe o incidente ou no fim do processo. Nenhuma saída volta a um passo anterior. Procedimento 5: verificação do alerta antes do estado **Resolved**. |
| (sem registro das ações) | [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor) | A frase "Registro:" em cada passo que registra um dado no incidente. Estes passos são o passo 4 do procedimento 1, o passo 2 do procedimento 4 e o passo 1 do procedimento 5. |
| Um parágrafo com todas as ações | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R4.1](02-regras.md#r41-escreva-uma-instrução-ou-uma-afirmação-por-frase-revisor) | 5 procedimentos, cada um com um título e com os passos em ordem |
| Obs: cuidado com o terminate | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | Aviso ATENÇÃO com instrução, risco e consequência, antes do passo 3 do procedimento 2 |
| pode causar problemas | [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor), [R3.8](02-regras.md#r38-use-poder-e-dever-com-um-único-significado-revisor) | "O serviço `api-catalogo` perde a conexão e retorna o código de status `500` para as requisições desta conexão." |

---

## Exemplo 3: Descrição de um endpoint de API REST

Contexto: a documentação de referência da API de contas. O leitor é um desenvolvedor de uma aplicação cliente. Estes dados não estão no texto "Antes":

- O campo `perfil` tem o papel de acesso do usuário: `leitor`, `editor` ou `admin`.
- O corpo de cada resposta de erro tem os campos `codigo` e `mensagem`. O código de status `400` também tem a lista `erros`.
- O token de acesso é uma credencial. O cofre de segredos define a variável de ambiente `API_TOKEN` com o token do desenvolvedor.
- O shell substitui a variável `$API_TOKEN` pelo valor antes de executar um comando. Em um argumento do comando `curl`, o token fica visível na lista de processos (`ps`). O comando `printf` é um comando interno do shell e não aparece na lista de processos.

### Antes

> **POST /v1/usuarios**
>
> Este endpoint é utilizado para a criação de novos usuários na plataforma. É necessário que seja enviado um token válido no header Authorization. O body deve conter os campos nome, email e perfil (este último é opcional, sendo que o default é 'leitor'). Caso o email já esteja cadastrado, será retornado um 409. Em caso de sucesso, a API irá retornar 201 com o objeto do usuário criado. Erros de validação retornam 400 com a lista de campos inválidos.
>
> Ex.: `curl -X POST https://api.exemplo.com.br/v1/usuarios -H "Authorization: Bearer SEU_TOKEN" -d '{"nome":"Ana","email":"ana@exemplo.com.br"}'`

### PTS-BR

> #### `POST /v1/usuarios`
>
> O endpoint `POST /v1/usuarios` cria a conta de um usuário.
>
> ##### Cabeçalhos
>
> A requisição precisa destes 2 cabeçalhos:
>
> - O cabeçalho `Authorization`, com um token de acesso válido.
> - O cabeçalho `Content-Type`, com o valor `application/json`.
>
> ##### Corpo da requisição
>
> O corpo da requisição tem o formato JSON, com os campos da tabela abaixo.
>
> | Campo | Tipo | Uso | Descrição |
> |---|---|---|---|
> | `nome` | string | Obrigatório | O nome do usuário. |
> | `email` | string | Obrigatório | O e-mail do usuário. Cada conta tem um e-mail diferente. |
> | `perfil` | string | Opcional | O papel de acesso do usuário: `leitor`, `editor` ou `admin`. Valor padrão: `leitor`. |
>
> ##### Exemplo de requisição
>
> O exemplo precisa da ferramenta `curl` 7.55 ou de uma versão mais nova.
>
> > **PERIGO:** Envie o token ao comando `curl` apenas pela opção `--header @-`. O histórico do shell e a lista de processos mostram os argumentos de cada comando. Uma pessoa com o token pode criar e alterar contas de usuários.
>
> ```shell
> printf 'Authorization: Bearer %s\n' "$API_TOKEN" | curl --request POST \
>   --header @- \
>   --header "Content-Type: application/json" \
>   --data '{"nome": "Ana Souza", "email": "ana.souza@exemplo.com.br"}' \
>   https://api.exemplo.com.br/v1/usuarios
> ```
>
> - `$API_TOKEN`: a variável de ambiente com o seu token de acesso. O comando `printf` escreve o cabeçalho `Authorization` com o token.
> - `--header @-`: o comando `curl` lê o cabeçalho `Authorization` da saída do comando `printf`. O token não aparece nos argumentos do comando `curl`.
>
> ##### Respostas
>
> O endpoint retorna estes códigos de status. Os códigos `429` e `5xx` são iguais para todos os endpoints e estão na seção "Erros gerais" da API de contas.
>
> | Código de status | Descrição | Corpo da resposta |
> |---|---|---|
> | `201` | A API criou a conta do usuário. | Os dados da conta, com os campos `id`, `nome`, `email`, `perfil` e `criado_em`. |
> | `400` | Um ou mais campos do corpo da requisição são inválidos. | Um corpo de erro com o código `campos_invalidos` e o array `erros`. |
> | `401` | O token de acesso é inválido ou expirou. | Um corpo de erro com o código `token_invalido`. |
> | `409` | Outra conta tem o e-mail do campo `email`. | Um corpo de erro com o código `email_em_uso`. |
>
> ##### Exemplo de resposta com o código de status `201`
>
> ```json
> {
>   "id": "u_8f14e45f",
>   "nome": "Ana Souza",
>   "email": "ana.souza@exemplo.com.br",
>   "perfil": "leitor",
>   "criado_em": "2026-11-18T13:45:00Z"
> }
> ```
>
> ##### Corpo de erro
>
> O corpo de uma resposta de erro tem o formato JSON, com os campos da tabela abaixo.
>
> | Campo | Tipo | Descrição |
> |---|---|---|
> | `codigo` | string | O código do erro. Use este campo no código da aplicação cliente. |
> | `mensagem` | string | Uma descrição do erro para o desenvolvedor. A equipe altera o texto do campo entre versões. Não use este campo no código da aplicação cliente. |
> | `erros` | array | Apenas no código de status `400`. Um item para cada campo inválido, com os campos `campo` e `descricao`. |
>
> Exemplo de resposta com o código de status `400`:
>
> ```json
> {
>   "codigo": "campos_invalidos",
>   "mensagem": "Um ou mais campos são inválidos.",
>   "erros": [
>     {"campo": "email", "descricao": "O endereço de e-mail não tem o caractere @."}
>   ]
> }
> ```

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Este endpoint é utilizado para a criação de novos usuários | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | O endpoint como sujeito e o verbo principal: "O endpoint `POST /v1/usuarios` cria a conta de um usuário." |
| na plataforma | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Remova estas palavras. A API de contas tem apenas este endpoint com este nome. |
| É necessário que seja enviado um token válido | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R6.5](02-regras.md#r65-use-listas-e-tabelas-para-itens-paralelos-revisor) | Uma lista dos cabeçalhos da requisição: "O cabeçalho `Authorization`, com um token de acesso válido." |
| header Authorization | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | "o cabeçalho `Authorization`" |
| O body deve conter | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R3.8](02-regras.md#r38-use-poder-e-dever-com-um-único-significado-revisor) | "O corpo da requisição tem o formato JSON, com os campos da tabela abaixo." |
| (sem o cabeçalho `Content-Type`) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | "O cabeçalho `Content-Type`, com o valor `application/json`." |
| perfil (no texto) | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | O campo `perfil` continua como literal. Na descrição, use o nome técnico "papel de acesso" e a lista dos valores aceitos. |
| os campos nome, email e perfil | [R6.5](02-regras.md#r65-use-listas-e-tabelas-para-itens-paralelos-revisor), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | Uma tabela com uma linha para cada campo |
| (este último é opcional, sendo que o default é 'leitor') | [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor), [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) | Coluna "Uso" e o texto "Valor padrão: `leitor`." |
| Caso o email já esteja cadastrado | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) | Linha do código de status `409`: "Outra conta tem o e-mail do campo `email`." |
| será retornado um 409 | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | Uma tabela de respostas, com o código de status em cada linha |
| a API irá retornar 201 | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale) | Linha do código de status `201`: "A API criou a conta do usuário." |
| com o objeto do usuário criado | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | Os campos da resposta e um exemplo de resposta com o código de status `201` |
| Erros de validação retornam 400 | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R4.3](02-regras.md#r43-escreva-o-sujeito-antes-do-verbo-e-faça-a-concordância-vale) | "Um ou mais campos do corpo da requisição são inválidos." |
| com a lista de campos inválidos | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | A seção "Corpo de erro", com os campos `codigo`, `mensagem` e `erros`, e um exemplo de resposta com o código de status `400` |
| (sem resposta para o token inválido) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | Linha do código de status `401` |
| (sem os códigos de status de todos os endpoints) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | A frase "Os códigos `429` e `5xx` [...] estão na seção "Erros gerais" da API de contas." A tabela não diz que tem todos os códigos. |
| (sem a versão do `curl`) | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor) | "O exemplo precisa da ferramenta `curl` 7.55 ou de uma versão mais nova." A opção `--header @-` não existe em versões anteriores. |
| (o campo `mensagem` sem regra de uso) | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R6.6](02-regras.md#r66-não-escreva-instruções-em-texto-descritivo-revisor) | "A equipe altera o texto do campo entre versões. Não use este campo no código da aplicação cliente." |
| Ex.: | [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Uma seção "Exemplo de requisição" |
| SEU_TOKEN | [R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor), [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) | A variável de ambiente `$API_TOKEN` e a descrição da variável depois do bloco. O valor do token não aparece no comando. |
| `-H "Authorization: Bearer SEU_TOKEN"` | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) | O comando `printf` escreve o cabeçalho, e o comando `curl` lê o cabeçalho com a opção `--header @-`. Uma variável de ambiente em um argumento (`--header "Authorization: Bearer $API_TOKEN"`) protege o histórico, mas não a lista de processos. |
| O comando `curl` em uma linha | [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | O comando tem mais de 100 caracteres: uma opção por linha, com `\` no fim da linha |
| (sem aviso sobre o token no comando) | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | Aviso PERIGO antes do bloco de código: o histórico do shell e a lista de processos mostram uma credencial. Uma credencial visível para outras pessoas é PERIGO ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 1). |
| -X, -H, -d | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | As opções longas do `curl`: `--request`, `--header`, `--data` |

---

## Exemplo 4: Mensagens de erro e diálogos de confirmação

Contexto: textos da interface de uma aplicação de projetos. Estes dados não estão no texto "Antes":

- O servidor recusa arquivos com mais de 25 MB.
- O tempo limite da sessão é 30 min sem atividade.
- O código PRJ-500 identifica um erro: o sistema não gravou o projeto, e a causa do erro não é conhecida.
- A exclusão de um projeto exclui também os arquivos e os deploys do projeto.
- O sistema de tradução da aplicação usa o formato MessageFormat. Uma mensagem com uma quantidade tem um texto para 0, um texto para 1 e um texto para 2 ou mais.

### Antes

> | Situação | Texto |
> |---|---|
> | Erro: arquivo grande demais | `Ops! Não foi possível fazer o upload do arquivo. Tente novamente!` |
> | Erro: sessão expirada | `Sua sessão expirou. Favor efetuar o login novamente.` |
> | Erro: falha ao salvar o projeto | `Algo deu errado :( Erro desconhecido.` |
> | Confirmação: excluir um projeto | `Tem certeza que deseja excluir? Essa ação não poderá ser desfeita.` Botões: [Sim] [Não] |
> | Confirmação: revogar um token | `Deseja realmente revogar o token? As integrações que utilizam o mesmo irão parar de funcionar.` Botões: [OK] [Cancelar] |
> | Sucesso: excluir arquivos | `{0} arquivo(s) excluído(s) com sucesso!` |

### PTS-BR

> | Situação | Texto |
> |---|---|
> | Erro: arquivo com mais de 25 MB | `O upload do arquivo {nome_arquivo} falhou. O arquivo tem mais de 25 MB. Envie um arquivo com até 25 MB.` |
> | Erro: sessão expirada | `A sua sessão expirou. O tempo limite da sessão é 30 min sem atividade. Entre de novo.` |
> | Erro: as alterações do projeto não estão gravadas | `As alterações do projeto {nome_projeto} não estão gravadas. Tente de novo depois de 5 min. Se o erro continuar, envie o código PRJ-500 ao suporte.` |
> | Caixa de diálogo: excluir um projeto | `Excluir o projeto {nome_projeto}? O sistema também vai excluir os arquivos e os deploys do projeto. Você não pode desfazer a exclusão.` Botões: [Excluir projeto] [Cancelar] |
> | Caixa de diálogo: revogar um token | `Revogar o token {nome_token}? As aplicações que usam este token perdem o acesso imediatamente.` Botões: [Revogar token] [Cancelar] |
> | Sucesso: arquivos excluídos | Texto para 0: `Nenhum arquivo excluído.` Texto para 1: `{quantidade} arquivo excluído.` Texto para 2 ou mais: `{quantidade} arquivos excluídos.` |
>
> No arquivo de tradução, a mensagem de sucesso tem os 3 textos no formato MessageFormat:
>
> ```text
> {quantidade, plural, =0 {Nenhum arquivo excluído.} one {# arquivo excluído.} other {# arquivos excluídos.}}
> ```
>
> O sinal `#` mostra o valor da variável `quantidade`. A regra de plural do português usa a chave `one` para os valores 0 e 1. A chave `=0` tem prioridade sobre a chave `one` e mostra o texto do valor 0.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Ops! | [R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor) | Remova a palavra "Ops" e o sinal "!". |
| Não foi possível fazer o upload do arquivo | [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor), [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale) | O que aconteceu, com o item afetado como sujeito: "O upload do arquivo {nome_arquivo} falhou." |
| (sem a causa do erro de upload) | [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) | A causa em outra frase: "O arquivo tem mais de 25 MB." |
| Tente novamente! | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor), [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) | Uma ação que resolve o erro: "Envie um arquivo com até 25 MB." |
| Sua sessão expirou. | [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) | "A sua sessão expirou." e a causa em outra frase: "O tempo limite da sessão é 30 min sem atividade." |
| Favor efetuar o login novamente. | [R9.3](02-regras.md#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor), [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Entre de novo." (ENTRAR: começar uma sessão) |
| Algo deu errado :( | [R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor) | O que aconteceu, com o item afetado como sujeito: "As alterações do projeto {nome_projeto} não estão gravadas." |
| Erro desconhecido. | [R10.5](02-regras.md#r105-escreva-mensagens-de-erro-sem-humor-e-sem-culpa-revisor) | O sistema não conhece a causa. Portanto, a mensagem não tem a frase de causa e tem uma ação: "Tente de novo depois de 5 min." |
| (sem código para o suporte) | [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) | "Se o erro continuar, envie o código PRJ-500 ao suporte." As mensagens da regra [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor) usam as mesmas palavras. |
| Tem certeza que deseja excluir? | [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) | A ação e o item, com o sinal "?": "Excluir o projeto {nome_projeto}?" |
| (sem a consequência da exclusão) | [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor), [R10.4](02-regras.md#r104-escreva-a-mensagem-de-erro-com-o-que-aconteceu-e-o-que-fazer-revisor), [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | "O sistema também vai excluir os arquivos e os deploys do projeto." Os arquivos não podem ser o sujeito de EXCLUIR na voz ativa. A regra [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) usa o mesmo sujeito. |
| Essa ação não poderá ser desfeita. | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Você não pode desfazer a exclusão." |
| [Sim] [Não] | [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) | [Excluir projeto] [Cancelar] |
| Deseja realmente revogar o token? | [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Revogar o token {nome_token}?" |
| As integrações que utilizam o mesmo | [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "As aplicações que usam este token" |
| irão parar de funcionar | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | O efeito exato: "perdem o acesso imediatamente" |
| [OK] | [R10.6](02-regras.md#r106-escreva-rótulos-de-botão-e-diálogos-de-confirmação-com-o-verbo-da-ação-revisor) | [Revogar token] |
| {0} | [R10.8](02-regras.md#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor) | Uma variável com nome: `{quantidade}` |
| arquivo(s) excluído(s) | [R10.8](02-regras.md#r108-escreva-textos-com-variáveis-que-funcionam-com-qualquer-valor-revisor) | 3 textos no sistema de tradução: um texto para 0, um texto para 1 e um texto para 2 ou mais |
| com sucesso! | [R10.7](02-regras.md#r107-escreva-mensagens-de-andamento-e-de-sucesso-curtas-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | Remova as palavras "com sucesso" e o sinal "!": `{quantidade} arquivos excluídos.` |

---

## Exemplo 5: Avisos de segurança

Contexto: 2 procedimentos. Estes dados não estão no texto "Antes":

- O primeiro procedimento limpa o banco `clientes_hml` do ambiente de homologação, no servidor `clientes-hml-db-01`. O script `limpar_base.sh` recebe o servidor na opção `--host` e o banco na opção `--dbname`.
- O banco de produção `clientes` tem os dados dos clientes. A equipe faz um backup do banco `clientes` 1 vez por dia.
- A senha do usuário `sre` está no cofre de segredos da equipe.
- O outro procedimento gera um token de API no portal `portal.exemplo.com.br`. O portal mostra o token apenas 1 vez. O token tem as permissões da conta que gera o token.

### Antes

> **Limpeza da base de homolog**
>
> **IMPORTANTE!!!** Muito cuidado ao rodar o script de limpeza, pois o mesmo apaga TODOS os dados da base. NUNCA rode em PRODUÇÃO!!!
>
> 1. Exportar a variável PGDATABASE com o nome da base de homolog.
> 2. Conferir se o psql está apontando pra base certa.
> 3. Rodar o `limpar_base.sh`.
>
> **Geração de token de API**
>
> 1. Ir em Configurações > Tokens de API.
> 2. Clicar no botão "Gerar token".
> 3. Copiar o token e guardar ele no cofre.
>
> Obs.: o token só é exibido uma vez, então tome cuidado para não perder o mesmo. Atenção ao fechar a janela!

### PTS-BR

> #### Limpar o banco de homologação `clientes_hml`
>
> ##### Antes de começar
>
> - Confirme que o arquivo `~/.pgpass` contém a senha do usuário `sre` do servidor `clientes-hml-db-01`. A senha está no cofre de segredos da equipe.
> - Confirme que apenas o seu usuário pode ler e alterar o arquivo `~/.pgpass`:
>   ```shell
>   ls -l ~/.pgpass
>   ```
>   A primeira coluna da saída mostra o valor `-rw-------`. Com outra permissão, o comando `psql` não lê o arquivo e pede a senha.
>   - Se a primeira coluna mostrar outro valor, altere a permissão do arquivo para 600:
>     ```shell
>     chmod 600 ~/.pgpass
>     ```
>
> ##### Procedimento
>
> 1. Verifique o servidor e o banco da conexão:
>    ```shell
>    psql --host clientes-hml-db-01 --username sre --dbname clientes_hml --command "\conninfo"
>    ```
>    O comando mostra o banco e o servidor da conexão:
>    ```text
>    You are connected to database "clientes_hml" as user "sre" on host "clientes-hml-db-01" (address "10.20.4.12") at port "5432".
>    ```
>    - Se o comando mostrar o banco `clientes_hml` e o servidor `clientes-hml-db-01`, vá para o passo 2.
>    - Se o comando mostrar outro banco ou outro servidor, não execute o script. Informe o gestor da equipe com a saída do comando. Este procedimento termina neste passo.
>
> > **PERIGO:** Execute o script `limpar_base.sh` apenas no banco `clientes_hml` do servidor `clientes-hml-db-01`. O script exclui todas as tabelas do banco da opção `--dbname`. No banco de produção `clientes`, a equipe perde os dados dos clientes gravados depois do último backup.
>
> 2. Execute o script no banco `clientes_hml` do servidor `clientes-hml-db-01`:
>    ```shell
>    ./limpar_base.sh --host clientes-hml-db-01 --dbname clientes_hml
>    ```
> 3. Verifique as tabelas do banco `clientes_hml`:
>    ```shell
>    psql --host clientes-hml-db-01 --username sre --dbname clientes_hml --command "\dt"
>    ```
>    O comando mostra a mensagem "Did not find any relations." A mensagem indica que o banco não tem nenhuma tabela.
>
> #### Gerar um token de API
>
> 1. No portal `portal.exemplo.com.br`, selecione **Configurações** > **Tokens de API**.
> 2. Clique em **Gerar token**.
>
>    A janela **Token gerado** mostra o token.
>
> > **CUIDADO:** Copie o token antes de fechar a janela **Token gerado**. O portal mostra o token apenas 1 vez. Sem a cópia do token, você precisa gerar um token novo.
>
> 3. Clique no ícone de cópia ao lado do token.
>
> > **PERIGO:** Grave o token apenas no cofre de segredos da equipe. Um token em um chamado, em uma mensagem, em um arquivo ou em um comando fica visível para outras pessoas. Uma pessoa com o token tem acesso à API com as permissões da sua conta.
>
> 4. Grave o token no cofre de segredos da equipe.
> 5. Na página **Tokens de API**, verifique a lista de tokens.
>
>    A lista mostra o token do passo 2 com o estado **Ativo**.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Limpeza da base de homolog | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Título no infinitivo, com o nome do glossário-base e o nome do banco: "Limpar o banco de homologação `clientes_hml`" |
| IMPORTANTE!!! | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | **PERIGO:** a consequência é a perda dos dados de depois do último backup. O backup não tem estes dados ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 1). |
| (aviso no início da página, longe do passo) | [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | Aviso imediatamente antes do passo 2 |
| Muito cuidado ao rodar o script de limpeza | [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Uma instrução específica, com o banco e o servidor: "Execute o script `limpar_base.sh` apenas no banco `clientes_hml` do servidor `clientes-hml-db-01`." |
| pois o mesmo apaga TODOS os dados da base | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | Risco: "O script exclui todas as tabelas do banco da opção `--dbname`." |
| NUNCA rode em PRODUÇÃO!!! | [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor), [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | Consequência exata: "No banco de produção `clientes`, a equipe perde os dados dos clientes gravados depois do último backup." |
| Exportar a variável PGDATABASE | [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor) | O servidor e o banco nas opções `--host` e `--dbname` de cada comando. Um comando não depende de uma variável definida em outro passo. |
| Conferir se o psql está apontando pra base certa | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passo 1: "Verifique o servidor e o banco da conexão", a saída esperada em um bloco separado e uma saída para cada resultado |
| (sem a origem da senha) | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor), [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor) | Seção "Antes de começar": a senha no arquivo `~/.pgpass` e no cofre de segredos, e a permissão 600 do arquivo. A senha não aparece em nenhum comando. |
| (sem verificação no fim) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | Passo 3, com o resultado do passo |
| Geração de token de API | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) | "Gerar um token de API" |
| Ir em Configurações > Tokens de API | [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor), [R10.3](02-regras.md#r103-escreva-caminhos-de-menu-e-teclas-em-um-formato-fixo-revisor), [R5.4](02-regras.md#r54-escreva-a-condição-e-o-local-antes-da-ação-revisor) | "No portal `portal.exemplo.com.br`, selecione **Configurações** > **Tokens de API**." |
| Clicar no botão "Gerar token" | [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor), [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) | "Clique em **Gerar token**." |
| Copiar o token e guardar ele no cofre | [R5.3](02-regras.md#r53-escreva-uma-instrução-por-passo-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | Passos 3 e 4. "Grave o token no cofre de segredos da equipe." |
| (sem aviso sobre a exposição do token) | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) | Aviso PERIGO antes do passo 4: um token fora do cofre de segredos fica visível para outras pessoas. Uma credencial visível para outras pessoas é PERIGO ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 1). |
| Obs.: | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) | **CUIDADO:** a consequência é uma tarefa que o leitor faz de novo: gerar um token novo ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 3). |
| o token só é exibido uma vez | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | "O portal mostra o token apenas 1 vez." |
| tome cuidado para não perder o mesmo | [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale) | "Copie o token antes de fechar a janela **Token gerado**." |
| Atenção ao fechar a janela! | [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | Consequência: "Sem a cópia do token, você precisa gerar um token novo." |
| (aviso depois do passo 3) | [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | Aviso antes do passo 3 |
| (sem verificação no fim) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | Passo 5: a lista de tokens mostra o token com o estado **Ativo**. |

---

## Exemplo 6: Notas de versão

Contexto: as notas de versão da API de pedidos para os desenvolvedores das aplicações clientes. A versão 3.0.0 tem uma alteração incompatível com a versão 2.9.4. Estes dados não estão no texto "Antes":

- O endpoint `GET /v2/pedidos` retorna no máximo 100 pedidos em cada página.
- Um teste da equipe mediu o tempo de resposta para uma lista de 1 000 pedidos. A versão 3.0.0 responde em até 300 ms. A versão 2.9.4 responde em até 1,2 s.
- A equipe vai remover o endpoint `GET /v1/pedidos` em 2027-03-01.

### Antes

> **Release 3.0.0 da API de Pedidos - 18/11/2026**
>
> **Novidades**
>
> - Adicionado suporte a paginação por cursor no endpoint de listagem de pedidos.
> - Agora é possível filtrar os pedidos por status.
>
> **Correções**
>
> - Corrigido bug onde o webhook pedido.pago era disparado duas vezes.
> - Melhorias de performance na listagem, que agora está bem mais rápida.
>
> **BREAKING CHANGES**
>
> - O campo `valor` foi renomeado para `valor_total`. O campo antigo deixará de ser enviado.
> - O endpoint /v1/pedidos foi deprecado e será removido em breve. Favor migrar para o /v2 o quanto antes.

### PTS-BR

> #### Notas de versão da API de pedidos 3.0.0
>
> Data: 2026-11-18
>
> ##### Funcionalidades novas
>
> - O endpoint `GET /v2/pedidos` aceita o parâmetro de consulta `cursor`. Com o parâmetro `cursor`, a aplicação cliente obtém os pedidos em páginas de até 100 pedidos.
> - O endpoint `GET /v2/pedidos` aceita o parâmetro de consulta `status`. Com o parâmetro `status`, a aplicação cliente filtra os pedidos pelo estado, por exemplo `pago`.
>
> ##### Defeitos corrigidos
>
> - A versão 2.9.4 envia o webhook `pedido.pago` 2 vezes para cada pedido. A versão 3.0.0 envia o webhook `pedido.pago` 1 vez para cada pedido.
>
> ##### Desempenho
>
> - Para uma lista de 1 000 pedidos, o endpoint `GET /v2/pedidos` da versão 3.0.0 responde em até 300 ms. A versão 2.9.4 responde em até 1,2 s.
>
> ##### Alterações incompatíveis
>
> Uma aplicação cliente da versão 2.9.4 precisa das alterações desta seção para funcionar com a versão 3.0.0. O procedimento "Atualizar uma aplicação cliente para a versão 3.0.0" descreve as alterações.
>
> - A versão 3.0.0 envia o campo `valor_total` em vez do campo `valor`.
> - O endpoint `GET /v1/pedidos` está obsoleto. A equipe vai remover o endpoint `GET /v1/pedidos` em 2027-03-01.
>
> ##### Atualizar uma aplicação cliente para a versão 3.0.0
>
> > **ATENÇÃO:** Substitua todas as leituras do campo `valor` antes do deploy da aplicação cliente. A versão 3.0.0 não envia o campo `valor`. Uma aplicação cliente que lê o campo `valor` não recebe o total de cada pedido.
>
> 1. No código da aplicação cliente, substitua o campo `valor` pelo campo `valor_total`.
> 2. Substitua a URL `/v1/pedidos` pela URL `/v2/pedidos`.
> 3. Execute os testes da aplicação cliente.
>
>    Nenhum teste falha.
> 4. Execute o deploy da aplicação cliente no ambiente de homologação.
> 5. Na aplicação cliente do ambiente de homologação, abra a lista de pedidos.
>
>    A lista mostra o total correto de cada pedido.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Release 3.0.0 | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | "Notas de versão" e "versão 3.0.0" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [seção 5.5](04-termos-tecnicos.md#55-lista-de-decisões)) |
| API de Pedidos | [R8.6](02-regras.md#r86-use-maiúsculas-apenas-no-início-das-frases-e-em-nomes-próprios-revisor) | "API de pedidos" |
| 18/11/2026 | [R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor) | 2026-11-18 |
| Novidades | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Funcionalidades novas" |
| Adicionado suporte a paginação por cursor | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R4.3](02-regras.md#r43-escreva-o-sujeito-antes-do-verbo-e-faça-a-concordância-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | O endpoint como sujeito: "O endpoint `GET /v2/pedidos` aceita o parâmetro de consulta `cursor`." |
| endpoint de listagem de pedidos | [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | O literal do endpoint: `GET /v2/pedidos` |
| Agora é possível filtrar os pedidos por status | [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | "Com o parâmetro `status`, a aplicação cliente filtra os pedidos pelo estado" |
| Correções | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "Defeitos corrigidos" |
| Corrigido bug | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | A versão como sujeito, com o resultado de cada versão |
| onde o webhook pedido.pago era disparado duas vezes | [R1.9](02-regras.md#r19-use-onde-apenas-para-lugar-vale), [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | "A versão 2.9.4 envia o webhook `pedido.pago` 2 vezes para cada pedido." A versão como sujeito mostra que o defeito é da versão 2.9.4. |
| Melhorias de performance | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | Uma seção "Desempenho" |
| agora está bem mais rápida | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "responde em até 300 ms" para 1 000 pedidos e o valor da versão 2.9.4 |
| BREAKING CHANGES | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | "Alterações incompatíveis" |
| O campo `valor` foi renomeado para `valor_total`. | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor) | "A versão 3.0.0 envia o campo `valor_total` em vez do campo `valor`." |
| O campo antigo deixará de ser enviado. | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | A frase do item anterior e o aviso ATENÇÃO |
| foi deprecado | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | "está obsoleto" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), critério E2) |
| será removido em breve | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | "A equipe vai remover o endpoint `GET /v1/pedidos` em 2027-03-01." |
| Favor migrar para o /v2 o quanto antes. | [R9.3](02-regras.md#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor), [R6.6](02-regras.md#r66-não-escreva-instruções-em-texto-descritivo-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | O procedimento "Atualizar uma aplicação cliente para a versão 3.0.0" e o aviso ATENÇÃO |

---

## Exemplo 7: Procedimento de um processo interno

Contexto: o processo de acesso de um colaborador novo. O processo tem 3 responsáveis: o gestor do colaborador novo, o analista de segurança e o analista de acesso. Estes dados não estão no texto "Antes":

- O analista de segurança decide cada chamado em até 2 dias úteis.
- O analista de acesso cria as contas em até 2 dias úteis depois da aprovação.
- A tabela **Papéis de acesso por cargo** do Service Desk mostra o papel de acesso de cada cargo.
- O histórico do chamado registra cada alteração de estado e cada comentário, com a data e o nome do responsável.
- No Microsoft Entra ID, uma conta nova com a opção **Gerar senha automaticamente** recebe uma senha temporária. No primeiro login, o colaborador novo precisa criar uma senha nova, e a senha temporária não funciona mais.
- A equipe de identidade resolve os erros do Microsoft Entra ID. A equipe recebe os incidentes no Service Desk.

### Antes

> **Processo de Onboarding de Acessos**
>
> O gestor deverá abrir um ticket no Service Desk com antecedência mínima de 5 dias úteis, informando nome, cargo, data de início e perfil de acesso do novo colaborador. Após a aprovação do mesmo pela Segurança da Informação, o time de TI realizará a criação das contas nos sistemas (AD, e-mail, VPN, etc.) e procederá à liberação dos acessos conforme o perfil. A senha provisória será enviada ao gestor através do cofre de senhas. É importante garantir que o MFA esteja habilitado. Ao final, o chamado deve ser fechado pelo analista responsável.

### PTS-BR

> #### Dar acesso a um colaborador novo
>
> Neste processo, um *colaborador novo* é uma pessoa que ainda não tem contas nos sistemas internos. O processo cria as contas do colaborador novo e adiciona as contas aos grupos do papel de acesso do cargo.
>
> O processo tem 3 procedimentos, um para cada responsável:
>
> | Procedimento | Responsável | Prazo | Registro |
> |---|---|---|---|
> | "Pedir o acesso" | Gestor do colaborador novo | 5 dias úteis ou mais antes do primeiro dia do colaborador novo | O chamado, no Service Desk |
> | "Analisar o chamado de acesso" | Analista de segurança | 2 dias úteis depois da data do chamado | A decisão, a causa da decisão e o estado do chamado, no histórico do chamado |
> | "Criar as contas do colaborador novo" | Analista de acesso | 2 dias úteis depois da aprovação | A lista das contas e o estado do chamado, no histórico do chamado |
>
> ##### Pedir o acesso
>
> - **Responsável:** gestor do colaborador novo
> - **Entrada:** o nome, o cargo e a data de início do colaborador novo
> - **Gatilho e prazo:** a data de início de um colaborador novo. Prazo: 5 dias úteis ou mais antes do primeiro dia do colaborador novo.
>
> 1. No Service Desk, crie um chamado com o modelo **Acesso de colaborador novo**.
> 2. Preencha os campos **Nome**, **Cargo** e **Data de início**.
> 3. Na lista **Papel de acesso**, selecione o papel de acesso do cargo.
> 4. Clique em **Enviar**.
>
>    O Service Desk mostra o número do chamado, por exemplo `ACS-2041`. O chamado tem o estado **Em análise**.
>
>    Registro: o chamado, no Service Desk.
> 5. Depois de 4 dias úteis, verifique o estado do chamado:
>    - Se o estado for **Resolvido**, vá para o passo 6.
>    - Se o estado for **Recusado** pela primeira vez, leia a causa no campo **Comentário** e volte ao passo 1.
>    - Se o estado for **Recusado** de novo, envie os números dos 2 chamados ao gestor da equipe de segurança. Este procedimento termina neste passo.
>    - Se o estado for **Em análise**, envie o número do chamado ao gestor da equipe de segurança. Este procedimento termina neste passo.
>    - Se o estado for **Aprovado**, envie o número do chamado ao gestor da equipe de acesso. Este procedimento termina neste passo.
> 6. No primeiro dia do colaborador novo, mostre ao colaborador novo a senha temporária do cofre de segredos.
>
>    O colaborador novo entra na conta do Microsoft Entra ID e cria uma senha nova.
>
>    - Se o colaborador novo entrar na conta, o processo termina neste passo.
>    - Se o login falhar, crie um incidente para a equipe de identidade com o número do chamado. O processo termina neste passo.
>
> ##### Analisar o chamado de acesso
>
> - **Responsável:** analista de segurança
> - **Entrada:** o chamado do procedimento "Pedir o acesso", do gestor do colaborador novo
> - **Gatilho e prazo:** um chamado com o estado **Em análise**. Prazo: 2 dias úteis depois da data do chamado.
>
> 1. No Service Desk, abra a página do chamado do colaborador novo.
> 2. Compare o papel de acesso do chamado com a linha do cargo na tabela **Papéis de acesso por cargo**.
> 3. No campo **Comentário** do chamado, escreva a decisão e a causa da decisão.
>
>    Registro: a decisão e a causa da decisão, no histórico do chamado.
> 4. Altere o estado do chamado de acordo com o resultado do passo 2:
>    - Se os 2 papéis de acesso forem iguais, selecione o estado **Aprovado** e vá para o passo 5.
>    - Se os 2 papéis de acesso forem diferentes, selecione o estado **Recusado** e vá para o passo 5.
>
>    O Service Desk envia um e-mail ao gestor do colaborador novo com o estado do chamado.
>
>    Registro: o estado do chamado, no histórico do chamado.
> 5. Atualize a página do chamado e verifique o estado do chamado:
>    - Se o estado for **Aprovado**, o procedimento "Criar as contas do colaborador novo" recebe o chamado. Este procedimento termina neste passo.
>    - Se o estado for **Recusado**, o procedimento "Pedir o acesso" recebe o chamado. Este procedimento termina neste passo.
>    - Se o estado for **Em análise**, envie o número do chamado ao gestor da equipe de segurança. Este procedimento termina neste passo.
>
> ##### Criar as contas do colaborador novo
>
> - **Responsável:** analista de acesso
> - **Entrada:** o chamado com o estado **Aprovado**, do analista de segurança
> - **Gatilho e prazo:** a aprovação do chamado. Prazo: 2 dias úteis depois da aprovação.
>
> O procedimento "Remover o acesso de um colaborador" desativa as contas e é o rollback deste procedimento.
>
> ###### Antes de começar
>
> - Confirme que o chamado tem o estado **Aprovado**.
> - Confirme que a sua conta tem o papel de acesso **Administrador de Usuários** no Microsoft Entra ID.
>
> ###### Procedimento
>
> 1. No Service Desk, abra a página do chamado do colaborador novo.
> 2. No Microsoft Entra ID, crie a conta do colaborador novo com a opção **Gerar senha automaticamente** marcada.
> 3. No Microsoft Entra ID, adicione a conta aos grupos do papel de acesso do chamado.
> 4. Crie as contas dos sistemas da tabela **Sistemas do papel de acesso** do chamado.
> 5. Ative a autenticação multifator (MFA) na conta do Microsoft Entra ID.
> 6. No Microsoft Entra ID, verifique a MFA e os grupos da conta:
>    - Se a MFA estiver ativa e a conta estiver em todos os grupos, vá para o passo 7.
>    - Se o resultado for outro, crie um incidente para a equipe de identidade. Escreva o número do chamado no incidente. Este procedimento termina neste passo.
>
> > **PERIGO:** Compartilhe a senha temporária apenas no cofre de segredos. Uma senha em um chamado, em um e-mail ou em uma mensagem fica visível para outras pessoas. Até o primeiro login do colaborador novo, uma pessoa com a senha tem acesso a todos os sistemas do colaborador novo.
>
> 7. No cofre de segredos, compartilhe a senha temporária com o gestor do colaborador novo.
> 8. No campo **Comentário** do chamado, escreva a lista das contas do passo 2 e do passo 4.
>
>    Registro: a lista das contas, no histórico do chamado.
> 9. Altere o estado do chamado para **Resolvido**.
>
>    O Service Desk envia um e-mail ao gestor do colaborador novo com o estado do chamado.
>
>    Registro: o estado do chamado, no histórico do chamado.
> 10. Atualize a página do chamado e verifique o estado do chamado:
>     - Se o estado for **Resolvido**, o gestor do colaborador novo recebe o chamado no passo 5 de "Pedir o acesso". Este procedimento termina neste passo.
>     - Se o estado for outro, envie o número do chamado ao gestor da equipe de acesso. Este procedimento termina neste passo.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Processo de Onboarding de Acessos | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R8.6](02-regras.md#r86-use-maiúsculas-apenas-no-início-das-frases-e-em-nomes-próprios-revisor) | Título no infinitivo: "Dar acesso a um colaborador novo" |
| novo colaborador | [R2.4](02-regras.md#r24-nomeie-um-conceito-longo-com-um-nome-curto-revisor) | Um nome curto, definido na primeira ocorrência: *colaborador novo* |
| Um parágrafo com 3 responsáveis e 7 ações | [R6.5](02-regras.md#r65-use-listas-e-tabelas-para-itens-paralelos-revisor), [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | Uma tabela com o responsável, o prazo e o registro de cada procedimento, e um procedimento para cada responsável |
| O gestor deverá abrir um ticket | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | O bloco **Responsável**, **Entrada** e **Gatilho e prazo** antes do passo 1, e o imperativo: "crie um chamado" |
| com antecedência mínima de 5 dias úteis | [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor), [R4.1](02-regras.md#r41-escreva-uma-instrução-ou-uma-afirmação-por-frase-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | O item **Gatilho e prazo**, com o prazo do texto "Antes": "Prazo: 5 dias úteis ou mais antes do primeiro dia do colaborador novo." |
| perfil de acesso | [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | O nome técnico "papel de acesso" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md)) |
| informando nome, cargo, data de início e perfil de acesso | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R10.1](02-regras.md#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor), [R10.2](02-regras.md#r102-use-o-verbo-do-tipo-de-elemento-revisor) | Passos 2 e 3, com os rótulos exatos dos campos |
| Após a aprovação do mesmo | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | O item **Entrada** ("o chamado com o estado **Aprovado**, do analista de segurança") e a seção "Antes de começar" |
| pela Segurança da Informação | [R8.6](02-regras.md#r86-use-maiúsculas-apenas-no-início-das-frases-e-em-nomes-próprios-revisor), [R4.4](02-regras.md#r44-escreva-o-sujeito-se-o-texto-tiver-mais-de-um-autor-de-ação-revisor), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | Um procedimento para o analista de segurança: "Analisar o chamado de acesso" |
| um ticket [...] o chamado | [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | Um nome para o item em todo o processo: "o chamado". O verbo PEDIR fica apenas no título da ação do gestor: "Pedir o acesso". |
| (sem o caminho do chamado recusado) | [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passo 4 de "Analisar o chamado de acesso": uma saída para **Aprovado** e uma saída para **Recusado**, cada uma com o destino. Passo 5 de "Pedir o acesso": uma saída para cada estado, também para o chamado sem resposta no prazo (**Em análise** e **Aprovado**). A saída que volta ao passo 1 tem um limite. Com 2 chamados recusados, o gestor envia os números ao gestor da equipe de segurança, e o procedimento termina. |
| (sem verificação da decisão) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | Passo 5 de "Analisar o chamado de acesso": o analista de segurança verifica o estado do chamado. Cada saída diz qual procedimento recebe o chamado. |
| (sem o registro da decisão) | [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor) | Passos 3 e 4 de "Analisar o chamado de acesso", com 2 frases "Registro:". Os registros são a decisão, a causa da decisão e o estado do chamado, no histórico do chamado. |
| o time de TI realizará a criação das contas | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | "**Responsável:** analista de acesso" e os passos 2 e 4: "crie a conta" |
| (AD, e-mail, VPN, etc.) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor), [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) | "Crie as contas dos sistemas da tabela **Sistemas do papel de acesso** do chamado." |
| procederá à liberação dos acessos conforme o perfil | [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "adicione a conta aos grupos do papel de acesso do chamado" |
| A senha provisória será enviada ao gestor | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "compartilhe a senha temporária com o gestor do colaborador novo" |
| (o gestor conhece a senha do colaborador novo) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Passo 2: a opção **Gerar senha automaticamente**. A senha temporária não funciona depois do primeiro login do colaborador novo. |
| através do cofre de senhas | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | "No cofre de segredos" ([`04-termos-tecnicos.md`](04-termos-tecnicos.md), [NT-16](04-termos-tecnicos.md#nt-16-segurança-e-identidade)) |
| (sem aviso sobre a senha fora do cofre) | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor) | Aviso PERIGO antes do passo 7: uma senha fora do cofre de segredos fica visível para outras pessoas. Uma credencial visível para outras pessoas é PERIGO ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 1). |
| É importante garantir que o MFA esteja habilitado | [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) | "Ative a autenticação multifator (MFA) na conta do Microsoft Entra ID." |
| (sem a lista das contas no chamado) | [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor) | Passo 8: a lista das contas no campo **Comentário** e a frase "Registro:" |
| (sem verificação da MFA) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passo 6: verificação da MFA e dos grupos, com uma saída para cada resultado. A verificação está antes do passo 7, que compartilha a senha. Com a MFA inativa, o gestor não recebe a senha. |
| Ao final | [R1.3](02-regras.md#r13-use-cada-palavra-apenas-na-classe-gramatical-aprovada-revisor) | FINAL é apenas adjetivo. O passo 10 é o último passo. |
| o chamado deve ser fechado pelo analista responsável | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor) | Passo 9: o analista de acesso altera o estado do chamado para **Resolvido**, com a frase "Registro:". Passo 10: o analista de acesso verifica o estado, com uma saída para cada resultado. O procedimento altera o estado do chamado. Portanto, o último passo verifica o estado (exemplo da regra [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor)). |
| (a senha temporária não chega ao colaborador novo) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passo 6 de "Pedir o acesso": no primeiro dia, o gestor mostra a senha ao colaborador novo. O passo tem uma saída para o login e uma saída para o erro. Com o passo 6, o processo termina com o colaborador novo na conta. |

---

## Exemplo 8: Arquivo `README.md` de uma biblioteca

Contexto: o arquivo `README.md` da biblioteca Python `brvalida`. O leitor é um desenvolvedor que vai instalar a biblioteca pela primeira vez. Estes dados não estão no texto "Antes":

- Um teste da equipe mediu o desempenho: a biblioteca valida 100 000 números de CPF em aproximadamente 1 s.
- A função `validar_cnpj()` recebe um número de CNPJ e retorna `True` ou `False`.
- O comando `pip show` mostra a versão instalada de um pacote.
- A versão 1.4.0 valida apenas números de CNPJ com os caracteres de 0 a 9. Desde 2026-07, a Receita Federal também cria números de CNPJ com os caracteres de A a Z.

### Antes

> **brvalida**
>
> Uma lib simples e super rápida pra validar CPF e CNPJ em Python.
>
> **Instalação**
>
> Basta rodar `pip install brvalida` e pronto! Obs: é necessário Python 3.9+.
>
> **Como usar**
>
> É só importar a função e passar o documento como string, a mesma retorna True se o doc for válido:
>
> ```python
> from brvalida import validar_cpf
> validar_cpf("123.456.789-09")  # True
> ```
>
> Também dá pra formatar o CPF usando o formatar_cpf(), que aceita com ou sem máscara. Caso o valor seja inválido, será lançada uma exceção ValueError.

### PTS-BR

> #### Biblioteca `brvalida`
>
> A biblioteca `brvalida` valida números do Cadastro de Pessoas Físicas (CPF) e do Cadastro Nacional da Pessoa Jurídica (CNPJ). A biblioteca também formata números de CPF. A biblioteca valida 100 000 números de CPF em aproximadamente 1 s.
>
> ##### Requisitos
>
> - Python 3.9 ou uma versão mais nova
>
> ##### Instalar a biblioteca
>
> 1. Instale o pacote `brvalida`:
>    ```shell
>    pip install brvalida
>    ```
> 2. Verifique a versão instalada:
>    ```shell
>    pip show brvalida
>    ```
>    A linha `Version` mostra o número da versão, por exemplo `1.4.0`.
>
> ##### Validar um número de CPF
>
> A função `validar_cpf()` recebe um número de CPF como string. Quando o número é válido, a função retorna o valor `True`. Quando o número é inválido, a função retorna o valor `False`.
>
> ```python
> from brvalida import validar_cpf
>
> validar_cpf("123.456.789-09")  # True
> validar_cpf("12345678900")     # False
> ```
>
> ##### Validar um número de CNPJ
>
> A função `validar_cnpj()` recebe um número de CNPJ como string, nos formatos `11.222.333/0001-81` e `11222333000181`. Quando o número é válido, a função retorna o valor `True`. Quando o número é inválido, a função retorna o valor `False`.
>
> A versão 1.4.0 valida apenas números de CNPJ com os caracteres de 0 a 9. Para um número de CNPJ com os caracteres de A a Z, a função retorna o valor `False`.
>
> ```python
> from brvalida import validar_cnpj
>
> validar_cnpj("11.222.333/0001-81")  # True
> validar_cnpj("11222333000100")      # False
> ```
>
> ##### Formatar um número de CPF
>
> A função `formatar_cpf()` recebe um número de CPF nos formatos `123.456.789-09` e `12345678909`. A função retorna o número no formato `000.000.000-00`. Quando o número é inválido, a função lança a exceção `ValueError`.
>
> ```python
> from brvalida import formatar_cpf
>
> formatar_cpf("12345678909")  # "123.456.789-09"
> formatar_cpf("12345678900")  # ValueError
> ```

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| brvalida (título) | [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor), [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor) | "Biblioteca `brvalida`": o substantivo de classe antes do nome, e o nome em código |
| Uma lib | [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) | "A biblioteca `brvalida`" (nome do glossário-base) |
| simples e super rápida | [R9.3](02-regras.md#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Um valor exato do Contexto: "valida 100 000 números de CPF em aproximadamente 1 s" |
| pra validar | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor) | "valida" |
| CPF e CNPJ | [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor) | O nome completo e a sigla entre parênteses, na primeira ocorrência |
| (o texto cita o CNPJ, mas não documenta a função) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | A seção "Validar um número de CNPJ" |
| (sem o limite da versão 1.4.0) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "A versão 1.4.0 valida apenas números de CNPJ com os caracteres de 0 a 9." e o resultado para os outros números de CNPJ |
| Instalação | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) | Título no infinitivo: "Instalar a biblioteca" |
| Basta rodar `pip install brvalida` e pronto! | [R9.3](02-regras.md#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | Passo 1, com o comando em um bloco de código |
| Obs: é necessário Python 3.9+. | [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor), [R5.2](02-regras.md#r52-use-o-imperativo-nos-passos-revisor), [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor) | Seção "Requisitos": "Python 3.9 ou uma versão mais nova" |
| (sem verificação da instalação) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | Passo 2, com o comando `pip show` e o resultado do passo |
| Como usar | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor) | Um título para cada tarefa: "Validar um número de CPF", "Validar um número de CNPJ" e "Formatar um número de CPF" |
| É só importar a função e passar o documento como string | [R9.3](02-regras.md#r93-não-use-palavras-vazias-de-julgamento-ou-de-cortesia-revisor), [R1.2](02-regras.md#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor), [R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor) | "A função `validar_cpf()` recebe um número de CPF como string." |
| a mesma retorna True se o doc for válido | [R1.8](02-regras.md#r18-não-use-o-mesmo-como-pronome-e-repita-o-substantivo-se-o-referente-for-ambíguo-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor), [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) | "Quando o número é válido, a função retorna o valor `True`." Um comportamento do sistema que sempre acontece usa "quando" e o presente. |
| (sem o resultado para um número inválido) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | "Quando o número é inválido, a função retorna o valor `False`." e uma linha no exemplo |
| Também dá pra formatar o CPF usando o formatar_cpf() | [R3.10](02-regras.md#r310-use-o-verbo-específico-não-um-verbo-geral-revisor), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | "A função `formatar_cpf()` recebe um número de CPF" |
| que aceita com ou sem máscara | [R1.2](02-regras.md#r12-use-cada-palavra-apenas-com-o-significado-aprovado-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Os 2 formatos exatos: `123.456.789-09` e `12345678909`. MASCARAR é um verbo técnico com outro significado. |
| Caso o valor seja inválido, será lançada uma exceção ValueError. | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | "Quando o número é inválido, a função lança a exceção `ValueError`." |

---

## Exemplo 9: Runbook de restauração de um banco de dados

Contexto: uma migração com defeito excluiu os itens dos pedidos no banco `pedidos`. O gerente de incidente decide restaurar o banco com um backup. O leitor é o analista de plantão da equipe de banco de dados. Estes dados não estão no texto "Antes":

- O banco `pedidos` é um banco PostgreSQL 16 no servidor `pedidos-db-01` do ambiente de produção. A tabela `itens_pedido` tem os itens dos pedidos.
- O serviço `api-pedidos` usa o banco `pedidos`. O serviço está no namespace `pedidos` do cluster `prod-sa-east-1`. Nenhuma ferramenta GitOps e nenhum objeto `HorizontalPodAutoscaler` alteram o número de réplicas do serviço.
- O worker `pedidos-worker` e o job de relatórios `relatorios-diarios` também se conectam ao banco `pedidos`.
- O incidente do PagerDuty tem a data e a hora de início da migração com defeito. O PagerDuty mostra um destes estados: **Triggered**, **Acknowledged** ou **Resolved**.
- A equipe faz um backup do banco `pedidos` todos os dias às 02:00 UTC-03:00, com o comando `pg_dump --format=custom`. Os backups estão na pasta `/backup/pedidos` do servidor `backup-01`. Um backup tem aproximadamente 20 GB.
- Para cada backup, o job de backup grava 2 arquivos. O arquivo `pedidos-AAAA-MM-DD.dump` tem o backup. O arquivo `pedidos-AAAA-MM-DD.linhas` tem o número de linhas das tabelas `pedidos` e `itens_pedido`. O job conta as linhas com o mesmo snapshot do comando `pg_dump` (opção `--snapshot`).
- O servidor `adm-01` é o host de administração da equipe de banco de dados. No servidor `adm-01`, a pasta `/mnt/backup/pedidos` dá acesso de leitura à pasta `/backup/pedidos` do servidor `backup-01`. O servidor `backup-01` não tem as credenciais do banco de produção nem do cluster.
- O usuário `restauracao` do banco tem os papéis de acesso `pedidos_ddl` e `pg_signal_backend`. O papel de acesso `pedidos_ddl` pode excluir e criar as tabelas do banco `pedidos`. O usuário `restauracao` não tem o atributo `SUPERUSER`. A senha do usuário está no cofre de segredos, no item `pedidos-db-01/restauracao`.
- O comando `pg_restore` não restaura os dados que o PostgreSQL usa para planejar as consultas. Sem o comando `ANALYZE`, as consultas do serviço `api-pedidos` demoram mais depois da restauração.
- O RPO do banco `pedidos` é 24 h. O RTO é 2 h. A cópia do estado atual do banco demora aproximadamente 15 min. A restauração demora aproximadamente 40 min.
- A decisão de restauração do gerente de incidente também aprova a indisponibilidade do serviço `api-pedidos` durante a cópia e a restauração.
- Depois do incidente, a equipe do serviço `api-pedidos` adiciona ao banco os pedidos da cópia do estado atual, com outro procedimento.
- A equipe de plataforma de dados recebe os incidentes que o analista de plantão encaminha. A equipe de plataforma de dados não é a equipe do analista de plantão.

### Antes

> **Restore do banco de pedidos**
>
> Em caso de perda de dados, restaurar o último backup. Primeiro derrubar a API de pedidos pra ninguém gravar no banco. Pegar o dump mais recente no servidor de backup e rodar o pg_restore com --clean no banco de prod. Depois conferir se os dados voltaram, subir a API de novo e ver se está tudo ok.
>
> Obs.: a restauração demora bastante e os pedidos feitos depois do backup são perdidos.

### PTS-BR

> #### Restaurar o banco `pedidos` com um backup
>
> - **Responsável:** analista de plantão da equipe de banco de dados
> - **Entrada:** a decisão de restauração do gerente de incidente, no incidente do PagerDuty
> - **Gatilho e prazo:** a decisão de restauração. Prazo: 2 h depois da decisão (RTO).
>
> ##### Objetivos de recuperação
>
> - RPO: 24 h. A empresa aceita a perda de até 24 h de pedidos. O backup tem os dados do banco `pedidos` até as 02:00 UTC-03:00 do dia do backup.
> - RTO: 2 h. A cópia do estado atual e a restauração demoram aproximadamente 1 h. Durante este tempo, o serviço `api-pedidos` está parado.
> - A restauração exclui do banco os dados gravados depois do backup. O procedimento 2 grava estes dados em uma cópia antes da restauração.
>
> ##### Procedimentos
>
> O runbook tem 6 procedimentos:
>
> 1. "Escolher e verificar o backup"
> 2. "Parar os clientes do banco e copiar o estado atual"
> 3. "Restaurar o backup"
> 4. "Iniciar o serviço `api-pedidos`"
> 5. "Reverter a restauração"
> 6. "Encaminhar o incidente com o serviço parado"
>
> O procedimento 4 é o rollback do procedimento 2. O procedimento 5 é o rollback do procedimento 3.
>
> ##### Antes de começar
>
> - Confirme que o incidente do PagerDuty tem a decisão de restauração do gerente de incidente.
> - Entre no host de administração `adm-01`. Execute todos os comandos deste runbook no servidor `adm-01`.
> - Confirme que o arquivo `~/.pgpass` do servidor `adm-01` contém a senha do usuário `restauracao` do servidor `pedidos-db-01`. A senha está no cofre de segredos, no item `pedidos-db-01/restauracao`.
> - Confirme que apenas o seu usuário pode ler e alterar o arquivo `~/.pgpass`:
>   ```shell
>   ls -l ~/.pgpass
>   ```
>   A primeira coluna da saída mostra o valor `-rw-------`. Com outra permissão, o comando `psql` não lê o arquivo e pede a senha.
>   - Se a primeira coluna mostrar outro valor, altere a permissão do arquivo para 600:
>     ```shell
>     chmod 600 ~/.pgpass
>     ```
> - Confirme que a sua conta pode escalar o serviço `api-pedidos` no cluster `prod-sa-east-1`:
>   ```shell
>   kubectl auth can-i patch deployments/api-pedidos \
>     --subresource scale \
>     --context prod-sa-east-1 \
>     --namespace pedidos
>   ```
>   O comando mostra a resposta `yes`.
> - Confirme que a pasta `/restauracao` do servidor `adm-01` tem 40 GB ou mais de espaço livre:
>   ```shell
>   df --human-readable /restauracao
>   ```
>   A coluna `Avail` mostra o espaço livre.
> - Instale estas ferramentas:
>   - as ferramentas `psql`, `pg_dump` e `pg_restore` 16 ou uma versão mais nova
>   - a ferramenta `kubectl` 1.30 ou uma versão mais nova
>
> ##### Procedimento 1: Escolher e verificar o backup
>
> Este procedimento não altera o ambiente de produção. Nas saídas de falha, o serviço `api-pedidos` continua sem alteração.
>
> 1. No incidente do PagerDuty, leia a data e a hora de início da migração com defeito.
> 2. Liste os arquivos de backup do banco `pedidos`:
>    ```shell
>    ls -l /mnt/backup/pedidos
>    ```
>    O comando mostra 2 arquivos para cada dia, por exemplo `pedidos-2026-11-18.dump` e `pedidos-2026-11-18.linhas`.
> 3. Escolha o último backup antes da hora de início da migração.
>
>    Exemplo: a migração começou às 01:30 UTC-03:00 de 2026-11-18. O backup correto é o backup de 2026-11-17. O backup de 2026-11-18 também tem o defeito.
>
>    A hora em que a equipe encontrou o defeito não indica o backup correto.
> 4. No incidente do PagerDuty, registre a data do backup do passo 3.
>
>    Registro: a data do backup, no incidente do PagerDuty.
> 5. Verifique o arquivo do backup:
>    ```shell
>    pg_restore --list /mnt/backup/pedidos/pedidos-<data-do-backup>.dump
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<data-do-backup>`: a data do passo 4, no formato AAAA-MM-DD, por exemplo `2026-11-18`.
>
>    O comando mostra a lista dos objetos do backup. O comando não altera o banco.
>
>    - Se a lista tiver uma linha com o texto `TABLE DATA public itens_pedido`, vá para o passo 6.
>    - Se o comando mostrar outra saída, informe o gerente de incidente com a saída do comando. Este procedimento termina neste passo.
> 6. Verifique o servidor e o banco da conexão:
>    ```shell
>    psql --host pedidos-db-01 --username restauracao --dbname pedidos --command "\conninfo"
>    ```
>    O comando mostra o banco e o servidor da conexão:
>    ```text
>    You are connected to database "pedidos" as user "restauracao" on host "pedidos-db-01" (address "10.20.8.15") at port "5432".
>    ```
>    - Se o comando mostrar o banco `pedidos` e o servidor `pedidos-db-01`, vá para o passo 7.
>    - Se o comando mostrar outro banco, outro servidor ou um erro, informe o gerente de incidente. Este procedimento termina neste passo.
> 7. Verifique a URL do cluster `prod-sa-east-1`:
>    ```shell
>    kubectl cluster-info --context prod-sa-east-1
>    ```
>    - Se o comando mostrar a URL `https://k8s.prod-sa-east-1.exemplo.com.br`, vá para o passo 8.
>    - Se o comando mostrar outra URL, informe o gerente de incidente. Este procedimento termina neste passo.
> 8. Obtenha o número de réplicas do serviço `api-pedidos`:
>    ```shell
>    kubectl get deployment api-pedidos \
>      --context prod-sa-east-1 \
>      --namespace pedidos \
>      --output jsonpath='{.spec.replicas}'
>    ```
>    - Se o comando mostrar um número, por exemplo `6`, vá para o passo 9.
>    - Se o comando mostrar a mensagem `NotFound`, informe o gerente de incidente. Este procedimento termina neste passo.
> 9. No incidente do PagerDuty, registre o número de réplicas do passo 8.
>
>    Registro: o número de réplicas do serviço, no incidente do PagerDuty. O procedimento 4 usa este número.
>
>    Depois do registro, siga o procedimento 2.
>
> ##### Procedimento 2: Parar os clientes do banco e copiar o estado atual
>
> O procedimento 4 é o rollback deste procedimento. O procedimento 4 inicia o serviço `api-pedidos` com o número de réplicas do procedimento 1.
>
> > **ATENÇÃO:** Escale o serviço `api-pedidos` para 0 réplicas apenas com a decisão de restauração no incidente. Depois do passo 1, os pods do serviço param. Durante aproximadamente 1 h, os clientes não podem criar nem consultar pedidos.
>
> 1. Escale o objeto `Deployment` `api-pedidos` para 0 réplicas:
>    ```shell
>    kubectl scale deployment/api-pedidos --replicas 0 --context prod-sa-east-1 --namespace pedidos
>    ```
>    O comando mostra a mensagem "deployment.apps/api-pedidos scaled".
> 2. Depois de 1 min, verifique os pods do serviço `api-pedidos`:
>    ```shell
>    kubectl get pods \
>      --context prod-sa-east-1 \
>      --namespace pedidos \
>      --selector app.kubernetes.io/name=api-pedidos
>    ```
>    - Se o comando mostrar a mensagem "No resources found in pedidos namespace.", vá para o passo 3.
>    - Se o comando mostrar um ou mais pods, repita este passo. Depois de 3 vezes, siga o procedimento 6.
> 3. Liste as sessões dos outros clientes do banco `pedidos`:
>    ```shell
>    psql --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --command "SELECT pid, usename, application_name FROM pg_stat_activity \
>        WHERE datname = 'pedidos' AND pid <> pg_backend_pid();"
>    ```
>    A condição `pid <> pg_backend_pid()` exclui a sessão do próprio comando `psql`.
>
>    - Se o comando mostrar o texto `(0 rows)`, vá para o passo 5.
>    - Se o comando mostrar uma ou mais linhas, vá para o passo 4.
>
> > **ATENÇÃO:** Feche apenas as sessões do banco `pedidos` do servidor `pedidos-db-01`. O comando fecha as conexões dos outros clientes do banco, por exemplo o worker `pedidos-worker`. Até o fim da restauração, estes clientes retornam erros.
>
> 4. Feche as sessões do passo 3:
>    ```shell
>    psql --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --command "SELECT pid, usename, pg_terminate_backend(pid) FROM pg_stat_activity \
>        WHERE datname = 'pedidos' AND pid <> pg_backend_pid();"
>    ```
>    - Se todas as linhas mostrarem o valor `t` na coluna `pg_terminate_backend`, volte ao passo 3 depois de 1 min. Depois de 3 vezes, siga o procedimento 6.
>    - Se uma linha mostrar o valor `f` ou se o comando mostrar o texto `ERROR`, siga o procedimento 6.
> 5. Conte as linhas das tabelas `pedidos` e `itens_pedido`:
>    ```shell
>    psql --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --command "SELECT (SELECT count(*) FROM pedidos) AS pedidos, \
>        (SELECT count(*) FROM itens_pedido) AS itens_pedido;"
>    ```
>    O comando mostra o número de linhas de cada tabela, nas colunas `pedidos` e `itens_pedido`.
> 6. Copie o estado atual do banco `pedidos` para um arquivo do servidor `adm-01`:
>    ```shell
>    pg_dump --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --format=custom \
>      --file /restauracao/pedidos-antes-<data-e-hora>.dump
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<data-e-hora>`: a data e a hora deste passo, no formato `AAAA-MM-DD-HHMM`, por exemplo `2026-11-18-0935`.
>
>    - Se o comando terminar sem mensagens, vá para o passo 7.
>    - Se o comando mostrar uma linha com o texto `pg_dump: error`, siga o procedimento 6.
> 7. Verifique o arquivo da cópia:
>    ```shell
>    pg_restore --list /restauracao/pedidos-antes-<data-e-hora>.dump
>    ```
>    - Se a lista tiver uma linha com o texto `TABLE DATA public itens_pedido`, vá para o passo 8.
>    - Se o comando mostrar outra saída, siga o procedimento 6.
> 8. No incidente do PagerDuty, registre os números do passo 5 e o nome do arquivo do passo 6.
>
>    Registro: o número de linhas das 2 tabelas e o nome do arquivo da cópia, no incidente do PagerDuty.
>
>    Depois do registro, siga o procedimento 3.
>
> ##### Procedimento 3: Restaurar o backup
>
> O procedimento 5 é o rollback deste procedimento. O procedimento 5 restaura a cópia do procedimento 2.
>
> > **PERIGO:** Restaure o backup apenas depois da cópia do procedimento 2. O comando exclui as tabelas do banco `pedidos` e cria as tabelas do backup. Sem a cópia, a empresa perde todos os pedidos gravados depois do backup.
>
> 1. Restaure o backup no banco `pedidos`:
>    ```shell
>    PGOPTIONS='-c lock_timeout=60s' pg_restore \
>      --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --clean \
>      --if-exists \
>      --single-transaction \
>      /mnt/backup/pedidos/pedidos-<data-do-backup>.dump
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<data-do-backup>`: a data do passo 4 do procedimento 1.
>
>    Com a opção `--single-transaction`, o PostgreSQL desfaz toda a restauração quando um erro acontece. A variável `PGOPTIONS` dá ao comando um tempo limite de 60 s para cada bloqueio. Com uma sessão nova no banco, o comando mostra um erro depois de 60 s e não aguarda sem limite.
>
>    - Se o comando terminar sem mensagens, vá para o passo 2.
>    - Se o comando mostrar uma linha com o texto `pg_restore: error`, siga o procedimento 6. O banco `pedidos` continua com os dados de antes deste passo.
> 2. Execute o comando `ANALYZE` no banco `pedidos`:
>    ```shell
>    psql --host pedidos-db-01 --username restauracao --dbname pedidos --command "ANALYZE;"
>    ```
>    O comando mostra o texto `ANALYZE`.
> 3. Leia o número de linhas das tabelas `pedidos` e `itens_pedido` no backup:
>    ```shell
>    cat /mnt/backup/pedidos/pedidos-<data-do-backup>.linhas
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<data-do-backup>`: a data do passo 4 do procedimento 1.
>
>    O comando mostra uma linha para cada tabela:
>    ```text
>    pedidos 1843077
>    itens_pedido 5120334
>    ```
> 4. Conte as linhas das tabelas `pedidos` e `itens_pedido` no banco restaurado:
>    ```shell
>    psql --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --command "SELECT (SELECT count(*) FROM pedidos) AS pedidos, \
>        (SELECT count(*) FROM itens_pedido) AS itens_pedido;"
>    ```
>    O comando mostra o número de linhas de cada tabela, nas colunas `pedidos` e `itens_pedido`.
> 5. No incidente do PagerDuty, registre os números dos passos 3 e 4.
>
>    Registro: o número de linhas do backup e do banco restaurado, no incidente do PagerDuty.
> 6. Compare os números dos passos 3 e 4 para cada tabela:
>    - Se os números das 2 tabelas forem iguais, siga o procedimento 4.
>    - Se um número for diferente, siga o procedimento 6. O banco `pedidos` tem os dados do backup. O gerente de incidente decide sobre o procedimento 5.
>
> ##### Procedimento 4: Iniciar o serviço `api-pedidos`
>
> 1. Escale o objeto `Deployment` `api-pedidos` para o número de réplicas do procedimento 1:
>    ```shell
>    kubectl scale deployment/api-pedidos \
>      --replicas <numero-de-replicas> \
>      --context prod-sa-east-1 \
>      --namespace pedidos
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<numero-de-replicas>`: o número do passo 9 do procedimento 1, por exemplo `6`.
>
>    O comando mostra a mensagem "deployment.apps/api-pedidos scaled".
> 2. Monitore os pods novos:
>    ```shell
>    kubectl rollout status deployment/api-pedidos \
>      --context prod-sa-east-1 \
>      --namespace pedidos \
>      --timeout 5m
>    ```
>    - Se o comando mostrar a mensagem "successfully rolled out", vá para o passo 3.
>    - Se o comando mostrar outra mensagem, encaminhe o incidente para a equipe do serviço `api-pedidos`, com a saída do comando. O banco tem os dados restaurados. Este procedimento termina neste passo.
> 3. Teste o endpoint `/health` do serviço `api-pedidos`:
>    ```shell
>    curl --fail --silent --show-error --max-time 10 https://pedidos.exemplo.com.br/health
>    ```
>    - Se o comando mostrar o texto `{"status":"ok"}`, vá para o passo 4.
>    - Se o comando mostrar um erro, encaminhe o incidente para a equipe do serviço `api-pedidos`, com a saída do comando. O banco tem os dados restaurados. Este procedimento termina neste passo.
> 4. No incidente do PagerDuty, informe ao gerente de incidente o fim da restauração, com a hora em UTC-03:00.
>
>    Registro: a hora do fim da restauração, no incidente do PagerDuty. Este procedimento termina neste passo.
>
> ##### Procedimento 5: Reverter a restauração
>
> Siga este procedimento apenas com a decisão de rollback do gerente de incidente. O procedimento restaura a cópia do procedimento 2. Depois do rollback, o banco `pedidos` tem os dados de antes da restauração, também os dados com o defeito da migração.
>
> ###### Antes de começar
>
> - Confirme que o incidente do PagerDuty tem a decisão de rollback do gerente de incidente.
> - Confirme que o incidente tem o nome do arquivo da cópia e o número de linhas das 2 tabelas, do passo 8 do procedimento 2.
>
> ###### Procedimento
>
> 1. Faça os passos 1 a 7 do procedimento 2. No passo 6, use o nome de arquivo `pedidos-antes-do-rollback-<data-e-hora>.dump`.
>
>    O serviço `api-pedidos` está parado. O arquivo novo tem os pedidos gravados depois da restauração.
>
>    Depois do passo 7 do procedimento 2, vá para o passo 2 deste procedimento.
>
> > **PERIGO:** Restaure a cópia apenas depois do passo 1. O comando exclui as tabelas do banco `pedidos` e cria as tabelas da cópia. Sem o arquivo novo do passo 1, a empresa perde os pedidos gravados depois da restauração.
>
> 2. Restaure a cópia do procedimento 2 no banco `pedidos`:
>    ```shell
>    PGOPTIONS='-c lock_timeout=60s' pg_restore \
>      --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --clean \
>      --if-exists \
>      --single-transaction \
>      /restauracao/<nome-do-arquivo-da-copia>
>    ```
>    Substitua o espaço reservado, com os sinais `<` e `>`:
>
>    - `<nome-do-arquivo-da-copia>`: o nome do arquivo no incidente, por exemplo `pedidos-antes-2026-11-18-0935.dump`.
>
>    - Se o comando terminar sem mensagens, vá para o passo 3.
>    - Se o comando mostrar uma linha com o texto `pg_restore: error`, siga o procedimento 6. O banco `pedidos` continua com os dados do backup.
> 3. Execute o comando `ANALYZE` no banco `pedidos`:
>    ```shell
>    psql --host pedidos-db-01 --username restauracao --dbname pedidos --command "ANALYZE;"
>    ```
>    O comando mostra o texto `ANALYZE`.
> 4. Conte as linhas das tabelas `pedidos` e `itens_pedido`:
>    ```shell
>    psql --host pedidos-db-01 \
>      --username restauracao \
>      --dbname pedidos \
>      --command "SELECT (SELECT count(*) FROM pedidos) AS pedidos, \
>        (SELECT count(*) FROM itens_pedido) AS itens_pedido;"
>    ```
>    O comando mostra o número de linhas de cada tabela, nas colunas `pedidos` e `itens_pedido`.
> 5. No incidente do PagerDuty, registre os números do passo 4.
>
>    Registro: o número de linhas do banco depois do rollback, no incidente do PagerDuty.
> 6. Compare os números do passo 4 com os números da cópia, no incidente:
>    - Se os números das 2 tabelas forem iguais, siga o procedimento 4.
>    - Se um número for diferente, siga o procedimento 6.
>
> ##### Procedimento 6: Encaminhar o incidente com o serviço parado
>
> As saídas de falha dos procedimentos 2, 3 e 5 indicam este procedimento. Nestas saídas, o serviço `api-pedidos` está parado. Os clientes não podem criar nem consultar pedidos.
>
> 1. No incidente do PagerDuty, escreva o estado do serviço `api-pedidos`, o passo com a falha e a saída do comando.
>
>    O gerente de incidente recebe estes dados no incidente.
>
>    Registro: o estado do serviço, o passo e a saída do comando, no incidente do PagerDuty.
> 2. No PagerDuty, encaminhe o incidente para a equipe de plataforma de dados.
> 3. Depois de 10 min, verifique o estado do incidente no PagerDuty:
>    - Se o estado for **Acknowledged**, a equipe de plataforma de dados é responsável pelo incidente. O gerente de incidente decide quando o serviço `api-pedidos` volta e com quais dados. Este procedimento termina neste passo.
>    - Se o estado for **Triggered**, informe o gerente de incidente. O gerente de incidente é responsável pelo incidente. Este procedimento termina neste passo.
>    - Se o estado for **Resolved**, o processo termina neste passo.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Restore do banco de pedidos | [R5.1](02-regras.md#r51-escreva-os-passos-em-uma-lista-numerada-na-ordem-de-execução-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor) | Título no infinitivo, com o nome do banco: "Restaurar o banco `pedidos` com um backup" |
| (sem responsável e sem prazo) | [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | O bloco **Responsável**, **Entrada** e **Gatilho e prazo**. O prazo é o RTO. |
| Em caso de perda de dados | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | O item **Gatilho e prazo**: a decisão de restauração do gerente de incidente |
| (sem RPO e sem RTO) | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Seção "Objetivos de recuperação": o RPO de 24 h e o RTO de 2 h, com o efeito de cada valor |
| restaurar o último backup | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R5.12](02-regras.md#r512-escreva-o-registro-que-a-etapa-gera-revisor) | Passos 1 a 4 do procedimento 1: o último backup antes do início da migração com defeito, com a frase "Registro:". Um backup de depois do início da migração também tem o defeito. Portanto, o passo 3 não usa a hora em que a equipe encontrou o defeito. |
| Pegar o dump mais recente | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | "Escolha o último backup antes da hora de início da migração", com um exemplo |
| no servidor de backup | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor) | O analista de plantão executa os comandos no host de administração `adm-01`, não no servidor de backup. A pasta `/mnt/backup/pedidos` dá acesso apenas de leitura aos backups. O servidor de backup não tem as credenciais do banco de produção nem do cluster. |
| (usuário de banco sem papel definido) | [R7.9](02-regras.md#r79-não-coloque-segredos-na-linha-de-comando-nem-no-texto-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R5.6](02-regras.md#r56-escreva-os-pré-requisitos-antes-do-passo-1-revisor) | O usuário `restauracao`, sem o atributo `SUPERUSER`, com os papéis de acesso da restauração. A senha está no arquivo `~/.pgpass` com a permissão 600 e no cofre de segredos. |
| (sem verificação do arquivo do backup) | [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | Passo 5 do procedimento 1: o comando `pg_restore --list` verifica o arquivo antes de qualquer alteração em produção. Na saída de erro, o serviço continua sem alteração. |
| derrubar a API de pedidos | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R1.10](02-regras.md#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor) | "Escale o objeto `Deployment` `api-pedidos` para 0 réplicas" (verbo técnico ESCALAR). O aviso diz "os pods do serviço param", com o sujeito no plural ([R1.10](02-regras.md#r110-não-use-a-forma-para-do-verbo-parar-se-a-frase-também-tiver-a-leitura-de-preposição-revisor)). |
| pra ninguém gravar no banco | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | Aviso ATENÇÃO antes do passo 1 do procedimento 2. A consequência é uma indisponibilidade total com recuperação conhecida: o procedimento 4 ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 2). |
| (sem os outros clientes do banco) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor) | Passos 3 e 4 do procedimento 2: o analista de plantão lista e fecha as sessões dos outros clientes. O passo 4 tem um aviso ATENÇÃO e um limite de 3 vezes. Sem estes passos, o comando `pg_restore --clean` aguarda o fim das outras sessões antes de excluir cada tabela. |
| (sem cópia do estado atual) | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.3](02-regras.md#r73-escreva-o-aviso-na-ordem-instrução-risco-consequência-revisor), [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) | Passos 5 a 8 do procedimento 2: o número de linhas, a cópia com o comando `pg_dump`, a verificação da cópia e a frase "Registro:". O aviso PERIGO do procedimento 3 tem a mesma instrução que o exemplo da regra [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor): a cópia antes da alteração. |
| rodar o pg_restore com --clean no banco de prod | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor), [R5.8](02-regras.md#r58-escreva-os-comandos-para-digitar-em-blocos-de-código-revisor) | Passos 6 e 7 do procedimento 1: o comando `\conninfo` mostra o servidor e o banco, e o comando `kubectl cluster-info` mostra o cluster. Passo 1 do procedimento 3: o comando completo, com o servidor e o banco nas opções `--host` e `--dbname`. |
| (restauração sem transação e sem tempo limite) | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor) | A opção `--single-transaction`: com um erro, o PostgreSQL desfaz toda a restauração. A variável `PGOPTIONS` com o parâmetro `lock_timeout`: o comando não aguarda sem limite. |
| (`<data-do-backup>` sem explicação) | [R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor) | A frase "Substitua o espaço reservado, com os sinais `<` e `>`" e a lista depois de cada bloco de código |
| os pedidos feitos depois do backup são perdidos | [R3.3](02-regras.md#r33-use-a-voz-ativa-revisor), [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.6](02-regras.md#r76-escreva-a-consequência-com-o-objeto-e-o-efeito-revisor) | Aviso PERIGO antes do passo 1 do procedimento 3. Sem a cópia, a consequência é a perda dos pedidos gravados depois do backup. O backup não tem estes dados ([R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), item 1). O exemplo 5 tem o mesmo nível para a mesma consequência. |
| (sem `ANALYZE` depois da restauração) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Passo 2 do procedimento 3. O comando `pg_restore` não restaura os dados que o PostgreSQL usa para planejar as consultas. |
| conferir se os dados voltaram | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Passos 3 a 6 do procedimento 3: o número de linhas da tabela `pedidos` e da tabela `itens_pedido`, no backup e no banco restaurado. A tabela `itens_pedido` é a tabela que a migração alterou. |
| subir a API de novo | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Procedimento 4: "Escale o objeto `Deployment` `api-pedidos` para o número de réplicas do procedimento 1". O passo 8 do procedimento 1 lê o número no cluster. O runbook não tem um número fixo. |
| ver se está tudo ok | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R5.9](02-regras.md#r59-termine-com-um-passo-de-verificação-revisor) | Passos 2 e 3 do procedimento 4: o estado dos pods e o endpoint `/health`, com o resultado exato |
| (sem caminho de volta) | [R5.13](02-regras.md#r513-escreva-um-procedimento-para-reverter-cada-alteração-do-ambiente-de-produção-revisor) | Procedimento 5, "Reverter a restauração", com a seção "Antes de começar", um aviso PERIGO e uma verificação. A seção "Procedimentos" diz qual procedimento é o rollback de cada procedimento. |
| (saídas de falha sem o estado do serviço) | [R5.11](02-regras.md#r511-escreva-cada-ponto-de-decisão-com-todas-as-saídas-revisor), [R5.10](02-regras.md#r510-escreva-o-responsável-do-procedimento-e-de-cada-etapa-revisor) | Procedimento 6: o gerente de incidente recebe o estado do serviço `api-pedidos`, e o incidente vai para a equipe de plataforma de dados. O incidente não volta para a equipe do analista de plantão. |
| a restauração demora bastante | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "A cópia do estado atual e a restauração demoram aproximadamente 1 h." |
| Obs.: | [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor), [R7.4](02-regras.md#r74-escreva-o-aviso-antes-da-ação-perigosa-revisor), [R7.7](02-regras.md#r77-marque-o-aviso-apenas-com-a-palavra-de-sinalização-revisor) | Os avisos ATENÇÃO e PERIGO, cada um antes do passo da ação |

---

## Exemplo 10: Comunicados de um incidente na página de status

Contexto: 3 comunicados do incidente do exemplo 9 na página de status da loja. O leitor é um cliente da loja. Estes dados não estão no texto "Antes":

- Às 08:50 UTC-03:00 de 2026-11-18, a equipe de operação encontrou o defeito. A página **Meus pedidos** mostra os pedidos sem a lista de produtos.
- Durante o defeito, os clientes podem criar pedidos novos. O defeito não alterou os pagamentos dos pedidos.
- Durante a restauração, das 09:30 até aproximadamente 10:30 UTC-03:00, os clientes não podem criar nem consultar pedidos.
- A restauração usa o backup das 02:00 UTC-03:00. Até as 18:00 UTC-03:00, a equipe do serviço adiciona de novo os pedidos criados entre 02:00 e 09:30 UTC-03:00.
- A página de status mostra um destes estados: **Investigando**, **Identificado**, **Monitorando** ou **Resolvido**. A empresa publica uma atualização a cada 30 min ou menos. O exemplo mostra o primeiro comunicado, um comunicado de atualização e o último comunicado.
- Um comunicado de incidente não tem a causa interna do incidente. A análise pós-incidente tem a causa.

### Antes

> **Instabilidade na plataforma** (09:00)
>
> Estamos enfrentando uma instabilidade pontual e alguns clientes podem estar com dificuldades para visualizar seus pedidos. Nosso time já está atuando para normalizar a situação o mais breve possível. Pedimos desculpas pelo transtorno!
>
> **Atualização** (09:25)
>
> Identificamos a causa raiz (falha em uma migration do banco de dados) e vamos realizar uma manutenção emergencial. A plataforma ficará fora do ar por alguns minutos. Em breve traremos novidades.
>
> **Resolvido** (10:45)
>
> Problema resolvido! A plataforma já está 100% operacional. Caso algum pedido feito hoje não apareça, entre em contato com o SAC.

### PTS-BR

> #### Pedidos sem a lista de produtos
>
> ##### Comunicado 1: início do incidente
>
> Data e hora: 2026-11-18 09:00 UTC-03:00. Estado: **Investigando**.
>
> Desde as 08:50 UTC-03:00, a página **Meus pedidos** do site e da aplicação da loja mostra os seus pedidos sem a lista de produtos. Você pode criar pedidos novos. O defeito não altera os pagamentos. A equipe de operação procura a causa do defeito.
>
> A próxima atualização é às 09:30 UTC-03:00.
>
> ##### Comunicado 2: atualização
>
> Data e hora: 2026-11-18 09:25 UTC-03:00. Estado: **Identificado**.
>
> A equipe de operação encontrou a causa e vai corrigir os pedidos. Das 09:30 até aproximadamente 10:30 UTC-03:00, você não pode criar nem consultar pedidos no site e na aplicação da loja. O defeito não altera os pagamentos.
>
> A próxima atualização é às 09:55 UTC-03:00.
>
> ##### Comunicado 3: resolução
>
> Data e hora: 2026-11-18 10:45 UTC-03:00. Estado: **Resolvido**.
>
> Desde as 10:35 UTC-03:00, você pode criar e consultar pedidos no site e na aplicação da loja. A página **Meus pedidos** mostra a lista de produtos de cada pedido.
>
> Os pedidos criados entre 02:00 e 09:30 UTC-03:00 de 2026-11-18 não estão na página **Meus pedidos**. Até as 18:00 UTC-03:00 de 2026-11-18, a equipe adiciona estes pedidos à página. Se um pedido não estiver na página depois das 18:00 UTC-03:00, envie o número do pedido ao suporte.
>
> Este comunicado é o último comunicado deste incidente.

### Alterações

| Trecho original | Regra | Forma PTS-BR |
|---|---|---|
| Instabilidade na plataforma | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | Título com o efeito para o cliente: "Pedidos sem a lista de produtos" |
| (09:00) | [R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor) | A data e a hora com o fuso horário em cada comunicado: "Data e hora: 2026-11-18 09:00 UTC-03:00." |
| (sem o estado da página de status) | [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor), [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | O estado da página de status em cada comunicado, em negrito: **Investigando**, **Identificado** e **Resolvido** |
| Estamos enfrentando uma instabilidade pontual | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | A hora de início e o efeito: "Desde as 08:50 UTC-03:00, a página **Meus pedidos** [...] mostra os seus pedidos [...]" |
| alguns clientes podem estar com dificuldades | [R3.8](02-regras.md#r38-use-poder-e-dever-com-um-único-significado-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R9.1](02-regras.md#r91-escreva-para-o-leitor-na-forma-você-revisor) | Um fato, na forma "você": "mostra os seus pedidos sem a lista de produtos" |
| (sem o que o cliente pode fazer) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "Você pode criar pedidos novos." e "O defeito não altera os pagamentos." |
| Nosso time já está atuando | [R3.6](02-regras.md#r36-use-o-gerúndio-apenas-para-uma-ação-em-andamento-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "A equipe de operação procura a causa do defeito." |
| o mais breve possível, Em breve traremos novidades | [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor) | A hora da próxima atualização em cada comunicado: "A próxima atualização é às 09:30 UTC-03:00." |
| Pedimos desculpas pelo transtorno! | [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor) | Remova a frase. O comunicado tem o efeito, a ação da equipe e a hora da próxima atualização. |
| Identificamos a causa raiz (falha em uma migration do banco de dados) | [R8.3](02-regras.md#r83-não-use-ponto-e-vírgula-barra-entre-palavras-nem-inserções-revisor), [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "A equipe de operação encontrou a causa e vai corrigir os pedidos." A causa interna está na análise pós-incidente. |
| vamos realizar uma manutenção emergencial | [R3.5](02-regras.md#r35-use-o-verbo-não-um-verbo-suporte-com-um-substantivo-vale), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | O efeito para o cliente: "você não pode criar nem consultar pedidos" |
| ficará fora do ar por alguns minutos | [R3.1](02-regras.md#r31-use-apenas-os-tempos-verbais-aprovados-vale), [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | O intervalo exato: "Das 09:30 até aproximadamente 10:30 UTC-03:00" |
| Problema resolvido! | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R8.1](02-regras.md#r81-termine-as-frases-com-ponto-final-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | A hora e o efeito: "Desde as 10:35 UTC-03:00, você pode criar e consultar pedidos" |
| 100% operacional | [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | "A página **Meus pedidos** mostra a lista de produtos de cada pedido." |
| Caso algum pedido feito hoje não apareça | [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor), [R9.4](02-regras.md#r94-escreva-referências-estáveis-revisor), [R6.4](02-regras.md#r64-escreva-valores-não-palavras-vagas-revisor) | O intervalo dos pedidos afetados e o prazo da correção: "entre 02:00 e 09:30 UTC-03:00" e "Até as 18:00 UTC-03:00" |
| entre em contato com o SAC | [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor), [R1.1](02-regras.md#r11-use-apenas-palavras-aprovadas-e-termos-técnicos-vale) | "envie o número do pedido ao suporte" |
| (sem o fim dos comunicados) | [R9.5](02-regras.md#r95-escreva-listas-completas-revisor) | "Este comunicado é o último comunicado deste incidente." |

---

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · **06 Exemplos** · [Versões](CHANGELOG.md)

<!-- rodape -->
Feito com ❤️ em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Alguns direitos reservados.

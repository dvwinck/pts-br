# 04 — Termos técnicos

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · **04 Termos técnicos** · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

PTS-BR — Português Técnico Simplificado, versão 1.0.0, 2026-11-18.
A estrutura do PTS-BR segue a estrutura do ASD-STE100. O PTS-BR não é uma tradução oficial do ASD-STE100, e a ASD não aprovou o PTS-BR.

Este arquivo controla o **vocabulário técnico** do PTS-BR: as categorias de nomes técnicos, os verbos técnicos, a política de estrangeirismos e o glossário-base de TI. O vocabulário geral está em [`03-dicionario.md`](03-dicionario.md).

## Sumário

1. [Escopo e definições](#1-escopo-e-definições)
2. [Regras gerais dos termos técnicos](#2-regras-gerais-dos-termos-técnicos)
3. [Categorias de nomes técnicos](#3-categorias-de-nomes-técnicos)
4. [Verbos técnicos](#4-verbos-técnicos)
5. [Política de estrangeirismos](#5-política-de-estrangeirismos)
6. [Glossário-base de TI](#6-glossário-base-de-ti)
7. [Glossário do projeto](#7-glossário-do-projeto)

---

## 1. Escopo e definições

| Termo | Definição |
|---|---|
| Nome técnico | Um substantivo ou um grupo de substantivos que identifica um item, um conceito ou um artefato de TI ou do projeto. Um nome técnico pertence a uma das categorias da seção 3. |
| Verbo técnico | Um verbo que identifica uma operação técnica. A seção 4 tem a lista fechada dos verbos técnicos. |
| Estrangeirismo | Uma palavra de outra língua, em geral do inglês, que o texto usa como nome técnico. A seção 5 define quando o PTS-BR aceita um estrangeirismo. |
| Literal | Um texto que o leitor digita, que o sistema lê ou que o sistema mostra. Exemplos: um comando, um nome de arquivo, um rótulo de interface, uma mensagem. Um literal não é vocabulário do texto. Copie o literal sem alteração e use o formato da regra [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor). |
| Glossário-base | A lista de termos técnicos de TI que todos os projetos usam (seção 6). |
| Glossário do projeto | A lista de nomes de um produto ou de uma equipe: componentes, telas, papéis e ambientes (seção 7). |
| Sigla de uso geral | Uma sigla da tabela da seção 6.1. O texto pode usar a sigla sem o nome completo (regra [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor)). |

O dicionário ([`03-dicionario.md`](03-dicionario.md)) e este arquivo não têm palavras em comum, com 3 exceções:

- Algumas palavras gerais do dicionário também têm um significado técnico em uma categoria da seção 3 (03-dicionario.md, regra D7). Estas palavras são ENTRADA, EXCEÇÃO, FORMA, LINHA, PROCESSO e TABELA. Escreva o tipo antes do nome técnico. Exemplos: "a exceção `TimeoutError`", "o processo `nginx`", "a tabela `pedidos`", "a linha 42 da tabela `clientes`", "a forma flexionada".
- "Nós", plural do nome técnico "nó", tem a mesma forma do pronome "nós", que o dicionário não aprova. Escreva sempre um artigo, uma contração ou um número antes do plural técnico: "os nós", "dos nós", "3 nós". O pronome não tem estas palavras antes (03-dicionario.md, regra D11, e 02-regras.md, regra [R9.1](02-regras.md#r91-escreva-para-o-leitor-na-forma-você-revisor)). O PTS-BR não usa "node" no lugar de "nó".
- "Conta", nome técnico (seção 6.2), tem a mesma forma do verbo CONTAR do dicionário ("O script conta as linhas"). Escreva sempre um artigo, uma contração ou um pronome antes do nome técnico: "a conta", "da conta", "sua conta" (03-dicionario.md, regra D11).

---

## 2. Regras gerais dos termos técnicos

**T1. Use o nome técnico como substantivo.** Não crie um verbo nem um adjetivo a partir de um nome técnico.

> Não aprovado: A resposta está cacheada.
> PTS-BR: O serviço armazena a resposta no cache.

**T2. Use um nome para cada item ([R1.4](02-regras.md#r14-use-uma-palavra-para-cada-conceito-revisor)).** Use o nome do glossário-base ou do glossário do projeto. Não alterne sinônimos.

> Não aprovado: Crie o diretório `backup`. Depois, copie os arquivos para a pasta `backup`.
> PTS-BR: Crie a pasta `backup`. Depois, copie os arquivos para a pasta `backup`.

**T3. Use o nome técnico apenas com o significado técnico.** Não use um nome técnico com um significado não técnico ([R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor)).

> Não aprovado: Faça o deploy da ideia para a diretoria.
> PTS-BR: Mostre a ideia ao gestor.

**T4. Escreva o nome completo da sigla na primeira ocorrência.** As siglas da tabela de siglas de uso geral (seção 6.1) e do glossário-base (seção 6.2) não precisam do nome completo. Para outra sigla, escreva o nome completo e a sigla entre parênteses na primeira ocorrência do documento. Depois, use apenas a sigla.

> PTS-BR: O tempo médio entre falhas (MTBF) do disco é 1 000 000 h. O MTBF do disco novo é 2 000 000 h.

**T5. Escreva o artigo e o substantivo de classe antes de um literal ([R1.5](02-regras.md#r15-escreva-os-artigos-e-o-substantivo-de-classe-antes-de-literais-revisor)).**

> Não aprovado: Execute `git push`. Altere `PORT`.
> PTS-BR: Execute o comando `git push`. Altere a variável `PORT`.

**T6. Não traduza um literal.** Copie o literal com as letras maiúsculas e minúsculas originais. Se a interface estiver em inglês, escreva o rótulo em inglês.

> PTS-BR: Clique em **Deploy**. O pipeline executa o deploy.

**T7. Limite as cadeias de nomes ([R2.1](02-regras.md#r21-use-no-máximo-3-substantivos-em-uma-cadeia-com-de-revisor), [R2.3](02-regras.md#r23-não-use-a-ordem-do-inglês-em-substantivos-compostos-revisor)).** Use no máximo 3 substantivos em uma cadeia nominal com "de". Um termo composto do glossário-base (seção 6), por exemplo "banco de dados", conta como 1 substantivo. Use a ordem do português: escreva o núcleo primeiro.

> Não aprovado: Reinicie o database server.
> PTS-BR: Reinicie o servidor de banco de dados.

**T8. Use um verbo técnico apenas com o significado técnico (seção 4).** Para o significado geral, use o verbo do dicionário.

---

## 3. Categorias de nomes técnicos

Um nome técnico pode estar fora do dicionário se pertencer a uma destas 25 categorias. Cada categoria tem uma definição, uma regra de uso, exemplos e uma frase em PTS-BR.

### NT-01 Produtos, softwares e serviços externos

- **Definição:** O nome próprio de um produto, de um software ou de um serviço de outra empresa ou de um projeto de código aberto.
- **Regra de uso:** Escreva o nome com a grafia oficial do produto, com as maiúsculas originais. Use o artigo masculino ("o PostgreSQL"), exceto se o nome tiver um núcleo feminino em português ("a AWS", empresa). Não traduza o nome e não use o nome no plural.
- **Exemplos:** PostgreSQL, Kubernetes, GitHub, GitLab, Jira, Grafana, Amazon S3, AWS Lambda, Microsoft Entra ID, Docker.
- **PTS-BR:** Atualize o PostgreSQL para a versão 16.

### NT-02 Componentes do sistema do projeto

- **Definição:** O nome de uma parte do sistema que a equipe cria e mantém: um serviço, um módulo, uma fila, um job.
- **Regra de uso:** Use o nome do glossário do projeto. Escreva o tipo do componente antes do nome. Use o mesmo nome em todos os documentos.
- **Exemplos:** o serviço de pagamentos, a API de pedidos, o worker de e-mail, a fila `pedidos-novos`, o job `limpeza-diaria`.
- **PTS-BR:** O serviço de pagamentos envia um evento para a fila `pedidos-novos`.

### NT-03 Comandos, código e identificadores

- **Definição:** Um texto que um computador lê: um comando, uma opção de comando, uma função, uma classe, uma variável, um parâmetro, uma chave de configuração.
- **Regra de uso:** Use o formato de código ([R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor)). Escreva o tipo do item antes do literal (T5). Copie o literal sem alteração.
- **Exemplos:** Comandos: o comando `kubectl apply`, a opção `--dry-run`. Código: a função `validar_cpf()`, o método `salvar()`, o argumento `timeout`, a exceção `TimeoutError`, a classe `PedidoService`, a variável `PORT`. Configuração: a chave `max_connections`.
- **PTS-BR:** Defina a chave `max_connections` como `200`.

### NT-04 Arquivos, pastas, caminhos e URLs

- **Definição:** O nome ou o endereço de um arquivo, de uma pasta ou de um recurso na web.
- **Regra de uso:** Use o formato de código. Use "pasta", não "diretório" (T2). Escreva a URL completa, com o protocolo.
- **Exemplos:** o arquivo `config.yaml`, a pasta `/var/log`, a URL `https://api.exemplo.com.br/v1/pedidos`.
- **PTS-BR:** Copie o arquivo `config.yaml` para a pasta `/etc/app`.

### NT-05 Elementos de interface

- **Definição:** Uma parte da interface que o usuário vê ou usa.
- **Regra de uso:** O tipo do elemento é um nome técnico. O rótulo do elemento é um literal: escreva o rótulo em negrito, com o texto exato da interface ([R10.1](02-regras.md#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor)). Use o verbo do tipo do elemento ([R10.2](02-regras.md#r102-use-o-verbo-do-tipo-de-elemento-revisor) e seção 4.2.A). O nome de um ícone também é um nome técnico desta categoria: "o ícone de lápis", "o ícone de engrenagem". Se o ícone tiver um rótulo ou um texto alternativo, escreva também o rótulo: "o ícone de lápis (**Editar**)".
- **Exemplos:** Formulários: botão, campo, formulário, caixa de seleção, botão de opção, lista suspensa, interruptor. Navegação e janelas: menu, guia, ícone, link, janela, caixa de diálogo, tela, página, barra de ferramentas, barra lateral, barra de rolagem. Funções da interface: perfil, busca, campo de busca, filtro, notificação. Ícones: lápis, engrenagem, lixeira, lupa, sino, seta.
- **PTS-BR:** Digite o e-mail no campo **E-mail**. Clique em **Salvar**. Para alterar a foto do seu perfil, clique no ícone de lápis.

### NT-06 Teclas e grupos de teclas

- **Definição:** Uma tecla do teclado, um grupo de teclas que o usuário pressiona ao mesmo tempo, ou uma parte do mouse.
- **Regra de uso:** Escreva a tecla em negrito, com o texto do teclado. Junte as teclas com "+", sem espaços ([R10.3](02-regras.md#r103-escreva-caminhos-de-menu-e-teclas-em-um-formato-fixo-revisor)). Use o verbo PRESSIONAR. Para as 4 teclas de seta, escreva a direção: "a seta para baixo". Para a roda do mouse, use o verbo técnico ROLAR.
- **Exemplos:** tecla, teclado, tecla de seta, seta, **Enter**, **Esc**, **Tab**, **Ctrl+C**, **Ctrl+Shift+P**, **Cmd+K**, botão do mouse, roda do mouse.
- **PTS-BR:** Pressione **Ctrl+C** para parar o processo. Pressione a seta para baixo para escolher a próxima opção da lista.

### NT-07 Mensagens e textos do sistema

- **Definição:** Um texto que o sistema mostra ao usuário ou grava em um log.
- **Regra de uso:** Escreva o texto entre aspas duplas, sem alteração ([R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor)). Não traduza a mensagem. Se a mensagem estiver em inglês, explique o significado na próxima frase.
- **Exemplos:** "Arquivo salvo.", "Connection refused", "Acesso negado".
- **PTS-BR:** A aplicação cliente mostra a mensagem "Connection refused". O servidor recusa a conexão.

### NT-08 Códigos, identificadores e números de referência

- **Definição:** Um código que identifica um erro, um item ou uma versão, também em outro sistema.
- **Regra de uso:** Use o formato de código. Copie o código sem alteração. Escreva o tipo do código antes do código.
- **Exemplos:** Códigos: o código de status `404`, o código de erro `ERR_CERT_DATE_INVALID`, a CVE `CVE-2024-3094`. Identificadores: o chamado `OPS-1234`, o commit `a1b2c3d`, a versão `v2.4.1`, o CPF `123.456.789-09`.
- **PTS-BR:** A API retorna o código de status `429` quando a aplicação cliente envia mais requisições que o limite de taxa.

### NT-09 Protocolos e padrões técnicos

- **Definição:** Um conjunto de regras que define como os sistemas enviam e recebem dados ou como um dado é escrito.
- **Regra de uso:** Use a sigla oficial. As siglas da seção 6.1 não precisam do nome completo. Escreva a versão quando a versão afeta o comportamento. Use o artigo masculino ("o protocolo"): "o HTTP", "o OAuth 2.0".
- **Exemplos:** HTTP, HTTPS, TLS 1.3, SSH, SFTP, SMTP, DNS, OAuth 2.0, OpenID Connect, gRPC, WebSocket, ISO 8601.
- **PTS-BR:** O servidor aceita apenas o TLS 1.3.

### NT-10 Formatos de dados e de arquivo

- **Definição:** A estrutura de um arquivo ou de um conjunto de dados.
- **Regra de uso:** Use o nome oficial em maiúsculas. As siglas da seção 6.1 não precisam do nome completo. Use o artigo masculino ("o formato JSON", "um arquivo CSV").
- **Exemplos:** JSON, YAML, CSV, XML, PDF, PNG, Parquet, Markdown, ZIP.
- **PTS-BR:** Converta o relatório para o formato CSV.

### NT-11 Linguagens, frameworks e bibliotecas

- **Definição:** Uma linguagem de programação, um framework ou uma biblioteca de software.
- **Regra de uso:** Use a grafia oficial. Escreva a versão com o número completo quando a versão afeta o procedimento.
- **Exemplos:** linguagem de programação, interpretador, Python 3.12, Java 21, TypeScript, Go, Django, React, Node.js 20, Spring Boot.
- **PTS-BR:** O build precisa do Node.js 20 ou de uma versão mais nova.

### NT-12 Infraestrutura física e virtual

- **Definição:** Um equipamento ou uma máquina virtual que executa software ou que envia e recebe dados.
- **Regra de uso:** Use o nome do glossário-base. "Nó" tem o plural "nós" (seção 1).
- **Exemplos:** servidor, nó, cluster, máquina virtual, contêiner, disco, memória, processador, mouse, cabo, SSD, rack, switch, roteador, balanceador de carga, data center, plataforma.
- **PTS-BR:** Drene o nó 3 antes da manutenção.

### NT-13 Recursos de nuvem

- **Definição:** Um recurso que um provedor de nuvem cria e vende pelo tempo ou pelo consumo.
- **Regra de uso:** Em texto geral, use o nome do glossário-base ("instância de máquina virtual", "bucket"). Use o nome do produto do provedor de nuvem apenas em texto específico para este provedor de nuvem ("a instância EC2").
- **Exemplos:** instância, bucket, região, zona de disponibilidade, VPC, sub-rede, grupo de segurança, função sem servidor, fila gerenciada, cota.
- **PTS-BR:** Crie o bucket na região `sa-east-1`.

### NT-14 Rede e endereços

- **Definição:** Um item que identifica ou que liga sistemas em uma rede.
- **Regra de uso:** Use o formato de código para um valor que o leitor digita ou copia ("o endereço `10.0.0.12`"). Para uma referência geral, escreva o valor sem formato ("a porta 443").
- **Exemplos:** endereço IP, porta, domínio, sub-rede, gateway, proxy, firewall, VPN, DNS, CIDR, internet, tráfego.
- **PTS-BR:** Crie uma regra no firewall que permite o tráfego do endereço de origem `10.0.0.12` para a porta 443.

### NT-15 Dados e banco de dados

- **Definição:** Um item que armazena, organiza ou obtém dados em um banco de dados.
- **Regra de uso:** Use o nome do glossário-base. Para a tabela de um banco, escreva "a tabela `pedidos`" ou "a tabela do banco", para separar este significado do significado geral de TABELA (03-dicionario.md, D7). Um item de uma tabela do banco é uma "linha" (D7). Não use "registro" com este significado. REGISTRO (03) documenta uma ação, um resultado ou um evento.
- **Exemplos:** Estrutura: banco de dados, tabela do banco, coluna, linha, índice, esquema, chave primária. Operações: consulta, transação, migração, réplica primária, réplica secundária. Cópias: retenção, backup completo, backup incremental, recuperação até um ponto no tempo.
- **PTS-BR:** Crie um índice na coluna `cliente_id` da tabela `pedidos`.

### NT-16 Segurança e identidade

- **Definição:** Um item que identifica uma pessoa ou um sistema, que controla o acesso ou que descreve um ataque ou uma vulnerabilidade.
- **Regra de uso:** Use o nome do glossário-base. Não escreva o valor real de um segredo em um documento. Use um espaço reservado ([R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor)). Para o conjunto de permissões de RBAC ou de IAM, use "papel de acesso". Se a interface mostrar **Função** ou **Role**, o rótulo é um literal (E1). Não use "perfil de acesso" nem "função" com este significado.
- **Exemplos:** Credenciais: senha, token, chave de API, chave privada, chave SSH, certificado, segredo, credencial, cofre de segredos. Acesso: conta, conta de serviço, superusuário, papel de acesso, política, privilégio mínimo, MFA, SSO, LDAP. Riscos: vulnerabilidade, CVE, dados pessoais, dados pessoais sensíveis, DDoS.
- **PTS-BR:** Armazene a chave de API no cofre de segredos. Não escreva a chave no código.

### NT-17 Desenvolvimento e entrega de software

- **Definição:** Um conceito ou um artefato do desenvolvimento, do teste e da entrega de software.
- **Regra de uso:** Use o nome do glossário-base e a forma da política de estrangeirismos (seção 5). Para a ação, use um verbo técnico ou um verbo do dicionário com o nome técnico: "Crie um commit", "Execute o deploy".
- **Exemplos:** repositório, commit, branch, merge, pull request, build, deploy, pipeline, artefato, tag, versão, dependência, pacote, código-fonte, entrega contínua.
- **PTS-BR:** Crie um commit com as alterações. Depois, crie um pull request para o branch `main`.

### NT-18 Ambientes

- **Definição:** Um conjunto de servidores, de configurações e de dados com um uso definido.
- **Regra de uso:** Na primeira ocorrência, escreva "ambiente de" e o nome: "o ambiente de produção". Depois, você pode usar apenas o nome: "produção". Use os nomes do glossário do projeto.
- **Exemplos:** produção, homologação, desenvolvimento, ambiente local, ambiente de teste.
- **PTS-BR:** Teste a migração no ambiente de homologação antes da produção.

### NT-19 Papéis de pessoas em processos

- **Definição:** O nome de uma responsabilidade que uma pessoa ou uma equipe tem em um processo ou em um sistema.
- **Regra de uso:** Use o nome do papel, não o nome da pessoa. Use o papel para descrever quem faz uma ação. Não use o papel em uma instrução ao leitor: escreva a instrução no imperativo ([R9.1](02-regras.md#r91-escreva-para-o-leitor-na-forma-você-revisor)). Use cada nome com um significado:
  - "papel": a responsabilidade de uma pessoa em um processo (esta categoria).
  - "papel de acesso": um conjunto de permissões em um sistema ([NT-16](#nt-16-segurança-e-identidade)).
  - RESPONSÁVEL (03): a pessoa ou a equipe que faz uma etapa de um processo.
  - CARGO (03): a posição de uma pessoa na estrutura da empresa.
  - "função": apenas a função de código ([NT-03](#nt-03-comandos-código-e-identificadores)).
- **Exemplos:** Sistemas: administrador, desenvolvedor, operador, designer, usuário, cliente. Processos: revisor, aprovador, solicitante, gestor, colaborador. Incidentes: analista de plantão, gerente de incidente. Produto: dono do produto, gerente de produto. Documentos: leitor, redator.
- **PTS-BR:** O analista de plantão recebe o alerta e cria o incidente.

### NT-20 Artefatos de processo

- **Definição:** Um documento, um registro ou um evento que um processo de trabalho cria ou usa.
- **Regra de uso:** Use o nome do glossário-base ou do glossário do projeto. Escreva o identificador do artefato no formato de código ([NT-08](#nt-08-códigos-identificadores-e-números-de-referência)).
- **Exemplos:** Registros: chamado, issue, solicitação de mudança, auditoria, desvio, ação corretiva. Incidentes: incidente, causa raiz, mitigação, linha do tempo, análise pós-incidente, lições aprendidas. Comunicação: comunicado de incidente, página de status. Documentos: runbook, ADR, notas de versão, critério de aceite, ponto de decisão. Planejamento: recuperação de desastre, sprint, backlog, janela de manutenção.
- **PTS-BR:** Registre a decisão no ADR `ADR-012`.

### NT-21 Métricas, indicadores e níveis de serviço

- **Definição:** Um valor que mede o comportamento, o desempenho ou a qualidade de um sistema ou de um processo.
- **Regra de uso:** Escreva o valor com a unidade ([NT-22](#nt-22-unidades-de-medida)). Defina a métrica no glossário na primeira ocorrência.
- **Exemplos:** Desempenho: latência, taxa de erro, disponibilidade, degradação, percentil 99 (p99), vazão, largura de banda. Qualidade: cobertura de testes, falso positivo, falso negativo, indicador, meta. Níveis de serviço: SLA, SLO, SLI, MTTR, RPO, RTO.
- **PTS-BR:** O SLO de latência p99 da API é 300 ms.

### NT-22 Unidades de medida

- **Definição:** Uma quantidade padrão que mede tempo, tamanho, velocidade ou frequência.
- **Regra de uso:** Use os símbolos do Sistema Internacional e da norma IEC 80000-13. Não traduza o símbolo.
  - Depois de um número, escreva sempre o símbolo, não o nome da unidade: "10 min", "1 h", "30 s", "512 MB". Sem número, escreva o nome: "a cada minuto". Para a hora, escreva sempre o número e o símbolo ("a cada 1 h"), porque a palavra "hora" é o momento do dia (03-dicionario.md, HORA).
  - Escreva um espaço entre o número e o símbolo ([R8.4](02-regras.md#r84-escreva-números-e-unidades-em-um-formato-fixo-vale)), exceto antes de "%".
  - Prefixo decimal: 1 kB = 1 000 B (com a letra "k" minúscula). MB, GB e TB com maiúsculas. Prefixo binário: 1 KiB = 1 024 B, MiB, GiB e TiB.
  - Use o prefixo da unidade que o sistema configura ou mostra. A memória e os limites de um contêiner usam o prefixo binário (MiB, GiB).
  - Para uma taxa de dados, use bit/s com prefixo: kbit/s, Mbit/s, Gbit/s. Não use "Mbps" nem "Gb".
  - Separador de milhar: um espaço ("10 000"). Separador decimal: a vírgula ("2,5 s"). Não use o ponto como separador de milhar.
- **Exemplos:** Tempo: ms, s, min, h, dia útil, fuso horário, deslocamento. Dados: bit, byte (B), kB, MB, GB, TB, KiB, MiB, GiB, kbit/s, Mbit/s, Gbit/s, prefixo decimal, prefixo binário. Outras: GHz, %, vCPU.
- **PTS-BR:** Defina o limite de memória do contêiner como 512 MiB. O link tem 1 Gbit/s.

### NT-23 Normas, leis e documentos de referência

- **Definição:** O nome de uma lei, de uma norma técnica ou de um documento de referência externo.
- **Regra de uso:** Escreva o nome oficial e o número. Use o artigo do núcleo em português: "a LGPD" (lei), "a ISO/IEC 27001" (norma), "a RFC 9110" (especificação).
- **Exemplos:** LGPD, ISO/IEC 27001, ABNT NBR ISO/IEC 25010, RFC 9110, OWASP Top 10, PCI DSS.
- **Nomes da lei:** Os nomes que uma lei define são literais da lei. Na LGPD, "operador", "controlador" e "titular" têm o significado da lei, não o significado de [NT-19](#nt-19-papéis-de-pessoas-em-processos). Escreva a lei na primeira ocorrência: "o operador (LGPD)", "o titular (LGPD)".
- **PTS-BR:** Este procedimento segue a ISO/IEC 27001, controle A.8.13.

### NT-24 Valores de estado do sistema

- **Definição:** Um valor que o sistema mostra para indicar o estado de um item.
- **Regra de uso:** Em prosa, escreva "estado", não "status" (seção 5.5). O valor de estado é um literal. Copie o valor como o sistema mostra, com o formato da origem ([R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor)):
  - Valor de uma CLI, de uma API ou de um log: formato de código (`Running`).
  - Rótulo da interface: negrito (**Ativo**).

  Se o valor estiver em inglês, escreva o significado em português na mesma frase ou na próxima.
- **Exemplos:** `Running`, `Pending`, `CrashLoopBackOff`, **Ativo**, **Concluído**.
- **PTS-BR:** O pod está no estado `Pending`. O pod aguarda um nó com recursos livres. Na página **Pedidos**, o pedido está no estado **Concluído**.

### NT-25 Termos de linguagem e de redação

- **Definição:** Um nome que um texto sobre a escrita usa para descrever outro texto. Exemplos: as partes de um texto, as classes de palavras, as formas verbais e os sinais de pontuação.
- **Regra de uso:** Use estes nomes apenas em texto sobre a escrita: esta especificação, os materiais de treinamento, um guia de estilo ou um comentário de revisão. A lista de metalinguagem de 01-introducao.md, seção 11.2, tem o mesmo escopo. Uma palavra de exemplo dentro do texto é uma menção: escreva a palavra entre aspas ou em formato de código.
- **Exemplos:**
  - Partes do texto: palavra, frase, oração, oração subordinada, parágrafo, título, legenda, sumário, introdução, prosa, texto descritivo, redação, lista numerada, sublista.
  - Classes de palavras: substantivo, adjetivo, advérbio, artigo, preposição, conjunção, pronome, numeral, locução, classe gramatical, locução adverbial, locução prepositiva.
  - Pronomes e partes da frase: pronome relativo, pronome indefinido, pronome demonstrativo, pronome oblíquo, pronome átono, sujeito, sujeito indeterminado, complemento, núcleo, cadeia nominal.
  - Verbos: verbo, verbo auxiliar, verbo-suporte, verbo técnico, verbo pronominal, forma verbal, conjugação, terminação.
  - Vozes e modos: voz ativa, voz passiva, voz passiva sintética, imperativo, indicativo, subjuntivo.
  - Formas nominais e tempos: infinitivo, infinitivo flexionado, gerúndio, gerundismo, particípio, presente, pretérito perfeito, pretérito imperfeito, futuro, futuro do pretérito.
  - Posição do pronome: próclise, ênclise, mesóclise.
  - Forma das palavras: forma, singular, plural, masculino, feminino, gênero, forma flexionada, radical, prefixo, contração, palavra derivada, forma aportuguesada, grafia, sigla, abreviatura.
  - Letras e números: letra, maiúscula, minúscula, algarismo, acento, crase, separador de milhar, separador decimal.
  - Sinais: vírgula, ponto, ponto e vírgula, dois-pontos, aspas, aspas duplas, parênteses, colchetes, travessão, hífen, sinal de pontuação.
  - Pontos e formatos: ponto de exclamação, ponto de interrogação, negrito, itálico.
  - Significado: significado, sinônimo, homógrafo, termo, termo composto, definição, categoria, conceito, vocabulário, gíria, estrangeirismo, metalinguagem, menção, literal.
  - Nomes do PTS-BR: nome técnico, palavra de sinalização, princípio, fronteira de significado, texto normativo.
  - Documentos e ferramentas: glossário, glossário-base, glossário do projeto, dicionário, entrada do dicionário, ordem alfabética, especificação, guia de estilo, linter.
  - Língua e pessoas: língua, português, inglês, espanhol, gramática, tradução, tradutor, redator, leitor.
- **PTS-BR:** Escreva o verbo do passo no imperativo. Use a vírgula depois de uma condição no início da frase.

---

## 4. Verbos técnicos

### 4.1 Regras

**VT1. Use o verbo técnico apenas com o significado da tabela.** Para outro significado, use o verbo do dicionário que a coluna "Uso não técnico" indica.

**VT2. Use o verbo técnico com os objetos da categoria.** "Compile o código" é aprovado. "Compile os resultados" não é aprovado.

**VT3. Use as mesmas formas verbais do dicionário.** Imperativo em procedimentos. Presente, pretérito perfeito e "vai" + infinitivo em texto descritivo. Em uma condição, use a forma que a regra [R3.2](02-regras.md#r32-use-o-subjuntivo-apenas-em-condições-com-se-ou-quando-revisor) define para o tipo de condição (01-introducao.md, seção 5.2).

**VT4. Não use verbo com radical estrangeiro ([R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale)).** Use, nesta ordem:

1. Um verbo técnico desta seção: "Mescle o branch".
2. Um verbo do dicionário com o nome técnico: "Crie um commit", "Execute o deploy".
3. FAZER com o nome técnico, apenas se nenhum outro verbo tiver o significado correto: "Faça o rebase do branch".

**VT5. Um verbo técnico não aprova a palavra derivada.** Use a palavra derivada apenas se o glossário-base listar o substantivo: "a migração", "a autenticação" e "a criptografia" estão no glossário.

**VT6. A lista é fechada.** Para adicionar um verbo técnico à lista, envie um PMD (05-governanca.md, seção 7).

### 4.2 Lista de verbos técnicos

#### A. Interface do usuário

Estes verbos seguem a regra [R10.2](02-regras.md#r102-use-o-verbo-do-tipo-de-elemento-revisor). MARCAR, ATIVAR, DESATIVAR e PRESSIONAR também são verbos de interface, mas estão no dicionário geral.

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| CLICAR | Pressionar o botão do mouse em um botão, em um link, em um ícone ou em uma guia da tela. | Clique em **Salvar**. | — |
| TOCAR | Fazer a ação de CLICAR em uma tela de toque. | Toque em **Aprovar**. | Toque no assunto na reunião. (Use: Informe o assunto na reunião.) |
| SELECIONAR | Escolher um item em uma lista, em um menu ou em um grupo de botões de opção. | Selecione **Configurações** > **Segurança**. | Selecione a melhor opção para o cliente. (Use: Escolha a melhor opção para o cliente.) |
| DESMARCAR | Remover a marca de uma caixa de seleção. | Desmarque a caixa **Lembrar de mim**. | — |
| DIGITAR | Escrever um texto com o teclado em um campo ou em um terminal. | Digite o nome do projeto no campo **Nome**. | — |
| COLAR | Colocar em um campo, em um arquivo ou em um terminal o texto que você copiou antes. | Copie o token e cole o token no campo **Token**. | — |
| ARRASTAR | Mover um item na tela com o mouse, sem soltar o botão, ou em uma tela de toque. | Arraste o arquivo para a área **Anexos**. | — |
| ROLAR | Mover o conteúdo de uma janela para mostrar outra parte do conteúdo. | Role a página até a seção **Tokens**. | — |
| EXPANDIR | Mostrar o conteúdo de um item que está recolhido. | Expanda a seção **Avançado**. | Expanda o time. (Use: Adicione pessoas à equipe.) |
| RECOLHER | Ocultar o conteúdo de um item que está expandido. | Recolha a barra lateral. | Recolha os logs. (Use: Colete os logs.) |
| CAPTURAR | Gerar uma imagem da tela ou de uma parte da tela. | Capture a tela com a mensagem de erro. | Capture os requisitos. (Use: Identifique os requisitos.) |

#### B. Arquivos e dados

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| SALVAR | Gravar no armazenamento as alterações de um arquivo, de um documento ou de um formulário, por uma ação do usuário. GRAVAR (03) é a ação do sistema. | Salve o arquivo e feche o editor. | O backup salvou o projeto. (Use: A equipe recuperou o projeto com o backup.) |
| EDITAR | Alterar o conteúdo de um arquivo ou de um campo com um editor ou com um formulário. | Edite o arquivo `config.yaml`. | Edite o processo de aprovação. (Use: Altere o processo de aprovação.) |
| BAIXAR | Transferir um arquivo de um servidor remoto para o computador local. | Baixe o instalador na página de versões. | Baixe o limite para 10. (Use: Diminua o limite para 10.) |
| SOBRESCREVER | Gravar dados novos no lugar de dados que já existem. | O comando sobrescreve o arquivo de destino. | — |
| COMPACTAR | Diminuir o tamanho de um ou mais arquivos com um formato como o ZIP. | Compacte a pasta de logs em um arquivo ZIP. | Compacte o texto. (Use: Escreva um texto mais curto.) |
| DESCOMPACTAR | Gerar de novo os arquivos originais de um arquivo compactado. | Descompacte o arquivo `release.tar.gz`. | — |
| IMPORTAR | Colocar em um sistema dados que estão em um arquivo ou em outro sistema. | Importe os usuários do arquivo CSV. | Este erro não importa. (Use: Este erro não afeta o resultado.) |
| EXPORTAR | Gravar dados de um sistema em um arquivo ou em outro sistema. | Exporte o relatório em formato PDF. | — |
| SINCRONIZAR | Fazer 2 ou mais sistemas ou pastas terem os mesmos dados. | Sincronize a pasta local com o bucket. | Sincronize com a equipe. (Use: Informe a equipe.) |

#### C. Banco de dados

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| CONSULTAR | Obter dados de um banco de dados ou de uma API com uma consulta. | Consulte a tabela `pedidos` para obter os pedidos de 2026-11-18. | Consulte a documentação. (Use: Leia a documentação.) |
| INDEXAR | Criar um índice para os dados de uma tabela ou de um conjunto de documentos. | Indexe a coluna `email` da tabela `usuarios`. | — |
| MIGRAR | Mover dados, um esquema ou um sistema para outra versão, outro formato ou outra plataforma. | Migre o banco para o PostgreSQL 16. | O analista migrou para a equipe de dados. (Use: O analista foi para a equipe de dados.) |
| REPLICAR | Copiar dados de um servidor para outro servidor, de forma contínua. | A réplica primária replica os dados para 2 réplicas secundárias. | Replique o e-mail para a equipe. (Use: Encaminhe o e-mail à equipe.) |
| TRUNCAR | Excluir todas as linhas de uma tabela do banco, sem excluir a tabela. | Trunque a tabela `sessoes_temporarias`. | — |
| PARTICIONAR | Dividir uma tabela ou um disco em partes que o sistema gerencia de forma separada. | Particione a tabela `eventos` por mês. | Particione o trabalho entre as equipes. (Use: Divida o trabalho entre as equipes.) |

#### D. Programação

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| COMPILAR | Converter código-fonte em código que um computador executa. | Compile o projeto com o comando `mvn package`. | Compile os resultados em um relatório. (Use: Junte os resultados em um relatório.) |
| DEPURAR | Executar o código passo a passo para encontrar a causa de um defeito. | Depure a função `calcular_frete()`. | — |
| IMPLEMENTAR | Escrever o código que faz um requisito, uma interface ou uma funcionalidade funcionar. | Implemente a interface `Pagamento`. | Implemente o processo novo de plantão. (Use: Comece a usar o processo novo de plantão.) |
| INICIALIZAR | Dar o primeiro valor a uma variável ou preparar um componente para o primeiro uso. | Inicialize a variável `contador` com `0`. | Inicialize o servidor. (Use: Ligue o servidor.) |
| INSTANCIAR | Criar um objeto a partir de uma classe. | Instancie a classe `Cliente` com o ID do usuário. | — |
| DECLARAR | Escrever no código o nome e o tipo de uma variável, de uma função ou de uma classe. | Declare a variável `total` como `int`. | Declare o incidente. (Use: Registre o incidente.) |
| CHAMAR | Fazer um código executar uma função, um método ou um endpoint. | A função chama o endpoint `/v1/estoque`. | Chame o gerente de incidente. (Use: Envie uma mensagem ao gerente de incidente.) |
| PASSAR | Fornecer um argumento a uma função, a um método, a um comando ou a um endpoint, no momento da chamada. | Passe o argumento `timeout` para a função `conectar()`. | Todos os testes passaram. (Use: Todos os testes tiveram sucesso.) / O uso de CPU passou de 90%. (Use: O consumo de CPU é maior que 90%.) / Passe o arquivo para a equipe. (Use: Envie o arquivo para a equipe.) |
| RETORNAR | Enviar um valor ou um código como resultado de uma função, de um comando ou de uma requisição. | O comando retorna o código `0` quando a operação tem sucesso. | Retorne o contato do cliente. (Use: Responda ao cliente.) |
| LANÇAR | Gerar uma exceção no código. | O método lança a exceção `TimeoutError`. | Lance a versão 3. (Use: Publique a versão 3.) |
| TRATAR | Escrever o código que responde a uma exceção ou a um erro. | Trate a exceção `TimeoutError` na aplicação cliente. | Este capítulo trata de segurança. (Use: Esta seção é sobre segurança.) |
| VALIDAR | Verificar de forma automática, com regras definidas, se um dado, um arquivo ou um certificado é válido. | O script valida o arquivo com o esquema JSON. | Valide a ideia com o cliente. (Use: Mostre a ideia ao cliente e peça a aprovação.) |
| REFATORAR | Alterar a estrutura do código sem alterar o comportamento. | Refatore a classe `Pedido` antes de adicionar o campo novo. | — |
| FORMATAR | Aplicar a um código, a um texto ou a um disco um formato padrão definido. | Formate o código com o Prettier. | — |
| SERIALIZAR | Converter um objeto em uma sequência de bytes ou de texto para armazenar ou enviar o objeto. | O serviço serializa o pedido em JSON. | — |
| DESSERIALIZAR | Converter uma sequência de bytes ou de texto em um objeto. | A aplicação cliente desserializa a resposta. | — |

#### E. Controle de versão

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| CLONAR | Criar uma cópia local de um repositório remoto. | Clone o repositório com o comando `git clone`. | Clone a configuração do servidor A. (Use: Copie a configuração do servidor A.) |
| MESCLAR | Juntar as alterações de um branch em outro branch. | Mescle o branch `feature/login` no branch `main`. | Mescle as duas planilhas. (Use: Junte os 2 arquivos.) |
| REVERTER | Voltar o código, uma configuração ou um deploy à versão anterior. | Reverta o deploy para a versão 2.3.0. | Reverta a situação com o cliente. (Use: Resolva o problema com o cliente.) |

As operações abaixo não têm verbo técnico. Use a forma da coluna "PTS-BR".

| Operação (comando) | PTS-BR |
|---|---|
| commit (`git commit`) | Crie um commit. |
| `push` (`git push`) | Envie os commits para o repositório remoto. |
| `pull` (`git pull`) | Atualize o branch local com o comando `git pull`. |
| `fetch` (`git fetch`) | Obtenha as alterações do repositório remoto com o comando `git fetch`. |
| `checkout` ou `switch` (`git switch`) | Execute o comando `git switch main` para usar o branch `main`. |
| `cherry-pick` (`git cherry-pick`) | Aplique o commit `a1b2c3d` no branch `main`. |
| rebase (`git rebase`) | Faça o rebase do branch `feature/login` no branch `main`. |
| tag (`git tag`) | Crie a tag `v2.4.0`. |
| fork | Crie um fork do repositório. |
| `stash` (`git stash`) | Execute o comando `git stash` para armazenar as alterações locais sem commit. |

#### F. Deploy e operação

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| PROVISIONAR | Criar e configurar a infraestrutura que um sistema precisa. | Provisione o cluster com o Terraform. | Provisione o material da reunião. (Use: Prepare os documentos da reunião.) |
| ESCALAR | Aumentar ou diminuir a capacidade de um sistema com mais ou menos recursos. | Escale o objeto `Deployment` `api` para 6 réplicas. | Escale o incidente para o nível 2. (Use: Encaminhe o incidente para o nível 2.) |
| HOSPEDAR | Executar um sistema ou armazenar um site em um servidor ou em um provedor de nuvem. | A empresa hospeda a API em 2 data centers. | — |
| DESINSTALAR | Remover um programa de um sistema e os arquivos que a instalação criou. | Desinstale a versão antiga do agente. | — |
| BALANCEAR | Distribuir requisições ou carga entre 2 ou mais servidores. | O balanceador de carga balanceia o tráfego entre 3 nós. | — |
| DRENAR | Mover as cargas de trabalho de um nó para outros nós e impedir cargas novas no nó, antes de uma manutenção. | Drene o nó 3 com o comando `kubectl drain`. | Drene a fila de chamados. (Use: Resolva os chamados da fila.) |

O deploy não tem verbo técnico. Use "executar o deploy" (01-introducao.md, seção 5.4). Para o rollback, use REVERTER.

> PTS-BR: Execute o deploy da versão 2.4.0. Se a verificação de integridade falhar, reverta o deploy.

#### G. Rede

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| ROTEAR | Escolher o caminho de um pacote de rede ou de uma requisição até o destino. | O gateway roteia as requisições de `/v1` para o serviço `pedidos-v1`. | — |
| REDIRECIONAR | Enviar uma requisição, um tráfego ou uma saída para outro destino de forma automática. | O servidor redireciona o HTTP para o HTTPS. | — |
| MAPEAR | Associar um item de um sistema a um item de outro sistema, por exemplo uma porta a outra porta. | Mapeie a porta 8080 do contêiner para a porta 80 do host. | Mapeie os riscos do projeto. (Use: Identifique os riscos do projeto.) |

#### H. Segurança

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| AUTENTICAR | Verificar a identidade de uma pessoa ou de um sistema. | O gateway autentica cada requisição com o token. | — |
| AUTORIZAR | Dar a uma identidade autenticada a permissão para uma ação. | A política autoriza o grupo `devops` a ler os segredos. | O gerente autorizou a compra. (Use: O gerente aprovou a compra.) |
| CRIPTOGRAFAR | Converter dados com uma chave para impedir a leitura sem a chave. | Criptografe o backup com AES-256. | — |
| DESCRIPTOGRAFAR | Converter dados criptografados de novo para a forma original, com a chave. | O serviço descriptografa o arquivo na memória. | — |
| ASSINAR | Gerar uma assinatura digital para um arquivo, um commit ou uma mensagem. | Assine os commits com a sua chave SSH. | Assine o canal de alertas. (Use: Adicione o seu e-mail à lista de alertas.) |
| REVOGAR | Cancelar a validade de um token, de uma chave, de um certificado ou de uma permissão antes do fim da validade. | Se a chave de API estiver em um repositório público, revogue a chave imediatamente. | — |
| EXPIRAR | Chegar ao fim do período de validade. Para um token, uma senha, um certificado ou uma sessão. | O token expira em 1 h. | O prazo do projeto expirou. (Use: O prazo do projeto terminou.) |
| ROTACIONAR | Substituir uma credencial ou um arquivo de log por um item novo, em intervalos definidos. | Rotacione as chaves de acesso a cada 90 dias. | Rotacione o plantão. (Use: Altere a ordem do plantão.) |
| AUDITAR | Analisar registros e configurações para verificar se um sistema segue uma norma ou uma política. | Audite os acessos ao banco de produção 1 vez por mês. | — |
| MASCARAR | Substituir parte de um dado por caracteres fixos para ocultar o dado. | Mascare o CPF nos logs: `***.***.***-12`. | — |
| ANONIMIZAR | Alterar dados pessoais. Depois da alteração, ninguém pode identificar a pessoa com os dados. | Anonimize os dados antes da cópia para o ambiente de teste. | — |
| ISOLAR | Separar um sistema da rede ou de outros sistemas para impedir que um ataque ou uma falha afete outros sistemas. | Isole da rede o servidor que o ataque acessou. | — |

#### I. Testes e qualidade

Para o resultado de um teste, use FALHAR (03) ou SUCESSO (03): "Todos os testes tiveram sucesso.", "O teste 3 falhou." PASSAR é um verbo de programação (seção 4.2.D).

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| HOMOLOGAR | Testar e aprovar uma versão no ambiente de homologação antes da produção. | A equipe de QA homologa a versão 2.4.0. | — |

#### J. Observabilidade

| Verbo | Significado técnico | Exemplo PTS-BR | Uso não técnico |
|---|---|---|---|
| INSTRUMENTAR | Adicionar ao código as chamadas de função que geram métricas, logs ou rastros. | Instrumente o serviço com o SDK do OpenTelemetry. | — |
| RASTREAR | Registrar o caminho de uma requisição entre os serviços de um sistema. | O sistema rastreia cada requisição com um ID. | Rastreie o pedido do cliente. (Use: Procure o pedido do cliente.) |

---

## 5. Política de estrangeirismos

### 5.1 Princípio

O PTS-BR aceita uma palavra estrangeira apenas como nome técnico da lista da seção 5.5 e com o gênero da lista. A seção 5.4 de 01-introducao.md e a regra [R1.7](02-regras.md#r17-use-estrangeirismos-apenas-da-lista-de-termos-técnicos-vale) têm a mesma decisão. Um literal (código, rótulo, mensagem, nome de produto) não é um estrangeirismo do texto: copie o literal sem alteração.

### 5.2 Critérios de decisão

Aplique os critérios nesta ordem. O primeiro critério que se aplica ao termo define a decisão.

| Critério | Condição | Decisão |
|---|---|---|
| E1 | O termo é um literal: um comando, um rótulo de interface, um nome de produto, uma mensagem ou um valor do sistema? | Copie o literal sem alteração, com o formato da [R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor). A lista não se aplica. |
| E2 | O termo é um verbo, um adjetivo ou um advérbio? | Não aprovado. Use um verbo técnico (seção 4) ou uma palavra do dicionário. Exemplos: "deprecated" (use OBSOLETO), "hardcoded" (use "fixo no código"). |
| E3 | Existe um termo em português com o mesmo significado e com uso estável em TI? | Use o termo em português (decisão **Português**). |
| E4 | Não existe um termo em português com uso estável? | Mantenha o termo em inglês como nome técnico (decisão **Manter**). |
| E5 | Existe um termo em português com uso estável, mas o leitor conhece melhor o termo em inglês, ou o leitor conhece os 2 termos? | Use o termo preferido. Escreva o outro termo apenas uma vez, entre parênteses, na primeira ocorrência do documento (decisão **Ambos**). |

**Teste de uso estável (E3).** Um termo em português tem uso estável se as 2 condições forem verdadeiras:

1. O termo aparece com o mesmo significado em 1 ou mais destes lugares:
   - A interface em português do Brasil de uma ferramenta que o leitor usa.
   - Uma norma ABNT NBR ou a tradução oficial de uma norma ISO/IEC.
   - O glossário aprovado do projeto.
2. O leitor não lê o termo como outro termo de TI. Exemplo: "implantação" falha nesta condição, porque o leitor lê "implantação" como "implementação" (01-introducao.md, seção 5.4).

### 5.3 Grafia dos estrangeirismos aprovados

| Regra | Exemplo PTS-BR |
|---|---|
| Escreva o termo sem itálico e sem aspas ([R8.8](02-regras.md#r88-use-cada-formato-tipográfico-com-um-único-significado-revisor)). O itálico é apenas para a ocorrência que define um termo. | Crie um commit. |
| Escreva o termo em minúsculas. Escreva as siglas e os nomes próprios em maiúsculas. | o token, a API, o GitHub |
| No plural, use a forma do inglês. | os commits, os tokens, os "proxies" |
| Use o gênero da lista. Se o termo não estiver na lista, envie um PMD para adicionar o termo. Para uma sigla nova do glossário do projeto, use o gênero do núcleo da sigla em português. | a API (interface), o SLA (acordo) |
| Use a forma aportuguesada apenas se a lista indicar esta forma. | o contêiner |
| Escreva os termos compostos como na lista, com ou sem hífen. | o e-mail, o pull request, a feature flag |
| Escreva o artigo antes do termo. | Crie o pull request. |

### 5.4 Verbos com radical estrangeiro

**Decisão:** O PTS-BR não aprova nenhum verbo com radical estrangeiro. A decisão se aplica também a verbos que aparecem em dicionários gerais ou que a equipe usa todos os dias.

**Justificativa:**

1. A conjugação destes verbos não é estável. Os redatores escrevem "commito", "comito" e "commitamos" para o mesmo verbo.
2. O leitor não nativo não encontra estes verbos em um dicionário de português. Um programa de tradução automática também não traduz estes verbos de forma correta.
3. Estes verbos são gíria. A regra [R9.2](02-regras.md#r92-não-use-linguagem-figurada-gíria-nem-personificação-revisor) proíbe gíria.
4. Cada um destes verbos tem uma forma aprovada (VT4). A forma aprovada é um verbo técnico, ou um verbo do dicionário ou FAZER com o nome técnico.
5. Um linter verifica um critério simples ("nenhum verbo com radical estrangeiro") com menos erros que uma lista de exceções.

A coluna "Formas flexionadas não aprovadas" lista as formas que os redatores escrevem. O linter procura o infinitivo e estas formas (05-governanca.md, seção 6).

| Não aprovado | PTS-BR | Formas flexionadas não aprovadas |
|---|---|---|
| deployar, dar deploy, fazer o deploy | Execute o deploy. | deployo, deploya, deployam, deployei, deployou, deployaram, deploye, deployem, deployando, deployado |
| commitar, comitar, dar commit | Crie um commit. | commito, commita, commitam, commitei, commitou, commitaram, commite, commitem, commitando, commitado |
| mergear, dar merge, fazer o merge | Mescle o branch. | mergeio, mergeia, mergeiam, mergeei, mergeou, mergearam, mergeie, mergeiem, mergeando, mergeado |
| pushar, dar push | Envie os commits para o repositório remoto. | pusho, pusha, pusham, pushei, pushou, pusharam, pushe, pushem, pushando, pushado |
| pullar, dar pull | Atualize o branch local com o comando `git pull`. | pullo, pulla, pullam, pullei, pullou, pullaram, pulle, pullem, pullando, pullado |
| buildar | Gere o build. Compile o projeto. | buildo, builda, buildam, buildei, buildou, buildaram, builde, buildem, buildando, buildado |
| startar, dar start | Inicie o serviço. | starto, starta, startam, startei, startou, startaram, starte, startem, startando, startado |
| setar | Defina a variável. Configure o parâmetro. | seto, setam, setei, setou, setaram, setem, setando, setado |
| resetar, dar reset | Redefina a senha. Reinicie o roteador. | reseto, reseta, resetam, resetei, resetou, resetaram, resete, resetem, resetando, resetado |
| deletar | Exclua o arquivo. | deleto, deleta, deletam, deletei, deletou, deletaram, delete, deletem, deletando, deletado |
| logar | Entre no portal. O sistema registra o evento no log. | loga, logam, loguei, logou, logaram, logue, loguem, logando, logado |
| deslogar | Saia do portal. | deslogo, desloga, deslogam, desloguei, deslogou, deslogaram, deslogue, desloguem, deslogando, deslogado |
| printar | Capture a tela. O script mostra o valor na saída. | printo, printa, printam, printei, printou, printaram, printe, printem, printando, printado |
| debugar, debuggar | Depure o código. | debugo, debuga, debugam, debuguei, debugou, debugaram, debugue, debuguem, debugando, debugado |
| mockar | Simule o serviço com um mock. | mocko, mocka, mockam, mockei, mockou, mockaram, mocke, mockem, mockando, mockado |
| upar, dar upload | Envie o arquivo. | upo, upa, upam, upei, upou, uparam, upe, upem, upando, upado |
| dropar | Exclua a tabela do banco (comando `DROP TABLE`). | dropo, dropa, dropam, dropei, dropou, droparam, drope, dropem, dropando, dropado |
| checar, checkar | Verifique o estado do serviço. | checo, checa, checam, chequei, checou, checaram, cheque, chequem, checando, checado |
| linkar | Adicione o link do documento ao chamado. | linko, linka, linkam, linkei, linkou, linkaram, linke, linkem, linkando, linkado |
| forkar | Crie um fork do repositório. | forko, forka, forkam, forkei, forkou, forkaram, forke, forkem, forkando, forkado |
| rebasear | Faça o rebase do branch. | rebaseio, rebaseia, rebaseiam, rebaseei, rebaseou, rebasearam, rebaseie, rebaseiem, rebaseando, rebaseado |
| cachear | Armazene a resposta no cache. | cacheio, cacheia, cacheiam, cacheei, cacheou, cachearam, cacheie, cacheiem, cacheando, cacheado |
| pingar | Teste a conexão com o comando `ping`. | pingo, pinga, pingam, pinguei, pingou, pingaram, pingue, pinguem, pingando, pingado |
| customizar | Personalize o painel. | customizo, customiza, customizam, customizei, customizou, customizaram, customize, customizem, customizando, customizado |
| bootar | Ligue o servidor. Inicie o sistema operacional. | booto, boota, bootam, bootei, bootou, bootaram, boote, bootem, bootando, bootado |
| tunar | Ajuste os parâmetros do banco. | tuno, tuna, tunam, tunei, tunou, tunaram, tune, tunem, tunando, tunado |
| shippar | Publique a versão. | shippo, shippa, shippam, shippei, shippou, shipparam, shippe, shippem, shippando, shippado |
| rankear | Ordene os resultados. | rankeio, rankeia, rankeiam, rankeei, rankeou, rankearam, rankeie, rankeiem, rankeando, rankeado |
| plugar | Conecte o cabo. | plugo, pluga, plugam, pluguei, plugou, plugaram, plugue, pluguem, plugando, plugado |
| releasar | Publique a versão 2.4.0. | releaso, releasa, releasam, releasei, releasou, releasaram, release, releasem, releasando, releasado |
| stashar | Execute o comando `git stash`. | stasho, stasha, stasham, stashei, stashou, stasharam, stashe, stashem, stashando, stashado |
| tagear, taguear, taggear | Crie a tag `v2.4.0`. | tageio, tageia, tageiam, tageei, tageou, tagearam, tageie, tageiem, tageando, tageado |
| fetchar | Obtenha as alterações do repositório remoto com o comando `git fetch`. | fetcho, fetcha, fetcham, fetchei, fetchou, fetcharam, fetche, fetchem, fetchando, fetchado |
| squashar | Junte os commits do branch em 1 commit. | squasho, squasha, squasham, squashei, squashou, squasharam, squashe, squashem, squashando, squashado |
| rollbackar | Reverta o deploy. | rollbacko, rollbacka, rollbackam, rollbackei, rollbackou, rollbackaram, rollbacke, rollbackem, rollbackando, rollbackado |
| upgradear | Atualize o pacote para a versão 3.0. | upgradeio, upgradeia, upgradeiam, upgradeei, upgradeou, upgradearam, upgradeie, upgradeiem, upgradeando, upgradeado |
| downgradear | Instale a versão anterior do pacote. | downgradeio, downgradeia, downgradeiam, downgradeei, downgradeou, downgradearam, downgradeie, downgradeiem, downgradeando, downgradeado |
| parsear | Converta o texto em um objeto. | parseio, parseia, parseiam, parseei, parseou, parsearam, parseie, parseiem, parseando, parseado |
| dockerizar | Crie uma imagem de contêiner para a aplicação. | dockerizo, dockeriza, dockerizam, dockerizei, dockerizou, dockerizaram, dockerize, dockerizem, dockerizando, dockerizado |
| hardcodar | Escreva o valor fixo no código. | hardcodo, hardcoda, hardcodam, hardcodei, hardcodou, hardcodaram, hardcode, hardcodem, hardcodando, hardcodado |
| zipar | Compacte a pasta em um arquivo ZIP. | zipo, zipa, zipam, zipei, zipou, ziparam, zipe, zipem, zipando, zipado |
| trackear | Rastreie a requisição. Registre o evento. | trackeio, trackeia, trackeiam, trackeei, trackeou, trackearam, trackeie, trackeiem, trackeando, trackeado |
| bugar | O sistema tem um defeito. O sistema falha. | bugo, buga, bugam, buguei, bugou, bugaram, bugue, buguem, bugando, bugado |
| crashar | O processo para com um erro. | crasho, crasha, crasham, crashei, crashou, crasharam, crashe, crashem, crashando, crashado |
| atachar | Anexe o arquivo ao chamado. | atacho, atacha, atacham, atachei, atachou, atacharam, atache, atachem, atachando, atachado |
| syncar | Sincronize a pasta com o bucket. | synco, synca, syncam, synquei, syncou, syncaram, synque, synquem, syncando, syncado |

### 5.5 Lista de decisões

Legenda da coluna "Decisão": **Manter** = o PTS-BR aprova o termo em inglês como nome técnico. **Português** = use o termo em português. O termo em inglês é aprovado apenas como literal (E1). **Ambos** = use o termo preferido (em negrito). Escreva o outro termo uma vez, entre parênteses, na primeira ocorrência.

| Termo em inglês | Decisão | Forma no PTS-BR | Gênero | Critério | Nota |
|---|---|---|---|---|---|
| API | Manter | API | a | E4 | Núcleo "interface". "a API de pedidos". |
| argument | Português | argumento | o | E3 | Verbo: PASSAR ("Passe o argumento"). |
| array | Manter | array | o | E4 | "Vetor" tem outros significados fora da programação. |
| backend | Manter | backend | o | E4 | — |
| backlog | Manter | backlog | o | E4 | — |
| backup | Ambos | **backup**; cópia de segurança | o | E5 | Ação: "Faça um backup". |
| bandwidth | Português | largura de banda | a | E3 | — |
| bastion | Ambos | **host de administração**; bastion | o | E5 | O servidor que a equipe usa para executar os comandos que gerenciam a produção (seção 6.2). |
| body | Português | corpo | o | E3 | MDN em português: "corpo da requisição", "corpo da resposta". |
| branch | Manter | branch | o | E4 | "Ramo" não tem uso estável. |
| browser | Português | navegador | o | E3 | — |
| bucket | Manter | bucket | o | E4 | Nome do recurso nos provedores de nuvem. |
| bug | Português | defeito | o | E3 | "Bug" apenas como literal (tipo de issue no rastreador). |
| build | Manter | build | o | E4 | Ação: "Gere o build". "buildar" não é aprovado. |
| cache | Manter | cache | o | E4 | "cachear" não é aprovado. |
| changelog | Manter | changelog | o | E4 | Nome do arquivo [`CHANGELOG.md`](CHANGELOG.md). Para o leitor final, use "notas de versão". |
| chart | Manter | chart | o | E4 | Pacote do Helm: "o chart `loja-web`". |
| checklist | Ambos | **lista de verificação**; checklist | a | E5 | Os 2 termos têm uso estável. A especificação usa "lista de verificação". |
| cluster | Manter | cluster | o | E4 | — |
| commit | Manter | commit | o | E4 | Ação: "Crie um commit". |
| compliance | Português | conformidade | a | E3 | — |
| console | Manter | console | o | E4 | "o console da AWS". |
| container | Português | contêiner | o | E3 | "container" apenas em literais (`docker container ls`). |
| cookie | Manter | cookie | o | E4 | — |
| dashboard | Português | painel | o | E3 | Apenas a tela de métricas. Para a interface que gerencia um serviço, use "console" ou "portal". |
| data breach | Português | vazamento de dados | o | E3 | — |
| data center | Manter | data center | o | E4 | — |
| database | Português | banco de dados | o | E3 | — |
| dataset | Português | conjunto de dados | o | E3 | — |
| deadline | Português | prazo | o | E3 | — |
| debug | Português | depuração; verbo DEPURAR | a | E3 | "Debug" apenas como literal (modo **Debug**). |
| default | Português | padrão | o | E3 | 01-introducao.md, seção 5.4. |
| deploy | Manter | deploy | o | E4 | "Implantação" falha no teste de uso estável. Ação: "Execute o deploy". |
| design | Manter | design | o | E4 | O plano de uma interface que um designer cria: "o design da tela de login". |
| diff | Manter | diff | o | E4 | — |
| disaster recovery | Português | recuperação de desastre | a | E3 | — |
| download | Manter | download | o | E4 | Verbo: BAIXAR. |
| downtime | Português | indisponibilidade | a | E3 | — |
| driver | Manter | driver | o | E4 | — |
| dump | Manter | dump | o | E4 | "o dump de memória". |
| e-mail | Manter | e-mail | o | E4 | Com hífen. |
| endpoint | Manter | endpoint | o | E4 | — |
| exception | Português | exceção | a | E3 | Exceção de código ([NT-03](#nt-03-comandos-código-e-identificadores)). |
| failover | Manter | failover | o | E4 | — |
| feature | Português | funcionalidade | a | E3 | 01-introducao.md, seção 5.4. |
| feature flag | Manter | feature flag | a | E4 | — |
| feedback | Português | comentário | o | E3 | — |
| field | Português | campo | o | E3 | Campo de uma tela, de um formulário ou de um objeto JSON. |
| firewall | Manter | firewall | o | E4 | — |
| fork | Manter | fork | o | E4 | Ação: "Crie um fork". |
| framework | Manter | framework | o | E4 | — |
| frontend | Manter | frontend | o | E4 | — |
| gateway | Manter | gateway | o | E4 | — |
| hardware | Manter | hardware | o | E4 | — |
| hash | Manter | hash | o | E4 | — |
| header | Português | cabeçalho | o | E3 | "o cabeçalho `Authorization`". |
| health check | Português | verificação de integridade | a | E3 | — |
| host | Manter | host | o | E4 | Computador ligado a uma rede, com um nome ou um endereço IP: "a porta 80 do host", "o nome do host". Para o papel do computador que responde a requisições de um serviço, use "servidor". |
| hotfix | Manter | hotfix | o | E4 | — |
| issue | Manter | issue | a | E4 | "Item" não é específico. "Questão" não é aprovado (03). |
| issue tracker | Português | rastreador de issues | o | E3 | — |
| job | Manter | job | o | E4 | — |
| kernel | Manter | kernel | o | E4 | — |
| layout | Manter | layout | o | E4 | A posição dos elementos de interface em uma tela. |
| least privilege | Português | privilégio mínimo | o | E3 | — |
| link | Manter | link | o | E4 | — |
| linter | Manter | linter | o | E4 | — |
| load balancer | Português | balanceador de carga | o | E3 | — |
| log | Manter | log | o | E4 | Verbo: REGISTRAR (03). "logar" não é aprovado. |
| login | Manter | login | o | E4 | Ação: "Entre no portal" (ENTRAR, 03). |
| marketing | Manter | marketing | o | E4 | — |
| logout | Manter | logout | o | E4 | Ação: "Saia do portal" (SAIR, 03). |
| manifest | Português | manifesto | o | E3 | Kubernetes: "o manifesto `deployment.yaml`". |
| merge | Manter | merge | o | E4 | Verbo: MESCLAR. |
| mock | Manter | mock | o | E4 | "mockar" não é aprovado. Use SIMULAR (03). |
| namespace | Manter | namespace | o | E4 | — |
| node | Português | nó | o | E3 | Plural "nós", sempre depois de artigo, contração ou número (seção 1). |
| notebook | Manter | notebook | o | E4 | — |
| notification | Português | notificação | a | E3 | — |
| observability | Português | observabilidade | a | E3 | — |
| offline | Manter | offline | — | E4 | Adjetivo sem plural: "o modo offline", "o agente está offline". Para a conexão de um item, use DESCONECTAR: "O agente está desconectado do servidor." |
| on-call | Português | plantão | o | E3 | "o analista de plantão". |
| online | Manter | online | — | E4 | Adjetivo sem plural: "o usuário está online". Para a conexão de um item, use CONECTAR: "O agente está conectado ao servidor." |
| pagination | Português | paginação | a | E3 | — |
| password | Português | senha | a | E3 | — |
| patch | Manter | patch | o | E4 | — |
| payload | Manter | payload | o | E4 | Apenas o conteúdo de uma mensagem, de um evento ou de um webhook. Para uma requisição ou uma resposta HTTP, use "corpo" ("body"). |
| pendrive | Manter | pendrive | o | E4 | — |
| pipeline | Manter | pipeline | o | E4 | — |
| placeholder | Manter | placeholder | o | E4 | Apenas o texto de exemplo de um campo vazio da interface ([R10.9](02-regras.md#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor)). Para o texto entre `<` e `>` de um comando, use "espaço reservado" ([R8.9](02-regras.md#r89-escreva-espaços-reservados-em-um-formato-único-revisor)). |
| plugin | Manter | plugin | o | E4 | — |
| pod | Manter | pod | o | E4 | Kubernetes. |
| postmortem | Ambos | **análise pós-incidente**; postmortem | a | E5 | — |
| product manager | Português | gerente de produto | o | E3 | — |
| prompt | Manter | prompt | o | E4 | O texto que um programa mostra quando aguarda uma entrada do usuário. |
| proxy | Manter | proxy | o | E4 | Plural: "proxies". |
| pull request | Manter | pull request (PR) | o | E4 | No GitLab, "merge request" é um literal. |
| query | Português | consulta | a | E3 | Verbo: CONSULTAR. |
| query string | Português | parâmetro de consulta | o | E3 | "o parâmetro de consulta `pagina`". |
| queue | Português | fila | a | E3 | — |
| quota | Português | cota | a | E3 | — |
| rack | Manter | rack | o | E4 | — |
| rate limit | Português | limite de taxa | o | E3 | Console do Google Cloud em português. |
| rebase | Manter | rebase | o | E4 | Ação: "Faça o rebase". |
| refactoring | Português | refatoração | a | E3 | Verbo: REFATORAR. |
| registry | Manter | registry | o | E4 | Um registry contém repositórios de imagens: "o registry `ghcr.io`", "o repositório de imagens `org/loja-web`". A palavra "repositório" sem complemento é um repositório Git. Não traduza "registry" como "registro": REGISTRO (03) é o texto que documenta uma ação. |
| release | Português | versão | a | E3 | "release" apenas em literais (branch `release/2.4`). |
| release notes | Português | notas de versão | as | E3 | — |
| request | Português | requisição | a | E3 | 01-introducao.md, seção 5.4. |
| role | Português | papel de acesso | o | E3 | RBAC e IAM. Se a interface mostrar **Função**, o rótulo é um literal (E1). Não use "perfil de acesso". |
| rollback | Manter | rollback | o | E4 | Verbo: REVERTER. |
| root | Português | superusuário | o | E3 | "root" apenas como literal: "o usuário `root`". |
| root cause | Português | causa raiz | a | E3 | — |
| runbook | Manter | runbook | o | E4 | — |
| script | Manter | script | o | E4 | — |
| secret | Português | segredo | o | E3 | — |
| secrets manager | Português | cofre de segredos | o | E3 | O nome do produto é um literal ([NT-01](#nt-01-produtos-softwares-e-serviços-externos)): "o HashiCorp Vault". |
| serverless | Português | sem servidor | — | E3 | AWS em português: "computação sem servidor". "função sem servidor". |
| service account | Português | conta de serviço | a | E3 | Consoles do Google Cloud e do Azure em português. |
| setup | Português | configuração; instalação | a | E3 | 01-introducao.md, seção 5.4. |
| shell | Manter | shell | o | E4 | — |
| site | Manter | site | o | E4 | — |
| snapshot | Manter | snapshot | o | E4 | — |
| software | Manter | software | o | E4 | — |
| sprint | Manter | sprint | a | E4 | Feminino, como no Guia do Scrum em português. |
| staging | Português | homologação | a | E3 | "o ambiente de homologação". |
| stakeholder | Português | parte interessada | a | E3 | — |
| status | Português | estado | o | E3 | "Status" apenas em literais (campo **Status**, comando `systemctl status`) e nos nomes técnicos "código de status" e "página de status". |
| status code | Português | código de status | o | E3 | MDN em português. |
| string | Manter | string | a | E4 | Núcleo "cadeia de caracteres". |
| switch | Manter | switch | o | E4 | Equipamento de rede. |
| tag | Manter | tag | a | E4 | — |
| template | Português | modelo | o | E3 | — |
| thread | Manter | thread | a | E4 | — |
| throughput | Português | vazão | a | E3 | — |
| ticket | Português | chamado | o | E3 | — |
| timeout | Ambos | **tempo limite**; timeout | o | E5 | — |
| token | Manter | token | o | E4 | — |
| trace | Português | rastro | o | E3 | O verbo é RASTREAR. |
| troubleshooting | Português | solução de problemas | a | E3 | — |
| upload | Manter | upload | o | E4 | Verbo: ENVIAR (03). "upar" não é aprovado. |
| user | Português | usuário | o | E3 | — |
| webhook | Manter | webhook | o | E4 | — |
| workaround | Português | solução temporária | a | E3 | — |
| worker | Manter | worker | o | E4 | — |
| workflow | Manter | workflow | o | E4 | Arquivo de automação do GitHub Actions: "o workflow `docs-lint.yml`". Para um processo de trabalho, use PROCESSO (03). |

---

## 6. Glossário-base de TI

O glossário-base define os termos técnicos que todos os projetos usam. Use o termo com o gênero e com o significado da tabela. A coluna "Categoria" indica a categoria da seção 3.

### 6.1 Tabela de siglas de uso geral

O texto pode usar estas siglas sem o nome completo, também na primeira ocorrência (regra [R8.7](02-regras.md#r87-defina-as-siglas-na-primeira-ocorrência-revisor)). Use o gênero da tabela. As siglas do glossário-base (seção 6.2) também não precisam do nome completo: API, CI, DNS, IP, SLA, SLI, SLO, URL e VPN. Para uma sigla que não está nas 2 tabelas, aplique a regra T4.

| Sigla | Nome completo | Gênero | Categoria | Significado |
|---|---|---|---|---|
| ACL | Access Control List | a | [NT-16](#nt-16-segurança-e-identidade) | Lista de controle de acesso. |
| AD | Active Directory | o | [NT-16](#nt-16-segurança-e-identidade) | Serviço da Microsoft que armazena e autentica as contas, os grupos e os computadores de uma organização. |
| ADR | Architecture Decision Record | o | [NT-20](#nt-20-artefatos-de-processo) | Documento de uma decisão de arquitetura. |
| CD | Continuous Delivery | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Entrega contínua: prática que prepara cada versão para o deploy de forma automática. |
| CDN | Content Delivery Network | a | [NT-13](#nt-13-recursos-de-nuvem) | Rede de servidores que envia o conteúdo da web de um servidor na região do usuário. |
| CIDR | Classless Inter-Domain Routing | o | [NT-14](#nt-14-rede-e-endereços) | Formato de uma faixa de endereços IP, por exemplo `10.0.0.0/16`. |
| CLDR | Common Locale Data Repository | o | [NT-23](#nt-23-normas-leis-e-documentos-de-referência) | Banco de dados público com as regras de cada língua e de cada país: plural, datas, números e moedas. O ICU e o i18next usam o CLDR. |
| CLI | Command-Line Interface | a | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Interface de linha de comando de um programa. |
| CNPJ | Cadastro Nacional da Pessoa Jurídica | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Número que identifica uma empresa no Brasil. |
| CORS | Cross-Origin Resource Sharing | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Regra do navegador que controla as requisições entre domínios diferentes. |
| CPF | Cadastro de Pessoas Físicas | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Número que identifica uma pessoa no Brasil. |
| CPU | Central Processing Unit | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Processador central de um computador. |
| CSR | Certificate Signing Request | o | [NT-16](#nt-16-segurança-e-identidade) | Pedido de certificado: arquivo com a chave pública que um servidor envia a uma autoridade certificadora. |
| CSV | Comma-Separated Values | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato de texto com valores separados por vírgula. |
| CVE | Common Vulnerabilities and Exposures | a | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Identificador público de uma vulnerabilidade. |
| CVSS | Common Vulnerability Scoring System | o | [NT-16](#nt-16-segurança-e-identidade) | Padrão que dá um valor de 0 a 10 a uma vulnerabilidade, pelo risco da vulnerabilidade. |
| DDoS | Distributed Denial of Service | o | [NT-16](#nt-16-segurança-e-identidade) | Ataque que envia requisições de 2 ou mais computadores ao mesmo tempo para fazer um serviço ficar indisponível. |
| DHCP | Dynamic Host Configuration Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo que dá um endereço IP e uma configuração de rede a cada equipamento de uma rede. |
| EDR | Endpoint Detection and Response | o | [NT-16](#nt-16-segurança-e-identidade) | Software que monitora os computadores de uma empresa para detectar ataques e responder aos ataques. |
| GPU | Graphics Processing Unit | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Processador gráfico. |
| HPA | Horizontal Pod Autoscaler | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Objeto do Kubernetes que altera o número de réplicas de um objeto `Deployment` pelo consumo de CPU ou por outra métrica. |
| HTML | HyperText Markup Language | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato das páginas web. |
| HTTP | Hypertext Transfer Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de transferência de dados da web. |
| HTTPS | HTTP Secure | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | HTTP com criptografia TLS. |
| IAM | Identity and Access Management | o | [NT-16](#nt-16-segurança-e-identidade) | Controle das identidades e dos acessos. |
| ICU | International Components for Unicode | a | [NT-11](#nt-11-linguagens-frameworks-e-bibliotecas) | Biblioteca que formata textos, datas, números e plurais de acordo com as regras do CLDR. |
| ID | Identifier | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Identificador: valor que identifica um item. |
| IdP | Identity Provider | o | [NT-16](#nt-16-segurança-e-identidade) | Provedor de identidade: sistema que autentica os usuários para outros sistemas. |
| IOPS | Input/Output Operations Per Second | as | [NT-22](#nt-22-unidades-de-medida) | Operações de leitura e de escrita em disco por segundo. |
| ISO | International Organization for Standardization | a | [NT-23](#nt-23-normas-leis-e-documentos-de-referência) | Organização que publica as normas ISO. |
| JSON | JavaScript Object Notation | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato de texto para objetos de dados. |
| JWT | JSON Web Token | o | [NT-16](#nt-16-segurança-e-identidade) | Formato de token assinado. |
| KMS | Key Management Service | o | [NT-16](#nt-16-segurança-e-identidade) | Serviço que cria, armazena e controla as chaves de criptografia. |
| LAN | Local Area Network | a | [NT-14](#nt-14-rede-e-endereços) | Rede local: a rede dos equipamentos de um lugar, por exemplo de um data center. |
| LDAP | Lightweight Directory Access Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo que consulta e altera as contas e os grupos de um serviço de identidade, por exemplo do AD. |
| LGPD | Lei Geral de Proteção de Dados Pessoais | a | [NT-23](#nt-23-normas-leis-e-documentos-de-referência) | Lei brasileira sobre os dados pessoais. |
| MFA | Multi-Factor Authentication | a | [NT-16](#nt-16-segurança-e-identidade) | Autenticação multifator (seção 6.2). |
| MTTR | Mean Time to Recovery | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Tempo médio de recuperação de um serviço depois de um incidente. |
| NAT | Network Address Translation | o | [NT-14](#nt-14-rede-e-endereços) | Tradução de endereços de rede. |
| NTP | Network Time Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo que sincroniza o relógio dos computadores de uma rede. |
| OIDC | OpenID Connect | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de autenticação sobre o OAuth 2.0: um IdP confirma a identidade do usuário para uma aplicação. |
| OTP | One-Time Password | a | [NT-16](#nt-16-segurança-e-identidade) | Senha de uso único: a senha funciona apenas 1 vez. |
| PDF | Portable Document Format | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato de documento que mostra o mesmo conteúdo em qualquer sistema. |
| PID | Process Identifier | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Número que identifica um processo no sistema operacional. |
| PITR | Point-in-Time Recovery | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Recuperação até um ponto no tempo (seção 6.2). |
| PKI | Public Key Infrastructure | a | [NT-16](#nt-16-segurança-e-identidade) | Infraestrutura de chave pública: as autoridades certificadoras, os certificados e as regras que criam e verificam os certificados de uma organização. |
| PNG | Portable Network Graphics | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato de imagem. |
| PR | Pull Request | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Forma curta de "pull request". |
| QA | Quality Assurance | a | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | A equipe ou a atividade que testa uma versão antes do deploy. |
| RAID | Redundant Array of Independent Disks | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Grupo de discos que o sistema usa como 1 disco, com cópias dos dados, para continuar a funcionar depois da falha de 1 disco. |
| RAM | Random Access Memory | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Memória do computador. Em prosa, use "memória" (seção 6.2). |
| RBAC | Role-Based Access Control | o | [NT-16](#nt-16-segurança-e-identidade) | Controle de acesso com papéis de acesso. |
| REST | Representational State Transfer | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Estilo de API que usa os métodos do HTTP com recursos que têm uma URL própria. |
| RPO | Recovery Point Objective | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Objetivo de ponto de recuperação: a perda máxima de dados que a empresa aceita, medida em tempo. |
| RTO | Recovery Time Objective | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Objetivo de tempo de recuperação: o tempo máximo para o serviço funcionar de novo. |
| SAML | Security Assertion Markup Language | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Padrão de login único em XML: um IdP envia a uma aplicação uma mensagem que confirma a identidade do usuário. |
| SBOM | Software Bill of Materials | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Lista dos componentes de um software, com a versão de cada componente. |
| SDK | Software Development Kit | o | [NT-11](#nt-11-linguagens-frameworks-e-bibliotecas) | Conjunto de bibliotecas e de ferramentas para usar uma plataforma ou uma API. |
| SFTP | SSH File Transfer Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de transferência de arquivos com SSH. |
| SIEM | Security Information and Event Management | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Sistema que coleta e analisa os logs de segurança de uma empresa para detectar ataques. |
| SMTP | Simple Mail Transfer Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de envio de e-mail. |
| SOC | Security Operations Center | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Equipe que monitora os eventos de segurança e que responde aos incidentes de segurança. |
| SQL | Structured Query Language | o | [NT-11](#nt-11-linguagens-frameworks-e-bibliotecas) | Linguagem de consulta de bancos de dados. |
| SRE | Site Reliability Engineering | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | A equipe ou a prática que mantém os serviços em produção com metas de disponibilidade. |
| SSD | Solid-State Drive | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Tipo de disco rápido. |
| SSH | Secure Shell | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de acesso remoto com criptografia. |
| SSO | Single Sign-On | o | [NT-16](#nt-16-segurança-e-identidade) | Login único: um login dá acesso a vários sistemas. |
| TCP | Transmission Control Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de rede que cria uma conexão e que confirma cada pacote de rede que o destino recebe. |
| TI | Tecnologia da informação | a | — | A área de uma empresa que mantém os sistemas e os computadores. |
| TLS | Transport Layer Security | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de criptografia das conexões de rede. |
| TOTP | Time-based One-Time Password | a | [NT-16](#nt-16-segurança-e-identidade) | OTP que um programa de autenticação gera a cada 30 s, por exemplo para a MFA. |
| TTL | Time To Live | o | [NT-14](#nt-14-rede-e-endereços) | Tempo máximo em que um registro DNS ou um item de cache é válido. |
| UDP | User Datagram Protocol | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Protocolo de rede sem conexão que não confirma os pacotes de rede. |
| UI | User Interface | a | [NT-05](#nt-05-elementos-de-interface) | Interface do usuário. |
| USB | Universal Serial Bus | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Padrão de conexão de equipamentos. |
| UTC | Coordinated Universal Time | o | [NT-22](#nt-22-unidades-de-medida) | Hora de referência de todos os fusos horários. |
| UUID | Universally Unique Identifier | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Identificador de 128 bits, por exemplo `550e8400-e29b-41d4-a716-446655440000`. |
| vCPU | Virtual CPU | a | [NT-22](#nt-22-unidades-de-medida) | CPU virtual de uma máquina virtual ou de um contêiner. |
| VLAN | Virtual LAN | a | [NT-14](#nt-14-rede-e-endereços) | Rede local virtual: parte de uma rede física que funciona como uma rede separada. |
| VM | Virtual Machine | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Máquina virtual. |
| VPC | Virtual Private Cloud | a | [NT-13](#nt-13-recursos-de-nuvem) | Rede privada virtual em um provedor de nuvem. |
| WAF | Web Application Firewall | o | [NT-14](#nt-14-rede-e-endereços) | Firewall que analisa as requisições HTTP e bloqueia os ataques a uma aplicação web. |
| WAL | Write-Ahead Log | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Log em que o banco de dados grava cada alteração antes de alterar os arquivos de dados. A PITR usa o WAL. |
| WAN | Wide Area Network | a | [NT-14](#nt-14-rede-e-endereços) | Rede que conecta as redes de lugares diferentes, por exemplo os data centers de uma empresa. |
| XML | Extensible Markup Language | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato de texto em que um nome marca o início e o fim de cada valor. |
| YAML | YAML Ain't Markup Language | o | [NT-10](#nt-10-formatos-de-dados-e-de-arquivo) | Formato de texto para configurações. |

### 6.2 Termos

| Termo | Gênero | Categoria | Definição |
|---|---|---|---|
| ação corretiva | a | [NT-20](#nt-20-artefatos-de-processo) | Ação que remove a causa de um desvio ou de um incidente para impedir que o problema aconteça de novo. |
| acessibilidade | a | [NT-05](#nt-05-elementos-de-interface) | Qualidade de uma interface que todas as pessoas podem usar, também as pessoas que usam um leitor de tela ou apenas o teclado. |
| administrador | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa com permissão para configurar um sistema e gerenciar as contas do sistema. |
| agendador | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Componente que executa jobs em datas e horas definidas. |
| agente | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Programa que funciona em um servidor e que coleta dados ou executa tarefas para outro sistema. |
| alvo | o | [NT-18](#nt-18-ambientes) | Sistema, ambiente ou recurso em que um comando ou um deploy faz a ação, por exemplo o cluster `prod-sa-east-1`. |
| ambiente | o | [NT-18](#nt-18-ambientes) | Conjunto de servidores, de configurações e de dados com um uso definido, por exemplo teste ou produção. |
| ambiente de homologação | o | [NT-18](#nt-18-ambientes) | Ambiente igual ao ambiente de produção, que a equipe usa para testar uma versão antes do deploy em produção. |
| ambiente de produção | o | [NT-18](#nt-18-ambientes) | Ambiente que os clientes usam. |
| análise pós-incidente | a | [NT-20](#nt-20-artefatos-de-processo) | Documento que descreve um incidente, a causa e as ações para evitar um incidente igual. |
| analista | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa de uma equipe de TI que analisa, configura ou mantém sistemas. Escreva a área ou o papel: "o analista de suporte", "o analista de plantão". |
| analista de plantão | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que está no plantão de um serviço e que recebe os alertas do serviço. |
| API | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Interface que um software tem para outro software usar as operações e os dados deste software, com regras definidas. |
| aplicação | a | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Programa que faz um trabalho para usuários ou para outros sistemas, por exemplo um site ou uma API. |
| aplicação cliente | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Programa que envia requisições a um servidor. |
| aprovador | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que aprova ou recusa um pedido, uma alteração ou um documento. |
| argumento | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Valor que o código passa para um parâmetro no momento da chamada. Verbo: PASSAR. |
| armazenamento | o | [NT-13](#nt-13-recursos-de-nuvem) | Recurso que mantém dados de forma permanente, por exemplo um disco ou um bucket. |
| arquitetura | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Estrutura de um sistema: os componentes, as conexões entre os componentes e as regras do projeto. |
| artefato | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Arquivo que o pipeline gera e que a equipe usa no deploy, por exemplo um pacote ou uma imagem. |
| assinatura digital | a | [NT-16](#nt-16-segurança-e-identidade) | Código que uma chave privada gera e que confirma quem criou um arquivo e que o arquivo não tem alterações. |
| atalho de teclado | o | [NT-06](#nt-06-teclas-e-grupos-de-teclas) | Grupo de teclas que inicia um comando da interface, por exemplo **Ctrl+S**. |
| ataque | o | [NT-16](#nt-16-segurança-e-identidade) | Ação de uma pessoa ou de um programa que tenta acessar, alterar ou parar um sistema sem permissão. |
| atributo | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Nome e valor de um elemento HTML ou de um objeto, por exemplo o atributo `aria-label` de um botão. |
| auditoria | a | [NT-20](#nt-20-artefatos-de-processo) | Verificação formal e independente de que um sistema ou um processo segue uma norma, uma lei ou uma política. |
| autenticação | a | [NT-16](#nt-16-segurança-e-identidade) | Verificação da identidade de uma pessoa ou de um sistema. |
| autenticação multifator | a | [NT-16](#nt-16-segurança-e-identidade) | Autenticação com a senha e com 1 ou mais verificações a mais, por exemplo um código temporário. Sigla: MFA. |
| automação | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Uso de scripts e de ferramentas que fazem uma tarefa sem a ação de uma pessoa. |
| autoridade certificadora | a | [NT-16](#nt-16-segurança-e-identidade) | Organização que assina certificados e que confirma a identidade do dono de cada certificado. |
| autorização | a | [NT-16](#nt-16-segurança-e-identidade) | Permissão que um sistema dá a uma identidade autenticada para uma ação. |
| backlog | o | [NT-20](#nt-20-artefatos-de-processo) | Lista ordenada das tarefas que a equipe ainda não fez. |
| backup | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Cópia de dados que você usa para restaurar os dados depois de uma perda. |
| backup completo | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Backup com todos os dados de um sistema. |
| backup incremental | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Backup apenas com os dados alterados depois do backup anterior. |
| balanceador de carga | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Componente que distribui as requisições entre 2 ou mais servidores. |
| banco | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Nome curto de "banco de dados". Use depois da primeira ocorrência de "banco de dados" no documento, ou com o nome do banco: "o banco `pedidos`". |
| banco de dados | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Sistema que armazena dados organizados e que permite consultar e alterar estes dados. |
| biblioteca | a | [NT-11](#nt-11-linguagens-frameworks-e-bibliotecas) | Conjunto de código que um programa usa para fazer tarefas comuns. |
| bloco | o | [NT-25](#nt-25-termos-de-linguagem-e-de-redação) | Grupo de linhas que um documento mostra separado do texto, por exemplo um bloco de código. |
| booleano | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Tipo de dado com apenas 2 valores: `true` ou `false`. |
| botão | o | [NT-05](#nt-05-elementos-de-interface) | Elemento da interface que inicia uma ação quando o usuário clica no elemento. |
| branch | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Linha de desenvolvimento separada em um repositório. |
| bucket | o | [NT-13](#nt-13-recursos-de-nuvem) | Item que contém arquivos em um serviço de armazenamento de nuvem. |
| build | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Processo que converte o código-fonte em um artefato. Para o resultado do build, use "artefato". |
| busca | a | [NT-05](#nt-05-elementos-de-interface) | Função da interface que procura itens com o texto que o usuário digita, por exemplo no campo de busca. Para a ação do leitor, use PROCURAR (03-dicionario.md). |
| cabeçalho | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Parte inicial de uma mensagem ou de um arquivo, com dados sobre o conteúdo. Exemplos: o cabeçalho HTTP `Authorization`, o cabeçalho YAML de um documento. |
| cache | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Área de armazenamento rápido que mantém uma cópia de dados para responder mais rápido. |
| caixa de seleção | a | [NT-05](#nt-05-elementos-de-interface) | Elemento da interface que o usuário marca ou desmarca. |
| campo | o | [NT-05](#nt-05-elementos-de-interface) | Item com nome que contém um valor: em uma tela, em um formulário, em um objeto JSON ou em uma linha de uma tabela. |
| causa raiz | a | [NT-20](#nt-20-artefatos-de-processo) | Causa principal de um incidente ou de um desvio. Se a equipe corrigir a causa raiz, o problema não acontece de novo. |
| certificado | o | [NT-16](#nt-16-segurança-e-identidade) | Certificado digital: arquivo que associa uma chave pública a uma identidade, com a assinatura de uma autoridade certificadora. |
| chamado | o | [NT-20](#nt-20-artefatos-de-processo) | Pedido de suporte ou de acesso que uma pessoa registra em um sistema de chamados. Use "chamado" para o item. Use "pedido" apenas no nome de um modelo de chamado. |
| chave de API | a | [NT-16](#nt-16-segurança-e-identidade) | Código secreto que identifica uma aplicação cliente em uma API. |
| chave privada | a | [NT-16](#nt-16-segurança-e-identidade) | Chave secreta que apenas o dono tem e que gera assinaturas ou descriptografa dados. |
| chave pública | a | [NT-16](#nt-16-segurança-e-identidade) | Chave que o dono pode distribuir e que verifica assinaturas ou criptografa dados. |
| chave SSH | a | [NT-16](#nt-16-segurança-e-identidade) | Chave privada e chave pública que autenticam um usuário em um servidor com o SSH. |
| ciclo de vida | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Sequência dos estados de um item, da criação até a exclusão, por exemplo o ciclo de vida de uma versão. |
| cliente | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa ou empresa que usa um produto da empresa. Para o programa, use "aplicação cliente". |
| cluster | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Grupo de servidores que funcionam juntos como um sistema. |
| cobertura de testes | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Porcentagem do código que os testes automáticos executam. |
| código de status | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Número de 3 algarismos que um servidor HTTP retorna na resposta para indicar o resultado da requisição, por exemplo `200` ou `404`. |
| código-fonte | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Texto de um programa em uma linguagem de programação. |
| cofre de segredos | o | [NT-16](#nt-16-segurança-e-identidade) | Serviço que armazena segredos com criptografia e que controla o acesso a cada segredo. |
| colaborador | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que faz um trabalho para a empresa. |
| comando | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Texto que o usuário digita no terminal ou no shell para executar um programa ou uma operação. Para uma frase no imperativo, use INSTRUÇÃO (03). |
| commit | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Conjunto de alterações que o Git grava em um repositório, com o nome da pessoa que criou o commit, uma data e uma mensagem. |
| computador | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Equipamento que executa programas e processa dados. |
| comunicado de incidente | o | [NT-20](#nt-20-artefatos-de-processo) | Texto que a empresa publica para os clientes durante um incidente, com o impacto, o estado e a hora da próxima atualização. |
| conformidade | a | [NT-20](#nt-20-artefatos-de-processo) | Estado de um sistema ou de um processo que segue uma norma, uma lei ou uma política. |
| console | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Interface em que o administrador gerencia um serviço de nuvem ou uma ferramenta, por exemplo o console da AWS. |
| consulta | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Pedido de dados a um banco de dados ou a uma API. |
| consumidor | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Componente que obtém e processa as mensagens de uma fila. |
| conta | a | [NT-16](#nt-16-segurança-e-identidade) | Identidade de uma pessoa ou de um sistema em um serviço, com credenciais e permissões. Escreva um artigo ou um pronome antes do nome (seção 1). |
| conta de serviço | a | [NT-16](#nt-16-segurança-e-identidade) | Conta que um programa usa para acessar outro sistema. Uma pessoa não entra em um sistema com uma conta de serviço. |
| contêiner | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Processo isolado que executa uma aplicação com as dependências da aplicação, a partir de uma imagem. |
| contexto | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Configuração do `kubectl` que define o cluster, o usuário e o namespace de um comando. Escreva o nome: "o contexto `prod-sa-east-1`" ([R7.8](02-regras.md#r78-identifique-o-ambiente-antes-de-um-comando-que-altera-ou-exclui-dados-revisor)). |
| corpo | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Parte de uma requisição ou de uma resposta HTTP que contém os dados, depois do cabeçalho. |
| cota | a | [NT-13](#nt-13-recursos-de-nuvem) | Quantidade máxima de um recurso que uma conta ou um projeto pode usar. |
| credencial | a | [NT-16](#nt-16-segurança-e-identidade) | Informação que confirma uma identidade, por exemplo uma senha, um token ou uma chave. |
| criptografia | a | [NT-16](#nt-16-segurança-e-identidade) | Processo que converte dados com uma chave para impedir a leitura sem a chave. |
| dados pessoais | os | [NT-16](#nt-16-segurança-e-identidade) | Dados que identificam uma pessoa ou que permitem identificar uma pessoa (LGPD). |
| dados pessoais sensíveis | os | [NT-16](#nt-16-segurança-e-identidade) | Dados pessoais que a LGPD classifica como sensíveis e protege com regras a mais. A LGPD tem a lista destes dados. |
| degradação | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Desempenho menor de um serviço sem perda de funcionalidade, por exemplo uma latência maior. A palavra de sinalização é CUIDADO (02-regras.md, [R7.1](02-regras.md#r71-use-o-nível-de-aviso-da-consequência-mais-grave-revisor)). |
| dependência | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Pacote ou serviço que outro software precisa para funcionar. |
| deploy | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Processo que coloca uma versão de um software em um ambiente. |
| desenvolvedor | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que escreve, testa e mantém o código de um software. |
| deslocamento | o | [NT-22](#nt-22-unidades-de-medida) | Diferença entre um fuso horário e o UTC, por exemplo `-03:00`. |
| desvio | o | [NT-20](#nt-20-artefatos-de-processo) | Diferença entre o resultado de um processo e a norma, a regra ou o requisito do processo. |
| dia útil | o | [NT-22](#nt-22-unidades-de-medida) | Dia em que a empresa funciona, de acordo com o calendário da empresa. Plural: dias úteis. |
| disponibilidade | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Porcentagem do tempo em que um sistema funciona e responde. |
| DNS | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Sistema que converte nomes de domínio em endereços IP. |
| domínio | o | [NT-14](#nt-14-rede-e-endereços) | Nome de um site ou de um serviço na internet, por exemplo `exemplo.com.br`. |
| dono do produto | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que decide as prioridades e os requisitos de um produto. |
| editor | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Programa que altera o conteúdo de arquivos de texto ou de código. |
| elemento | o | [NT-05](#nt-05-elementos-de-interface) | Nome curto de "elemento de interface", depois da primeira ocorrência no documento. No código de uma página, escreva o literal: "o elemento `<button>`". |
| elemento de interface | o | [NT-05](#nt-05-elementos-de-interface) | Parte da interface que o usuário vê ou usa: um botão, um campo, um menu ou uma guia. |
| endereço | o | [NT-14](#nt-14-rede-e-endereços) | Valor que identifica o lugar de um item em uma rede, por exemplo um endereço IP, uma URL ou um endereço de e-mail. Escreva o tipo: "o endereço IP", "o endereço de e-mail". |
| endereço IP | o | [NT-14](#nt-14-rede-e-endereços) | Número que identifica um equipamento em uma rede. |
| endpoint | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Endereço de uma API que recebe um tipo de requisição. |
| entrada do dicionário | a | [NT-25](#nt-25-termos-de-linguagem-e-de-redação) | Linha do dicionário com uma palavra, a classe, o significado ou a alternativa e os exemplos. |
| esquema | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Estrutura de um banco de dados ou de um documento: tabelas, campos, tipos e regras. |
| exceção | a | [NT-03](#nt-03-comandos-código-e-identificadores) | Objeto que o código lança quando um erro acontece durante a execução. Escreva o nome: "a exceção `TimeoutError`" (03-dicionario.md, D7). |
| failover | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Transferência do trabalho de um componente com falha para um componente de reserva, por exemplo da réplica primária para a réplica secundária. |
| falso negativo | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Resultado de uma ferramenta ou de um teste que não indica um erro que existe. |
| falso positivo | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Resultado de uma ferramenta ou de um teste que indica um erro que não existe, por exemplo um alerta do linter para uma frase correta. |
| fila | a | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Componente que armazena mensagens em ordem até um consumidor processar as mensagens. |
| filtro | o | [NT-05](#nt-05-elementos-de-interface) | Condição que limita os itens que uma lista ou uma tela mostra. Para a ação, use FILTRAR (03-dicionario.md). |
| firewall | o | [NT-14](#nt-14-rede-e-endereços) | Sistema que permite ou bloqueia o tráfego de rede de acordo com regras. |
| formulário | o | [NT-05](#nt-05-elementos-de-interface) | Tela ou parte de uma tela com campos que o usuário preenche e envia. |
| framework | o | [NT-11](#nt-11-linguagens-frameworks-e-bibliotecas) | Conjunto de código e de regras que define a estrutura de uma aplicação. |
| função | a | [NT-03](#nt-03-comandos-código-e-identificadores) | Bloco de código com nome que recebe argumentos e executa uma tarefa. Não use "função" para um papel de acesso nem para um cargo ([NT-19](#nt-19-papéis-de-pessoas-em-processos)). |
| gateway | o | [NT-14](#nt-14-rede-e-endereços) | Componente que recebe as requisições e encaminha as requisições para os sistemas internos. |
| gatilho | o | [NT-20](#nt-20-artefatos-de-processo) | Evento ou condição que inicia um processo, um procedimento ou um pipeline. |
| gerente de incidente | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que organiza e controla a resposta a um incidente. |
| gestor | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que gerencia uma equipe e que aprova as tarefas e os recursos da equipe. |
| hash | o | [NT-16](#nt-16-segurança-e-identidade) | Valor de tamanho fixo que o sistema calcula a partir de um dado. |
| host | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Computador ligado a uma rede, com um nome ou um endereço IP, por exemplo "a porta 80 do host". Use "host" quando o texto é sobre o computador na rede (o endereço, o nome, as portas, os usuários do computador). Para o papel do computador que responde a requisições de um serviço, use "servidor". |
| host de administração | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Servidor com acesso controlado que a equipe usa para executar os comandos que gerenciam a produção. Os outros servidores da produção aceitam conexões SSH apenas deste servidor. Também "bastion" (seção 5.5). |
| identidade | a | [NT-16](#nt-16-segurança-e-identidade) | Conjunto de dados que identifica uma pessoa ou um sistema para outro sistema, por exemplo um usuário ou uma conta de serviço. |
| identificador | o | [NT-08](#nt-08-códigos-identificadores-e-números-de-referência) | Valor que identifica um item, por exemplo um ID, um UUID ou o número de um chamado. |
| imagem | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Arquivo com um sistema de arquivos e com a configuração que um contêiner usa para iniciar. |
| imagem decorativa | a | [NT-05](#nt-05-elementos-de-interface) | Imagem que não dá informação. O texto alternativo de uma imagem decorativa é vazio ([R10.9](02-regras.md#r109-escreva-textos-de-validação-de-acessibilidade-de-link-e-de-estado-vazio-com-a-ação-revisor)). |
| incidente | o | [NT-20](#nt-20-artefatos-de-processo) | Evento que faz um serviço parar ou que diminui a qualidade de um serviço. |
| incidente de segurança | o | [NT-16](#nt-16-segurança-e-identidade) | Incidente que afeta a segurança de dados ou de sistemas, por exemplo um acesso sem permissão ou um vazamento de dados. |
| indicador | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Métrica que mede o resultado de um processo e que a equipe compara com uma meta. |
| índice | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Estrutura que um banco de dados usa para encontrar as linhas de uma tabela em menos tempo. |
| infraestrutura | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Conjunto dos servidores, das redes e dos serviços em que os sistemas funcionam. |
| instalador | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Programa que instala um software em um computador. |
| instância | a | [NT-13](#nt-13-recursos-de-nuvem) | Cópia em execução de uma máquina virtual, de um banco de dados ou de outro recurso de nuvem. Escreva o tipo: "a instância de máquina virtual", "a instância de banco de dados". |
| integração contínua (CI) | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Prática que gera o build e executa os testes de forma automática a cada commit. |
| interface | a | [NT-05](#nt-05-elementos-de-interface) | Parte de um software que uma pessoa ou outro software usa para controlar o software, por exemplo as telas de uma aplicação ou uma API. |
| internet | a | [NT-14](#nt-14-rede-e-endereços) | Rede pública que conecta as redes de computadores. |
| issue | a | [NT-20](#nt-20-artefatos-de-processo) | Item de trabalho em um rastreador: um defeito, uma tarefa ou uma funcionalidade. |
| janela de manutenção | a | [NT-20](#nt-20-artefatos-de-processo) | Período aprovado em que a equipe tem permissão para parar ou alterar um serviço. |
| job | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Tarefa que um agendador ou um pipeline executa. |
| kernel | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Parte central do sistema operacional que controla o hardware e os processos. |
| largura de banda | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Quantidade máxima de dados que uma conexão de rede envia por segundo, em bit/s. |
| latência | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Tempo entre o envio de uma requisição e o momento em que a aplicação cliente recebe a resposta. |
| lei | a | [NT-23](#nt-23-normas-leis-e-documentos-de-referência) | Norma oficial que todas as pessoas e todas as empresas de um país precisam cumprir. |
| leitor | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que lê um documento. |
| licença | a | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Permissão de uso de um software, com as condições que o fornecedor define. |
| lições aprendidas | as | [NT-20](#nt-20-artefatos-de-processo) | Parte da análise pós-incidente com o que a equipe aprendeu e com as ações para o futuro. |
| limite de taxa | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Número máximo de requisições que uma aplicação cliente pode enviar a uma API em um período. Depois do limite, a API retorna o código de status `429`. |
| linha (de tabela) | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Item de uma tabela de banco de dados, com 1 valor em cada coluna. Escreva "a linha 42 da tabela `clientes`" (03-dicionario.md, D7). Não use "registro" com este significado. |
| linha do tempo | a | [NT-20](#nt-20-artefatos-de-processo) | Lista dos eventos de um incidente em ordem, com a data e a hora em UTC ([R8.5](02-regras.md#r85-escreva-datas-no-formato-iso-8601-e-horas-com-o-fuso-horário-revisor)). |
| lixeira | a | [NT-04](#nt-04-arquivos-pastas-caminhos-e-urls) | Pasta que mantém os arquivos excluídos por um tempo, antes da exclusão permanente. |
| log | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Arquivo ou fluxo de eventos que um sistema registra em ordem de tempo. |
| login | o | [NT-16](#nt-16-segurança-e-identidade) | Início de uma sessão em um sistema com as credenciais do usuário. |
| manifesto | o | [NT-04](#nt-04-arquivos-pastas-caminhos-e-urls) | Arquivo YAML ou JSON que descreve os objetos que o Kubernetes cria, por exemplo `deployment.yaml`. |
| máquina virtual | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Computador que um software simula sobre um computador físico. |
| memória | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Componente que armazena os dados e os programas em uso em um computador (RAM). |
| merge | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Ação de juntar as alterações de um branch em outro branch. |
| meta | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Valor de um indicador que a equipe precisa obter em um período. |
| métrica | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Número que um sistema mede em intervalos definidos. |
| microsserviço | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Serviço pequeno e independente que faz uma parte do trabalho do sistema e que tem deploy próprio. |
| migração | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Alteração da estrutura ou dos dados de um banco, ou ação de mover um sistema para outra plataforma, com um procedimento controlado. |
| mitigação | a | [NT-20](#nt-20-artefatos-de-processo) | Ação que diminui o impacto de um incidente antes da correção da causa raiz. Para a ação, use DIMINUIR (03), não "mitigar". |
| mock | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Objeto que simula um componente real durante um teste. |
| módulo | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Parte de um software com um objetivo definido e com uma interface própria. |
| navegador | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Programa que mostra páginas da web. |
| nó | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Servidor ou máquina virtual que faz parte de um cluster. Plural: "os nós" (seção 1). |
| nome do host | o | [NT-14](#nt-14-rede-e-endereços) | Nome de um host na rede, por exemplo `db-01.exemplo.com.br`. Em uma URL, é a parte entre o protocolo e o caminho. O literal `hostname` é o nome do comando e do campo. |
| notificação | a | [NT-07](#nt-07-mensagens-e-textos-do-sistema) | Mensagem que um sistema envia a uma pessoa sobre um evento, por exemplo um e-mail ou um alerta na tela. |
| nulo | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Valor que indica a falta de um valor: `null` no JSON, `NULL` no SQL. |
| número decimal | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Tipo de dado de um número com parte decimal, por exemplo `2.5` no JSON. |
| número inteiro | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Tipo de dado de um número sem parte decimal, por exemplo `42`. |
| objeto | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Estrutura de dados com campos e valores, em um programa ou em um formato de dados como o JSON. |
| observabilidade | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Capacidade de entender o estado interno de um sistema com os logs, as métricas e os rastros que o sistema gera. |
| operação de escrita | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Operação que grava ou altera dados em um disco ou em um banco de dados. |
| operação de leitura | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Operação que obtém dados de um disco ou de um banco de dados, sem alterar os dados. |
| operador | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que monitora e controla um sistema em produção. Na LGPD, "operador" é um nome da lei ([NT-23](#nt-23-normas-leis-e-documentos-de-referência)). |
| pacote | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Arquivo que contém um software ou uma biblioteca e os dados para instalar o software ou a biblioteca. |
| pacote de rede | o | [NT-14](#nt-14-rede-e-endereços) | Unidade de dados que uma rede envia de um equipamento para outro equipamento. |
| página de status | a | [NT-04](#nt-04-arquivos-pastas-caminhos-e-urls) | Site em que a empresa publica o estado dos serviços e os comunicados de incidente. |
| paginação | a | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Ação de dividir uma resposta grande de uma API em partes que a aplicação cliente pede uma de cada vez. |
| painel | o | [NT-05](#nt-05-elementos-de-interface) | Tela que mostra métricas, gráficos e estados de um sistema ("dashboard"). Para a interface que gerencia um serviço, use "console" ou "portal". |
| palavra de sinalização | a | [NT-25](#nt-25-termos-de-linguagem-e-de-redação) | Palavra no início de um aviso que indica o nível de risco: PERIGO, ATENÇÃO, CUIDADO ou NOTA (02-regras.md, seção 7). |
| papel | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Responsabilidade de uma pessoa em um processo, por exemplo revisor ou aprovador. Para um conjunto de permissões, use "papel de acesso". |
| papel de acesso | o | [NT-16](#nt-16-segurança-e-identidade) | Conjunto de permissões que um sistema atribui a uma identidade (RBAC ou IAM). Se a interface mostrar **Função** ou **Role**, o rótulo é um literal (E1). |
| parâmetro | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Nome de um valor que uma função, um comando ou uma requisição recebe, por exemplo `timeout`. O valor é o argumento. |
| parâmetro de consulta | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Nome e valor depois do sinal `?` de uma URL, por exemplo `?pagina=2`. |
| pasta | a | [NT-04](#nt-04-arquivos-pastas-caminhos-e-urls) | Item do sistema de arquivos que contém arquivos e outras pastas. |
| patch | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Alteração pequena que corrige um defeito ou uma vulnerabilidade. |
| percentil | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Valor que separa uma porcentagem das medidas. O percentil 99 (p99) da latência é maior que 99% das latências medidas. |
| perfil | o | [NT-05](#nt-05-elementos-de-interface) | Conjunto dos dados da conta de um usuário que a interface mostra ao usuário, por exemplo o nome e a foto. Para um conjunto de permissões, use "papel de acesso" ([NT-16](#nt-16-segurança-e-identidade)). Para o trabalho de uma pessoa, use CARGO (03-dicionario.md). |
| permissão de escrita | a | [NT-16](#nt-16-segurança-e-identidade) | Permissão para criar, alterar e excluir os dados ou os arquivos de um recurso. |
| permissão de leitura | a | [NT-16](#nt-16-segurança-e-identidade) | Permissão para ver os dados ou os arquivos de um recurso, sem alterar os dados ou os arquivos. |
| pipeline | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Sequência automática de etapas que gera o build, testa e executa o deploy de um software. |
| placeholder | o | [NT-05](#nt-05-elementos-de-interface) | Texto de exemplo dentro de um campo vazio da interface. O campo não mostra o texto depois que o usuário começa a digitar. |
| plantão | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Período em que uma pessoa responde aos alertas e aos incidentes de um serviço. |
| plataforma | a | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Conjunto de hardware, de sistema operacional e de serviços em que um sistema funciona. |
| política | a | [NT-16](#nt-16-segurança-e-identidade) | Conjunto de regras que define o que uma pessoa ou um sistema pode fazer. |
| ponto de decisão | o | [NT-20](#nt-20-artefatos-de-processo) | Passo de um procedimento ou de um processo em que o responsável escolhe 1 de 2 ou mais caminhos. |
| porta | a | [NT-14](#nt-14-rede-e-endereços) | Número que identifica um serviço em um endereço IP. |
| portal | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Site em que os usuários ou os clientes acessam os serviços de uma empresa, por exemplo o portal de suporte. |
| privacidade | a | [NT-16](#nt-16-segurança-e-identidade) | Controle que uma pessoa tem sobre o uso dos dados pessoais da pessoa (LGPD). |
| privilégio mínimo | o | [NT-16](#nt-16-segurança-e-identidade) | Regra que dá a cada conta apenas as permissões necessárias para o trabalho da conta. |
| programa | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Software que um computador executa. |
| prompt | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Texto que um programa mostra quando aguarda uma entrada do usuário, por exemplo `$` no terminal ou `Password:`. |
| protocolo | o | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Conjunto de regras que define como 2 sistemas enviam e recebem dados. |
| provedor de identidade | o | [NT-16](#nt-16-segurança-e-identidade) | Sistema que autentica os usuários para outros sistemas, por exemplo o Microsoft Entra ID. Sigla: IdP (seção 6.1). |
| provedor de nuvem | o | [NT-13](#nt-13-recursos-de-nuvem) | Empresa que vende recursos de nuvem, por exemplo a AWS ou o Google Cloud. |
| proxy | o | [NT-14](#nt-14-rede-e-endereços) | Servidor que recebe as requisições de uma aplicação cliente e envia as requisições para outro servidor. |
| pull request | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Pedido para mesclar as alterações de um branch em outro branch, com revisão. |
| rastreador de issues | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Sistema que registra e organiza as issues, por exemplo o Jira. |
| rastro | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Registro do caminho de uma requisição entre os serviços de um sistema, com o tempo de cada parte. |
| recuperação até um ponto no tempo | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Restauração de um banco de dados ao estado de um momento exato, com um backup e com o log de transações. Sigla: PITR. |
| recuperação de desastre | a | [NT-20](#nt-20-artefatos-de-processo) | Plano e procedimentos que fazem os sistemas funcionar de novo depois de uma perda grande. Exemplo: a perda de todos os data centers de uma região. |
| recurso | o | [NT-13](#nt-13-recursos-de-nuvem) | Item que um sistema usa ou que um sistema dá a outro sistema, por exemplo CPU, memória, disco, uma instância ou um endpoint. |
| redator | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que escreve um documento. |
| rede | a | [NT-14](#nt-14-rede-e-endereços) | Conjunto de equipamentos conectados que enviam e recebem dados. |
| região | a | [NT-13](#nt-13-recursos-de-nuvem) | Grupo de data centers de um provedor de nuvem na mesma área, por exemplo São Paulo. |
| registry | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Serviço que armazena repositórios de imagens de contêiner ou de pacotes, por exemplo o Amazon ECR ou o registry do `npm`. |
| regra de negócio | a | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Regra de um processo da empresa que um sistema implementa, por exemplo o valor mínimo de um pedido. |
| réplica | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Cópia de um banco de dados ou de um serviço que o sistema mantém atualizada. |
| réplica primária | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Réplica de um banco de dados que recebe as operações de escrita. |
| réplica secundária | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Réplica de um banco de dados que recebe uma cópia dos dados da réplica primária e que responde apenas a leituras. |
| repositório | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Repositório Git: local que armazena o código com o histórico das versões. Dentro de um registry, escreva "repositório de imagens". Para pacotes de software, escreva "repositório de pacotes". |
| repositório de pacotes | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Serviço que armazena pacotes de software e as versões dos pacotes, por exemplo o repositório `apt` do Ubuntu. |
| requisição | a | [NT-09](#nt-09-protocolos-e-padrões-técnicos) | Mensagem que uma aplicação cliente envia a um servidor para pedir uma ação ou dados. |
| retenção | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Período em que um sistema mantém dados, logs ou backups antes de excluir os dados. |
| revisor | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que revisa um texto ou um código antes da aprovação. |
| roda do mouse | a | [NT-06](#nt-06-teclas-e-grupos-de-teclas) | Parte do mouse que rola o conteúdo da tela. Use o verbo técnico ROLAR: "Role a página com a roda do mouse." |
| rollback | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Ação de reverter um sistema, um banco de dados ou um deploy à versão anterior. |
| rótulo | o | [NT-05](#nt-05-elementos-de-interface) | Texto que identifica um elemento de interface, por exemplo o texto de um botão. O rótulo é um literal ([R10.1](02-regras.md#r101-escreva-o-nome-exato-do-elemento-de-interface-em-negrito-revisor)). |
| runbook | o | [NT-20](#nt-20-artefatos-de-processo) | Procedimento escrito que a equipe segue para manter um serviço ativo ou para resolver um incidente. |
| script | o | [NT-03](#nt-03-comandos-código-e-identificadores) | Arquivo de texto com comandos que um interpretador executa em ordem. |
| segredo | o | [NT-16](#nt-16-segurança-e-identidade) | Valor secreto que um sistema usa, por exemplo uma senha ou uma chave de API. |
| senha | a | [NT-16](#nt-16-segurança-e-identidade) | Sequência de caracteres secreta que confirma a identidade de um usuário. |
| serviço | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Programa que funciona de forma contínua e que responde a requisições de outros programas, por exemplo o serviço `nginx` ou o serviço de pagamento. |
| servidor | o | [NT-12](#nt-12-infraestrutura-física-e-virtual) | Computador ou máquina virtual que recebe requisições e envia respostas. Para o programa, use "serviço" ou "aplicação". |
| sessão | a | [NT-16](#nt-16-segurança-e-identidade) | Período entre o login e o logout de um usuário em um sistema. |
| seta | a | [NT-06](#nt-06-teclas-e-grupos-de-teclas) | Tecla ou ícone que indica uma direção na tela. Escreva a direção: "a seta para baixo", "a seta para a direita". |
| severidade | a | [NT-20](#nt-20-artefatos-de-processo) | Nível do impacto de um incidente ou de um defeito, por exemplo SEV1 a SEV4. Para os níveis S1 a S3 de um desvio de redação (05-governanca.md, seção 4.3), escreva "severidade do desvio". |
| shell | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Programa que lê os comandos que o usuário digita no terminal e que executa os comandos, por exemplo o `bash`. |
| sincronização | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Operação que faz 2 ou mais sistemas ou pastas terem os mesmos dados. Verbo: SINCRONIZAR. |
| sistema operacional | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Software que controla o hardware de um computador e que executa os outros programas. |
| site | o | [NT-04](#nt-04-arquivos-pastas-caminhos-e-urls) | Conjunto de páginas web com um domínio próprio. |
| SLA | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Sigla de "service level agreement": o nível de serviço mínimo que o fornecedor define com o cliente em um documento formal. |
| SLI | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Sigla de "service level indicator": a métrica que mede uma parte do serviço. |
| SLO | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Objetivo de nível de serviço: o valor que a equipe define como meta para um SLI. |
| snapshot | o | [NT-15](#nt-15-dados-e-banco-de-dados) | Cópia do estado de um disco, de um banco ou de uma máquina virtual em um momento. |
| solicitação de mudança | a | [NT-20](#nt-20-artefatos-de-processo) | Pedido formal para alterar um sistema em produção, com o risco e com o plano de rollback. Não use "GMUD" nem "RDM" (seção 6.3). |
| solicitante | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa que cria um chamado ou um pedido. |
| sprint | a | [NT-20](#nt-20-artefatos-de-processo) | Período fixo, em geral de 1 a 4 semanas, em que a equipe faz um conjunto de tarefas planejadas. |
| string | a | [NT-03](#nt-03-comandos-código-e-identificadores) | Sequência de caracteres que um programa trata como texto. |
| sub-rede | a | [NT-14](#nt-14-rede-e-endereços) | Parte de uma rede com uma faixa de endereços IP própria. |
| superusuário | o | [NT-16](#nt-16-segurança-e-identidade) | Conta com todas as permissões de um sistema, por exemplo o usuário `root` no Linux. Use esta conta apenas quando nenhuma outra conta tem a permissão. |
| tag | a | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Nome fixo que identifica um commit ou uma imagem, em geral uma versão. |
| taxa de erro | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Porcentagem das requisições que terminam com erro em um período. |
| tela | a | [NT-05](#nt-05-elementos-de-interface) | Conjunto de elementos de interface que a aplicação mostra ao mesmo tempo. |
| tempo limite | o | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Tempo máximo que um sistema aguarda uma resposta antes de cancelar a operação. |
| terminal | o | [NT-01](#nt-01-produtos-softwares-e-serviços-externos) | Programa que mostra uma linha de comando em que o usuário digita os comandos para o shell. |
| thread | a | [NT-03](#nt-03-comandos-código-e-identificadores) | Sequência de execução dentro de um processo do sistema operacional. |
| token | o | [NT-16](#nt-16-segurança-e-identidade) | Código que um sistema gera e que confirma uma identidade ou uma permissão por um tempo limitado. |
| tráfego | o | [NT-14](#nt-14-rede-e-endereços) | Dados que uma rede ou um componente envia e recebe em um período. |
| transação | a | [NT-15](#nt-15-dados-e-banco-de-dados) | Grupo de operações de banco de dados que o banco aplica por completo ou não aplica. |
| URL | a | [NT-04](#nt-04-arquivos-pastas-caminhos-e-urls) | Endereço completo de um recurso na web. |
| usuário | o | [NT-19](#nt-19-papéis-de-pessoas-em-processos) | Pessoa ou sistema que usa um software com uma conta própria. |
| variável | a | [NT-03](#nt-03-comandos-código-e-identificadores) | Nome que armazena um valor em um programa ou em uma configuração. |
| variável de ambiente | a | [NT-03](#nt-03-comandos-código-e-identificadores) | Variável que o sistema operacional dá a um processo no início. |
| vazamento de dados | o | [NT-16](#nt-16-segurança-e-identidade) | Incidente de segurança em que dados secretos ou dados pessoais ficam disponíveis para pessoas sem permissão. |
| vazão | a | [NT-21](#nt-21-métricas-indicadores-e-níveis-de-serviço) | Quantidade de requisições ou de dados que um sistema processa por unidade de tempo ("throughput"). |
| versionamento semântico | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Regra de números de versão no formato `MAJOR.MINOR.PATCH`, por exemplo 2.4.1. MAJOR, MINOR e PATCH são os nomes das 3 partes do número. |
| volume | o | [NT-13](#nt-13-recursos-de-nuvem) | Área de armazenamento que um contêiner ou uma máquina virtual usa como um disco, por exemplo um volume do Kubernetes. Para uma quantidade, use QUANTIDADE (03). |
| VPN | a | [NT-14](#nt-14-rede-e-endereços) | Rede privada virtual: conexão criptografada entre um computador e uma rede privada. |
| vulnerabilidade | a | [NT-16](#nt-16-segurança-e-identidade) | Defeito de um software ou de uma configuração que permite um ataque. |
| web | a | [NT-14](#nt-14-rede-e-endereços) | Conjunto das páginas e dos serviços que a internet tem com o HTTP. |
| webhook | o | [NT-17](#nt-17-desenvolvimento-e-entrega-de-software) | Requisição HTTP que um sistema envia de forma automática para outro sistema quando um evento acontece. |
| worker | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Processo que obtém tarefas de uma fila e executa as tarefas. |

### 6.3 Siglas e termos não aprovados

Estas siglas e estes termos são comuns nas equipes brasileiras, mas o PTS-BR não aprova o uso em prosa. Use a forma da coluna "PTS-BR". Um literal (o nome de um campo ou de um tipo de chamado na ferramenta) segue a regra E1.

| Não aprovado | PTS-BR | Nota |
|---|---|---|
| GMUD, RDM | solicitação de mudança | Siglas internas sem padrão entre empresas. |
| KPI | indicador | — |
| plantonista | analista de plantão | Também em [`03-dicionario.md`](03-dicionario.md). |
| perfil de acesso, função (de acesso) | papel de acesso | [NT-16](#nt-16-segurança-e-identidade) e [NT-19](#nt-19-papéis-de-pessoas-em-processos). |
| status (em prosa) | estado | [NT-24](#nt-24-valores-de-estado-do-sistema). |
| payload (de uma requisição HTTP) | corpo | Seção 5.5. |
| código HTTP | código de status | Seção 6.2. |
| evidência | registro | REGISTRO (03-dicionario.md). Para um item de uma tabela do banco, use "linha". |
| mitigar | diminuir | DIMINUIR (03-dicionario.md). O substantivo "mitigação" é aprovado (seção 6.2). |

---

## 7. Glossário do projeto

Cada projeto mantém um glossário com os nomes que o glossário-base não tem. O glossário do projeto segue estas regras:

1. Cada termo pertence a uma categoria da seção 3.
2. Cada termo tem um gênero, uma definição em PTS-BR e um único significado.
3. Cada termo indica os sinônimos que o projeto não aprova. Exemplo: "serviço de cobrança" é aprovado. "billing" e "módulo financeiro" não são aprovados.
4. Um termo do projeto não pode ter o nome de uma palavra do dicionário ou do glossário-base com outro significado.
5. Um estrangeirismo novo segue os critérios da seção 5.2. O dono do glossário do projeto aprova o termo (05-governanca.md, seção 7.1).

Modelo de entrada:

| Termo | Gênero | Categoria | Definição | Sinônimos não aprovados |
|---|---|---|---|---|
| serviço de cobrança | o | [NT-02](#nt-02-componentes-do-sistema-do-projeto) | Serviço que calcula o pagamento de cada cliente e que envia a cobrança 1 vez por mês. | billing, módulo financeiro |

---

<!-- nav -->
[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · [03 Dicionário](03-dicionario.md) · **04 Termos técnicos** · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)

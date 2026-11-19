#!/usr/bin/env python3
"""Linter PTS-BR em Python: aplica as mesmas regras do Vale sem o Vale.

O script lê os arquivos tools/vale/PTSBR/*.yml e traduz cada padrão para o módulo
`re` do Python. Assim o Vale e este script usam a mesma fonte de regras.
O script usa apenas a biblioteca padrão do Python 3.9 ou mais nova.

Modos:
  python3 tools/check_spec.py ARQUIVO.md [...]   Verifica arquivos Markdown.
  python3 tools/check_spec.py --spec [ARQUIVO.md ...]
                                                  Verifica o texto da própria especificação
                                                  (README, 01, 02, 04, 05 e 06, ou os arquivos dados).
  python3 tools/check_spec.py --teste             Executa os testes das regras e do 06.
  python3 tools/check_spec.py --teste --motor vale --vale CAMINHO
                                                  Executa os mesmos testes com o Vale.
  python3 tools/check_spec.py --metricas ARQUIVO.md [...]
                                                  Calcula M1 e as palavras candidatas de M2 e
                                                  mostra a linha [METRICAS] do registro (05, 4.1).
  python3 tools/check_spec.py --mensagens ARQUIVO.json|ARQUIVO.po [...]
                                                  Verifica as mensagens de interface de um arquivo
                                                  de tradução (JSON plano ou aninhado, gettext .po
                                                  ou .pot), com a regra Mensagens (R10.5, R10.7,
                                                  R10.8). Cada alerta mostra a chave da mensagem.
  python3 tools/check_spec.py --lista-branca ARQUIVO.md [...]
  python3 tools/check_spec.py --lista-branca --spec [ARQUIVO.md ...]
                                                  Mostra as palavras fora da lista branca
                                                  (decisão E1, regra D9 do 03): a frequência,
                                                  os locais (arquivo:linha) e a porcentagem.
                                                  A lista branca verifica a forma, não o significado.

Opções:
  --resumo        Mostra apenas a contagem por arquivo e por regra.
  --regra NOME    Mostra apenas a regra NOME (por exemplo, PalavrasNaoAprovadas).
  --limite-frase auto|descritivo|procedimento|pasta
                  auto (padrão): 20 palavras em itens de lista numerada, 25 nas
                  outras frases (R4.2). pasta: o limite do Vale para a pasta do arquivo, de
                  acordo com as seções do .vale.ini (--config; sem --config, o .vale.ini do
                  diretório atual ou o .vale.ini das regras). Os outros valores usam um só limite.
  --config ARQUIVO
                  Um .vale.ini: o script lê MinAlertLevel, StylesPath, as seções [glob],
                  BasedOnStyles e PTSBR.<Regra> = YES|NO|suggestion|warning|error, como o Vale.
                  O caminho de cada arquivo é comparado em relação à pasta do .vale.ini.
                  Sem --config, o script usa todas as regras, exceto a regra Mensagens.
  --glossario ARQUIVO
                  O glossário do projeto (tabela do modelo de 04, seção 7). A coluna "Termo"
                  entra na lista branca. A coluna "Sinônimos não aprovados" gera a regra
                  GlossarioProjeto (R1.1) em todos os modos.
  --falhar        Sai com o código 1 se existir um alerta (o padrão: apenas alertas de nível error).
  --metricas      Calcula M1 e M2 (05, seção 5) por arquivo, em vez da lista de alertas. M2 conta
                  cada palavra 1 vez: o linter e a lista branca na mesma linha contam 1 vez, e
                  um tempo verbal não aprovado (CK-3.1) fica fora de M2.
  --json ARQUIVO  Com --metricas ou --lista-branca: grava o resultado em JSON.
  --regras PASTA  Pasta das regras: a pasta PTSBR com os arquivos .yml, ou a pasta do
                  StylesPath que contém a pasta PTSBR. Padrão: tools/vale/PTSBR, ou o
                  StylesPath do --config.
  --dicionario ARQUIVO
                  O 03-dicionario.md da versão que a equipe usa (lista branca e M2).
  --termos ARQUIVO
                  O 04-termos-tecnicos.md da versão que a equipe usa (lista branca e M2).
  --meta PCT      Com --lista-branca: sai com o código 1 se as palavras fora passarem de PCT %.
  --locais N      Com --lista-branca: número de locais por palavra (padrão: 5; 0 = todos).

Num repositório de equipe, use --regras (ou --config), --dicionario e --termos: o script não depende da
estrutura de pastas da especificação. A isenção --spec vale apenas para o texto da própria
especificação (01-introducao.md, seção 11.1).

Diferenças conhecidas em relação ao Vale:
  - O código em linha conta como 1 palavra na regra de frase longa (R4.2). O Vale não lê o código em linha.
  - A divisão de frases é uma aproximação da divisão do Vale.
  - O script não verifica o negrito de até 3 palavras (rótulo de interface, valor de estado,
    palavra de sinalização: R8.8) e conta este negrito como 1 palavra. O Vale não verifica
    nenhum negrito (IgnoredScopes = code, tt, strong).
  - "código de status" e "códigos de status" são um nome técnico do 04: a regra
    PalavrasNaoAprovadas não alerta "status" nesta locução (nos dois motores).
"""
import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

import lista_branca

BASE = pathlib.Path(__file__).resolve().parent.parent
ESTILOS = BASE / "tools" / "vale"
REGRAS_DIR = ESTILOS / "PTSBR"
TESTES_DIR = ESTILOS / "testes"
ARQUIVOS_SPEC = ["README.md", "01-introducao.md", "02-regras.md", "04-termos-tecnicos.md",
                 "05-governanca.md", "06-exemplos.md"]
# A lista branca também verifica o texto do 03 (as definições e os exemplos PTS-BR).
ARQUIVOS_LISTA_BRANCA = ["README.md", "01-introducao.md", "02-regras.md", "03-dicionario.md",
                         "04-termos-tecnicos.md", "05-governanca.md", "06-exemplos.md"]
# Em --spec, as células destas colunas mostram usos não aprovados de propósito.
COLUNAS_IGNORADAS = ("não aprovad", "uso não técnico", "termo em inglês", "trecho original",
                     "sinônimos não aprovados", "antes", "forma completa", "nome completo", "inglês")


# ---------------------------------------------------------------- leitura das regras

def ler_yaml_simples(texto):
    """Lê o subconjunto de YAML das regras PTSBR: chaves simples, lista 'tokens' e mapa 'swap'."""
    dados, chave_atual = {}, None

    def valor(v):
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
            v = v[1:-1]
            return v.replace("''", "'") if v and texto else v
        return v

    for linha in texto.splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        if linha.startswith("  - "):
            dados.setdefault(chave_atual, []).append(valor(linha[4:]))
        elif linha.startswith("  ") and chave_atual == "swap":
            m = re.match(r"\s+'(.*)':\s*(.*)$", linha)
            dados.setdefault("swap", []).append((m.group(1), valor(m.group(2))))
        else:
            k, _, v = linha.partition(":")
            chave_atual = k.strip()
            if v.strip():
                dados[chave_atual] = valor(v)
    return dados


def classe_para_python(conteudo):
    r"""Traduz o conteúdo de uma classe [...] com \p{L} ou \p{N}."""
    tem_l, tem_n = r"\p{L}" in conteudo, r"\p{N}" in conteudo
    resto = conteudo.replace(r"\p{L}", "").replace(r"\p{N}", "")
    partes = []
    if tem_l and tem_n:
        partes.append(r"[^\W_]")
    elif tem_l:
        partes.append(r"[^\W\d_]")
    elif tem_n:
        partes.append(r"\d")
    if resto:
        partes.append("[" + resto + "]")
    return "(?:" + "|".join(partes) + ")"


def regex_para_python(padrao):
    r"""Traduz um padrão do Vale (regexp2) para o módulo re: \p{L} e \p{N}."""
    saida, i = [], 0
    while i < len(padrao):
        c = padrao[i]
        if c == "\\":
            saida.append(padrao[i:i + 2])
            i += 2
            continue
        if c == "[":
            j, fim = i + 1, None
            if j < len(padrao) and padrao[j] == "^":
                j += 1
            while j < len(padrao):
                if padrao[j] == "\\":
                    j += 2
                    continue
                if padrao[j] == "]":
                    fim = j
                    break
                j += 1
            conteudo = padrao[i + 1:fim]
            if (r"\p{L}" in conteudo or r"\p{N}" in conteudo) and not conteudo.startswith("^"):
                saida.append(classe_para_python(conteudo))
            else:
                saida.append(padrao[i:fim + 1])
            i = fim + 1
            continue
        saida.append(c)
        i += 1
    texto = "".join(saida)
    return texto.replace(r"\p{L}", r"[^\W\d_]").replace(r"\p{N}", r"\d")


class Regra:
    def __init__(self, arquivo=None, nome=None, dados=None):
        """Uma regra de um arquivo .yml, ou uma regra em memória (nome + dados no formato do .yml)."""
        self.nome = nome or arquivo.stem
        d = dados if dados is not None else ler_yaml_simples(arquivo.read_text(encoding="utf-8"))
        self.tipo = d["extends"]
        self.mensagem = d.get("message", "")
        self.nivel = d.get("level", "warning")
        flags = re.IGNORECASE if d.get("ignorecase") == "true" else 0
        self.padroes = []
        if self.tipo == "existence":
            for t in d.get("tokens", []):
                self.padroes.append((re.compile(regex_para_python(t), flags), None))
        elif self.tipo == "substitution":
            for chave, troca in d.get("swap", []):
                self.padroes.append((re.compile(regex_para_python(chave), flags), troca))
        elif self.tipo == "occurrence":
            self.maximo = int(d["max"])
            self.token = re.compile(regex_para_python(d["token"]))
        else:
            raise ValueError(f"{arquivo}: tipo {self.tipo} sem suporte")

    def formatar(self, encontrado, troca=None):
        msg = self.mensagem
        if troca is not None:
            msg = msg.replace("%[1]s", troca).replace("%[2]s", encontrado)
            return msg.replace("%s", troca, 1).replace("%s", encontrado, 1)
        return msg.replace("%s", encontrado, 1)


def definir_regras(pasta):
    """--regras: aceita a pasta PTSBR ou a pasta do StylesPath que contém PTSBR."""
    global REGRAS_DIR, ESTILOS, TESTES_DIR
    pasta = pathlib.Path(pasta).resolve()
    if (pasta / "PTSBR").is_dir():
        pasta = pasta / "PTSBR"
    if not any(pasta.glob("*.yml")):
        sys.exit(f"Erro: a pasta {pasta} não tem arquivos .yml de regras.")
    REGRAS_DIR, ESTILOS = pasta, pasta.parent
    if (ESTILOS / "testes").is_dir():
        TESTES_DIR = ESTILOS / "testes"


def carregar_regras():
    return {r.nome: r for r in (Regra(p) for p in sorted(REGRAS_DIR.glob("*.yml")))}


# Regras que valem apenas num modo: Mensagens (R10.5, R10.7, R10.8) apenas com --mensagens.
REGRAS_DE_MODO = {"Mensagens"}
NIVEIS = {"suggestion": 0, "warning": 1, "error": 2}


def ativas_padrao(regras):
    """{nome: nível} das regras de um arquivo Markdown sem --config (igual ao .vale.ini da versão)."""
    return {n: r.nivel for n, r in regras.items() if n not in REGRAS_DE_MODO}


# ---------------------------------------------------------------- --config (.vale.ini)

def glob_para_regex(glob):
    """Glob de seção do .vale.ini: {a,b}, **/ (0 ou mais pastas), * e ? (sem /)."""
    saida, i = "", 0
    while i < len(glob):
        if glob.startswith("**/", i):
            saida, i = saida + "(?:.*/)?", i + 3
        elif glob.startswith("**", i):
            saida, i = saida + ".*", i + 2
        elif glob[i] == "{":
            j = glob.index("}", i)
            saida += "(?:" + "|".join(glob_para_regex(x).pattern[:-2] for x in glob[i + 1:j].split(",")) + ")"
            i = j + 1
        elif glob[i] == "*":
            saida, i = saida + "[^/]*", i + 1
        elif glob[i] == "?":
            saida, i = saida + "[^/]", i + 1
        else:
            saida, i = saida + re.escape(glob[i]), i + 1
    return re.compile(saida + r"\Z")


def glob_vale(glob, relativo):
    """Um glob sem "/" ("*.md") vale para o nome do arquivo em qualquer pasta."""
    rx = glob_para_regex(glob)
    if "/" not in glob:
        return bool(rx.match(relativo.rsplit("/", 1)[-1]))
    return bool(rx.match(relativo))


class ConfigVale:
    """--config: lê um .vale.ini como o Vale.

    Lê MinAlertLevel e StylesPath (em relação ao arquivo), as seções [glob], BasedOnStyles e
    PTSBR.<Regra> = YES | NO | suggestion | warning | error. O caminho de cada arquivo é
    comparado em relação à pasta do .vale.ini, também com um caminho absoluto.
    """

    def __init__(self, caminho):
        self.caminho = pathlib.Path(caminho).resolve()
        if not self.caminho.exists():
            sys.exit(f"Erro: o arquivo de configuração {caminho} não existe.")
        self.pasta = self.caminho.parent
        self.min_nivel = "suggestion"
        self.styles_path = None
        self.secoes = []
        secao = None
        for linha in self.caminho.read_text(encoding="utf-8").splitlines():
            linha = linha.strip()
            if not linha or linha.startswith(("#", ";")):
                continue
            m = re.match(r"^\[(.+)\]$", linha)
            if m:
                secao = (m.group(1), {"estilos": None, "regras": {}})
                self.secoes.append(secao)
                continue
            chave, _, valor = linha.partition("=")
            chave, valor = chave.strip(), valor.strip()
            if secao is None:
                if chave == "MinAlertLevel":
                    self.min_nivel = valor.lower()
                elif chave == "StylesPath":
                    self.styles_path = (self.pasta / valor).resolve()
            elif chave == "BasedOnStyles":
                secao[1]["estilos"] = {e.strip() for e in valor.split(",") if e.strip()}
            elif chave.startswith("PTSBR."):
                secao[1]["regras"][chave[len("PTSBR."):]] = valor

    def relativo(self, caminho):
        absoluto = pathlib.Path(caminho).resolve()
        try:
            return absoluto.relative_to(self.pasta).as_posix()
        except ValueError:
            return pathlib.Path(caminho).as_posix().removeprefix("./")

    def ativas(self, caminho, regras):
        """{nome: nível} das regras que valem para o arquivo, depois de MinAlertLevel."""
        relativo = self.relativo(caminho)
        niveis = {}
        for glob, dados in self.secoes:
            if not glob_vale(glob, relativo):
                continue
            if dados["estilos"] is not None and "PTSBR" in dados["estilos"]:
                for nome, regra in regras.items():
                    niveis.setdefault(nome, regra.nivel)
            for nome, valor in dados["regras"].items():
                if valor.upper() == "NO":
                    niveis[nome] = None
                elif valor.upper() == "YES":
                    niveis[nome] = regras[nome].nivel if nome in regras else None
                elif valor.lower() in NIVEIS:
                    niveis[nome] = valor.lower()
        minimo = NIVEIS.get(self.min_nivel, 0)
        return {n: v for n, v in niveis.items() if v and n in regras and NIVEIS[v] >= minimo}


# ---------------------------------------------------------------- Markdown -> blocos de texto

def limpar_inline(texto, spec):
    texto = re.sub(r"<!--.*?-->", " ", texto)
    texto = re.sub(r"`[^`]*`", "X", texto)                        # código em linha conta 1 palavra
    texto = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", texto)       # links e imagens
    texto = re.sub(r"<https?://[^>]*>|https?://\S+", " ", texto)   # URLs
    texto = re.sub(r"</?[a-zA-Z][^>]*>", " ", texto)               # tags HTML
    # Negrito curto (até 3 palavras) é um literal (R8.8): rótulo de interface ("**Salvar**"),
    # valor de estado da interface ("**Concluído**") ou palavra de sinalização. Conta 1 palavra.
    texto = re.sub(r"\*\*([^*\n]+?)\*\*|__([^_\n]+?)__",
                   lambda m: "X" if len((m.group(1) or m.group(2)).split()) <= 3 else m.group(0), texto)
    texto = texto.replace("**", "").replace("__", "")
    texto = re.sub(r"(?<![\w*])\*(?!\s)([^*]+)(?<!\s)\*(?![\w*])", r"\1", texto)
    if spec:
        # menção metalinguística: a palavra entre aspas quando o texto fala da palavra
        # Conta 1 palavra, como o código em linha, para a divisão de frases ficar correta.
        # Uma citação que termina com ponto também termina a frase.
        texto = re.sub(r"\"[^\"\n]*\"|“[^”\n]*”|‘[^’\n]*’",
                       lambda m: "X." if m.group(0)[-2:-1] in (".", "!", "?") else "X", texto)
    return texto


def blocos_markdown(texto, spec=False, nome=""):
    """Devolve blocos [texto, [(deslocamento, linha)], eh_passo, regras_desligadas, tipo]."""
    linhas = texto.splitlines()
    blocos, atual = [], None
    em_codigo = False
    cerca = ""
    pular_exemplo = False
    desligadas_global = set()
    tudo_desligado = False
    colunas_fora = set()
    secao_06 = None
    inicio = 0
    if linhas and linhas[0].strip() == "---":
        for j in range(1, len(linhas)):
            if linhas[j].strip() == "---":
                inicio = j + 1
                break

    def fechar():
        nonlocal atual
        if atual and atual[0].strip():
            blocos.append(atual)
        atual = None

    def novo(texto_linha, n, passo, tipo="texto"):
        nonlocal atual
        fechar()
        atual = [texto_linha, [(0, n)], passo, set(desligadas_global) | ({"*"} if tudo_desligado else set()), tipo]

    for idx in range(inicio, len(linhas)):
        n = idx + 1
        bruta = linhas[idx]
        corpo = bruta
        while True:  # tira os marcadores de citação
            m = re.match(r"^\s{0,3}>\s?", corpo)
            if not m:
                break
            corpo = corpo[m.end():]
        s = corpo.strip()

        # diretivas do Vale
        m = re.match(r"<!--\s*vale\s+(.*?)\s*-->", s)
        if m:
            arg = m.group(1)
            if arg == "off":
                tudo_desligado = True
            elif arg == "on":
                tudo_desligado = False
            else:
                for nome_regra, estado in re.findall(r"PTSBR\.(\w+)\s*=\s*(YES|NO)", arg):
                    (desligadas_global.add if estado == "NO" else desligadas_global.discard)(nome_regra)
            fechar()
            continue

        # blocos de código cercados
        if re.match(r"^(```|~~~)", s):
            if not em_codigo:
                em_codigo, cerca = True, s[:3]
            elif s.startswith(cerca):
                em_codigo = False
            fechar()
            continue
        if em_codigo:
            continue

        if spec and nome == "06-exemplos.md":
            if s.startswith("## "):
                secao_06 = "exemplo"
            elif s.startswith("### "):
                secao_06 = s[4:].strip()
            if secao_06 not in (None, "PTS-BR"):
                fechar()
                continue

        if spec:
            if re.search(r"N[ãa]o aprovad[oa]s?\s*:|^\*\*N[ãa]o aprovado", s) or re.match(r"^-?\s*\*\*N[ãa]o aprovado", s):
                pular_exemplo = True
                fechar()
                continue
            if pular_exemplo:
                if bruta.lstrip().startswith(">") or s == "":
                    fechar()
                    continue
                if re.match(r"^(-\s*)?\*\*|^#|^(-\s*)?(PTS-BR|Aprovado)\b", s):
                    pular_exemplo = False
                elif re.match(r"^\d+\.\s", s) or bruta.startswith("   "):
                    fechar()
                    continue
                else:
                    pular_exemplo = False

        if not s:
            fechar()
            continue

        # tabelas: cada célula é um bloco
        if s.startswith("|"):
            fechar()
            celulas = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in celulas if c):
                continue
            proxima = linhas[idx + 1].strip() if idx + 1 < len(linhas) else ""
            if re.match(r"^\|[-| :]+\|$", proxima):  # linha de cabeçalho
                colunas_fora = {i for i, c in enumerate(celulas)
                                if spec and any(k in c.lower() for k in COLUNAS_IGNORADAS)}
            for i, c in enumerate(celulas):
                if i in colunas_fora:
                    continue
                novo(limpar_inline(c, spec), n, False, "tabela")
                fechar()
            continue
        colunas_fora = set()

        if re.match(r"^#{1,6}\s", s):
            novo(limpar_inline(re.sub(r"^#+\s*", "", s), spec), n, False)
            fechar()
            continue
        if s in ("---", "***", "___"):
            fechar()
            continue

        m_item = re.match(r"^(\d+[.)]|[-*+])\s+", s)
        if m_item:
            passo = m_item.group(1)[0].isdigit()
            novo(limpar_inline(s[m_item.end():], spec), n, passo)
            continue
        texto_limpo = limpar_inline(s, spec)
        if atual is None:
            novo(texto_limpo, n, False)
        else:
            atual[1].append((len(atual[0]) + 1, n))
            atual[0] += "\n" + texto_limpo
    fechar()
    return blocos


def linha_de(mapa, pos):
    linha = mapa[0][1]
    for desloc, n in mapa:
        if desloc <= pos:
            linha = n
    return linha


FIM_FRASE = re.compile(r"(?<=[.!?])\s+(?=[\"“(*\[]?[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ0-9])|:\s*\n")


def verificar_texto(texto, regras, spec=False, nome="", limite="auto", ativas=None):
    """Alertas [(linha, regra, trecho, mensagem, nível)].

    ativas: {nome: nível} das regras do arquivo (padrão: ativas_padrao). limite "pasta": as
    regras de frase longa de ativas (--config). Os outros limites escolhem a regra de frase
    longa pelo tipo de frase (R4.2) ou para o arquivo inteiro.
    """
    ativas = ativas_padrao(regras) if ativas is None else ativas
    alertas = []
    for bloco, mapa, passo, desligadas, _ in blocos_markdown(texto, spec, nome):
        if "*" in desligadas:
            continue
        for regra in regras.values():
            if regra.nome in desligadas:
                continue
            if regra.tipo == "occurrence":
                proc = regra.nome == "FraseLongaProcedimento"
                if limite == "pasta":
                    nivel = ativas.get(regra.nome)
                    usar = nivel is not None
                else:  # o tipo de frase escolhe a regra; a configuração liga ou desliga R4.2
                    nivel = ativas.get(regra.nome) or ativas.get("FraseLonga") or ativas.get("FraseLongaProcedimento")
                    usar = nivel is not None and {"auto": proc == passo, "descritivo": not proc,
                                                  "procedimento": proc}[limite]
                if not usar:
                    continue
                pos = 0
                for frase in FIM_FRASE.split(bloco):
                    inicio = bloco.find(frase, pos)
                    pos = max(inicio, 0) + len(frase)
                    qtd = len(regra.token.findall(frase))
                    if qtd > regra.maximo:
                        alertas.append((linha_de(mapa, max(inicio, 0)), regra, f"{qtd} palavras",
                                        regra.mensagem, nivel))
                continue
            if regra.nome not in ativas:
                continue
            for padrao, troca in regra.padroes:
                for m in padrao.finditer(bloco):
                    alertas.append((linha_de(mapa, m.start()), regra, m.group(0).replace("\n", " "),
                                    regra.formatar(m.group(0).replace("\n", " "), troca), ativas[regra.nome]))
    alertas.sort(key=lambda a: (a[0], a[1].nome))
    return alertas


# ---------------------------------------------------------------- motor Vale (testes)

def vale_em_textos(textos, vale, limite="auto"):
    """Executa o Vale sobre {nome: texto}. Devolve {nome: [(linha, regra, trecho, mensagem)]}."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        for nome, texto in textos.items():
            (tmp / f"{nome}.md").write_text(texto, encoding="utf-8")
        ini = tmp / ".vale.ini"
        desligar = {"auto": "PTSBR.FraseLongaProcedimento = NO", "descritivo": "PTSBR.FraseLongaProcedimento = NO",
                    "procedimento": "PTSBR.FraseLonga = NO", "todas": "",
                    "mensagens": "PTSBR.FraseLongaProcedimento = NO"}[limite]
        if limite != "mensagens":  # a regra Mensagens vale apenas para mensagens de interface
            desligar += "\nPTSBR.Mensagens = NO"
        ini.write_text(f"StylesPath = {ESTILOS}\nMinAlertLevel = suggestion\nVocab = PTSBR\nIgnoredScopes = code, tt, strong\n\n"
                       f"[*.md]\nBasedOnStyles = PTSBR\n{desligar}\n", encoding="utf-8")
        r = subprocess.run([vale, "--config", str(ini), "--output", "JSON", "--no-exit", "."],
                           cwd=tmp, capture_output=True, text=True)
        if r.returncode != 0 and not r.stdout.strip():
            sys.exit(f"Erro do Vale: {r.stderr}")
        dados = json.loads(r.stdout or "{}")
    saida = {nome: [] for nome in textos}
    for caminho, lista in dados.items():
        nome = pathlib.Path(caminho).stem
        for a in lista:
            regra = a["Check"].split(".", 1)[1]
            saida[nome].append((a["Line"], regra, a.get("Match", ""), a["Message"]))
    return saida


# ---------------------------------------------------------------- modos

def secoes_06():
    """Extrai os textos 'Antes' e 'PTS-BR' de cada exemplo do 06."""
    if not (BASE / "06-exemplos.md").exists():  # repositório de equipe: sem o 06
        return {}
    texto = (BASE / "06-exemplos.md").read_text(encoding="utf-8")
    exemplos, ex, sec = {}, None, None
    for linha in texto.splitlines():
        if linha.startswith("## Exemplo"):
            ex = linha[3:].split(":")[0].strip().replace(" ", "")
            sec = None
            continue
        if linha.startswith("### "):
            sec = linha[4:].strip()
            continue
        if ex and sec in ("Antes", "PTS-BR"):
            exemplos.setdefault((ex, sec), []).append(re.sub(r"^\s{0,3}>\s?", "", linha))
    # Mensagens de interface entre crases (frase com maiúscula no início e ponto no fim)
    # são texto para o linter, como na extração dos arquivos de tradução (05, seção 6).
    mensagem = re.compile(r"`([A-ZÁÉÍÓÚÂÊÔÃÕÇ][^`]*[.!?])`")
    return {k: mensagem.sub(r"\1", "\n".join(v)) for k, v in exemplos.items()}


def casos_de_teste():
    """Lê tools/vale/testes/<Regra>/{deve_alertar,nao_deve_alertar}.md: um caso por linha.

    Um caso pode ter "\\n" para representar uma quebra de linha dentro do parágrafo.
    """
    casos = []
    for pasta in sorted(p for p in TESTES_DIR.iterdir() if p.is_dir()):
        for arquivo, esperado in (("deve_alertar.md", True), ("nao_deve_alertar.md", False)):
            caminho = pasta / arquivo
            if not caminho.exists():
                continue
            for n, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), 1):
                if linha.strip() and not linha.startswith(("#", "<!--")):
                    texto = linha.strip().replace("\\n", "\n")  # "\n" no caso = quebra de linha
                    casos.append((pasta.name, esperado, texto, f"{pasta.name}/{arquivo}:{n}"))
    return casos


def modo_teste(regras, motor, vale):
    casos = casos_de_teste()
    textos = {f"caso{i}": c[2] for i, c in enumerate(casos)}
    ex06 = secoes_06()
    for (ex, sec), t in ex06.items():
        textos[f"{ex}_{'antes' if sec == 'Antes' else 'ptsbr'}"] = t
    if motor == "vale":
        resultado = vale_em_textos(textos, vale)
        if any(c[0].startswith("FraseLongaProcedimento") for c in casos):
            proc = vale_em_textos({k: v for k, v in textos.items() if k.startswith("caso")}, vale, "procedimento")
            for k, v in proc.items():
                resultado[k] += [a for a in v if a[1] == "FraseLongaProcedimento"]
        de_modo = {f"caso{i}": c[2] for i, c in enumerate(casos) if c[0] in REGRAS_DE_MODO}
        if de_modo:
            for k, v in vale_em_textos(de_modo, vale, "mensagens").items():
                resultado[k] += [a for a in v if a[1] in REGRAS_DE_MODO]
    else:
        resultado = {}
        todas = {n: r.nivel for n, r in regras.items()}
        for k, t in textos.items():
            lim, ativas = "auto", None
            if k.startswith("caso"):
                regra_caso = casos[int(k[4:])][0]
                lim = "procedimento" if regra_caso == "FraseLongaProcedimento" else "descritivo"
                ativas = todas if regra_caso in REGRAS_DE_MODO else None
            resultado[k] = [(a[0], a[1].nome, a[2], a[3]) for a in verificar_texto(t, regras, limite=lim, ativas=ativas)]

    falhas = 0
    print(f"== Casos de teste das regras (motor: {motor}) ==")
    por_regra = {}
    for i, (regra, esperado, texto, origem) in enumerate(casos):
        alertou = any(a[1] == regra for a in resultado[f"caso{i}"])
        ok = alertou == esperado
        por_regra.setdefault(regra, [0, 0])[0 if ok else 1] += 1
        if not ok:
            falhas += 1
            print(f"  FALHA {origem}: {'deveria alertar' if esperado else 'alertou sem motivo'}: {texto}")
    for regra, (ok, ruim) in sorted(por_regra.items()):
        print(f"  {regra:<24} {ok} ok, {ruim} falha(s)")

    print(f"\n== 06-exemplos.md: textos 'Antes' (precisam de alertas) e 'PTS-BR' (zero ou quase zero) ==")
    total_antes = total_ptsbr = 0
    for ex in sorted({k[0] for k in ex06}, key=lambda x: int(re.sub(r"\D", "", x) or 0)):
        antes = resultado.get(f"{ex}_antes", [])
        ptsbr = resultado.get(f"{ex}_ptsbr", [])
        total_antes += len(antes)
        total_ptsbr += len(ptsbr)
        if not antes:
            falhas += 1
        print(f"  {ex}: Antes {len(antes)} alerta(s){'  <- FALHA' if not antes else ''}; PTS-BR {len(ptsbr)} alerta(s)")
        for a in ptsbr:
            print(f"      PTS-BR linha {a[0]}: {a[1]}: {a[2]}")
    print(f"\n  Total: Antes {total_antes}; PTS-BR {total_ptsbr} (cada alerta PTS-BR é um falso positivo ou um desvio real do 06).")
    print(f"\nResultado: {'OK' if falhas == 0 else f'{falhas} falha(s)'}")
    return 1 if falhas else 0


# Regras que contam palavras não aprovadas (M2, 05 seção 5.4).
REGRAS_M2 = ("PalavrasNaoAprovadas", "Haver", "GlossarioProjeto")


def metricas(texto, regras, limite="auto", ativas=None, lexico=None, nome=""):
    """Calcula M1 e M2 (05, seção 5) de um texto. Não conta tabelas nem código.

    M2: as palavras candidatas, cada uma 1 vez. Uma palavra que o linter (PalavrasNaoAprovadas,
    Haver, GlossarioProjeto) e a lista branca mostram na mesma linha conta 1 vez. Uma forma de
    um tempo verbal não aprovado de um verbo aprovado é um desvio de R3.1 (CK-3.1) e fica fora
    de M2. O revisor confirma as candidatas: M2 = candidatas confirmadas ÷ palavras × 1 000.
    """
    ativas = ativas_padrao(regras) if ativas is None else ativas
    token = regras["FraseLonga"].token
    palavras = frases = acima = 0
    for bloco, _, passo, _, tipo in blocos_markdown(texto):
        if tipo == "tabela":
            continue
        if limite == "pasta":
            procedimento = "FraseLongaProcedimento" in ativas
        else:
            procedimento = limite == "procedimento" or (limite == "auto" and passo)
        maximo = 20 if procedimento else 25
        for frase in FIM_FRASE.split(bloco):
            n = len(token.findall(frase))
            if n == 0:
                continue
            frases += 1
            palavras += n
            acima += n > maximo
    alertas = verificar_texto(texto, regras, limite=limite, ativas=ativas)
    por_regra = {}
    for a in alertas:
        por_regra[a[1].nome] = por_regra.get(a[1].nome, 0) + 1
    # M2 não conta as tabelas (seção 5.1): as linhas de tabela ficam vazias, com o mesmo número.
    texto = re.sub(r"(?m)^\s*\|.*$", "", texto)
    alertas = verificar_texto(texto, regras, limite=limite, ativas=ativas)
    do_linter = [a for a in alertas if a[1].nome in REGRAS_M2]
    cobertas = {(a[0], t) for a in do_linter for t in lista_branca.TOKEN.findall(a[2].lower())}
    da_lista, tempos = [], []
    if lexico is not None:
        _, fora, _ = palavras_fora(texto, nome, lexico, spec=False)
        for palavra, linha in fora:
            if (linha, palavra) in cobertas:
                continue
            (tempos if lexico.tempo_nao_aprovado(palavra) else da_lista).append((palavra, linha))
    candidatas = len(do_linter) + len(da_lista)
    return {
        "palavras": palavras,
        "frases": frases,
        "frases_acima_do_limite": acima,
        "M1_frases_dentro_do_limite_pct": round(100 * (frases - acima) / frases, 1) if frases else None,
        "M2_candidatas": candidatas,
        "M2_candidatas_por_1000_palavras": round(1000 * candidatas / palavras, 2) if palavras else None,
        "M2_candidatas_linter": [f"{a[0]}: {a[2]}" for a in do_linter],
        "M2_candidatas_lista_branca": [f"{linha}: {p}" for p, linha in da_lista],
        "tempos_verbais_fora_de_M2": [f"{linha}: {p}" for p, linha in tempos],
        "alertas_por_1000_palavras": round(1000 * len(alertas) / palavras, 2) if palavras else None,
        "alertas_por_regra": dict(sorted(por_regra.items())),
    }


def decimal(valor):
    """Número com a vírgula decimal (R8.4)."""
    return "—" if valor is None else f"{valor:.1f}".replace(".", ",")


# Nome de arquivo fora do formato de código ("05-governanca.md"): um literal (NT-04).
ARQUIVO_NOME = re.compile(r"(?<![\w/.-])[\w./-]+\.(?:md|yml|yaml|txt|py|ini|json|zip|csv|html)(?![\w])")


def texto_lista_branca(texto, nome):
    """No 03, a primeira célula de uma entrada "Não aprovada" é uma menção, e o código da classe é um literal."""
    if nome == "03-dicionario.md":
        texto = re.sub(r"(?m)^\| [^|]+? \| Não aprovada \|", "| X | X |", texto)
        texto = re.sub(r"\((?:v|s|adj|adv|prep|conj|pron|art|num|loc|abrev)\)", " ", texto)
    return texto


def palavras_fora(texto, nome, lexico, spec, nomes_vistos=None):
    """Lista branca de 1 texto: (total, [(palavra em minúsculas, linha)], nomes próprios).

    Um nome próprio no início da frase é aceito se o mesmo nome aparece com maiúscula no meio
    de outra frase (nomes_vistos; padrão: os nomes do próprio texto).
    """
    texto = ARQUIVO_NOME.sub("X", texto_lista_branca(texto, nome))
    blocos = [(b[0], b[1]) for b in blocos_markdown(texto, spec, nome) if "*" not in b[3]]
    total, fora, nomes = lista_branca.verificar_blocos(blocos, lexico, lista_branca.siglas_definidas(texto))
    vistos = {n for n, _ in nomes} if nomes_vistos is None else nomes_vistos
    fora_reais = [(p.lower(), linha) for p, linha, inicio in fora if not (inicio and p in vistos)]
    return total, fora_reais, len(nomes) + len(fora) - len(fora_reais)


def modo_lista_branca(arquivos, args):
    lexico = lista_branca.Lexico(dicionario=args.dicionario, termos=args.termos, spec=args.spec,
                                 glossario=args.glossario)
    por_arquivo, palavras, nomes_total = {}, {}, 0
    textos = []
    for caminho in arquivos:
        absoluto = caminho.resolve()
        nome = str(absoluto.relative_to(BASE)) if absoluto.is_relative_to(BASE) else str(caminho)
        textos.append((nome, caminho.name, caminho.read_text(encoding="utf-8")))
    # Um nome próprio no início da frase: o mesmo nome aparece com maiúscula no meio de outra frase.
    nomes_vistos = set()
    for _, nome_arquivo, texto in textos:
        texto = ARQUIVO_NOME.sub("X", texto_lista_branca(texto, nome_arquivo))
        blocos = [(b[0], b[1]) for b in blocos_markdown(texto, args.spec, nome_arquivo) if "*" not in b[3]]
        nomes_vistos |= {n for n, _ in lista_branca.verificar_blocos(blocos, lexico)[2]}
    for nome, nome_arquivo, texto in textos:
        total, fora_reais, n_nomes = palavras_fora(texto, nome_arquivo, lexico, args.spec, nomes_vistos)
        por_arquivo[nome] = {"palavras": total, "fora": len(fora_reais), "nomes_proprios": n_nomes,
                             "pct_fora": round(100 * len(fora_reais) / total, 2) if total else 0.0}
        nomes_total += n_nomes
        for palavra, linha in fora_reais:
            palavras.setdefault(palavra, []).append(f"{nome}:{linha}")
    total = sum(v["palavras"] for v in por_arquivo.values())
    n_fora = sum(v["fora"] for v in por_arquivo.values())
    pct = round(100 * n_fora / total, 2) if total else 0.0
    if not args.resumo:
        print("== Palavras fora da lista branca (frequência e locais) ==")
        for palavra, locais in sorted(palavras.items(), key=lambda x: (-len(x[1]), x[0])):
            mostrar = locais if args.locais == 0 else locais[:args.locais]
            resto = len(locais) - len(mostrar)
            print(f"  {palavra:<22} {len(locais):>4}  {', '.join(mostrar)}{f' (+{resto})' if resto else ''}")
        print()
    print("== Resumo por arquivo ==")
    for nome, v in por_arquivo.items():
        print(f"  {nome}: {v['palavras']} palavras, {v['fora']} fora ({v['pct_fora']:.2f}%), "
              f"{v['nomes_proprios']} nomes próprios (NT-01)")
    print(f"\nTotal: {total} palavras, {n_fora} fora da lista branca ({pct:.2f}%), "
          f"{len(palavras)} palavras diferentes; {nomes_total} nomes próprios aceitos (NT-01).")
    print("A lista branca verifica a forma da palavra, não o significado. O revisor verifica o "
          "significado (05, item CK-1.2).")
    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(
            {"arquivos": por_arquivo, "total": total, "fora": n_fora, "pct_fora": pct,
             "palavras": {p: l for p, l in sorted(palavras.items(), key=lambda x: -len(x[1]))}},
            ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if args.meta is not None and pct > args.meta else 0


# ---------------------------------------------------------------- --glossario

def regra_glossario(glossario):
    """Regra em memória: os sinônimos não aprovados do glossário do projeto (04, seção 7)."""
    swap = []
    for termo, sinonimos in glossario:
        for sinonimo in sinonimos:
            formas = sorted({sinonimo, sinonimo + "s"} if " " not in sinonimo else {sinonimo}, key=len, reverse=True)
            corpo = "|".join(r"\s+".join(re.escape(p) for p in f.split()) for f in formas)
            swap.append((r"(?<![\p{L}-])(?:" + corpo + r")(?![\p{L}-])", termo))
    if not swap:
        return None
    return Regra(nome="GlossarioProjeto", dados={
        "extends": "substitution", "level": "warning", "ignorecase": "true", "swap": swap,
        "message": "R1.1: '%[2]s' não é aprovado no glossário do projeto. Use '%[1]s'."})


# ---------------------------------------------------------------- --mensagens

def mensagens_json(texto):
    """[(chave, None, mensagem)] de um JSON plano ou aninhado. A chave junta os níveis com "."."""
    saida = []

    def visitar(valor, chave):
        if isinstance(valor, dict):
            for k, v in valor.items():
                visitar(v, f"{chave}.{k}" if chave else str(k))
        elif isinstance(valor, list):
            for i, v in enumerate(valor):
                visitar(v, f"{chave}[{i}]")
        elif isinstance(valor, str) and valor.strip():
            saida.append((chave, None, valor))
    visitar(json.loads(texto), "")
    return saida


def mensagens_po(texto):
    """[(chave, linha, mensagem)] de um arquivo .po ou .pot (gettext).

    O texto é o msgstr (ou cada msgstr[n] do plural). Se o msgstr estiver vazio, o texto é o
    msgid (e o msgid_plural): um arquivo .pot ou um projeto com as mensagens fonte em português.
    """
    def literal(resto):
        m = re.match(r'^"(.*)"\s*$', resto.strip())
        if not m:
            return ""
        return m.group(1).replace('\\"', '"').replace("\\n", " ").replace("\\t", " ").replace("\\\\", "\\")

    entradas, atual, campo = [], None, None
    for n, linha in enumerate(texto.splitlines(), 1):
        s = linha.strip()
        if not s or s.startswith("#"):
            if atual and s == "":
                entradas.append(atual)
                atual, campo = None, None
            continue
        m = re.match(r"^(msgctxt|msgid_plural|msgid|msgstr(?:\[\d+\])?)\s+(.*)$", s)
        if m:
            if m.group(1) in ("msgctxt", "msgid") and atual and "msgid" in atual and \
                    (m.group(1) == "msgctxt" or "msgstr" in "".join(atual)):
                entradas.append(atual)
                atual = None
            atual = atual or {"linha": n}
            campo = m.group(1)
            atual[campo] = literal(m.group(2))
        elif s.startswith('"') and atual is not None and campo:
            atual[campo] += literal(s)
    if atual:
        entradas.append(atual)
    saida = []
    for e in entradas:
        msgid = e.get("msgid", "")
        if not msgid:  # cabeçalho do arquivo
            continue
        chave = (e["msgctxt"] + " | " if e.get("msgctxt") else "") + f'msgid "{msgid[:40]}"'
        traducoes = [v for k, v in sorted(e.items()) if k.startswith("msgstr") and v.strip()]
        textos = traducoes or [msgid] + ([e["msgid_plural"]] if e.get("msgid_plural") else [])
        for t in textos:
            saida.append((chave, e["linha"], t))
    return saida


def extrair_mensagens(caminho):
    texto = caminho.read_text(encoding="utf-8")
    if caminho.suffix.lower() == ".json":
        return mensagens_json(texto)
    if caminho.suffix.lower() in (".po", ".pot"):
        return mensagens_po(texto)
    sys.exit(f"Erro: --mensagens lê arquivos .json, .po e .pot. Arquivo: {caminho}")


def verificar_mensagens(caminho, regras, glossario_regra=None):
    """Alertas das mensagens de um arquivo de tradução: [(chave, linha, regra, trecho, mensagem, nível)].

    Cada mensagem é 1 parágrafo. As regras são as regras do Markdown mais a regra Mensagens
    (R10.5, R10.7, R10.8). O limite de frase é o limite do texto descritivo (25 palavras).
    """
    ativas = {n: r.nivel for n, r in regras.items()}
    saida = []
    for chave, linha, mensagem in extrair_mensagens(caminho):
        texto = " ".join(mensagem.split())
        # Um texto que parece um item de lista ou um título ("- ", "1. ", "#") é texto da mensagem.
        texto = re.sub(r"^(\d+[.)]|[-*+#]+)(\s)", r"\1​\2", texto)
        for a in verificar_texto(texto, regras, limite="descritivo", ativas=ativas):
            saida.append((chave, linha, a[1], a[2], a[3], a[4]))
    return saida


# ---------------------------------------------------------------- testes das opções de equipe

def testar_opcoes(regras):
    """Testes de --config, --glossario, --mensagens e da contagem de M2."""
    falhas, total = 0, 0

    def confere(nome, obtido, esperado):
        nonlocal falhas, total
        total += 1
        if obtido != esperado:
            falhas += 1
            print(f"  FALHA {nome}: esperado {esperado!r}, obtido {obtido!r}")

    longa = " ".join(["palavra"] * 22) + "."  # 22 palavras: alerta com o limite de 20, não com 25
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        (tmp / "docs" / "ops" / "sub").mkdir(parents=True)
        (tmp / ".vale.ini").write_text(
            f"StylesPath = {REGRAS_DIR.parent}\nMinAlertLevel = suggestion\n\n[*.md]\nBasedOnStyles = PTSBR\n"
            "PTSBR.FraseLongaProcedimento = NO\nPTSBR.Mensagens = NO\n\n[docs/ops/**/*.md]\n"
            "PTSBR.FraseLonga = NO\nPTSBR.FraseLongaProcedimento = YES\n\n[docs/sem/*.md]\nPTSBR.Haver = NO\n",
            encoding="utf-8")
        config = ConfigVale(tmp / ".vale.ini")

        def frase_longa(caminho):
            ativas = config.ativas(caminho, regras)
            return any(a[1].tipo == "occurrence" for a in verificar_texto(longa, regras, limite="pasta", ativas=ativas))
        confere("--config: arquivo direto na pasta de procedimentos", frase_longa(tmp / "docs/ops/x.md"), True)
        confere("--config: arquivo numa subpasta", frase_longa(tmp / "docs/ops/sub/y.md"), True)
        confere("--config: caminho absoluto", frase_longa((tmp / "docs/ops/x.md").resolve()), True)
        confere("--config: arquivo fora da pasta", frase_longa(tmp / "docs/z.md"), False)
        confere("--config: PTSBR.Haver = NO", "Haver" in config.ativas(tmp / "docs/sem/a.md", regras), False)
        confere("--config: Mensagens desligada no Markdown", "Mensagens" in config.ativas(tmp / "a.md", regras), False)
        (tmp / ".vale.ini").write_text("MinAlertLevel = error\n\n[*.md]\nBasedOnStyles = PTSBR\n", encoding="utf-8")
        confere("--config: MinAlertLevel = error", ConfigVale(tmp / ".vale.ini").ativas(tmp / "a.md", regras), {})

        (tmp / "glossario.md").write_text(
            "| Termo | Gênero | Categoria | Definição | Sinônimos não aprovados |\n|---|---|---|---|---|\n"
            "| serviço de cobrança | o | NT-02 | Serviço que calcula o pagamento. | billing, módulo financeiro |\n",
            encoding="utf-8")
        glossario = lista_branca.ler_glossario(tmp / "glossario.md")
        regra = regra_glossario(glossario)
        com_glossario = dict(regras, GlossarioProjeto=regra)
        alertas = verificar_texto("Reinicie o billing. Abra o módulo financeiro.", com_glossario)
        confere("--glossario: sinônimos não aprovados", sum(a[1].nome == "GlossarioProjeto" for a in alertas), 2)
        lexico = lista_branca.Lexico(spec=False, glossario=tmp / "glossario.md")
        _, fora, _ = lista_branca.verificar_blocos([("Reinicie o serviço de cobrança.", [(0, 1)])], lexico)
        confere("--glossario: termo na lista branca", [f[0] for f in fora], [])

        (tmp / "pt-BR.json").write_text(json.dumps(
            {"arquivo": {"salvo": "Arquivo salvo com sucesso!", "excluido": "{0} arquivo(s) excluído(s)."},
             "erro": "O painel não está disponível. Atualize a página."}, ensure_ascii=False), encoding="utf-8")
        alertas = verificar_mensagens(tmp / "pt-BR.json", regras)
        confere("--mensagens JSON: chaves com alerta", sorted({a[0] for a in alertas if a[2].nome == "Mensagens"}),
                ["arquivo.excluido", "arquivo.salvo"])
        (tmp / "pt_BR.po").write_text(
            'msgid ""\nmsgstr ""\n"Plural-Forms: nplurals=2; plural=(n > 1);\\n"\n\n'
            '#: app.py:10\nmsgid "File saved."\nmsgstr "Arquivo salvo."\n\n'
            'msgid "Unknown error"\nmsgstr ""\n"Erro desconhecido."\n\n'
            'msgid "%s file deleted"\nmsgid_plural "%s files deleted"\nmsgstr[0] "%s arquivo excluído."\n'
            'msgstr[1] "%s arquivos excluídos."\n', encoding="utf-8")
        mensagens = mensagens_po((tmp / "pt_BR.po").read_text(encoding="utf-8"))
        confere("--mensagens .po: mensagens extraídas", [m[2] for m in mensagens],
                ["Arquivo salvo.", "Erro desconhecido.", "%s arquivo excluído.", "%s arquivos excluídos."])
        alertas = verificar_mensagens(tmp / "pt_BR.po", regras)
        confere("--mensagens .po: linhas com alerta", sorted({a[1] for a in alertas if a[2].nome == "Mensagens"}), [9, 13])

    lexico = lista_branca.Lexico(spec=False)
    m = metricas("Há 3 erros no log. O sistema enviava o e-mail.\n", regras, lexico=lexico)
    confere("--metricas: M2 conta 'há' 1 vez e não conta o tempo verbal", (m["M2_candidatas"], len(m["tempos_verbais_fora_de_M2"])), (1, 1))
    print(f"  {'OpcoesEquipe':<24} {total - falhas} ok, {falhas} falha(s)")
    return falhas


def imprimir(arquivo, alertas, resumo, filtro):
    alertas = [a for a in alertas if not filtro or a[1].nome == filtro]
    if resumo:
        cont = {}
        for a in alertas:
            cont[a[1].nome] = cont.get(a[1].nome, 0) + 1
        detalhes = ", ".join(f"{k} {v}" for k, v in sorted(cont.items()))
        print(f"{arquivo}: {len(alertas)} alerta(s){': ' + detalhes if detalhes else ''}")
    else:
        for linha, regra, trecho, msg, nivel in alertas:
            print(f"{arquivo}:{linha}: [{nivel}] PTSBR.{regra.nome}: {msg}")
    return alertas


def main():
    ap = argparse.ArgumentParser(description="Linter PTS-BR em Python (mesmas regras do Vale).")
    ap.add_argument("arquivos", nargs="*")
    ap.add_argument("--spec", action="store_true")
    ap.add_argument("--teste", action="store_true")
    ap.add_argument("--motor", choices=["python", "vale"], default="python")
    ap.add_argument("--vale", default=shutil.which("vale") or "vale")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("--regra")
    ap.add_argument("--limite-frase", choices=["auto", "descritivo", "procedimento", "pasta"], default="auto")
    ap.add_argument("--config", metavar="ARQUIVO")
    ap.add_argument("--falhar", action="store_true")
    ap.add_argument("--metricas", action="store_true")
    ap.add_argument("--json", metavar="ARQUIVO")
    ap.add_argument("--lista-branca", action="store_true")
    ap.add_argument("--regras", metavar="PASTA")
    ap.add_argument("--dicionario", metavar="ARQUIVO")
    ap.add_argument("--termos", metavar="ARQUIVO")
    ap.add_argument("--glossario", metavar="ARQUIVO")
    ap.add_argument("--mensagens", action="store_true")
    ap.add_argument("--meta", type=float, metavar="PCT")
    ap.add_argument("--locais", type=int, default=5, metavar="N")
    args = ap.parse_args()

    config = ConfigVale(args.config) if args.config else None
    if args.regras:
        definir_regras(args.regras)
    elif config and config.styles_path and (config.styles_path / "PTSBR").is_dir():
        definir_regras(config.styles_path)
    if config is None and args.limite_frase == "pasta":
        local = pathlib.Path(".vale.ini")
        config = ConfigVale(local if local.exists() else ESTILOS / ".vale.ini")
    regras = carregar_regras()
    glossario = lista_branca.ler_glossario(args.glossario) if args.glossario else []
    regra_gl = regra_glossario(glossario)
    if regra_gl:
        regras["GlossarioProjeto"] = regra_gl

    def ativas_de(caminho):
        ativas = config.ativas(caminho, regras) if config else ativas_padrao(regras)
        if regra_gl:
            ativas.setdefault("GlossarioProjeto", regra_gl.nivel)
        return ativas

    if args.teste:
        codigo = modo_teste(regras, args.motor, args.vale)
        if not args.regras:  # os testes da lista branca usam o 03 e o 04 da especificação
            print("\n== Lista branca (E1): frases conhecidas ==")
            codigo |= 1 if lista_branca.testar(lista_branca.Lexico(args.dicionario, args.termos, spec=False)) else 0
            print("\n== Opções de equipe: --config, --glossario, --mensagens, --metricas ==")
            codigo |= 1 if testar_opcoes(regras) else 0
        return codigo

    if args.spec and not args.arquivos:
        lista = ARQUIVOS_LISTA_BRANCA if args.lista_branca else ARQUIVOS_SPEC
        arquivos = [BASE / f for f in lista]
    else:
        arquivos = [pathlib.Path(a) for a in args.arquivos]
    if not arquivos:
        ap.print_help()
        return 2
    fora_da_spec = [str(c) for c in arquivos if args.spec and not c.resolve().is_relative_to(BASE)]
    if fora_da_spec:
        sys.exit("Erro: a isenção --spec vale apenas para o texto da própria especificação "
                 f"(01-introducao.md, seção 11.1). Remova --spec para: {', '.join(fora_da_spec)}")
    if args.lista_branca:
        return modo_lista_branca(arquivos, args)
    if args.mensagens:
        todos = []
        for caminho in arquivos:
            for chave, linha, regra, trecho, msg, nivel in verificar_mensagens(caminho, regras, regra_gl):
                if args.regra and regra.nome != args.regra:
                    continue
                local = f"{caminho}:{linha}" if linha else f"{caminho}"
                print(f"{local}: {chave}: [{nivel}] PTSBR.{regra.nome}: {msg}")
                todos.append(nivel)
        erros = sum(n == "error" for n in todos)
        print(f"\nTotal: {len(todos)} alerta(s), {erros} de nível error.")
        return 1 if erros or (args.falhar and todos) else 0
    if args.metricas:
        lexico = lista_branca.Lexico(dicionario=args.dicionario, termos=args.termos, spec=False,
                                     glossario=args.glossario)
        resultado = {str(c): metricas(c.read_text(encoding="utf-8"), regras, args.limite_frase, ativas_de(c),
                                      lexico, c.name)
                     for c in arquivos}
        for nome, m in resultado.items():
            print(f"{nome}: {m['palavras']} palavras, {m['frases']} frases, M1 {decimal(m['M1_frases_dentro_do_limite_pct'])}%, "
                  f"M2: {m['M2_candidatas']} palavras candidatas ({decimal(m['M2_candidatas_por_1000_palavras'])} "
                  f"por 1 000 palavras)")
            for local in m["M2_candidatas_linter"] + m["M2_candidatas_lista_branca"]:
                print(f"  candidata M2, linha {local}")
            for local in m["tempos_verbais_fora_de_M2"]:
                print(f"  tempo verbal (CK-3.1, fora de M2), linha {local}")
            print(f"  Registro: [METRICAS][palavras: {m['palavras']}][M1: {decimal(m['M1_frases_dentro_do_limite_pct'])}]"
                  f"[M2-candidatas: {m['M2_candidatas']}]")
        if args.json:
            pathlib.Path(args.json).write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
        return 0
    todos = []
    for caminho in arquivos:
        texto = caminho.read_text(encoding="utf-8")
        alertas = verificar_texto(texto, regras, spec=args.spec, nome=caminho.name,
                                  limite=args.limite_frase, ativas=ativas_de(caminho))
        absoluto = caminho.resolve()
        nome = absoluto.relative_to(BASE) if absoluto.is_relative_to(BASE) else caminho
        todos += imprimir(nome, alertas, args.resumo, args.regra)
    erros = [a for a in todos if a[4] == "error"]
    print(f"\nTotal: {len(todos)} alerta(s), {len(erros)} de nível error.")
    return 1 if erros or (args.falhar and todos) else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Gera a regra Vale de palavras não aprovadas (R1.1 e R1.7) a partir do 03 e do 04.

Fontes:
  - as linhas "Não aprovada" das tabelas do 03-dicionario.md. O 03 é gerado por
    tools/build.py a partir de tools/d*.txt;
  - a coluna "Não aprovado" da tabela de verbos com radical estrangeiro do
    04-termos-tecnicos.md, seção 5.4 (decisão E9): "deployar", "commitar", "mergear";
  - a coluna "Não aprovado" das siglas e dos termos não aprovados do 04, seção 6.3.
A cadeia completa é: d*.txt -> build.py --render -> 03-dicionario.md (+ 04) -> este
script -> tools/vale/PTSBR/PalavrasNaoAprovadas.yml.

Uma forma não aprovada que é igual a uma palavra aprovada do 03 ou a um termo de 1 palavra do
04 fica fora da regra. Exemplos: "seta" (forma de "setar", e SETA do 04, NT-06), "roda" (forma
de "rodar", e RODA do 04), "busca" (forma de "buscar", e BUSCA do 03). A lista branca
(tools/lista_branca.py) define as palavras aprovadas.

Palavras obsoletas: as entradas "Obsoleta" do 03 (05, seção 8.1) geram a regra
tools/vale/PTSBR/PalavrasObsoletas.yml, com o nível suggestion, e os casos de teste da regra em
tools/vale/testes/PalavrasObsoletas/. Sem entradas obsoletas, o script remove a regra e os testes.

Uso:
  python3 tools/gerar_regras_dicionario.py             # grava os arquivos YAML
  python3 tools/gerar_regras_dicionario.py --verificar # sai com 1 se um arquivo estiver desatualizado

O script usa apenas a biblioteca padrão do Python 3.9 ou mais nova.
"""
import pathlib
import re
import sys

import lista_branca

BASE = pathlib.Path(__file__).resolve().parent.parent
DICIONARIO = BASE / "03-dicionario.md"
TERMOS = BASE / "04-termos-tecnicos.md"
SAIDA = BASE / "tools" / "vale" / "PTSBR" / "PalavrasNaoAprovadas.yml"
SAIDA_OBSOLETAS = BASE / "tools" / "vale" / "PTSBR" / "PalavrasObsoletas.yml"
TESTES_OBSOLETAS = BASE / "tools" / "vale" / "testes" / "PalavrasObsoletas"
ACEITOS = BASE / "tools" / "vale" / "config" / "vocabularies" / "PTSBR" / "accept.txt"

L = r"\p{L}"
INICIO = r"(?<![\p{L}-])"
FIM = r"(?![\p{L}-])"

# Palavras que outra regra Vale cobre. O gerador não repete a palavra aqui.
COBERTAS = {
    "haver": "Haver.yml",
    "o mesmo": "OMesmo.yml",
}

# Padrões escritos à mão para palavras com homógrafo comum (falso positivo).
# Cada padrão já inclui os limites de palavra.
PADROES_MANUAIS = {
    # "logo" conjunção ("Logo, o serviço..."), não o substantivo ("o logo da empresa").
    "logo": INICIO + r"logo(?=\s*,)|(?<=,\s)logo" + FIM,
    # "caso" conjunção. Não alerta em "o caso", "neste caso", "caso de teste".
    "caso": INICIO + r"(?<!o\s)(?<!um\s)(?<!este\s)(?<!esse\s)(?<!cada\s)(?<!do\s)(?<!no\s)(?<!quer\s)caso" + FIM + r"(?!\s+de\s)",
    # "isto é" explicativo ("isto é, ..."). "Isto é obrigatório" é PTS-BR.
    "isto é": INICIO + r"isto\s+é(?=\s*,)|(?<=,\s)isto\s+é" + FIM,
    # Regra D11 do 03: "nós" depois de artigo, contração ou número é o plural de "nó".
    "nós": INICIO + r"(?<!os\s)(?<!\d\s)(?<!Plural:\s)nós" + FIM,
    # "status" em prosa é não aprovado (use "estado"). "código de status" é um nome técnico
    # do 04 (NT-08), e "página de status" também. Os rótulos de interface em negrito e os literais em código ficam fora
    # do texto que o linter lê (R8.8).
    "status": INICIO + r"(?<!código\sde\s)(?<!códigos\sde\s)(?<!página\sde\s)(?<!páginas\sde\s)status" + FIM,
}

# Formas geradas que coincidem com um substantivo comum de outro sentido. O gerador remove estas formas.
FORMAS_EXCLUIDAS = {"garantia", "garantias", "prova", "provas"}

# Formas irregulares ou com mudança de radical. Substituem as formas regulares.
IRREGULARES = {
    "cair": "cai caem caiu caíram caia caiam caindo caído caída caídos caídas cairá cairão",
    "conseguir": "consigo consegue conseguem consiga consigam conseguiu conseguiram conseguindo conseguido",
    "prosseguir": "prossigo prossegue prosseguem prossiga prossigam prosseguiu prosseguiram prosseguindo",
    "subir": "subo sobe sobem suba subam subiu subiram subindo subido subida",
    "sugerir": "sugiro sugere sugerem sugira sugiram sugeriu sugeriram sugerindo sugerido sugerida",
    "conferir": "confiro confere conferem confira confiram conferiu conferiram conferindo conferido",
    "inserir": "insiro insere inserem insira insiram inseriu inseriram inserindo inserido inserida",
    "requerer": "requeiro requer requerem requeira requeiram requereu requereram requerendo requerido requerida",
    "prover": "provejo provê proveem proveja provejam proveu proveram provendo provido provida",
    "descobrir": "descubro descobre descobrem descubra descubram descobriu descobriram descobrindo descoberto descoberta",
    "possuir": "possuo possui possuem possua possuam possuiu possuíram possuindo possuído",
    "incluir": "incluo inclui incluem inclua incluam incluiu incluíram incluindo incluído incluída incluídos incluídas",
    "concluir": "concluo conclui concluem conclua concluam concluiu concluíram concluindo concluído concluída",
    "produzir": "produzo produz produzem produza produzam produziu produziram produzindo produzido produzida",
    "reduzir": "reduzo reduz reduzem reduza reduzam reduziu reduziram reduzindo reduzido reduzida",
    "atingir": "atinjo atinge atingem atinja atinjam atingiu atingiram atingindo atingido",
    "exigir": "exijo exige exigem exija exijam exigiu exigiram exigindo exigido",
    "adquirir": "adquiro adquire adquirem adquira adquiram adquiriu adquiriram adquirindo adquirido",
    "interromper": "interrompe interrompem interrompa interrompam interrompeu interromperam interrompido interrompida",
}

# Locuções que começam com um verbo: formas do verbo inicial.
VERBO_LOC = {
    "fazer": "fazer faz fazem faça façam fez fizeram fazendo",
    "dar": "dar dá dão dê deem deu deram dando",
    "dispor": "dispor dispõe dispõem disponha disponham dispôs dispondo",
}

PRONOMES = {
    "esse": "esse essa esses essas desse dessa desses dessas nesse nessa nesses nessas",
    "isso": "isso disso nisso",
    "aquele": "aquele aquela aqueles aquelas daquele daquela daqueles daquelas naquele naquela naqueles naquelas àquele àquela",
    "aquilo": "aquilo daquilo naquilo àquilo",
    "ele": "ele ela eles elas nele nela neles nelas",
    "dele": "dele dela deles delas",
    "cujo": "cujo cuja cujos cujas",
    "o qual": "o qual,a qual,os quais,as quais,do qual,da qual,dos quais,das quais,no qual,na qual,nos quais,nas quais,pelo qual,pela qual",
    "tal": "tal tais",
    "diversos": "diversos diversas",
    "lhe": "lhe lhes",
    "o senhor": "o senhor,a senhora,os senhores,as senhoras",
}


OBSOLETAS = []  # [(palavra, classe, texto da coluna 3)] das entradas "Obsoleta" do 03


def ler_dicionario():
    """Lê as entradas do 03. Devolve (aprovadas, nao_aprovadas). Preenche OBSOLETAS."""
    aprovadas, nao = [], []
    OBSOLETAS.clear()
    padrao = re.compile(r"^\| (.+?) \((\w+)\) \| (Aprovada|Não aprovada|Obsoleta|Obsoleto) \| (.*?) \|")
    for linha in DICIONARIO.read_text(encoding="utf-8").splitlines():
        m = padrao.match(linha)
        if not m:
            continue
        palavra, classe, estado, alternativa = m.groups()
        if estado == "Aprovada":
            aprovadas.append((palavra.lower(), classe))
        elif estado.startswith("Obsolet"):
            aprovadas.append((palavra.lower(), classe))  # ainda aprovada até a próxima MAJOR
            OBSOLETAS.append((palavra.lower(), classe, alternativa.strip()))
        else:
            nao.append((palavra.lower(), classe, alternativa.strip()))
    return aprovadas, nao


# Coluna "Formas flexionadas não aprovadas" da tabela 5.4 do 04: formas que o 04 escreve.
FORMAS_04 = {}


def ler_termos_04():
    """Lê do 04 a tabela da seção 5.4 e a tabela da seção 6.3.

    Devolve [(termo, classe, alternativa)] no formato das entradas do 03: classe "v" para os
    verbos da 5.4, "loc" para as locuções ("dar push") e "s" para os termos da 6.3.
    """
    if not TERMOS.exists():
        return []
    entradas, secao = [], ""
    for linha in TERMOS.read_text(encoding="utf-8").splitlines():
        if linha.startswith("#"):
            secao = linha
            continue
        if not linha.startswith("|") or set(linha) <= set("|-: "):
            continue
        cel = [c.strip() for c in linha.strip().strip("|").split("|")]
        if cel[0].lower() in ("não aprovado", "termo em inglês"):
            continue
        if secao.startswith("### 5.4"):
            explicitas = {f.strip().lower() for f in cel[2].split(",") if f.strip()} if len(cel) > 2 else set()
            primeiro = cel[0].split(",")[0].strip().lower()
            FORMAS_04.setdefault(primeiro, set()).update(explicitas)
            frases = [f.strip().rstrip(".") for f in re.split(r"(?<=\.)\s+", cel[1]) if f.strip()]
            alternativa = "Use: " + "; ".join(re.sub(r"`[^`]*`", "", f).replace("  ", " ").strip() for f in frases)
            alternativa += " — 04-termos-tecnicos.md, seção 5.4"
            for termo in (t.strip().lower() for t in cel[0].split(",")):
                entradas.append((termo, "loc" if " " in termo else "v", alternativa))
        elif secao.startswith("### 6.3"):
            alternativa = f"Use: {cel[1]} — 04-termos-tecnicos.md, seção 6.3"
            for termo in (t.strip() for t in cel[0].split(",")):
                qualificador = re.search(r"\((.*?)\)", termo)
                nucleo = re.sub(r"\s*\(.*?\)", "", termo).strip()
                if qualificador and qualificador.group(1).startswith("de "):
                    # "função (de acesso)" -> "função de acesso"; "payload (de uma requisição HTTP)" ->
                    # "payload da requisição": apenas com o complemento, porque o termo sozinho tem
                    # outro uso aprovado.
                    resto = re.sub(r"^um[a]?\s+", "", qualificador.group(1)[3:]).split()[0].lower()
                    variantes = "|".join(f"{nucleo.lower()} {c} {resto}" for c in ("de", "da", "do", "de uma", "de um"))
                    entradas.append((variantes, "lista", alternativa))
                    continue
                if qualificador:
                    continue  # "status (em prosa)": o 03 já tem a entrada
                entradas.append((nucleo.lower(), "loc" if " " in nucleo else "s", alternativa))
    return entradas


def ortografia(radical, terminacao, desinencia):
    """Ajusta o radical antes de 'e' (verbos em -ar) ou de 'a'/'o' (-er/-ir)."""
    if terminacao == "ar" and desinencia[:1] in ("e", "é"):
        if radical.endswith("c"):
            return radical[:-1] + "qu"
        if radical.endswith("g"):
            return radical + "u"
        if radical.endswith("ç"):
            return radical[:-1] + "c"
    if terminacao in ("er", "ir") and desinencia[:1] in ("a", "o"):
        if radical.endswith("c"):
            return radical[:-1] + "ç"
        if radical.endswith("g"):
            return radical[:-1] + "j"
        if radical.endswith("gu"):
            return radical[:-1]
    return radical


# A 1ª pessoa do singular do presente ("-o") fica fora: o PTS-BR não usa "eu", e a
# forma coincide com substantivos aprovados ou técnicos ("endereço", "aviso", "retorno").
DESINENCIAS = {
    "ar": "as a amos am ei ou aste aram ava avam ávamos arei ará arão aremos aria ariam e es em emos ar armos arem ando ado ada ados adas",
    "er": "es e emos em i eu eram ia iam erei erá erão eremos eria eriam a as am amos er ermos erem endo ido ida idos idas",
    "ir": "es e imos em i iu iram ia iam irei irá irão iremos iria iriam a as am amos ir irmos irem indo ido ida idos idas",
}


def formas_verbo(infinitivo):
    pronominal = infinitivo.endswith("-se")
    base = infinitivo[:-3] if pronominal else infinitivo
    formas = {base}
    terminacao = base[-2:]
    if base in IRREGULARES:
        # A lista do verbo irregular substitui as formas regulares ("prover" -> "proveja", não "prova").
        formas |= set(IRREGULARES[base].split())
    elif terminacao in DESINENCIAS:
        radical = base[:-2]
        for d in DESINENCIAS[terminacao].split():
            formas.add(ortografia(radical, terminacao, d) + d)
        if terminacao == "ar" and radical.endswith("e"):
            # verbos em -ear: "mergear" -> "mergeia", "mergeie"; "rebasear" -> "rebaseie"
            formas |= {radical + d for d in ("io", "ia", "ias", "iam", "ie", "ies", "iem")}
    if pronominal:
        # "certifique-se", "certifica-se", "se certifique"
        return {f + "-se" for f in formas} | {"se " + f for f in formas}
    return formas


def formas_nome(palavra, classe):
    formas = {palavra}
    if classe not in ("s", "adj"):
        return formas
    if palavra.endswith("s"):
        return formas  # "status", "vírus": o plural é igual ao singular
    if palavra.endswith("ão"):
        formas.add(palavra[:-2] + "ões")
    elif palavra.endswith("ível"):
        formas.add(palavra[:-4] + "íveis")
    elif palavra.endswith("il"):  # "perfil" -> "perfis"
        formas.add(palavra[:-2] + "is")
    elif palavra.endswith("el"):  # "papel" -> "papéis"
        formas.add(palavra[:-2] + "éis")
    elif palavra.endswith("ol"):  # "farol" -> "faróis"
        formas.add(palavra[:-2] + "óis")
    elif palavra.endswith("l"):
        formas.add(palavra[:-1] + "is")
    elif palavra.endswith(("r", "z")):
        formas.add(palavra + "es")
    else:
        formas.add(palavra + "s")
    if classe == "adj" and palavra.endswith("o"):
        formas |= {palavra[:-1] + "a", palavra[:-1] + "as"}
    return formas


def formas_locucao(loc):
    """Variações de uma locução: verbo inicial, contração final ('de' -> 'do')."""
    palavras = loc.split()
    variantes = [palavras]
    if palavras[0] in VERBO_LOC:
        variantes = [[f] + palavras[1:] for f in VERBO_LOC[palavras[0]].split()]
    if palavras[0] == "relativo":
        variantes = [[f] + palavras[1:] for f in ("relativo", "relativa", "relativos", "relativas")]
    resultado = set()
    for v in variantes:
        ultima = v[-1]
        if ultima == "de" and len(v) > 1:
            for c in ("de", "do", "da", "dos", "das"):
                resultado.add(" ".join(v[:-1] + [c]))
        elif ultima == "a" and len(v) > 1:
            for c in ("a", "à", "ao", "aos", "às"):
                resultado.add(" ".join(v[:-1] + [c]))
        else:
            resultado.add(" ".join(v))
    return resultado


def formas(palavra, classe):
    if classe == "lista":  # variantes escritas por ler_termos_04(), separadas por "|"
        return set(palavra.split("|"))
    if palavra in PRONOMES:
        separador = "," if "," in PRONOMES[palavra] else " "
        return set(PRONOMES[palavra].split(separador))
    if " " in palavra:
        return formas_locucao(palavra)
    if classe == "v":
        return formas_verbo(palavra) | FORMAS_04.get(palavra, set())
    return formas_nome(palavra, classe)


def regex_forma(forma):
    partes = [re.escape(p).replace(r"\-", "-") for p in forma.split(" ")]
    return r"\s+".join(partes)


def ler_aceitos():
    if not ACEITOS.exists():
        return []
    linhas = ACEITOS.read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in linhas if l.strip() and not l.startswith("#")]


def excecoes_aceitas(formas_palavra, aceitos):
    """Gera lookbehind e lookahead para nomes próprios do accept.txt ('Time Machine').

    Devolve (antes, depois): o texto que entra antes e depois do grupo de formas.
    """
    antes_re, depois_re = "", ""
    for termo in aceitos:
        tokens = termo.split()
        for i, t in enumerate(tokens):
            if t.lower() in formas_palavra:
                if i > 0:
                    antes = r"\s".join(re.escape(x) for x in tokens[:i])
                    antes_re += r"(?<!" + antes + r"\s)"
                if i < len(tokens) - 1:
                    depois = r"\s+".join(re.escape(x) for x in tokens[i + 1:])
                    depois_re += r"(?!\s+" + depois + r")"
    return antes_re, depois_re


def alternativa_texto(alternativa):
    fonte = "04-termos-tecnicos.md" if "04-termos-tecnicos.md" in alternativa else "03-dicionario.md"
    if alternativa.startswith("Reescreva"):
        return f"uma reescrita da frase ({fonte})"  # a coluna do 03 começa com "Reescreva:"
    texto = alternativa.removeprefix("Use:").strip()
    texto = texto.split(" — ")[0]
    opcoes = [re.sub(r"\s*\(\w+\)", "", o).strip().lower() for o in texto.split(";")]
    return " ou ".join(f"'{o}'" for o in opcoes if o) + f" ({fonte})"


def formas_da_lista_branca():
    """Formas de 1 palavra aprovadas no 03 e no 04 (a lista branca, sem a metalinguagem), e os
    termos compostos aprovados ("roda do mouse", "tecla de seta")."""
    lexico = lista_branca.Lexico(dicionario=DICIONARIO, termos=TERMOS, spec=False)
    compostos = sorted({termo for lista in lexico.compostos.values() for _, termo, _ in lista})
    return set(lexico.origem), compostos


def gerar():
    aprovadas, nao = ler_dicionario()
    no_03 = {p for p, _, _ in nao}
    nao = nao + [e for e in ler_termos_04() if e[0] not in no_03]
    formas_aprovadas = set()
    for palavra, classe in aprovadas:
        if classe == "v":
            formas_aprovadas |= formas_verbo(palavra)
        elif " " not in palavra:
            formas_aprovadas |= formas_nome(palavra, classe)
    # Uma forma gerada igual a uma palavra aprovada do 03 ou do 04 fica fora ("seta"). Dentro de
    # um termo composto aprovado ("roda do mouse"), a forma não gera alerta (lookbehind e lookahead).
    de_1_palavra, compostos = formas_da_lista_branca()
    formas_aprovadas |= de_1_palavra
    aceitos = ler_aceitos() + compostos
    linhas = [
        "# R1.1 e R1.7 (Seção 1) — GERADO por tools/gerar_regras_dicionario.py. Não edite este arquivo.",
        "# Fontes: as entradas \"Não aprovada\" do 03-dicionario.md, as tabelas 5.4 e 6.3 do",
        "# 04-termos-tecnicos.md e o accept.txt.",
        f"# Entradas: {len(nao)}. Palavras que outra regra cobre: {', '.join(sorted(COBERTAS))}.",
        "extends: substitution",
        "message: \"R1.1: '%[2]s' não é aprovada. Use %[1]s.\"",
        "level: warning",
        "ignorecase: true",
        "nonword: true",
        "swap:",
    ]
    total = 0
    for palavra, classe, alternativa in sorted(nao):
        if palavra in COBERTAS:
            continue
        if palavra in PADROES_MANUAIS:
            padrao = PADROES_MANUAIS[palavra]
        else:
            fs = formas(palavra, classe)
            if " " not in palavra and classe != "lista":
                fs = {f for f in fs if (f == palavra or f not in formas_aprovadas) and f not in FORMAS_EXCLUIDAS}
            if not fs:
                continue
            corpo = "|".join(regex_forma(f) for f in sorted(fs, key=lambda x: (-len(x), x)))
            antes, depois = excecoes_aceitas(fs, aceitos)
            padrao = INICIO + antes + "(?:" + corpo + ")" + FIM + depois
        assert "'" not in padrao, palavra
        sugestao = alternativa_texto(alternativa).replace('"', "'")
        linhas.append(f"  '{padrao}': \"{sugestao}\"")
        total += 1
    return "\n".join(linhas) + "\n", total


def gerar_obsoletas():
    """PalavrasObsoletas.yml e os casos de teste. Devolve {caminho: conteúdo} ({} sem obsoletas)."""
    if not OBSOLETAS:
        return {}
    linhas = [
        "# R1.1 (Seção 1), palavras obsoletas — GERADO por tools/gerar_regras_dicionario.py. Não edite.",
        "# Fonte: as entradas \"Obsoleta\" do 03-dicionario.md (05-governanca.md, seção 8.1).",
        "# Uma palavra obsoleta continua aprovada até a próxima versão MAJOR. Nível: suggestion.",
        f"# Entradas: {len(OBSOLETAS)}.",
        "extends: substitution",
        "message: \"R1.1: '%[2]s' é obsoleta e sai do dicionário na próxima versão MAJOR. Use %[1]s.\"",
        "level: suggestion",
        "ignorecase: true",
        "nonword: true",
        "swap:",
    ]
    deve, nao_deve = ["# GERADO por tools/gerar_regras_dicionario.py. Uma forma de cada palavra obsoleta."], \
        ["# GERADO por tools/gerar_regras_dicionario.py. A palavra substituta de cada palavra obsoleta."]
    for palavra, classe, alternativa in sorted(OBSOLETAS):
        fs = formas(palavra, classe)
        corpo = "|".join(regex_forma(f) for f in sorted(fs, key=lambda x: (-len(x), x)))
        padrao = INICIO + "(?:" + corpo + ")" + FIM
        sugestao = alternativa_texto(alternativa).replace('"', "'")
        linhas.append(f"  '{padrao}': \"{sugestao}\"")
        deve.append(f"O texto usa a palavra {palavra}.")
        substituta = re.sub(r"\s*\(\w+\)", "", alternativa.removeprefix("Use:").split(" — ")[0].split(";")[0]).strip().lower()
        if substituta and substituta not in fs:
            nao_deve.append(f"O texto usa a palavra {substituta}.")
    return {SAIDA_OBSOLETAS: "\n".join(linhas) + "\n",
            TESTES_OBSOLETAS / "deve_alertar.md": "\n".join(deve) + "\n",
            TESTES_OBSOLETAS / "nao_deve_alertar.md": "\n".join(nao_deve) + "\n"}


def main():
    conteudo, total = gerar()
    obsoletas = gerar_obsoletas()
    arquivos = {SAIDA: conteudo, **obsoletas}
    remover = [] if obsoletas else [c for c in (SAIDA_OBSOLETAS, TESTES_OBSOLETAS / "deve_alertar.md",
                                                TESTES_OBSOLETAS / "nao_deve_alertar.md") if c.exists()]
    if "--verificar" in sys.argv:
        desatualizados = [c for c, t in arquivos.items()
                          if (c.read_text(encoding="utf-8") if c.exists() else "") != t] + remover
        if desatualizados:
            for c in desatualizados:
                print(f"DESATUALIZADO: {c.relative_to(BASE)}. Execute: python3 tools/gerar_regras_dicionario.py")
            return 1
        print(f"OK: {SAIDA.relative_to(BASE)} corresponde ao 03-dicionario.md e ao 04 ({total} entradas). "
              f"Palavras obsoletas: {len(OBSOLETAS)}.")
        return 0
    for caminho, texto in arquivos.items():
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(texto, encoding="utf-8")
        print(f"Gravado: {caminho.relative_to(BASE)}")
    for caminho in remover:
        caminho.unlink()
        print(f"Removido (sem palavras obsoletas no 03): {caminho.relative_to(BASE)}")
    if remover and TESTES_OBSOLETAS.exists() and not any(TESTES_OBSOLETAS.iterdir()):
        TESTES_OBSOLETAS.rmdir()
    print(f"{total} entradas de palavras não aprovadas. Palavras obsoletas: {len(OBSOLETAS)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

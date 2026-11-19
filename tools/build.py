"""Gera o 03-dicionario.md a partir de d1.txt, d2.txt, d3.txt e intro.md, e verifica as fontes.

Uso:
    python3 build.py                      # apenas verifica
    python3 build.py --render ../03-dicionario.md
    python3 build.py --lex                # mostra também as palavras dos exemplos sem entrada
    python3 build.py --teste              # testa as verificações do estado O (obsoleta) com linhas de teste

Formato de cada linha das fontes (6 campos separados por "|"):
    A|PALAVRA|classe|significado|exemplo PTS-BR|uso incorreto (Use: forma correta)
    N|palavra|classe|ALTERNATIVA (classe); OUTRA (classe) — comentário|exemplo PTS-BR|frase não aprovada
    O|PALAVRA|classe|SUBSTITUTA (classe) — exclusão na versão X.0.0. Comentário|exemplo PTS-BR com a substituta|frase com a palavra obsoleta

Estado O (obsoleta, 05-governanca.md, seção 8.1): uma palavra aprovada que a próxima versão MAJOR exclui.
A palavra fica em MAIÚSCULAS. A substituta é uma entrada aprovada. O comentário tem a versão da exclusão
("exclusão na versão 2.0.0"). O 03 mostra a decisão "Obsoleta" e a alternativa "Use: SUBSTITUTA (classe)".
Os exemplos PTS-BR das outras entradas não usam a palavra obsoleta.

O build falha (código de saída 1) se encontrar uma linha PROBLEM.
"""
import sys, re, unicodedata, collections, pathlib

base = pathlib.Path(__file__).parent
ROOT = base.parent
SOURCES = ["d1.txt", "d2.txt", "d3.txt", "d4.txt"]


def norm(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(ch) != "Mn")


def load_rows():
    rows, bad = [], []
    for f in SOURCES:
        for ln, line in enumerate((base / f).read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip() or line.startswith("#"):
                continue
            p = line.split("|")
            if len(p) != 6:
                bad.append(("BAD FIELDS", f, ln, line))
                continue
            if p[0] not in STATES:
                bad.append(("BAD STATE", f, ln, p[0]))
                continue
            rows.append(dict(st=p[0], w=p[1].strip(), c=p[2].strip(), m=p[3].strip(), ex=p[4].strip(),
                             bad=p[5].strip(), src=f"{f}:{ln}"))
    return rows, bad


# Estados de uma entrada: A (aprovada), N (não aprovada), O (obsoleta, 05-governanca.md, seção 8.1)
STATES = {"A": "Aprovada", "N": "Não aprovada", "O": "Obsoleta"}


# ---------------------------------------------------------------------------
# Morfologia: formas flexionadas das palavras aprovadas (para as verificações léxicas)
# ---------------------------------------------------------------------------
VOW = "aeiouáéíóúâêôãõ"

IRREG = {
    "ser": "é são foi foram for forem seja sejam sendo sido ser serem sou somos era eram",
    "estar": "está estão esteve estiveram estiver estiverem esteja estejam estando estado estar estarem estou",
    "ter": "tem têm teve tiveram tiver tiverem tenha tenham tendo tido ter terem tenho",
    "conter": "contém contêm conteve contiveram contiver contiverem contenha contenham contendo contido contida contidos contidas",
    "manter": "mantém mantêm manteve mantiveram mantiver mantiverem mantenha mantenham mantendo mantido mantida mantidos mantidas",
    "obter": "obtém obtêm obteve obtiveram obtiver obtiverem obtenha obtenham obtendo obtido obtida obtidos obtidas",
    "ir": "vai vão foi foram for forem vá vão indo ido ir irem vou",
    "fazer": "faz fazem fez fizeram fizer fizerem faça façam fazendo feito feita feitos feitas fazer fazerem",
    "desfazer": "desfaz desfazem desfez desfizeram desfizer desfizerem desfaça desfaçam desfeito desfeita",
    "poder": "pode podem pôde puderam puder puderem possa possam podendo podido",
    "dar": "dá dão deu deram der derem dê deem dando dado dada dados dadas",
    "ver": "vê veem viu viram vir virem veja vejam vendo visto vista vistos vistas",
    "saber": "sabe sabem soube souberam souber souberem saiba saibam sabendo sabido",
    "ler": "lê leem leu leram ler lerem leia leiam lendo lido lida lidos lidas",
    "pedir": "pede pedem pediu pediram pedir pedirem peça peçam pedindo pedido pedida",
    "medir": "mede medem mediu mediram medir medirem meça meçam medindo medido medida",
    "perder": "perde perdem perdeu perderam perder perderem perca percam perdendo perdido perdida perdidos perdidas",
    "seguir": "segue seguem seguiu seguiram seguir seguirem siga sigam seguindo seguido seguida",
    "sair": "sai saem saiu saíram sair saírem saia saiam saindo saído",
    "repetir": "repete repetem repetiu repetiram repetir repetirem repita repitam repetindo repetido repetida",
    "corrigir": "corrige corrigem corrigiu corrigiram corrigir corrigirem corrija corrijam corrigindo corrigido corrigida corrigidos corrigidas",
    "consumir": "consome consomem consumiu consumiram consumir consumirem consuma consumam consumindo consumido",
    "impedir": "impede impedem impediu impediram impedir impedirem impeça impeçam impedindo impedido impedida",
    "proteger": "protege protegem protegeu protegeram proteger protegerem proteja protejam protegendo protegido protegida protegidos protegidas",
    "escolher": "escolhe escolhem escolheu escolheram escolher escolherem escolha escolham escolhendo escolhido escolhida",
    "reproduzir": "reproduz reproduzem reproduziu reproduziram reproduzir reproduzirem reproduza reproduzam reproduzindo reproduzido",
    "transferir": "transfere transferem transferiu transferiram transferir transferirem transfira transfiram transferindo transferido transferida",
    "escrever": "escreve escrevem escreveu escreveram escrever escreverem escreva escrevam escrevendo escrito escrita escritos escritas",
    "descrever": "descreve descrevem descreveu descreveram descrever descreverem descreva descrevam descrevendo descrito descrita descritos descritas",
    "abrir": "abre abrem abriu abriram abrir abrirem abra abram abrindo aberto aberta abertos abertas",
    "imprimir": "imprime imprimem imprimiu imprimiram imprimir imprimirem imprima imprimam imprimindo impresso impressa imprimido",
    "dizer": "diz dizem disse disseram disser disserem diga digam dizendo dito dita",
    "vir": "vem vêm veio vieram vier vierem venha venham vindo",
    "pôr": "põe põem pôs puseram puser puserem ponha ponham pondo posto",
    "querer": "quer querem quis quiseram quiser quiserem queira queiram",
    "trazer": "traz trazem trouxe trouxeram trouxer trouxerem traga tragam trazendo trazido",
    "conhecer": "conhece conhecem conheceu conheceram conhecer conhecerem conheça conheçam conhecendo conhecido conhecida",
    "servir": "serve servem serviu serviram servir servirem sirva sirvam servindo servido",
    "preferir": "prefere preferem preferiu preferiram preferir preferirem prefira prefiram preferindo preferido",
    "sugerir": "sugere sugerem sugeriu sugeriram sugerir sugerirem sugira sugiram",
    "investir": "investe investem",
    "construir": "constrói constroem construiu construíram construir construírem construa construam construindo construído",
    "destruir": "destrói destroem destruiu destruíram destruir destruírem destrua destruam destruindo destruído",
    "requerer": "requer requerem",
    "valer": "vale valem valeu valeram valer valerem valha valham",
    "caber": "cabe cabem coube couberam couber couberem caiba caibam",
    "haver": "há houve houver haja",
    "dormir": "dorme dormem",
    "subir": "sobe sobem",
    "fugir": "foge fogem",
    "cobrir": "cobre cobrem coberto coberta",
    "descobrir": "descobre descobrem descoberto",
    "traduzir": "traduz traduzem traduziu traduziram traduzir traduzirem traduza traduzam traduzindo traduzido traduzida",
    "proibir": "proíbe proíbem proibiu proibiram proibir proibirem proíba proíbam proibindo proibido proibida proibidos proibidas",
    "prover": "provê proveem proveu proveram prover proverem proveja provejam provendo provido provida",
    "reunir": "reúne reúnem",
    "expor": "expõe expõem expôs expuseram expor exporem expuser expuserem exponha exponham expondo exposto exposta expostos expostas",
    "extrair": "extrai extraem extraiu extraíram extrair extraírem extraia extraiam extraindo extraído extraída extraídos extraídas",
    "reescrever": "reescreve reescrevem reescreveu reescreveram reescrever reescreverem reescreva reescrevam reescrevendo reescrito reescrita reescritos reescritas",
}


def verb_forms(v):
    v = v.lower()
    out = {v}
    if v in IRREG:
        out |= set(IRREG[v].split())
        if v not in ("ser", "estar", "ter", "ir", "fazer", "poder", "dar", "ver", "saber", "ler", "haver", "vir", "pôr", "querer", "dizer", "trazer", "caber", "valer"):
            pass
        else:
            return out
    # verbo pronominal ("conectar-se")
    if v.endswith("-se"):
        v = v[:-3]
        out.add(v)
    if len(v) < 3:
        return out
    st, t = v[:-2], v[-2:]
    if t == "ar":
        # radical do subjuntivo/imperativo
        if st.endswith("c"):
            sj = st[:-1] + "qu"
        elif st.endswith("g"):
            sj = st + "u"
        elif st.endswith("ç"):
            sj = st[:-1] + "c"
        else:
            sj = st
        suf = ["a", "am", "ou", "aram", "ar", "arem", "ado", "ada", "ados", "adas", "ando"]
        out |= {st + s for s in suf}
        out |= {sj + "e", sj + "em"}
        if st.endswith("e"):  # -ear: bloquear, renomear
            out |= {st + "ia", st + "iam", st + "ie", st + "iem"}
    elif t in ("er", "ir", "ôr"):
        if t == "ir" and st.endswith("u") and not st.endswith(("gu", "qu")):  # -uir: excluir, atribuir
            out |= {st + s for s in ["i", "em", "iu", "íram", "ir", "írem", "a", "am", "ído", "ída", "ídos", "ídas", "indo"]}
            return out
        if st.endswith("c"):
            sj = st[:-1] + "ç"
        elif st.endswith("g"):
            sj = st[:-1] + "j"
        elif st.endswith("gu"):
            sj = st[:-1]
        else:
            sj = st
        ve = "e" if t == "er" else "i"
        suf = ["e", "em", ve + "u", ve + "ram", t, t + "em", "ido", "ida", "idos", "idas", ve + "ndo"]
        out |= {st + s for s in suf}
        out |= {sj + "a", sj + "am"}
        if t == "ir":
            out |= {st + "iu", st + "iram"}
    return out


def nominal_forms(w, fem_ok=True):
    w = w.lower()
    out = {w}
    def plural(x):
        r = set()
        if x[-1] in "aeiouéóáíú" and not x.endswith("ão"):
            r.add(x + "s")
        if x.endswith("ão"):
            r |= {x[:-2] + "ões", x[:-2] + "ães", x + "s"}
        if x.endswith(("r", "z")):
            r.add(x + "es")
        if x.endswith("s"):
            r.add(x)
            if x.endswith("ês"):
                r.add(x[:-2] + "eses")
            r.add(x + "es")
        if x.endswith("al"):
            r.add(x[:-1] + "is")
        if x.endswith("el"):
            r.add(x[:-2] + "éis")
            r.add(x[:-2] + "eis")
        if x.endswith("ol"):
            r.add(x[:-2] + "óis")
        if x.endswith("ul"):
            r.add(x[:-1] + "is")
        if x.endswith("il"):
            r.add(x[:-2] + "is")
            r.add(x[:-2] + "eis")
        if x.endswith("m"):
            r.add(x[:-1] + "ns")
        if x.endswith("x"):
            r.add(x)
        if x[-1] not in VOW + "rzslmx":
            r.add(x + "s")
        # acento que cai no plural: "caractere", "mês", "ônibus"
        return r
    out |= plural(w)
    if not fem_ok:
        return out
    fem = set()
    if w.endswith("o"):
        fem.add(w[:-1] + "a")
    if w.endswith("ão"):
        fem |= {w[:-2] + "ã", w[:-2] + "ona"}
    if w.endswith("or"):
        fem.add(w + "a")
    if w.endswith("ês"):
        fem.add(w[:-2] + "esa")
    if w.endswith("um"):
        fem.add(w + "a")
    for f in fem:
        out.add(f)
        out |= plural(f)
    return out


PRON_EXTRA = {
    "este": "esta estes estas",
    "seu": "sua seus suas",
    "outro": "outra outros outras",
    "todo": "toda todos todas",
    "algum": "alguma alguns algumas",
    "nenhum": "nenhuma nenhuns nenhumas",
    "qual": "quais",
    "vários": "várias",
    "pouco": "pouca poucos poucas",
    "ambos": "ambas",
    "um": "uma uns umas",
    "o": "a os as",
    "primeiro": "primeira primeiros primeiras",
    "você": "vocês",
    "cada": "",
    "qualquer": "quaisquer",
    "que": "",
}

CONTRACTIONS = {
    # preposição + artigo / demonstrativo aprovado
    "do", "da", "dos", "das", "no", "na", "nos", "nas", "ao", "aos", "à", "às", "pelo", "pela", "pelos", "pelas",
    "num", "numa", "nuns", "numas", "deste", "desta", "destes", "destas", "neste", "nesta", "nestes", "nestas",
    "dum", "duma",
}


def approved_lexicon(rows):
    """Conjunto de formas (minúsculas, com acento) das palavras aprovadas."""
    lex = set(CONTRACTIONS)
    for r in rows:
        if r["st"] not in ("A", "O"):  # a palavra obsoleta continua em conformidade até a versão MAJOR
            continue
        w, c = r["w"].lower(), r["c"]
        parts = w.split()
        if len(parts) > 1:
            lex |= set(parts)
            if c in ("s", "adj"):
                for x in parts:
                    lex |= nominal_forms(x)
            continue
        if c == "v":
            lex |= verb_forms(w)
        elif c in ("s", "adj"):
            lex |= nominal_forms(w, fem_ok=(c == "adj"))
            if w.endswith("mente"):
                lex.add(w)
        elif c == "pron" or c == "art" or c == "num":
            lex.add(w)
            lex |= set(PRON_EXTRA.get(w, "").split())
            lex |= nominal_forms(w) if c == "num" else set()
        else:
            lex.add(w)
    return lex


def not_approved_forms(rows, lex, tech=frozenset()):
    """Formas das palavras não aprovadas de uma palavra (sem as formas que também são aprovadas)."""
    out = {}
    for r in rows:
        if r["st"] != "N":
            continue
        w, c = r["w"].lower(), r["c"]
        if " " in w or "/" in w or w.endswith("."):
            continue
        if c == "v":
            fs = verb_forms(w)
        elif c in ("s", "adj"):
            fs = nominal_forms(w, fem_ok=(c == "adj"))
        else:
            fs = {w}
        fs = {f for f in fs if f not in lex and (f == w or f not in tech)}
        out[w] = fs
    return out


TOKEN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)*")


def strip_literals(text):
    """Remove código, texto entre aspas e negrito de rótulo (literais, R8.8)."""
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"\"[^\"]*\"|“[^”]*”", " ", text)
    text = re.sub(r"\*\*[^*]+\*\*", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text


# ---------------------------------------------------------------------------
# Verificações de estilo nos exemplos PTS-BR (R3.1, R4.3, R8.4, R9.4, D1)
# ---------------------------------------------------------------------------
NUM_WORDS = r"dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|quinze|vinte|trinta|quarenta|cinquenta|sessenta|cem|cento|duzentos|trezentos|quinhentos|mil|milhão|milhões"
ORDINALS = r"segund[ao]s?|terceir[ao]s?|quart[ao]s?|quint[ao]s?|sext[ao]s?|sétim[ao]s?|oitav[ao]s?|non[ao]s?|décim[ao]s?"
UNIT_WORDS = r"milissegundos?|segundos?|minutos?|horas?|bytes?|kilobytes?|megabytes?|gigabytes?|terabytes?|por cento"
STYLE_CHECKS = [
    ("número por extenso (R8.4)", re.compile(r"(?<![\w-])(" + NUM_WORDS + r")(?![\w-])", re.I)),
    ("ordinal por extenso (R8.4)", re.compile(r"(?<![\w-])(o|a|os|as|do|da|no|na) (" + ORDINALS + r") (?!a\b)(\w+)", re.I)),
    ("unidade por extenso depois de número (R8.4)", re.compile(r"\d\s*(" + UNIT_WORDS + r")(?![\w-])", re.I)),
    ("ponto como separador de milhar (R8.4)", re.compile(r"(?<![\w.])\d{1,3}(\.\d{3})+(?![\w.])")),
    ("palavra que depende da data de leitura (R9.4)", re.compile(r"(?<![\w-])(ontem|hoje|amanhã|atualmente|recentemente|em breve)(?![\w-])", re.I)),
    # R8.4 e UM (art): quantidade 1 com algarismo ("1 vez por mês"); HORA é o momento do dia (duração: "1 h")
    ("\"uma vez\" ou \"um/uma\" + unidade de tempo (R8.4: use 1)", re.compile(
        r"(?<![\w-])(uma vez(?! que)|(um|uma) (minuto|hora|dia|semana|mês|ano)(?= (por|a cada|depois|antes|de espera)))(?![\w-])", re.I)),
    ("\"hora\" como duração (HORA: momento do dia; use \"1 h\")", re.compile(
        r"(?<![\w-])((a cada|por|uma|meia) hora|horas? (de duração|seguidas))(?![\w-])", re.I)),
    ("\"só\" (use APENAS)", re.compile(r"(?<![\w-])só(?![\w-])", re.I)),
    ("\"há\" (use EXISTIR ou TER)", re.compile(r"(?<![\w-])há(?![\w-])", re.I)),
    ("futuro simples ou \"irá\" (R3.1)", re.compile(r"(?<![\w-])(\w{2,}(?:ará|erá|irá|arão|erão|irão)|será|serão|terá|terão|fará|farão|poderá|poderão|irá|irão)(?![\w-])", re.I)),
    ("pronome átono ou passiva com \"se\" depois do verbo (R3.4, R3.7)", re.compile(r"\w-(se|lo|la|los|las|lhe|lhes)(?![\w-])", re.I)),
    ("\"o mesmo\" como pronome (R1.8)", re.compile(r"(?<![\w-])(o|a|os|as|do|da|no|na|ao|pelo|pela) mesm[oa]s?(?![\w-]) (?!\w+ )?(?=[.,;)]|$)", re.I)),
    # R3.5: verbo-suporte + substantivo derivado de verbo ("Faça a verificação", "faz o bloqueio")
    ("verbo-suporte com substantivo derivado (R3.5)", re.compile(
        r"(?<![\w-])(faz|fazem|faça|façam|fez|fizeram|fazer|realiz\w*|efetu\w*|proced\w*|providenci\w*|dá|dão|dê|deem|deu|deram|dar)"
        r"\s+(o|a|os|as|um|uma)\s+(?!(?:documento|argumento|elemento|segmento|instrumento|mensagem|imagem|momento|pagamento)s?(?![\w-]))"
        r"\w+(ção|ções|mento|mentos|agem|agens|eio|eios)(?![\w-])", re.I)),
    # R9.4: palavras relativas à data de publicação (E6: ATUAL e AGORA apenas para o momento do leitor)
    ("versão relativa à data de publicação (R9.4)", re.compile(
        r"(?<![\w-])((nova|última|atual|mais recente) (versão|release)|(versão|release) (nova|atual|mais nova|mais recente))(?![\w-])", re.I)),
    ("\"agora\" para uma alteração de versão (R9.4)", re.compile(
        r"(?<![\w-])agora (usa|tem|é|são|aceita|aceitam|retorna|retornam|envia|mostra|precisa|exige|suporta|funciona)(?![\w-])", re.I)),
]

# R6.4: palavra vaga sem um valor na mesma frase (E6)
VAGUE = re.compile(r"(?<![\w-])(vári[oa]s|grandes?|pequen[oa]s?|rápid[oa]s?|lent[oa]s?|alt[oa]s?|baix[oa]s?|frequentes?|pouc[oa]s?|muit[oa]s?)(?![\w-])", re.I)
# R8.5: hora sem fuso horário na mesma frase
HOUR = re.compile(r"(?<![\w:])\d{1,2}:\d{2}(?![\d:])")


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+|\s+/\s+", text) if s.strip()]
# ex.: "o segundo passo" (ordinal) é erro; "o tempo limite é de 30 segundos" é unidade
STYLE_ALLOW = {
    # "o segundo" como substantivo de unidade: "1 segundo" já é pego pela regra de unidade
}


def pts_texts(r):
    """Os textos PTS-BR de uma entrada: exemplo e as formas corretas entre "(Use: ...)"."""
    out = [r["ex"]]
    if r["st"] == "A":
        out += re.findall(r"\(Use: ([^)]*)\)", r["bad"])
    return [t for t in out if t and t != "—"]


def style_problems(text):
    t = strip_literals(text)
    out = []
    for name, rx in STYLE_CHECKS:
        for m in rx.finditer(t):
            out.append((name, m.group(0)))
    for s in sentences(t):
        # "o nível mais alto" é um superlativo exato, não uma palavra vaga
        vague = [m for m in VAGUE.finditer(s)
                 if not (re.match(r"(?i)alt|baix", m.group(1)) and s[:m.start()].lower().endswith("mais "))]
        if vague and not re.search(r"\d", s):
            out.append(("palavra vaga sem valor na frase (R6.4)", s))
    for s in sentences(text):  # o fuso horário pode estar em um literal
        if HOUR.search(strip_literals(s)) and "UTC" not in s:
            out.append(("hora sem fuso horário (R8.5)", s))
    return out


def main():
    rows, bad = load_rows()
    problems = list(bad)

    approved = {}
    for r in rows:
        if r["st"] == "A":
            if r["w"] != r["w"].upper():
                problems.append(("approved not upper", r["w"]))
            key = (r["w"], r["c"])
            if key in approved:
                problems.append(("dup approved", key))
            approved[key] = r
    appr_words = {k[0] for k in approved}
    homographs = collections.Counter(k[0] for k in approved)
    allowed_homo = {"A", "QUE"}
    for w, n in homographs.items():
        if n > 1 and w not in allowed_homo:
            problems.append(("approved homograph", w))

    na = {}
    for r in rows:
        if r["st"] == "N":
            if r["w"] != r["w"].lower():
                problems.append(("N not lower", r["w"]))
            if r["w"] in na:
                problems.append(("dup N", r["w"]))
            na[r["w"]] = r
            if r["w"].upper() in appr_words:
                problems.append(("both A and N", r["w"]))
            alt = r["m"].split(" — ")[0].strip()
            if alt.startswith("—"):
                continue
            for a in alt.split(";"):
                a = a.strip()
                m = re.fullmatch(r"(.+?) \((\w+)\)", a)
                if not m:
                    problems.append(("alt parse", r["w"], a)); continue
                if (m.group(1), m.group(2)) not in approved:
                    problems.append(("alt missing", r["w"], a))
        # uma definição, um significado: ";" na definição indica dois significados
        if r["st"] == "A" and re.search(r";", r["m"].split(". ")[0]):
            problems.append(("two senses (;) in definition", r["w"], r["m"]))

    problems += obsolete_problems(rows, approved, na)

    # vazamento: palavra não aprovada (forma flexionada) nos textos PTS-BR e nas definições
    lex = approved_lexicon(rows)
    tech = tech_lexicon()
    naf = not_approved_forms(rows, lex, tech)
    leak_rx = {w: re.compile(r"(?<![\w-])(" + "|".join(map(re.escape, sorted(fs, key=len, reverse=True))) + r")(?![\w-])")
               for w, fs in naf.items() if fs}
    # "nós" depois de artigo, contração ou número é o plural do nome técnico "nó" (intro.md, D11)
    TECH_NOS = re.compile(r"(?<!\w)(os|dos|nos|aos|pelos|\d+) nós(?!\w)")
    for r in rows:
        texts = pts_texts(r) + ([r["m"]] if r["st"] == "A" else [])
        text = TECH_NOS.sub(r"\1", strip_literals(" ".join(texts)).lower())
        for w, rx in leak_rx.items():
            if rx.search(text) and not (r["st"] == "N" and r["w"] == w):
                problems.append(("leak", r["w"], w))
        for t in pts_texts(r):
            for p in style_problems(t):
                problems.append(("style", r["w"], p[0], p[1]))

    # "para" (forma de PARAR) antes de artigo ou substantivo (D6, nota sobre PARAR)
    for r in rows:
        for t in pts_texts(r):
            for m in re.finditer(r"(?<![\w-])(o|a|um|uma)(?: \w+){1,2} para (o|a|os|as|um|uma|de|quando|se|\.|$)(?!\w)", strip_literals(t)):
                if re.search(r"(serviço|servidor|processo|banco|job|worker|pod|sistema|deploy|reinício|teste|disco|agente|cluster) para (o|a|os|as|um|uma|quando|\.|$)(?!\w)", m.group(0)):
                    problems.append(("PARAR × para (D6)", r["w"], m.group(0)))

    # uma palavra, um status: o 03 e o glossário do 04 não têm a mesma palavra, exceto D7 e D11
    D7 = {"entrada", "exceção", "processo", "tabela", "linha"}
    for term in glossary_terms():
        k = term.lower()
        if k in na:
            problems.append(("N no 03 e termo no glossário do 04", k))
        if k.upper() in appr_words and k not in D7:
            problems.append(("A no 03 e termo no glossário do 04 (fora de D7)", k))

    for p in problems:
        print("PROBLEM", p)

    nA = sum(1 for r in rows if r["st"] == "A")
    nN = sum(1 for r in rows if r["st"] == "N")
    nO = sum(1 for r in rows if r["st"] == "O")
    byclass = collections.Counter((r["st"], r["c"]) for r in rows)
    print("approved", nA, "not approved", nN, "obsolete", nO)
    print(sorted(byclass.items()))

    if "--lex" in sys.argv:
        unknown = collections.Counter()
        where = collections.defaultdict(set)
        for r in rows:
            for t in pts_texts(r):
                st = strip_literals(t)
                for m in TOKEN.finditer(st):
                    tok = m.group(0)
                    lo = tok.lower()
                    before = st[:m.start()].rstrip()
                    initial = (not before) or before[-1] in ".:!?/"
                    if lo in lex or lo in tech or tok.isupper() or (tok[0].isupper() and not initial):
                        continue
                    unknown[lo] += 1
                    where[lo].add(r["w"])
        for w, n in unknown.most_common():
            print("LEX", w, n, sorted(where[w])[:5])

    if "--teste" in sys.argv:
        problems += self_test()

    if "--render" in sys.argv:
        render(rows, nA, nN, nO)
        print("rendered")
    return 1 if problems else 0


def obsolete_problems(rows, approved, na):
    """Verificações do estado O: forma, substituta aprovada, versão da exclusão, uso nos exemplos."""
    out = []
    appr_words = {k[0] for k in approved}
    obs = {}
    for r in rows:
        if r["st"] != "O":
            continue
        w = r["w"]
        if w != w.upper():
            out.append(("O not upper", w))
        if w in obs:
            out.append(("dup O", w))
        obs[w] = r
        if w in appr_words:
            out.append(("both A and O", w))
        if w.lower() in na:
            out.append(("both N and O", w))
        alt, _, comment = r["m"].partition(" — ")
        if not re.search(r"(?i)exclusão na versão \d+\.0\.0", comment):
            out.append(("O sem a versão MAJOR da exclusão", w, r["m"]))
        for a in alt.split(";"):
            a = a.strip()
            m = re.fullmatch(r"(.+?) \((\w+)\)", a)
            if not m:
                out.append(("O alt parse", w, a)); continue
            if (m.group(1), m.group(2)) not in approved:
                out.append(("O alt missing", w, a))
        if not r["ex"] or r["ex"] == "—" or not r["bad"] or r["bad"] == "—":
            out.append(("O sem exemplo", w))
    # a palavra obsoleta não aparece nos textos PTS-BR (exemplos e formas corretas) de nenhuma entrada
    for w, ro in obs.items():
        fs = verb_forms(w) if ro["c"] == "v" else nominal_forms(w, fem_ok=(ro["c"] == "adj"))
        fs |= {w.lower()}
        rx = re.compile(r"(?<![\w-])(" + "|".join(map(re.escape, sorted(fs, key=len, reverse=True))) + r")(?![\w-])", re.I)
        for r in rows:
            if any(rx.search(strip_literals(t)) for t in pts_texts(r)):
                out.append(("palavra obsoleta em exemplo PTS-BR", r["w"], w))
    return out


def self_test():
    """Testa obsolete_problems() e a renderização do estado O com linhas de teste (não usa d*.txt)."""
    def row(line):
        p = line.split("|")
        return dict(st=p[0], w=p[1], c=p[2], m=p[3], ex=p[4], bad=p[5], src="teste")
    base_rows = [row("A|DEFINIR|v|Dar um valor a algo.|Defina a variável `PORT` como `8080`.|—")]
    casos = [
        # (linha O, número de problemas esperado)
        ("O|SETAR|v|DEFINIR (v) — exclusão na versão 2.0.0.|Defina a variável `PORT` como `8080`.|Sete a variável `PORT`.", 0),
        ("O|setar|v|DEFINIR (v) — exclusão na versão 2.0.0.|Defina a variável `PORT` como `8080`.|Sete a variável `PORT`.", 1),
        ("O|SETAR|v|AJUSTAR (v) — exclusão na versão 2.0.0.|Defina a variável `PORT` como `8080`.|Sete a variável `PORT`.", 1),
        ("O|SETAR|v|DEFINIR (v) — exclusão na versão 1.2.0.|Defina a variável `PORT` como `8080`.|Sete a variável `PORT`.", 1),
        ("O|DEFINIR|v|DEFINIR (v) — exclusão na versão 2.0.0.|Defina a variável `PORT` como `8080`.|Defina a variável.", 3),  # A e O; o exemplo usa a palavra obsoleta
        ("O|SETAR|v|DEFINIR (v) — exclusão na versão 2.0.0.|Sete a variável `PORT` como `8080`.|Sete a variável `PORT`.", 1),
    ]
    out = []
    for line, esperado in casos:
        rows = base_rows + [row(line)]
        approved = {(r["w"], r["c"]): r for r in rows if r["st"] == "A"}
        got = obsolete_problems(rows, approved, {})
        status = "ok" if len(got) == esperado else "FALHOU"
        print(f"TESTE {status}: {line.split('|')[1]} {line.split('|')[3][:40]!r} -> {len(got)} problema(s) {got}")
        if status != "ok":
            out.append(("self-test", line))
    print("TESTE linha renderizada:", render_row(row(casos[0][0])))
    return out


def render_row(r):
    """Uma linha da tabela do 03."""
    if r["st"] == "A":
        return f"| {r['w']} ({r['c']}) | Aprovada | {r['m']} | {r['ex']} | {r['bad']} |"
    if r["st"] == "O":
        return f"| {r['w']} ({r['c']}) | Obsoleta | Use: {r['m']} | {r['ex']} | {r['bad']} |"
    alt = ("Reescreva: " + r['m'][1:].strip()) if r['m'].startswith("—") else ("Use: " + r['m'])
    return f"| {r['w']} ({r['c']}) | Não aprovada | {alt} | {r['ex']} | {r['bad']} |"


def glossary_terms():
    """Primeira coluna do glossário-base (04, seção 6.2), sem o texto entre parênteses."""
    t = (ROOT / "04-termos-tecnicos.md").read_text(encoding="utf-8")
    return [re.sub(r"\s*\(.*?\)", "", m.group(1)).strip()
            for m in re.finditer(r"^\| ([^|]+?) \| (o|a|os|as) \| NT-", t, re.M)]


def tech_lexicon():
    """Palavras dos nomes técnicos de 04-termos-tecnicos.md (glossário, siglas, categorias, decisões, verbos)."""
    t = (ROOT / "04-termos-tecnicos.md").read_text(encoding="utf-8")
    words = set()
    def add(s):
        for tok in TOKEN.findall(s):
            words.add(tok.lower())
            words.update(nominal_forms(tok.lower(), fem_ok=False))
            words.update({tok.lower() + "s", tok.lower() + "es"})  # plural do inglês: "workers", "hashes"
            if "-" in tok:  # "verbo-suporte" -> "verbos-suporte"
                h, t = tok.lower().split("-", 1)
                words.update({x + "-" + t for x in nominal_forms(h, fem_ok=False)})
    # glossário-base e glossário de siglas: primeira coluna
    for m in re.finditer(r"^\| ([^|]+?) \| (o|a|os|as) \| ", t, re.M):
        add(re.sub(r"\(.*?\)", "", m.group(1)))
    for m in re.finditer(r"^\| ([A-Z][A-Za-z0-9/.-]*) \| ([^|]+) \| (o|a|os|as) \|", t, re.M):
        add(m.group(1))
    # categorias: linhas de exemplos
    for m in re.finditer(r"^- \*\*Exemplos:\*\* (.*)$", t, re.M):
        add(strip_literals(m.group(1)))
    # política de estrangeirismos: coluna "Forma no PTS-BR" das decisões Manter e Ambos
    for m in re.finditer(r"^\| [^|]+ \| (Manter|Ambos|Português) \| ([^|]+) \|", t, re.M):
        add(m.group(2).replace("*", ""))
    # verbos técnicos
    for m in re.finditer(r"^\| ([A-ZÁÉÍÓÚÂÊÔÃÕÇ]+) \| ", t, re.M):
        words |= verb_forms(m.group(1).lower())
    return words


RODAPE = "Feito com <3 em Joinville. 100% [PornCode](https://medium.com/@diogo.winck/manifesto-do-porn-coding-64c55df3e3eb). Nenhum direito reservado."
NAV = "[Início](README.md) · [01 Introdução](01-introducao.md) · [02 Regras](02-regras.md) · **03 Dicionário** · [04 Termos técnicos](04-termos-tecnicos.md) · [05 Governança](05-governanca.md) · [06 Exemplos](06-exemplos.md) · [Versões](CHANGELOG.md)"


def render(rows, nA, nN, nO):
    def sortkey(r):
        return (norm(r["w"]).replace("-", " "), {"A": 0, "O": 1, "N": 2}[r["st"]], r["c"])
    rows = sorted(rows, key=sortkey)
    groups = collections.OrderedDict()
    for r in rows:
        L = norm(r["w"])[0].upper()
        groups.setdefault(L, []).append(r)
    out = []
    head = "| Palavra (classe) | Decisão | Significado aprovado / Alternativa | Exemplo PTS-BR | Não aprovado |\n|---|---|---|---|---|"
    for L, rs in groups.items():
        out.append(f"## {L}\n\n{head}")
        for r in rs:
            out.append(render_row(r))
        out.append("")
    intro = (base / "intro.md").read_text(encoding="utf-8")
    letters = " · ".join(f"[{L}](#{L.lower()})" for L in groups)
    cls = collections.Counter(r["c"] for r in rows if r["st"] == "A")
    clsN = collections.Counter(r["c"] for r in rows if r["st"] == "N")
    clsO = collections.Counter(r["c"] for r in rows if r["st"] == "O")
    order = ["v", "s", "adj", "adv", "prep", "conj", "pron", "art", "num"]
    tbl = "| Classe | Aprovadas | Obsoletas | Não aprovadas |\n|---|---|---|---|\n" + "\n".join(
        f"| {c} | {cls.get(c,0)} | {clsO.get(c,0)} | {clsN.get(c,0)} |" for c in order + ["loc", "abrev"]) + f"\n| **Total** | **{nA}** | **{nO}** | **{nN}** |"
    intro = (intro.replace("{{NA}}", str(nA)).replace("{{NN}}", str(nN)).replace("{{NO}}", str(nO))
             .replace("{{LETRAS}}", letters).replace("{{TABELA_CLASSES}}", tbl))
    pathlib.Path(sys.argv[sys.argv.index("--render") + 1]).write_text(intro + "\n" + "\n".join(out).rstrip("\n") + "\n\n---\n\n<!-- nav -->\n" + NAV + "\n\n<!-- rodape -->\n" + RODAPE + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())

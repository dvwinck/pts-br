#!/usr/bin/env python3
"""Lista branca do PTS-BR: as palavras que um texto PTS-BR pode usar (decisão E1, regra D9 do 03).

Uma palavra é válida se for:
  (a) uma forma flexionada de uma entrada aprovada do 03-dicionario.md;
  (b) um nome técnico, um termo do glossário-base ou uma sigla do 04-termos-tecnicos.md;
  (c) uma palavra do vocabulário de metalinguagem (01-introducao.md, seção 11.2) ou dos
      termos de linguagem (04, NT-25). Apenas no texto da especificação (--spec);
  (d) uma palavra funcional aprovada: as contrações de uma preposição aprovada com um
      artigo ou com o pronome "este" aprovado (03, regra D2).
Uma sigla que o documento define na primeira ocorrência ("Forma por extenso (SIGLA)",
regra R8.7) também é válida nesse documento.
Um termo composto ("banco de dados", "pull request", "ponto de exclamação", "dentro de") é
uma unidade: o script aceita as palavras do termo apenas na sequência do termo. Uma palavra
do termo fora da sequência ("o ponto de decisão") precisa de uma entrada própria.
Uma entrada "Obsoleta" do 03 continua válida até a próxima versão MAJOR (05, seção 8.1).
A lista branca verifica a forma da palavra, não o significado. O revisor verifica o
significado (05, item CK-1.2).
No texto da especificação (--spec), os termos das tabelas de definições do 01 (seção 9) e do
05 (seção 1) também são válidos: estas tabelas são o glossário do projeto da especificação
(04, seção 7).

Um nome próprio (palavra com maiúscula no meio da frase, ou com maiúscula depois da primeira
letra) é um nome técnico da categoria NT-01 do 04. O script aceita o nome e conta o nome à parte.

Formas verbais (01-introducao.md, seção 5; 03, regra D2): infinitivo, infinitivo flexionado,
imperativo, presente, pretérito perfeito, futuro do subjuntivo, particípio e gerúndio (apenas com
"estar", R3.6). O script gera a 3ª pessoa (singular e plural), a forma de "você". O PTS-BR não usa
"eu", "tu" nem "nós" (R9.1). O pretérito imperfeito, o futuro simples e o futuro do pretérito não
são formas aprovadas: o script não gera estas formas.

Uso:
  python3 tools/lista_branca.py --explicar PALAVRA [...]   Mostra a origem de cada palavra
                                                           (ou o termo composto da palavra).
  python3 tools/lista_branca.py --teste                    Testa o léxico com frases conhecidas.
  python3 tools/check_spec.py --lista-branca --spec        Verifica a especificação (ver check_spec.py).

O script usa apenas a biblioteca padrão do Python 3.9 ou mais nova.
"""
import pathlib
import re
import sys
import unicodedata

BASE = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- formas verbais

# Desinências aprovadas, 3ª pessoa: (infinitivo e futuro do subjuntivo, infinitivo flexionado e
# futuro do subjuntivo plural, imperativo, presente, pretérito perfeito, particípio, gerúndio).
DESINENCIAS = {
    "ar": {"inf": ["ar", "arem"], "imp": ["e", "em"], "pres": ["a", "am"], "perf": ["ou", "aram"],
           "part": ["ado", "ada", "ados", "adas"], "ger": ["ando"]},
    "er": {"inf": ["er", "erem"], "imp": ["a", "am"], "pres": ["e", "em"], "perf": ["eu", "eram"],
           "part": ["ido", "ida", "idos", "idas"], "ger": ["endo"]},
    "ir": {"inf": ["ir", "irem"], "imp": ["a", "am"], "pres": ["e", "em"], "perf": ["iu", "iram"],
           "part": ["ido", "ida", "idos", "idas"], "ger": ["indo"]},
}

# Verbos irregulares: todas as formas aprovadas (3ª pessoa).
IRREGULARES = {
    "ser": "ser serem é são foi foram for forem seja sejam sendo sido",
    "estar": "estar estarem está estão esteve estiveram estiver estiverem esteja estejam estando estado",
    "ter": "ter terem tem têm teve tiveram tiver tiverem tenha tenham tendo tido tida tidos tidas",
    "ir": "ir irem vai vão foi foram for forem vá vão indo ido",
    "fazer": "fazer fazerem faz fazem fez fizeram fizer fizerem faça façam fazendo feito feita feitos feitas",
    "poder": "poder poderem pode podem pôde puderam puder puderem possa possam podendo podido",
    "dizer": "dizer dizerem diz dizem disse disseram disser disserem diga digam dizendo dito dita ditos ditas",
    "ver": "ver verem vê veem viu viram vir virem veja vejam vendo visto vista vistos vistas",
    "vir": "vir virem vem vêm veio vieram vier vierem venha venham vindo",
    "pôr": "pôr porem põe põem pôs puseram puser puserem ponha ponham pondo posto posta postos postas",
    "saber": "saber saberem sabe sabem soube souberam souber souberem saiba saibam sabendo sabido",
    "querer": "querer quererem quer querem quis quiseram quiser quiserem queira queiram querendo querido",
    "dar": "dar darem dá dão deu deram der derem dê deem dando dado dada dados dadas",
    "ler": "ler lerem lê leem leu leram ler leia leiam lendo lido lida lidos lidas",
    "trazer": "trazer trazerem traz trazem trouxe trouxeram trouxer trouxerem traga tragam trazendo trazido",
    "haver": "",  # não aprovado (R3.10); a entrada não existe como aprovada
    "perder": "perder perderem perde perdem perdeu perderam perca percam perdendo perdido perdida perdidos perdidas",
    "pedir": "pedir pedirem pede pedem pediu pediram peça peçam pedindo pedido pedida pedidos pedidas",
    "medir": "medir medirem mede medem mediu mediram meça meçam medindo medido medida medidos medidas",
    "impedir": "impedir impedirem impede impedem impediu impediram impeça impeçam impedindo impedido impedida impedidos impedidas",
    "sair": "sair saírem sai saem saiu saíram saia saiam saindo saído saída saídos saídas",
    "cair": "cair caírem cai caem caiu caíram caia caiam caindo caído caída",
    "ouvir": "ouvir ouvirem ouve ouvem ouviu ouviram ouça ouçam ouvindo ouvido",
    "proibir": "proibir proibirem proíbe proíbem proibiu proibiram proíba proíbam proibindo proibido proibida proibidos proibidas",
    "abrir": "abrir abrirem abre abrem abriu abriram abra abram abrindo aberto aberta abertos abertas",
    "cobrir": "cobrir cobrirem cobre cobrem cobriu cobriram cubra cubram cobrindo coberto coberta cobertos cobertas",
    "descobrir": "descobrir descobrirem descobre descobrem descobriu descobriram descubra descubram descobrindo descoberto descoberta",
    "escrever": "escrever escreverem escreve escrevem escreveu escreveram escreva escrevam escrevendo escrito escrita escritos escritas",
    "descrever": "descrever descreverem descreve descrevem descreveu descreveram descreva descrevam descrevendo descrito descrita descritos descritas",
    "imprimir": "imprimir imprimirem imprime imprimem imprimiu imprimiram imprima imprimam imprimindo impresso impressa impressos impressas imprimido",
    "dormir": "dormir dormirem dorme dormem dormiu dormiram durma durmam dormindo dormido",
}

# Prefixos dos verbos irregulares: "conter" = "con" + "ter".
FAMILIAS = {
    "ter": ["con", "man", "ob", "de", "re", "abs", "entre", "sus"],
    "fazer": ["des", "re", "satis"],
    "ver": ["pre", "re", "ante"],
    "vir": ["inter", "pro", "con", "sobre"],
    "pôr": ["com", "dis", "ex", "im", "pro", "re", "sup", "de", "pres", "trans"],
    "dizer": ["contra", "pre"],
    "abrir": ["entre", "re"],
    "cobrir": ["des", "en", "re"],
}
ACENTO_PREFIXO = {"tem": "tém", "vem": "vém", "pôr": "por", "porem": "porem"}


def _ortografia(radical, term, desinencia):
    """Ajusta o radical antes da desinência ("verifique", "proteja", "apareça", "siga")."""
    d = desinencia[:1]
    if term == "ar" and d in ("e", "é"):
        if radical.endswith("c"):
            return radical[:-1] + "qu"
        if radical.endswith("g"):
            return radical + "u"
        if radical.endswith("ç"):
            return radical[:-1] + "c"
    if term in ("er", "ir") and d in ("a", "o"):
        if radical.endswith("gu"):
            return radical[:-1]
        if radical.endswith("c"):
            return radical[:-1] + "ç"
        if radical.endswith("g"):
            return radical[:-1] + "j"
    return radical


def _ultima_vogal(radical):
    for i in range(len(radical) - 1, -1, -1):
        if radical[i] in "aeiouáéíóú":
            return i
    return -1


def formas_verbo(infinitivo):
    """Formas aprovadas de um verbo: 3ª pessoa dos tempos aprovados (01, seção 5)."""
    inf = infinitivo.lower().removesuffix("-se")
    if inf in IRREGULARES:
        return set(IRREGULARES[inf].split()) | {inf}
    for base, prefixos in FAMILIAS.items():
        for prefixo in prefixos:
            if inf == prefixo + base.replace("pôr", "por") or inf == prefixo + base:
                return {prefixo + ACENTO_PREFIXO.get(f, f) for f in IRREGULARES[base].split()}
    term = inf[-2:]
    if term not in DESINENCIAS:
        return {inf}
    radical = inf[:-2]
    formas = set()
    # verbos em -uir ("excluir", "substituir") e -air ("sair"): o "i" da desinência fica acentuado
    if term == "ir" and radical.endswith(("u", "a")) and not radical.endswith(("gu", "qu")):
        formas |= {inf, radical + "írem", radical + "i", radical + "em", radical + "iu",
                   radical + "íram", radical + "a", radical + "am", radical + "indo",
                   radical + "ído", radical + "ída", radical + "ídos", radical + "ídas"}
        return formas
    for tempo, lista in DESINENCIAS[term].items():
        for d in lista:
            formas.add(_ortografia(radical, term, d) + d)
    if term == "ar" and radical.endswith("e"):  # "bloquear": bloqueia, bloqueie
        formas |= {radical + "ia", radical + "iam", radical + "ie", radical + "iem"}
    if term == "ir" and radical.endswith("z"):  # "traduzir": traduz
        formas.add(radical)
    if term == "ir":
        i = _ultima_vogal(radical[:-1] if radical.endswith(("gu", "qu")) else radical)
        if i >= 0 and radical[i] == "e":  # "repetir": repita; "seguir": siga
            alt = radical[:i] + "i" + radical[i + 1:]
            formas |= {_ortografia(alt, term, "a") + "a", _ortografia(alt, term, "a") + "am"}
        if i >= 0 and radical[i] == "u":  # "consumir": consome
            alt = radical[:i] + "o" + radical[i + 1:]
            formas |= {alt + "e", alt + "em"}
    return formas


# ---------------------------------------------------------------- formas nominais

# Pronomes e numerais com feminino ou plural irregular.
PRONOMES_FLEXAO = {
    "este": "esta estes estas", "seu": "sua seus suas", "algum": "alguma alguns algumas",
    "nenhum": "nenhuma nenhuns nenhumas", "qual": "quais", "um": "uma uns umas",
}

# Particípios irregulares de verbos regulares (03, regra D3).
PARTICIPIOS = {
    "aceitar": "aceito aceita aceitos aceitas", "limpar": "limpo limpa limpos limpas",
    "soltar": "solto solta soltos soltas", "entregar": "entregue entregues",
    "imprimir": "impresso impressa impressos impressas", "pagar": "pago paga pagos pagas",
    "ganhar": "ganho ganha ganhos ganhas", "gastar": "gasto gasta gastos gastas",
    "salvar": "salvo salva salvos salvas", "eleger": "eleito eleita eleitos eleitas",
}

# Formatos de data e de hora escritos em maiúsculas (R8.5): um literal, não uma sigla.
FORMATO_DATA = re.compile(r"^(?:AAAA|AA|MM|DD|HH|SS|TN|T\d|N)(?:-(?:AAAA|AA|MM|DD|HH|SS|TN|N))*$")


def formas_nome(palavra, classe=None):
    """Plural e gênero de um substantivo ou de um adjetivo (03, regra D2).

    classe "s" (substantivo): o script gera apenas o plural, sem o feminino. Exceção: o
    feminino em "-a" de um substantivo em "-o" que nomeia uma pessoa ("usuário", "usuária").
    """
    p = palavra.lower()
    formas = {p}
    if len(p) < 2:
        return formas

    def plural(w):
        s = set()
        if not re.search(r"[aeiouáéíóúâêôãõ]", w.split("-")[-1]):
            s.add(w + "s")  # sigla em minúsculas ("pmd", "pts-br"): sem as regras do plural
        elif w.endswith(("ção", "são")):
            s.add(w[:-2] + "ões")  # "publicação" -> "publicações", nunca "publicaçãos"
        elif w.endswith("ão"):
            s |= {w[:-2] + "ões", w[:-2] + "ães", w + "s"}
        elif w.endswith(("ês", "ás")):
            s.add(w[:-2] + w[-2].translate(str.maketrans("êá", "ea")) + "ses")
        elif w.endswith(("s", "x")):
            s.add(w)
        elif w.endswith(("r", "z")):
            s.add(w + "es")
        elif w.endswith("m"):
            s.add(w[:-1] + "ns")
        elif w.endswith("al"):
            s.add(w[:-1] + "is")
        elif w.endswith("el"):
            s |= {w[:-2] + "éis", w[:-2] + "eis"}
        elif w.endswith("ol"):
            s.add(w[:-2] + "óis")
        elif w.endswith("ul"):
            s.add(w[:-1] + "is")
        elif w.endswith("il"):
            s |= {w[:-1] + "s", w[:-2] + "eis"}
        else:
            s.add(w + "s")
        return s

    formas |= plural(p)
    femininos = set(PRONOMES_FLEXAO.get(p, "").split())
    if p.endswith("ão"):
        if classe not in ("s",) and not p.endswith(("ção", "são")):
            femininos |= {p[:-2] + "ã", p[:-2] + "ona"}
    elif p.endswith("os"):  # "vários" -> "várias", "ambos" -> "ambas"
        femininos.add(p[:-2] + "as")
    elif p.endswith("o"):
        if classe != "s" or p.endswith(("ário", "eiro")):
            femininos.add(p[:-1] + "a")
    elif p.endswith("or"):
        if classe != "s" or p.endswith(("dor", "tor")):
            femininos.add(p + "a")
    elif p.endswith("ês"):
        if classe != "s":
            femininos.add(p[:-2] + "esa")
    for f in femininos:
        formas.add(f)
        formas |= plural(f)
    return formas


# ---------------------------------------------------------------- leitura das fontes

CLASSES = ("v", "s", "adj", "adv", "prep", "conj", "pron", "art", "num", "loc", "abrev")
PALAVRA = re.compile(r"[^\W\d_]+(?:-[^\W\d_]+)*")


def _tokens(texto):
    texto = re.sub(r"`[^`]*`", " ", texto).replace("*", " ")
    return [t.lower() for t in PALAVRA.findall(texto)]


def _celulas(linha):
    return [c.strip() for c in linha.strip().strip("|").split("|")]


# Palavras funcionais dentro de um termo composto: a forma com a contração também vale
# ("a partir de" vale também em "a partir destes arquivos").
FUNCIONAIS_TERMO = {
    "de": {"de", "do", "da", "dos", "das", "dum", "duma", "deste", "desta", "destes", "destas", "disto"},
    "em": {"em", "no", "na", "nos", "nas", "num", "numa", "neste", "nesta", "nestes", "nestas", "nisto"},
    "a": {"a", "à", "ao", "aos", "às"}, "por": {"por", "pelo", "pela", "pelos", "pelas"},
    "o": {"o", "os"}, "e": {"e"}, "ou": {"ou"}, "para": {"para"}, "com": {"com"}, "sem": {"sem"},
}
for _p in ("do", "da", "dos", "das"):
    FUNCIONAIS_TERMO[_p] = FUNCIONAIS_TERMO["de"]
for _p in ("no", "na", "nos", "nas"):
    FUNCIONAIS_TERMO[_p] = FUNCIONAIS_TERMO["em"]
ARTIGOS = {"o", "a", "os", "as", "um", "uma", "uns", "umas"}

# Formas de tempos não aprovados (01, seção 5): desinências da 3ª pessoa e de "você".
# Uma destas formas de um verbo aprovado é um desvio de R3.1 (CK-3.1), não uma palavra não
# aprovada: a métrica M2 não conta a forma (05, seção 5.4).
DESINENCIAS_NAO_APROVADAS = {
    "ar": "ava avam ará arão aria ariam ei aste amos ávamos aremos aríamos asse assem",
    "er": "ia iam erá erão eria eriam i este emos íamos eremos eríamos esse essem",
    "ir": "ia iam irá irão iria iriam i iste imos íamos iremos iríamos isse issem",
}
TEMPOS_IRREGULARES = {
    "ser": "era eram será serão seria seriam fosse fossem",
    "estar": "estava estavam estará estarão estaria estariam estivesse estivessem",
    "ter": "tinha tinham terá terão teria teriam tivesse tivessem",
    "ir": "ia iam irá irão iria iriam fosse fossem",
    "fazer": "fazia faziam fará farão faria fariam fizesse fizessem",
    "poder": "podia podiam poderá poderão poderia poderiam pudesse pudessem",
    "dever": "devia deviam deverá deverão deveria deveriam devesse devessem",
    "dizer": "dizia diziam dirá dirão diria diriam dissesse dissessem",
    "ver": "via viam verá verão veria veriam visse vissem",
    "vir": "vinha vinham virá virão viria viriam viesse viessem",
    "dar": "dava davam dará darão daria dariam desse dessem",
    "saber": "sabia sabiam saberá saberão saberia saberiam soubesse soubessem",
    "querer": "queria queriam quererá quererão quereria quereriam quisesse quisessem",
    "pôr": "punha punham porá porão poria poriam pusesse pusessem",
}


class Lexico:
    """Conjunto de formas válidas, com a origem de cada forma.

    origem: forma de 1 palavra -> origem. compostos: primeira forma de um termo composto ->
    [(sequência de conjuntos de formas, termo, origem)]. Uma palavra de um termo composto não
    entra em origem: a palavra vale apenas na sequência do termo.
    """

    def __init__(self, dicionario=None, termos=None, introducao=None, governanca=None, spec=True,
                 glossario=None):
        self.origem = {}
        self.compostos = {}
        self.verbos = {}  # infinitivo aprovado -> origem (para os tempos não aprovados)
        self.spec = spec
        self.dicionario = pathlib.Path(dicionario or BASE / "03-dicionario.md")
        self.termos = pathlib.Path(termos or BASE / "04-termos-tecnicos.md")
        self.introducao = pathlib.Path(introducao or BASE / "01-introducao.md")
        self.governanca = pathlib.Path(governanca or BASE / "05-governanca.md")
        self.aprovadas_03 = 0
        self.obsoletas_03 = 0
        self._tempos = None
        self._ler_03()
        self._ler_04()
        self._funcionais()
        if spec:
            self._ler_metalinguagem()
            self._ler_glossario_spec()
        if glossario:
            self.ler_glossario_projeto(glossario)

    def _add(self, forma, origem):
        forma = forma.lower()
        if forma and forma not in self.origem:
            self.origem[forma] = origem

    def _add_termo(self, toks, origem, ingles=False, flexao=True, classe=None):
        """Um termo: 1 palavra entra em origem; 2 palavras ou mais formam um termo composto."""
        while len(toks) > 1 and toks[0] in ARTIGOS:
            toks = toks[1:]
        if not toks:
            return
        if len(toks) == 1:
            t = toks[0]
            for f in (formas_nome(t, "s" if ingles else classe) if flexao else {t}):
                self._add(f, origem)
            if ingles:  # plural em inglês de um termo técnico: "workers", "hashes", "patches"
                self._add(t + ("es" if t.endswith(("sh", "ch", "x", "s")) else "s"), origem)
            return
        seq = []
        for t in toks:
            if t in FUNCIONAIS_TERMO:
                seq.append(frozenset(FUNCIONAIS_TERMO[t]))
            elif flexao:
                formas = set(formas_nome(t, "s")) | {t}
                if ingles:
                    formas.add(t + ("es" if t.endswith(("sh", "ch", "x", "s")) else "s"))
                seq.append(frozenset(formas))
            else:
                seq.append(frozenset({t}))
        seq = tuple(seq)
        termo = " ".join(toks)
        for f in seq[0]:
            lista = self.compostos.setdefault(f, [])
            if all(s != seq for s, _, _ in lista):
                lista.append((seq, termo, origem))

    def _add_termos(self, texto, origem, ingles=False, separar_e=False):
        """Uma lista de termos ("botão, campo, caixa de seleção. Navegação: menu").

        O rótulo antes de dois-pontos ("Formulários:") entra como palavras soltas.
        """
        texto = re.sub(r"`[^`]*`", " ", texto).replace("*", " ")
        texto = re.sub(r"\([^)]*\)", " ", texto) if not separar_e else texto
        for frase in re.split(r"\.\s+|\.$|;", texto):
            if ":" in frase:
                rotulo, frase = frase.split(":", 1)
                for t in _tokens(rotulo):  # rótulo: substantivo, sem feminino
                    self._add_termo([t], origem, classe="s")
            partes = re.split(r",| e | ou |/", frase) if separar_e else re.split(r",|/", frase)
            for parte in partes:
                self._add_termo(_tokens(parte), origem, ingles)

    # Compatibilidade: o nome antigo do método.
    def _add_nome(self, termo, origem, ingles=False):
        self._add_termos(termo, origem, ingles)

    def _ler_03(self):
        if not self.dicionario.exists():
            return
        padrao = re.compile(r"^\| (.+?) \(([\w ]+)\) \| (Aprovada|Obsoleta|Obsoleto) \|")
        for linha in self.dicionario.read_text(encoding="utf-8").splitlines():
            m = padrao.match(linha)
            if not m:
                continue
            palavra, classe = m.group(1).lower(), m.group(2)
            origem = f"03: {m.group(1)} ({classe})"
            if m.group(3) == "Aprovada":
                self.aprovadas_03 += 1
            else:  # obsoleta: válida até a próxima versão MAJOR (05, seção 8.1)
                self.obsoletas_03 += 1
                origem += ", obsoleta"
            if " " in palavra:  # locução aprovada: um termo composto, sem flexão
                self._add_termo(palavra.split(), origem, flexao=False)
            elif classe == "v":
                self.verbos.setdefault(palavra.removesuffix("-se"), origem)
                for f in formas_verbo(palavra) | set(PARTICIPIOS.get(palavra, "").split()):
                    self._add(f, origem)
            elif classe in ("s", "adj", "pron", "num"):
                for f in formas_nome(palavra, classe):
                    self._add(f, origem)
            else:
                self._add(palavra, origem)

    def _ler_04(self):
        if not self.termos.exists():
            return
        secao = ""
        nt = ""
        em_exemplos = False
        cab = None
        for linha in self.termos.read_text(encoding="utf-8").splitlines():
            if linha.startswith("#"):
                secao = linha
                m = re.match(r"###\s+(NT-\d+)", linha)
                nt = m.group(1) if m else ""
                em_exemplos = False
                cab = None
                continue
            if nt:
                m = re.match(r"^- \*\*Exemplos:\*\*\s*(.*)", linha)
                if m:
                    em_exemplos = True
                    origem = f"04: {nt}"
                    if nt == "NT-25" and not self.spec:
                        continue
                    self._add_termos(m.group(1), origem, ingles=True)
                    continue
                if em_exemplos and re.match(r"^\s{2,}- ", linha):
                    if nt == "NT-25" and not self.spec:
                        continue
                    self._add_termos(linha.strip()[2:], f"04: {nt}", ingles=True)
                    continue
                em_exemplos = False
            if not linha.startswith("|") or set(linha) <= set("|-: "):
                continue
            cel = _celulas(linha)
            if cab is None:
                cab = [c.lower() for c in cel]
                continue
            if "6.3" in secao or "5.4" in secao:  # termos não aprovados
                continue
            if "4.2" in secao or secao.startswith("####"):  # verbos técnicos
                if cab and cab[0] == "verbo" and re.fullmatch(r"[A-ZÇÃÕÁÉÍÓÚÂÊÔ]+", cel[0]):
                    self.verbos.setdefault(cel[0].lower(), f"04: verbo técnico {cel[0]}")
                    for f in formas_verbo(cel[0]):
                        self._add(f, f"04: verbo técnico {cel[0]}")
                continue
            if "5.5" in secao and len(cel) >= 3:
                origem = f"04: 5.5 {cel[0]}"
                manter = cel[1].lower().startswith(("manter", "ambos"))
                self._add_termos(cel[2], origem, ingles=manter)
                if manter:
                    self._add_termos(cel[0], origem, ingles=True)
                continue
            if "6.1" in secao:
                self._add(cel[0], f"04: sigla {cel[0]}")
                continue
            if "6.2" in secao:
                self._add_termos(cel[0], f"04: glossário {cel[0]}", ingles=True)
                # nomes em maiúsculas que a definição cria ("MAJOR, MINOR e PATCH são os nomes...")
                for nome in re.findall(r"\b[A-Z]{3,}\b", cel[-1]):
                    self._add(nome, f"04: glossário {cel[0]}")
                continue

    def _funcionais(self):
        """Contrações de preposição aprovada + artigo ou "este" aprovado (03, D2)."""
        contracoes = {
            "de": ["do", "da", "dos", "das", "dum", "duma", "duns", "dumas", "deste", "desta", "destes", "destas", "disto"],
            "em": ["no", "na", "nos", "nas", "num", "numa", "nuns", "numas", "neste", "nesta", "nestes", "nestas", "nisto"],
            "a": ["ao", "aos", "à", "às"],
            "por": ["pelo", "pela", "pelos", "pelas"],
        }
        for prep, formas in contracoes.items():
            if prep in self.origem:
                for f in formas:
                    self._add(f, f"funcional: contração de {prep.upper()} (03, D2)")
        for artigo, plural in (("o", "os"), ("a", "as"), ("um", "uns"), ("um", "uma"), ("um", "umas")):
            if artigo in self.origem:
                self._add(plural, f"funcional: flexão do artigo {artigo.upper()} (03, D2)")
        # "se" de verbo pronominal (R3.7), "não" e "este" são entradas do 03.

    def _ler_metalinguagem(self):
        for codigo in CLASSES:  # códigos de classe gramatical do 03 (seção 1.1)
            self._add(codigo, "03: 1.1 código de classe gramatical")
        if not self.introducao.exists():
            return
        dentro = False
        for linha in self.introducao.read_text(encoding="utf-8").splitlines():
            if linha.startswith("### 11.2"):
                dentro = True
                continue
            if dentro and linha.startswith("#"):
                break
            if dentro and linha.startswith("|") and not set(linha) <= set("|-: "):
                cel = _celulas(linha)
                if len(cel) >= 2 and cel[0].lower() != "grupo":
                    self._add_termos(cel[1], "01: 11.2 metalinguagem")

    def _ler_glossario_spec(self):
        """Glossário do projeto da especificação: 01 seção 9 e 05 seção 1 (04, seção 7)."""
        for caminho, inicio in ((self.introducao, "## 9."), (self.governanca, "## 1.")):
            if not caminho.exists():
                continue
            dentro = False
            for linha in caminho.read_text(encoding="utf-8").splitlines():
                if linha.startswith(inicio):
                    dentro = True
                    continue
                if dentro and linha.startswith("## "):
                    break
                if dentro and linha.startswith("|") and not set(linha) <= set("|-: "):
                    cel = _celulas(linha)
                    if cel and cel[0].lower() not in ("termo",):
                        nome = caminho.name[:2]
                        self._add_termos(cel[0], f"{nome}: glossário do projeto ({cel[0]})", separar_e=True)

    def ler_glossario_projeto(self, caminho):
        """--glossario: a tabela do glossário do projeto no modelo do 04, seção 7.

        A coluna "Termo" entra na lista branca. Devolve [(termo, [sinônimos não aprovados])].
        """
        return ler_glossario(caminho, self)

    # ------------------------------------------------------------ consulta

    def explicar(self, token):
        """Origem da palavra, ou None se a palavra está fora da lista branca."""
        t = token.lower()
        if t in self.origem:
            return self.origem[t]
        if t.endswith("-se") and t[:-3] in self.origem:  # verbo pronominal: "certifique-se"
            return self.origem[t[:-3]] + " + se"
        if "-" in t:
            partes = t.split("-")
            if all(p in self.origem for p in partes):
                return " + ".join(self.origem[p] for p in partes)
        sem = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
        if sem != t and sem in self.origem and t.isupper():
            return self.origem[sem]
        return None

    def termos_com(self, token):
        """Os termos compostos que têm a palavra (para --explicar)."""
        t = token.lower()
        saida = []
        for lista in self.compostos.values():
            for seq, termo, origem in lista:
                if any(t in s for s in seq) and (termo, origem) not in saida:
                    saida.append((termo, origem))
        return saida

    def tempo_nao_aprovado(self, token):
        """O infinitivo, se a palavra for uma forma de um tempo não aprovado de um verbo aprovado."""
        if self._tempos is None:
            self._tempos = {}
            for inf in self.verbos:
                if inf in TEMPOS_IRREGULARES:
                    for f in TEMPOS_IRREGULARES[inf].split():
                        self._tempos.setdefault(f, inf)
                    continue
                term = inf[-2:]
                if term not in DESINENCIAS_NAO_APROVADAS:
                    continue
                for d in DESINENCIAS_NAO_APROVADAS[term].split():
                    f = _ortografia(inf[:-2], term, d) + d
                    if f not in self.origem:
                        self._tempos.setdefault(f, inf)
        return self._tempos.get(token.lower())

    def termo_em(self, palavras, i):
        """Tamanho do termo composto mais longo que começa em palavras[i] (0 se nenhum)."""
        melhor = 0
        for seq, _, _ in self.compostos.get(palavras[i], ()):
            n = len(seq)
            if n > melhor and i + n <= len(palavras) and all(palavras[i + k] in seq[k] for k in range(n)):
                melhor = n
        return melhor


def ler_glossario(caminho, lexico=None):
    """Lê o glossário do projeto (04, seção 7): colunas "Termo" e "Sinônimos não aprovados".

    Devolve [(termo, [sinônimos])]. Com um léxico, os termos entram na lista branca.
    """
    caminho = pathlib.Path(caminho)
    if not caminho.exists():
        sys.exit(f"Erro: o glossário {caminho} não existe.")
    saida, cab = [], None
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        if not linha.startswith("|"):
            cab = None
            continue
        if set(linha) <= set("|-: "):
            continue
        cel = _celulas(linha)
        if cab is None:
            cab = [c.lower() for c in cel]
            continue
        if "termo" not in cab:
            continue
        termo = cel[cab.index("termo")]
        sinonimos = []
        for nome in ("sinônimos não aprovados", "sinonimos nao aprovados"):
            if nome in cab and cab.index(nome) < len(cel):
                sinonimos = [s.strip() for s in re.split(r"[,;]", cel[cab.index(nome)])
                             if s.strip() and s.strip() not in ("—", "-")]
        if lexico is not None:
            lexico._add_termos(termo, f"glossário do projeto: {termo}", ingles=True)
        saida.append((termo, sinonimos))
    return saida


# ---------------------------------------------------------------- verificação de blocos de texto

TOKEN = re.compile(r"[\w]+(?:[-’'][\w]+)*")
FIM = re.compile(r"[.!?:]\s*$")


# Sigla definida no próprio documento (R8.7): "Forma por extenso (SIGLA)" ou "SIGLA (Forma por extenso)".
SIGLA_DEFINIDA = re.compile(r"[^\W\d_][\w-]*(?:\s+[\w-]+){0,8}\s*\(([A-ZÇÃÕÁÉÍÓÚ][A-Z0-9ÇÃÕÁÉÍÓÚ-]+)\)"
                            r"|\b([A-Z][A-Z0-9-]+)\s+\((?:[^()\d]*[a-zà-ú][^()]*)\)")


def siglas_definidas(texto):
    """Siglas que o documento define na primeira ocorrência (R8.7)."""
    saida = set()
    for m in SIGLA_DEFINIDA.finditer(texto):
        sigla = m.group(1) or m.group(2)
        if sigla and sigla.isupper() and len(sigla) >= 2:
            saida.add(sigla)
    return saida


def classificar(token, inicio_frase, lexico, extras=frozenset()):
    """Devolve 'ok', 'nome' (nome próprio, NT-01) ou 'fora'."""
    if token in extras:
        return "ok"
    if any(c.isdigit() or c == "_" for c in token) or token == "X" or FORMATO_DATA.match(token):
        return None
    if len(token) == 1 and token.lower() not in lexico.origem:
        return None  # letra solta: item de lista "a)", variável
    if lexico.explicar(token):
        return "ok"
    if not token.isupper() and any(c.isupper() for c in token[1:]):
        return "nome"  # maiúscula depois da primeira letra: "GitHub", "macOS", "spaCy"
    if token[0].isupper() and not token.isupper() and not inicio_frase:
        return "nome"
    return "fora"


def verificar_blocos(blocos, lexico, extras=frozenset()):
    """blocos: [(texto, mapa_de_linhas)] -> (total, fora, nomes).

    fora: [(palavra como no texto, linha, início de frase)]. nomes: [(palavra, linha)].
    Um termo composto é uma unidade: as palavras do termo valem apenas na sequência do termo.
    """
    total, fora, nomes = 0, [], []
    for texto, mapa in blocos:
        achados = list(TOKEN.finditer(texto))
        palavras = [m.group(0).lower() for m in achados]
        no_termo = set()
        i = 0
        while i < len(achados):
            n = lexico.termo_em(palavras, i)
            # as palavras do termo estão juntas, apenas com espaço entre as palavras
            while n > 1 and any(texto[achados[k].end():achados[k + 1].start()].strip()
                                for k in range(i, i + n - 1)):
                n = 0
            if n > 1:
                no_termo.update(range(i, i + n))
                i += n
            else:
                i += 1
        for idx, m in enumerate(achados):
            token = m.group(0)
            antes = texto[:m.start()].rstrip()
            inicio = (not antes) or antes[-1] in ".!?:\n|" or antes.endswith(("—", "(", "\"", "“", "-"))
            c = "ok" if idx in no_termo and not any(ch.isdigit() for ch in token) and token != "X" \
                else classificar(token, inicio, lexico, extras)
            if c is None:
                continue
            total += 1
            linha = mapa[0][1]
            for desloc, n in mapa:
                if desloc <= m.start():
                    linha = n
            if c == "fora":
                fora.append((token, linha, inicio))
            elif c == "nome":
                nomes.append((token, linha))
    return total, fora, nomes


# ---------------------------------------------------------------- testes

VALIDAS = [
    "Verifique o estado do serviço.",
    "Os pods ficaram no estado `Running` depois de 2 min.",
    "Se o teste falhar, volte ao passo 2.",
    "O sistema vai enviar um e-mail quando o build terminar.",
    "Corrija o arquivo e execute o comando de novo.",
    "O script bloqueia a conta e exclui os arquivos.",
    "Os arquivos excluídos não estão no backup.",
    "Siga as instruções e mantenha o cluster no estado anterior.",
    "O pacote contém 3 arquivos. Os arquivos contêm a configuração.",
    "Este valor foi descrito na seção 4.",
    "Faça o rebase do branch.",
    "O Sistema de Pagamentos Online (SPO) envia o relatório. O SPO grava o log.",
    "Aguarde até os pods ficarem prontos.",
    "Crie o pull request no repositório.",
    "Os bancos de dados estão no cluster.",
]
FORA = [
    ("Realize a instalação do pacote.", "realize"),
    ("Os serviços estavam parados.", "estavam"),
    ("O sistema enviará um e-mail.", "enviará"),
    ("O comando faria a cópia.", "faria"),
    ("Deployei a versão.", "deployei"),
    ("Outrossim, reinicie o serviço.", "outrossim"),
    ("Abra o XPTO no portal.", "xpto"),
    # Termo composto do 04 ("provedor de identidade"): a parte do termo não vale sozinha.
    ("Verifique o provedor antes do deploy.", "provedor"),
    # O plural de "-ção" é "-ções".
    ("As publicaçãos estão prontas.", "publicaçãos"),
]


def testar(lexico=None):
    lexico = lexico or Lexico(spec=False)
    falhas = 0
    for frase in VALIDAS:
        _, fora, _ = verificar_blocos([(frase, [(0, 1)])], lexico, siglas_definidas(frase))
        if fora:
            falhas += 1
            print(f"  FALHA (frase válida com palavra fora): {frase} -> {', '.join(f[0] for f in fora)}")
    for frase, esperada in FORA:
        _, fora, _ = verificar_blocos([(frase, [(0, 1)])], lexico, siglas_definidas(frase))
        if esperada not in {f[0].lower() for f in fora}:
            falhas += 1
            print(f"  FALHA (a palavra '{esperada}' deveria estar fora): {frase}")
    print(f"  ListaBranca              {len(VALIDAS) + len(FORA) - falhas} ok, {falhas} falha(s)")
    return falhas


def main(argv):
    if "--teste" in argv:
        return 1 if testar() else 0
    if "--explicar" in argv:
        lexico = Lexico(spec="--sem-spec" not in argv)
        for p in argv[argv.index("--explicar") + 1:]:
            if p.startswith("--"):
                continue
            origem = lexico.explicar(p)
            termos = lexico.termos_com(p)
            texto = origem or "FORA da lista branca"
            if termos:
                texto += "; termo composto: " + ", ".join(f"'{t}' ({o})" for t, o in termos[:5])
            print(f"{p}: {texto}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

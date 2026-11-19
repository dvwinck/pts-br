#!/usr/bin/env python3
"""Monta a pasta de entrada do MkDocs (_build/docs) a partir dos arquivos da especificação.

Os arquivos da especificação não mudam. Na cópia para o site:
- a barra de navegação em texto (<!-- nav -->) sai, porque o site tem menu próprio;
- os links para README.md apontam para a página inicial do site (index.md);
- o README.md também vira a página leia-me.md;
- as 6 partes escondem a navegação lateral (o menu de abas já mostra as partes);
- os títulos das regras do 02 perdem a marca `[vale]`/`[revisor]` no texto e ganham o
  atributo data-verif (o pts.js mostra a marca como selo). O id do título não muda.
"""
import pathlib
import re
import shutil
import unicodedata

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "site-src"
DEST = RAIZ / "_build" / "docs"

NAV = re.compile(r"(?:\n---\n)?\n<!-- nav -->\n[^\n]*\n?")
README_LINK = re.compile(r"\]\(README\.md(#[^)]*)?\)")
REGRA = re.compile(r"^(### (R\d+\.\d+ .*?)) `\[(vale|revisor)\]`\s*$", re.M)


def slug(texto):
    """Mesmo slug do pymdownx.slugs.slugify(case="lower") usado no mkdocs.yml."""
    t = re.sub(r"`([^`]*)`", r"\1", texto)
    t = unicodedata.normalize("NFC", t).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def regra(m):
    titulo, verif = m.group(2), m.group(3)
    ident = slug(f"{titulo} `[{verif}]`")
    return f"### {titulo} {{ #{ident} data-verif=\"{verif}\" }}"


MARCADOR = re.compile(r"^( *)([-*+] |\d+[.)] )")
CERCA = re.compile(r"^ *(```|~~~)")
PREFIXO = re.compile(r"^((?:> ?)*)(.*)$")


def recuar_listas(texto):
    """Converte o recuo das listas aninhadas do estilo do GitHub (2 ou 3 espaços, alinhado
    ao texto do item) para os 4 espaços que o Python-Markdown exige. Mantém o conteúdo
    dos blocos de código. Trata cada nível de citação (">") em separado."""
    estados = {}
    saida = []
    for linha in texto.split("\n"):
        prefixo, resto = PREFIXO.match(linha).groups()
        chave = prefixo.replace(" ", "")
        est = estados.setdefault(chave, {"pilha": [], "cerca": None})
        for outra in list(estados):
            if outra != chave and len(outra) > len(chave):
                estados[outra] = {"pilha": [], "cerca": None}
        k = len(resto) - len(resto.lstrip(" "))

        if est["cerca"] is not None:
            orig, novo = est["cerca"]
            if k >= orig:
                resto = " " * (novo + k - orig) + resto[k:]
            if CERCA.match(resto):
                est["cerca"] = None
            saida.append(prefixo + resto)
            continue

        if not resto.strip():
            saida.append(linha)
            continue

        pilha = est["pilha"]
        m = MARCADOR.match(resto)
        if m:
            # No GitHub, uma lista pode começar logo depois de um parágrafo (com "-" ou "1.").
            # O Python-Markdown exige uma linha em branco antes: a função acrescenta essa linha.
            if not pilha and saida and re.match(r"[-*+]|1[.)]", m.group(2)):
                ant_prefixo, ant_resto = PREFIXO.match(saida[-1]).groups()
                if ant_prefixo.replace(" ", "") == chave and ant_resto.strip() and not ant_resto.lstrip().startswith("|"):
                    saida.append(prefixo.rstrip())
            while pilha and k < pilha[-1][0]:
                pilha.pop()
            novo = pilha[-1][1] if pilha and k >= pilha[-1][0] else (0 if k < 4 else k)
            if pilha and k >= pilha[-1][0]:
                novo = pilha[-1][1]
            pilha.append((k + len(m.group(2)), novo + 4))
            resto = " " * novo + resto[k:]
        elif k > 0 and pilha:
            while pilha and k < pilha[-1][0]:
                pilha.pop()
            if pilha:
                orig, novo = pilha[-1]
                resto = " " * (novo + k - orig) + resto[k:]
        elif k == 0 and not pilha:
            pass
        elif k == 0:
            # Linha sem recuo: fim da lista, exceto continuação preguiçosa de um parágrafo.
            anterior = saida[-1] if saida else ""
            if not PREFIXO.match(anterior).group(2).strip():
                pilha.clear()

        if CERCA.match(resto):
            n = len(resto) - len(resto.lstrip(" "))
            est["cerca"] = (k, n)
        saida.append(prefixo + resto)
    return "\n".join(saida)


def preparar(texto, nome):
    texto = NAV.sub("\n", texto)
    texto = recuar_listas(texto)
    texto = README_LINK.sub(lambda m: f"](index.md{m.group(1) or ''})", texto)
    if nome == "02-regras.md":
        texto = REGRA.sub(regra, texto)
    if re.match(r"0[1-6]-", nome):
        texto = "---\nhide:\n  - navigation\n---\n\n" + texto
    return texto


def copiar(origem, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    if origem.suffix == ".md":
        destino.write_text(preparar(origem.read_text(encoding="utf-8"), origem.name), encoding="utf-8")
    else:
        shutil.copy2(origem, destino)


def main():
    shutil.rmtree(RAIZ / "_build", ignore_errors=True)
    DEST.mkdir(parents=True)
    for nome in ["01-introducao.md", "02-regras.md", "03-dicionario.md", "04-termos-tecnicos.md",
                 "05-governanca.md", "06-exemplos.md", "CHANGELOG.md", "BRIEF.md"]:
        copiar(RAIZ / nome, DEST / nome)
    copiar(RAIZ / "README.md", DEST / "leia-me.md")
    for md in sorted((RAIZ / "reviews").rglob("*.md")):
        rel = md.relative_to(RAIZ)
        if "scripts-de-trabalho" not in rel.parts:
            copiar(md, DEST / rel)
    copiar(SRC / "index.md", DEST / "index.md")
    for arq in sorted((SRC / "assets").iterdir()):
        copiar(arq, DEST / "assets" / arq.name)
    print("pasta do site:", DEST.relative_to(RAIZ))


if __name__ == "__main__":
    main()

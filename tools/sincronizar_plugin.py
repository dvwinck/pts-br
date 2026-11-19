#!/usr/bin/env python3
"""Copia a especificação e o linter para o plugin do Claude Code (plugins/pts-br/especificacao).

Um plugin instalado não lê arquivos fora da própria pasta, e o Claude Code não segue links
simbólicos para fora do plugin. Por isso, o plugin tem uma cópia dos arquivos.

Uso (na raiz do repositório):
    python3 tools/sincronizar_plugin.py              # atualiza a cópia
    python3 tools/sincronizar_plugin.py --verificar  # código 1 se a cópia está desatualizada
"""
import filecmp
import pathlib
import shutil
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "plugins" / "pts-br" / "especificacao"

ARQUIVOS = [
    "LICENSE",
    "01-introducao.md",
    "02-regras.md",
    "03-dicionario.md",
    "04-termos-tecnicos.md",
    "05-governanca.md",
    "06-exemplos.md",
    "tools/check_spec.py",
    "tools/lista_branca.py",
    "tools/vale/.vale.ini",
    "tools/vale/config/vocabularies/PTSBR/accept.txt",
]
PASTAS = ["tools/vale/PTSBR"]


def lista():
    nomes = list(ARQUIVOS)
    for pasta in PASTAS:
        for arq in sorted((RAIZ / pasta).iterdir()):
            if arq.is_file():
                nomes.append(f"{pasta}/{arq.name}")
    return nomes


def verificar():
    esperados = set(lista())
    diferentes = [n for n in esperados if not (DESTINO / n).exists() or not filecmp.cmp(RAIZ / n, DESTINO / n, shallow=False)]
    sobrando = [str(p.relative_to(DESTINO)) for p in DESTINO.rglob("*")
                if p.is_file() and "__pycache__" not in p.parts
                and str(p.relative_to(DESTINO)) not in esperados] if DESTINO.exists() else []
    for n in sorted(diferentes):
        print("desatualizado:", n)
    for n in sorted(sobrando):
        print("sobrando:", n)
    if diferentes or sobrando:
        print("Execute: python3 tools/sincronizar_plugin.py")
        return 1
    print(f"OK: a cópia do plugin tem os {len(esperados)} arquivos atuais.")
    return 0


def sincronizar():
    if DESTINO.exists():
        shutil.rmtree(DESTINO)
    for n in lista():
        (DESTINO / n).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RAIZ / n, DESTINO / n)
    print(f"Copiados {len(lista())} arquivos para {DESTINO.relative_to(RAIZ)}.")
    return 0


if __name__ == "__main__":
    sys.exit(verificar() if "--verificar" in sys.argv else sincronizar())

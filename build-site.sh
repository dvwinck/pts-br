#!/bin/sh
# Monta a pasta de entrada do MkDocs (_build/docs) e gera o site em site/.
set -eu
cd "$(dirname "$0")"
rm -rf site
python3 site-src/preparar.py
mkdocs build "$@"

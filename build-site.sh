#!/bin/sh
# Monta a pasta de entrada do MkDocs (_build/docs) e gera o site em site/.
set -eu
cd "$(dirname "$0")"
rm -rf _build site
mkdir -p _build/docs/reviews
cp README.md 0[1-6]-*.md CHANGELOG.md BRIEF.md _build/docs/
cp reviews/*.md _build/docs/reviews/
for r in reviews/round-*; do mkdir -p "_build/docs/$r"; cp "$r"/*.md "_build/docs/$r/"; done
mkdocs build "$@"

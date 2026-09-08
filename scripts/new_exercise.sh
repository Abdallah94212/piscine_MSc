#!/usr/bin/env bash
# Cree un nouveau dossier dayXX/exXX a partir du template.
# Usage: ./scripts/new_exercise.sh <day> <exercise>
#   ex: ./scripts/new_exercise.sh 01 02   -> day01/ex02/

set -euo pipefail

if [ $# -ne 2 ]; then
    echo "Usage: $0 <day> <exercise>"
    echo "Exemple: $0 01 02   (cree day01/ex02/)"
    exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DAY=$(printf "%02d" "$1")
EX=$(printf "%02d" "$2")
TARGET="$ROOT_DIR/day$DAY/ex$EX"

if [ -d "$TARGET" ]; then
    echo "Le dossier $TARGET existe deja."
    exit 1
fi

mkdir -p "$TARGET"
cp "$ROOT_DIR/templates/exercise/README.md" "$TARGET/README.md"
cp "$ROOT_DIR/templates/exercise/main.py" "$TARGET/main.py"
sed -i '' "s/exXX/ex$EX/" "$TARGET/README.md" 2>/dev/null || sed -i "s/exXX/ex$EX/" "$TARGET/README.md"

echo "Cree: $TARGET"

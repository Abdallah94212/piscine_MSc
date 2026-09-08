# Piscine MSc

Depot de suivi de la piscine MSc : exercices, notes et rendus au fil des semaines.

## Structure

```
piscine_MSc/
├── day00/
│   └── ex00/
│       ├── README.md
│       └── main.py
├── day01/
│   └── ...
├── templates/
│   └── exercise/        # gabarit copie a chaque nouvel exercice
├── scripts/
│   └── new_exercise.sh  # cree un nouveau dayXX/exXX depuis le gabarit
├── .gitignore
└── README.md
```

Chaque jour = un dossier `dayXX/`. Chaque exercice = un sous-dossier `exXX/`
avec son propre `README.md` (enonce/approche) et son code.

## Environnement

- Python 3.14 (`python3 --version`)
- Un environnement virtuel par defaut a la racine :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # a creer/completer au fil des exercices
```

`.venv/` est ignore par git (voir `.gitignore`).

## Creer un nouvel exercice

```bash
./scripts/new_exercise.sh 01 02   # cree day01/ex02/ depuis templates/exercise/
```

## Methode de travail quotidienne

1. `./scripts/new_exercise.sh <day> <ex>` — scaffold l'exercice
2. Lire l'enonce, le noter dans le `README.md` de l'exercice
3. Developper dans `dayXX/exXX/`
4. Tester (`python3 main.py`, `pytest` si applicable)
5. `git add dayXX/exXX`
6. `git commit -m "..."` (voir convention ci-dessous)
7. `git push`

## Convention de commits

Format : `dayXX: exXX - resume court`

Exemples :
```
day00: ex00 - setup environnement et structure du repo
day01: ex02 - implementation de la fonction de tri
day01: ex03 - correction bug sur les cas limites
```

Un commit = un exercice (ou une correction ciblee). Eviter les commits
fourre-tout regroupant plusieurs jours/exercices.

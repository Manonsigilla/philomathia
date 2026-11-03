# Philomathia

Projet de remise à niveau en mathématiques pour la Data Science et l'intelligence
artificielle. L'idée est de revoir les notions de base (algèbre linéaire, probabilités,
statistiques, dérivées) et de les manipuler directement en Python, avant d'attaquer
le Machine Learning.

## Contexte

Ce projet a été réalisé dans le cadre de ma formation en Bachelor 2 Data & IA. Le but
n'est pas d'apprendre les formules par cœur, mais de comprendre à quoi elles servent
et de savoir les utiliser concrètement avec `numpy`, `pandas`, `matplotlib` et `sympy`.
Il se découpe en deux parties : une veille sur les notions mathématiques, puis une
série d'exercices sur un notebook Python.

## Pourquoi les maths sont importantes pour la Data Science

- **Les vecteurs et les matrices** servent à représenter les données. Chaque ligne d'un
  tableau est un vecteur, le tableau entier est une matrice. Les opérations matricielles
  sont partout : régression, réseaux de neurones, traitement d'images...
- **Les probabilités et les statistiques** permettent de gérer l'incertitude, de décrire
  les données et de comprendre les modèles (biais, variance, échantillonnage).
- **La moyenne, la médiane, les quartiles et les boxplots** donnent une première idée
  d'un jeu de données, de sa dispersion et des valeurs aberrantes. C'est indispensable
  avant de nettoyer ou de modéliser.
- **La corrélation** aide à repérer des variables liées et donc redondantes. Attention,
  corrélation ne veut pas dire causalité.
- **Le théorème central limite** explique pourquoi les moyennes d'échantillons se
  comportent bien, ce qui est à la base des intervalles de confiance et des tests.
- **La dérivée** est le cœur de l'optimisation, et donc de la descente de gradient
  utilisée pour entraîner les modèles.

Bref, sans ces bases, on peut exécuter du code de Machine Learning, mais difficilement
comprendre ce qu'il fait.

## Veille scientifique

La veille est dans [`veille.md`](veille.md). Pour les 12 notions demandées, j'ai donné
une définition, un exemple et une reformulation simple pour un public non spécialiste :
vecteur, matrice, probabilité et loi de probabilité, variables indépendantes, espérance,
variance et écart type, corrélation linéaire, moyenne/médiane/max/min, quartiles,
boxplot, histogramme, théorème central limite et dérivée.

## Travail réalisé dans le notebook

Le fichier [`Philomathia.ipynb`](Philomathia.ipynb) contient les 18 jobs (0 à 17) :

| Partie | Jobs | Contenu |
|---|---|---|
| Algèbre linéaire | 0 à 9 | vecteurs, matrices, dimensions, transposée, produit matriciel, matrice identité, inverse et déterminant |
| Probabilités et statistiques | 10 à 16 | simulations, probabilités d'événements, statistiques descriptives, histogramme, boxplot, analyse du jeu de données Wine, loi normale |
| Dérivées | 17 | calcul formel de 8 dérivées avec SymPy |
| Bonus | 1 et 2 | simulation du théorème central limite, quatre algorithmes de tri |

Quelques résultats :

- le produit matriciel n'est possible que si le nombre de colonnes de la première
  matrice est égal au nombre de lignes de la seconde ;
- l'inverse d'une matrice n'existe que pour une matrice carrée dont le déterminant
  est non nul ;
- sur 100 lancers de pièce simulés, j'obtiens environ 44 % de « Pile » et 56 % de
  « Face », ce qui est proche de 50/50 ;
- pour le vecteur `R` (450 valeurs entre 0 et 9) : moyenne ≈ 4,42, médiane = 4,
  variance ≈ 8,52 et écart type ≈ 2,92 ;
- dans le jeu de données Wine (178 lignes, 13 variables), les échelles sont très
  différentes (proline ≈ 1000, hue ≈ 1), et certaines variables sont fortement
  corrélées (`flavanoids` et `total_phenols` ≈ 0,86) ;
- la simulation du TCL donne des moyennes centrées autour de 5, avec un écart type
  d'environ 0,50, proche de la valeur théorique `10 / sqrt(12 × 30) ≈ 0,53`.

## Fichiers du projet

```
philomathia/
├── Philomathia.ipynb   # notebook des exercices (exécuté)
├── veille.md           # veille scientifique sur les 12 notions
├── presentation.pptx   # diapositives avec notes pour l'oral
├── README.md           # ce fichier
├── central_limit.py    # bonus 1 : simulation du TCL
└── sorts.py            # bonus 2 : algorithmes de tri
```

## Lancer le projet

```bash
# Créer et activer l'environnement virtuel
python -m venv .venv
.venv\Scripts\activate          # Windows (PowerShell / CMD)
source .venv/Scripts/activate   # Git Bash

# Installer les dépendances
pip install numpy pandas sympy matplotlib scikit-learn notebook

# Lancer le notebook
jupyter notebook Philomathia.ipynb
```

Dans VS Code, sélectionner le kernel `.venv (Python 3.11)`, puis faire
« Restart Kernel » > « Run All ». Le notebook s'exécute de haut en bas sans erreur.
Les deux fichiers `.py` du bonus sont importés depuis le notebook, donc il faut
lancer Jupyter depuis le dossier du projet.

---

Manon — Bachelor 2 Data & IA

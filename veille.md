# Veille scientifique — Philomathia

Dans le cadre du projet Philomathia, je me suis intéressée aux notions mathématiques
qui servent de base au Machine Learning. Pour chaque notion, je donne une définition,
au moins un exemple, puis une reformulation simple pour quelqu'un qui n'est pas
spécialiste (avec une image, une analogie ou une situation concrète).

---

## 1. Un vecteur

**Définition.** Un vecteur est un objet mathématique qui regroupe plusieurs nombres
dans un ordre donné. En dimension $n$, on l'écrit $v = (x_1, x_2, \dots, x_n)$ et on
dit que $v \in \mathbb{R}^n$. En géométrie, un vecteur possède une direction, un sens
et une longueur (sa norme). On peut l'additionner à un autre vecteur, le multiplier
par un nombre (un scalaire), et calculer des distances entre vecteurs.

**Exemple.** $v = (4, 1, 9)$ est un vecteur ligne de dimension 3. En physique, un
déplacement de 3 m vers la droite et de 2 m vers le haut se note $w = (3, 2)$.
En data, chaque ligne d'un tableau (un individu décrit par plusieurs variables) est
un vecteur.

**Pour vulgariser.** Un vecteur, c'est comme une fiche de renseignements : chaque case
donne une information sur le même objet. Si je relève les températures à 8 h, 12 h et
18 h, j'obtiens le vecteur $(12, 18, 15)$ : trois nombres, mais une seule et même
journée.

---

## 2. Une matrice

**Définition.** Une matrice est un tableau rectangulaire de nombres organisé en lignes
et en colonnes. Une matrice $A$ à $m$ lignes et $n$ colonnes est de dimension $m \times n$
et on note $A = (a_{i,j})$, où $a_{i,j}$ est l'élément situé à la ligne $i$ et à la
colonne $j$. Le produit matriciel, la transposée et l'inverse sont les opérations
usuelles. Une matrice peut représenter une application linéaire, un système
d'équations ou un jeu de données.

**Exemple.** $M = \begin{pmatrix} 1 & 2 \\ 5 & 6 \end{pmatrix}$ est une matrice
$2 \times 2$ (donc carrée). Un jeu de données comme celui des vins (178 individus,
13 variables) est une matrice de dimension $178 \times 13$.

**Pour vulgariser.** C'est un tableau Excel : les lignes sont les élèves et les
colonnes les matières. La matrice, c'est le tableau complet. Quand on multiplie deux
matrices, on combine ces tableaux, un peu comme on applique deux transformations
l'une après l'autre.

---

## 3. Une probabilité, une loi de probabilité

**Définition.** La probabilité d'un événement $A$ est un nombre réel compris entre
0 et 1 qui mesure ses chances de se produire. On la note $P(A)$, avec $P(\Omega) = 1$
pour l'ensemble de tous les résultats possibles. Pour deux événements incompatibles,
$P(A \cup B) = P(A) + P(B)$. Une loi de probabilité décrit comment se répartissent
les chances sur les différentes valeurs possibles d'une variable aléatoire
(par exemple la loi uniforme ou la loi normale).

**Exemple.** Pour un dé non truqué à 6 faces, $P(3) = \frac{1}{6}$. La loi uniforme
sur $\{1,\dots,6\}$ associe la même probabilité $\frac{1}{6}$ à chaque face. La loi
normale, elle, est une loi continue en forme de cloche.

**Pour vulgariser.** Une probabilité de 70 % de pluie ne veut pas dire qu'il va
pleuvoir à coup sûr : ça veut dire que dans des journées similaires, il pleut environ
7 fois sur 10. Une loi de probabilité, c'est la carte de répartition des chances sur
tous les résultats possibles.

---

## 4. Des variables indépendantes

**Définition.** Deux variables aléatoires $X$ et $Y$ sont indépendantes si, pour toutes
valeurs $x$ et $y$, on a $P(X = x \text{ et } Y = y) = P(X = x) \times P(Y = y)$.
Connaître la valeur de l'une n'apporte aucune information sur l'autre.

**Exemple.** Si je lance deux dés, le résultat du premier dé et celui du second sont
indépendants : $P(\text{dé 1} = 3 \text{ et dé 2} = 5) = \frac{1}{6} \times \frac{1}{6}$.
En revanche, la température extérieure et la consommation de chauffage ne sont pas
indépendantes.

**Pour vulgariser.** C'est comme deux ami(e)s qui choisissent leur plat sans se
concerter : le choix de l'un ne donne aucune indication sur le choix de l'autre.
À l'inverse, deux personnes qui partagent le même parapluie ne sont pas
indépendantes : si l'une est mouillée, l'autre a de grandes chances de l'être aussi.

---

## 5. Une espérance, une variance et un écart type

**Définition.** Pour une variable aléatoire discrète $X$ prenant les valeurs $x_i$
avec les probabilités $p_i$ :

- l'espérance est $E(X) = \sum_i x_i\, p_i$ (la valeur moyenne attendue sur le long terme) ;
- la variance est $\mathrm{Var}(X) = E\big[(X - E(X))^2\big] = E(X^2) - E(X)^2$
  (la dispersion autour de la moyenne) ;
- l'écart type est $\sigma(X) = \sqrt{\mathrm{Var}(X)}$, exprimé dans la même unité que $X$.

**Exemple.** Pour un dé équilibré : $E(X) = \frac{1+2+3+4+5+6}{6} = 3{,}5$.
La variance vaut $\frac{35}{12} \approx 2{,}92$ et l'écart type $\sigma \approx 1{,}71$.

**Pour vulgariser.** L'espérance, c'est la note que je m'attends à avoir en moyenne
sur beaucoup de contrôles. L'écart type dit si je suis régulière (petit écart type)
ou si mes notes varient beaucoup (grand écart type).

---

## 6. Une corrélation linéaire

**Définition.** La corrélation linéaire mesure la force et le sens d'une relation
linéaire entre deux variables quantitatives. Le coefficient de Pearson est

$$r = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

Il est compris entre $-1$ et $1$. Il vaut $1$ quand les points sont parfaitement
alignés sur une droite croissante, $-1$ sur une droite décroissante, et $0$ quand il
n'y a pas de relation linéaire. Attention : $r$ ne mesure que les relations
linéaires, et corrélation ne signifie pas causalité.

**Exemple.** La taille et le poids des personnes sont en général positivement
corrélées. Dans le jeu de données des vins, `flavanoids` et `total_phenols` sont
fortement corrélées (environ 0,86).

**Pour vulgariser.** « Quand l'un monte, l'autre monte aussi. » Mais ça ne dit pas
qui cause quoi : en été, les ventes de glaces et les noyades augmentent en même
temps, ce n'est évidemment pas la glace qui provoque les noyades. Le vrai facteur
commun, c'est la chaleur.

---

## 7. Une moyenne, une médiane, un maximum, un minimum

**Définition.**

- La moyenne est la somme des valeurs divisée par leur nombre : $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$.
- La médiane est la valeur qui coupe les données en deux : 50 % des valeurs sont
  en dessous, 50 % au-dessus.
- Le maximum et le minimum sont les valeurs extrêmes de l'échantillon.

**Exemple.** Notes $[8, 12, 15, 17]$ : moyenne $= 13$, médiane $= 13{,}5$, minimum
$= 8$, maximum $= 17$. Si on ajoute une note de $100$, la moyenne passe à $30{,}4$
mais la médiane reste à $13{,}5$.

**Pour vulgariser.** Une seule personne très riche peut faire monter le salaire moyen
d'une entreprise, alors que le salaire médian reste le salaire « du milieu ». C'est
pour ça qu'on regarde souvent la médiane : elle est moins sensible aux valeurs
extrêmes.

---

## 8. Les quartiles en statistique

**Définition.** Les quartiles partagent un échantillon trié en quatre parties de
même effectif. Le premier quartile $Q_1$ est la valeur sous laquelle se trouvent
25 % des données ; le deuxième quartile $Q_2$ est la médiane (50 %) ; le troisième
quartile $Q_3$ est la valeur sous laquelle se trouvent 75 % des données.

**Exemple.** Pour l'échantillon $R$ du notebook, `np.percentile(R, [25, 50, 75])`
donne approximativement $Q_1 = 2$, $Q_2 = 4$ et $Q_3 = 7$.

**Pour vulgariser.** Imagine une file d'attente rangée par ordre de taille : les
quartiles sont les personnes qui séparent la file en quatre groupes de même taille.
$Q_1$ est la fin du premier quart, $Q_3$ le début du dernier.

---

## 9. Boxplot en statistique

**Définition.** Le boxplot (boîte à moustaches) est une représentation graphique de
la dispersion d'une série statistique. La boîte va de $Q_1$ à $Q_3$ et contient 50 %
des données ; le trait à l'intérieur indique la médiane. Les moustaches s'étendent
jusqu'aux valeurs extrêmes non aberrantes, et les points isolés au-delà représentent
les valeurs aberrantes.

**Exemple.** Le boxplot de $R$ montre une boîte centrée autour de la médiane et des
points éventuels en dehors des moustaches.

**Pour vulgariser.** C'est une photo de la répartition : la boîte montre où se trouve
la moitié centrale des données, les moustaches montrent jusqu'où ça s'étend, et les
points isolés signalent les cas inhabituels (par exemple un prix beaucoup plus élevé
que les autres dans une liste d'appartements).

---

## 10. Histogramme en statistique

**Définition.** Un histogramme est un graphique qui regroupe les valeurs d'une
variable continue en intervalles (appelés classes ou bins), puis compte combien de
valeurs tombent dans chaque intervalle. Les barres sont contiguës. Sa forme dépend
du nombre de classes choisi, ce qui est une limite à garder en tête.

**Exemple.** L'histogramme des 450 valeurs de $R$, avec 10 classes, montre que les
valeurs sont à peu près uniformément réparties entre 0 et 9.

**Pour vulgariser.** C'est comme ranger les notes d'une classe par tranches
(0–5, 5–10, 10–15, 15–20) et compter combien d'élèves sont dans chaque tranche. On
voit tout de suite où se concentre la classe.

---

## 11. Le théorème central limite

**Définition.** Soient $X_1, X_2, \dots, X_n$ des variables aléatoires indépendantes
et de même loi, d'espérance $\mu$ et d'écart type $\sigma$ finis. Alors, quand $n$
devient grand, la moyenne empirique $\bar{X}_n$ suit approximativement une loi
normale de moyenne $\mu$ et d'écart type $\frac{\sigma}{\sqrt{n}}$ :

$$\bar{X}_n \approx \mathcal{N}\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$$

**Exemple.** Si je fais la moyenne de groupes de 30 lancers d'un dé, les moyennes
obtenues se répartissent en cloche autour de 3,5. Plus le groupe est grand, plus les
moyennes sont resserrées. C'est aussi ce qui explique que la moyenne d'un grand
échantillon soit un bon estimateur de la moyenne de la population.

**Pour vulgariser.** Si je pèse un seul objet, le résultat est imprévisible. Si je
pèse des groupes de 30 objets et que je fais la moyenne, les moyennes se rapprochent
de la vraie valeur et se répartissent en cloche. C'est le TCL qui dit pourquoi les
erreurs se compensent quand on accumule beaucoup d'observations.

---

## 12. Une dérivée

**Définition.** La dérivée d'une fonction $f$ en un point $x$ est la limite du taux
de variation :

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Elle correspond à la pente de la tangente à la courbe au point $x$, c'est-à-dire au
taux de variation instantané de $f$. Règles utiles : $(x^n)' = n x^{n-1}$,
$(e^x)' = e^x$, $(\ln x)' = \frac{1}{x}$, $(\sin x)' = \cos x$.

**Exemple.** Pour $f(x) = 3x^2 - 2x + 5$, on obtient $f'(x) = 6x - 2$. En physique,
la dérivée de la position par rapport au temps est la vitesse instantanée.

**Pour vulgariser.** C'est le compteur de vitesse de la voiture : la position dit où
on est, la dérivée par rapport au temps dit à quelle vitesse on roule à cet instant
précis. En Machine Learning, la dérivée sert à savoir dans quelle direction modifier
les paramètres pour faire diminuer l'erreur.

---

## Sources

- *Mathematics*, Wikipedia (encyclopédie libre).
- *Mathématiques*, Larousse 2023.
- NumPy : *The absolute basics for beginners* et documentation officielle.
- Tutoriel Python : calculs matriciels ; *Calcul matriciel*.
- *L'essentiel pour comprendre les probabilités* ; *Statistiques et probabilités*.
- *Dérivation* ; *Calculer la dérivée en Python*.
- *Algorithmes de tri : le problème du tri*.

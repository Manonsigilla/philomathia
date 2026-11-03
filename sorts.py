"""Quelques algorithmes de tri (job bonus 2)."""


def bubble_sort(lst):
    """Tri à bulles, complexité O(n²)."""
    lst = lst.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(lst):
    """Tri par insertion, complexité O(n²)."""
    lst = lst.copy()
    for i in range(1, len(lst)):
        valeur = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > valeur:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = valeur
    return lst


def merge_sort(lst):
    """Tri fusion, complexité O(n log n)."""
    if len(lst) <= 1:
        return lst
    milieu = len(lst) // 2
    gauche = merge_sort(lst[:milieu])
    droite = merge_sort(lst[milieu:])
    return _fusion(gauche, droite)


def _fusion(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    return resultat + gauche[i:] + droite[j:]


def quick_sort(lst):
    """Tri rapide, complexité O(n log n) en moyenne."""
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    plus_petits = [x for x in lst if x < pivot]
    egaux = [x for x in lst if x == pivot]
    plus_grands = [x for x in lst if x > pivot]
    return quick_sort(plus_petits) + egaux + quick_sort(plus_grands)

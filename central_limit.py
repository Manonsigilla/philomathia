"""Simulation du théorème central limite (job bonus 1)."""

import numpy as np
import matplotlib.pyplot as plt


def simuler_moyennes(n_echantillons=1000, taille=30, loi="uniforme"):
    """Tire n échantillons de taille donnée et renvoie leurs moyennes."""
    if loi == "uniforme":
        donnees = np.random.uniform(0, 10, size=(n_echantillons, taille))
    else:
        donnees = np.random.exponential(1, size=(n_echantillons, taille))
    return donnees.mean(axis=1)


def afficher(moyennes):
    """Affiche l'histogramme des moyennes d'échantillons."""
    plt.hist(moyennes, bins=30, density=True, edgecolor="white")
    plt.title("Distribution des moyennes d'échantillons")
    plt.xlabel("Moyenne")
    plt.ylabel("Densité")
    plt.show()

#### Imports et définition des variables globales
"""
Module principal pour l'exercice d'encodage ASCII art.

Ce fichier contient les implémentations itérative (artcode_i) et
récursive (artcode_r) de la fonction d'encodage de chaîne,
ainsi qu'une fonction main() pour les tester.
"""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en 
       argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    lettres = [s[0]]
    occurence = [1]
    for i in range(1,len(s)):
        if s[i] == s[i-1] :
            occurence[-1] +=1
        else:
            lettres.append(s[i])
            occurence.append(1)
    combine = zip(lettres,occurence)
    return list(combine)


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
       selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    if len(s) == 0 :
        return []
    premier_caractere = s[0]
    compteur = 0
    i = 0
    while i < len(s) and s[i] == premier_caractere:
        compteur += 1
        i += 1
    chaine_restante = s[i:]
    return [(premier_caractere, compteur)] + artcode_r(chaine_restante)


#### Fonction principale


def main():
    """
    Exécute des appels de test aux fonctions 'artcode_i' et 'artcode_r' 
    pour vérifier et afficher leur sortie sur une chaîne d'exemple.

    Args:
        Aucun.

    Returns:
        Rien.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

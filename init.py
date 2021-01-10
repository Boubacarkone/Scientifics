#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Fonction init servant à charger les donées à traiter par l'application.
'''
import pathlib
from os import path
import json
import re
from time import sleep
from progress.bar import Bar

def startswiths(chaine, *args):
    for i in args:
        if chaine.startswith(i) == True:
            return True    
    return False

def enlever_parent(chaine):
    '''
    Fonction servant à enlever les noms d'université ou villes entre parenthèses.
    '''
    m = re.compile(r'\(\w\)')#Expression régulière pour les (1) ou (nombres).
    chaine = m.sub('', chaine)
    ovr = chaine.find("(")
    fer = chaine.find(")")
    if  ovr != -1 and fer != -1:

        if ovr < fer:#Vérifier la présence de parenthèse.
            chaine = chaine[0:ovr+1] + chaine[fer:len(chaine)]
            chaine = chaine.replace('()', "")
            chaine = enlever_parent(chaine)
        elif ovr > fer:
            chaine = chaine[0:fer] + enlever_parent(chaine[ovr : len(chaine)])

    if ovr != -1 and fer == -1:
        chaine = enlever_parent(chaine + ')')
    return chaine

def spliter(chaine):
    '''
    Fonction servant à transformer la chaine des noms d'auteurs, en liste.
    '''
    chaine = chaine.replace(' and ', ',')
    chaine = chaine.replace('  ', ',')
    chaine = chaine.replace(' amd ', ',')
    chaine = chaine.replace(' & ', ',')
    chaine = chaine.replace('..', '.')
    liste = [i.strip() for i in chaine.split(',')]
    for i in liste:
        if ')' in i or i == '':
            liste.remove(i)
    return liste

def correction_noms(dico):
    '''
    Cette fonction va servir à corriger certains noms d'auteur taper en latex.
    '''
    with open('./data/dico_correction.txt', 'r') as f:
        dico_correction = json.load(f)
        for cle in dico:
            if cle in dico_correction:
                dico[cle] = dico_correction[cle]

def write(data_file, nom):
    '''
    Méthode pour l'écriture des variables liste et dico dans un fichiers.
    '''
    dossier = path.dirname(__file__)
    chemin = path.join(dossier, 'data', nom)
    with open(chemin, 'w') as data:
        data.write(json.dumps(data_file))

def initialiser(dossier, reference):
    '''
    Cette fonction va travailler les fichiers articles, et le fichier citations.
    Pour creer un fichier articles.txt contenant un dictionnaire dont les clefs
    seront des reférences d'articles et les valeurs la liste d'auteurs.
    Puis creer un autre fichier citations.txt qui va contenir la liste des citations.
    '''
    ##Traitement des citations:
    with open(reference, "r") as citation:
        liste = []
        for ligne in citation:
            ligne = ligne.split()
            liste.append(ligne)

    ##Traitement des articles:
    dico = {}
    extension = r"**/*.abs"
    fichiers_abs = [str(i) for i in pathlib.Path(dossier).glob(extension)]
    with Bar('Chargement des articles',max = len(fichiers_abs)) as bar:

        for fichier in fichiers_abs: #Boucle sur les chemins de fichiers
            sleep(0.000001)
            bar.next()
            with open(fichier, "r") as fabs:# Ouverture de chaque fichier
                lignes = fabs.readlines()
                chaine = ''

                for i in range(2, len(lignes)):
                    #Recherche de la chaine commençant par 'Authors' ou 'author'.
                    if lignes[i].startswith('Authors') == True:
                        chaine = lignes[i][9:-1]

                        if startswiths(lignes[i + 1], "Comment", "Journal", "Note", "Report", "Subj", "\\\\", "Title") == False:
                            chaine = chaine +' '+ lignes[i + 1][0:-1].strip()

                            if startswiths(lignes[i + 2], "Comment", "Journal", "Note", "Report", "Subj", "\\\\", "Title") == False:
                                chaine = chaine +' '+ lignes[i + 2][0:-1].strip()
                            #On s'arrête ici car souvent les noms d'auteurs ne depasse pas trois lignes.
                    elif lignes[i].startswith("Author") == True:
                        chaine = lignes[i][8:-1]

                        if startswiths(lignes[i + 1], "Comment", "Journal", "Note", "Report", "Subj", "\\\\", "Title") == False:
                            chaine = chaine +' '+ lignes[i + 1][0:-1].strip()
                            if startswiths(lignes[i + 2], "Comment", "Journal", "Note", "Report", "Subj", "\\\\") == False:
                                chaine = chaine +' '+ lignes[i + 2][0:-1].strip()

                    chaine = enlever_parent(chaine)
                    dico[path.basename(fichier)[0:7]] = spliter(chaine)

        # Correction des noms d'auteurs.
        correction_noms(dico)

        # Ecriture dans les fichiers articles.tx et citations.txt
        write(dico, 'articles.txt')
        write(liste, 'citations.txt')
        return print(f"\n\nDonnées chargées: \
    {len(dico)} articles    et     {len(liste)} citations.")

if __name__ == '__main__':
    pass
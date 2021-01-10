#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:13:48 2020
@author: kone
"""
import json
from os import path

def load(data_file):
    '''
    Méthode pour le chargement des données qui sont dans le dossier data à traiter.
    '''
    dossier = path.dirname(__file__)
    chemin = path.join(dossier, 'data', data_file)
    with open(chemin, 'r') as data:
        return json.load(data)

class Authors:
    '''
    Class authors avec deux méthodes utiles pour la suite.
    '''
    dico = load('articles.txt')
    lval = list(dico.values())

    def trouver_clefs(self, valeur):
        '''
        Trouver la ou les clés corespondantes à une valeur donnée.
        '''
        self.valeur = valeur
        l = []
        for cle, val in self.dico.items():
            if valeur == val:
                l.append(cle)
        return l

    def liste_arts_pubs(self, nom):
        '''
        Donne la liste des references d'articles publiés par un auteur donné.
        Même si l'auteur se trouve parmis plusieurs auteurs de l'articles.
        '''
        self.nom = nom
        liste = []
        for item in self.lval:
            for i in item:
                if nom.replace(" ", "").lower() == i.replace(" ", "").lower():
                    liste += self.trouver_clefs(item)
        return list(set(liste)) 

if __name__ == "__main__":
    pass
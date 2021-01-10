#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Création d'un graphes orienté de citations entre les articles.
'''
from pprint import pprint as pp
import networkx as nx
from progress.bar import Bar
import auteurs as aut


edges = aut.load('citations.txt')
nodes = list(aut.Authors.dico.keys())

def ajout_dico(dico, key, val):
    if key not in dico.keys():
        dico[key] = val
    else:
        if val > dico[key]:
            dico[key] = val
        else:
            pass


class Graphe_Citations(aut.Authors, nx.DiGraph):
    '''
    Class du graphe de citations
    '''
    def __init__(self):
        nx.DiGraph.__init__(self)
        self.add_nodes_from(nodes)
        self.add_edges_from(edges)

    def cite(self, auth):
        '''
        On définit cette méthodes à l'aide de la méthode liste_arts_pubs,
        afin de recupérer la liste des articles publiés par l'auteur auth.
        Et de la mthéode successors da la class Graphe de networkx.
        '''
        self.auth = auth
        liste_art = self.liste_arts_pubs(auth)
        l_aut = set()
        if liste_art != []:
            for item in liste_art:
                #Recherche des successeurs d'item.
                l = list(self.successors(item))
                if len(l) != 0:
                    for i in l:
                        if i not in liste_art:
                            for j in self.dico[i]:
                                l_aut.add(j)

            if l_aut == []:
                return f"l'auteur {auth} ne cite aucun auteurs étudiés !"
            print(f"Voici la liste des auteurs cités par {auth} : \n\n")
            return list(set(l_aut))
        return f"L'auteurs {auth} n'est pas parmi les auteurs étudiés."
    def influences_part(self, auth, N=None):
        '''
        Méthode sortant un dictionnaire pondérer des auteurs influencés par un auteur donné.
        La pondération représente l'intensité de cette influence.
        '''
        self.auth = auth
        self.N = N
        result = {}
        l_arts = self.liste_arts_pubs(auth) #liste des articles publié par auth.
        if l_arts != []:
            for item in l_arts:
                #Itérateur des articles x qui sont telque x D item avec une profondeur au plus N.
                ite = set(nx.single_target_shortest_path_length(self, item, N))
                for i in ite:
                    if i[0] not in l_arts:
                        intensite = 0
                        #Calcul de l'intensité.
                        if i[1] != 0:
                            intensite += round(1/i[1], 3)
                        for nom in self.dico[i[0]]:
                            #Trier et terminer le calcul d'intensité en faisant 
                            # les sommes quand il le faut.
                            #Ajout des noms d'auteurs influencés dans le dictionnaire result.
                            if nom not in result.keys():
                                result[nom] = intensite
                            else:
                                result[nom] = round(result[nom] + intensite, 3)
            return result
        return f"L'auteurs {auth} n'est pas parmi les auteurs étudiés."

    def qui_influences(self, auth, N=None):
        '''
        Sort la liste des autheurs qui influent l'auteur auth avec une pondération.
        La pondération représente l'intensité de cette
        '''
        self.auth = auth
        self.N = N
        result = {}
        l_arts = self.liste_arts_pubs(auth) #liste des articles publié par auth.
        if l_arts != []:
            for item in l_arts:
                #Pour chaque articles publié chercher tous les articles y.
                #Telque item D y avec une profondeur au plus N.
                for i in nx.single_source_shortest_path_length(self, item, N).items():
                    #Il ne reste plus qu'à faire exactement les même étape
                    #que pour la méthode précédante.
                    if i[0] not in l_arts:
                        intensite = 0
                        if i[1] != 0:
                            intensite += round(1/i[1], 3)
                        for nom in self.dico[i[0]]:
                            if nom not in result.keys():
                                result[nom] = intensite
                            else:
                                result[nom] = round(result[nom] + intensite, 3)
            return result
        return f"L'auteurs {auth} n'est pas parmi les auteurs étudiés."
    def communaute(self, auth, N = None):
        '''
        Sort la liste des communautés au tours de auth.
        '''
        self.auth = auth
        self.N = N
        inf_part = self.influences_part(auth, N)
        e_inf = self.qui_influences(auth, N)
        if type(inf_part) != str:
            inf_part = set(inf_part)
            e_inf = set(e_inf)
            if N == None:
                print(f"Voici la communauté auteur de {auth}: \n\n")
            else:
                print(f"Voici la communauté auteur de {auth} \
avec une prondeur au plus {N}: \n\n")
            return inf_part.intersection(e_inf)
        return f"L'auteurs {auth} n'est pas parmi les auteurs étudiés."



if __name__ == "__main__":
    pass
    

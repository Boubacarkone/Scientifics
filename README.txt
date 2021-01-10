Scientifics


Résumé:______________________________________________________________________ 

  L’application scientifics est une application python qui a été créer afin 
d’étudier une communauté de scientifiques ; physiciens et mathématiciens. 
Mais part sa conception elle est bien sûre capable aussi de traiter tout 
autre communauté constituer d’auteurs qui se citent entre eux. 
L’application travaille donc sur des données afin d’en sortir certaines 
informations, le détaille de cela sera dans la partie Fonctionnement. 

Fonctionnement :_____________________________________________________________
  Scientifics est une application qui fonctionne en ligne de commandes, sans 
interface graphique. Elle dispose 5 opérateurs ou fonctions ; init, 
clean data, influences_part, qui_influences, et communaute. 

Détaillons le rôle de chacune ces opérateurs. 

Dans un terminal pour utiliser l'application il faut se placer dans
Le dossier Scientifics puis exécuter une fonctions de la sorte, 
./Scientifics opérateur argument1 argument2 ...etc.

Init-------------------------------------------------------------------------
  IMPORTANT : Au lentement de l’application il faut lui donner les données sur 
	     lesquelles elle va travailler ceci se fait via la fonction init. 

   Elle a besoin de deux types de données ;
1) Un dossier contenant des articles, 
classés par années. Les articles seront des fichiers nommés « référence.abs », 
la référence correspond au numéro de référence de l’article. 
Ces fichiers doivent être écrits d’une certainement manière, 
voici l’exemple du fichier « 9709177.abs » qui donne ce qui suit entre
guillemet : 
"
------------------------------------------------------------------------------
\\
Paper: hep-th/9709177
From: selipsky@jdub.wustl.edu (Stephen B. Selipsky)
Date: Wed, 24 Sep 1997 23:18:32 GMT   (31kb)
Date (revised): Mon, 10 Nov 1997 17:24:38 GMT

Title: Analyzing Chiral Symmetry Breaking in Supersymmetric Gauge Theories
Authors: Thomas Appelquist (1), Andreas Nyffeler (1 and 2) and Stephen B.
  Selipsky (1 and 3) ((1) Yale University, (2) DESY-Zeuthen, (3) Washington
  University, St. Louis)
Comments: LaTex, 14 pages, including 1 figure in EPS format. Revised to correct
  gluino anomalous dimension, with minor accompanying text changes
Report-no: YCTP-P12-97, WUSTL-HEP-97-55
Journal-ref: Phys.Lett. B425 (1998) 300-308
\\
  We compare gap equation predictions for the spontaneous breaking of global
symmetries in supersymmetric Yang-Mills theory to nonperturbative results from
holomorphic effective action techniques. In the theory without matter fields,
both approaches describe the formation of a gluino condensate. With $N_f$
flavors of quark and squark fields, and with $N_f$ below a certain critical
value, the coupled gap equations have a solution for quark and gluino
condensate formation, corresponding to breaking of global symmetries and of
supersymmetry. This appears to disagree with the newer nonperturbative
techniques, but the reliability of gap equations in this context and whether
the solution represents the ground state remain unclear.
\\

"
Les articles de notre communauté scientifique se trouve sur ce lien : 
https://math.univ-angers.fr/~ducrot/pyds1/data/hep-th-abs.tar.gz

2) Elle a aussi besoin d’un fichier recensant toutes les références d’un article 
vers un autre. Celui de notre communauté scientifique est sur le lien :  
https://math.univ-angers.fr/~ducrot/pyds1/data/hep-th-citations.tar.gz

   Pour utiliser l'application sur les données ainsi recueillies on fait 
Appelle à la fonction init qui prend deux arguments : le premier argument doit 
être un chemin vers le dossier articles et le deuxième arguments un chemin vers 
le fichier de référencement.
Par exemple : 
python Scientifics init /.../Documents/hep-th-abs /Users/.../citations.txt

clean data -------------------------------------------------------------------
  ATTENTION : Cette fonction a un nom composé de deux mots clean et data.
Elle nettoie l'application, c'est à dire supprime toutes les données chargées
par la fonction init.
Bien sûre que cela n'est pas nécessaire pour passer d'une donnée à autre, car
la fonction init écrase les anciennes données à chaque utilisation. Mais 
clean data peut être utile si l'on souhaite supprimer nos données après étude 
pour une raison ou autre.

qui_influences ---------------------------------------------------------------
  Cette fonction sort la liste des auteurs qui ont une influence sur l'auteur
qui lui a été donné en argument. On peut ajouter un entier n en argument 
supplémentaire si l'on souhaite dicider de la profondeur de la recherche des
influenceurs. Voici son appelle : 

Python Scientifics qui_influences 'nom prénom' n = facultatif. 

  J'ai dis la liste,en réalité il s'agit d'un dictionnaire pondérer car nous
nous intéressons aussi à l'intensité de l'influence. Donc parmi les
résultats les nombres que vous allez voire en face de chaque auteurs
correspond donc à cette intensité. 

  Maintenant voici la façon dont est calculer cette intensité :
Pour un auteur A qui influe un auteur B. Imaginons que A et B soient des
ensembles au sens mathématique contenant des articles écrits par A et B.
Pour le calcul de l'intensité nous prendre chaque article de A et calculer 
L'inverse de la longueur de la chaines la plus courte entre cet article et 
tous les autres articles de B puis nous faisons la sommes ces résultats.
Le totale représente alors l'intensité de l'influence. 
  Cette intensité montre la proximité des deux auteurs une sorte de distance
inversé car plus L'intensité augmente, plus les deux auteurs sont proches. 
Et nous pouvons remarque que l'intensité augmente lors que les articles de A
et de B sont proches et si plusieurs articles de A atteignent des articles de
B.

influences_part --------------------------------------------------------------
  Cette fonction ressemble beaucoup a la précédente, sauf que celle-ci sort la 
la liste ou plutôt le dictionnaire pondéré dans auteurs qui sont influencés 
par l'auteur donner en argument, on peut aussi limiter la profondeur de 
recherche en rajoutant un argument n, un entier facultatif. 
La façon de l'appeler est identique à l'autre sauf qu'il faut mettre
influcences_part à la place de la fonction précédente. 

communaute -------------------------------------------------------------------
  La fonction communaute sort la liste des auteurs qui sont autours de 
l'auteur qui lui a été donné en argument, encore une fois un peut aussi 
limiter cette rechercher à une profondeur désirée n, un entier.
  Il s'agit de la liste des auteurs qui influent un auteur donné et qui sont 
à leurs tours influencés par cette auteur. La façon d'appeler cette fonction
est aussi identique aux autres fonctions.

cite -------------------------------------------------------------------------
   La fonction cite sort la liste des auteurs cités par l'auteur qui lui a été 
donné en argument. Il y a pas d'argument de profondeur car il s'agit des 
auteurs cité directement par un auteur donné. 

----------------------------Fin fonctinnement---------------------------------

Ce paragraphe est spécifique au données pour laquelle l'application a tété 
créée à savoir la Communauté scientifique dont nous souhaitons étudier.
Parmi les données articles qui ont été écrit en latex, il y a des  noms
d'auteurs qui comporte des accents. Pour gérer cela, enfin pour éviter d'avoir
à traiter ce problème, j'ai choisi de mettre au seins de l'application une
petite base des données contenant les articles qui ont des noms d'auteurs 
comportant les accents. J'en ai trouver 641 articles, dans cette base des 
données ces noms sont toujours avec des accents mais cette fois-ci ces accents 
sont reconnus par python. Donc l'application se sert de cette base pour
corriger les noms d'auteurs lors du chargement des données par init.

Puis j'ai le problème des articles qui n'ont pas de noms d'auteurs, très
souvent il y a juste le nombre de pages à la place des auteurs : 18 pages
J'ai décidé de les laisser tels quels car pour les calcules d'intensité ils 
peuvent intervenir.
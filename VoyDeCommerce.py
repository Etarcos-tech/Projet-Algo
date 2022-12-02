import random, copy
import matplotlib.pyplot as plt


#fonction kqui recupere les information de chaque ville( coordonnées des noeuds du graphe)

def getVille():
    ville = [["ville1", 0, 0,], ["ville2", 0, 3], ["ville3", 4, 2], ["ville4", 5, 0]]
    return ville

#fonction qui calcule la distance entre deux villes

def distance(ville, i, j):
    dx = ville[i][1] - ville[j][1]
    dy = ville[i][2] - ville[j][2]

    return (dx**2 + dy**2)**0.5

#fonction qui calcule la longueur d'un circuit de plusieurs villes

def longueurVille(ville):
    d = 0
    for i in range(0, (len(ville) - 1)):
        #pour l'ensemble de toutes les villes

        d += distance(ville, i, i+1)
        #entre la derniere ville et la premiere

    d += distance(ville, 0, -1)

    d += distance(ville, i, i+1)
    return d

#fonction qui permet d'obtenir le chemin absurde et de tracer le graphe

def graphe(ville,valeur,couleur):
    #les differentes villes
    x = [t[1] for t in ville]
    y = [t[2] for t in ville]
    #la derniere ville pour boucler sur la premiere
    x += [x [0]]
    y += [y [0]]

    plt.title("chemin courant en rouge et plus court chemin en vert ")
    plt.plot(x, y, valeur, color=couleur)
    for vil,x,y in ville :
        plt.text(x,y,vil)
    

#fonction choix du chemin a prendre en comparant deux distance

def choixChemin(ville):
    #on calcule la longueur du circuit actuel en supposant que c'est le meilleur
    best = longueurVille(ville)

    nbchg = 0 #nombre de change ment effectué
    
    while True:
        #on tire aleatoirement deux villes
        i = random.randint (0, len(ville) - 1)
        j = random.randint (0, len(ville) - 1)
        #on se rassure que ce n'est pas la meme ville
        if i==j: continue
        #on echange  si i est different de j

        e = ville[i]
        ville[i] = ville[j]
        ville[j] = e 

        #on calcule la nouvelle distance et on compare a l'ancienne pour pouvoir choisir le chemin

        d = longueurVille(ville)
        if d >= best:
            #si le resultat est plus long on rentre a l'ancienne ville
            nbchg += 1
            e = ville[i]
            ville[i] = ville[j]
            ville[j] = e
        else:
            #sinon le meilleur chemin est desormais passant par cette nouvelle ville 
            best = d
            nbchg = 0
        
        #on decide de s'arreter s'il n'y plusieur fois pas de modification
        if nbchg > 10: break

    #fonction d'eviter que les chemin se croisent
def retourne(ville, i, j):
    """ici on veut echanger les elements 
    i et j,
    i+1 et j-1,
    i+2 et j-2
    tant que i+k < j-k pour un k donné"""
    while i <= j:
        e = ville[i]
        ville[i] = ville[j]
        ville[j] = e
        i += 1
        j -= 1

#on applique la fonction precedente en tenant compte de la distance optimale
def croisement(ville):
    """cette fonction se comporte de la meme maniere
        que la fonction choixChemin dans le sens ou on
        annule un chemin pour prendre un autre"""

    best = longueurVille(ville)
    nbchg = 0
    while True:
         #on tire aleatoirement deux villes
        i = random.randint (0, len(ville) - 2)
        j = random.randint (i+1, len(ville) - 1)
        retourne(ville,i,j)

        d = longueurVille(ville)
        if d >= best:
            nbchg += 1
            retourne(ville,i,j)
        else:
            nbchg = 0
            best = d
        if nbchg > 1000: break

#fonction test de toute les autres fonctions

def enchaine(ville):
    graphe(ville,'->',"red")
    best = longueurVille (ville)
    copi = copy.deepcopy(ville)
    print ("debut", best)
    nom = 0
    while True:
        
        croisement(ville)
        d = longueurVille(ville)
        print ("coisement", d, best)

        choixChemin(ville)
        d = longueurVille(ville)
        print ("choixChemin", d, best)

        if d < best:
            best = d
            copi = copy.deepcopy(ville)
            nom = 0
        elif nom > 2:
            break
        else:
            nom += 1
            for k in range(0,3):
                i = random.randint (0, len(ville) - 2)
                j = random.randint (i+1, len(ville) - 1)
                e = ville[i]
                ville[i] = ville[j]
                ville[j] = e

    return copi

if __name__ == "__main__":
    ville = getVille()
    ville = enchaine(ville)
    graphe(ville,"","green")
    plt.show()
    plt.close()





import random

def jeu_du_devin_utilisateur():
    ''' R0 Jouer au jeu du devin - l'utilisateur devine '''

    # R1 Comment jouer au jeu devin
    #
    # Choisir un nombre compris entre 1 et 999
    #   solution: out
    # Faire deviner ce nombre
    #   solution: in
    #   nombre_essai: out
    # Féliciter le joueur
    #   nombre_essai: in

    # R2 Comment Faire deviner ce nombre
    #
    # trouvé = false
    # nombre_essai = 0
    # while non trouvé:
    #   Demander la proposition de l'utilisateur
    #       proposition: out
    #   Incrémenter le nombre d'essai
    #       nombre_essai: inout
    #   Donner un indice 
    #       solution: in
    #       proposition: in


    # Choisir un nombre compris entre 1 et 999
    nombre_devin = random.randint(1, 999)
    nombre_joueur = None
    nombre_essai = 0

    
    while nombre_devin != nombre_joueur:
        # Mettre à jour le nombre d'essai
        nombre_essai += 1

        # Demander un nombre au joueur
        nombre_joueur = int(input("Propostion {0}\n".format(nombre_essai)))

        if (nombre_joueur > nombre_devin):
            print("Le nombre est plus petit.")
        elif (nombre_joueur < nombre_devin):
            print("Le nombre est plus grand.")
        print()
    # Afficher le nombre d'essais
    print("Vous avez trouvé en {0} essai(s)!".format(nombre_essai))

    
def jeu_du_devin_machine():
    ''' R0 Jouer au jeu du devin - l'utilisateur devine '''

    # R1 Comment jouer au jeu devin - la machine devine
    #
    # Faire choisir un nombre compris entre 1 et 999
    #
    # Deviner ce nombre
    #   nombre_essai: out
    #
    # Indiquer le nombre d'essai.
    #   nombre_essai: in

    # R2 Comment Deviner ce nombre
    #
    # trouvé = false
    # nombre_essai = 0
    # while non trouvé:
    #   Choisir un nombre
    #       proposition: out
    #   Incrémenter le nombre d'essai
    #       nombre_essai: inout
    #   Récupérer un indice 
    #       proposition: in
    #       trouve: out

    # R3 Comment Choisir un nombre
    #  nombre_ordi = borne_inf + (borne_sup - borne_inf) // 2
    #  Mettre à jour l'intervalle définissant où est situé le nombre
    #  

    # R4 Comment Mettre à jour l'intervalle définissant où est situé le nombre
    #   borne_sup -= (borne_sup - borne_inf) // 2
    #   borne_inf += (borne_sup - borne_inf) // 2

    nombre_choisi = False

    while not nombre_choisi:
        reponse = input("Avez-vous choisi un nombre? (o/n)\n")
        nombre_choisi = reponse in ('o', 'O', 'y', 'Y')

        if not nombre_choisi:
            print ("J'attends")

    nombre_essai = 0
    borne_sup = 1000
    borne_inf = 0
    nombre_trouve = False

    while not nombre_trouve:
        # Choisir un nombre
        nombre_ordi = borne_inf + (borne_sup - borne_inf) // 2
        # Incrémenter le nombre d'essai
        nombre_essai += 1

        print("Je choisis {0}.".format(nombre_ordi))
        reponse = input("Trop grand, trop petit, trouvé?\n")

        # Récupérer un indice 
        if reponse == 'g':
            # Mettre à jour l'intervalle définissant où est situé le nombre
            borne_sup -= (borne_sup - borne_inf) // 2
        elif reponse == 'p':
            # Mettre à jour l'intervalle définissant où est situé le nombre
            borne_inf += (borne_sup - borne_inf) // 2
        elif reponse == 't':
            nombre_trouve = True

    # Afficher le nombre d'essais
    print("J'ai trouvé en {0} essai(s)!".format(nombre_essai))


if __name__ == "__main__":

    continer_jeu = True

    while continer_jeu:
        print ("1- L'ordinateur choisit un nombre et vous le devinez")
        print ("2- Vous choissez un nombre et l'ordinateur le devine")
        print ("0- Quitter le programme")

        choix = int(input())

        if choix == 1:
            jeu_du_devin_utilisateur()
        elif choix == 2:
            jeu_du_devin_machine()
        else:
            print ("Au revoir...")
            continer_jeu = False

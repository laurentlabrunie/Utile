
ACTIONS = {
    "1": "Activer un environnement virtuel ?",
    "2": "Désactiver un environnement virtuel ?",
    "99": "Quitter ?"
}

class action:

    @staticmethod
    def displayActions():
        for cle, valeur in ACTIONS.items():
            print("{} - {}".format(cle, valeur))

    @staticmethod
    def getAction():
        return input("Votre choix est : ")



print("Bienvenue sur l'outil SNA")
print("Que voulez vous faire ?")
action.displayActions()
print(ACTIONS[action.getAction()])

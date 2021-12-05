class Personne:
    def __init__(self):
        self.nom = "Michaud"
        self.prenom = "William"
        self.age = 9
        self.lieu_residence = "Reunion"
#------------------------------------------------------------------------------------------------------------
class Compteur:
    objets = 0
    def __init__(self):
        Compteur.objets += 1
    def combien(cls):
        print("Jusqu'à présent, {} objets ont été créés.".format(cls.objets_crees))
        combien = classmethod(combien)
#----------------------------------------------------------------------------------------------------------
class TableauNoir:
    def __init__(self):
        self.surface = ""
    def ecrire(self,message):
        if self.surface != "":
            self.surface += "\n"
        self.surface += message
    def lire(self):
        print(self.surface)
    def effacer(self):
        self.surface = ""
#-------------------------------------------------------------------------------------------------------------
class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)
#--------------------------------------------------------------------------------------------------------------
class Test:
    """Une classe de test tout simplement"""
    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"
    
    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))
#----------------------------------------------------------------------------------------------------------------
class Personne2:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
    def _get_lieu_residence(self):
    """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""
        
        
        print("On accède à un attribut !")
        return self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

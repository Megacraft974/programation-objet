class Time(object):
    "nouvelle classe temporelle"
    def __init__(self,hh=12,mm=00,ss=00,jj="mardi",jc=21,mo="decembre"):
        self.heure=hh
        self.minute=mm
        self.seconde=ss
        self.jour=jj
        self.jourchiffre=jc
        self.mois=mo
    def affiche_heure(self):
        print(str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))
    def affiche_jour(self):
        print("On est "+self.jour+" "+str(self.jourchiffre)+" "+self.mois+".")
        

            
#montre=Time(jj="jeudi",jc=30,mo="avril")
#montre.affiche_heure()
#montre.affiche_jour()
#_______________________________________________________________________________________________________________________________________________________________________________________
class Domino(object):
    def __init__(self,fa=3,fb=8):
        self.face_a =fa
        self.face_b =fb
    def affiche_point(self,face_a,face_b):
        face_a=str(face_a)
        face_b=str(face_b)
        print("face A : "+ face_a +" face B : "+ face_b )
    def valeur(self,face_a,face_b):
        face_c=face_a+face_b
        face_c=str(face_c)
        print("Total des points: "+face_c)

#d1=Domino()
#d1.affiche_point(3,8)
#d1.valeur(3,8)

#__________________________________________________________________________________________________________________________________________________________________________________        
class Maison(object):
    
    def __init__(self,h,l,h2,l2,cou):
        
        self.hauteur   = h
        self.longueur  = l
        self.hauteur2  = h2
        self.longueur2 = l2
        self.couleur   = cou
        
    def dessine(self,hauteur,hauteur2,longueur,longueur2,couleur):
        
        can.create_line(hauteur,hauteur2,longueur,longueur2,fill=couleur)
        longueur  = longueur + 50
        longueur2 = longueur2 + 50
        can.create_line(hauteur,hauteur2,longueur,longueur2,fill=couleur)

        
#___________________________________________________________________________________________________________________________________________________________________________________        
class CompteBancaire(object):
    
    def __init__(self,n="Dupont",s=1000,d=0,r=0):
        
        self.nom      = n
        self.solde    = s
        self.depots   = d
        self.retraits = r
        
    def depot(self,depots):
        
        self.solde = self.solde+depots
        
    def retrait(self,retraits):
        
        self.solde = self.solde-retraits
        
    def affiche(self):
        
        monsolde = str(self.solde)
        nom      = str(self.nom)
        print("Le solde du compte bancaire de "+nom+" est de "+monsolde+" euros.")
        
#compte = CompteBancaire("William",50000)
#compte.depot(2000)
#compte.retrait(1000)
#compte.affiche()

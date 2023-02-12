# partie 1.py
class compte:
   nombreDeComptes=0 #un attribut statique ou de classe
   #definition du constructeur
   def __init__(self,soldeInitial,nomClient,numCompteClient,adressCli="tanger"):
      print("je suis le constructeur") 
      self.__solde = soldeInitial #attribut privé d’instance
      self.__nom=nomClient               #attribut privé d’instance
      self.numCompte=numCompteClient   #attribut publique d’instance
      self.__class__.nombreDeComptes+=1  #attribut statique
      self.adresse=adressCli
      
   def GetSold(self):
      return self.__solde
  
   def __del__(self):
      """desctruction du compte """
      print("je suis le destructeur") 
      self.__class__.nombreDeComptes-=1

   
   def affiche(self):
      print("Le client, Mr/Mme/Mlle ",self.__nom,"qui habite à:",self.adresse,"  a: ",self.__solde,end=' ')
      print("dans le compte: ",self.numCompte)
   # définition de la méthode NouveauSolde()
   
   def afficherNombreDecomptes(): #méthode statique ou de classe
      print("Actuellement, il y a ",__class__.nombreDeComptes," comptes cres...")
   
   def NouveauSolde(self,valeurSolde):
      self.__solde = float(valeurSolde)
   # définition de la méthode Solde()
   def SoldeClient(self):
      return self.__solde
   # définition de la méthode AjouterDansCompte()
   def AjouterDansCompte(self,somme):
      self.__solde += somme
   # définition de la méthode Debit()
   def Debit(self,somme):
      self.__solde -= somme
   # définition de la méthode spéciale __add__ (surcharge de l'opérateur +)
   def __add__(self,somme):
      if type(somme)in (int,float):
         self.__solde += somme
      elif type(somme)==compte:
         c_houssam=compte(self.__solde+somme.__solde,'houssam',2022,'casa')
         #c_houssam.affiche()
         return c_houssam 
   # définition de la méthode spéciale __sub__ (surcharge de l'opérateur -)
   def __sub__(self,somme):
      if type(somme)in (int,float):
         self.__solde -= somme
   def __mul__(self, m):
      # redéﬁnit le comportement de l’opérateur *
      self.__solde *= m
   def __str__(self):
      x="Le client, Mr/Mme/Mlle "+self.__nom+" a: "+str(self.__solde)
      x=x+" dans le compte: "+str(self.numCompte)
      return x
   #def __dict__(self):
   #   return None
#   def __setattr__(self,attr,value):return None
#       try:
#          object.__setattr__(self,attr,value)
#          print("changement effectué avec succès")
#       except KeyError:
#          print('attribut manquant !')
#    
#    def __getattr__(self,attr):
#       try:
#          return object.__getattr__(self,attr)
#       except KeyError:
#          print('attribut manquant !')
   def __dict__(self):return None   
      
# if __name__ == '__main__':
#    y=compte(100,'rita','516465','casablanca') 
#    compte.affiche(y) 
#    y.affiche()
#    print(y)
#    y+20
#    y.affiche()
#    # taper compte. et voir les options (méthodes et membres statiques)
#    compte.afficherNombreDecomptes()
#    print(y.__dict__) #voir redéfinition de def __dict__(self) en haut
#    y.__dict__['_compte__solde']=123456789
#    y.affiche()
#    setattr(y,'adresse','Casablanca, Boulevard Abdelmoumen')
#    print(getattr(y,'adresse'))
#    y.__setattr__('adresse','Casablanca, Boulevard Abdelmoumen, CP 3000')
#    print(getattr(y,'adresse'))
#    y.__setattr__('__nom','Ghita')
#    y.affiche()
#    setattr(y,'__nom','Ghita')
#    y.affiche()
#    setattr(y,'_compte__nom','Ghita2')
#    y.affiche()
   
   
   
   

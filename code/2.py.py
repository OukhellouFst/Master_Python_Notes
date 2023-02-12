class User:#partie 2
    pass

def test1():# nous somme hors la classe user !!!
    Amine = User()
    ### Définition d'attributs pour cet objet
    Amine.id = 1
    Amine.name = 'Alami'
    Amine.password = '12345'
    Amine.__password = 'azerty'
    Amine.solde = 100000
    print('Bonjour, je suis '+Amine.name)
    print('Mon id est: '+str(Amine.id))
    print('Mon mot de passe est : '+str(Amine.password))
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    Amine.password = 'mot de passe plus sécurisé ???!!!'
    print(Amine.password)
    del(Amine.password)
    Amine.password='Nouveau Mot de passe'
    del(Amine.__password)
    #Amine.__password='même avec attribut privé!'
    try:
        print("nom=",Amine.name)
        print("password=",Amine.password)
        print("password=",Amine.__password)
    except:
        import sys
        print("Unexpected error:", sys.exc_info())


class personne():
    def __init__(self, id, name, password, solde=100000):
        self.id = id
        self.name = name
        self.__password = password
        self.solde = solde

    def affiche_personne(self):
        print("--------affiche personne-----")
        print('id=', self.id)
        print('name=', self.name)
        print('password=', self.__password)
        print('solde=', self.solde)

    def __str__(self):
        # Nous avons donc redéﬁni comment la fonction print() se comportait
        # avec une instance de la classe personne.
        Res_str = "id=" + str(self.id) + " et nom=" + str(self.name)
        Res_str += " solde=" + str(self.solde) + ' password=' + self.__password
        return Res_str

    def __len__(self):
        # Nous avons donc redéﬁni comment la fonction len() se comportait
        # avec une instance de la classe personne.
        Res_len = len(self.__dict__)
        return Res_len

    def __add__(self, montant):
        # redéﬁnit le comportement de l’opérateur +
        self.solde += montant

    def __sub__(self, montant):
        # redéﬁnit le comportement de l’opérateur -
        self.solde -= montant

    def __mul__(self, montant):
        # redéﬁnit le comportement de l’opérateur *
        self.solde *= montant
    def __dict__(self):
        return None

def test2():
    X = personne(10, "ALAMI", "101010")
    print(X.id)
    print(X.name)
    print(X)
    print(len(X))
    X+10; print(X)
    X*2; print(X)
    X.affiche_personne()

if __name__ == '__main__':
    test1()
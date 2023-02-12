class User:   #  partie 5
    def __init__(self,NumCIN, NumPermi_conduire):
        self.__CIN=NumCIN
        self.__NPERM=NumPermi_conduire
    def affiche(self):
        print("CIN=",self.__CIN)
        print("Numéro de Permis=",self.__NPERM)
if __name__ == '__main__':
    Amine = User(12345,"PERM456778")
    #del(Amine.__CIN)
    print(Amine.__dict__.keys())
    Amine.affiche()
    Amine.__dict__['_User__CIN']='BH400'
    Amine.affiche()

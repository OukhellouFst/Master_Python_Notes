class Animal : # partie 3
    def __init__(self, name):
        self.name= name
    def showInfo(self):
        print ("I'm " + self.name)

# La classe Cat est étendue (extends) de la classe Animal.
class Cat (Animal):
    def __init__(self, name, age):
        Animal.__init__(self,name)
        self.age = age

    # Remplacez (override) la méthode ayant le même nom de la classe mère.
    def showInfo(self):
        print ("I'm " + self.name)
        print (" age " + str(self.age))

class Etre_vivant_vaccine_contre_virus():
    def __init__(self,Vacc_ok, VaccNonOk):
        self.vaccins_faits=Vacc_ok
        self.vaccins_Non_faits=VaccNonOk
        # La méthode (method):
    def showInfo(self):
        print ("Vaccins faits:",self.vaccins_faits)
        print ("Vaccins non faits:",self.vaccins_Non_faits)

    # La méthode (method):
    def faire_vaccin(self,vaccin):
        if vaccin in self.vaccins_Non_faits:
            self.vaccins_faits.append(vaccin)
            self.vaccins_Non_faits.remove(vaccin)

class Animal_vaccine_contre_virus(Animal,Etre_vivant_vaccine_contre_virus):
    def __init__(self, name, VaccOk,VaccNonOk):
        Animal.__init__(self, name)
        Etre_vivant_vaccine_contre_virus.__init__(self,VaccOk,VaccNonOk)

    def showInfo(self):
        print ("-- Call Muliclass.showInfo: --")
        Animal.showInfo(self)
        Etre_vivant_vaccine_contre_virus.showInfo(self)

if __name__ == '__main__':
    c1=Animal_vaccine_contre_virus('Cat-1',['v1','v2','v3'],['v4','covid-19'])
    c1.showInfo()
    c1.faire_vaccin('v4')
    c1.showInfo()


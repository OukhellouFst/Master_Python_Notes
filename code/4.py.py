import math  # partie 4
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
     
    def __str__(self):
        return "x="+str(self.__x)+" et y= " + str(self.__y)
 
    def __add__(self, p):
        a = self.__x + p.__x
        b = self.__y + p.__y
        return Point(a, b)
        
    def __lt__(self,p):# Opérateur <
        m_self = math.sqrt((self.__x ** 2) + (self.__y ** 2))
        m_p = math.sqrt((p.__x ** 2) + (p.__y ** 2))
        return m_self < m_p
        
    def __le__(self, p):# Opérateur <=
        m_self = math.sqrt((self.__x ** 2) + (self.__y ** 2))
        m_p = math.sqrt((p.__x ** 2) + (p.__y ** 2))
        return m_self <= m_p
 
    # Opérateur >
    def __gt__(self, p):
        m_self = math.sqrt((self.__x ** 2) + (self.__y ** 2))
        m_p = math.sqrt((p.__x ** 2) + (p.__y ** 2))
        return m_self > m_p
 
    # Opérateur >=
    def __ge__(self, p):
        if (isinstance(p, Point)):
            m_self = math.sqrt((self.__x ** 2) + (self.__y ** 2))
            m_p = math.sqrt((p.__x ** 2) + (p.__y ** 2))
            return m_self >= m_p
        else:
            return None
 
    # Opérateur ==
    def __eq__(self, p):
        m_self = math.sqrt((self.__x ** 2) + (self.__y ** 2))
        m_p = math.sqrt((p.__x ** 2) + (p.__y ** 2))
        return m_self == m_p
    
    def __getitem__(self,key):
        if key==0:
            return self.__x
        elif key==1:
            return self.__y
        else:
            return "attention, entrer un indice correcte"
    
    def __setitem__(self,key,nouvelle_Valeur):
        if key==0:
            self.__x=nouvelle_Valeur
        elif key==1:
            self.__y=nouvelle_Valeur
        else:
            print("attention, entrer un indice correcte")

    
    def __pow__(self,V):
        if(isinstance(V, int) or isinstance(V, float)):
            a = self.__x**V
            b = self.__y**V
            return Point(a, b)
        elif(isinstance(V, Point)):
            a = self.__x**V.__x
            b = self.__y**V.__y
            return Point(a,b)

    
    def __truediv__(self,V):
        if(isinstance(V, int) or isinstance(V, float)):
            a = self.__x/V
            b = self.__y/V
            return Point(a, b)
        elif(isinstance(V, Point)):
            a = self.__x/V.__x
            b = self.__y/V.__y
            return Point(a,b)
    

    def __floordiv_(self,V):
        if(isinstance(V, int) or isinstance(V, float)):
            a = self.__x//V
            b = self.__y//V
            return Point(a, b)
        elif(isinstance(V, Point)):
            a = self.__x//V.__x
            b = self.__y//V.__y
            return Point(a,b)
    def __mod__(self,V):
        if(isinstance(V, int) or isinstance(V, float)):
            a = self.__x%V
            b = self.__y%V
            return Point(a, b)
        elif(isinstance(V, Point)):
            a = self.__x%V.__x
            b = self.__y%V.__y
            return Point(a,b)
    
if __name__ == '__main__':
    p1 = Point(2,4)
    p2 = Point(5,1)
    p3 = p1+p2
    print(p3)
    print(p1<p2)
    print(p1.__ge__(p2))
    print(p1[0])
    print(p1[10])
    C=p1**p2
    print("p1: ",p1,"p2: ",p2,"C=p1**p2: ",C)
    C=p1**2
    print("C=p1**2: ",C)


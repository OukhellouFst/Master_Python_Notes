from multipledispatch import dispatch
@dispatch(object)
def f(x):
    print("je suis une fonction avec un seul paramètre f1:"+str(x))
@dispatch(int,int)
def f(x,y):
    print("je suis une fonction avec deux paramètres f2:"+str(x)+ ' et '+ str(y))
@dispatch(float,float)
def f(x,y):
    print("je suis une fonction avec deux paramètres f3:"+str(x)+ ' et '+ str(y))

f(100)
f(1111,2222) #tester f(11.11,2222)==>NotImplementedError
f(10.6,40.5)


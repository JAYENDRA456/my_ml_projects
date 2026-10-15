"""def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))    """
"""def change(x):
    x=x+10
    print("inside:",x)
a=5
change(a)
print("outside:",a)"""
"""def myfun(x):
    x[1]=20

a=[5,22]    
myfun(a)
print(a)   """
"""def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
print(fibonacci(4))    """
"""def default (name="guest"):

    print("hello,",name)
default() #uses default value
default("jay")   #uses provided value"""
"""def student(fn,ln="mohan",std="fifth"):
    print(fn,ln,'studies in',std,'standard')
student('jayendra')
student(ln='durga',fn='rao',std='seventh')
student(fn='mohan',ln='rao')"""
 
'''def student(fn,ln="mohan",std="fifth"):
    print(fn,ln,'studies in',std,'standard')
student(fn='jay')
student(fn='seventh',ln='john') 
student(fn='five')   '''
def add_lst(item,lst=None):
    if lst is None:
        lst=[]
    lst.append(item) 
    return lst
print(add_lst('mango'))  
print(add_lst('apple'))
#dic
'''def add_dic(item,qty,d=None):
    if d is None:
        d={}
    d[item]=qty
    return d
print(add_dic(qty=5,item="pen",))
print(add_dic(6,"pencil"))'''


        
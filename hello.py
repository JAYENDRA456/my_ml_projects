#conditions
'''check=lambda a:"positive" if a>0 else "negitive" if a<0 else "zero"
print(check(5))
print(check(-2))'''
'''check=lambda x: if x % 2== 0 'even' else 'odd'
print(check(21))'''
#list comprehension
'''func=[lambda arg=x:arg*10 for x in range(1,5)]
for i in func:
    print(i(3))'''
"""a = range(1,9)
res=[val**2 for val in a] 
print(res)   """
"""a=[i for i in range(2,9)]
print(a)"""
c=[(x,y ) for x in range(1,3) for y in range(0,3)]
print(c)
mat=[[1,2,3],[4,5,6],[7,8,9]]
res=[val for row in mat for val in row ]
print(res)
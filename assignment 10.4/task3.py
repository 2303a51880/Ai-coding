def f(x,y):
 z=[]
 for i in x:
  if i>y:
   z.append(i)
 return z

a=[10,5,20,3,15]
b=10
print(f(a,b))

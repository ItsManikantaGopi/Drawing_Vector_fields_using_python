from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from sympy import *
from mpmath import *
from math import *
plt.style.use("ggplot")
plt.legend()
fig=plt.figure()
ax=fig.gca(projection='3d')

si=input("enter the i quantities:=")
sj=input("enter the j quantities:=")
sk=input("enter the k quantities:=")
j=i=1
n=int(input("enter the range :="))
zer=[]
iv=[]
jv=[]
kv=[]
xv=[]
yv=[]
zv=[]
for k in range(-n,n+1):
    x=k    
    for m in range(-n,n+1):
        y=m
        for o in range(-n,n+1):
            z=o
            ih=eval(si)
            jh=eval(sj)
            zh=eval(sk)
            yv.append(m)
            xv.append(k)
            zv.append(o)
            zer.append(0)
            v=sqrt((ih**2)+(jh**2)+(zh**2))
            try:
                iv.append(ih/v)
                jv.append(jh/v)
                kv.append(zh/v)
            except:
                iv.append(ih)
                jv.append(jh)
                kv.append(zh)
'''                
print((iv))
print((jv))
print((kv))
print((xv))
print((yv))
print((zv))'''

ax.plot(xv,zer,zer,color='black')
ax.plot(zer,yv,zer,color='black')
ax.plot(zer,zer,zv,color='black')
ax.quiver(xv,yv,zv,iv,jv,kv,color='red')
ax.set_xlabel('x axis', fontsize=20, rotation=150)
ax.set_ylabel('y axis',fontsize=20 )
ax.set_zlabel(r'z axis', fontsize=20, rotation=60)
plt.show()




    



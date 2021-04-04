#2d vector field program
from matplotlib import pyplot as plt
from sympy import *
from mpmath import *
from math import *
plt.style.use('ggplot')
si=input("enter the i quantities:=")
sj=input("enter the j quantities:=")
j=i=1
n=int(input("enter the range :="))
iv=[]
jv=[]
xv=[]
yv=[]
for k in range(-n,n+1):
    x=k    
    for m in range(-n,n+1):
        y=m
        yv.append(y)
        xv.append(x)
        ih=eval(si)
        jh=eval(sj)
        v=sqrt((ih**2)+(jh**2))
        try:
            iv.append(ih/v)
            jv.append(jh/v)
        except:
            iv.append(ih)
            jv.append(jh)
plt.quiver(xv,yv,iv,jv,color='red',scale_units="xy",angles="xy",scale=1)
plt.show()




    


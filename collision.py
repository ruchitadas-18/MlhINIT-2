import numpy as np
import matplotlib.pyplot as pt
import math as m


#for mass 1 
m1= int(input(" Enter mass of first partile: "))
u1= int(input (" Enter the intial velocity of the partile: "))

#for mass 2
m2 = int(input(" Enter mass of second particle: "))
u2 = int(input(" Enter intial velocity pf the particle: "))

l1=[]
l2=[]
#for elastic collision
if (m1==m2):
  #collision with a stationary body of equal mass
  print(" Velocity of first partile = 0")
  print(" Velocity of second particle = ", u1)
  print(" Angle of deflection: ",m.asin(1))
  
elif (m1!=m2):
  #collision of unequal mass
  #for first particle
  for i in range(0,u1):
    for j in range (0,u2):
      if(i==0 or j==0):
        v1 = ((m1-m2)/(m1+m2))*u1 
        v2 = ((2*m1)/(m1+m2))*u1
        i=+1
        j=+1
        a=round(v2,2)
        b=round(v1,2)
        l1.append(a)
        l2.append(b)
    
      elif (i>=j):
        v1=((m1-m2)/(m1+m2))*u1 + ((2*m2)/(m1+m2))*u2
        v2=((2*m1)/(m1+m2))*u1 -((m1-m2)/(m1+m2))*u2
        i+=1
        j+=1
        a= round(v2,2)
        b= round(v1,2)
        l1.append(a)
        l2.append(b)
  
      else:
        print("finish")
  
pt.plot(l1,l2)
pt.show()

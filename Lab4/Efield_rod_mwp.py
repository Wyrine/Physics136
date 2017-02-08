# Efield_rod_mwp.py
# a mimimally working program to serve as a starting point
# for a program to compute and display the electric field
# produced by a uniformly charged rod. Last mod 20170207

#group D
#Kirolos Shahat, Mina Meshreky, Wes Williams
# 
from __future__ import division
from visual import *
scene.width = 800
scene.height = 600
scene.background = color.white

## CONSTANTS
oofpez = 9e9
L = 0.8
Q = 2e-9
Nq = 5   # number of point charges used to model a uniformly charged rod
dxq = L/Nq
dQ = Q/Nq
scalefactor = .1 # initial value will need to be changed later

## OBJECTS
cylinder(pos=(-L/2,0,0), axis = (L,0,0), radius=0.02, opacity = 0.2)
## display Nq spheres
xq = -L/2 + dxq/2
while xq < L/2:
    sphere(pos=(xq,0,0), radius=.01, color=color.red)
    xq = xq + dxq

xobs = 0
yobs = L/4
obsloc = vector (xobs, yobs, 0)   # observation location

Earrow = arrow(pos=obsloc, axis=(0.1,0,0), color=color.orange)

## CALCULATIONS

Enet = vector(0,0,0)  ## starts out at zero and should build up 
xq = -L/2 + dxq/2
while xq < L/2:
    ## Calculate the source location as a vector:
    sourcelocation = vector(xq,0,0)
    ## Calculate the field dE (a vector) contributed by this point charge source:
    r = obsloc - sourcelocation
    magR = r.mag
    rHat = r/magR
    e = oofpez * Nq/(magR**2) * rHat

    ## Add this field contribution dE to Enet:
    Enet = Enet + e
    ## Move to the next source location:
    xq = xq + dxq

print("Enet = ",Enet)
print("mag = " , Enet.mag)
## Change the axis of Earrow to point in the direction of Enet and
## scale it so it looks reasonable:
Earrow.axis = Enet/Enet.mag * scalefactor




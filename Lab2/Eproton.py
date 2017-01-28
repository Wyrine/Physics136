from __future__ import division
from visual import *

#
#group 5B
#
#Alexa Cusick, Kirolos Shahat, Caitlin Lloyd, Erika Seiber
#

## constants
oofpez = 9e9
qproton = -1.6e-19
randomConstant = 3e-10
scaleFactor = randomConstant/2

print(oofpez)

## objects
partice = sphere(pos = (0,0,0), radius = 1e-11)

## initial values
obslocation = vector(2.1e-10, 2.1e-10, 0)
r = obslocation - partice.pos
print("Relative position vector is", r)
ra  = arrow(pos = partice.pos, axis = r, color = color.green)
label(pos=r/2, text='r')
magR = r.mag
print("Magnitude of r is", magR)
rhat = r/magR
print("Unit vector rhat is", rhat)
print (rhat)
E = (oofpez * qproton * rhat)/(magR**2)
print ("Electric field vector is", E)
ea = arrow(pos = obslocation, axis = E*(scaleFactor/E.mag), color=color.orange)
label(pos=obslocation*(3/2), text='E')

#next arrow
obslocation = vector(randomConstant,0,0)
r = obslocation - partice.pos
magR = r.mag
rhat = r/magR
E = (oofpez * qproton * rhat)/(magR**2)
ea = arrow(pos = vector(randomConstant,0,0), axis = E*(scaleFactor/E.mag), color=color.orange)
#next arrow
obslocation = vector(-randomConstant,0,0)
r = obslocation - partice.pos
magR = r.mag
rhat = r/magR
E = (oofpez * qproton * rhat)/(magR**2)
ea = arrow(pos = vector(-randomConstant,0,0), axis = E*(scaleFactor/E.mag), color=color.orange)
#next arrow
obslocation = vector(0,randomConstant,0)
r = obslocation - partice.pos
magR = r.mag
rhat = r/magR
E = (oofpez * qproton * rhat)/(magR**2)
ea = arrow(pos = vector(0,randomConstant,0), axis = E*(scaleFactor/E.mag), color=color.orange)
#next arrow
obslocation = vector(0,-randomConstant,0)
r = obslocation - partice.pos
magR = r.mag
rhat = r/magR
E = (oofpez * qproton * rhat)/(magR**2)
ea = arrow(pos = vector(0,-randomConstant,0), axis = E*(scaleFactor/E.mag), color=color.orange)
#next arrow
obslocation = vector(0,0,randomConstant)
r = obslocation - partice.pos
magR = r.mag
rhat = r/magR
E = (oofpez * qproton * rhat)/(magR**2)
ea = arrow(pos = vector(0,0,randomConstant), axis = E*(scaleFactor/E.mag), color=color.orange)
#next arrow
obslocation = vector(0,0,-randomConstant)
r = obslocation - partice.pos
magR = r.mag
rhat = r/magR
E = (oofpez * qproton * rhat)/(magR**2)
ea = arrow(pos = vector(0,0,-randomConstant), axis = E*(scaleFactor/E.mag), color=color.orange)


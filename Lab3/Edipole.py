## Edipole.py, Group 5B, 2/1/17
##
## Kirolos Shahat, Alexa Cusick, Caitlin Lloyd, Erika Seiber
##

##electric field visualiztion of a dipole with a proton and an electron


## setup
from __future__ import division
from visual import *
#scene.stereo = 'redcyan'

## constants
oofpez = 9e9
protDist = 4e-11
elecDist = -1 * protDist
d = 3e-10
qproton = 1.6e-19
qelectron = -1 * qproton
scaleFactor = 1e-10
sphereRad = 1e-11
theta = 0
deltat = 1e-17
mProton = 1.7e-27
#the starting location of the momentum principle proton
momentumProton = 4e-11

## objects
negSphere = sphere(pos = vector(elecDist, 0, 0), radius = sphereRad, color = color.blue)
posSphere = sphere(pos = vector(protDist, 0, 0), radius = sphereRad, color = color.red)


#first iteration is 12 electric field vectors in the xy plane
#second iteration is 12 electric field vectors in the sxz plane
for i in range (0, 2):
    
    ## initial values
    theta = 0
    ## calculations
    while theta < 2*pi:
        ## calculate new vector value for obslocation, using theta
        if i == 0:
            obsLoc = d*vector(cos(theta), sin(theta), 0)
        else:
            obsLoc = d*vector(cos(theta), 0, sin(theta))
        ##use superposition principle to calculate eNet at obsLoc
        rNeg = obsLoc - negSphere.pos
        rPos = obsLoc - posSphere.pos
        magRN = rNeg.mag
        magRP = rPos.mag
        rNHat = rNeg / magRN
        rPHat = rPos/magRP
        ePos = oofpez * (qelectron)/(magRN ** 2) * rNHat
        eNeg = oofpez * (qproton)/(magRP ** 2) * rPHat
        eNet = ePos + eNeg
        ##print values of obsLoc and eNet vector
        print("obsLoc", obsLoc)
        print("eNet", eNet)
        ##create an orange arrow to display eNet at obsLoc and scale it
        curScaleFactor = scaleFactor / eNet.mag
        eArrow = arrow(pos = obsLoc, axis = eNet * curScaleFactor, color = color.orange)
        ##calculate new value of theta in radians: add (2*pi/12) to theta
        theta += 2*pi/12

#initialize momentum, net force, a trail, and the proton location      
pf = vector(0,0,0)
fNet = 0
protLoc = sphere(pos = vector(0, momentumProton, 0), radius = sphereRad, color = color.red)
trail = curve (color=color.yellow)
#loop infinitely through the iterative momentum principle
while True:
    #slow down the loop iteration so that it prints properly
    rate(100)
    #setting the final momentum for the previous iteration to the initial
    #momentum of this iteration
    pi = pf
    #calculating net electric force from the dipole
    rNeg = protLoc.pos - negSphere.pos
    rPos = protLoc.pos - posSphere.pos
    magRN = rNeg.mag
    magRP = rPos.mag
    rNHat = rNeg / magRN
    rPHat = rPos/magRP
    ePos = oofpez * (qelectron)/(magRN ** 2) * rNHat
    eNeg = oofpez * (qproton)/(magRP ** 2) * rPHat
    eNet = ePos + eNeg
    #calculating net force
    fNet = eNet * qproton
    #calculating final momentum
    pf = pi + fNet * deltat
    #updating proton location
    protLoc.pos = protLoc.pos+ pi/mProton * deltat
    #updating the trail
    trail.append(pos = protLoc.pos)



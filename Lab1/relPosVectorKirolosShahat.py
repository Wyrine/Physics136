#
# RelPosVecSkeleton.py sbe 20170112
#   Draws a crude model of Nielsen room 207 showing location of tables
#   and yellow tennis ball hanging from ceiling
#
# standard, necessary, opening stuff:
#
from __future__ import division, print_function
from visual import *

# right button mouse drag spins  (Mac: option key + mouse)
# double button mouse drag zooms  (Mac: command key + mouse)

##################################################################################
#                                                                               ##
#                  This stuff makes labeled coordinate axes                     ##
#                                                                               ##
d = 10.0      #adjust length of axes as needed                                  ##      
r = d*0.002   #thickness of axes                                                ##
axiscolor = color.green #(0,0.2,0)                                                           ##
#                                                                               ##
scene.background=color.white  #this makes it easier to see when projected       ##
scene.x=scene.y=0                                                               ##
scene.width=scene.height=800                                                    ##
#                                                                               ##
xaxis=cylinder(pos=vector(0,0,0),axis=vector(d,0,0),color=axiscolor,radius=r)   ##
yaxis=cylinder(pos=vector(0,0,0),axis=vector(0,d/2,0),color=axiscolor,radius=r) ##
zaxis=cylinder(pos=vector(0,0,0),axis=vector(0,0,d),color=axiscolor,radius=r)   ##
#                                                                               ##
label(pos=xaxis.pos+xaxis.axis,text='x',color=axiscolor,box=0)                  ##                             ##
label(pos=yaxis.pos+yaxis.axis,text='y',color=axiscolor,box=0)                  ##                           ##
label(pos=zaxis.pos+zaxis.axis,text='z',color=axiscolor,box=0)                  ##                           ##
#                                                                               ##
##################################################################################
#
# parameters defining attributes of a group table, dimensions in meters
#
toprad=1.060
topthick=0.040
pedestalrad=0.280
pedestalht=0.220
legrad=toprad-0.30 # single fat leg in center
leght=0.720
pedestalcolor=(0.8,0.8,1.0)
topcolor=(0.6,0.6,0.6)
legcolor=color.white
#
# function to draw a table (would be better to use a class)
# p = position vector of center of top of pedestal
#
def table(p):    
    cylinder(pos=p, axis=vector(0,-pedestalht,0), radius=pedestalrad,
             color=pedestalcolor, opacity=0.5) # the pedestal
    cylinder(pos=p-vector(0,pedestalht,0), axis=vector(0,-topthick,0),
             radius=toprad, color=topcolor, opacity=0.5) # the top
    cylinder(pos=p-vector(0,(pedestalht+topthick+leght),0), axis=vector(0,leght,0),
             radius=legrad, color=legcolor, opacity=0.5) # the leg

#
# Table coords (of centers of tops of pedestals)(eventually put in an array or list)
#
Table1pos=vector(-2.730,0.980,2.450)
Table2pos=vector(-4.980,0.980,5.600)
Table3pos=vector(-0.070,0.980,5.660)
Table4pos=vector( 4.151,0.980,5.660)
Table5pos=vector( 2.190,0.980,2.450)

#
# draw tables (if defining a table class, instantiate the tables)
#
table(Table1pos)
table(Table2pos)
table(Table3pos)
table(Table4pos)
table(Table5pos)
#
# show the podium
#
podH=1.100
podL=0.970
podW=0.750
podx=-5.75
pody=podH/2
podz=1.40
podiumpos=vector(podx,2*pody,podz) # pos of top of podium
box(pos=vector(podx,pody,podz), axis=vector(0,podH,0),
    up=vector(0.7,1.0,1.0), color=color.orange, opacity=0.5)
#
# Show the tennisball/charge ball
#
yellowball=sphere(pos=vector(0.300,2.520,3.670), radius=0.070, color=color.yellow)
ryballArr=arrow(pos=vector(0,0,0), axis=yellowball.pos, shaftwidth=0.030, color = color.orange)
#
# For the Relative Position Vector activity, add your code after this comment
#
Table1posArrow=arrow(pos=vector(0,0,0), axis=Table1pos, color=color.red)

#from ball to table
rBtoT = Table1pos-yellowball.pos
ballToTableArrow = arrow(pos = yellowball.pos, axis = rBtoT, color = color.magenta)

#magnitude of rBtoT
unitVecRbTOt = rBtoT / rBtoT.mag

tableToBallUnitVectorArrow = arrow(pos = Table1pos, axis = unitVecRbTOt, color = color.green)

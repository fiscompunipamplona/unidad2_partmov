from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.02

def func (conds, t, g, l):
    dthe = conds[1]
    dome = -(g/l)*sin(conds[0])
    return array([dthe, dome], float)


g = 9.81
l = 0.1

thes = 45*pi/180.
omes = 0.

initcond = array([thes,omes], float)

n_steps = 1000
t_start = 0.
t_final = 15.
t_delta = (t_final - t_start) / n_steps
t = linspace(t_start, t_final, n_steps)

solu, outodeint = odeint( func, initcond, t, args = (g, l), full_output=True)

theta, omega = solu.T



# =====================

scene.range = 0.2 # m

xp = l*sin(thes)
yp = -l*cos(thes)
zp = 0.

sleeptime = 0.0001

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.cyan)

time_i = 0
t_run = 0

#for i in omega:
#    print(i)


while t_run < t_final:
    sleep(sleeptime)
    prtcl.pos = vector( l*sin(theta[time_i]), -l*cos(theta[time_i]), zp )
    
    t_run += t_delta
    time_i += 1

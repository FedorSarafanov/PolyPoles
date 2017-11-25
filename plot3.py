#-*- coding: utf-8 -*-

import pylab
import numpy as np
import math

nu=np.logspace(0, 5, num=100)
R1=13000
R2=13000
C=0.05*10e-6
w=nu*(2*np.pi)
fi = np.loadtxt('data/chem3.tsv', skiprows=1, delimiter='\t', usecols=(0, 5))
print(fi)
phi = np.arctan(w*R2*R2*C/(R1+R2+R1*(w*R2*C)**2))
data=np.hstack([w,phi])
np.savetxt('phi', phi)
np.savetxt('w', w)
pylab.semilogx(nu, phi, "r")


we=fi.T[0]
phi2=np.arcsin(fi.T[1])
pylab.semilogx(we, phi2, "b*")

pylab.grid(True)
pylab.show()
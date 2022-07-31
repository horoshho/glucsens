import py_pol
from py_pol.stokes import Stokes
from py_pol.mueller import Mueller
import numpy as np
import matplotlib.pyplot as plt
def plott(x):
    x1=len(x[:,0])
    x2=len(x[0,:])
    k=0###without first k vectors
    c = np.zeros((4, x2-k))
    for i in range(0+k,x2):
        c[:,i-k]=x[:,i]
    #print(c)
    S1 = Stokes('Vector')
    S1.from_matrix(c)
    #plt.figure()
    S1.draw_ellipse(draw_arrow=True, figsize=(6, 6))
    S2 = S1.parameters.alpha()
    b=np.degrees(S2)
    #print(b)
def plott1d(x):
    S1 = Stokes('Vector')
    S1.from_matrix(x)
    #plt.figure()
    S1.draw_ellipse(draw_arrow=True, figsize=(6, 6))
    S2 = S1.parameters.alpha()
    b=np.degrees(S2)
    print(b)
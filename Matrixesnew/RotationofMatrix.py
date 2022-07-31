import numpy as np
def Mrot(phi1):
    phi=np.deg2rad(phi1)
    Mrot=np.array([[1,0,0,0],[0,np.cos(2*phi),np.sin(2*phi),0],[0, -np.sin(2*phi),np.cos(2*phi),0],[0,0,0,1]])
    return Mrot
def rotofM(phi1,M):
    Mtot = np.matmul(np.matmul(Mrot(-phi1), M), Mrot(phi1))
    return Mtot
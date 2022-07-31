import numpy as np
from pathes import path
import matplotlib.pyplot as plt
def ext(x):
    f=open(x)
    f1 = open(x)
    i=0
    k=0
    for s in f1:
        k=k+1
    ss=0
    A=np.zeros((k))
    C = []
    B =np.zeros((k))
    D = []
    for line in f:
         xx = line[36:37] + '.' + line[38:41]
         xx1 = line[20:21] + '.' + line[22:25]
         #print(xx)
         #print(xx1)
         pow=line[43:44]
         pow1=line[27:28]
         #print(pow,pow1)
         try:
            A[i - 1] = float(xx1)*10**(-float(pow1))
            B[i - 1] = float(xx)*10**(-float(pow))

            #if A[i - 1]>3:
                #A[i - 1]=A[i - 1]/10
         except:
             pass
         i = i + 1
         #print(A[i-1])
    #print(A)
    return A,B
###First
hz5=path+'\laser1.txt'
An5,Bn5=ext(hz5)
#plt.title('Laser intensity')
#plt.plot(Bn5,  label='Io')
#plt.xlabel('time')
#plt.ylabel('intensity')
#plt.legend()
#plt.show()
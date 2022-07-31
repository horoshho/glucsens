import numpy as np
def renorm(x):
    a=x[1]**2+x[2]**2+x[3]**2
    if x[0]**2 < a:
        x[0] = a**(1/2)
    return x
def renormarr(x):
    x1=len(x[:,0])
    x2=len(x[0,:])
    for i in range(0,x1):
        a = x[1,i] ** 2 + x[2,i] ** 2 + x[3,i] ** 2
        if x[0,i] ** 2 < a:
            x[0, i]=a**(1/2)

    return x
def normarr(x):
    x1 = len(x[:, 0])
    x2 = len(x[0, :])
    for i in range(0, x1):
        if x[0, i] > 1:
            x[0, i] = x[0, i] / x[0, i]
            x[1, i] = x[1, i] / x[0, i]
            x[2, i] = x[2, i] / x[0, i]
            x[3, i] = x[3, i] / x[0, i]
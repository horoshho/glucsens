import numpy as np
import matplotlib.pyplot as plt
from LaserIntensitymodel import Bn5
from Mpol1T import Mpol134,devMpol134,Spol1ini,Spol1f34,Spol1inip
from LCT import Mlcv1,Mlcv2,Slcv1f,Slcv2f,devMlcv1,devMlcv2
from BSTT import Mbst,Sbstf,devMbst
from RotationofMatrix import Mrot
#from MtissueplusglassT import MfT,MlowT,devMlowT,devMfT,Snafsimple,Snalowsimple
from MtissueplusglassTupd import MfT,MlowT,devMlowT,devMfT,Snafsimple,Snalowsimple
from BSRT import Mbsr,devMbsr,Sbsrf
from Mpol3T import Mpol3,devMpol3
from Gaussiangenerator import rnum
from Vectorplot import plott1d,plott
from VectorRenormalization import renormarr,renorm
from Rmatr import rmat
from Mmirrorglasssyst import Mmirr,devMmirr,Sbmirr,Sbmirrm,Sbmirrp
devSpol1ini=Spol1inip-Spol1ini
plt.rcParams.update({'font.size': 28})
k=2
n=10000

Bf11=np.zeros(n)
Bf21=np.zeros(n)
Bff11=np.zeros(n)
Bff21=np.zeros(n)
D11=np.zeros(n)
D21=np.zeros(n)

Bf12=np.zeros(n)
Bf22=np.zeros(n)
Bff12=np.zeros(n)
Bff22=np.zeros(n)
D12=np.zeros(n)
D22=np.zeros(n)

Seq1=np.zeros(n)
Seq2=np.zeros(n)
Sf1=np.zeros(n)
Sf2=np.zeros(n)

Smeq1=np.zeros(n)
Smeq2=np.zeros(n)
Smf1=np.zeros(n)
Smf2=np.zeros(n)

B=np.mean(Bn5)
phi1=35.5-90
maxS=0

fing11=[]
fing12=[]
fing21=[]
fing22=[]

fing11eq=[]
fing12eq=[]
fing21eq=[]
fing22eq=[]

pol3=[]
ref1=[]
ref2=[]
pol3eq=[]
ref1eq=[]
ref2eq=[]
# Sbmirrp[:,0]=Sbmirrp[:,0]*(1-0.352/0.743)
# Sbmirrp[:,1]=Sbmirrp[:,1]*(1-0.339/0.743)
# Sbmirr[:,0]=Sbmirr[:,0]*(1-0.352/0.743)
# Sbmirr[:,1]=Sbmirr[:,1]*(1-0.339/0.743)
# Sbmirr1=Sbmirr
# Sbmirrp1=Sbmirrp
# Sbmirrp1[:,0]=Sbmirrp[:,0]*(0.352/0.743)
# Sbmirrp1[:,1]=Sbmirrp[:,1]*(0.339/0.743)
# Sbmirr1[:,0]=Sbmirr[:,0]*(0.352/0.743)
# Sbmirr1[:,1]=Sbmirr[:,1]*(0.339/0.743)
devSbmirr=Sbmirrp-Sbmirr
phi=np.array([0,2])
for s in range(0,n):
    Mapol3 = np.matmul(np.matmul(Mrot(-phi1), (Mpol3 + rmat(devMpol3))), Mrot(phi1))
    MafT = MfT  # + rmat(devMfT)
    Sapol1ini = Spol1ini + rmat(devSpol1ini)

    Sabmirr=Sbmirr+rmat(devSbmirr)
    Sabmirr[:,0]=Sabmirr[:,0]*(1-0.352/0.743)
    Sabmirr[:,1]=Sabmirr[:,1]*(1-0.339/0.743)
    Sabmirr1= Sabmirr[:, 0] * (0.352 / 0.743)
    Sabmirr2 = Sabmirr[:, 1] * ( 0.339 / 0.743)
    xf11 = np.dot(np.matmul(np.matmul(Mapol3, Mrot(phi[0])), MafT), Sabmirr[:,0])
    xff11 = np.dot(np.matmul(Mrot(phi[0]), MafT), Sabmirr[:,0])
    Bf11[s] = xf11[0]*0.92
    xf21 = np.dot(np.matmul(np.matmul(Mapol3, Mrot(phi[0])), MafT), Sabmirr[:,1])
    xff21 = np.dot(np.matmul(Mrot(phi[0]), MafT), Sabmirr[:,1])
    Bf21[s] = xf21[0]
    D11[s]=Sabmirr1[0]
    D21[s]=Sabmirr2[0]
    D12[s]=D11[s]
    D22[s]=D21[s]

    ###########################
    xf12 = np.dot(np.matmul(np.matmul(Mapol3, Mrot(phi[1])), MafT), Sabmirr[:, 0])
    xff12 = np.dot(np.matmul(Mrot(phi[1]), MafT), Sabmirr[:, 0])
    Bf12[s] = xf12[0]*0.92
    xf22 = np.dot(np.matmul(np.matmul(Mapol3, Mrot(phi[1])), MafT), Sabmirr[:, 1])
    xff22 = np.dot(np.matmul(Mrot(phi[1]), MafT), Sabmirr[:, 1])
    Bf22[s] = xf22[0]
    ##################################
    a11 = xff11
    a21 = xff21
    # a11[1:] = a11[1:] / ((xff11[1] ** 2 + xff11[2] ** 2 + xff11[3] ** 2) ** (1 / 2)) * (
    #         (((xff21[1] ** 2 + xff21[2] ** 2 + xff21[3] ** 2)+(xff11[1] ** 2 + xff11[2] ** 2 + xff11[3] ** 2))/2) ** (1 / 2))
    a11[1:] = a11[1:] / ((xff11[1] ** 2 + xff11[2] ** 2 + xff11[3] ** 2) ** (1 / 2)) * (
            (xff21[1] ** 2 + xff21[2] ** 2 + xff21[3] ** 2)  ** (1 / 2))
    a11[0] = a11[0] / xff11[0] * xff21[0]
    b11 = np.dot(Mapol3, a11)
    b21 = np.dot(Mapol3, a21)
    c11 = b11[0]
    c21 = b21[0]
    Seq1[s] = c21 / D21[s] - c11 / D11[s]
    Smeq1[s]=(c21 / D21[s] + c11 / D11[s])/2
    Sf1[s] = Bf21[s] / D21[s] - Bf11[s] / D11[s]
    Smf1[s]=(Bf21[s] / D21[s] + Bf11[s] / D11[s])/2
    #print(Bf21[s],D21[s])
    #print(Sf1)
    ###############################
    a12 = xff12
    a22 = xff22
    # a12[1:] = a12[1:] / ((xff12[1] ** 2 + xff12[2] ** 2 + xff12[3] ** 2) ** (1 / 2)) * (
    #         (((xff22[1] ** 2 + xff22[2] ** 2 + xff22[3] ** 2)+(xff12[1] ** 2 + xff12[2] ** 2 + xff12[3] ** 2))/2) ** (1 / 2))
    a12[1:] = a12[1:] / ((xff12[1] ** 2 + xff12[2] ** 2 + xff12[3] ** 2) ** (1 / 2)) * (
            (xff22[1] ** 2 + xff22[2] ** 2 + xff22[3] ** 2)  ** (1 / 2))
    a12[0] = a12[0] / xff12[0] * xff22[0]
    b12 = np.dot(Mapol3, a12)
    b22 = np.dot(Mapol3, a22)
    c12 = b12[0]
    c22 = b22[0]
    Seq2[s] = c22 / D22[s] - c12 / D12[s]
    Smeq2[s] = (c22 / D22[s] + c12 / D12[s])/2
    Sf2[s] = Bf22[s] / D22[s] - Bf12[s] / D12[s]
    Smf2[s] = (Bf22[s] / D22[s] + Bf12[s] / D12[s])/2
    #print(Sf2)
    print(s)
print('finish')
# np.save('Seq1.npy',Seq1)
# np.save('Sf1.npy',Sf1)
# np.save('Seq2.npy',Seq2)
# np.save('Sf2.npy',Sf2)
ss=(Sf2-Sf1)/((Smf2+Smf1)/2)
seq=(Seq2-Seq1)/((Smeq2+Smeq1)/2)
print(ss)
plt.plot(Sf1)
plt.figure()
plt.title('Unequal Polarized Parts \u03C6=-56.6\u00b0')
plt.hist((ss),100)
plt.xlabel(' \u0394(\u0394I)/I')
plt.ylabel('N counts')
plt.figure()
plt.title('Equal Polarized Parts \u03C6=-56.6\u00b0')
plt.hist((seq),100)
plt.xlabel(' \u0394(\u0394I)/I')
plt.ylabel('N counts')
#Saving
print(np.mean(ss),'mean uneq')
print(np.std(ss),'std uneq')
print(np.mean(seq),'mean eq')
print(np.std(seq),'std eq')

plt.show()
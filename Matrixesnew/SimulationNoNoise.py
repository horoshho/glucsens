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
plt.rcParams.update({'font.size': 28})
devSpol1ini=Spol1inip-Spol1ini
l=len(Bn5)
k=6
c=np.array([5,4.8,5.4,7,6.4,5])
concon=np.zeros_like(c)
A=np.zeros(l)
Blow1=np.zeros(l)
Blow2=np.zeros(l)
Bf1=np.zeros(l)
Bf2=np.zeros(l)
Bff1=np.zeros(l)
Bff2=np.zeros(l)
D1=np.zeros(l)
D2=np.zeros(l)
Sf=np.zeros(l)
Slow=np.zeros(l)
dif=np.zeros(l)
difr=np.zeros(l)
j=1
f=1
#print(l)
phi1=-np.array([0,15,30,45,60,75,90])
phi1=np.array([45,55,5,0])
#phi1=np.linspace(0,360,72)
#phi1=np.array([-8,-11,0,35.5-90])
phi1=np.array([0,35.5-90])#
#phi1=np.array([-60,-30,-10,0,10,30,60])
maxS=0
phi2=-phi1
for s in range(0,len(phi1)):
    j=1
    for i in range(0, l):
        phi = (c[j - 1] - 4.8) / 1.1  # 0 at 4.8, 2 deg at 7mmol
        concon[j-1]=phi*2.05+4.6
        Mapol3 = np.matmul(np.matmul(Mrot(-phi1[s]), (Mpol3 )), Mrot(phi1[s]))#+ rnum() * devMpol3
        MafT = MfT #+ rnum() * devMfT
        MalowT = MlowT #+ rnum() * devMlowT
        Mabst = Mbst #+ rnum() * devMbst
        Mabsr = Mbsr #+ rnum() * devMbsr
        Malcv1 = Mlcv1 #+ rnum() * devMlcv1
        Malcv2 = Mlcv2 #+ rnum() * devMlcv2
        Mapol1 = Mpol134 #+ rnum() * devMpol134
        Sapol1ini = Spol1ini #+ rnum() * devSpol1ini
        A[i] = phi*2.05+4.6#c[j - 1]#phi
        xlow1 = np.inner(np.matmul(
            np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(Mapol3, Mrot(phi)), MalowT), Mabst), Malcv1),
                      Mrot(-4.10864)),
            Mapol1), Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        Blow1[i] = xlow1[0]# + rnum() * xlow1[0] * 0.03
        xlow2 = np.inner(np.matmul(
            np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(Mapol3, Mrot(phi)), MalowT), Mabst), Malcv2),
                      Mrot(-4.0828)),
            Mapol1), Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        Blow2[i] = xlow2[0]# + rnum() * xlow2[0] * 0.03
        xf1 = np.inner(np.matmul(
            np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(Mapol3, Mrot(phi)), MafT), Mabst), Malcv1),
                      Mrot(-4.10864)),
            Mapol1), Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        xff1=np.dot(np.matmul(
            np.matmul(np.matmul(np.matmul(np.matmul(Mrot(phi), MafT), Mabst), Malcv1),
                      Mrot(-4.10864)),
            Mapol1), Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        Bf1[i] = xf1[0]/0.4742*0.94 #+ rnum() * xf1[0] * 0.03#multiplication due to detector closer position
        xf2 = np.inner(np.matmul(
            np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(Mapol3, Mrot(phi)), MafT), Mabst), Malcv2),
                      Mrot(-4.0828)),
            Mapol1), Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        xff2=np.dot(np.matmul(
            np.matmul(np.matmul(np.matmul( np.matmul(Mrot(phi),MafT), Mabst), Malcv2),
                      Mrot(-4.0828)),
            Mapol1), Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        Bf2[i] = xf2[0]/0.4742 #+ rnum() * xf2[0] * 0.03
        xr1 = np.inner(np.matmul(np.matmul(np.matmul(Mabsr, Malcv1), Mrot(-4.10864)), Mapol1),
                       Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        D1[i] = xr1[0]/1687 #+ rnum() * xr1[0] * 0.03
        xr2 = np.inner(np.matmul(np.matmul(np.matmul(Mabsr, Malcv2), Mrot(-4.0828)), Mapol1),
                       Sapol1ini[:, 0] * Bn5[i] * 10 ** (3))
        D2[i] = xr2[0]/1687 #+ rnum() * xr2[0] * 0.03#multiplication due to beamdumper
        Sf[i] = Bf2[i] / D2[i] - Bf1[i] / D1[i]#*0.99775
        Bff1[i]=((xff1[1]**2+xff1[2]**2+xff1[3]**2)**(1/2))/((xff2[1]**2+xff2[2]**2+xff2[3]**2)**(1/2))
        Bff2[i] = ((xff1[0] ** 2-xff1[1] ** 2 + xff1[2] ** 2 + xff1[3] ** 2) ** (1 / 2)) / (
                    (xff2[0] ** 2-xff2[1] ** 2 + xff2[2] ** 2 + xff2[3] ** 2) ** (1 / 2))
        a1=xff1
        a2=xff2
        #a1[1:]=a1[1:]/((xff1[1]**2+xff1[2]**2+xff1[3]**2)**(1/2))*((xff2[1]**2+xff2[2]**2+xff2[3]**2)**(1/2))
        a1[1:] = a1[1:] / ((xff1[1] ** 2 + xff1[2] ** 2 + xff1[3] ** 2) ** (1 / 2)) * (
                (((xff2[1] ** 2 + xff2[2] ** 2 + xff2[3] ** 2) + (
                            xff1[1] ** 2 + xff1[2] ** 2 + xff1[3] ** 2)) / 2) ** (1 / 2))
        a2[1:] = a2[1:] / ((xff2[1] ** 2 + xff2[2] ** 2 + xff2[3] ** 2) ** (1 / 2)) * (
                (((xff2[1] ** 2 + xff2[2] ** 2 + xff2[3] ** 2) + (
                        xff1[1] ** 2 + xff1[2] ** 2 + xff1[3] ** 2)) / 2) ** (1 / 2))
        a1[0]=a1[0]/xff1[0]*xff2[0]
        b1=np.inner(Mapol3,a1)
        b2=np.inner(Mapol3,a2)
        c1=b1[0]/0.4742
        c2 = b2[0] / 0.4742
        Slow[i] =c2 / D2[i] - c1/ D1[i]#Bf2[i] / D2[i] + Bf1[i] / D1[i]#(Bf2[i]-Bf1[i])/(Bf2[i]+Bf1[i])#Bf1[i] / D1[i]#- Blow2[i] / D2[i] +Blow1[i] / D1[i]*0.81326178
        if f==1:
            difr[i] = Bf2[i] / D2[i]#c2 / D2[i]
            dif[i] = Bf2[i]#c2
        else:
            difr[i] = Bf1[i] / D1[i]#c1/ D1[i]
            dif[i] = Bf1[i]#c1
        if i %100==0:
            if f==1:
                
                f=0
            else:

                f = 1

        if i < l / k * j:
            pass
        else:
            j = j + 1
            #print(phi)
        # print(i)
    print(s)
    print(D1[4000],D2[4000],Bf1[4000],Bf2[4000])
    if abs(Sf[4000]-Sf[10000])/(Bf2[4000] / D2[4000] )>maxS:
        phimax=phi1[s]
        maxS=abs(Sf[4000]-Sf[10000])
        rel=abs(Sf[4000]-Sf[10000])/(Bf2[4000]/D2[4000])#+Bf2[10000]/D2[10000])/2
        rel1=abs(Sf[4000]-Sf[10000])/((Sf[4000]+Sf[10000])/2)
        #print(abs(Slow[4000]-Slow[10000]),Slow[4000])
        #print(abs(Slow[4000]-Slow[10000])/Slow[4000])
    plt.title('Signal ratios difference of the setup model without noise')
    plt.plot(Sf,label='phi1='+str(phi1[s]-2))#+'  maximum intensity difference angle'#Slow
    plt.ylabel('Inensity ratios difference')
    plt.xlabel('Number of measurement')
    plt.legend()
    #######
    plt.figure()
    plt.title('Signal of the setup model without noise')
    plt.plot(dif, label='phi1=' + str(phi1[s]-2) )#+ '  maximum intensity difference angle'##dif##Bff1
    plt.ylabel('Inensity')
    plt.xlabel('Number of measurement')
    plt.legend()
    #######
    # #######
    # plt.figure()
    # plt.title('Signal of the setup model without noise')
    # plt.plot(Bff2, label='phi1=' + str(phi1[s]))  # + '  maximum intensity difference angle'
    # plt.ylabel('Inensity')
    # plt.xlabel('Number of measurement')
    # plt.legend()
    # #######
    #######
    plt.figure()
    plt.title('Signal ratios of the setup model without noise')
    plt.plot(difr, label='phi1=' + str(phi1[s]-2) )#+ '  maximum intensity difference angle'##difr##Slow
    plt.ylabel('Inensity ratios')
    plt.xlabel('Number of measurement')
    plt.legend()
   # plt.figure()
    #plt.plot(Slow,label='Slow phi1='+str(phi1[s]))
   # plt.legend()
    #plt.plot(Bf2/D2)
    #plott1d(renorm(xlow1))
    #plott1d(renorm(xlow2))
    #plt.figure()
    #xx = np.array([[xff1], [xff2]])#np.array([[b1], [b2]])
    xx = np.array([[a1], [a2]])
    from py_pol.stokes import Stokes
    S1 = Stokes('Stokes vectors incident on the detector')
    S1.from_matrix(xx)
    S1.draw_ellipse(draw_arrow=True, figsize=(6, 6))
    S2 = S1.parameters.alpha()
    b = np.degrees(S2)
    print(b)
    plt.figure()

print(phimax)

plt.title('Glucose concentration for simulation')
plt.plot(A)#A
plt.ylabel('C (mmol/dl)')
plt.xlabel('Number of measurement')
plt.legend()

#plott(renormarr(Snalowsimple))
#plt.figure()
#plt.plot(phi)
#print(phimax)
#print(maxS)
#print(rel)
#print(rel1)
plt.show()

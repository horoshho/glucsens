from Unwrapdata import *
from Vectorplot import *
from MatrixCalcFrom_8_Vectors import *
from pathes import path
#######DATA LOAD#######

#Vectors before LC

inicaa=path+'\inic.csv'
ini34pol1aa=path+'\ini34pol1.csv'
ini304pol1aa=path+'\ini304pol1.csv'
ini349pol1aa=path+'\ini349pol1.csv'

#Vectors after LC

##circ
lcv1circaa=path+'\lcv1circ.csv'
lcv2circaa=path+'\lcv2circ.csv'

##pol1 at 34
lcv1pol134aa=path+'\lcv1pol134.csv'
lcv2pol134aa=path+'\lcv2pol134.csv'
lcv3pol134aa=path+'\lcv3pol134.csv'

##pol1 at 304
lcv1pol1304aa=path+'\lcv1pol1304.csv'
lcv2pol1304aa=path+'\lcv2pol1304.csv'
lcv3pol1304aa=path+'\lcv3pol1304.csv'

##pol1 at 349
lcv1pol1349aa=path+'\lcv1pol1349.csv'
lcv2pol1349aa=path+'\lcv2pol1349.csv'
lcv3pol1349aa=path+'\lcv3pol1349.csv'

########DATA UNWRAP########

#Vectors before pol1

inic,avginic,devinic=ext(inicaa)
ini34pol1,avgini34pol1,devini34pol1=ext(ini34pol1aa)
ini304pol1,avgini304pol1,devini304pol1=ext(ini304pol1aa)
ini349pol1,avgini349pol1,devini349pol1=ext(ini349pol1aa)

#Vectors after pol1
##circ

lcv1circ,avglcv1circ,devlcv1circ=ext(lcv1circaa)
lcv2circ,avglcv2circ,devlcv2circ=ext(lcv2circaa)

##pol1 at 34

lcv1pol134,avglcv1pol134,devlcv1pol134=ext(lcv1pol134aa)
lcv2pol134,avglcv2pol134,devlcv2pol134=ext(lcv2pol134aa)
lcv3pol134,avglcv3pol134,devlcv3pol134=ext(lcv3pol134aa)

##pol1 at 304

lcv1pol1304,avglcv1pol1304,devlcv1pol1304=ext(lcv1pol1304aa)
lcv2pol1304,avglcv2pol1304,devlcv2pol1304=ext(lcv2pol1304aa)
lcv3pol1304,avglcv3pol1304,devlcv3pol1304=ext(lcv3pol1304aa)

##pol1 at 349

lcv1pol1349,avglcv1pol1349,devlcv1pol1349=ext(lcv1pol1349aa)
lcv2pol1349,avglcv2pol1349,devlcv2pol1349=ext(lcv2pol1349aa)
lcv3pol1349,avglcv3pol1349,devlcv3pol1349=ext(lcv3pol1349aa)


####MATRIXES BUILDED FROM VECTORS######
#Initial

Slcini=np.zeros((4,4))
Slcini[:,0]=avginic*1.442
Slcini[:,1]=avgini34pol1*0.765#/1.442
Slcini[:,2]=avgini304pol1*0.575#/1.442
Slcini[:,3]=avgini349pol1*0.720#/1.442

#LC at V1

Slcv1f=np.zeros((4,4))
Slcv1f[:,0]=avglcv1circ*1.406#/1.442
Slcv1f[:,1]=avglcv1pol134*0.758#/0.765
Slcv1f[:,2]=avglcv1pol1304*0.550#/0.575
Slcv1f[:,3]=avglcv1pol1349*0.700

#LC at V2

Slcv2f=np.zeros((4,4))
Slcv2f[:,0]=avglcv2circ*1.408#/1.442
Slcv2f[:,1]=avglcv2pol134*0.758#/0.765
Slcv2f[:,2]=avglcv2pol1304*0.552
Slcv2f[:,3]=avglcv2pol1349*0.700

#LC at V3
##Recommended not to use as 0-th element was extrapolated
Slcv3f=np.zeros((4,4))
Slcv3f[:,0]=(avglcv1circ+avglcv1circ)/2
Slcv3f[:,1]=avglcv3pol134
Slcv3f[:,2]=avglcv3pol1304
Slcv3f[:,3]=avglcv3pol1349

######MATRIXES OF VECTORS+DEV#########

#Initial

Slcinip=np.zeros((4,4))
Slcinip[:,0]=(avginic+devinic)*1.442
Slcinip[:,1]=(avgini34pol1+devini34pol1)*0.765
Slcinip[:,2]=(avgini304pol1+devini304pol1)*0.575
Slcinip[:,3]=(avgini349pol1+devini349pol1)*0.720

##LC at V1

Slcv1fp=np.zeros((4,4))
Slcv1fp[:,0]=(avglcv1circ+devlcv1circ)*1.406
Slcv1fp[:,1]=(avglcv1pol134+devlcv1pol134)*0.758
Slcv1fp[:,2]=(avglcv1pol1304+devlcv1pol1304)*0.550
Slcv1fp[:,3]=(avglcv1pol1349+devlcv1pol1349)*0.700

##LC at V2

Slcv2fp=np.zeros((4,4))
Slcv2fp[:,0]=(avglcv2circ+devlcv2circ)*1.408
Slcv2fp[:,1]=(avglcv2pol134+devlcv2pol134)*0.758
Slcv2fp[:,2]=(avglcv2pol1304+devlcv2pol1304)*0.552
Slcv2fp[:,3]=(avglcv2pol1349+devlcv2pol1349)*0.700



######MATRIXES OF VECTORS-DEV#########

#Initial

Slcinim=np.zeros((4,4))
Slcinim[:,0]=(avginic-devinic)*1.442
Slcinim[:,1]=(avgini34pol1-devini34pol1)*0.765
Slcinim[:,2]=(avgini304pol1-devini304pol1)*0.575
Slcinim[:,3]=(avgini349pol1-devini349pol1)*0.720

##LC at V1

Slcv1fm=np.zeros((4,4))
Slcv1fm[:,0]=(avglcv1circ-devlcv1circ)*1.406
Slcv1fm[:,1]=(avglcv1pol134-devlcv1pol134)*0.758
Slcv1fm[:,2]=(avglcv1pol1304-devlcv1pol1304)*0.550
Slcv1fm[:,3]=(avglcv1pol1349-devlcv1pol1349)*0.700

##LC at V2

Slcv2fm=np.zeros((4,4))
Slcv2fm[:,0]=(avglcv2circ-devlcv2circ)*1.408
Slcv2fm[:,1]=(avglcv2pol134-devlcv2pol134)*0.758
Slcv2fm[:,2]=(avglcv2pol1304-devlcv2pol1304)*0.552
Slcv2fm[:,3]=(avglcv2pol1349-devlcv2pol1349)*0.700

######MUELLER MATRIXES OF LC#######

#LC at V1
Mlcv1=matrix8(Slcini,Slcv1f)
Mlcv1p=matrix8(Slcini,Slcv1fp)
Mlcv1m=matrix8(Slcini,Slcv1fm)

#LC at V2
Mlcv2=matrix8(Slcini,Slcv2f)
Mlcv2p=matrix8(Slcini,Slcv2fp)
Mlcv2m=matrix8(Slcini,Slcv2fm)

######STANDART DEVIATION OF MATRIXES########

devMlcv1=((Mlcv1p-Mlcv1)+(Mlcv1-Mlcv1m))/2
devMlcv2=((Mlcv2p-Mlcv2)+(Mlcv2-Mlcv2m))/2
######Rotation of Mlcv1,2 due to errors after component replacement
from RotationofMatrix import *
#Mlcv1=np.matmul(np.matmul(Mrot(-0.012),Mlcv1),Mrot(0.012))
#Mlcv2=np.matmul(np.matmul(Mrot(-0.012),Mlcv2),Mrot(0.012))
#Mlcv1,Mlcv2-matrixes itself
#Slcini-initial vector
#Slcv1f,Slcv2f-final vectors

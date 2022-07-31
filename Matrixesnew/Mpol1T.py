from Unwrapdata import *
from Vectorplot import *
from MatrixCalcFrom_8_Vectors import *
from pathes import path

#######DATA LOAD#######

#Vectors before pol1

inicaa=path+'\inic.csv'
lcforpol1v1aa=path+'\lcforpol1v1.csv'
lcforpol1v2aa=path+'\lcforpol1v2.csv'
lcforpol1v3aa=path+'\lcforpol1v3.csv'

#Vectors after pol1
##pol1 at 34
ini34pol1aa=path+'\ini34pol1.csv'
pol134lcv1aa=path+'\pol134lcv1.csv'
pol134lcv2aa=path+'\pol134lcv2.csv'
pol134lcv3aa=path+'\pol134lcv3.csv'
##pol1 at 304
ini304pol1aa=path+'\ini304pol1.csv'
pol1304lcv1aa=path+'\pol1304lcv1.csv'
pol1304lcv2aa=path+'\pol1304lcv2.csv'
pol1304lcv3aa=path+'\pol1304lcv3.csv'

##pol1 at 349
ini349pol1aa=path+'\ini349pol1.csv'
pol1349lcv1aa=path+'\pol1349lcv1.csv'
pol1349lcv2aa=path+'\pol1349lcv2.csv'
pol1349lcv3aa=path+'\pol1349lcv3.csv'

########DATA UNWRAP########

#Vectors before pol1

inic,avginic,devinic=ext(inicaa)
lcforpol1v1,avglcforpol1v1,devlcforpol1v1=ext(lcforpol1v1aa)
lcforpol1v2,avglcforpol1v2,devlcforpol1v2=ext(lcforpol1v2aa)
lcforpol1v3,avglcforpol1v3,devlcforpol1v3=ext(lcforpol1v3aa)

#Vectors after pol1
##pol1 at 34

from RotationofMatrix import *
ini34pol1,avgini34pol1,devini34pol1=ext(ini34pol1aa)
pol134lcv1,avgpol134lcv1,devpol134lcv1=ext(pol134lcv1aa)
#avgini34pol1=avgpol134lcv1##as there was some displacment in pol position
avgini34pol1=np.inner(Mrot(-3.15),avgini34pol1)##as there was some displacment in pol position
pol134lcv2,avgpol134lcv2,devpol134lcv2=ext(pol134lcv2aa)
pol134lcv3,avgpol134lcv3,devpol134lcv3=ext(pol134lcv3aa)

##pol1 at 304

ini304pol1,avgini304pol1,devini304pol1=ext(ini304pol1aa)
pol1304lcv1,avgpol1304lcv1,devpol1304lcv1=ext(pol1304lcv1aa)
#avgini304pol1=avgpol1304lcv1##as there was some displacment in pol position
avgini304pol1=np.inner(Mrot(-3.21),avgini304pol1)##as there was some displacment in pol position
pol1304lcv2,avgpol1304lcv2,devpol1304lcv2=ext(pol1304lcv2aa)
pol1304lcv3,avgpol1304lcv3,devpol1304lcv3=ext(pol1304lcv3aa)

##pol1 at 349

ini349pol1,avgini349pol1,devini349pol1=ext(ini349pol1aa)
pol1349lcv1,avgpol1349lcv1,devpol1349lcv1=ext(pol1349lcv1aa)
pol1349lcv2,avgpol1349lcv2,devpol1349lcv2=ext(pol1349lcv2aa)
pol1349lcv3,avgpol1349lcv3,devpol1349lcv3=ext(pol1349lcv3aa)

###rotation due to experiment geometry
avgpol1349lcv1=np.inner(Mrot(90),avgpol1349lcv1)
avgpol1349lcv2=np.inner(Mrot(90),avgpol1349lcv2)
avgpol1349lcv3=np.inner(Mrot(90),avgpol1349lcv3)
#avgini349pol1=avgpol1349lcv1##as there was some displacment in pol position
avgini349pol1=np.inner(Mrot(-2.8),avgini349pol1)##as there was some displacment in pol position
####MATRIXES BUILDED FROM VECTORS######
#Initial

Spol1ini=np.zeros((4,4))
Spol1ini[:,0]=avginic*1.442
Spol1ini[:,1]=avglcforpol1v1*1.42#/1.442
Spol1ini[:,2]=avglcforpol1v2*1.42#/1.442
Spol1ini[:,3]=avglcforpol1v3*1.396#/1.442

#pol1 at 34

Spol1f34=np.zeros((4,4))
Spol1f34[:,0]=avgini34pol1*0.765#/1.442
Spol1f34[:,1]=avgpol134lcv1*1.038#/1.42
Spol1f34[:,2]=avgpol134lcv2*0.968#/1.42
Spol1f34[:,3]=avgpol134lcv3*0.985#/1.396

#pol1 at 304

Spol1f304=np.zeros((4,4))
Spol1f304[:,0]=avgini304pol1*0.575#/1.442
Spol1f304[:,1]=avgpol1304lcv1*0.296#/1.42
Spol1f304[:,2]=avgpol1304lcv2*0.360#/1.42
Spol1f304[:,3]=avgpol1304lcv3*0.310#/1.396

#pol1 at 349

Spol1f349=np.zeros((4,4))
Spol1f349[:,0]=avgini349pol1*0.72#/1.442
Spol1f349[:,1]=avgpol1349lcv1*0.1355#/1.42
Spol1f349[:,2]=avgpol1349lcv2*0.090#/1.42
Spol1f349[:,3]=avgpol1349lcv3*0.1175#/1.396

######MATRIXES OF VECTORS+DEV#########

#Initial

Spol1inip=np.zeros((4,4))
Spol1inip[:,0]=(avginic+devinic)*1.442
Spol1inip[:,1]=(avglcforpol1v1+devlcforpol1v1)*1.42#/1.442
Spol1inip[:,2]=(avglcforpol1v2+devlcforpol1v2)*1.42#/1.442
Spol1inip[:,3]=(avglcforpol1v3+devlcforpol1v3)*1.396#/1.442

#pol1 at 34

Spol1f34p=np.zeros((4,4))
Spol1f34p[:,0]=(avgini34pol1+devini34pol1)*0.765#/1.442
Spol1f34p[:,1]=(avgpol134lcv1+devpol134lcv1)*1.038#/1.42
Spol1f34p[:,2]=(avgpol134lcv2+devpol134lcv2)*0.968#/1.42
Spol1f34p[:,3]=(avgpol134lcv3+devpol134lcv3)*0.985#/1.396

#pol1 at 304

Spol1f304p=np.zeros((4,4))
Spol1f304p[:,0]=(avgini304pol1+devini304pol1)*0.575#/1.442
Spol1f304p[:,1]=(avgpol1304lcv1+devpol1304lcv1)*0.296#/1.42
Spol1f304p[:,2]=(avgpol1304lcv2+devpol1304lcv2)*0.360#/1.42
Spol1f304p[:,3]=(avgpol1304lcv3+devpol1304lcv3)*0.310#/1.396

#pol1 at 349

Spol1f349p=np.zeros((4,4))
Spol1f349p[:,0]=(avgini349pol1+devini349pol1)*0.72#/1.442
Spol1f349p[:,1]=(avgpol1349lcv1+devpol1349lcv1)*0.1355#/1.42
Spol1f349p[:,2]=(avgpol1349lcv2+devpol1349lcv2)*0.090#/1.42
Spol1f349p[:,3]=(avgpol1349lcv3+devpol1349lcv3)*0.1175#/1.396

######MATRIXES OF VECTORS-DEV#########

#Initial

Spol1inim=np.zeros((4,4))
Spol1inim[:,0]=(avginic-devinic)*1.442
Spol1inim[:,1]=(avglcforpol1v1-devlcforpol1v1)*1.42#/1.442
Spol1inim[:,2]=(avglcforpol1v2-devlcforpol1v2)*1.42#/1.442
Spol1inim[:,3]=(avglcforpol1v3-devlcforpol1v3)*1.396#/1.442

#pol1 at 34

Spol1f34m=np.zeros((4,4))
Spol1f34m[:,0]=(avgini34pol1-devini34pol1)*0.765#/1.442
Spol1f34m[:,1]=(avgpol134lcv1-devpol134lcv1)*1.038#/1.42
Spol1f34m[:,2]=(avgpol134lcv2-devpol134lcv2)*0.968#/1.42
Spol1f34m[:,3]=(avgpol134lcv3-devpol134lcv3)*0.985#/1.396

#pol1 at 304

Spol1f304m=np.zeros((4,4))
Spol1f304m[:,0]=(avgini304pol1-devini304pol1)*0.575#/1.442
Spol1f304m[:,1]=(avgpol1304lcv1-devpol1304lcv1)*0.296#/1.42
Spol1f304m[:,2]=(avgpol1304lcv2-devpol1304lcv2)*0.360#/1.42
Spol1f304m[:,3]=(avgpol1304lcv3-devpol1304lcv3)*0.310#/1.396

#pol1 at 349

Spol1f349m=np.zeros((4,4))
Spol1f349m[:,0]=(avgini349pol1-devini349pol1)*0.72#/1.442
Spol1f349m[:,1]=(avgpol1349lcv1-devpol1349lcv1)*0.1355#/1.42
Spol1f349m[:,2]=(avgpol1349lcv2-devpol1349lcv2)*0.090#/1.42
Spol1f349m[:,3]=(avgpol1349lcv3-devpol1349lcv3)*0.1175#/1.396

######MUELLER MATRIXES OF POL1#######

#pol1 at 34
Mpol134=matrix8(Spol1ini,Spol1f34)
Mpol134p=matrix8(Spol1inip,Spol1f34p)
Mpol134m=matrix8(Spol1inim,Spol1f34m)

#pol1 at 304
Mpol1304=matrix8(Spol1ini,Spol1f304)
Mpol1304p=matrix8(Spol1inip,Spol1f304p)
Mpol1304m=matrix8(Spol1inim,Spol1f304m)

#pol1 at 349
Mpol1349=matrix8(Spol1ini,Spol1f349)
Mpol1349p=matrix8(Spol1inip,Spol1f349p)
Mpol1349m=matrix8(Spol1inim,Spol1f349m)

######STANDART DEVIATION OF MATRIXES########

devMpol134=((Mpol134p-Mpol134)+(Mpol134-Mpol134m))/2
devMpol1304=((Mpol1304p-Mpol1304)+(Mpol1304-Mpol1304m))/2
devMpol1349=((Mpol1349p-Mpol1349)+(Mpol1349-Mpol1349m))/2
######Rotation of Mpol1 due to errors after component replacement
Mpol134=np.matmul(np.matmul(Mrot(3.238),Mpol134),Mrot(-3.238))
Mpol134p=np.matmul(np.matmul(Mrot(3.238),Mpol134p),Mrot(-3.238))
Mpol134m=np.matmul(np.matmul(Mrot(3.238),Mpol134m),Mrot(-3.238))
devMpol134=((Mpol134p-Mpol134)+(Mpol134-Mpol134m))/2
#Mpol134,Mpol1304,Mpol1349-matrixes itself
#Spol1ini-initial vectors
#Spol1f34,Spol1f304,Spol1f349-final vectors

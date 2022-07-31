from Unwrapdata import *
from Vectorplot import *
from MatrixCalcFrom_8_Vectors import *
from pathes import path

#######DATA LOAD#######

#Vectors before BS

lcv1pol134aa=path+'\lcv1pol134.csv'
lcv2pol134aa=path+'\lcv2pol134.csv'
lcv3pol134aa=path+'\lcv3pol134.csv'
lcv4pol134aa=path+'\lcv4pol134.csv'
lcv1npol134aa=path+'\lcv1npol134.csv'
lcv2npol134aa=path+'\lcv2npol134.csv'
#Vectors after BS
##BST
bstv1naa=path+r'\bstv1n.csv'
bstv2naa=path+r'\bstv2n.csv'
bstv3aa=path+r'\bstv3.csv'
bstv4aa=path+r'\bstv4.csv'
bstv1aa=path+r'\bstv1.csv'
bstv2aa=path+r'\bstv2.csv'

########DATA UNWRAP########

#Vectors before BS

lcv1pol134,avglcv1pol134,devlcv1pol134=ext(lcv1pol134aa)
lcv2pol134,avglcv2pol134,devlcv2pol134=ext(lcv2pol134aa)
lcv3pol134,avglcv3pol134,devlcv3pol134=ext(lcv3pol134aa)
lcv4pol134,avglcv4pol134,devlcv4pol134=ext(lcv4pol134aa)
lcv1npol134,avglcv1npol134,devlcv1npol134=ext(lcv1npol134aa)
lcv2npol134,avglcv2npol134,devlcv2npol134=ext(lcv2npol134aa)

#Vectors after BS

bstv1n,avgbstv1n,devbstv1n=ext(bstv1naa)
bstv2n,avgbstv2n,devbstv2n=ext(bstv2naa)
bstv3,avgbstv3,devbstv3=ext(bstv3aa)
bstv4,avgbstv4,devbstv4=ext(bstv4aa)
bstv1,avgbstv1,devbstv1=ext(bstv1aa)
bstv2,avgbstv2,devbstv2=ext(bstv2aa)

####MATRIXES BUILDED FROM VECTORS######
#Initial

Sbstini=np.zeros((4,4))
Sbstini[:,0]=avglcv1npol134*0.743
Sbstini[:,1]=avglcv2npol134*0.743
Sbstini[:,2]=avglcv3pol134*0.736
Sbstini[:,3]=avglcv4pol134*0.739

#After BS

Sbstf=np.zeros((4,4))
Sbstf[:,0]=avgbstv1n*0.3075
Sbstf[:,1]=avgbstv2n*0.3145
Sbstf[:,2]=avgbstv3*0.3035/0.3082*0.3145
Sbstf[:,3]=avgbstv4*0.302/0.3088*0.3145

#for deviation

Sbstf1=np.zeros((4,4))
Sbstf1[:,0]=avgbstv1
Sbstf1[:,1]=avgbstv2
Sbstf1[:,2]=avgbstv3
Sbstf1[:,3]=avgbstv4

######MATRIXES OF VECTORS+DEV#########

#Initial

Sbstinip=np.zeros((4,4))
Sbstinip[:,0]=(avglcv1npol134+devlcv1npol134)*0.743
Sbstinip[:,1]=(avglcv2npol134+devlcv2npol134)*0.743
Sbstinip[:,2]=(avglcv3pol134+devlcv3pol134)*0.736
Sbstinip[:,3]=(avglcv4pol134+devlcv4pol134)*0.739

#After BS

Sbstfp=np.zeros((4,4))
Sbstfp[:,0]=(avgbstv1n+devbstv1n)*0.3075
Sbstfp[:,1]=(avgbstv2n+devbstv2n)*0.3145
Sbstfp[:,2]=(avgbstv3+devbstv3)*0.3035/0.3082*0.3145
Sbstfp[:,3]=(avgbstv4+devbstv4)*0.302/0.3088*0.3145

#for deviation

Sbstf1p=np.zeros((4,4))
Sbstf1p[:,0]=avgbstv1+devbstv1
Sbstf1p[:,1]=avgbstv2+devbstv2
Sbstf1p[:,2]=avgbstv3+devbstv3
Sbstf1p[:,3]=avgbstv4+devbstv4

######MATRIXES OF VECTORS-DEV#########

#Initial

Sbstinim=np.zeros((4,4))
Sbstinim[:,0]=(avglcv1npol134-devlcv1npol134)*0.743
Sbstinim[:,1]=(avglcv2npol134-devlcv2npol134)*0.743
Sbstinim[:,2]=(avglcv3pol134-devlcv3pol134)*0.736
Sbstinim[:,3]=(avglcv4pol134-devlcv4pol134)*0.739

#After BS

Sbstfm=np.zeros((4,4))
Sbstfm[:,0]=(avgbstv1n-devbstv1n)*0.3075
Sbstfm[:,1]=(avgbstv2n-devbstv2n)*0.3145
Sbstfm[:,2]=(avgbstv3-devbstv3)*0.3035/0.3082*0.3145
Sbstfm[:,3]=(avgbstv4-devbstv4)*0.302/0.3088*0.3145

#for deviation

Sbstf1m=np.zeros((4,4))
Sbstf1m[:,0]=avgbstv1-devbstv1
Sbstf1m[:,1]=avgbstv2-devbstv2
Sbstf1m[:,2]=avgbstv3-devbstv3
Sbstf1m[:,3]=avgbstv4-devbstv4

######MUELLER MATRIXES OF POL1#######

#BST
Mbst=matrix8(Sbstini,Sbstf)
Mbstp=matrix8(Sbstinip,Sbstfp)
Mbstm=matrix8(Sbstinim,Sbstfm)

#for deviation

Mbst1=matrix8(Sbstini,Sbstf1)
Mbst1p=matrix8(Sbstinip,Sbstf1p)
Mbst1m=matrix8(Sbstinim,Sbstf1m)

######STANDART DEVIATION OF MATRIXES########

devMbst=((Mbstp-Mbst)+(Mbst-Mbstm))/2

#for deviation

devMbst1=((Mbst1p-Mbst1)+(Mbst1-Mbst1m))/2
#Mbst-matrix itself
#Sbstini-initial vectors
#Sbstf-final vectors
#Use devMbst1 for deviation calculation
# from py_pol.stokes import Stokes
# from VectorRenormalization import renormarr
# plott(renormarr(Sbstf1))
# plott(renormarr(np.dot(Mbst1,Sbstini)))
# S1 = Stokes('1')
# S1.from_matrix(renormarr(Sbstf1))
# S1.draw_ellipse(draw_arrow=True, figsize=(6, 6))
# S1 = Stokes('2')
# S1.from_matrix(renormarr(np.dot(Mbst1,Sbstini)))
# S1.draw_ellipse(draw_arrow=True, figsize=(6, 6))
# plt.show()
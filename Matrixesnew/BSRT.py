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
bstv1naa=path+r'\bsrv1n.csv'
bstv2naa=path+r'\bsrv2n.csv'
bstv3aa=path+r'\bsrv3.csv'
bstv4aa=path+r'\bsrv4.csv'
#bstv1aa=r'C:\Users\averin\Desktop\SetupModel\setupmodel\bsrv1.csv'
#bstv2aa=r'C:\Users\averin\Desktop\SetupModel\setupmodel\bsrv2.csv'

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
#bstv1,avgbstv1,devbstv1=ext(bstv1aa)
#bstv2,avgbstv2,devbstv2=ext(bstv2aa)

####MATRIXES BUILDED FROM VECTORS######
#Initial

Sbsrini=np.zeros((4,4))
Sbsrini[:,0]=avglcv1npol134*0.743
Sbsrini[:,1]=avglcv2npol134*0.743
Sbsrini[:,2]=avglcv3pol134*0.736
Sbsrini[:,3]=avglcv4pol134*0.739

#After BS

Sbsrf=np.zeros((4,4))
Sbsrf[:,0]=avgbstv1n*0.352
Sbsrf[:,1]=avgbstv2n*0.339
Sbsrf[:,2]=avgbstv3*0.337/0.336*0.339
Sbsrf[:,3]=avgbstv4*0.344/0.338*0.339

######MATRIXES OF VECTORS+DEV#########

#Initial

Sbstinip=np.zeros((4,4))
Sbstinip[:,0]=(avglcv1npol134+devlcv1npol134)*0.743
Sbstinip[:,1]=(avglcv2npol134+devlcv2npol134)*0.743
Sbstinip[:,2]=(avglcv3pol134+devlcv3pol134)*0.736
Sbstinip[:,3]=(avglcv4pol134+devlcv4pol134)*0.739

#After BS

Sbstfp=np.zeros((4,4))
Sbstfp[:,0]=(avgbstv1n+devbstv1n)*0.352
Sbstfp[:,1]=(avgbstv2n+devbstv2n)*0.339
Sbstfp[:,2]=(avgbstv3+devbstv3)*0.337/0.336*0.339
Sbstfp[:,3]=(avgbstv4+devbstv4)*0.344/0.338*0.339


######MATRIXES OF VECTORS-DEV#########

#Initial

Sbstinim=np.zeros((4,4))
Sbstinim[:,0]=(avglcv1npol134-devlcv1npol134)*0.743
Sbstinim[:,1]=(avglcv2npol134-devlcv2npol134)*0.743
Sbstinim[:,2]=(avglcv3pol134-devlcv3pol134)*0.736
Sbstinim[:,3]=(avglcv4pol134-devlcv4pol134)*0.739

#After BS

Sbstfm=np.zeros((4,4))
Sbstfm[:,0]=(avgbstv1n-devbstv1n)*0.352
Sbstfm[:,1]=(avgbstv2n-devbstv2n)*0.339
Sbstfm[:,2]=(avgbstv3-devbstv3)*0.337/0.336*0.339
Sbstfm[:,3]=(avgbstv4-devbstv4)*0.344/0.338*0.339



######MUELLER MATRIXES OF POL1#######

#BST
Mbsr=matrix8(Sbsrini,Sbsrf)
Mbstp=matrix8(Sbstinip,Sbstfp)
Mbstm=matrix8(Sbstinim,Sbstfm)



######STANDART DEVIATION OF MATRIXES########

devMbsr=((Mbstp-Mbsr)+(Mbsr-Mbstm))/2


#Mbst-matrix itself
#Sbstini-initial vectors
#Sbstf-final vectors
#Use devMbst1 for deviation calculation
from VectorRenormalization import renormarr
#plott(renormarr(np.matmul(Mbsr+devMbsr,Sbsrini)))
#plott(renormarr(Sbsrf))
#plt.show()
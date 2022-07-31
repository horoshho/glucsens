from Unwrapdata import *
from Vectorplot import *
from MatrixCalcFrom_8_Vectors import *
from pathes import path
#######DATA LOAD#######

#Vectors before pol2

bpol3v1naa=path+r'\bpol3v1n.csv'
bpol3v2naa=path+r'\bpol3v2n.csv'
bpol3v3aa=path+r'\bpol3v3.csv'
bpol3v4aa=path+r'\bpol3v4.csv'

#Vectors after pol2
##BST
apol3v1naa=path+r'\apol3v1n.csv'
apol3v2naa=path+r'\apol3v2n.csv'
apol3v3aa=path+r'\apol3v3.csv'
apol3v4aa=path+r'\apol3v4.csv'

########DATA UNWRAP########

#Vectors before pol2

bpol3v1n,avgbpol3v1n,devbpol3v1n=ext(bpol3v1naa)
bpol3v2n,avgbpol3v2n,devbpol3v2n=ext(bpol3v2naa)
bpol3v3,avgbpol3v3,devbpol3v3=ext(bpol3v3aa)
bpol3v4,avgbpol3v4,devbpol3v4=ext(bpol3v4aa)

#Vectors after pol2

apol3v1n,avgapol3v1n,devapol3v1n=ext(apol3v1naa)
apol3v2n,avgapol3v2n,devapol3v2n=ext(apol3v2naa)
apol3v3,avgapol3v3,devapol3v3=ext(apol3v3aa)
apol3v4,avgapol3v4,devapol3v4=ext(apol3v4aa)

####MATRIXES BUILDED FROM VECTORS######
#Initial

Sbpol3=np.zeros((4,4))
Sbpol3[:,0]=avgbpol3v1n*0.1265
Sbpol3[:,1]=avgbpol3v2n*0.130
Sbpol3[:,2]=avgbpol3v3*0.1315*0.130/0.1335
Sbpol3[:,3]=avgbpol3v4*0.131*0.130/0.1335

#After pol2

Sapol3=np.zeros((4,4))
Sapol3[:,0]=avgapol3v1n*0.02065
Sapol3[:,1]=avgapol3v2n*0.03638
Sapol3[:,2]=avgapol3v3*0.047
Sapol3[:,3]=avgapol3v4*0.043


######MATRIXES OF VECTORS+DEV#########

#Initial

Sbpol3p=np.zeros((4,4))
Sbpol3p[:,0]=(avgbpol3v1n+devbpol3v1n)*0.1265
Sbpol3p[:,1]=(avgbpol3v2n+devbpol3v2n)*0.130
Sbpol3p[:,2]=(avgbpol3v3+devbpol3v3)*0.1315*0.130/0.1335
Sbpol3p[:,3]=(avgbpol3v4+devbpol3v4)*0.131*0.130/0.1335

#After pol2

Sapol3p=np.zeros((4,4))
Sapol3p[:,0]=(avgapol3v1n+devapol3v1n)*0.02065
Sapol3p[:,1]=(avgapol3v2n+devapol3v2n)*0.03638
Sapol3p[:,2]=(avgapol3v3+devapol3v3)*0.047
Sapol3p[:,3]=(avgapol3v4+devapol3v4)*0.043

######MATRIXES OF VECTORS-DEV#########

#Initial

Sbpol3m=np.zeros((4,4))
Sbpol3m[:,0]=(avgbpol3v1n-devbpol3v1n)*0.1265
Sbpol3m[:,1]=(avgbpol3v2n-devbpol3v2n)*0.130
Sbpol3m[:,2]=(avgbpol3v3-devbpol3v3)*0.1315*0.130/0.1335
Sbpol3m[:,3]=(avgbpol3v4-devbpol3v4)*0.131*0.130/0.1335

#After pol2

Sapol3m=np.zeros((4,4))
Sapol3m[:,0]=(avgapol3v1n-devapol3v1n)*0.02065
Sapol3m[:,1]=(avgapol3v2n-devapol3v2n)*0.03638
Sapol3m[:,2]=(avgapol3v3-devapol3v3)*0.047
Sapol3m[:,3]=(avgapol3v4-devapol3v4)*0.043

######MUELLER MATRIXES OF POL1#######

#Pol2
Mpol3=matrix8(Sbpol3,Sapol3)
Mpol3p=matrix8(Sbpol3p,Sapol3p)
Mpol3m=matrix8(Sbpol3m,Sapol3m)

######STANDART DEVIATION OF MATRIXES########

devMpol3=((Mpol3p-Mpol3)+(Mpol3-Mpol3m))/2

#Mpol3-matrix itself
#Sbpol3-initial vector
#Sapol3-final vector
#devMpol3-deviation
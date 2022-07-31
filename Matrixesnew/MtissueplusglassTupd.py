from Mglplustissueupd import devMnlowsimple,Mnlowsimple,devMnfsimple,Mnfsimple,np, Snalensimple,Snafsimple,Mnlowmsimple,Mnlowpsimple,Mnfmsimple,Mnfpsimple,Snalowsimple
Mtrf=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])*480*10**(-3)/305
Mtrlow=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])*570*10**(-3)/305
MfT=np.matmul(Mnfsimple,Mtrf)
MfpT=np.matmul(Mnfpsimple,Mtrf)
MfmT=np.matmul(Mnfmsimple,Mtrf)
devMfT=((MfpT-MfT)+(MfT-MfmT))/2
MlowT=np.matmul(Mnlowsimple,Mtrlow)
MlowpT=np.matmul(Mnlowpsimple,Mtrlow)
MlowmT=np.matmul(Mnlowmsimple,Mtrlow)
devMlowT=((MlowpT-MlowT)+(MlowT-MlowmT))/2
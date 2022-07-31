import numpy as np
import re
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 22})

def opener(expnum,k):

    a=r'D:\Python\08.07.2022forhome'
    dpath = a+r'\meas' + expnum + k + '.npy'
    cpath = a+r'\vid' + expnum + k + '.npy'
    ctpath = a+r'\ctime' + expnum + k + '.npy'
    dtpath = a+r'\dtime' + expnum + k + '.npy'

    b = np.load(cpath)
    print(b.shape)
    b1 = np.load(dpath)
    print(b1.shape)
    t = np.load(ctpath)
    print(t.shape)
    t1 = np.load(dtpath)
    print(t1.shape)

    fin = []
    for i in range(len(t)):
        for j in range(len(t1)):
            if t1[j] >= t[i]:
                fin.append(j)
                break

    bb1 = b1
    #grad search of LC cycle finish points
    g = 5
    cg = np.zeros_like(bb1)
    for i in range(len(bb1) - g):
        cg[i] = bb1[i] - np.mean(bb1[i:i + g])
    #grad search of LC cycle start points
    g = 5
    cg2 = np.zeros_like(bb1)
    for i in range(len(bb1) - g):
        cg2[i] = np.mean(bb1[i - g:i + 1]) - bb1[i]
    # plt.plot(bb1)
    # #plt.figure()
    # plt.plot(cg+2441)
    # plt.title('CG')
    # plt.figure()
    # plt.plot(cg2)
    # plt.title('CG1')
    f = 0
    sti = 0
    fni = 0
    stcg = np.ones_like(cg) * -2000
    fncg = np.ones_like(cg) * -2000
    nst = []
    nfin = []
    for i in range(len(cg)):
        if cg[i] > 300 and f == 0 and 1000>i - sti > 330:
            stcg[i] = cg[i]
            sti = i
            f = 1
            nst.append(i)
        if cg[i] < -300 and f == 1 and 1000>i - fni > 500:
            fncg[i] = cg[i]
            fni = i
            f = 0
            nfin.append(i)
    # plt.plot(bb1)
    # # plt.figure()
    # # plt.plot(cg + 2441)
    # plt.plot(nst,bb1[nst],'*r')
    # plt.plot(nfin, bb1[nfin],'*g')
    # plt.figure()
    # plt.plot(cg)
    # plt.title('CG')
    from scipy.signal import find_peaks
    peaksmax, _ = find_peaks(cg, width=[6, 60])
    peaksmin, _ = find_peaks(1 - cg, width=[6, 60])
    peaks2max, _ = find_peaks(cg2, width=[6, 60])
    peaks2min, _ = find_peaks(1 - cg2, width=[6, 60])
    maxfn = []
    maxst = []
    for i in range(len(peaksmax)):
        for j in range(len(peaks2min)):
            if cg[peaksmax[i]] > 20 and 10 < peaksmax[i] - peaks2min[
                j] < 20:  # If grad is high enough and far enough from previous peak
                maxfn.append(peaksmax[i]-1)
                maxst.append(peaks2min[j]+2)#rise time 75ms we have 33 ms per point=>either +2 or +3#were 2
                break
    minfn = []
    minst = []
    for i in range(len(peaksmin)):
        for j in range(len(peaks2max)):
            if cg[peaksmin[i]] < -20 and 7 < peaksmin[i] - peaks2max[
                j] < 15:  # If grad is high enough and far enough from previous peak
                minfn.append(peaksmin[i]-1)
                minst.append(peaks2max[j]+2)#rise time 75ms we have 33 ms per point=>either +2 or +3#were 2
                break
    # plt.figure()
    # plt.plot(bb1)
    # plt.plot(maxst, bb1[maxst], '*r')
    # plt.plot(maxfn, bb1[maxfn], '*g')
    # plt.plot(minst, bb1[minst], '*r')
    # plt.plot(minfn, bb1[minfn], '*g')
    avgmax = []
    avgmin = []
    maxpos = []
    minpos = []
    mnpos=[]
    avgmn=[]
    avgfeat=[]
    lef = 0  # Displacement from right and left edges of LC cycles, to subtract points where LC is not saturated
    rig = 0
    for i in range(len(maxfn)):
        for j in range(len(minst)):
            if 4 < minst[j] - maxfn[i] < 10:
                avgmax.append(np.mean(bb1[maxst[i] + lef:maxfn[i] - rig]))
                avgmin.append(np.mean(bb1[minst[j] + lef:minfn[j] - rig]))
                avgmn.append((avgmax[-1]+avgmin[-1])/2)
                avgfeat.append((avgmax[-1] - avgmin[-1]) )

                maxpos.append((-maxst[i] - lef + maxfn[i] - rig) / 2 + maxst[i] + lef)
                minpos.append((-minst[j] - lef + minfn[j] - rig) / 2 + minst[j] + lef)
                mnpos.append((minpos[-1]-maxpos[-1])/2+maxpos[-1])
                break
    # plt.figure()
    # plt.plot(bb1)
    # plt.plot(mnpos, avgmn, '*r')
    #plt.plot(minpos, avgmin, '*g')
    st1 = []
    fn1 = []
    st1.append(0)
    Afeat=np.empty((min(len(nfin),len(nst)),len(mnpos)))
    Amn = np.empty((min(len(nfin), len(nst))+1, len(mnpos)))
    Amn[:]=np.nan
    Apos = np.empty((min(len(nfin), len(nst)), len(mnpos)))
    for i in range(len(maxpos) - 1):
        if avgmax[i]  > 3000 and avgmax[i + 1]  < 3000:
            fn1.append(i)
        if i + 2 == len(maxpos):
            fn1.append(i + 1)
        if avgmax[i]  < 3000 and avgmax[i + 1]  > 3000:
            st1.append(i + 1)
    minle=min(len(nfin),len(nst))
    for i in range(len(mnpos)):
        for j in range(minle):
            # if mnpos[i] in range(nst[j]+70,nfin[j]-15):
            #     Afeat[j,i]=avgfeat[i]
            #     Apos[j,i]=mnpos[i]
            if 0<mnpos[i]<nst[j]  and j==0:
                Amn[0,i]=avgmn[i]
            if  j!=minle-1 and nfin[j]<mnpos[i]<nst[j+1]   :#and j!=0
                Amn[j+1,i]=avgmn[i]
            if  j==minle-1 and nfin[j]<mnpos[i]<len(cg) :
                Amn[j+1,i]=avgmn[i]
    mneig=np.zeros(min(len(nfin), len(nst))+1)
    for i in range(min(len(nfin), len(nst))+1):
        mneig[i]=np.nanmean(Amn[i,:])
    # fsig=np.array([])
    # mxsig = np.array([])
    # mnsig = np.array([])
    # poss = np.array([])
    fsig=[]
    mxsig = []
    mnsig = []
    poss = []
    vall=[]
    avgval=[]
    avgvalcorr = []
    fsignocorr=[]
    for i in range(len(mnpos)):
        for j in range(min(len(nfin), len(nst))):
            if nst[j]+ 70 <mnpos[i]< nfin[j] - 15 :
                #fsig=np.concatenate((fsig,avgfeat[i]))#/((mneig[j]+mneig[j+1])/2)))
                fsig.append( avgfeat[i]/((mneig[j]+mneig[j+1])/2))
                fsignocorr.append( avgfeat[i])
                avgval.append(avgmn[i])
                avgvalcorr.append(avgmn[i]/((mneig[j]+mneig[j+1])/2))
                #mxsig=np.concatenate((mxsig,avgmax[i]/((mneig[j]+mneig[j+1])/2)))
                mxsig.append(avgmax[i] / ((mneig[j] + mneig[j + 1]) / 2))
                #mnsig = np.concatenate((mnsig,avgmin[i] / ((mneig[j] + mneig[j + 1]) / 2)))
                mnsig.append( avgmin[i] / ((mneig[j] + mneig[j + 1]) / 2))
                #poss=np.concatenate((poss,mnpos[i]))
                poss.append( mnpos[i])
                vall.append(((mneig[j] + mneig[j + 1]) / 2))
                #print(range(nst[j] + 70, nfin[j] - 15))
                break
    print(avgfeat)
    print(mneig)
    print(fsig)
    plt.figure()
    plt.title('Experiment 5.1.')
    plt.plot(bb1,label='4.6 mmol/dl')
    plt.plot(mnpos, avgmn, '*g',label='all founded point')
    plt.plot(poss, avgval, '*r',label='measured finger signal')
    plt.legend()
    pctr = np.zeros((len(poss), b[0].shape[0], b[0].shape[1]))
    newpos = np.zeros(len(poss))
    removed=[]
    for i in range(len(poss)):
        for j in range(len(fin) - 1):
            if fin[j] < poss[i]  <= fin[j + 1]:
                if b[j,555,1212]>=249:
                    pctr[i] = b[j]
                if b[j, 555, 1212] < 249:
                    f=0
                    for k in range(1,3):
                        if b[j+k,555,1212]>=249:
                            pctr[i] = b[j+k]
                            f=1
                            break
                        if b[j-k,555,1212]>=249:
                            pctr[i] = b[j-k]
                            f=1
                            break
                    if f==0:
                        print(i,'removed element')
                        removed.append(i)
                        pctr[i] = b[j]
                # if b[j,555,1212]<249 and b[j+1,555,1212]>=249 and b[j-1,555,1212]>=249:
                #     if abs(poss[i]-fin[j + 2])>abs(poss[i]-fin[j - 1]):
                #         pctr[i] = b[j-1]
                #     else:
                #         pctr[i] = b[j + 1]
                # if b[j, 555, 1212] < 249 and b[j + 1, 555, 1212] >=249 and b[j - 1, 555, 1212] < 249:
                #     pctr[i] = b[j + 1]
                # if b[j, 555, 1212] < 249 and b[j + 1, 555, 1212] < 249 and b[j - 1, 555, 1212] >= 249:
                #     pctr[i] = b[j - 1]

                break
    #Determining the points with finger singal, its feature value and making correction with regard to reference signal
    np.save('pctr' + expnum + k + '.npy',pctr)
    np.save('signal' + expnum + k + '.npy', fsig)
    np.save('maxsig' + expnum + k + '.npy', mxsig)
    np.save('minsig' + expnum + k + '.npy', mnsig)
    np.save('pos' + expnum + k + '.npy', poss)
    np.save('removed' + expnum + k + '.npy', removed)
    # np.save('signal' + expnum + k + '1.npy', fsig)
    # np.save('signal' + expnum + k + '11.npy', fsignocorr)
    # np.save('avgval' + expnum + k + '1.npy', avgvalcorr)

expnum='5'
k=np.linspace(1,5,5)
for i in range(1):#was len(k) by default, not to load a lot of large picture files it was reduced to 1
    opener(expnum,str(int(1)))#was k[i]
#opener(expnum,'5')
plt.show()
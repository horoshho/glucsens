import pyvisa
import numpy as np
from pyvisa.constants import StopBits, Parity

#Ini of lock in
rm = pyvisa.ResourceManager('@py')
my_instrument = rm.open_resource('ASRL5::INSTR',
    baud_rate=9600, data_bits=8, write_termination = '\n',read_termination='\n',
    parity=Parity.none)

#Ini of camera
from instrumental.drivers.cameras import uc480
instruments = uc480.list_instruments()
cam = uc480.UC480_Camera(instruments[0])
import time

#Lock in preset
my_instrument.write('REST')
time.sleep(0.5)
my_instrument.write('*CLS')
my_instrument.write('SRAT9')#5#8
my_instrument.write('REST')

#Camera preset
cam.start_live_video(framerate="10Hz")
my_instrument.write('STRT')
kpath=r'C:\Users\averin\Desktop\exp05.05.2022\k.txt'
kval=open(kpath,'r')
k=int(kval.read())
kstr=str(k)
kval.close()
print(k)
expnum='2'
#k='1'# number in file name for save
rf='w'#recording format
css=0#Camera amount of images at the beggining of the loop
dss=0#Signal amount of points at the beggining of the loop
carr=[]#Array of camera images
darr=[]#Array of detector signals
dpath=r'C:\Users\averin\Desktop\exp05.05.2022\meas'+expnum+kstr+'.npy'
cpath=r'C:\Users\averin\Desktop\exp05.05.2022\vid'+expnum+kstr+'.npy'
ctpath=r'C:\Users\averin\Desktop\exp05.05.2022\ctime'+expnum+kstr+'.npy'
dtpath=r'C:\Users\averin\Desktop\exp05.05.2022\dtime'+expnum+kstr+'.npy'
kval=open(kpath,'w')
kval.write(str(k+1))
kval.close()
cf=open(cpath,rf)
df=open(dpath,rf)
ctime=open(ctpath,rf)
dtime=open(dtpath,rf)
x=np.array([])
ctimeful=np.array([])
dtimeful=np.array([])

st=time.time()
plencarr=0
while True:
    try:
        carr.append(cam.grab_image(timeout='100s', copy=True, exposure_time='99.9ms'))  # Tacking images from camera
        my_instrument.write('SPTS?')
        n1 = int(my_instrument.read('\r'))
        if n1 > 100:
            my_instrument.write('PAUS')
            st1 = time.time()  # computation and acquisition start time
            my_instrument.write('TRCL?1,0,' + str(n1 - 1))
            x1 = (my_instrument.read_bytes(4 * (n1 - 1), 1500))  # Reading data from lock in
            fin11 = time.time()  # fin11-st1 time for data acquisition from lock in without encoding
            realdata = np.frombuffer(x1, dtype="<i2")
            numbers = realdata[::2] * 2.0 ** (realdata[1::2] - 124)  # Lock in data encoding
            x3 = numbers
            x=np.append(x,x3)
            fin1 = time.time()  # computation and aquisition start time
            print(len(carr))
            csf = len(carr)  # amount of images recorded at that moment, css-amount of images recorded previously
            clen = csf - css  # amount of images recorded per loop
            css = csf
            tlen = st1 - st  # Time of data collection in the loop
            ctime=[tlen / clen * i + st for i in range(clen)]# approximate time of image capture
            ctimeful=np.append(ctimeful,ctime)
            dtime=[tlen / len(x3) * i + st for i in range(len(x3))]# approximate time of data point capture
            dtimeful = np.append(dtimeful, dtime)
            curt = time.time()  # current time
            print(st1 - st, ' How much time one loop of data recording took')
            print(fin11 - st1, ' How much time data aquisition took')
            print(fin1 - st1, ' How much time data aquisition plus encoding took')
            print(curt - fin1, 'How much other file recordings took')
            my_instrument.write('REST')
            st = time.time()
            my_instrument.write('STRT')
    except KeyboardInterrupt:
        print('KeyboardInterrupt exception is caught')
        A=np.zeros((csf,1024,1280))
        for i in range(0, csf):
            A[i,:,:]= carr[i]
        np.save(dpath,x)
        np.save(dtpath,dtimeful)
        np.save(cpath, A)
        np.save(ctpath,ctimeful)

        break

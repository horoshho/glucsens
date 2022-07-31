# glucsens
- openertst.py 
Description: it is a program that threats signal collected from lock-in amplifier and camera pictures. 
It founds points where signal from finger was measured appropriately, devide this signal by reference neighbours to avoid long term signal drifts in photodiode.
And assign camera pictures to each measured from finger point.
How to use: at the beggining of the file change variable a to the folder path to files 'meas51.npy', 'vid51.npy', 'ctime51.npy', 'dtime51.npy'.
Output: files with threated signal from finger and its corresponding images.
- Regrssioncheckupd3.py
Description: it finds regression between images of the finger, their signal and referencly measured glucose concentration.
How to use: change path variable at the beggining to folder where are 'pctr51.npy'...'pctr55.npy','signal51.npy'...'signal55.npy' located.
Output: r2 estimations from different regression methods applied to that data.
- multirecord2.py
Description: Simultaneous record of the signal from lock-in amplifier and camera.

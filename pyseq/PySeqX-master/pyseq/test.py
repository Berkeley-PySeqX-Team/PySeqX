import sys
sys.path.insert(0, "C:\\Users\\clarklab\\Desktop\\pyseq\\PySeqX-master")
import pyseq
hs = pyseq.HiSeq()                  
hs.initializeCams()                
hs.initializeInstruments()          # Initialize x,y,z & objective stages. Initialize lasers and optics (filters)

hs = pyseq.HiSeq(xCOM='COM67', yCOM='COM68', fpgaCOM=['COM10', 'COM11'], laser1COM='COM12', laser2COM='COM13')


# Positioning the stage
# Currently all of the stages move to absolute positions that are defined in steps
Y = 4000000
X = 1000
Z = 0

#hs.y.move(Y)         # Y should be between -7000000 and 7500000
#hs.x.move(X)         # X should be between 1000 and 50000
#hs.z.move([Z, Z, Z]) # Z should be between 0 and 25000

#hs.obj.move(31000)   # Objective should be between 0 and 65000
import sys
#print(sys.path)
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()                  
hs.initializeCams()                
hs.initializeInstruments()          # Initialize x,y,z & objective stages. Initialize lasers and optics (filters)

#hs = pyseq.HiSeq(xCOM='COM67', yCOM='COM68', fpgaCOM=['COM10', 'COM11'], laser1COM='COM12', laser2COM='COM13')


# Positioning the stage
# Currently all of the stages move to absolute positions that are defined in steps
Y = 100000
X = 37500
Z = 0
print("******CHECKPOINT 1*******")
prev_x = hs.x.position
#hs.y.move(Y)         # Y should be between -7000000 and 7500000


#hs.x.move(X)         # X should be between 1000 and 50000
#print("Finished x move.")
#hs.z.move([Z, Z, Z]) # Z should be between 0 and 25000  
#final_x = hs.x.position
#hs.obj.move(31000)   # Objective should be between 0 and 65000

#print("x positions:", prev_x, final_x)


#print y stage pos
prev_y = hs.y._position
hs.y.move(Y)         # Y should be between -7000000 and 7500000

#print("Finished x move.")
#hs.z.move([Z, Z, Z]) # Z should be between 0 and 25000  
final_y = hs.y._position

print("y positions:", prev_y, final_y)
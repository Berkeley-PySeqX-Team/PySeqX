import sys
#print(sys.path)
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq() 
#hs.x.move(50000) #when it is moving, bit 1 is printed, and when it stops, it is bit 0
#hs.f.initialize()
#hs.z.initialize()
#x_pos_fin = hs.x.position
#print(x_pos_fin)

##Y movement
y_pos_init = hs.y._position
Y = 1000000 # Z should be between -7000000 and 7000000  
hs.y.move(Y) 

y_pos_fin = hs.y._position
print(y_pos_init ,y_pos_fin)

## Z movement
#z_pos_init = hs.z.check_position()
#Z = 21000 # Z should be between 0 and 25000  
#hs.z.move([Z,Z,Z]) 

#z_pos_fin = hs.z.check_position()
#print(z_pos_init ,z_pos_fin)

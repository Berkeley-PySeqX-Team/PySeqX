import sys
#print(sys.path)
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()   

#Initialisation instruments = don't need to run this part if already run once (only run the test part => we can do a separate file for initialize and ten just test commands) 
hs.f.initialize()
#hs.y.command('s r0x24 0') #not sure if needed
hs.z.initialize() #sets to 30000

#Test
z_pos_init = hs.z.position
Z = 0 # Z should be between 0 and 25000  
hs.z.move([Z,Z,Z]) #when it is moving, bit 1 is printed, and when it stops, it is bit 0
z_pos_fin = hs.z.position
print(z_pos_init ,z_pos_fin)

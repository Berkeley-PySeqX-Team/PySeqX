import sys
#print(sys.path)
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq,time

hs = pyseq.HiSeq()   

#Initialisation instruments = don't need to run this part if already run once (only run the test part => we can do a separate file for initialize and ten just test commands) 
#hs.f.initialize()
#hs.y.command('s r0x24 21') #not sure if needed
#hs.x.initialize() #sets to 30000

print("wait")
#time.sleep(20)
#Test
x_pos_init = hs.x.position
X = 50000 # possible range of value is betzeen 1000 and 50000
hs.x.move(X) #when it is moving, bit 1 is printed, and when it stops, it is bit 0
hs.x.move(10000)
hs.x.move(30000)
x_pos_fin = hs.x.position
print(x_pos_init ,x_pos_fin)


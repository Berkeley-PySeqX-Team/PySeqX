import sys, time
#print(sys.path)
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
#sys.path.insert(0, "C:\\Users\\clarklab\\Desktop\pyseq\\PySeqX-master") # I try with the other code
import pyseq

hs = pyseq.HiSeq()
#hs.f.initialize()
#hs.message('Initializing X & Y stages')
prev_y = hs.y.position
print(prev_y)
time.sleep(5)

# EL: i only initialize upon startup, and then comment these three lines out.
#hs.y.command('s r0x24 21')
#hs.x.initialize()
#hs.y.initialize()
####################################
prev_y = hs.y.position
print("2:", prev_y)
time.sleep(5)
Y = 150000

hs.y.move(Y)         # Y should be between -15000000 and 0

final_y = hs.y.position
#hs.obj.move(31000)   # Objective should be between 0 and 65000

print("y positions:", prev_y, final_y)
#i feel like it is not working because of a velocity error 'Ystage::Status Register::28:: Velocity window. Set if the absolute velocity error exceeds the velocity window value.'
#happens after this command :g r0xa0
import sys, time
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

# Test script for flowcell A
# There are ten valve in total (1,2,...,10)

hs = pyseq.HiSeq()

prev_valve = hs.v10['A'].check_valve()
time.sleep(5)

hs.v10['A'].initialize()

#move to valve one
hs.v10['A'].move(5)

final_valve = hs.v10['A'].check_valve()

print("valve positions:", f'initialize position for A: {prev_valve}', f'initialize position for A: {final_valve}')


# Test script for flowcell B
# There are ten valve in total (1,2,...,10)

prev_valve = hs.v10['B'].check_valve()
time.sleep(5)

hs.v10['B'].initialize()

#move to valve one
hs.v10['B'].move(5)

final_valve = hs.v10['B'].check_valve()

print("valve positions:", f'initialize position for B: {prev_valve}', f'initialize position for B: {final_valve}')

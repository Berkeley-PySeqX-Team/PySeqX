import sys, time
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()
#hs.T.initialize()

temp_chiller=hs.T.get_chiller_T()
print('Temperature of chiller:', temp_chiller)
temp_fc_a=hs.T.get_fc_T('A')
print('Temperature of A:',temp_fc_a)
temp_fc_b=hs.T.get_fc_T('B')
print('Temperature of B:',temp_fc_b)

#set temperature 20 to 60C for flow cell/ 0.1 to 20C for chiller
T1=20
hs.T.set_fc_T('B',T1)
temp_fc_b_fin=hs.T.get_fc_T('B')
print('Temperature of B:',temp_fc_b_fin)

hs.T.set_chiller_T(10,3)
temp_chiller_f=hs.T.get_chiller_T()
print('Temperature of chiller:', temp_chiller_f)
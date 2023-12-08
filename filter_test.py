import sys, time, os
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()
hs.f.initialize()

optics = pyseq.optics.Optics(hs.f)
optics.initialize()
optics.move_ex('green', 1)
optics.move_ex('red',0.2)
optics.move_em_in(False)
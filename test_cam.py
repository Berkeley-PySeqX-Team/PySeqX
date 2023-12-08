import sys, time, os
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq

# Test script for cam1
hs = pyseq.HiSeq()

print(hs.image_path)
#hs.f.initialize()
#sys.exit(0)
hs.initializeInstruments() # can only call this function at the beginning and then don't
#hs.obj.initialize()
#hs.optics.initialize()
#
hs.initializeCams()

#hs.take_picture(1, "test_img")
hs.take_picture(1, image_name="test_img")



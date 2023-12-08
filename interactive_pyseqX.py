
import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()


def interactive():
    while True:
        module = input("Instrument? \n fpga \n lasers \nobjective \noptics \npump \
                        \nv10 \nv24 \nxstage \nystage \nzstage \ntemperature \ncam1 \ncam2 \n")
        
        classlookup = {'fpga': hs.f, 'ystage': hs.y, 'xstage': hs.x, 'lasers': hs.lasers, \
                    'zstage': hs.z, 'objective': hs.obj, 'optics': hs.optics, 'cam1': hs.cam1, 'cam2': hs.cam2, \
                        'pump': hs.p, 'v10': hs.v10, 'v24': hs.v24, 'temperature': hs.T}
        if module=="exit":
            return
        instrument = classlookup[module]

        initfirst = input("Initialize Instrument First? y/n \n")
        if initfirst == 'y':
            instrument.initialize()
            
        T=True
        while T:
            command = input("Command? ")
            if command == "exit":
                T=False
            else:
                instrument.command(command)

interactive()
                
                
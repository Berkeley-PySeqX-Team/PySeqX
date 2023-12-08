import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()


def test_cam():
    hs.initializeCams()
    hs.initializeInstruments()
    # hs.y.command('s r0x24 21')
    # hs.x.initialize()
    # hs.y.initialize()
    # hs.z.initialize()
    while True:
        move = input('move stage? y/n (exit to exit) \n')
        if move == 'exit':
            return
        if move == 'y':

            ypos = int(input('y position? -7000000 to 7500000 \n'))
            xpos = int(input('x position 1000 to 50000 \n'))
            zpos = int(input('z position? 1 integer 0 to 25000 \n'))
            hs.message('moving x stage')
            xfin = hs.x.move(xpos)
            hs.message('moving y stage')
            yfin = hs.y.move(ypos)
            hs.message('moving z stage')
            zfin = hs.z.move([zpos,zpos,zpos])
            print('x position ', xfin, '\ny position ', yfin, '\nzfin ', zfin)
        cont = input('take another pictures? y/n (exit to exit) \n')
        if cont == 'exit':
            return
        if cont == 'n':
            continue
        frames = int(input('frames? \n'))
        imagename = input('image name? \n')
        print(hs.image_path)
        hs.take_picture(frames, imagename)

test_cam()
    

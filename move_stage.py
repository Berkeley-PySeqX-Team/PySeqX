## WORK IN PROGRESS!!! DOES NOT WORK!!! Feel free to debug if you see something.
# adapted from kelly's while true loop
import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PySeqX-master-JacobEdits\\PySeqX-master")
import pyseq, time, asyncio

hs = pyseq.HiSeq()
x = 30000
y = 0
z=[0,0,0]

#Initialisation instruments = don't need to run this part if already run once (only run the test part => we can do a separate file for initialize and ten just test commands

ansInit = input("Initialize? y/n ")
ansInit = ansInit.lower()
if (ansInit == "y"): 
    hs.f.initialize()
    hs.y.command('s r0x24 21') #not sure if needed
    hs.x.initialize() #sets to 30000
    hs.y.initialize()
    hs.z.initialize()
elif (ansInit != "n"):
    sys.exit(1)
while True:
    print("Current x, y, z: ({}, {}, {})".format(hs.x.position, hs.y.position, hs.z.position))
    print("Moving to: ({}, {}, {})".format(x,y,z))
    time.sleep(10)

    hs.x.move(x)
    hs.y.move(y)
    hs.z.move(z)
    print("Intended move: ({}, {}, {})".format(x,y,z))
    print("Actual position: ({}, {}, {})".format(hs.x.position, hs.y.position, hs.z.position))

    ansExit = input("Exit? ")
    if (ansExit.lower() == "y"):
        sys.exit(2)
    while True:
        new_move = input("Format new move \"x,y,z\": ")
        try:
            assert len(new_move.split(",")) == 3
            assert all(isinstance(val, int) for val in new_move)
        except AssertionError:
            print("reformat response, got {}".format(new_move))
        except:
            pass # idk tbh lmao
        else:
            x, y, *_ = new_move
            z = new_move[-1] * 3
            break
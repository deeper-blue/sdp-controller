import communication
import time
import json
import internal_logic

counter=0
req=communication.Requester('1111','1111')
def Control():
    contReq=True

    ply_count=0
    while contReq:
        t0 = time.time()
        r=req.sendResponse(ply_count)
        if(r.status_code==200):
            t1 =  time.time()
            print("Got response: %fs" % (t1 - t0))
            jsonfile=r.json()
            print(jsonfile)

            for actions,i in enumerate (jsonfile["history"]):
                ply_count= internal_logic.parseJson(jsonfile["history"][actions],ply_count)
                r=req.sendResponse(ply_count)
                print(r)
            time.sleep(10)
            t2 = time.time()
            print("Took: %fs" % (t2 - t0))
            print("\n")

Control()

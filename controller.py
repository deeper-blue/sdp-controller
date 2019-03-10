import communication
import time
import json
#import internal_logic

counter=0
req=communication.Requester('1111','1111')
def Control():
    contReq=True
    ply_count=0
    while contReq:
        r=req.sendResponse(ply_count)
        jsonfile=r.json()
        print(jsonfile)

        for actions in (jsonfile["history"]):
            error,ply_count= internal_logic.parseJson(jsonfile["history"]["actions"])
            if error=="":
                r=req.sendResponse(ply_count)
            contReq=stop
            print(r)
        time.sleep(10)
Control()

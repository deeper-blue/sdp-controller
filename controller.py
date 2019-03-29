import sys
import communication
import time
import json
import internal_logic
from controller_config import config
import client as cl

# Arguably dangerous to assume these exist, but OK to crash if they don't
# since these values are necessary
version = config['controller']['version']

if len(sys.argv)==1:
    controller_id = config['controller']['id']
    robot_ip = config['robot']['ip']
else:
    controller_id = sys.argv[1]
    robot_ip = sys.argv[2]




req = communication.Requester(controller_id, version)

def control_loop():

    ply_count = 0

    while True:
        t0 = time.time()
        r = req.sendResponse(ply_count)
        if r.status_code == 200:
            t1 = time.time()
            print("Got response: {}s".format(t1 - t0))
            jsonfile = r.json()
            print(jsonfile)

            for actions, i in enumerate(jsonfile["history"]):
                ply_count = internal_logic.parseJson(jsonfile["history"][actions],ply_count)
                r = req.sendResponse(ply_count)
                print(r)

            time.sleep(10)
            t2 = time.time()
            print("Took: {}s".format(t2 - t0))
            print("\n")

try:
    control_loop()
except KeyboardInterrupt:
    internal_logic.close()
    sys.exit(0)

# Close robot connection
internal_logic.close()

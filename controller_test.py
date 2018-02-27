import triad_openvr
import time
import sys
import asyncio
import datetime
import random
import websockets


v = triad_openvr.triad_openvr()
v.print_discovered_objects()


async def time(websocket, path):
    while True:
        interval = 1/250
        # start = time.time()
        txt = ""
        for each in v.devices["controller_1"].get_pose_euler():
            txt += "%.4f" % each
            txt += " "
        print("\r" + txt, end="")
        websocket.send(txt)
        # sleep_time = interval-(time.time()-start)
        # if sleep_time>0:
        #     time.sleep(sleep_time)
        await websocket.send(txt)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()





# if len(sys.argv) == 1:
#     interval = 1/250
# elif len(sys.argv) == 2:
#     interval = 1/float(sys.argv[0])
# else:
#     print("Invalid number of arguments")
#     interval = False
    
# if interval:
#     while(True):
#         start = time.time()
#         txt = ""
#         for each in v.devices["controller_1"].get_pose_euler():
#             txt += "%.4f" % each
#             txt += " "
#         print("\r" + txt, end="")
#         websocket.send(txt)
#         sleep_time = interval-(time.time()-start)
#         if sleep_time>0:
#             time.sleep(sleep_time)
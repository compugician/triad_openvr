import triad_openvr
import time
import sys
import struct
# import socket
import random
import asyncio
import websockets

controllerData = 'no data yet'


v = triad_openvr.triad_openvr()
v.print_discovered_objects()

interval = 1/10
    
async def update_vive(websocket, path):
    while(True):
        start = time.time()
        controllerData = ""
        for each in v.devices["controller_1"].get_pose_euler():
            controllerData += "%.4f" % each
            controllerData += " "
        for each in v.devices["controller_2"].get_pose_euler():
            controllerData += "%.4f" % each
            controllerData += " "
        # data =  v.devices["tracker_1"].get_pose_quaternion()
        # sent = sock.sendto(struct.pack('d'*len(data), *data), server_address)
        await websocket.send(controllerData)
        print("\r" + controllerData, end="")
        sleep_time = interval-(time.time()-start)
        await asyncio.sleep(sleep_time)


start_server = websockets.serve(update_vive, '0.0.0.0', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

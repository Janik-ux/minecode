from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
try:
    while True:
        blockEvents = mc.events.pollBlockHits()
        if blockEvents:
            for blockEvent in blockEvents:
                mc.postToChat("Hit detected")
                x,y,z = blockEvent.pos
                mc.setBlock(x,y,z,56)
        sleep(1)
except KeyboardInterrupt:
    print("Stopped")
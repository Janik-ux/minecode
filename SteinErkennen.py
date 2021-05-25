from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True :
    x,y,z = mc.player.getPos()
    print(x,y-1,z)
    block_beneath = mc.getBlockWithData(x,y-1,z)
    print(block_beneath)
    time.sleep(1)
    hits = mc.events.pollBlockHits()
    for hit in hits :
        print(hit)
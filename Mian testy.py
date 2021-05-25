from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()
while True :
    hits = mc.events.pollBlockHits()
    for hit in hits :
        print(hit)
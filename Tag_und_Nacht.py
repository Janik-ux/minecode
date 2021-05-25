from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()

while True :
    mc.setBlocks(62, 63, -60, -193, 63, 195, 0)
    mc.postToChat("Guten Morgen!")
    time.sleep(600)
    mc.setBlocks(62, 63, -60, -193, 63, 195, 35, 15)
    mc.postToChat("Gute Nacht!")
    time.sleep(600)
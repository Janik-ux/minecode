from mcpi.minecraft import Minecraft
import mcpi.block as block
#import time
mc = Minecraft.create()

x, y, z = mc.player.getPos()
x1 = x + 60
z1 = z + 60
# a = 0
# b = 1
# print(x)
# mc.saveCheckpoint()
# mc.setBlocks(x+1, y+1, z+1, x+1, y+1, z+1, 355)
#mc.setBlocks(-10, 62, 12, -12, 62, 10, 0)
#mc.setBlocks(71, 13, -11, 16, 20, -11, 155)
mc.setBlocks(57, 21, -12, 70, 21, -66, 35,7)
# mc.setBlocks(95, -38, -5, 94, -39, -4, 11)
# time.sleep(10)
# mc.restoreCheckpoint()
# mc.setBlock(20,55,-6, 10)
# mc.setBlocks(-73, -63, -45, -73, -45, -48, 42)
# mc.camera.setNormal()
# mc.saveCheckpoint()
# mc.setBlocks(-160,63,-160, 160,63,160, 0)
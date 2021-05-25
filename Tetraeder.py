from mcpi.minecraft import Minecraft
import mcpi.block as block
#import time
mc = Minecraft.create()

x, y, z = mc.player.getPos()
x1 = x + 6
# z1 = z
groundy = y
groundz = z
mc.saveCheckpoint()
print(x,x1)

while True:
    mc.setBlocks(x,y,z,x1,y,z,46,1)
    if x1 - x == 0:
        break
    x += 1
    x1 -= 1
    z += 1
    print(x,x1)

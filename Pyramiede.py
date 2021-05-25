from mcpi.minecraft import Minecraft
import mcpi.block as block
#import time
mc = Minecraft.create()

x, y, z = mc.player.getPos()
x1 = x + 2
z1 = z + 2
mc.saveCheckpoint()

# def smallen(x,z,x1,z1):
#     x += 1
#     z += 1
#     x1 -= 1
#     z1 -= 1
while x1 - x != 0:
    mc.setBlocks(x,y,z,x1,y,z1,46,1)
    mc.setBlocks(x+1,y,z+1,x1-1,y,z1-1, 0)
    if y < 25:
        x -= 1
        z -= 1
        x1 += 1
        z1 += 1
    else:
        x += 1
        z += 1
        x1 -= 1
        z1 -= 1
    y += 1
    # print(x,y,z,x1,y,z1)
a = input("Restore?")
if a == "j" :
    mc.restoreCheckpoint()
else:
    None
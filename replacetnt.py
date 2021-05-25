afrom mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    block1 = mc.getBlock(-15,-57,-68)
    block2 = mc.getBlock(-15,-58,-67)
    block3 = mc.getBlock(-15,-57,-67)
    print(block1)
    if block1 == 0:
        mc.setBlock(-15,-57,-68, 46, 1)
        print("Yes")
    if block2 == 0:
        mc.setBlock(-15,-58,-67, 46, 1)
        print("Yeah")
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getPos()
a = 0
b = 1
# print(x)
mc.setBlocks(x+1, y-62, z-39, x+0, y-62, z-103, 0)
#mc.setBlocks(1, -62, -39, 0, -62, -103, 0)
#mc.setBlocks(-240, -58, -240, 240, -63, 240, 0)
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getPos()

mc.player.setPos(0, 180, 0)

# mc.player.setPos(x, y+30, z)
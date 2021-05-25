
from mcpi.minecraft import Minecraft
import time
import shutil
mc = Minecraft.create()

count = 0
while True :
    position = mc.player.getPos()
    position = list(position)
    position = [round(n) for n in position]
    if position[0] in range(-99, -101, -1) and position[1] == 6 and position[2] in range(65, 67) :
        shutil.copy2("/opt/minecraft-pi/data/images/mob/char.png", "/opt/minecraft-pi/data/images/mob/steve.png")
        shutil.copy2("/home/pi/Minecraft_Skins/agentsmith.png", "/opt/minecraft-pi/data/images/mob/char.png")
    else :
        None
from mcpi.minecraft import Minecraft
import mcpi.block as block
#import time
mc = Minecraft.create()

#lavagraben
setBlocks(50, -10, -70, 70, 0, 70, 11)
setBlocks(-70, -10, 50, 70, 0, 70, 11)
setBlocks(-50, -10, -70, -70, 0, 70, 11)
setBlocks(-70, -10, -50, 70, 0, -70, 11)

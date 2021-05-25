from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()



while True :
    hitted = mc.events.pollBlockHits()
    x, y, z = mc.player.getPos()
    print(hitted)
    for hit in hitted:
        print(hit.pos.x)
        if hit.pos.x == -70 and hit.pos.y == -61 and hit.pos.z == -45 :
            time.sleep(1.5)
            mc.setBlocks(-71,-62,-47,-72,-62,-46, 52)
            mc.player.setPos(x,y+1,z)
            #mc.setBlocks(-71,-63,-47,-72,-63,-46, 0)
            #mc.setBlocks(-71,-59,-47,-72,-59,-46, 52)
            #mc.setBlocks(-71,-60,-47,-72,-60,-46, 0)
#            time.sleep(1)
#            mc.player.setPos(x,y+2,z)
#            mc.setBlocks(-71,-61,-47,-72,-61,-46, 52)
##            mc.setBlocks(-71,-62,-47,-72,-62,-46, 0)
##            mc.setBlocks(-71,-58,-47,-72,-58,-46, 52)
##            mc.setBlocks(-71,-59,-47,-72,-59,-46, 0)
#            time.sleep(1)
#            mc.player.setPos(x,y+3,z)
#            mc.setBlocks(-71,-60,-47,-72,-60,-46, 52)
##            mc.setBlocks(-71,-61,-47,-72,-61,-46, 0)
##            mc.setBlocks(-71,-57,-47,-72,-57,-46, 52)
##            mc.setBlocks(-71,-58,-47,-72,-58,-46, 0)
#            time.sleep(1)
#            mc.player.setPos(x,y+4,z)
#            mc.setBlocks(-71,-59,-47,-72,-59,-46, 52)
##            mc.setBlocks(-71,-60,-47,-72,-60,-46, 0)
##            mc.setBlocks(-71,-56,-47,-72,-56,-46, 52)
##            mc.setBlocks(-71,-57,-47,-72,-57,-46, 0)
#            time.sleep(1)
#            mc.player.setPos(x,y+5,z)
#            mc.setBlocks(-71,-58,-47,-72,-58,-46, 52)
##            mc.setBlocks(-71,-59,-47,-72,-59,-46, 0)
##            mc.setBlocks(-71,-56,-47,-72,-56,-46, 52)
##            mc.setBlocks(-71,-57,-47,-72,-57,-46, 0)
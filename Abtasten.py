from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create("162.55.163.154")
x, y, z = mc.player.getPos()
stone_pos = []
v = 3
for Blockx in range(int(x-v),int(x+v)) :
    #print(Blockx)
    for Blocky in range(int(y-v), int(y+v)) :
        print(Blocky)
        for Blockz in range(int(z-v), int(z+v)) :
            #print(str(Blockz))
            test = mc.getBlock(Blockx, Blocky, Blockz)
            print(test)
            #if test != 0 :
            stone_pos.append([test,Blockx,Blocky, Blockz])
            #print(stone_pos)

                #mc.player.setPos(Blockx, Blocky+10, Blockz)
                #print(Blockx, Blocky
print(stone_pos)
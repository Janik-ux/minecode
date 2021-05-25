from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x, y, z = mc.player.getPos()
stone_pos = []
stone_rel_pos = []
v = 1
projektname = input("Geben Sie einen Projektnamen ein.")
try :
    with open(projektname + ".txt", "r") as f :
        print("Ah. Sie schon wieder. Wollen Sie Ihr Kunstwerk irgendwohin bauen, oder ein neues einscannen?")
except :
    print("Anscheinend gibt es dieses Projekt noch nicht. Bitte geben Sie die äußeren Koordinaten Ihres Kunstwerkes an.")
    with open(projektname + ".txt", "w") as f :
        for Blockx in range(int(x-v),int(x+v)) :
            #print(Blockx)
            for Blocky in range(int(y-v), int(y+v)) :
                #print(Blocky)
                for Blockz in range(int(z-v), int(z+v)) :
                    #print(str(Blockz))
                    test = mc.getBlock(Blockx, Blocky, Blockz)
                    #print(test)
                    #if test != 0 :
                    stone_pos.append([test,Blockx,Blocky, Blockz])

        erster_stein = stone_pos[0]
        #print(erster_stein)

        for stein in stone_pos :
            x = erster_stein[1] - stein[1]
            y = erster_stein[2] - stein[2]
            z = erster_stein[3] - stein[3]
            stone_rel_pos.append([stein[0], x, y, z])
        print(stone_rel_pos)

        for item in stone_pos :
            f.write("%s\n" % item)
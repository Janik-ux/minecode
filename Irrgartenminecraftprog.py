from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()

spawnpoint = 99.5, -2, 16.7
def respawn() :
    mc.postToChat("Tot!!!!")
    time.sleep(1)
    mc.player.setPos(spawnpoint)

def beamen(x, y, z) :
    mc.postToChat("Beamen...")
    time.sleep(1.4)
    mc.player.setPos(x, y, z)

while True :
    position = mc.player.getPos()
    position = list(position)
    position = [round(n) for n in position]
    # print(position)
    hits = mc.events.pollBlockHits()
        # hit = list(hit)
        # print(hit)
        #if hit
# Fallen:
    if position[0] in range(99, 101) and position[1] == -9 and position[2] in range(7, 9) :
        respawn()
    elif position[0] in range(101, 103) and position[1] == -30 and position[2] in range(18, 21) :
        respawn()
    elif position[0] in range(93, 97) and position[1] in range(0, 3) and position[2] in range(1, 3) :
        respawn()
    elif position[0] in range(99, 101) and position[1] == -24 and position[2] in range(18, 20) :
        respawn()
    elif position[0] in range(99, 101) and position[1] == -24 and position[2] in range(20, 23) :
        respawn()
    elif position[0] in range(91, 97) and position[1] == -11 and position[2] in range(30, 34) :
        respawn()
    elif position[0] in range(101, 103) and position[1] == -30 and position[2] in range(22, 24) :
        respawn()
    elif position[0] in range(101, 103) and position[1] == -30 and position[2] in range(25, 28) :
        respawn()
    elif position[0] in range(101, 103) and position[1] == -30 and position[2] in range(28, 30) :
        respawn()
    elif position[0] in range(99, 101) and position[1] == -30 and position[2] in range(27, 29) :
        respawn()
    elif position[0] in range(97, 99) and position[1] == -10 and position[2] == 18 :
        respawn()
    elif position[0] in range(88, 90) and position[1] == -10 and position[2] in range(17, 19) :
        mc.setBlocks(89, -11, 18, 87, -11, 15, 0)
        time.sleep(2)
        mc.setBlocks(89, -11, 18, 87, -11, 15, 42)
    elif position[0] in range(88, 90) and position[1] == -27 and position[2] in range(15, 19) :
        respawn()
    elif position[0] in range(88, 90) and position[1] == -10 and position[2] in range(23, 25) :
        mc.setBlocks(88, -11, 26, 88, -11, 20, 0)
        time.sleep(2)
        mc.setBlocks(88, -11, 26, 88, -11, 20, 1)
    elif position[0] in range(88, 90) and position[1] == -42 and position[2] in range(23, 25) :
        respawn()

# transporter:
    elif position[0] in range(35, 37) and position[1] == 5 and position[2] in range(-17, -19, -1) :
        beamen(23.5, 4, -100.6)
    elif position[0] in range(23, 25) and position[1] == 4 and position[2] in range(-99, -101, -1) : # von Bank
        beamen(35.4, 5, -16.4) # nach Platz
    elif position[0] in range(88, 90) and position[1] == -10 and position[2] in range(28, 30) : # von Bank
        beamen(-146.5, -8, 137.5) # nach Platz
    elif position[0] in range(21, 23) and position[1] == -19 and position[2] in range(-35, -37, -1) :
        beamen(21.5, 4, -104.5)
    elif position[0] in range(21, 23) and position[1] == 4 and position[2] in range(-105, -107, -1) :
        beamen(21.5, -19, -36.6)

    else :
        for hit in hits :
            print(hit.pos.x)
            if hit.pos.x == 89 and hit.pos.y == -9 and hit.pos.z == 20 :
                time.sleep(1.5)
                mc.setBlocks(89, -10, 20, 89, -9, 20, 0)
                time.sleep(1.3)
                mc.setBlocks(89, -10, 20, 89, -9, 20, 1)
                if position[0] in range(90, 92) and position[1] == -10 and position[2] in range(28, 30) :
                    print("derturm")
                    mc.setBlocks(89, -10, 28, 89, -9, 28, 0)
                    time.sleep(1.5)
                    mc.setBlocks(89, -10, 28, 89, -9, 28, 1)
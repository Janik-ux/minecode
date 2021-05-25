from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()

spawnpoint = 99.5, -2, 16.7
def respawn() :
    mc.postToChat("Tot!!!!")
    time.sleep(1)
    mc.player.setPos(spawnpoint)

spawnpoint = 0.5, 9, 0.5
def Tot() :
    mc.postToChat("Tot!!!!")
    time.sleep(1)
    mc.player.setPos(spawnpoint)

def beamen(x, y, z) :
    mc.postToChat("Beamen...")
    time.sleep(1.4)
    mc.player.setPos(x, y, z)

def mauerzufahren():
    time.sleep(1)
    mc.setBlocks(-126, 8, 118, -126, 9, 118, 98, 2)
    time.sleep(2.5)
    mc.setBlocks(-120, 8, 117, -120, 10, 108, 98, 2)
    mc.setBlocks(-132, 8, 117, -132, 10, 108, 98, 2)
    time.sleep(2)
    mc.setBlocks(-121, 8, 117, -121, 10, 108, 98, 2)
    mc.setBlocks(-131, 8, 117, -131, 10, 108, 98, 2)
    time.sleep(2)
    mc.setBlocks(-122, 8, 117, -122, 10, 108, 98, 2)
    mc.setBlocks(-130, 8, 117, -130, 10, 108, 98, 2)
    time.sleep(2)
    mc.setBlocks(-123, 8, 117, -123, 10, 108, 98, 2)
    mc.setBlocks(-129, 8, 117, -129, 10, 108, 98, 2)
    time.sleep(2)
    mc.setBlocks(-124, 8, 117, -124, 10, 108, 98, 2)
    mc.setBlocks(-128, 8, 117, -128, 10, 108, 98, 2)
    time.sleep(2)
    mc.setBlocks(-125, 8, 117, -125, 10, 108, 98, 2)
    mc.setBlocks(-127, 8, 117, -127, 10, 108, 98, 2)
    time.sleep(2)
    mc.setBlocks(-126, 8, 117, -126, 10, 108, 98, 2)
    time.sleep(5)

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
    elif position[0] in range(-111, -113, -1) and position[1] == 8 and position[2] in range(119, 121) :
        mc.setBlock(-112, 9, 117, 0)
    elif position[0] in range(-111, -113, -1) and position[1] == 8 and position[2] in range(116, 118) :
        mc.setBlock(-112, 9, 117, 95)
        mc.setBlock(-112, 8, 118, 64, 3)
        mc.setBlock(-112, 9, 118, 64, 11)
    elif position[0] in range(-125, -127, -1) and position[1] == 8 and position[2] in range(117, 119) :
        mauerzufahren()
        secondpos = mc.player.getPos()
        secondpos = list(secondpos)
        secondpos = [round(n) for n in secondpos]
        if secondpos[0] in range(-119, -133, -1) and secondpos[1] == 8 and secondpos[2] in range(108, 119):
            Tot()
        time.sleep(2)
        mc.setBlocks(-120, 8, 117, -132, 10, 108, 0)
        mc.setBlocks(-126, 8, 118, -126, 9, 118, 0)
    elif position[0] in range(-102, -106, -1) and position[1] == 8 and position[2] in range(129, 131) :
        time.sleep(0.3)
        mc.setBlocks(-102, 7, 128, -106, 7, 132, 0)
        time.sleep(2)
        mc.setBlocks(-102, 7, 128, -106, 7, 132, 35, 5)
    elif position[0] in range(-110, -112, -1) and position[1] == 8 and position[2] in range(130, 132) :
        mc.setBlocks(-111, 8, 129, -111, 9, 129, 85)


# transporter:
    elif position[0] in range(35, 37) and position[1] == 5 and position[2] in range(-17, -19, -1) :
        beamen(23.5, 4, -100.6)
    elif position[0] in range(23, 25) and position[1] == 4 and position[2] in range(-99, -101, -1) :
        beamen(35.4, 5, -16.4) # nach Platz
    elif position[0] in range(88, 90) and position[1] == -10 and position[2] in range(28, 30) :
        beamen(-146.5, -8, 137.5) # nach Platz
    elif position[0] in range(21, 23) and position[1] == -19 and position[2] in range(-35, -37, -1) :
        beamen(21.5, 4, -104.5)
    elif position[0] in range(21, 23) and position[1] == 4 and position[2] in range(-105, -107, -1) :
        beamen(21.5, -19, -36.6)

    else :
        for hit in hits :
            print(hits)
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
            if hit.pos.x == -104 and hit.pos.y == 8 and hit.pos.z == 118 or hit.pos.x == -104 and hit.pos.y == 9 and hit.pos.z == 118 :
                time.sleep(0.05)
                mc.setBlock(-104, 7, 119, 0)
                time.sleep(0.5)
                mc.setBlock(-104, 7, 119, 5)
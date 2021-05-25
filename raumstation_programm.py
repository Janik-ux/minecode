from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()
kltorupdown = {1:0, 2:0, 3:0}
def drive(a, b, tor):
    if kltorupdown[tor] == 0:
        return range(a, b, check_neg(a-1,b)), 1
    else:
        return reversed(list(range(a, b+1))), -1

def kltor(xp1, zp1, xp2, zp2, yps, ype, tor):
    coordlist, updown = drive(yps, ype, tor)
    for y in coordlist:
        mc.setBlocks(xp1,y,zp1,xp2,y,zp2, 0)
        mc.setBlocks(xp1,y+updown,zp1,xp2,y+updown,zp2, 35, 7)
        print(y+updown)
        mc.setBlocks(y-40,35,-100,y-40,35,-109, 42*kltorupdown[tor])
        mc.setBlocks(-(y-15),35,-100,-(y-15),35, -109, 42*kltorupdown[tor])
        time.sleep(0.2)
    global kltorupdown
    kltorupdown[tor] += updown

def check_neg(a, b):
    if a < 0 or b < 0:
        neg = -1
    else:
        neg = 1
    return neg

def in_range(x1, x2, y1, y2, z1, z2):
    negx = check_neg(x1, x2)
    negy = check_neg(y1, y2)
    negz = check_neg(z1, z2)
    # print(negx)
    if position[0] in range(x1, x2, negx) and position[1] in range(y1, y2, negy) and position[2] in range(z1, z2, negz):
        return True
    else:
        return False

while True:
    position = mc.player.getPos()
    position = list(position)
    position = [round(n) for n in position]
    # global position
    # print(position)

    # Türen

    # osition[0] in range(-26, -29, -1) and position[1] == -51 and position[2] in range(-158, -160, -1)
    if in_range(42, 46, 13, 14, -70, -73) or in_range(42, 46, 13, 14, -64, -67):
        mc.setBlocks(43,13,-68,43,16,-68, 0)
        mc.setBlocks(44,13,-68,44,16,-68, 0)
        time.sleep(0.07)
        mc.setBlocks(42,13,-68,42,16,-68, 0)
        mc.setBlocks(45,13,-68,45,16,-68, 0)
        time.sleep(0.07)
        mc.setBlocks(41,13,-68,41,16,-68, 0)
        mc.setBlocks(46,13,-68,46,16,-68, 0)
        time.sleep(2)
        mc.setBlocks(41,13,-68,41,16,-68, 42)
        mc.setBlocks(46,13,-68,46,16,-68, 42)
        time.sleep(0.1)
        mc.setBlocks(42,13,-68,42,16,-68, 42)
        mc.setBlocks(45,13,-68,45,16,-68, 42)
        time.sleep(0.1)
        mc.setBlocks(43,13,-68,43,16,-68, 42)
        mc.setBlocks(44,13,-68,44,16,-68, 42)

    hitted = mc.events.pollBlockHits()
    for hit in hitted:
        print(hit.pos.x)
        # kleine Hangertür 1
        if hit.pos.x == -13 and hit.pos.y == 29 and hit.pos.z == -110 or hit.pos.x == -14 and hit.pos.y == 36 and hit.pos.z == -97 :
            kltor(-20, -109, -5, -100, 27, 36, 1)

    # Hangertor groß

        elif (hit.pos.x == 16 and hit.pos.y == 14 and hit.pos.z == -77) or (hit.pos.x == 16 and hit.pos.y == 14 and hit.pos.z == -117) or hit.pos.x == 14 and hit.pos.y == 14 and hit.pos.z == -77 or hit.pos.x == 14 and hit.pos.y == 14 and hit.pos.z == -117 :
            l, updown = drive(13, 32, 2)
            for y in l:
                mc.setBlocks(15,y,-115,15,y,-79, 20*kltorupdown[2])
                time.sleep(0.1)
            kltorupdown[2] += updown
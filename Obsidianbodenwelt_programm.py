sfrom mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()

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
    print(position)
    # Tür
    # osition[0] in range(-26, -29, -1) and position[1] == -51 and position[2] in range(-158, -160, -1)
    if in_range(-26, -29, -51, -52, -158, -160) or in_range(-26, -29, -51, -52, -152, -154):
        mc.setBlocks(-28,-48,-156,-28,-51,-156, 0)
        mc.setBlocks(-27,-48,-156,-27,-51,-156, 0)
        time.sleep(0.07)
        mc.setBlocks(-29,-48,-156,-29,-51,-156, 0)
        mc.setBlocks(-26,-48,-156,-26,-51,-156, 0)
        time.sleep(0.07)
        mc.setBlocks(-30,-48,-156,-30,-51,-156, 0)
        mc.setBlocks(-25,-48,-156,-25,-51,-156, 0)
        time.sleep(2)
        mc.setBlocks(-30,-48,-156,-30,-51,-156, 42)
        mc.setBlocks(-25,-48,-156,-25,-51,-156, 42)
        time.sleep(0.1)
        mc.setBlocks(-29,-48,-156,-29,-51,-156, 42)
        mc.setBlocks(-26,-48,-156,-26,-51,-156, 42)
        time.sleep(0.1)
        mc.setBlocks(-28,-48,-156,-28,-51,-156, 42)
        mc.setBlocks(-27,-48,-156,-27,-51,-156, 42)
        # position[0] in range(-49, -51, -1) and position[1] == -57 and position[2] in range(-131, -133, -1)
    elif in_range(-49, -51, -57, -58, -131, -133) or in_range(-55, -57, -57, -58, -131, -134):
        mc.setBlocks(-53,-54,-132,-53,-57,-132, 0)
        mc.setBlocks(-53,-54,-133,-53,-57,-133, 0)
        time.sleep(0.07)
        mc.setBlocks(-53,-54,-131,-53,-57,-131, 0)
        mc.setBlocks(-53,-54,-134,-53,-57,-134, 0)
        time.sleep(0.07)
        mc.setBlocks(-53,-54,-130,-53,-57,-130, 0)
        mc.setBlocks(-53,-54,-135,-53,-57,-135, 0)
        time.sleep(2)
        mc.setBlocks(-53,-54,-130,-53,-57,-130, 42)
        mc.setBlocks(-53,-54,-135,-53,-57,-135, 42)
        time.sleep(0.07)
        mc.setBlocks(-53,-54,-131,-53,-57,-131, 42)
        mc.setBlocks(-53,-54,-134,-53,-57,-134, 42)
        time.sleep(0.07)
        mc.setBlocks(-53,-54,-132,-53,-57,-132, 42)
        mc.setBlocks(-53,-54,-133,-53,-57,-133, 42)
        # position[0] in range(-49, -51, -1) and position[1] == -57 and position[2] in range(-131, -133, -1)
   # elif in_range(9, 11, -57, -58, -111, -113) or in_range(4, 6, -57, -58, -111, -113):
   #     mc.setBlocks(7,-54,-112,7,-57,-112, 0)
   #     mc.setBlocks(7,-54,-111,7,-57,-111, 0)
   #     time.sleep(0.07)
   #     mc.setBlocks(7,-54,-113,7,-57,-113, 0)
   #     mc.setBlocks(7,-54,-110,7,-57,-110, 0)
   #     time.sleep(0.07)
   #     mc.setBlocks(7,-54,-114,7,-57,-114, 0)
   #     mc.setBlocks(7,-54,-109,7,-57,-109, 0)
   #     time.sleep(2)
   #     mc.setBlocks(7,-54,-114,7,-57,-114, 42)
   #     mc.setBlocks(7,-54,-109,7,-57,-109, 42)
   #     time.sleep(0.07)
   #     mc.setBlocks(7,-54,-113,7,-57,-113, 42)
   #     mc.setBlocks(7,-54,-110,7,-57,-110, 42)
   #     time.sleep(0.07)
   #     mc.setBlocks(7,-54,-112,7,-57,-112, 42)
   #     mc.setBlocks(7,-54,-111,7,-57,-111, 42)
    elif in_range(-11, -13, -61, -65, -99, -102) or in_range(-3, -6, -61, -65, -99, -102):
        mc.setBlock(-8,-62,-102, 0)
        mc.setBlock(-8,-61,-101, 0)
        mc.setBlock(-8,-60,-100, 0)
        mc.setBlock(-8,-59,-99, 0)
        time.sleep(0.07)
        mc.setBlock(-8,-60,-99, 0)
        mc.setBlock(-8,-61,-102, 0)
        time.sleep(0.07)
        mc.setBlocks(-8,-61,-100,-8,-61,-99, 0)
        mc.setBlock(-8,-62,-102, 42)
        mc.setBlocks(-8,-60,-102,-8,-60,-101, 0)
        mc.setBlock(-8,-59,-99, 42)
        time.sleep(0.07)
        mc.setBlocks(-8,-59,-102,-8,-59,-99, 0)
        mc.setBlocks(-8,-62,-102,-8,-62,-99, 0)
        time.sleep(2)
        mc.setBlocks(-8,-59,-102,-8,-59,-99, 42)
        mc.setBlocks(-8,-62,-102,-8,-62,-99, 42)
        time.sleep(0.07)
        mc.setBlocks(-8,-61,-100,-8,-61,-99, 42)
        mc.setBlock(-8,-62,-102, 0)
        mc.setBlocks(-8,-60,-102,-8,-60,-101, 42)
        mc.setBlock(-8,-59,-99, 0)
        time.sleep(0.07)
        mc.setBlock(-8,-60,-99, 42)
        mc.setBlock(-8,-61,-102, 42)
        time.sleep(0.07)
        mc.setBlock(-8,-62,-102, 42)
        mc.setBlock(-8,-61,-101, 42)
        mc.setBlock(-8,-60,-100, 42)
        mc.setBlock(-8,-59,-99, 42)
    hitted = mc.events.pollBlockHits()
    x, y, z = mc.player.getPos()
    print(hitted)
    for hit in hitted:
        print(hit.pos.x)
        if hit.pos.x == 6 and hit.pos.y == -56 and hit.pos.z == -110 or hit.pos.x == 8 and hit.pos.y == -56 and hit.pos.z == -113 :
            time.sleep(0.3)
            mc.setBlocks(7,-57,-112,7,-57,-111, 0)
            time.sleep(0.07)
            mc.setBlocks(7,-56,-112,7,-56,-111, 0)
            time.sleep(0.07)
            mc.setBlocks(7,-55,-112,7,-55,-111, 0)
            time.sleep(2)
            mc.setBlocks(7,-55,-112,7,-55,-111, 42)
            time.sleep(0.07)
            mc.setBlocks(7,-56,-112,7,-56,-111, 42)
            time.sleep(0.07)
            mc.setBlocks(7,-57,-112,7,-57,-111, 42)
        # Fahrstuhl
  #  elif in_range(-70, -73, -61, -63, -45, -48):
  #        mc.player.setPos(x,y+1,z)
  #      mc.setBlocks(-71,-62,-47,-72,-62,-46, 52)
  #      mc.setBlocks(-71,-63,-47,-72,-63,-46, 0)
  #      mc.setBlocks(-71,-59,-47,-72,-59,-46, 52)
  #      mc.setBlocks(-71,-60,-47,-72,-60,-46, 0)
  #      time.sleep(0.07)
  #      mc.player.setPos(x,y+1,z)
  #      mc.setBlocks(-71,-61,-47,-72,-61,-46, 52)
  #      mc.setBlocks(-71,-62,-47,-72,-62,-46, 0)
  #      mc.setBlocks(-71,-58,-47,-72,-58,-46, 52)
  #      mc.setBlocks(-71,-59,-47,-72,-59,-46, 0)
  #      time.sleep(0.07)
  #      mc.player.setPos(x,y+1,z)
  #      mc.setBlocks(-71,-60,-47,-72,-60,-46, 52)
  #      mc.setBlocks(-71,-61,-47,-72,-61,-46, 0)
  #      mc.setBlocks(-71,-57,-47,-72,-57,-46, 52)
  #      mc.setBlocks(-71,-58,-47,-72,-58,-46, 0)
  #      time.sleep(0.07)
  #      mc.player.setPos(x,y+1,z)
  #      mc.setBlocks(-71,-59,-47,-72,-59,-46, 52)
  #      mc.setBlocks(-71,-60,-47,-72,-60,-46, 0)
  #      mc.setBlocks(-71,-56,-47,-72,-56,-46, 52)
  #      mc.setBlocks(-71,-57,-47,-72,-57,-46, 0)
  #      time.sleep(0.07)
  #      mc.player.setPos(x,y+1,z)
  #      mc.setBlocks(-71,-58,-47,-72,-58,-46, 52)
  #      mc.setBlocks(-71,-59,-47,-72,-59,-46, 0)
  #      mc.setBlocks(-71,-56,-47,-72,-56,-46, 52)
  #      mc.setBlocks(-71,-57,-47,-72,-57,-46, 0)
        #time.sleep(2)
        #mc.setBlocks(7,-54,-114,7,-57,-114, 42)
        #mc.setBlocks(7,-54,-109,7,-57,-109, 42)
        #time.sleep(0.07)
        #mc.setBlocks(7,-54,-113,7,-57,-113, 42)
        #mc.setBlocks(7,-54,-110,7,-57,-110, 42)
        #time.sleep(0.07)
        #mc.setBlocks(7,-54,-112,7,-57,-112, 42)
        #mc.setBlocks(7,-54,-111,7,-57,-111, 42)
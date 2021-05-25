from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()

#def beamen(x, y, z) :
#    mc.postToChat("Drücken sie den roten Stein, um in den Hauptturm zu beamen, den Grünen")
#    time.sleep(0.4)
#    mc.player.setPos(x, y, z)

def transporter(x, y, z) :
    mc.player.setPos(x, y, z)

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

while True :
    position = mc.player.getPos()
    position = list(position)
    position = [round(n) for n in position]
    print(position)
# transporter:
    if in_range(19,21,6,7,17,19):               # von Platz
        transporter(-43.6, 5, 6.6)                             # nach Bank
    elif in_range(19,21,6,7,37,39):             # von Platz
        transporter(-27.7, 4, -96.5)                           # nach Zentral
    elif in_range(19,21,6,7,52,54):             # von Platz
        transporter(-111.7, -10, -117.5)                       # nach Eckwasser
    elif in_range(-42,-44,4,5,2,4):             # von Bank
        transporter(-32.4, 4, -96.5)                           # nach Zentral
    elif in_range(-42,-44,5,6,6,8):             # von Bank
        transporter(20.7, 6, 17.5)                             # nach Platz
    elif in_range(-47,-49,4,5,5,7):             # von Bank
        transporter(-118.4, -10, -114.5)                       # nach Eckwasser
    elif in_range(-26,-28,4,5,-96,-98):         # von Zentral
        transporter(20.7, 6, 37.5)                             # nach Platz
    elif in_range(-33,-35,4,5,-96,-98):         # von Zentral
        transporter(-43.7, 4, 2.5)                             # nach Bank
    elif in_range(-33,-35,4,5,-101,-103):       # von Zentral
        transporter(-111.7, -10, -113.5)                       # nach Eckwasser
    elif in_range(-110,-112,-10,-11,-117,-119): # von Eckwasser
        transporter(20.7, 6, 52.5)                             # nach Platz
    elif in_range(-110,-112,-10,-11,-113,-114): # von Eckwasser
        transporter(-32.4, 4, -101.5)                          # nach Zentral
    elif in_range(-119,-121,-10,-11,-114,-116): # von Eckwasser
        transporter(-48.6, 4, 4.5)                             # nach Bank
    elif in_range(-69,-71,-13,-14,-90,-92):     # von Mitarbeiterquartier
        transporter(89.3, 3, 31.5)                             # nach V(links)
    elif in_range(-69,-71,-13,-14,-92,-94):      # von Mitarbeiterquartier
        transporter(89.3, 3, 37.5)                             # nach V(rechts)
    elif in_range(90,92,3,4,31,32):             # von V(links)
        transporter(-68.3, -13, -90.5)                         # nach Mitarbeiterquartier
    elif in_range(90,92,3,4,37,39):             # von V(rechts)
        transporter(-68.3, -13, -92.5)                         # nach Mitarbeiterquartier
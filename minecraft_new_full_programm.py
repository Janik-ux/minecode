from mcpi.minecraft import Minecraft
from tqdm import tqdm
import time
import os
mc = Minecraft.create()

def steinarten(stone):
    steinart = []
    for ste in stone:
        if ste[3] not in steinart:
            steinart.append(ste[3])
        else:
            None
    return steinart

def is_int(s):
    s = s.split(",")
    for n in s:
        #print(n)
        #print(type(n))
        try:
            int(n)
            return True
        except(ValueError):
            return False

def asc_range(a, b):
    if a > b:
        return range(b, a+1)
    else:
        return range(a, b+1)

def ask_for_change(stone_rel_pos, antwort, a, b):
    # antwort will be a list. it searches in stone_rel_pos at the a'th position for the 1. Item in antwort and replaces every b'th position of stone_rel_pos with the 2. Item in antwort
    if is_int(antwort):
        antwort = antwort.split(",")
        # print(antwortc[0])
        for stone in stone_rel_pos:
            # print(stone[a])
            if int(stone[a]) == int(antwort[0]):
                stone[b] = int(antwort[1])
                # print(stone[3])
            else:
                None
    elif antwort == "n":
        print("Na gut, dann nicht!")
    else:
        print("Das waren leider keine Zahlen!:-(")

def save_project(stone_rel_pos):
    with open(projektname + ".txt", "w") as f:
        for item in stone_rel_pos:
            row = ','.join(str(x) for x in item)
            f.write("%s\n" % row)

def rel_pos(stone_pos):
    stone_rel_pos = []
    erster_stein = stone_pos[0]
    # print(erster_stein)
    for stein in stone_pos:
        x = erster_stein[0] - stein[0]
        y = erster_stein[1] - stein[1]
        z = erster_stein[2] - stein[2]
        c = [x, y, z, stein[3], stein[4]]
        stone_rel_pos.append([abs(n) for n in c])
    # print(stone_rel_pos)
    return stone_rel_pos

def abtasten(inx_a, inx_b, iny_a, iny_b, inz_a, inz_b):
    stone_pos = []
    # print(inx_a, inx_b, iny_a, iny_b, inz_a, inz_b)
    for Blockx in asc_range(inx_a, inx_b):
        # print(Blockx)
        for Blocky in asc_range(iny_a, iny_b):
            # print(Blocky)
            for Blockz in asc_range(inz_a, inz_b):
                # print(Blockz)
                blockart1 = mc.getBlockWithData(Blockx, Blocky, Blockz)
                blockart1 = list(blockart1)
                print(blockart1)
                stone_pos.append([Blockx, Blocky, Blockz, blockart1[0], blockart1[1]])
    # print(stone_pos)
    return stone_pos

def antwort_umwandeln(antwort):
    splitted = antwort.split(",")
    inx_a = int(splitted[0])
    iny_a = int(splitted[1])
    inz_a = int(splitted[2])
    inx_b = int(splitted[3])
    iny_b = int(splitted[4])
    inz_b = int(splitted[5])
    return inx_a, inx_b, iny_a, iny_b, inz_a, inz_b

def scannen():
    antwort = input("Bitte geben Sie die äußeren Koordinaten Ihres Kunstwerkes an.")
    # print(type(antwort))
    if is_int(antwort) :
        inx_a, inx_b, iny_a, iny_b, inz_a, inz_b = antwort_umwandeln(antwort)
    # print("Antwort umgewandelt.")
        stone_pos = abtasten(inx_a, inx_b, iny_a, iny_b, inz_a, inz_b)
    # print("Abgetastet.")
        stone_rel_pos = rel_pos(stone_pos)
    # print("relpos ermittelt.")
        save_project(stone_rel_pos)
        print("Scannen war erfolgreich. Was Sie da gebaut haben ist aber echt beachtlich!")
        time.sleep(2)
    else :
        print("Das waren keine Koordinaten! Sie müssen nochmal von Vorn beginnen.")
        time.sleep(3)

def bauen(projektname):
    with open(projektname + ".txt", "r") as f:
        stone_rel_pos = []
        idCount = 0
        datenwertCount = 0
        nocoord = False # we suggest, we have coords
        for line in f:
            position = line[:-1].split(",")
            position = [int(x) for x in position]
            stone_rel_pos.append(position)

            # check if all is like we want it to be
            if len(position) < 3:
                print("missing coords for blocks, can't go ahead")
                nocoord = True
                break
            if len(position) < 4: # es könnte theoretisch auch nur die Id verlorengegangen sein, sodass nun der Datenwert als Id eigelesen wird. Ist dann halt so...
                position.append(152)
                idCount += 1
            if len(position) < 5:
                position.append(0)
                datenwertCount += 1

    # no coords means no building
    if nocoord:
        return
    print("Vermisse BlockIds bei {} Blöcken. I set this block's id to 152 (RedstoneBlock). You can later change the ids of all redstoneBlocks to whatever you want.".format(idCount))
    print("Vermisse Datenwert bei {} Blöcken. ersetze ihn durch null.".format(datenwertCount))

    print("Ihr Bauwerk besteht aus folenden Steinarten: " + str(steinarten(stone_rel_pos)))
    antwortc = input("Sollten Sie bestimmte Steine ersetzen wollen geben Sie bitte erst den zu Ersetzenden und dann den gewünschten Steinindex Kommasepariert ein. Drücken Sie andernfalls einfach ein'n'.")
    ask_for_change(stone_rel_pos, antwortc, 3, 3)

    antwortd = input("Sollten Sie den Datenwert eines bestimmten Steins verändern wollen geben Sie bitte den Stein und den gewünschten Datenwert an. Drücken Sie anderenfalls einfach ein 'n'.")
    ask_for_change(stone_rel_pos, antwortd, 3, 4)

    Steinabstand = stone_rel_pos[-1]
    # print(type(position))
    # print(stone_rel_pos)
    print("Ihr Bauwerk hat eine länge von " + str(Steinabstand[0] + 1) + " Steinen, eine Höhe von " + str(Steinabstand[1] + 1) + " Steinen und eine Breite von " + str(Steinabstand[2] + 1) + " Steinen.")
    input("Positionieren Sie sich bitte so, dass Ihr künstlerisches Meisterwerk vor Ihnen gebaut werden kann. Und drücken Sie Enter, um Ihr Bauwerk entstehen zu lassen.")
    x, y, z = mc.player.getPos()
    mc.saveCheckpoint()

    # main building tqdm is for the progress bar
    for posi in tqdm(stone_rel_pos, desc="Building...", ascii=False):
        mc.setBlock(x + posi[0], y + posi[1], z + posi[2], posi[3], posi[4])
        time.sleep(0.001)

    antwortb1 = input("Theoretisch dürften Sie das Duplikat Ihres Werkes nun vor sich sehen. sollte es Ihnen nicht gefallen und Sie möchten es wieder löschen drüscken Sie 'l' anderenfalls einfach nur Enter.")
    if antwortb1 == "l":
        mc.restoreCheckpoint()
        print("Das hätten wir beginnen Sie einfach von Vorn.\n")
    else:
        print("Viel Spaß damit!\n")

try:
    while True:
        projektname = input("Geben Sie einen Projektnamen ein.")
        if os.path.isfile(projektname + ".txt"):
            antwort1 = input("Ah. Sie schon wieder. Wollen Sie Ihr Kunstwerk irgendwohin bauen, oder ein neues einscannen? Geben sie 'b' für bauen und 's' für einscannen ein.")
            if antwort1 == "b":
                bauen(projektname)
            elif antwort1 == "s":
                scannen()
            else:
                print("Es tut mir leid, aber das war nicht meine Frage.")
                time.sleep(3)
        else:
            print("Anscheinend gibt es dieses Projekt noch nicht.")
            scannen()
        antwort5 = input("Wollen Sie das Projekt '" + projektname + "' behalten oder löschen? Drücken Sie 'b' für behalten und 'l' für löschen.")
        if antwort5 == "l":
            os.remove(projektname + ".txt")
            print("Ihr Projekt wurde gelöscht!\n")
        elif antwort5 == "b":
            print("Ihr Projekt wurde gespeichert unter " + os.path.realpath(projektname + ".txt") + ".\n")
        else:
            print("Das hatte ich nicht gefragt. Naja egal Ihr projekt hab ich jetzt einfach unter" + os.path.realpath(projektname + ".txt") + " gespeichert.\n")
except KeyboardInterrupt:
    print("\nAuf Wiedersehen!")

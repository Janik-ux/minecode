from mcpi.minecraft import Minecraft
import time
import os
mc = Minecraft.create()
x, y, z = mc.player.getPos()
v = 1

def asc_range(a, b) :
    if a > b :
        return range(b, a+1)
    else :
        return range(a, b+1)

def save_project(stone_rel_pos) :
    with open(projektname + ".txt", "w") as f :
        for item in stone_rel_pos :
            row = ','.join(str(x) for x in item)
            f.write("%s\n" % row)
def rel_pos(stone_pos) :
    stone_rel_pos = []
    erster_stein = stone_pos[0]
    #print(erster_stein)
    for stein in stone_pos :
        x = erster_stein[0] - stein[0]
        y = erster_stein[1] - stein[1]
        z = erster_stein[2] - stein[2]
        c = [x, y, z, stein[3]]
        stone_rel_pos.append([abs(n) for n in c])
    # print(stone_rel_pos)
    return stone_rel_pos

def abtasten(inx_a, inx_b, iny_a, iny_b, inz_a, inz_b) :
    stone_pos = []
    #print(inx_a, inx_b, iny_a, iny_b, inz_a, inz_b)
    for Blockx in asc_range(inx_a, inx_b) :
        #print(Blockx)
        for Blocky in asc_range(iny_a, iny_b) :
            #print(Blocky)
            for Blockz in asc_range(inz_a, inz_b) :
                #print(Blockz)
                blockart = mc.getBlock(Blockx, Blocky, Blockz)
                stone_pos.append([Blockx, Blocky, Blockz, blockart])
    return stone_pos

def antwort_umwandeln(antwort) :
    splitted = antwort.split(",")
    inx_a = int(splitted[0])
    iny_a = int(splitted[1])
    inz_a = int(splitted[2])
    inx_b = int(splitted[3])
    iny_b = int(splitted[4])
    inz_b = int(splitted[5])
    return inx_a, inx_b, iny_a, iny_b, inz_a, inz_b

def scannen() :
    antwort = input("Bitte geben Sie die äußeren Koordinaten Ihres Kunstwerkes an.")
    # if not isinstance(antwort, str) :
    # print(type(antwort))
    inx_a, inx_b, iny_a, iny_b, inz_a, inz_b = antwort_umwandeln(antwort)
    stone_pos = abtasten(inx_a, inx_b, iny_a, iny_b, inz_a, inz_b)
    stone_rel_pos = rel_pos(stone_pos)
    save_project(stone_rel_pos)
    print("Scannen war erfolgreich. Was Sie da gebaut haben ist aber echt beachtlich!")
    time.sleep(2)
    # else :
        # print("Das waren keine Koordinaten! Sie müssen nochmal von Vorn beginnen.")
        # time.sleep(3)

def bauen(projektname) :
    with open(projektname + ".txt", "r") as f :
        stone_rel_pos = []
        for line in f:
            position = line[:-1].split(",")
            position = [ int(x) for x in position ]
            stone_rel_pos.append(position)
        Steinabstand = stone_rel_pos[-1]
        # print(type(position))
        # print(stone_rel_pos)
        print("Ihr Bauwerk hat eine länge von " + str(Steinabstand[0] + 1) + " Steinen, eine Höhe von " + str(Steinabstand[1] + 1) + " Steinen und eine Breite von " + str(Steinabstand[2] + 1) + " Steinen.")
        antwortb = input("Positionieren Sie sich bitte so, dass Ihr künstlerisches Meisterwerk vor Ihnen gebaut werden kann. Und drücken Sie Enter, um Ihr Bauwerk entstehen zu lassen.")
        x, y, z = mc.player.getPos()
        mc.saveCheckpoint()
        for posi in stone_rel_pos :
            print(posi)
            mc.setBlock(x + posi[0], y + posi[1], z + posi[2], posi[3])
        antwortb1 = input("Theoretisch dürften Sie das Duplikat Ihres Werkes nun vor sich sehen. sollte es Ihnen nicht gefallen und Sie möchten es wieder löschen drüscken Sie 'l' anderenfalls einfach nur Enter.")
        if antwortb1 == "l" :
            mc.restoreCheckpoint()
            print("Das hätten wir beginnen Sie einfach von Vorn.")
        else :
            print("Viel Spaß damit!")
        time.sleep(2)



while True :
    projektname = input("Geben Sie einen Projektnamen ein.")
    if os.path.isfile(projektname + ".txt") :
        antwort1 = input("Ah. Sie schon wieder. Wollen Sie Ihr Kunstwerk irgendwohin bauen, oder ein neues einscannen? Geben sie 'b' für bauen und 's' für einscannen ein.")
        if antwort1 == "b" :
            bauen(projektname)
        elif antwort1 == "s" :
            scannen()
        else :
            print("Es tut mir leid, aber das war nicht meine Frage.")
            time.sleep(3)
    else :
        print("Anscheinend gibt es dieses Projekt noch nicht.")
        scannen()
    antwort5 = input("Wollen Sie das Projekt '" + projektname + "' behalten oder löschen? Drücken Sie 'b' für behalten und 'l' für löschen.")
    if antwort5 == "l" :
        os.remove(projektname + ".txt")
        print("Ihr Projekt wurde gelöscht!")
        time.sleep(2)
    elif antwort5 == "b" :
        print("Ihr Projekt wurde gespeichert unter " + os.path.realpath(projektname + ".txt") + ".")
        time.sleep(2)
    else :
        print("Das hatte ich nicht gefragt. Naja egal Ihr projekt hab ich jetzt einfach unter" + os.path.realpath(projektname + ".txt") + " gespeichert.")
        time.sleep(2)
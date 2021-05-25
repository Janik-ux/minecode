stone_rel_pos = []

erster_stein = stone_pos[0]
print(erster_stein)

for stein in stone_pos :
  x = erster_stein[1] - stein[1]
  y = erster_stein[2] - stein[2]
  z = erster_stein[3] - stein[3]
  stone_rel_pos.append(str(stein), str(x), str(y), str(z))
print(stone_rel_pos)
import random

goblin1 = "Ярик"
g1_hp = random.randint(60, 100)
g1_hp_max = g1_hp
g1_ap = random.randint(10, 20)

goblin2 = "Славик"
g2_hp = random.randint(60, 100)
g2_hp_max = g2_hp
g2_ap = random.randint(10, 20)

round = 1

while g1_hp > 0 and g2_hp > 0:
    print("Раунд", round)
    n = random.randint(0,1)
    luck = random.randint(1,20)

    if luck == 20:
        g1_hp = g1_hp_max
        g2_hp = g2_hp_max
        if g2_hp < g2_hp_max and g1_hp < g2_hp_max:
            print("Все гоблины востанавливают здоровье")
        elif g1_hp < g1_hp_max:
            print(goblin1, "востанавливает здоровье")
        elif g2_hp < g2_hp_max:
            print(goblin2, "востанавливает здоровье")

    if n == 0:
        dice = random.randint(1, 6)
        g2_hp = g2_hp - g1_ap - dice
        print(goblin1, " атакует ", goblin2, "а с силой ", g1_ap + dice, sep = "")
        if g2_hp < 0 :
            g2_hp = 0
        print("У ", goblin2, "а осталось ", g2_hp, " очков здоровья", sep = "")
    else:
        dice = random.randint(1, 6)
        g1_hp = g1_hp - g2_ap - dice
        print(goblin2, " атакует ", goblin1, "а с силой ", g2_ap + dice, sep = "")
        if g1_hp < 0 :
            g1_hp = 0
        print("У ", goblin1, "а осталось ", g1_hp, " очков здоровья", sep = "")

    print()
    round += 1

if g1_hp > 0:
    print(goblin1, 'спит')
    print(goblin2, 'сторожит')
else:
    print(goblin2, 'спит')
    print(goblin1, 'сторожит')

print("Игра окончена")

input('Press ENTER to exit')
import random
#creater empty player_list for list of characters
player_list = []
#empty dictionary for character name and their stats
players = {}
#enemy_list
enemy_list = []
#enemy dictionary
enemies = {}

#this for loop allows the naming of characters and random stat selection
for i in range(0,2):
    name = input("Ally name > ")
    stat_dictionary = {}
    stat_dictionary['HP'] = random.randint(35,75)
    stat_dictionary["ATK"] = random.randint(10,30)
    stat_dictionary["DEF"] = random.randint(10,30)
    stat_dictionary["SPD"] = random.randint(1,20)
    stat_dictionary["LCK"] = random.randint(1,11)
    players[name] = stat_dictionary
    player_list.insert(i,name)

print(players)

for i in range(0,2):
    name = input("Enemy name > ")
    enemy_stat_dictionary = {}
    enemy_stat_dictionary['HP'] = random.randint(35,75)
    enemy_stat_dictionary["ATK"] = random.randint(10,30)
    enemy_stat_dictionary["DEF"] = random.randint(10,30)
    enemy_stat_dictionary["SPD"] = random.randint(1,20)
    enemy_stat_dictionary["LCK"] = random.randint(1,11)
    enemies[name] = enemy_stat_dictionary
    enemy_list.insert(i,name)
print(enemies)
'''
Work in progress, trying to create classes with preselected moves.
'''

class Ally:
    def __init__(self, name, HP, ATK, DEF, SPD, LCK):
        self.name = names
        self.move = []

    def add_move(self, move):
        self.move.append(move)


    for i in range(0,2):
        name = input("Ally name > ")
        stat_dictionary = {}
        stat_dictionary['HP'] = random.randint(35,75)
        stat_dictionary["ATK"] = random.randint(10,30)
        stat_dictionary["DEF"] = random.randint(10,30)
        stat_dictionary["SPD"] = random.randint(1,20)
        stat_dictionary["LCK"] = random.randint(1,11)
        players[name] = stat_dictionary
        player_list.insert(i,name)

    print(players)


for i in range(0,2):
    name = input("Ally name > ")
    stat_dictionary = {}
    stat_dictionary['HP'] = random.randint(35,75)
    stat_dictionary["ATK"] = random.randint(10,30)
    stat_dictionary["DEF"] = random.randint(10,30)
    stat_dictionary["SPD"] = random.randint(1,20)
    stat_dictionary["LCK"] = random.randint(1,11)
    players[name] = stat_dictionary
    player_list.insert(i,name)

print(players)

for i in range(0,2):
    name = input("Enemy name > ")
    enemy_stat_dictionary = {}
    enemy_stat_dictionary['HP'] = random.randint(35,75)
    enemy_stat_dictionary["ATK"] = random.randint(10,30)
    enemy_stat_dictionary["DEF"] = random.randint(10,30)
    enemy_stat_dictionary["SPD"] = random.randint(1,20)
    enemy_stat_dictionary["LCK"] = random.randint(1,11)
    enemies[name] = enemy_stat_dictionary
    enemy_list.insert(i,name)
print(enemies)


'''
so the above portion is one way to get stats

the code below focuses on classes,
I need to work on combining both ideas

'''

class Ally:
    def __init__(self, name, hp, atk, dfn, spd, lck):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.spd = spd
        self.lck = lck

    def show_stats(self):
        print ('{}\n\
Health:{}\n\
Attack:{}\n\
Defense:{}\n\
Speed:{}\n\
Luck:{}'.format(self.name, self.hp, self.atk, self.dfn, self.spd, self.lck))

Ally_1 = Ally('Santa', 9, 7, 9, 6, 3)

Ally_1.show_stats()

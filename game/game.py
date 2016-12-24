from Ally import Ally
from Foe import Foe
from Move import Move
import random as r


def gen_stats(person):
    '''
    INPUT: takes person objects stat attributes which equal 0
    USAGE: to randomly generate stats within limits
    OUTPUT: none
    '''

    person.hp = r.randint(14, 18)
    person.atk = r.randint(9, 11)
    person.dfn = r.randint(9, 12)
    person.spd = r.randint(5, 10)
    person.lck = r.randint(1, 5)
    stat_total = stat_sum(person)
    if stat_total != 45:
        gen_stats(person)
    else:
        return


def stat_sum(person):
    '''
    INPUT: takes the person object and adds up all the stat attributes
    USAGE: to find the stat sum in order to balance out the stat distribution
    OUTPUT: none, just returns stat_total
    '''

    stat_total = (person.hp + person.atk + person.dfn + person.spd + person.lck)
    return stat_total


def print_stats(person):
    '''
    INPUT: person objects and its attributes
    USAGE: to print out the objects name and attributes
    OUTPUT: prints out name and stats
    '''

    print('\nName: {}\n\
Level: {}\n\
Health: {}\n\
Attack: {}\n\
Defense: {}\n\
Speed: {}\n\
Luck: {}\n'.format(person.name, person.level, person.hp, person.atk, person.dfn, person.spd, person.lck))


def attack(attacker, attackee):
    '''
    INPUT: takes in two objects as arguments
    USAGE: to basically take hp away from another player
    OUTPUT: none
    '''

    move_no = 0

    for i in attacker.moves[0]:
        print('{} {}\n'.format(move_no, i))
        move_no += 1

    move_choice = int(input('Which move would you like to use?> '))

    use_move(attacker, attackee, attacker.moves[0][move_choice])


def use_move(attacker, attackee, move):
    '''
    INPUT: takes in two objects and a move object
    USAGE: this function uses the move object and it affects the objects meant to be affected by the move object
    OUTPUT: the after effects of the move utilized and a miss statement if the move objects fails (on purpose)
    '''

    if move.power == '--':
        print('not an attacking move')

    else:

        chances = 100 - (move.accuracy * 100)

        if r.randint(1, 100) < chances:
            print('Missed!')

        else:
            modifier = 1
            damage = (((2 * attacker.level + 10) / 250) * (attacker.atk / attackee.dfn) * move.power + 2) * modifier
            damage = round(damage, 0)
            attackee.hp -= damage
            if attackee.hp < 0:
                attackee.hp = 0


def print_move_stats(move):
    '''
    INPUT: move object
    USAGE: to print the move object dict in a nutshell except formatted for user friendly display
    OUTPUT: move objects attributes in a user friendly manner
    '''

    print('{}\nPower: {}\nAccuracy: {}\nCritical Rate: {}'.format(move.name,
    move.power, (str(round(move.accuracy * 100))) + '%' , str(round(move.critrate * 100)) +'%'))


def battle_sequence(person1, person2):
    '''
    INPUT: two player objects
    USAGE: to navigate through a battle sequence between the two player objects
    OUTPUT: whatever is necessary within the sequence
    '''

    pass


def

def main():
    '''
    INPUT: none
    USAGE: runs the game
    OUTPUT: whatever the game dictates
    '''
    user = input('What is your name? > ')
    player1 = Ally(user)
    gen_stats(player1)
    print_stats(player1)

    foe1 = Foe('Felix')
    gen_stats(foe1)
    print_stats(foe1)

    move01 = Move('Tackle', 35, .95, .05)
    move02 = Move('Slash', 40, .90, .05)
    # TODO work on non attack move
    move03 = Move('Taunt', '--', .95, '--')

    separate_move_list = [move01, move02, move03]
    player1.moves.append(separate_move_list)

    print('\nEntering Battle Mode')

    while foe1.hp > 0:
        print('(a)ttack, (d)efend, (i)tem, (r)un')
        choice_input = input(' > ')

        if choice_input == 'a':
            attack(player1, foe1)
            print_stats(player1)
            print_stats(foe1)

        elif choice_input == 'd':
            print('Defend feature soon')

        elif choice_input == 'i':
            print('item feature soon')

        elif choice_input == 'r':
            print('No running away yet')

        attack(foe1, player1)



    print('{} has been knocked out'.format(foe1.name))
    print_stats(foe1)





main()
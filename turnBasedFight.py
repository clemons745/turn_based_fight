#! /usr/bin/python3

#####
#
# Name: turnBasedFight.py
#
# Description: A turn based pokemon style game
#
# Version: 0.1dev
#
# Date: 4/20/2018
#
# Author: Tony Clemons (clemons745@gmail.com)
#
#####

import random
import sys


def getComputerMove(health):
    chance = random.randint(1, 100)

    if health == 100:
        if chance >= 50:
            return 1
        else:
            return 2
    elif health <= 35:
        if chance <= 50:
            return 3
        elif chance > 50 and chance <= 75:
            return 1
        else:
            return 2
    elif health > 35 and health < 100:
        if chance <= 33:
            return 1
        elif chance > 33 and chance <= 66:
            return 2
        else:
            return 3
    else:
        raise Exception('Error occured in getComputerMove')


def useMove(health, move):
    if move == 1:
        newHealth = health - random.randint(18, 25)
    elif move == 2:
        newHealth = health - random.randint(10, 35)
    elif move == 3:
        newHealth = health + random.randint(18, 25)
    else:
        raise Exception('Error occured processing useMove.')

    if newHealth <= 0:
        # Can't have negative health, so return 0 if health is < 0
        return 0
    elif newHealth > 100:
        # Can't have more than 100 health, return 100 if health > 100
        return 100
    else:
        return newHealth


def main():
    # Set Health
    userHealth = 100
    computerHealth = 100
    turn = 0

    # Print current health and options
    while True:
        turn += 1
        print('\nYour Health: %s' % userHealth)
        print('Computer Health: %s' % computerHealth)
        print('''\nWhich move would you like to use?
1 Slash (18-25 damage)
2 Uppercut (10-35 damage)
3 Heal (heals you 18-25 health)
4 Quit

Selection: ''', end='')
        # Collect selection from user and ensure it is valid
        while True:
            try:
                userMove = int(input())
            except ValueError:
                print('\nInvalid. Please enter Selection: ', end='')
                continue
            if userMove < 1 or userMove > 4:
                print('\nInvalid. Please enter Selection: ', end='')
                continue
            elif userMove >= 1 and userMove <= 3:
                break
            elif userMove == 4:
                sys.exit()
            else:
                raise Exception('Error occured processing selection.')

        if userMove == 3:
            # If user wants to heal, pass the users health
            # to useMove instead of the computer
            userHealth = useMove(userHealth, userMove)
        else:
            # Pass the computer health to useMove
            computerHealth = useMove(computerHealth, userMove)

        # If computerHealth is 0, the user has won, so break form the loop
        if computerHealth == 0:
            break

        # Computers Turn
        computerMove = getComputerMove(computerHealth)

        if computerMove == 3:
            # If computer wants to heal, pass the computers health
            # to useMove instead of the user
            computerHealth = useMove(computerHealth, computerMove)
        else:
            # Pass the user health to useMove
            userHealth = useMove(userHealth, computerMove)

        if userHealth == 0:
            break

        if computerMove == 1:
            print('\nComputer used Slash!')
        elif computerMove == 2:
            print('\nComputer used Uppercut!')
        elif computerMove == 3:
            print('\nComputer healed!')
        else:
            raise Exception('An error occured printing computer action.')

    print('\nYour Health: %s' % userHealth)
    print('Computer Health: %s' % computerHealth)
    if computerHealth == 0:
        print('\nYou win! Game lasted %s turns.' % turn)
    elif userHealth == 0:
        print('\nYou lose! Game lasted %s turns.' % turn)
    else:
        raise Exception('Error occured printing result')


if __name__ == '__main__':
    main()

#! /usr/bin/python

__author__ = 'sebassdc'

import sys, os

# Clears() helps to easy clean screan in various platforms.
def clears():
    plat = sys.platform
    if plat.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

# Calculate how many xp points has been obtained given de levels
def obtained(level):
    if level <= 16:
        return 17 * level
    elif level <= 30:
        return 1.5*level**2 - 29.5*level + 360
    else:
        return 3.5 * level ** 2 - 151.5 * level + 2220

# Calculate how many xp points you need to increase yout level
def needed(level):
    if level <= 16:
        return 17
    elif level < 30:
        return (3 * level) - 28
    else:
        return (7 * level) - 148

# Makes a diagnostic
def diagnostico(level):
    print "You have %d exp points and need %d points to the next level.\n\n" % (obtained(level), needed(level))


# print a few common errors
def error(s):
    if s == "numargs":
        print "Incorrect number of arguments\n\n"
        help()
    elif s == "nomenu":
        print "Incorrect number option\n\n"
    elif s == "wrong_option":
        print "Unknowed option\n\n"
        help()


# App help
def help():
    helper_list = "minexp use: \n minexp [option] [level]\n Options:\n [-o: obtained, -n: How many i need?, -d: diagnosis, -h: help]\n\n"
    print helper_list


# MAKING A FRIENDLY CLI

# This interafce shows a little menu
def interfaz1():
    menu1 = "What do you wany?\n1. Check obtained experience\n2. How many i need for the next level?\n3. Run a diagnosis? \n4. Quit\n"
    while True:
        option = input(menu1)
        if int(option) > 4:
            clears()
            error("nomenu")
            continue
        if option == 4:
            sys.exit()
        level = int(input('Your xp level: '))
        if option == 1:
            clears()
            print "Until now you have %d xp points\n\n" % obtained(level)

            continue
        elif option == 2:
            clears()
            print "%d of experience you need to level up\n\n" % needed(level)
            continue
        elif option == 3:
            clears()
            diagnostico(level)
        else:
            error("nomenu")


# This run a diagnosis by default
# Either shows the help
def interfaz2():
    level = sys.argv[1]
    if level == '-h' or level == 'help':
        help()
    else:
        diagnostico(int(level))


# Given the option this interface shows specifically what do you want
def interfaz3():
    level = int(sys.argv[2])
    option = sys.argv[1]
    if option == '-o':
        print "Until now you have %d xp points\n\n" % obtained(level)
    elif option == '-n':
        print "%d of experience you need to level up" % needed(level)
    elif option == '-d':
        diagnostico(int(level))
    else:
        error("wrong_option")


if __name__ == "__main__":

    longi = len(sys.argv) # checking how many args we hnndle
    if longi == 1:
        interfaz1()
    elif longi == 2:
        interfaz2()
    elif longi == 3:
        interfaz3()
    else:
        error("numargs")

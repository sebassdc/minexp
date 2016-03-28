#! /usr/bin/python

__author__ = 'sebassdc'

import sys, os


def clears():
    plat = sys.platform
    if plat.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def obtained(level):
    if level <= 16:
        return 17 * level
    elif level <= 30:
        return 1.5*level**2 - 29.5*level + 360
    else:
        return 3.5 * level ** 2 - 151.5 * level + 2220


def needed(level):
    if level <= 16:
        return 17
    elif level < 30:
        return (3 * level) - 28
    else:
        return (7 * level) - 148


def diagnostico(level):
    print "Tienes %d puntos exp y necesitas %d puntos para el siguiente nivel.\n\n" % (obtained(level), needed(level))

def error(s):
    if s == "numargs":
        print "Incorrect number of arguments\n\n"
        help()
    elif s == "nomenu":
        print "Incorrect number option\n\n"
    elif s == "wrong_option":
        print "Unknowed option\n\n"
        help()

def help():
    helper_list = "minexp use: \n minexp [option] [level]\n Options:\n [-o: obtained, -n: How many i need?, -d: diagnosis, -h: help]\n\n"
    print helper_list


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


def interfaz2():
    level = sys.argv[1]
    if level == '-h' or level == 'help':
        help()
    else:
        diagnostico(int(level))

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
    longi = len(sys.argv)
    if longi == 1:
        interfaz1()
    elif longi == 2:
        interfaz2()
    elif longi == 3:
        interfaz3()
    else:
        error("numargs")
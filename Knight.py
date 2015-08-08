#!/usr/bin/env python
# -*- coding: utf-8 -*-


def setTable():
    """genera tablero de ajedrez, con valor del 1 a 64, de longitud 8x8"""
    init = 1
    end = 9
    table = []
    for i in range(init, end):
        table.append(range(init, end))
        init = end
        end += 8
    return table


def setIndex(index):
    """ verifica si el caballo puede mover mas alla de su posicion"""
    if index + 2 >= 8:
        return (index - 2, index + 1)
    if index - 2 >= 0:
        return (index - 2, index + 3)
    if index - 2 <= 0:
        return (index, index + 3)


def setRadius(pos):
    """genera el radio de movimiento del caballo"""
    table = setTable()
    assert pos in range(1, 65)
    for i in range(0, 8):
        if pos in table[i]:
            length = i
            index = table[i].index(pos)
            break
        else:
            continue

    indexRow = setIndex(index)
    lengthRow = setIndex(length)
    radius = []
    for i in range(lengthRow[0], lengthRow[1]):
        radius.append(table[i][indexRow[0]:indexRow[1]])

    return radius
    
def totalMov(radio):
	"""calculo la cantidad de movimiento que puede hacer en su radio"""
	width = len(radio)
	hight = len(radio[0])
	lenKinght = 3
	total = (width*hight+lenKinght) / lenKinght
	return total

def main():
    """ generamos el radio de movimiento del caballo segun la ubicacion en el tablero"""
    result = []
    for pos in range(1, 65):
        result.append(setRadius(pos))
    for i in range(0, 64):
        print "======== {0} ========".format(i + 1)
        for x in result[i]:
            print x


if __name__ == '__main__':
    main()

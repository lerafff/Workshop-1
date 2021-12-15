from typing import List


def read_input():
    map = [[0 for i in range(10)] for j in range(10)]
    # 0 - empty tile, 1 - attacked empty tile, 2 - ship tile, 3 - attacked ship tile

    four_sized = 1
    three_sized = 2
    two_sized = 3
    one_sized = 4

    read_ships(map, 4, four_sized)
    read_ships(map, 3, three_sized)
    read_ships(map, 2, two_sized)
    read_ships(map, 1, one_sized)

    return map


def read_ships(map, size: int, count: int):
    # reading input for <count> <size>-sized ships
    for _ in range(count):
        i, j = None
        while map[i][j] != 0:
            print("please write a non occupied tile coords")
            i, j = None

        for i in range(i, i+size):
            map[i][j] = 2


def ships_destroyed(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 2:
                return False
    return True


print("Input for player 1")
map_p1 = read_input()
map_p2 = read_input()

while 1:
    
=======
"""
Battlehip game
"""

def print_field(field):
    for i in  field:
        for j in range(len(i)):
            print (i[j], end= '    ')
        print()


def shoot(field):
    row=int(input('Row: '))
    column=int(input('Column: '))
    try: 
        place=field[row][column]
        return (row, column)
    except: 
        print('Некоректні координати')
        shoot(field)


def init():
    field = [['.'] * field_sz for _ in range(field_sz)]
    return field


def init_ships(num, sizes):
    """
    Create the list of ships.
    """

    ships = []

    for sz_ship in sizes:
        for _ in range(num):
            ships.append(sz_ship)

    return ships


def check_coord(row, col, battle_field):
    """
    Satus codes:
        0 - the cell killed
        1 - the cell is taken
        2 - the cell is empty (missing shot)
    """

    if battle_field[row][col] == '.':
        return 2
    if battle_field[row][col] == 'X':
        return 1

    return 0


def set_ship(row, col, ship_sz, battle_field):
    for i in range(row, row + battle_field + 1):
        battle_field[i][col] = 'O'


def set_ships_field(field, ships):
    for ship in ships:
        print("Size of ship: " + str(ship) + "\nEnter your coordinate")
        coord = shoot()

        set_ship(coord[0], coord[1], ship, field)
        print_field(field)


def main():
    """
    Operations with user.
    """

    battle_field_1 = init(10)
    ships_1 = init_ships(3, [1, 2, 3])

    set_ships_field(battle_field_1, ships_1)

    battle_field_2 = inti(10)
    ships_2 = init_ships(3, [1, 2, 3])

    set_ships_field(battle_field_2, ships_2)


if __name__ == "__main__":
    main()


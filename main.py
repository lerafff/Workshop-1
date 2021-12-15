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
        i, j = input_read()
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

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
        i, j = -1, -1
        while map[i][j] != 0:
            print("please write a non occupied tile coords")
            i, j = -1, -1  # read input with other func

        for i in range(i, i+size):
            map[i][j] = 2


print("Input for player 1")
map_p1 = read_input()
map_p2 = read_input()


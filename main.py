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


def input_read():
    while True:
        print('Введіть координату клітинки:')
        point = input()
        if point == 'exit':
            print('Дякую за гру!')
            exit()
        elif point[1:] == '10' and len(point) == 3 and point[0].isalpha:
            return (ord(point[0]) - 97, int(point[1:]) - 1)
        elif len(point) != 2 or not point[0].isalpha or not point[1].isnumeric:
            print('Некоректна координата!')
        elif point[0] not in 'abcdefghij' or int(point[1]) not in range(1, 11):
            print('Координата виходить за межі поля')
        else:
            break
    return (ord(point[0]) - 97, int(point[1]) - 1)


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


def game():
    print('Хід першого гравця:')
    map1 = read_input()
    print('Хід другого гравця:')
    map2 = read_input()
    while not ships_destroyed(map1) and not ships_destroyed(map2):
        print('Хід першого гравця:')
        print(shots_map2)
        shot = input_read()
        print(shots_map1)
        print('Хід другого гравця:')
        shot = input_read()


def printMap(map: List[List[int]]):
    print("    A B C D E F G H I J")
    row_number = 1
    for row in map:
        if row_number == 10:
            mid = "■".join(row) + "■ "
            print(f"{row_number}|{mid}|")
        else:
            mid = "■".join(row) + "■ "
            print(f"{row_number} |{mid}|")
        row_number = row_number + 1

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
        elif point[0] not in 'abcdefghij' or int(point[1]) not in range(1,11):
            print('Координата виходить за межі поля')
        else:
            break
    return (ord(point[0]) - 97, int(point[1]) - 1)


def ships_destroyed(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 2:
                return False
    return True


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



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


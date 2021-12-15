def input_read():
    while True:
        print('Введіть координату клітинки:')
        point = input()
        if len(point) != 2 or not point[0].isalpha or not point[1].isnumeric:
            print('Некоректна координата!')
        elif point[0] not in 'abcdefghij' or point[1] not in range(1,11):
            print('Координата виходить за межі поля')
        else:
            break
    return (ord(point[0]) - 97, point[1] - 1)

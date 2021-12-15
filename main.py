from typing import List


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
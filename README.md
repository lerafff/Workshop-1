# Workshop-1

Програма є реалізацією Battleship game. Гравець бачить чисте поле спочатку, а тоді хід за ходом 
ставить фігури(кораблики) і бачить позначені якимось знаком комірки, куди він вже стріляв


|Function         |Description                                                    |
|:----------------|:-------------------------------------------------------------:|              
|read_input()	    |	reads figures diffent sizes									                  |
|coord_read()     | reads coordinates and defines it it is right				          |
|read_ships()     | defines which size is the ship								                |
|printMap()       | prints map with frame of coordinates						              |
|game()           | main function which calls all needed functions				        |

Кораблі ставляться на поле за координатами з dataframe 
Гра триває доти, поки хтось один не програє або якийсь гравець не вийде з гри(є функція exit, яка дозволяє гравцю покинути гру у будь-який час
Всі функції викликаються в main функції (game) і послідовно гравець вводить всі необхідні дані

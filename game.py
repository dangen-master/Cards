from random import shuffle
from time import sleep

game_map, game_map_2 = [], []
spisok_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
List_of_completed_moves = []


def new_game():
    global game_map, game_map_2
    a = [i for i in range(1, 36) for _ in range(2)]
    print(a)
    shuffle(a)
    game_map = [a[i: i + 7] for i in range(0, 70, 7)]
    game_map_2 = [['#' for _ in range(7)] for __ in range(10)]
    print(' ' * 4, *list([c for c in range(1, 8)]), sep='\t')
    print(' ' * 3, '-' * 30)
    for i in range(1, len(game_map) + 1):
        print(i, '|', *game_map[i - 1], sep='\t')
    print()


def print_game_map():
    global game_map, game_map_2
    print(' ' * 4, *list([c for c in range(1, 8)]), sep='\t')
    print(' ' * 3, '-' * 30)
    for i in range(1, len(game_map_2) + 1):
        print(i, '|', *game_map_2[i - 1], sep='\t')
    print()


def input_data():
    global game_map, game_map_2, List_of_completed_moves
    data_entry = input("Карта 1:  ").split()
    while True:
        while True:  # проверка корректности ввода
            if len(data_entry) != 2:
                data_entry = input("Неверный ход:  ").split()
                continue
            if data_entry[0] not in spisok_input and \
                    data_entry[1] not in spisok_input[:8]:
                data_entry = input("Неверный ход:  ").split()
                continue
            break
        data_entry_2 = input("Карта 2:  ").split()
        while True:  # проверка корректности ввода
            if len(data_entry_2) != 2:
                data_entry_2 = input("Неверный ввод:  ").split()
                continue
            if data_entry_2[0] not in spisok_input and \
                    data_entry_2[1] not in spisok_input[:8]:
                data_entry_2 = input("Неверный ввод:  ").split()
                continue
            if data_entry == data_entry_2:
                data_entry_2 = input("Неверный ввод:  ").split()
                continue
            if ((int(data_entry[0]) - 1, int(data_entry[1]) - 1),
                (int(data_entry_2[0]) - 1, int(data_entry_2[1]) - 1)) in List_of_completed_moves:
                data_entry = input("Карта 1 :  ").split()
                data_entry_2 = input("Карта 2:  ").split()
                continue
            break
        break

    data_entry = [int(data_entry[0]) - 1, int(data_entry[1]) - 1]
    data_entry_2 = [int(data_entry_2[0]) - 1, int(data_entry_2[1]) - 1]
    open_map(data_entry, data_entry_2)
    sleep(3)
    check(data_entry, data_entry_2)


def open_map(x, y):
    global game_map, game_map_2
    game_map_2[int(x[0])][int(x[1])] = game_map[int(x[0])][int(x[1])]
    game_map_2[int(y[0])][int(y[1])] = game_map[int(y[0])][int(y[1])]
    print(' ' * 4, *list([c for c in range(1, 8)]), sep='\t')
    print(' ' * 3, '-' * 30)
    for i in range(1, len(game_map_2) + 1):
        print(i, '|', *game_map_2[i - 1], sep='\t')
    print()


def check(x, y):
    global game_map, game_map_2, List_of_completed_moves
    if game_map[int(x[0])][int(x[1])] == game_map[int(y[0])][int(y[1])]:
        List_of_completed_moves.append(((x[0], x[1]), (y[0], y[1])))
    else:
        game_map_2[int(y[0])][int(y[1])] = '#'
        game_map_2[int(x[0])][int(x[1])] = '#'


def skan():
    global game_map_2
    count = 0
    for i in range(10):
        for ii in range(7):
            if game_map_2[i][ii] == '#':
                count += 1
    return count


def end_of_the_game():
    print('END')


def clear_desk():
    for i in range(40):
        print()


new_game()
while skan() != 0:
    sleep(3)
    clear_desk()
    print_game_map()
    input_data()
end_of_the_game()

a = "         "
lista = [[a[0], a[1], a[2]],
         [a[3], a[4], a[5]],
         [a[6], a[7], a[8]]]

print("---------")
print("|", lista[0][0], lista[0][1], lista[0][2], "|")
print("|", lista[1][0], lista[1][1], lista[1][2], "|")
print("|", lista[2][0], lista[2][1], lista[2][2], "|")
print("---------")

def move(symbol):
    f = input("Enter the coordinates: ")
    f = f.split()
    if (len(f) == 2 and int(f[0]) and int(f[1])) is False:
        print("You should enter numbers!")
        move(symbol)
    else:
        x = int(f[0])
        y = int(f[1])
        if (0 < x < 4 and 0 < y < 4) is False:
            print("Coordinates should be from 1 to 3!")
            move(symbol)
        elif (lista[x - 1][y - 1] == " " or lista[x - 1][y - 1] == "_") is False:
            print("This cell is occupied! Choose another one!")
            move(symbol)
        else:
            lista[x - 1][y - 1] = symbol
            print("---------")
            print("|", lista[0][0], lista[0][1], lista[0][2], "|")
            print("|", lista[1][0], lista[1][1], lista[1][2], "|")
            print("|", lista[2][0], lista[2][1], lista[2][2], "|")
            print("---------")

turn = 0
while turn <= 9:
    if turn % 2 == 0:
        move("X")
    else:
        move("O")

    if lista[0][0] == lista[0][1] == lista[0][2] == "OOO" or lista[1][0] == lista[1][1] == lista[1][2] == "OOO" or lista[1][0] == lista[1][1] == lista[1][2] == "OOO" or lista[0][0] == lista[1][0] == lista[2][0] == "O" or \
            lista[0][1] == lista[1][1] == lista[2][1] == "O" or lista[0][2] == lista[1][2] == lista[2][2] == "O" or \
            lista[0][0] == lista[1][1] == lista[2][2] == "O" or lista[0][2] == lista[1][1] == lista[2][0] == "O":
        o_wins = True
    else:
        o_wins = False
    if lista[0][0] == lista[0][1] == lista[0][2] == "XXX" or lista[1][0] == lista[1][1] == lista[1][2] == "XXX" or lista[2][0] == lista[2][1] == lista[2][2] == "XXX" or lista[0][0] == lista[1][0] == lista[2][0] == "X" or \
            lista[0][1] == lista[1][1] == lista[2][1] == "X" or lista[0][2] == lista[1][2] == lista[2][2] == "X" or \
            lista[0][0] == lista[1][1] == lista[2][2] == "X" or lista[0][2] == lista[1][1] == lista[2][0] == "X":
        x_wins = True
    else:
        x_wins = False

    number_of_x = 0
    number_of_o = 0
    not_finished = False
    for x in lista:
        for pole in x:
            if pole == "X":
                number_of_x += 1
            elif pole == "O":
                number_of_o += 1
            elif pole == " " or "_":
                not_finished = True

    impossible = False
    if number_of_x >= (number_of_o + 2) or number_of_o >= (number_of_x + 2):
        impossible = True

    #print(x_wins, o_wins, number_of_x, number_of_o, not_finished, impossible)
    if x_wins is False and o_wins is False and not_finished is True and impossible is False:
        #print("Game not finished")
        pass
    elif x_wins is False and o_wins is False and not_finished is False:
        print("Draw")
        break
    elif x_wins is True and o_wins is True or impossible is True:
        #print("Impossible")
        pass
    elif x_wins is True:
        print("X wins")
        break
    elif o_wins is True:
        print("O wins")
        break
    turn += 1
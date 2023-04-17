class NineByNine:
    def __init__(self, userName, userTable):
        self.name = userName
        self.table = userTable
        self.move = 0

    def findEmpty(self, table):
        for row in range(len(table[0])):
            for column in range(len(table[0])):
                if table[row][column] == 0:
                    return (row, column)

        return None

    def checkValidity(self, table, number, position):
        for column in range(len(table[0])):
            if table[position[0]][column] == number and position[1] != column:
                return False

        for row in range(len(table[0])):
            if table[row][position[1]] == number and position[0] != row:
                return False

        box_x = position[1] // 3
        box_y = position[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if table[i][j] == number and (i, j) != position:
                    return False

        return True

    def solveTable(self, table):
        empty = self.findEmpty(table)
        self.move += 1

        if not empty:
            return True
        else:
            row, column = empty

        for number in range(1, 10):
            if self.checkValidity(table, number, (row, column)):
                table[row][column] = number

                if self.solveTable(table):
                    return True

                table[row][column] = 0

        return False

    def printTable(self, table):
        for row in range(len(table)):
            if row % 3 == 0 and row != 0:
                print('- - - - - - - - - - -')

            for column in range(len(table[0])):
                if column % 3 == 0 and column != 0:
                    print('|', end = ' ')

                if column == 8:
                    print(str(table[row][column]))
                else:
                    print(str(table[row][column]) + ' ', end = '')

class FourByFour(NineByNine):
    def findEmpty(self, table):
        for row in range(len(table[0])):
            for column in range(len(table[0])):
                if table[row][column] == 0:
                    return (row, column)

        return None

    def checkValidity(self, table, number, position):
        for column in range(len(table[0])):
            if table[position[0]][column] == number and position[1] != column:
                return False

        for row in range(len(table[0])):
            if table[row][position[1]] == number and position[0] != row:
                return False

        box_x = position[1] // 2
        box_y = position[0] // 2

        for i in range(box_y * 2, box_y * 2 + 2):
            for j in range(box_x * 2, box_x * 2 + 2):
                if table[i][j] == number and (i, j) != position:
                    return False

        return True

    def solveTable(self, table):
        empty = self.findEmpty(table)
        self.move += 1

        if not empty:
            return True
        else:
            row, column = empty

        for number in range(1, 5):
            if self.checkValidity(table, number, (row, column)):
                table[row][column] = number

                if self.solveTable(table):
                    return True

                table[row][column] = 0

        return False

    def printTable(self, table):
        for row in range(len(table)):
            if row % 2 == 0 and row != 0:
                print('- - - - -')

            for column in range(len(table[0])):
                if column % 2 == 0 and column != 0:
                    print('|', end = ' ')

                if column == 3:
                    print(str(table[row][column]))
                else:
                    print(str(table[row][column]) + ' ', end = '')

def runNineByNine():
    games = []

    while True:
        print('\n9x9 SUDOKU SOLVER PROGRAM')
        userName = input('\nGood day! What is your name?: ')

        userReady = input(f'\nHello {userName}, do you want me to help you solve a 9x9 Sudoku problem? (y/n): ')
        if userReady.lower() == 'y':
            while True:
                userTable = []

                for row in range(9):
                    userRows = [int(number) for number in input(f'Enter the numbers (separated with a space) for row {row + 1}: ').split(' ')]
                    userTable.append(userRows)

                newgame = NineByNine(userName, userTable)
                games.append(newgame)

                print(' ')
                newgame.printTable(userTable)
                userTableIsCorrect = input('Is this your table? Is it correct? (y/n): ')

                if userTableIsCorrect.lower() == 'y':
                    break
                else:
                    continue

        else:
            print('Goodbye!')
            break

        print('\nI am now solving... Please wait...')
        print('\nDone!')

        print(f'\nHere is the unsolved table: ')
        newgame.printTable(userTable)

        newgame.solveTable(userTable)
        allTables.append(newgame.table)

        print('\nHere is the solved table: ')
        newgame.printTable(userTable)

        print(f'\nIt took me {newgame.move} moves to solve your sudoku problem.')

        playAgain = input('\nDo you want to solve a new table? (y/n): ')
        if playAgain.lower() != 'y':
            print('\nThank you for trusting me!')

            for gameNumber in range(len(games)):
                print(f"\n{games[gameNumber].name}'s solved sudoku problem: ")
                games[gameNumber].printTable(games[gameNumber].table)
            print(' ')
            break
        else:
            print(' ')
            continue

def runFourByFour():
    games = []

    while True:
        print('\n4x4 SUDOKU SOLVER PROGRAM')
        userName = input('\nGood day! What is your name?: ')

        userReady = input(f'\nHello {userName}, do you want me to help you solve a 4x4 Sudoku problem? (y/n): ')
        if userReady.lower() == 'y':
            while True:
                userTable = []

                for row in range(4):
                    userRows = [int(number) for number in input(f'Enter the numbers (0 for blanks - separated with a space) for row {row + 1}: ').split(' ')]
                    userTable.append(userRows)

                newgame = FourByFour(userName, userTable)
                games.append(newgame)

                print(' ')
                newgame.printTable(userTable)
                userTableIsCorrect = input('Is this your table? Is it correct? (y/n): ')

                if userTableIsCorrect.lower() == 'y':
                    break
                else:
                    continue
        else:
            print('Goodbye!')
            break

        print(f'\nHere is the unsolved table: ')
        newgame.printTable(userTable)

        newgame.solveTable(userTable)
        allTables.append(newgame.table)

        print('\nHere is the solved table: ')
        newgame.printTable(userTable)

        print(f'\nIt took me {newgame.move} moves to solve your sudoku problem.')

        playAgain = input('\nDo you want to solve a new table? (y/n): ')
        if playAgain.lower() != 'y':
            print('\nThank you for trusting me!')

            for gameNumber in range(len(games)):
                print(f"\n{games[gameNumber].name}'s solved sudoku problem: ")
                games[gameNumber].printTable(games[gameNumber].table)
            print(' ')
            break
        else:
            print(' ')
            continue

allTables = []

def printSolvedTable(allTables):
    print('\nHere are all the solved 4x4 and 9x9 table:\n')

    for table in allTables:
        tableLength = len(table)
        if tableLength == 4:
            for row in range(4):
                if row % 2 == 0 and row != 0:
                    print('- - - - -')

                for column in range(4):
                    if column % 2 == 0 and column != 0:
                        print('|', end = ' ')

                    if column == 3:
                        print(str(table[row][column]))
                    else:
                        print(str(table[row][column]) + ' ', end = '')

            print(' ')

        if tableLength == 9:
            for row in range(9):
                if row % 3 == 0 and row != 0:
                    print('- - - - - - - - - - -')

                for column in range(9):
                    if column % 3 == 0 and column != 0:
                        print('|', end=' ')

                    if column == 8:
                        print(str(table[row][column]))
                    else:
                        print(str(table[row][column]) + ' ', end='')

            print(' ')

def main(tables):
    while True:
        print('-------SUDOKU SOLVER PROGRAM-------')
        userChoice = input('Press 1 - 4x4 Sudoku Solver Program\nPress 2 - 9x9 Sudoku Solver Program\nPress 3 - Exit\nChoice: ')

        if userChoice == '1':
            runFourByFour()
            continue

        if userChoice == '2':
            runNineByNine()
            continue

        if userChoice == '3':
            printSolvedTable(tables)
            break

        else:
            print('\nThat is not an option!!!\n')

main(allTables)





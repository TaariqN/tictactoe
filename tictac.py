class Board:
    def __init__(self):
        # initialising a 3 by 3 grid fot the board
        self.grid = [[0 for yCoord in range(3)] for xCoord in range(3)]
        for xCoord in range(3):
            for yCoord in range(3):
                self.grid[xCoord][yCoord] = "-"

        # creates an empty 3 by 3 grid

    def showGrid(self):
        # Iterates through the  grid so as to output all of its current element
        print("COORDINATES 0,0 IS ON THE TOP LEFT AND 3,3 ON BOTTOM RIGHT")
        for xCoord in range(3):
            for yCoord in range(3):
                print(self.grid[xCoord][yCoord], end=" ")
            print("")

    def isEmpty(self, xCoord, yCoord):
        empty = True
        if self.grid[xCoord][yCoord] != "-":
            empty = False

        return empty

    def fillGrid(self, xCoord, yCoord, symbol):
        # changes the value of a specific position in the grid
        self.grid[xCoord][yCoord] = symbol

    def checkRows(self, symbol):

        rowCount = 0  # contains the index of current row being checked in the Grid
        matching_row = False

        # for xCoord in range(3):
        while not matching_row:
            elementsCheck = 0  # stores the number of similar symbol in a particular row

            for yCoord in range(3):
                # print(self.grid[xCoord][yCoord], end=" ")
                if self.grid[rowCount][yCoord] == symbol:
                    elementsCheck += 1
                    if elementsCheck == 3:
                        matching_row = True
                        return matching_row

            rowCount += 1
            # xCoord += 1
            if rowCount == 3:
                # print("test output")
                return matching_row

    def checkColumns(self, symbol):

        colCount = 0  # contains the index of current column being checked in the Grid
        matching_col = False

        # for xCoord in range(3):
        while not matching_col:
            elementsCheck = 0  # stores the number of similar symbol in a particular row

            for xCoord in range(3):
                # print(self.grid[xCoord][yCoord], end=" ")
                if self.grid[xCoord][colCount] == symbol:
                    elementsCheck += 1
                    if elementsCheck == 3:
                        matching_col = True
                        return matching_col

            colCount += 1

            if colCount == 3:
                # print("test output")
                return matching_col

    def checkDiagonals(self, symbol):
        matching_diag = False  # if a matched diagonal is found then matching_diag returns true
        # checks the first diagonal
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == symbol:

            matching_diag = True
            return matching_diag
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == symbol:
            matching_diag = True
            return matching_diag

        else:
            # if there is no matching diagonals then matching_diag will remain false
            return matching_diag


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:

    def __init__(self):
        self.grid = Board()

    def show(self):
        self.grid.showGrid()

    def playerInput(self, player):

        wrongCoordinates = True
        while wrongCoordinates:
            print("coordinates of x and y should be between 1 and 3 inclusive")
            x = int(input("Row number : ")) - 1

            y = int(input("Column number : ")) - 1

            if (0 <= x < 3) and (0 <= y < 3):
                if not self.grid.isEmpty(x, y):
                    print("This position is already taken, please select another position")
                else:

                    break

        self.grid.fillGrid(x, y, player.symbol)

    def winCheck(self, player):
        # use this method in play
        won = False
        if self.grid.checkRows(player.symbol):  # if there is a row with the same symbols
            # print("player {} wins".format(player.name))
            won = True
        elif self.grid.checkColumns(player.symbol):  # if there is a column with the same symbols
            # print("player {} wins".format(player.name))
            won = True
        elif self.grid.checkDiagonals(player.symbol):
            # print("player {} wins".format(player.name))
            won = True

        return won

    def play(self, currentPlayer, turnNumber):
        endgame = False
        print(currentPlayer.name, "'s turn")
        self.playerInput(currentPlayer)
        if self.winCheck(currentPlayer):
            print("player {} wins\n".format(currentPlayer.name))
            endgame = True
            return endgame

        elif turnNumber == 8:
            endgame = True
            return endgame

        else:
            return endgame


# def fillGrid(self):

newgame = Game()

player1 = Player(input("Enter Player 1 name (X):"), "X")  # player1 is X by default and always plays first
player2 = Player(input("Enter Player 2 name (O):"), "O")

newgame.show()
# turn = 0
for turn in range(9):
    # since player 1 plays first the turn number of player 1 will always be an even number

    if turn % 2 == 0:
        gameState = newgame.play(player1, turn)

    else:
        gameState = newgame.play(player2, turn)

    newgame.show()
    if gameState and turn == 8:
        print("DRAW")
        break
    elif gameState:
        break

# newgame.winCheck(player1)

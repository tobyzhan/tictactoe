# Tic Tac Toe

import random
class TicToc:
    def drawBoard(self,board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def chooseLetter(self):
        print('Player one would you like to be X or O?')
        letterOne = input()
        letterOne = letterOne.upper()
        while True:
            if letterOne == 'X':
                letterTwo = 'O'
                print('Player one is '+ letterOne +' and Player two is '+letterTwo)
                return letterOne, letterTwo
            elif letterOne == 'O':
                letterTwo = 'X'
                print('Player one is '+ letterOne +' and Player two is '+letterTwo)
                return letterOne, letterTwo
            else:
                print('Please pick between X and O!')
                chooseLetter()
                break
            
    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player one'
        else:
            return 'player two'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self,board, letterOne,letterTwo, move):
        if turn == 'player one':
            board[move] = letterOne
        if turn == 'player two':
            board[move] = letterTwo

    def isWinner(self,bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self,board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self,board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(self,board,turn):
        if turn == 'player one':
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
                print('Player one, what is your next move? (1-9)')
                move = input()
            return int(move)
        if turn == 'player two':
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
                print('Player two, what is your next move? (1-9)')
                move = input()
            return int(move)
    

    def getPlayer2Move(self,board, letterTwo):
        # Given a board and the computer's letter, determine where to move and return that move.
        if letterTwo == 'X':
            letterOne = 'O'
        else:
            letterOne = 'X'

    def isBoardFull(self,board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True


print('Welcome to Tic Tac Toe by Meena and Toby!')
game = TicTacToe()
while True:
    # Reset the board
    theBoard = [' '] * 10
    letterOne, letterTwo = game.chooseLetter()
    turn = game.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'playerOne':
            # Player's turn.
            game.drawBoard(theBoard)
            move = game.getPlayerMove(theBoard, letterOne)
            game.makeMove(theBoard, letterOne, move)

            if game.isWinner(theBoard, letterOne):
                game.drawBoard(theBoard)
                print('Hooray! Player one you have won the game!')
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'playerTwo'

        else:
            # Computer's turn.
            move = game.getPlayerMove(theBoard, letterTwo)
            makeMove(theBoard, letterTwo, move)

            if isWinner(theBoard, letterTwo):
                drawBoard(theBoard)
                print('Player one has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'playerOne'

    if not replay():
        break





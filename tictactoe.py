## Tic Tac Toe
import random
class TicTacToe:
  def drawBoard(board,move):
      theBoard = '''
    _______________________
   |       |       |       | 
   |   7   |   8   |   9   |
   |_______|_______|_______|
   |       |       |       |
   |   4   |   5   |   6   |
   |_______|_______|_______|
   |       |       |       |
   |   1   |   2   |   3   |
   |_______|_______|_______|'''
      print(board)
      for i in range(1, 10):
        if (board[i] == 'O' or board[i] == 'X'):
          blankBoard = blankBoard.replace(str(i), board[i])
        else:
          blankBoard = blankBoard.replace(str(i), ' ')
      print(theBoard)
   
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
            
  def replay():
        playagain = input("Do you want to play again (y/n) ? ")
        if playagain.lower() == 'y':
            return True
        if playagain.lower() == 'n':
            return False
         
        
  def makeMove(board, letter, move):
        board[move] = letter

  def isWinner(bo, le):
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

  def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

  def isSpaceFree(board, move):
  # Return true if the passed move is free on the passed board.
      return board[move] == ' '

  def getPlayerMove(board,move,turn):
  # Let the player type in his move.
      move = ' '
      while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
          print('What is your next move? (1-9)')
          move = input()
      return int(move)

  def whoGoesFirst(self):
      # Randomly choose the player who goes first.
      if random.randint(0, 1) == 0:
          return 'playerOne'
      else:
          return 'playerTwo'

  def isBoardFull(board):
  # Return True if every space on the board has been taken. Otherwise return False.
      for i in range(1, 10):
          if isSpaceFree(board, i):
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





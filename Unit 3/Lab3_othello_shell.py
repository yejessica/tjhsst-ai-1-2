# Name: Jessica Ye
# Date: 1/10/22

import random

class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      # best_move = [1, 1] # change this
      pos_moves = self.find_moves(board, color)
      best_move = random.choice(list(pos_moves.keys()))
      moveArr = [best_move//8, best_move%8]
      # print(board)
      # print(best_move)
      return moveArr, 0

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      counter = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.':
               counter+=1
      return counter

   def find_moves(self, board, color):
    # finds all possible moves
      # return 1
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
               flipped_stones = self.find_flipped(board, i, j, color)
               if len(flipped_stones) > 0:
                  moves_found.update({i*self.y_max+j: flipped_stones})
      # print(moves_found)
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      # return 1
      if board[x][y] != ".":
        return []
      if color == self.black:
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
               if board[x_pos][y_pos] == ".":
                  break
               if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
               temp_flip.append([x_pos, y_pos])
               x_pos += incr[0]
               y_pos += incr[1]
      return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8


   def best_strategy(self, board, color):
    # returns best move
      # return best_move, 0
      color = "@" if color == "#000000" else "O"
      move, v = self.max_value(board, color, 3)
      return move, v

   def max_value(self, board, color, search_depth):
      # color = "@" if color == "#ffffff" else "O"
      v = -50000000
      bestMove = [-1,-1]
      posMoves = self.find_moves(board, color) #DICTIONARY
      moveNums = list(posMoves.keys())
      if len(moveNums) == 0:
         return [-1,-1], -1
      for a in moveNums:
         moveCoords = [a//8, a%8]
         if search_depth == 0:
            return moveCoords, self.evaluate(board, color, posMoves)
         else:
            # copy the board to a new board
            newBoard = [[i for i in col] for col in board]
            newBoard = self.make_move(newBoard, color, a, posMoves)
            temp, value = self.min_value(newBoard, self.opposite_color[color], search_depth-1)
            if v < value:
               v = value
               bestMove = moveCoords
 
      return bestMove, v 

   def min_value(self, board, color, search_depth):
      # print(color)
      # color = "@" if color == "#ffffff" else "O"
      v = 50000000
      bestMove = [-1,-1]
      posMoves = self.find_moves(board, color)
      moveNums = list(posMoves.keys())
      if len(moveNums) == 0:
         return [-1,-1], -1
      for a in moveNums:
         # possible = self.evaluate(board, color, posMoves)
         moveCoords = [a//8, a%8]
         if search_depth == 0:
            return moveCoords, self.evaluate(board, color, posMoves)
         else:
            # copy the board to a new board
            newBoard = [[i for i in col] for col in board]
            newBoard = self.make_move(newBoard, color, a, posMoves)
            temp, value = self.max_value(newBoard, self.opposite_color[color], search_depth-1)
            if v > value:
               v = value
               bestMove = moveCoords

      return bestMove, v
   # def minimax(self, board, color, search_depth):
   #  # returns best "value"
   #    return 1

   # def negamax(self, board, color, search_depth):
   #  # returns best "value"
   #    return 1
      
   # def alphabeta(self, board, color, search_depth, alpha, beta):
   #  # returns best "value" while also pruning
   #    pass

   # def make_key(self, board, color):
   #  # hashes the board
   #    return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
      counter = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.':
               counter+=1
      return counter

   def make_move(self, board, color, move, posMoves):
      # returns board that has been updated
      moveCoords = [move//8, move%8]
      board[moveCoords[0]][moveCoords[1]] = color
      for pos in posMoves[move]:
         board[pos[0]][pos[1]] = color
      # return 1
      # print(board) #TEMP CHECK
      return board

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      opposite_moves = self.find_moves(board, "@" if color == "O" else "O")
      # print(opposite_moves)
      posMoves = list(opposite_moves.keys())
      evalNum = len(possible_moves) - len(posMoves)
      # for move in posMoves:
      #    # moveCoords = [move//8, move%8]
      #    newBoard = [[i for i in col] for col in board]
      #    newBoard = make_move(newBoard, color, move, posMoves)
         
      return evalNum

   # def score(self, board, color):
   def score(self, board, color):
    # returns the score of the board 
    #OPTIMIZE????
      scoreBlack = 0
      scoreWhite = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
               if board[i][j] == "@":
                  scoreBlack += 1
               if board[i][j] == "O":
                  scoreWhite += 1
      return scoreBlack, scoreWhite
      # return 1

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
               flipped_stones = self.find_flipped(board, i, j, color)
               # print(flipped_stones)
               if len(flipped_stones) > 0:
                  moves_found.update({i*self.y_max+j: flipped_stones})
      # print(moves_found)
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      # return 1
      if board[x][y] != ".":
        return []
      if color == self.black:
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos and x_pos < self.x_max and 0 <= y_pos and y_pos < self.y_max:
               if board[x_pos][y_pos] == ".":
                  break
               if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
               temp_flip.append([x_pos, y_pos])
               x_pos += incr[0]
               y_pos += incr[1]
      # print(flipped_stones)
      return flipped_stones

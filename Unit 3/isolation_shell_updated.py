# Name: Jessica Ye
# Date: 12/10/21
# from isolation_runner import make_move
# from Ye_J_U3_L1 import minimax
import random

# from isolation_runner import find_moves

class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      moves = self.find_moves(board, color)
      if len(moves) == 0:
         # print("???")
         return (-1,-1), 0
      
      # returns best move
      # (column num, row num), 0
      # print(color)
      # print(board)
      # print(moves)
      r = random.choice(moves)
      # print(r)
      return r, 0
      # return 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]

      y_max = 5
      x_max = 5
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
            # print(self.first_turn)
            if self.first_turn and board[i][j] == '.': 
               moves_found.add(i*y_max+j)
            if (color == "#000000" and board[i][j] == 'X') or (color == "#ffffff" and board[i][j] == 'O'):
               for incr in self.directions:
                  x_pos = i + incr[0]
                  y_pos = j + incr[1]
                  stop = False
                  while 0 <= x_pos < x_max and 0 <= y_pos < y_max:
                        if board[x_pos][y_pos] != '.':
                           stop = True
                        if not stop:    
                           moves_found.add(x_pos*y_max+y_pos)
                        x_pos += incr[0]
                        y_pos += incr[1]
         self.first_turn = False
      coordSets = []
      #ROWS: %
      #COLS: //
      #(COLS, ROWS)
      for i in moves_found:
         newSet = (i//y_max, i%x_max)
         coordSets.append(newSet)
      return coordSets

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True

   def best_strategy(self, board, color):
      # returns best move
      # return best_move, 0
      # returnMove = self.minimax(board, color, 3) 
      # print(self.minimax(board, color, 3) )
      # print(returnMove)
      # if returnMove == (-1,-1):
      #    print("hi")
      v, move = self.min_value(board, color, 3)
      return move, v
      # return self.minimax(board, color, 3) 


   def minimax(self, board, color, search_depth):
      # search_depth: start from 2
      # returns best "value"
      # return best_move, 1
      v, move = self.max_value(board, color, search_depth)
      # print(move)
      return move, v 

   def max_value(self, board, color, search_depth):
      v = -50000000
      bestMove = (-1,-1)
      posMoves = self.findmoves(board, color)
      # print(posMoves)
      # print(len(posMoves))
      # print("searcH",search_depth)
      if len(posMoves) == 0:
         return -1, (-1,-1)
      for a in posMoves:
         # possible = self.evaluate(board, color, posMoves)
         if search_depth == 0:
            return self.evaluate(board, color, posMoves), a
         else:
            # copy the board to a new board
            newBoard = [[i for i in col] for col in board]
            newBoard = self.make_move(newBoard, color, a)
            value, temp = self.min_value(newBoard, self.opposite_color[color], search_depth-1)
            if v < value:
               v = value
               bestMove = a
      # if bestMove == (0,0):
      #    # print("hoi")
      #    bestMove = posMoves[0]
      return v, bestMove
         # if search_depth == 
      
         

   def min_value(self, board, color, search_depth):
      v = 50000000
      bestMove = (-1,-1)
      posMoves = self.findmoves(board, color)
      # print(posMoves)

      # print(len(posMoves))
      # print("searcH",search_depth)
      if len(posMoves) == 0:
         return 1, (-1,-1)
      for a in posMoves:
         # possible = self.evaluate(board, color, posMoves)
         if search_depth == 0:
            return self.evaluate(board, color, posMoves), a
         else:
            # copy the board to a new board
            newBoard = [[i for i in col] for col in board]
            newBoard = self.make_move(newBoard, color, a)
            value, temp = self.max_value(newBoard, self.opposite_color[color], search_depth-1)
            if v > value:
               v = value
               bestMove = a
      # if bestMove == (0,0):
      #    # print("hoi")
      #    bestMove = posMoves[0]
      return v, bestMove

   # def negamax(self, board, color, search_depth):
   #    # returns best "value"
   #    return 1
      
   # def alphabeta(self, board, color, search_depth, alpha, beta):
   #    # returns best "value" while also pruning
   #    pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      
      for i in range(len(board)):
         for j in range(len(board[i])):
            if((board[i][j]=="O" and color == self.white) or (board[i][j]=="X" and color == self.black)):
               board[i][j] = "W"
               break
         else:
            continue
         break
      board[move[0]][move[1]] = "X" if color == self.black else "O"
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      # return 1

      eval = len(possible_moves) - len(self.findmoves(board, self.opposite_color[color]))
      return eval


   def findmoves(self, board, color):
      # finds all possible moves
      # return set()
      symbol = 'X' if color == "#000000" else 'O'
      if not any(symbol in b for b in board):
         self.first_turn = True
      y_max = 5
      x_max = 5
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
            # print(self.first_turn)
            if self.first_turn and board[i][j] == '.': 
               moves_found.add(i*y_max+j)
            if (color == "#000000" and board[i][j] == 'X') or (color == "#ffffff" and board[i][j] == 'O'):
               for incr in self.directions:
                  x_pos = i + incr[0]
                  y_pos = j + incr[1]
                  stop = False
                  while 0 <= x_pos < x_max and 0 <= y_pos < y_max:
                        if board[x_pos][y_pos] != '.':
                           stop = True
                        if not stop:    
                           moves_found.add(x_pos*y_max+y_pos)
                        x_pos += incr[0]
                        y_pos += incr[1]
      self.first_turn = False
      coordSets = []
      #ROWS: %
      #COLS: //
      #(COLS, ROWS)
      for i in moves_found:
         newSet = (i//y_max, i%x_max)
         coordSets.append(newSet)
      return coordSets


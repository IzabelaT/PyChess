import Board
import Moves


class Play:

    def __init__(self):
        self.x, self.y, self.selection, self.turn, self.possible_moves = None
        self.board = [['br', 'bh', 'bb', 'bq', 'bk', 'bb', 'bh', 'br'],['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],['wr', 'wh', 'wb', 'wq', 'wk', 'wb', 'wh', 'wr']]
        self.turn = 'w'
        self.possible_moves = []
    
    
    
    def play(self):
        
      self.selection, self.turn, self.possible_moves
      self.x = int((self.x - self.x % 80) / 80)
      self.y = int((self.y - self.y % 80) / 80)
    
        if self.selection == '' and self.board[self.y][self.x] != 'e':
            if self.board[self.self.y][self.x][0] == self.turn:
                self.selection = [self.x, self.self.y]
                self.possible_moves = Moves.possibleMoves(self.x, self.y, board[self.y][self.x], board)
                if board[self.y][self.x][1] == 'k':
                    if board[self.y][self.x][0] == 'w':
                        if self.x == 4 and self.y == 7:
                            if board[7][7] == 'wr':
                                if board[7][6] == 'e' and board[7][5] == 'e':
                                    self.possible_moves.append([7, 7])
                            if board[7][0] == 'wr':
                                if board[7][3] == 'e' and board[7][2] == 'e' and board[7][1] == 'e':
                                    self.possible_moves.append([0, 7])
                    else:
                        if self.x == 4 and self.y == 0:
                            if board[0][7] == 'br':
                                if board[0][6] == 'e' and board[0][5] == 'e':
                                    self.possible_moves.append([7, 0])
                            if board[0][0] == 'br':
                                if board[0][3] == 'e' and board[0][2] == 'e' and board[0][1] == 'e':
                                    self.possible_moves.append([0, 0])
                main.select(self.x, self.y)
                for move in self.possible_moves:
                    main.highlight(move[0], move[1])
    
        elif [self.x, self.y] == self.selection:
            main.unselect(self.selection[0], self.selection[1])
            for move in Moves.possible_moves:
                main.un_highlight(move[0], move[1])

            self.selection = ''
            self.possible_moves = []
    
        elif [self.x, self.y] in Moves.possible_moves:
            moved = False
            if board[self.selection[1]][self.selection[0]][1] == 'k':
                if board[self.selection[1]][self.selection[0]][0] == 'w':
                    if self.selection == [4, 7]:
                        if [self.x, self.y] == [0, 7]:
                            main.move(0, 7, 2, 7)
                            main.move(4, 7, 1, 7)
                            board[7][2], board[7][1] = board[7][0], board[7][4]
                            board[7][1], board[7][4] = 'e','e'
                            moved = True
                        elif [self.x, self.y] == [7, 7]:
                            main.move(7, 7, 5, 7)
                            main.move(4, 7, 6, 7)
                            board[7][5], board[7][6] = board[7][7], board[7][4]
                            board[7][7], board[7][4] = 'e','e'
                            moved = True
                else:
                    if self.selection == [4, 0]:
                        if [self.x, self.y] == [0, 0]:
                            main.move(0, 0, 2, 0)
                            main.move(4, 0, 1, 0)
                            board[0][2], board[0][1] = board[0][0], board[0][4]
                            board[0][0], board[0][4] = 'e','e'
                            moved = True
                        elif [self.x, self.y] == [7, 0]:
                            main.move(7, 0, 5, 0)
                            main.move(4, 0, 6, 0)
                            board[0][5], board[0][6] = board[0][7], board[0][4]
                            board[0][7], board[0][4] = 'e','e'
                            moved = True
            if not moved:
                main.move(self.selection[0], self.selection[1], self.x, self.y)
                board[self.y][self.x] = board[self.selection[1]][self.selection[0]]
                board[self.selection[1]][self.selection[0]] = 'e'
    
            main.unselect(self.selection[0], self.selection[1])
            for move in Moves.possible_moves(self.y,self.x):
                main.un_highlight(move[0], move[1])

            self.possible_moves = []
            self.selection = ''
    
            if self.turn == 'w':
                turn = 'b'
            else:
                turn = 'w'
    
            found = False
            for line in board:
                for piece in line:
                    if piece == turn + 'k':
                        found = True
                        break
    
            if not found:
                if turn == 'b':
                    print('White Wins')
                else:
                    print('Black Wins')
                main.destroy()


    main = Board.Board(Play.play)
    main.window.mainloop()

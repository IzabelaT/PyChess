import tkinter
import os


class Board:
    SIZE = 640

    def __init__(self, trigger):
        self.click = ''

        self.window = tkinter.Tk()
        self.window.geometry(f'{self.SIZE}x{self.SIZE}')
        self.window.title('Chess')
        self.icon = tkinter.PhotoImage(file="icon/chess.png")
        self.window.iconphoto(True,self.icon)
        self.window.minsize(self.SIZE,self.SIZE)
        self.window.maxsize(self.SIZE,self.SIZE)

        self.board = tkinter.Canvas(self.window, width=640, height=640)
        self.board.pack()

        self.pieces = {'black': {}, 'white': {}}
        directories = os.listdir('pieces')

        if '.DS_Store' in directories:
            directories.remove('.DS_Store')

        for directory in directories:
            dirs = os.listdir('pieces/' + directory)
            for subdir in dirs:
                self.pieces[directory][subdir.replace('.gif', '')] = tkinter.PhotoImage(
                    file='pieces/' + directory + '/' + subdir).subsample(5, 5)

        self.squares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

        self.boardSquares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

        for x in range(8):
            for y in range(8):
                if x % 2 == y % 2:
                    self.boardSquares[y][x] = self.board.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80,
                                                                          fill='#b3b3b3')
                else:
                    self.boardSquares[y][x] = self.board.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80,
                                                                          fill='#666666')

        self.createForm(0, 0, 'black', 'rook')
        self.createForm(7, 0, 'black', 'rook')
        self.createForm(1, 0, 'black', 'knight')
        self.createForm(6, 0, 'black', 'knight')
        self.createForm(2, 0, 'black', 'bishop')
        self.createForm(5, 0, 'black', 'bishop')
        self.createForm(4, 0, 'black', 'king')
        self.createForm(3, 0, 'black', 'queen')
        for x in range(8):
            self.createForm(x, 1, 'black', 'pawn')
            self.createForm(x, 6, 'white', 'pawn')
        self.createForm(0, 7, 'white', 'rook')
        self.createForm(7, 7, 'white', 'rook')
        self.createForm(1, 7, 'white', 'knight')
        self.createForm(6, 7, 'white', 'knight')
        self.createForm(2, 7, 'white', 'bishop')
        self.createForm(5, 7, 'white', 'bishop')
        self.createForm(4, 7, 'white', 'king')
        self.createForm(3, 7, 'white', 'queen')

        self.board.bind('<Button>', trigger)

    def move(self, x1, y1, x2, y2):
        self.board.move(self.squares[y1][x1], (x2 - x1) * 80, (y2 - y1) * 80)
        if self.squares[y2][x2] != '':
            self.board.delete(self.squares[y2][x2])
        self.squares[y2][x2] = self.squares[y1][x1]
        self.squares[y1][x1] = ''

    def createForm(self, x, y, color, piece):
        img = self.pieces[color][piece]
        self.squares[y][x] = self.board.create_image(x * 80 + 40, y * 80 + 40, image=img)

    def highlight(self, x, y):
        self.board.itemconfig(self.boardSquares[y][x], fill='lightblue')

    def un_highlight(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardSquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardSquares[y][x], fill='#666666')

    def select(self, x, y):
        self.board.itemconfig(self.boardSquares[y][x], fill='green')

    def unselect(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardSquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardSquares[y][x], fill='#666666')

    def destroy(self):
        self.window.destroy()

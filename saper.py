import random
import tkinter as tk

class ButtonField(tk.Button):
    def __init__(self,  *args, **kwargs):
        tk.Button.__init__(self, command= self.gameLogic, photo = PhotoImage(file="empty.gif"),  *args, **kwargs)
        self.config(activebackground=self.cget('background'))
        self.__Mine = False
        self.__checked = False
        self.bind('<Button-3>', self.rightclick)
        self.clicks = 0


    def gameLogic(self):
        if self.isChecked() or self.clicks != 0:
            pass
        else:
            self.config(relief = "sunken") #make button pressed
            self.__checked = True
            if self.hasMine():
                self.config(bg="black")
                self.config(activebackground="black")
            else:
                mines = self.minesAround()
                if mines != 0:
                    self.config(text = self.minesAround())


    def rightclick(self, event):
        self.clicks = (self.clicks + 1) % 3
        if self.clicks == 1:
            self.config(text = "*")
        elif self.clicks == 2:
            self.config(text = "?")
        else:
            self.config(text = " ")


    def hints(self):
        if self.hasMine():
            self.config(bg='grey')

    def isChecked(self):
        return self.__checked

    def setMine(self):
        self.__Mine = True

    def hasMine(self):
        return self.__Mine

    def setMineAmount(self, amount):
        self.__minesAmount = amount

    def minesAround(self):
        return self.__minesAmount


class MineField(object):
    def __init__(self, dimX, dimY, mineNumber):
        board = []
        for i in range(0, dimX, 1):
            board.append([])
            for j in range(0, dimY, 1):
                board[i].append(ButtonField())
        self.__board = board
        self.setMines(mineNumber)
        self.checkIfNeighboursHasMines()

    def getBoard(self):
        return self.__board


    def setMines(self, mineNumber):
            random.seed()
            mineCreated = 0
            while mineCreated < mineNumber:
                xrand = random.randrange(0,len(self.__board),1)
                yrand = random.randrange(0,len(self.__board[0]),1)
                if(self.hasMine(xrand,yrand)):
                    pass
                else:
                    self.__board[xrand][yrand].setMine()
                    mineCreated+=1

    def checkIfNeighboursHasMines(self):
        for i in range(0, len(self.__board), 1):
            for j in range(0, len(self.__board[i]), 1):
                minesAmount = 0
                if i == 0:
                    if j == 0:
                        if(self.hasMine(i, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j+1)):
                            minesAmount+=1
                    elif j == len(self.__board[i]) - 1:
                        if(self.hasMine(i, j-1)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j-1)):
                            minesAmount+=1
                    else:
                        if(self.hasMine(i, j-1)):
                            minesAmount+=1
                        if(self.hasMine(i, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j-1)):
                            minesAmount+=1

                elif i == len(self.__board) - 1:
                    if j == 0:
                        if(self.hasMine(i, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j+1)):
                            minesAmount+=1
                    elif j == len(self.__board[i]) - 1:
                        if(self.hasMine(i, j-1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j-1)):
                            minesAmount+=1
                    else:
                        if(self.hasMine(i, j-1)):
                            minesAmount+=1
                        if(self.hasMine(i, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j-1)):
                            minesAmount+=1
                elif j == 0:
                        if(self.hasMine(i+1, j)):
                            minesAmount+=1
                        if(self.hasMine(i, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j+1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j+1)):
                            minesAmount+=1
                elif j == len(self.__board[i]) - 1:
                        if(self.hasMine(i+1, j)):
                            minesAmount+=1
                        if(self.hasMine(i, j-1)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j)):
                            minesAmount+=1
                        if(self.hasMine(i-1, j-1)):
                            minesAmount+=1
                        if(self.hasMine(i+1, j-1)):
                            minesAmount+=1
                else:
                    if(self.hasMine(i+1, j)):
                        minesAmount+=1
                    if(self.hasMine(i-1, j)):
                        minesAmount+=1
                    if(self.hasMine(i, j+1)):
                        minesAmount+=1
                    if(self.hasMine(i, j-1)):
                        minesAmount+=1
                    if(self.hasMine(i+1, j-1)):
                        minesAmount+=1
                    if(self.hasMine(i-1, j-1)):
                        minesAmount+=1
                    if(self.hasMine(i+1, j+1)):
                        minesAmount+=1
                    if(self.hasMine(i-1, j+1)):
                        minesAmount+=1
                self.__board[i][j].setMineAmount(minesAmount)

    def hasMine(self, x, y):
        return self.__board[x][y].hasMine()
    def minesAround(self, x, y):
        return self.__board[x][y].minesAround()

class Game(object):
    def __init__(self, dimX, dimY, mineNumber):
        self.minefield = MineField(dimX, dimY, mineNumber)

    def getBoard(self):
        return self.minefield.getBoard()




class Saper(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        root.title("Saper")
        root.bind_all('<Key>', self.keyPressed)
        self.xyz = [0, 0, 0]

        dimX = 8
        dimY = 8
        mineNumber = 19
        if dimX > 15 or dimX < 2 or dimY > 15 or dimY < 2:
            raise Exception("nieprawidłowy rozmiar mapy, min 2x2, max 15x15")
        if mineNumber > dimX * dimY:
            raise Exception("Tyle min nie zmiesci sie na planszy")
        self.__mineNumber = mineNumber
        self.__board = Game(dimX,dimY, mineNumber).getBoard()
        self.create_widgets(self.__board)

    def create_widgets(self, board):
        for i in range(0, len(board), 1):
            for j in range(0, len(board[0]), 1):
                    board[i][j].grid(row=i, column=j)

    def showHints(self):
        for i in range(0, len(self.__board), 1):
            for j in range(0, len(self.__board[0]), 1):
                    self.__board[i][j].hints()

    def keyPressed(self, event):
        #xyzzy
        if event.keycode == 53: #x
            self.xyz = [1, 0, 0]
        elif event.keycode == 29: #y
            if self.xyz[2] != 0 and self.xyz[2] != 2:
                self.xyz = [0, 0, 0]
            else:
                self.xyz[1] = self.xyz[1] + 1
        elif event.keycode == 52: #z
            if self.xyz[1] != 1:
                self.xyz=[0, 0, 0]
            else:
                self.xyz[2] = self.xyz[2] + 1
        else:
            self.xyz = [0, 0, 0]

        if self.xyz[0] == 1 and self.xyz[1] == 2 and self.xyz[2] == 2:
            saper.showHints()









root = tk.Tk()
global saper
saper = Saper(master=root)

def move_dir():
    while True: # edit 1: now looping always
        #print 'moving', direction
        pos = pos + direction
        yield 0.5 # move once every 0.5 seconds


#move_dir(root)
#root.mainloop()
#while 1:
saper.mainloop()

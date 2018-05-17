import random
import tkinter as tk
from tkinter import messagebox


class ButtonField(tk.Button):
    empty = None
    flag = None
    qmark = None
    cheat = None
    bomb = None
    pbomb = None
    tiles = []

    def __init__(self,  *args, **kwargs):
        tk.Button.__init__(self, command= self.leftclick, *args, **kwargs)
        self.config(image=self.empty)
        self.__Mine = False
        self.__checked = False
        self.bind('<Button-3>', self.rightclick)
        self.clicks = 0
        self.__flagged = False

    def setCallback(self, function):
        self.callback = function


    def leftclick(self, *args):
        for arg in args:
            if arg == True:
                if self.hasMine():
                    return
        if self.isChecked() or self.clicks == 1:
            pass
        else:
            self.__checked = True
            if self.hasMine():
                self.config(image = self.bomb)
                self.callback(1)
            else:
                mines = self.minesAround()
                self.config(image = self.tiles[mines])
                if self.minesAround() == 0:
                    self.callback(-1, self)
                else:
                    self.callback(0)

    def rightclick(self, event):
        if self.__checked:
            return
        self.clicks = (self.clicks + 1) % 3
        if self.clicks == 1:
            self.config(image=self.flag)
            self.__flagged = True
            self.callback(2)
        elif self.clicks == 2:
            self.config(image=self.qmark)
            self.callback(3)
        else:
            self.config(image=self.empty)
            self.__flagged = False
            self.callback(4)


    def endGame(self):
        if not self.isChecked():
            self.__checked = True
            if self.hasMine():
                if self.clicks != 1: #Bomb is here <flag mark>
                    self.config(image=self.pbomb)
            else:
                self.config(image=self.tiles[self.__minesAmount])


    def highlight(self):
        if self.hasMine():
            self.config(image = self.cheat)

    def isFlagged(self):
        return self.__flagged

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
    def __init__(self, dimX, dimY, mineNumber, callback):
        board = []
        ButtonField.empty = tk.PhotoImage(file="icons/empty.gif")
        ButtonField.flag = tk.PhotoImage(file="icons/flag.gif")
        ButtonField.qmark = tk.PhotoImage(file="icons/qmark.gif")
        ButtonField.bomb = tk.PhotoImage(file="icons/bomb.gif")
        ButtonField.pbomb = tk.PhotoImage(file="icons/pbomb.gif")
        ButtonField.cheat = tk.PhotoImage(file="icons/cheat.gif")

        for i in range(0, 9):
            path = "icons/n" + str(i) + ".gif"
            ButtonField.tiles.append(tk.PhotoImage(file=path))

        for i in range(0, dimX, 1):
            board.append([])
            for j in range(0, dimY, 1):
                board[i].append(ButtonField())
                board[i][j].setCallback(callback)
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
                if(self.__board[xrand][yrand].hasMine()):
                    pass
                else:
                    self.__board[xrand][yrand].setMine()
                    mineCreated+=1

    def hasMine(self, x, y):
        return self.__board[x][y].hasMine()

    def minesAround(self, x, y):
        return self.__board[x][y].minesAround()

    def checkIfNeighboursHasMines(self):
        for i in range(0, len(self.__board), 1):
            for j in range(0, len(self.__board[0]), 1):
                minesAmount = 0
                # for x in range(0,3):
                #     for y in range (0, 3):
                #         try:
                #             if x == 1:
                #                 if y == 1:
                #                     raise IndexError("its this field")
                #             if self.__board[i+1-y][j+1-x].hasMine(): # [j+1-x] = j+1, j, j-1
                #                 minesAmount+=1 # [i+1-y] = i+1, i, i-1
                #         except IndexError as e:
                #             print(i," ", j, " ", e)
                #             pass
                # self.__board[i][j].setMineAmount(minesAmount)
                #all this below can be replaced with this, but sth wrong with 1st column

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



class Minesweeper(tk.Frame):
    def __init__(self, master=None):
        self.__board = []
        super().__init__(master)
        root.resizable(False, False)
        root.title("Saper")
        root.bind_all('<Key>', self.keyPressed)
        self.__xyz = [0, 0, 0]
        self.__minesweepericon = tk.PhotoImage(file='icons/minesweeper.png')
        self.__minesweepericon = self.__minesweepericon.subsample(6)

        self.__dimX = tk.Text(root, width=6, height = 1)
        self.__dimY = tk.Text(root, width=6, height = 1 )
        self.__mines=tk.Text(root, width=6, height = 1)
        self.__dimX.insert('1.0',"8")
        self.__dimY.insert('1.0',"8")
        self.__mines.insert('1.0',"10")
        self.__dimX.grid(row=0, column=0)
        self.__dimY.grid(row=0, column=1)
        self.__mines.grid(row=0, column=2)


        newGame = tk.Button()
        newGame.config(image=self.__minesweepericon, command = self.startNewGame)
        newGame.grid(row=1, columnspan=3)
        self.__newGame = newGame


    def create_widgets(self, board):
        width = len(board[0])
        if width % 2 == 0:
            width = width % 2 + 1
        else:
            width = width % 2
        self.__dimX.grid(columnspan = width*2)
        self.__dimY.grid(columnspan = width*2, column=width*3)
        self.__mines.grid(columnspan = width*2, column = width*6)
        self.__newGame.grid(column = 0,columnspan = len(board[0]))
        self.__mineLabel = tk.Label(text = self.__mineNumber)
        self.__mineLabel.grid(row =1, column=1)#, columnspan = len(board[0]))
        for i in range(0, len(board), 1):
            for j in range(0, len(board[0]), 1):
                    board[i][j].grid(row=i +2, column=j)

    def startNewGame(self):
        try:
            dimX = int(self.__dimX.get(1.0, 1.9))
            dimY = int(self.__dimY.get(1.0, 1.9))
            mines = int(self.__mines.get(1.0, 1.9))
        except ValueError:
            tk.messagebox.showinfo("Bad parameters", "input has to be a positive number")
            return
        try:
            if dimX > 15 or dimX < 2 or dimY > 15 or dimY < 2:
                raise Exception("invalid map size, min 2x2, max 15x15")
            if mines > dimX * dimY:
                raise Exception("too many mines to this board")
            if mines < 0:
                raise Exception("Mine number has to be positive")
        except Exception as e:
            tk.messagebox.showinfo("Bad parameters", e)
            return
        self.__mineNumber = mines
        self.__board = MineField(dimX, dimY, mines, self.checkStatus).getBoard()
        self.create_widgets(self.__board)
        self.__xyz = [0,0,0]


    def showCheats(self):
        for i in range(0, len(self.__board), 1):
            for j in range(0, len(self.__board[0]), 1):
                    self.__board[i][j].highlight()

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
            saper.showCheats()


    def endGame(self):
        for i in range(0, len(self.__board), 1):
            for j in range(0, len(self.__board[0]), 1):
                    self.__board[i][j].endGame()

    def checkFlags(self):
        if self.__mineNumber == 0:
            endFlag = True
            for i in range(0, len(self.__board), 1):
                for j in range(0, len(self.__board[0]), 1):
                        if self.__board[i][j].isChecked():
                            endFlag = False
                            break
                        if self.__board[i][j].isFlagged():
                            if not self.__board[i][j].hasMine():
                                endFlag = False
                                break
            if(endFlag):
                tk.messagebox.showinfo(" ", "Wygrana")
                self.endGame()


    def checkStatus(self, status, *args):
        """
        status:
           -1 tile with no mines around
            0 casual click
            1 mine clicked
            2 tile flagged
            3 tile question mark
            4 tile unmarked
        """
        if status == -1:
            for arg in args:
                for i in range(0, len(self.__board), 1):
                    for j in range(0, len(self.__board[0]), 1):
                        if self.__board[i][j] == arg:
                            for x in range(0,3):
                                for y in range (0, 3):
                                    try:
                                        self.__board[i+1-y][j+1-x].leftclick(True) # [j+1-x] = j+1, j, j-1
                                    except IndexError:# [i+1-y] = i+1, i, i-1
                                        pass
                            return

        elif status == 1:
            self.endGame()
            tk.messagebox.showinfo(" ", "Przegrales")
        elif status == 2:
            self.__mineNumber -=1
            self.__mineLabel.config(text = self.__mineNumber)
            self.checkFlags()

        elif status == 3:
            self.__mineNumber +=1
            self.__mineLabel.config(text = self.__mineNumber)
            self.checkFlags()
        elif status == 4:
            self.checkFlags()
        else:
            endFlag = True
            for i in range(0, len(self.__board)):
                for j in range(0, len(self.__board[0])):
                    if not self.__board[i][j].isChecked():
                        if not self.__board[i][j].hasMine():
                            endFlag = False
            if endFlag:
                tk.messagebox.showinfo(" ", "Wygrana")







root = tk.Tk()
saper = Minesweeper(master=root)
saper.mainloop()

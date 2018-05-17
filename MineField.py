import tkinter as tk
import ButtonField
from ButtonField import *

class MineField(object):
    def __init__(self, dimX, dimY, mineNumber, callback):
        board = []
        #b = ButtonField()
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

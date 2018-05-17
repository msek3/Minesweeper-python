import tkinter as tk
from MineField import *
from ButtonField import *

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
app = Minesweeper(master=root)
app.mainloop()

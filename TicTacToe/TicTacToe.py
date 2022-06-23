from random import *
import os, sys
path = list(os.getcwd().split("\\"))
edpath = ""
for i in path:
    edpath += i + "/"
sys.path
sys.path.append(edpath + "ShortCode/")

from threading import Thread
from time import sleep
from ShortCode.InDev.UI import *

grid = [None, None, None,
        None, None, None,
        None, None, None]
cases = [["o", None, None,
          None, "o", None,
          None, None, "o"],
         [None, None, "o",
          None, "o", None,
          "o", None, None],
         ["o", None, None,
          "o", None, None,
          "o", None, None],
         [None, "o", None,
          None, "o", None,
          None, "o", None],
         [None, None, "o",
          None, None, "o",
          None, None, "o"],
         [None, None, None,
          None, None, None,
          "o", "o", "o"],
         [None, None, None,
          "o", "o", "o",
          None, None, None],
         ["o", "o", "o",
          None, None, None,
          None, None, None]]
format = "    e     e     e\n    e     e     e\n    e     e     e"

root = GetRoot("TicTacToe by Uday", "200x210")
root.resizable(False, False)

buff = GetLabel(root, "")

out = StringVar(root)
entry = GetEntry(root, out, "10", 15, GetFont(size=15), borderSize=3)
text = GetLabel(root, "Enter difficulty. 0\nis HIGHEST, 10 is\nLOWEST", font=GetFont(size=15))

difficulty = 100000
submitted = False
def SetDifficulty():
    global difficulty
    global submitted
    try:
        diff = int(out.get())
        if(diff >= 0 and diff <= 10):
            difficulty = diff

            root.destroy()
            submitted = True
    except:
        return
            
buff2 = GetLabel(root, "")

button = GetButton(root, "START", font=GetFont(size=15), function=SetDifficulty)

turn = 1
text = None
won = False

while submitted == False:
    nothing = None

    if submitted:
        break;

    root.mainloop()

    if submitted == False:
        break;
else:
    root = GetRoot("TicTacToe by Uday", "200x250")
    root.resizable(False, False)
    out = None

    def k(arg, func):
        global out
        global text
        GetLabel(root, "")
    
        text = Text(root, height=3, width=11, font=GetFont(size=20))
        text.insert(0.0, format)
        text['state'] = DISABLED
        text.pack()

        GetLabel(root, "")

        GetLabel(root, "Enter placement (1-9):", font=GetFont(size=13))

        out = StringVar(root)
        GetEntry(root, out, "", 15, GetFont(size=15))

        GetLabel(root, "", font=GetFont(size=1))
        GetButton(root, "SUBMIT", font=GetFont(size=10), width=20, height=1, function=func)

    def updategame(arg):
        global won
        global turn

        while True:
            if won == False:
                if turn == 0:
                    RunInternalTurn()
                    turn = 1

                result = CheckWin()
                if result[0] == False:
                    sleep(0.5)
                    finish(1)

                elif result[0] == True:
                    sleep(0.5)
                    finish(2)

                if None not in grid:
                    sleep(0.5)
                    finish(3)

                sleep(1)
            else:
                break

    if __name__ == "__main__":
        oldtext = None
        def PRINT():
            global text
            global oldtext

            if text != None:
                if oldtext != None:
                    oldtext.pack_forget()
                    oldtext = None

                string = format
                lst = []

                for i in format:
                    lst.append(i)

                index = 0
                for i in range(len(lst)):
                    if(lst[i] == "e"):
                        if(grid[index] == 'o'):
                            lst[i] = "o"
                        if(grid[index] == 'x'):
                            lst[i] = "x"
                        
                        index += 1

                string = ""
                for i in lst:
                    string += i

                text['state'] = NORMAL
                text.delete("0.0", "end")
                text.insert(0.0, string)
                text['height'] = 3
                text['width'] = 11
                text['font'] = GetFont(size=20)
                text['state'] = DISABLED
                text.pack()
        def CheckWin():
            global won
            if None not in grid:
                won = True

            special = -1
            special2 = -1
            for i in cases:
                o = 0
                x = 0
                for j in range(len(i)):
                    if i[j] == "o" and grid[j] == "o":
                        o += 1
                    if i[j] == "o" and grid[j] == "x":
                        x += 1
                if o == 3:
                    won = True
                    return [False]
                elif x == 3:
                    won = True
                    return [True]
                elif x == 2 and o == 0:
                    special = cases.index(i)
                    special2 = "x"
                elif o == 2 and x == 0:
                    special = cases.index(i)
                    special2 = "o"

            if(special == -1):
                return ["None"]
            else:
                return ["None", special, special2]
        def RunTurn():
            global turn
            try:
                if turn == 1 and won == False:
                    index = int(out.get())
                    if index not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or grid[index - 1] == "x" or grid[index - 1] == "o":
                        return
                    else:
                        grid[index - 1] = "o"

                    turn = 0
                    PRINT()
            except:
                return
        def RunInternalTurn():
            input = CheckWin()
            if won == False:
                def randomTurn():
                    index = int(randrange(0, 9))
                    
                    i = False
                    while(True):
                        if grid[index] == "x" or grid[index] == "o":
                            if i == False:
                                index += 1
                            else:
                                index -= 1
                            if index == 8:
                                i = True
                        else:
                            grid[index] = "x"
                            break
                if(len(input) == 1):
                    randomTurn()
                elif(difficulty == 0 or int(randrange(0, difficulty) == int(difficulty / 2))):
                    i = cases[input[1]]
                    for j in range(len(i)):
                        if(input[2] == "x"):
                            if i[j] == "o" and grid[j] != "x":
                                if grid[j] == "o":
                                    randomTurn()
                                    break
                                grid[j] = "x"
                        elif(input[2] == "o"):
                            if i[j] == "o" and grid[j] != "o":
                                if grid[j] == "x":
                                    randomTurn()
                                    break
                                grid[j] = "x"
                        elif(input[2] == -1):
                            randomTurn()
                            break
                else:
                    randomTurn()

                PRINT()
        def finish(code):
            global root
            if int(code) == 1:
                showinfo("TicTacToe by Uday", "Yay! You won the game.")
            if int(code) == 2:
                showinfo("TicTacToe by Uday", "The computer won this time. Try again!")
            if int(code) == 3:
                showinfo("TicTacToe by Uday", "It's a draw! Everyone wins!")

            root.destroy()
        
        thread2 = Thread(target = k, args = (12, RunTurn), daemon = True)
        thread = Thread(target = updategame, args = (12,), daemon = True)
        thread2.start()
        thread.start()
        
        root.mainloop()
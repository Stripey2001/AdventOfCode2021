Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)

Draw = Input[0]
Draw = Draw.split(",")
Draw[-1] = Draw[-1][:-1]

def CreateBoard(Input,i):
    Board = []
    for j in range(0,5):
        Row=[]
        i+=1
        for k in range(0,5):
            if Input[i][k*3] == " ":
                Number = int(Input[i][k*3+1])
            else:
                Number = (int(Input[i][k*3])*10) + int(Input[i][k*3+1])
            Row.append(Number)
        Board.append(Row)
    return Board, i

def TakeTurn(Draw,TurnNo,Boards):
    Number = int(Draw[TurnNo])
    for i in range(0,len(Boards)):
        for j in range(0,len(Boards[0])):
            for k in range(0,len(Boards[0][0])):
                if Boards[i][j][k] == Number:
                    Boards[i][j][k] = "x"
    return Boards

def CheckRow(Board,RowNo):
    Won = True
    for i in range(0,5):
        if Board[RowNo][i] != "x":
            Won = False
    return Won

def CheckColumn(Board,ColumnNo):
    Won = True
    for i in range(0,5):
        if Board[i][ColumnNo] != "x":
            Won = False
    return Won



def CheckWin(Boards):
    for Board in Boards:
        Won = False
        for i in range(0,5):
            Won = CheckColumn(Board,i)
            if Won:
                return True, Board
            Won = CheckRow(Board,i)
            if Won:
                return True, Board
    return False,Board

def CheckScore(Board):
    Score = 0
    for Row in Board:
        for Item in Row:
            if Item != "x":
                Score += Item
    return Score


Boards = []
Board = []
i = 1
for j in range(0,int((len(Input)-1)/6)):
    Board, i = CreateBoard(Input,i)
    Boards.append(Board)
    i+=1

WinningBoard = []
Winner = False
for i in range(0,len(Draw)):
    Boards = TakeTurn(Draw,i,Boards)
    Winner, WinningBoard = CheckWin(Boards)
    if Winner:
        break
Score = CheckScore(WinningBoard)
print(Score)
print(Draw[i])
print(Score*int(Draw[i]))

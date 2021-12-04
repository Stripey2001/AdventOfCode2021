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



def CheckWin(Board):
    Won = False
    for i in range(0,5):
        Won = CheckColumn(Boards[j],i)
        if Won:
            return True
        Won = CheckRow(Boards[j],i)
        if Won:
            return True
    return False

def CheckScore(Board):
    Score = 0
    for Row in Board:
        for Item in Row:
            if Item != "x":
                Score += Item
    return Score

def CheckBoardStates(BoardState):
    Count = 0
    for Item in BoardState:
        if Item == True:
            Count+=1
    return Count

Boards = []
Board = []
i = 1
for j in range(0,int((len(Input)-1)/6)):
    Board, i = CreateBoard(Input,i)
    Boards.append(Board)
    i+=1

BoardStates = [False]*len(Boards)

WinningBoard = []
Loser = False
Winner = False
LastBoard=0
NoOfWon = 0
for i in range(0,len(Draw)):
    Winner = False
    Boards = TakeTurn(Draw,i,Boards)
    for j in range(0,len(Boards)):
        BoardState=CheckWin(Boards[j])
        if BoardState:
            BoardStates[j] = True
    NoOfWon = CheckBoardStates(BoardStates)
    if NoOfWon == len(Boards)-1:
        for k in range(0,len(BoardStates)):
            if BoardStates[k] == False:
                LastBoard = k
    if NoOfWon == len(Boards):
        Loser = True
        WinningBoard = Boards[LastBoard]
    if Loser:
        break

print(WinningBoard)
Score = CheckScore(WinningBoard)
print(Score)
print(Draw[i])
print(Score*int(Draw[i]))

Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(int(line))

Increased = 0
Decreased = 0

SlidingDoor = []

for i in range(0,len(Input)-2):
    Door = Input[i]+Input[i+1]+Input[i+2]
    SlidingDoor.append(Door)

for i in range(1,len(SlidingDoor)):
    if SlidingDoor[i] > SlidingDoor[i-1]:
        Increased+=1
    elif SlidingDoor[i] < SlidingDoor[i-1]:
        Decreased+=1

print(Increased,Decreased)

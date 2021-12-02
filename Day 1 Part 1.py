Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(int(line))

Increased = 0
Decreased = 0

for i in range(1,len(Input)):
    if Input[i] >= Input[i-1]:
        Increased += 1
    elif Input[i] < Input[i-1]:
        Decreased += 1    

print(Increased,Decreased)

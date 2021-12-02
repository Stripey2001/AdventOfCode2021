Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
print(Input)

Horizontal = 0
Vertical = 0
Aim = 0

for i in range(0,len(Input)):
    if Input[i][0] == "f":
        Horizontal += int(Input[i][-2])
        Vertical += int(Input[i][-2])*Aim
    elif Input[i][0] == "u":
        Aim -= int(Input[i][-2])
    else:
        Aim += int(Input[i][-2])

print(Horizontal)
print(Vertical)
print(Horizontal*Vertical)

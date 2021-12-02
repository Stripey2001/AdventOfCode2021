Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
print(Input)

Horizontal = 0
Vertical = 0

for i in range(0,len(Input)):
    if Input[i][0] == "f":
        Horizontal += int(Input[i][-2])
    elif Input[i][0] == "u":
        Vertical -= int(Input[i][-2])
    else:
        Vertical += int(Input[i][-2])

print(Horizontal)
print(Vertical)
print(Horizontal*Vertical)

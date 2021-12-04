Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)

Bits = [0]*(len(Input[0])-1)

print(Bits)

for Line in Input:
    for i in range(0,len(Bits)):
        if Line[i] == "1":
            Bits[i] += 1

print(Bits)

Gamma = ""
Epsilon = ""

for Bit in Bits:
    if Bit > (len(Input)/2):
        Gamma = Gamma + "1"
        Epsilon = Epsilon + "0"
    else:
        Gamma = Gamma + "0"
        Epsilon = Epsilon + "1"

print(Gamma,Epsilon)
print(int(Gamma,2),int(Epsilon,2))
print(int(Gamma,2)*int(Epsilon,2))

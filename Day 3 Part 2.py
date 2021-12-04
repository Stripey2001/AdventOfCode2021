Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
 
ConstInput = Input
for i in range(0,len(Input[0])-1):
    TempInput = []
    Bit = 0
    OGR = "0"
    for j in range(0,len(Input)):
        if Input[j][i] == "1":
            Bit += 1
    if Bit >= (len(Input)/2):
        OGR = "1"
    for Line in Input:
        if Line[i] == OGR:
            TempInput.append(Line)
    Input = TempInput
    #print(Input)
    if len(Input) == 1:
        break

OxygenGenRating = Input[0]

Input = ConstInput
for i in range(0,len(Input[0])-1):
    TempInput = []
    Bit = 0
    CSR = "1"
    for j in range(0,len(Input)):
        if Input[j][i] == "1":
            Bit += 1
    if Bit >= (len(Input)/2):
        CSR = "0"
    for Line in Input:
        if Line[i] == CSR:
            TempInput.append(Line)
    Input = TempInput
    #print(Input)
    if len(Input) == 1:
        break

C02ScrubRating = Input[0]

print(OxygenGenRating,C02ScrubRating)
print(int(OxygenGenRating,2),int(C02ScrubRating,2))
print(int(OxygenGenRating,2)*int(C02ScrubRating,2))

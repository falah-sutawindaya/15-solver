def openandformat():
    k=[]
    f = open('berkasteks.txt', 'r')
    d = f.read().split("\n")
    print(d)
    for elemen in d:
        k.append(elemen.split(" "))
    print(k)
    for i in range(0,len(k)):
        for j in range(0,len(k)):
            if (k[i][j] == ''):
                k[i][j] = '0'
            if (int(k[i][j]) < 10):
                k[i][j] = '0' + k[i][j]
    return k

def printFormat(k):
    for el in k:
        print(el)

def cost(soal):
    salah = []
    for i in soal:
        for j in i:
            salah.append(int(j))

    # print(salah)
    sum=0
    for i in range(0,16):
        if (salah[i] != i+1):
            if (salah[i]!=0):
                sum+=1
    return sum

def generatemove(soal):
    move = {
        0:[1,4], 1:[0,2,5], 2:[1,3,6], 3:[2,7],
        4:[0,5], 5:[1,4,6,9], 6:[2,5,7,10], 7:[3,6,11],
        8:[4,9,12], 9:[5,8,10,13], 10:[6,9,11,14], 11:[7,10,15],
        12:[8,13], 13:[9,12,14], 14:[10,13,15], 15:[11,14]
    }
    salah = []
    for i in soal:
        for j in i:
            salah.append(int(j))
    # print(salah)
    return move[salah.index(0)]

def gerak(kesitu):
    lurus = []
    for i in soal:
        for j in i:
            lurus.append(int(j))
    temp = lurus[kesitu]
    lurus[lurus.index(0)] = temp
    lurus[kesitu] = 0
    print("sesudah: ")
    print(lurus) 
    return lurus

soal = openandformat()
printFormat(soal)

totalSalah = cost(soal)
print(totalSalah)
print("===========")
print(generatemove(soal))

lurus = []
for i in soal:
    for j in i:
        lurus.append(int(j))

print(lurus)



# for i in range(0,4):
#     for j in range(0,4):



moveMemory = None












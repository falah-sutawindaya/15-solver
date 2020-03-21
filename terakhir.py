def openandformat():
    k=[]
    f = open('salah.txt', 'r')
    d = f.read().split("\n")
    # print(d)
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

def costLurus(lurus):
    sum=0
    for i in range(0,16):
        if (lurus[i] != i+1):
            if (lurus[i]!=0):
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

def formatSoal(lurus):
    new = []
    for i in range(0,4):
        new.append([])
    for i in range(0,4):
        new[0].append(str(lurus[i]))
        new[1].append(str(lurus[i+4]))
        new[2].append(str(lurus[i+8]))
        new[3].append(str(lurus[i+12]))
    for i in range(0,4):
        for j in range(0,4):
            if (int(new[i][j])<10):
                new[i][j]='0'+str(new[i][j])
    # bidak
    for i in new:
        print(i)
    return new

def isGoal(lurus):
    goal_node=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    for i in range(0,len(goal_node)):
        if (lurus[i]!=goal_node[i]):
            return False
    return True


# Import dari Text tetapi format String
soal = openandformat()
print(soal)

# print horizontal
printFormat(soal)

# liat cost posisi terbaru
totalSalah = cost(soal)
# print(totalSalah)

print("============================================")
print(generatemove(soal)) 
# for i in generatemove(soal):
#     print(cost())
lurusdancost = {}
count=0
for i in generatemove(soal):
    formatSoal(gerak(i))
    print(costLurus(gerak(i)))
    lurusdancost[count] = [gerak(i),costLurus(gerak(i))]
    count+=1
# lastPosition = None
print(lurusdancost)












def openandformat():
    k=[]
    f = open('coba.txt', 'r')
    d = f.read().split("\n")
    # print(d)
    for elemen in d:
        k.append(elemen.split(" "))
    # print(k)
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

def gerak(kesitu, soal):
    lurus = []
    for i in soal:
        for j in i:
            lurus.append(int(j))
    temp = lurus[kesitu]
    lurus[lurus.index(0)] = temp
    lurus[kesitu] = 0
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
    return new
# def formatSoal(lurus):
#     new = []
#     luruszero = lurus
#     for i in range(0,len(luruszero)):
#         if luruszero[i] < 10:
#             luruszero[i] = '0' + str(luruszero[i])
#         else:
#             luruszero[i] = str(luruszero[i])
#     for i in range(0,4):
#         new.append([])
#     for i in range(0,4):
#         new[0].append(luruszero[i])
#         new[1].append(luruszero[i+4])
#         new[2].append(luruszero[i+8])
#         new[3].append(luruszero[i+12])
#     print(new)
#     return new


def ilanginLast_move(generated, last_move):
    if last_move == None:
        return generated
    elif last_move not in generated:
        return generated
    else:
        generated.remove(last_move)
        return generated

def isGoal(lurus):
    goal_node=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    for i in range(0,len(goal_node)):
        if (lurus[i]!=goal_node[i]):
            return False
    return True

def bikinLurus(soal):
    lurus = []
    for i in soal:
        for j in i:
            lurus.append(int(j))    
    return lurus


# ============================================= INISIASI =============================================
# Import dari Text tetapi format String
soal = openandformat()

# print horizontal
printFormat(soal)
print("============================================")
perubahan = soal


# ============================================= ALGORITMA =============================================
last_move = None 
while (not isGoal(bikinLurus(perubahan))):
    try: 
        # Jejak Pergerakan Node 
        # Mencari Pergerakan Node yang Mungkin [2,5,7,10] dan memasukannya ke Objek of Kemungkinan {[lurus], [lurus], [lurus]}
        lurusdancost = {}
        kurang={}
        count=0
        print(ilanginLast_move(generatemove(perubahan), last_move))
        for i in ilanginLast_move(generatemove(perubahan), last_move):
            formatSoal(gerak(i,perubahan))
            # print(costLurus(gerak(i, perubahan))) 
            print(costLurus(gerak(i, perubahan)))
            kurang[count] = costLurus(gerak(i, perubahan))
            lurusdancost[count] = [gerak(i, perubahan), costLurus(gerak(i, perubahan))]
            count+=1

        # Hasil Objek of Kemungkinan adalah lurus dan cost
        print(lurusdancost)
        last_move = bikinLurus(perubahan).index(0)

        # Mencari Node dengan Least Cost Search (NextMoveLurus = [lurus])
        nextMoveLurus = None
        min = lurusdancost[0][1]
        if (len(lurusdancost) == 1):
            nextMoveLurus = lurusdancost[0][0]
        else:
            for k, v in lurusdancost.items():
                if (v[1] < min):
                    min = v[1]
                    nextMoveLurus = v[0]
        
        perubahan = formatSoal(nextMoveLurus)
        printFormat(perubahan)
    except TypeError:
        print("")
        print("tidak bisa di selesaikan b&b")
        break









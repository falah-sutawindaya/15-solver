import time

def openandformat(namaFile):
    k=[]
    f = open(namaFile, 'r')
    d = f.read().split("\n")
    for elemen in d:
        k.append(elemen.split(" "))
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
        4:[0,5,8], 5:[1,4,6,9], 6:[2,5,7,10], 7:[3,6,11],
        8:[4,9,12], 9:[5,8,10,13], 10:[6,9,11,14], 11:[7,10,15],
        12:[8,13], 13:[9,12,14], 14:[10,13,15], 15:[11,14]
    }
    salah = []
    for i in soal:
        for j in i:
            salah.append(int(j))
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

def kurang(i, lurus):
    lurus_temp = lurus.remove(0)
    tot=0
    for x in range(i,len(lurus)):
        if lurus[i]>lurus[x]:
            tot+=1
    return tot

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

def printJumlahKurangdanX():
    posisi = {}
    X = None
    jumlahKurang=0
    for i in range(0,len(bikinLurus(soal))):
        if (bikinLurus(soal)[i] == 0):
            print('Posisi '+ str(i+1) + ': ' + 'Node Kosong')
            X = i+1
        else:
            posisiKe = 'Posisi '+ str(i+1)
            posisi[posisiKe] = kurang(i,bikinLurus(soal))
            jumlahKurang+=kurang(i,bikinLurus(soal))

    print('Kurang pada setiap posisi: ' + str(posisi))
    print('Jumlah kurang(i) + X =  ' + str(jumlahKurang+X))
    

def algo(solusi):
    start_time = time.time()
    perubahan = soal
    last_move = None 
    jumlahSimpul=1
    ada_solusi=True
    while (not isGoal(bikinLurus(perubahan))):
        try: 
        # Jejak Pergerakan Node 
        # Mencari Pergerakan Node yang Mungkin [2,5,7,10] dan memasukannya ke Objek of Kemungkinan {[lurus], [lurus], [lurus]}
            lurusdancost = {}
            count=0
            for i in ilanginLast_move(generatemove(perubahan), last_move):
                formatSoal(gerak(i,perubahan))
                lurusdancost[count] = [gerak(i, perubahan), costLurus(gerak(i, perubahan))]
                count+=1
                jumlahSimpul+=1

            # Hasil Objek of Kemungkinan adalah lurus dan cost
            last_move = bikinLurus(perubahan).index(0)

            # Mencari Node dengan Least Cost Search (NextMoveLurus = [lurus])
            nextMoveLurus = None
            min = lurusdancost[0][1]
            nextMoveLurus = lurusdancost[0][0]    
            if (len(lurusdancost) == 1):
                nextMoveLurus = lurusdancost[0][0]
            else:
                count_same=0
                for k, v in lurusdancost.items():
                    if (v[1] < min):
                        min = v[1]
                        nextMoveLurus = v[0]
                for k, v in lurusdancost.items():
                    if (v[1] == min):
                        count_same+=1
            
            if (count_same > 1):
                print("")
                print("tidak bisa di selesaikan b&b")
                ada_solusi = False
                break
            
            perubahan = formatSoal(nextMoveLurus)
            solusi.append(nextMoveLurus)
        except TypeError:
            print("")
            print("tidak bisa di selesaikan b&b")
            break

    waktu = " %s seconds " % (time.time() - start_time)
    if (ada_solusi):
        print("Langkah-Langkah: ")
        for i in solusi:
            for j in formatSoal(i):
                print(j)
            print("============================================")
    
    
    print('')
    print('Jumlah simpul di bangkitkan: ' + str(jumlahSimpul))
    print('waktu eksekusi: '+waktu)

# ============================================= INISIASI =============================================
# Import dari Text tetapi format String
soal = openandformat("instansiasi.txt")

# print horizontal & informasi
print("============================================")
print("Matriks Posisi Awal: ")
printFormat(soal)
print("")
print("============================================")
print("informasi: ")
solusi=[]
printJumlahKurangdanX()
print("============================================")
print("")

# ============================================= ALGORITMA =============================================
algo(solusi)





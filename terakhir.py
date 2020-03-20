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

soal = openandformat()
printFormat(soal)

totalSalah = cost(soal)
print(totalSalah)

moveMemory = None












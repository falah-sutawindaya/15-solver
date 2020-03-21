def ilanginLast_move(generated, last_move):
    if last_move == None:
        return generated
    elif last_move not in generated:
        return generated
    else:
        return generated.remove(last_move)
    
def formatSoal(lurus):
    new = []
    luruszero = lurus
    lurus = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in range(0,len(luruszero)):
        if luruszero[i] < 10:
            luruszero[i] = '0' + str(luruszero[i])
        else:
            luruszero[i] = str(luruszero[i])
    for i in range(0,4):
        new.append([])
    for i in range(0,4):
        new[0].append(luruszero[i])
        new[1].append(luruszero[i+4])
        new[2].append(luruszero[i+8])
        new[3].append(luruszero[i+12])
    print(new)
    return new



# lurus = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# formatSoal(lurus)

b = {0: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15], 2], 1: [[1,2], 3]}
print(len(b))

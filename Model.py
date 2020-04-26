#reading the chip sequences from Stations.txt file

def bit_seq():
    y, a, b, c, d = [], [], [], [], []
    bit_sequence = open("Data.txt", "r")
    file = bit_sequence.readlines()
    for i in range(1,5):
        info = file[i]
        x = info.split(", ")
        for j in x:
            y.append(int(j))
        if i == 1:
            a = y.copy()
        if i == 2:
            b = y.copy()
        if i == 3:
            c = y.copy()
        if i == 4:
            d = y.copy()
        y = []
    return a,b,c,d


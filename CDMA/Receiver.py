# obtains the chip sequence of the station which the receiver listens
def chip_assignment(listen):
    chip = []
    if listen == "a": info = file[1]
    elif listen == "b": info = file[2]
    elif listen == "c": info = file[3]
    elif listen == "d": info = file[4]
    else: print("Check the \"receive.txt\" file, Enter station you want to listen correctly, e.g., \"a\" or \"b\" or \"c\" or \"d\" ")
    info = info.strip(); info = info.split(", ")
    for i in info:
        chip.append(int(i))
    return chip

#calculates the normalized innner product of sequence S and the station receiver wants to listen to
def inner_product(chip):
    sum = 0; S = []; Seq = file[8]; Seq = Seq.strip(); Seq = Seq.split(", ")
    for i in Seq:
        S.append(int(i))
    for j in range(len(chip)):
        sum += chip[j]*S[j]
    return sum/8

bit_sequence = open("receive.txt", "r")
file = bit_sequence.readlines()
listen = file[6]; listen = listen.strip(); listen = listen.lower()

if listen.isalpha() is True: chip = chip_assignment(listen)
else: print("Check the \"receive.txt\" file, Enter station you want to listen correctly, e.g., \"a\" or \"b\" or \"c\" or \"d\" ")

in_prod = inner_product(chip)

if in_prod == 1: print("Station " + listen + " sent bit 1")
elif in_prod == -1: print("Station " + listen + " sent bit 0")
elif in_prod == 0: print("Station " + listen + " is not active, so no bit is received")
else: print("Error! Enter the data in 'receive.txt' and trans.txt in correct format")
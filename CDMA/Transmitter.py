#checks pairwise orthogonality of chip sequences
def Walsch():
    chip_list1 = []
    def chip_func(i):
        chip = []
        info = file[i]
        info = info.strip("\n");
        info = info.strip();
        info = info.split(", ")
        for j in info:
            chip.append(int(j))
        return chip
    for i in range(4):
        x = chip_func(i + 1)
        chip_list1.append(x)
    #checks auto correlation, S (inner product) S = 1
    for j in range(len(chip_list1)):
        sum = 0
        for i in chip_list1[j]:
            sum += i*i
        sum /=8
        if sum == 1:
            pass
    #check cross co-relation

    i = 0
    while(i < 3):
        for k in range(i+1,len(chip_list1)):
            sum =0
            for m in range(8):
                sum += chip_list1[i][m]*chip_list1[k][m]
            sum = sum / 8
            if sum == 0:
                pass
            else:
                print("Check Chip sequence " + str([i+1]) + " and"+ str([k+1]) + " as they are not orthogonal")

        i +=1

#returns the chip sequence of each active station
def bit_seq(stn_name):
    chip = []
    if stn_name == "a": info = file[1]
    elif stn_name == "b": info = file[2]
    elif stn_name == "c": info = file[3]
    elif stn_name == "d": info = file[4]
    else: print("Check the \"trans.txt\" file, Enter stations in the following format only (lowercase), e.g., \"a, b, d\" or \"a, c \" ")
    info = info.strip(); info = info.split(", ")
    for i in info:
        chip.append(int(i))
    return chip

#returns the negation of a chip sequence, if 0 is transmitted by a station
def not_gate(valu):
    neg_seq = []
    for i in valu:
        if i == -1: neg_seq.append(+1)
        elif i == 1: neg_seq.append(-1)
        else: print("Check the \"trans.txt\" file, & Enter Code Sequence for Stations in correct format")
    return neg_seq

#obtains the chip sequence of each station
def  transmit():
    #reads the stations which are active
    stn_activ = file[6]
    stn_activ = stn_activ.casefold(); stn_activ = stn_activ.strip(); stn_activ = stn_activ.split(", ")

    #reads the bit transmitted by each station
    stn_bit_str = file[9]
    stn_bit_str = stn_bit_str.strip(); stn_bit_str = stn_bit_str.split(", ")

    #stores the chip sequence for each station
    chip_seq = []
    if len(stn_activ) == len(stn_bit_str):
        for i in range(len(stn_activ)):
            if stn_bit_str[i] == "1":
                chip_seq.append(bit_seq(stn_activ[i]))
            elif stn_bit_str[i] == "0":
                chip_seq.append(not_gate(bit_seq(stn_activ[i])))
            else:
                print("Please check the \"trans.txt\" file, & enter the input in the correct format")
    return(chip_seq)

#calculate the value S, i.e., linear addition of the individual chip sequence of active stations
def sum_seq(chip_seq):
    S=[]; i = 0
    while i < len(chip_seq[0]):
        sum = 0
        for j in range(len(chip_seq)):
            sum += chip_seq[j][i]
        S.append(sum)
        i +=1
    return  S

#transmits S (code for the receiver to receive)
def transmit_S(S):
    S = str(S); S = S.replace('[',''); S = S.replace(']','');
    S = S +'\n'

    #store the sequence in transmitter, at trans.txt
    file[11] = S
    bit_sequence = open("trans.txt", "w")
    bit_sequence.writelines(file)
    bit_sequence.close()

    #transmit the sequence S to reciever, i.e., write to receive.txt
    bit_sequence1 = open("receive.txt", "r")
    file1 = bit_sequence1.readlines()
    file1[8] = S
    bit_sequence1 = open("receive.txt", "w")
    bit_sequence1.writelines(file1)
    bit_sequence1.close()

bit_sequence = open("trans.txt", "r")
file = bit_sequence.readlines()
Walsch()
chip_seq = transmit()
S = sum_seq(chip_seq)
transmit_S(S)
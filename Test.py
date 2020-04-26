import Model
a,b,c,d = Model.bit_seq()

y = []
x = []
y.append(a)
y.append(b)
y.append(c)
y.append(d)
#-------

#------------
j = 0
#print(y)
def walsch_code(a,b,c,d):
    y = []
    y.append(a); y.append(b); y.append(c); y.append(d)
    for each_sequence in y:
        for j in y:
            while j != each_sequence:
                for k in j:
                    sum1 = (sum1 + k * k)
                sum1 = sum1 / 8
                print(sum1)
walsch_code(a,b,c,d)

'''sum = 0
        sum1 = 0
        # check inner product of each chip sequence with itself = 1
        for i in each_sequence:
            sum = (sum + i*i)
        sum = sum/8
        print(sum)'''

for each_sequence in y:
    for j in y:
        while j != each_sequence:
            sum1=0
            # check inner product of each chip sequence with another = 0
            m = 0
            for l in each_sequence:
                sum1 = sum1 + l*m
                m += 1
            sum1 = sum1 / 8
            print(sum1)

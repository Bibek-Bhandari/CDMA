bit_sequence = open("Data.txt", "r")
file = bit_sequence.readlines()


def evalu(valu):
  x = [1,1,1,1,1]
  y = [1,2,3,4,5,6]
  z = [1,5,6,7,8,433333]
  retd = []
  if valu == "a":
    retd = x
  elif valu == "c":
    retd = z
  else:
    retd = y
  return retd


stn_activ = file[6]
stn_activ.lower();
stn_activ.strip();
stn_activ = stn_activ.split(", ")

# reads the bit transmitted by each station
stn_bit_str = file[9]
stn_bit_str.strip();
stn_bit_str = stn_bit_str.split(", ")

chip_seq = []

for i in range(len(stn_activ)):
    x = stn_activ[i]
    y = evalu(x)
    chip_seq.append(y)

print(chip_seq)
#--------
print("from here")
print(stn_activ[-1])
stn_bit_str[-1] = stn_bit_str[-1].strip('\n')
print(stn_activ[-1])
n = len(stn_activ)
for i in range(n):
    print(stn_bit_str[i])
    print("Loop no.", i)
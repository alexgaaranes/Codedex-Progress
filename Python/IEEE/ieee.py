

while(True):
    str_num = input("Enter 32-bit floating point number: ");
    if len(str_num) == 32:
        break
    else:
        print("Please enter a 32-bit binary string!")

# Get the parts
sign_bit = int(str_num[0])

str_exp = str_num[1:9]
str_mant = str_num[9:]

# Convert the string to decimal
exp = 0
for i in range(len(str_exp)):
    exp += 2**(len(str_exp)-i-1) * int(str_exp[i])
exp = exp - 127

#print(str_exp + " " + str_mant)

# Get the mantissa x base^exp
if exp >= 0:
    str_frac = str_mant[exp:]
    str_whole = "1" + str_mant[:exp]
else:
    str_whole = "0"
    str_frac = "1"+str_mant

#print(str_whole+"."+str_frac)

# Convert the binary to whole
whole = 0
frac = 0
for i in range(len(str_whole)):
    #print(str_whole[-1*(i+1)]+ " = " + str(2**(i)))
    whole += 2**(i) * int(str_whole[-1*(i+1)])

for i in range(len(str_frac)):
    frac += 1/(2**(i+1)) * int(str_frac[i])

print("Result: ",(-1*int(sign_bit))*(float(whole)+frac))



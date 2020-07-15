'''
Exemplo: 

  1         1        0        1
1*2^3     1*2^2     0*2^1   1*2^0

8 + 4 + 0 + 1 = 13
'''

def bin_to_dec (num):
    j = 0
    dec = 0
    for i in reversed(num):
        dec += int(i) * (2 ** j) 
        j += 1
    return dec

num = input("Digite o valor em binário: ")

print(bin_to_dec(num))

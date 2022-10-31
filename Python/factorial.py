#!/usr/local/bin/python3.6
# try number 2 at factorial
from decimal import Decimal

factorial = input("Please give a number to factor: ")
factorial = int(factorial)
sum = 1

halfF = factorial / 2
halfF = int(halfF + 1)
m = []
for i in range(1, halfF):
    j = factorial - i
    s = j * i
    m.append(s)
    print(i, "*", j, "=", s)
    sum *= s
sum *= 2
print(sum)
print(m)

# for i in range(1,len(m)+1):
#	print(m[i-1],"\t",i*50,"\t",i*50)

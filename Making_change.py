import math

Total = input("Enter dollar deposit here: ")
fltotal = round(float(Total), 2)
Totalcents = fltotal * 100

print(Totalcents)

t = 200
l = 100
q = 25
d = 10
n = 5
p = 1

Tam = Totalcents//t
Lam = (Totalcents-Tam * t)//l
Qam = (Totalcents-(Tam * t)-(Lam * l))//q
Dam = (Totalcents-(Tam * t)-(Lam * l)-(Qam * q))//d
Nam = (Totalcents-(Tam * t)-(Lam * l)-(Qam * q)-(Dam * d))//n
Pam = (Totalcents-(Tam * t)-(Lam * l)-(Qam * q)-(Dam * d)-(Nam * n))//p

T = "toonies"
L = "loonies"
Q = "quarters"
D = "dimes"
N = "nickels"
P = "pennies"
space = " "
a = str(Tam)
b = str(Lam)
c = str(Qam)
d = str(Dam)
e = str(Nam)
f = str(Pam)
print(a + space + T + space + b + space + L + space + c + space + Q + space + d + space + D + space + e + space + N + space + f + space + P)
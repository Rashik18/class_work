G = 6.673*10**-11
M = 5.97*10**24
R = 6371
T = float(input("enter time:"))
h = ((G*M*T*T)/(4*3*1416*3.1416))**(1/3)-R
print("The Altitude of the Satellite is:",h)


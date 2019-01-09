'''For a satellite, orbiting around the earth with a time period, T,
we know that
h =((GMT^2/4(pi)^2)^(1/3))-R

Where G = 6.67x10e-11
M = 5.97x1024kg and

R = 6371km
I Write a program to calculate the altitude of a satellite for the
input time period.'''



G = 6.673*10**-11
M = 5.97*10**24
R = 6371
T = float(input("enter time:"))
h = ((G*M*T*T)/(4*3*1416*3.1416))**(1/3)-R
print("The Altitude of the Satellite is:",h)


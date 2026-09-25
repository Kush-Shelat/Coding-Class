num = int(input("enter the number : "))
t = num
numlen = 5

while t>0:
    numlen = numlen+1
    t = int(t/10)

if numlen>=4:
    numlen = int(numlen/2)
    
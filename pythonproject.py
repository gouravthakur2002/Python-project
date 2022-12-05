
def isLeap(a):
    if (a % 400 == 0):
        return 1
    if a % 100 != 0 :
        if a % 4 == 0:
            return 1
        return 2
    else:
        return 2
a=input("Enter first date\nIn (DD/MM/YYYY: ")
b=input("Enter second date\nIn (DD/MM/YYYY: ")
c=int(a[6:])
d=int(b[6:])
leapyears=''
nonleapyears=''
for i in range(c,d+1):
    s=isLeap(i)
    if (s==1):
        leapyears=leapyears+str(i)+','
    else:
        nonleapyears=nonleapyears+str(i)+','
leapyears=leapyears[0:len(leapyears)-1]
print("Leap years are:")
print(leapyears)
nonleapyears=nonleapyears[0:len(nonleapyears)-1]
print("Non Leap Years are:")
print(nonleapyears)

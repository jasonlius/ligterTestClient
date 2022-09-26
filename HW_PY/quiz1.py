def isSmallPal(n):
    n =abs(n)
    if(type(n)!=int and (n<1000 and n>9999)):
        return False
    thuDig = n//1000
    hunDig = (n-(thuDig*1000))//100
    tenDig = (n-(thuDig*1000)-(hunDig*100))//10
    oneDig = n % 10
    if(oneDig*1000+tenDig*100+hunDig*10+thuDig == n):
        return True
    else:
        return False
print(isSmallPal(1234))
print(isSmallPal(43234423))
print(isSmallPal(1221))
print(isSmallPal(1122))
print(isSmallPal(12424))
print(isSmallPal(1234))
print(isSmallPal(1234))
print(isSmallPal(-1221))

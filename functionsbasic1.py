#1
#I predict it will output 5
def a():
    return 5
print(a())

#2
#I predict it will output 10
def a():
    return 5
print(a()+a())

#3
#I predict it will output 5
def a():
    return 5 
    return 10
print(a())

#4 
#I predict it will output 5
def a(): 
    return 5
    print(10)
print(a())

#5 
#I predict it will output 5 and say x is undefined.
def a():
    print(5)
x = a()
print(x) 

#6 
#I predict it will output 3, 5, then 8
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7 
#I predict it will output 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 
#I predict it will output 100, 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9 
#I predict it will output 7, 14, 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10
#I predict it will output 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
#I predict it will output 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12
#I predict it will output 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13
#I predict it will output 500, 500, 300, 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
#I predict it will output 1, 3, 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
#I predict it will output 1, 3, 5, 10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)















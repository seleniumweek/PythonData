
def greet():
    print("hello")
greet()

def add(num1, num2):
    sum = num1+num2
    print(sum)    

add(22,32)

def squareroot(num):
    root = num * num
    return root

value = squareroot(5)
print(value)

for i in [1,2,3,4]:
    result = squareroot(i)
    print(result)

def findsum(*number):
        results = 0
        for n in number:
            results = n * n
        print(results)

findsum(2,3,4,5,6)

def fact(x):
    if x == 1:
        return 1
    else:
        return(x * fact(x-1))

print("Factorial numer is: ",fact(4))       

add = lambda val:val+4
print(add(2))

add = lambda val1, val2:val1+val2
print(add(2,3))
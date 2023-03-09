
words = ["Apple","Orange","Banana","Kiwi"]
for word in words:
    print("Actual word is: "+word)
    for letter in word:
        print("Letters are: "+letter)
         
for x in range(5):
    print(x)

for y in range(1,20,5):
    print(y)  

isSix = False
for num in range(2,10,2):
              if num == 6:
                isSix = True
                break
print("issix contains: ", isSix)            


count = 0
highestcount = 5
while  count <= highestcount:
    print("current coiunt is: ", count)
    count +=1
else:
    print ("while end")   

number = 0
if number ==0:
    print("number is zero")
elif number < 0:
    print("number is below zero ")
else:
    print("number is above zero")


newnum = 6
if newnum <= 0:
    if newnum == 0:
        print("zero")
    else:
        print("not zero")
elif(newnum >= 0):
    print("greater than zero")
else:
    print("Negitive nuber")   

 

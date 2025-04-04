
count=0
for number in range(1,21):
 if number % 2==0:
    count+=number
print(count)



#i = 1
#for t in range(1,6):
 # print(i * '*')
  #i+=1



for numbers in range(1,6):
    for i in range (1,6):
        i *=numbers
        print(i,end=' ')
    print()
  

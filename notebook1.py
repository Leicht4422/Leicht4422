name = input('name' )
print('my', 'name', 'is', name )

val1 = int(input("enter value1"))
val2 = int(input("enter value2"))

val3 = val1 * val2
print(val3)

#create a list variable
numbers = []
#iterate request 5 times for the list size
for i in range(0, 5):
    print('enter no at yr loc', i , ":")
    #accept float no from user
    item = float(input())
    #add no received frm input
    numbers.append(item)
    
print(numbers)

num = 5895.455656
#using %.nf n for decimal  place
print('%.2f' % num)
print('%.0f' % num)

value = 8
#0 reps the data stored in var value under the function str,format()
print('octal value of 8 is {0:o}'.format(value))

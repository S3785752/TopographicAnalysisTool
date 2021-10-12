minimum = input('enter the minimum value = ' )


maximum = input('enter the maximum value = ' )   


numClasses = input('enter the number of classes = ' )


classBlocks = ( float(maximum) - float(minimum) ) / float(numClasses)

print('******the following are the class breaks******')

# calculation of the classes 

n = 0
 
for i in range(int(numClasses)):
    row1 = str(minimum) + ' thru ' + str((float(minimum) - 0.0001 + classBlocks)) + ' = ' + str(n + 1)
    print(row1)
    n = n + 1
    minimum = float(minimum) + float(classBlocks)
    rowFinal = '* = NULL'
    if n == int(numClasses):
        print(rowFinal)
    





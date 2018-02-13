set1works = False
set2works = False

while (set1works == False): #Loops until the user enters a valid set
    set1 = str(input('Please enter the first set, surrounded by curly braces and separated by commas: {1,2,3}\n'))
    if ((set1[0]=='{') & (set1[-1]=='}')): #Checks to make sure the set is valid
        set1 = set1[1:-1] #Removes the curly braces from the set
        set1arr = set1.split(',') #Splits the set into an array
        set1works = True
    else:
        print("That input was not a valid set")

while (set2works == False):
    set2 = str(input('Please enter the second set, surrounded by curly braces and separated by commas: {4,5,6}\n'))
    if ((set2[0]=='{') & (set2[-1]=='}')):
        set2 = set2[1:-1]
        set2arr = set2.split(',')
        set2works = True
    else:
        print("That input was not a valid set")

result = []
i=0
for x in range(0, len(set1arr)):
    for y in range(0, len(set2arr)):
        result.append([set1arr[x],set2arr[y]]) #Fills result with the product of the two sets
        i+=1

print("{", end='')
for x in range(0, len(set1arr)):
    for y in range(0, len(set2arr)):
        if ((x!=0) | (y!=0)):
            print(",", end='')
        print("{" + set1arr[x] + "," + set2arr[y] + "}", end='') #Prints the resulting set as a product of two sets
print("}", end='')

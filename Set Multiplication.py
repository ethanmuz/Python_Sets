set1works = False;
set2works = False;
while (set1works == False):
    set1 = str(input('Please enter the first set, surrounded by curly braces and separated by commas: {1,2,3}\n'));
    if ((set1[0]=='{') & (set1[-1]=='}')):
        set1 = set1[1:-1];
        set1arr = set1.split(',');
        set1works = True;
    else:
        print("That input was not a valid set");
while (set2works == False):
    set2 = str(input('Please enter the second set, surrounded by curly braces and separated by commas: {4,5,6}\n'));
    if ((set2[0]=='{') & (set2[-1]=='}')):
        set2 = set2[1:-1];
        set2arr = set2.split(',');
        set2works = True;
    else:
        print("That input was not a valid set");

print(set1arr);
print(set2arr);

result = [];
i=0;
print(len(set1arr));
print(len(set2arr));
for x in range(0, len(set1arr)):
    for y in range(0, len(set2arr)):
        print(str(x) + " " + str(y));
        result.append([set1arr[x],set2arr[y]]);
        i+=1;
print(result);

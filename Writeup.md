# Python Sets

#### February 7, 2018

The sets I'm working with in Python, we learned about in Discrete Math. The main aspect that interested me is set multiplication, where {1,2,3} x {4,5,6} = {{1,4},{1,5},{1,6},{2,4},{2,5},{2,6},{3,4},{3,5},{3,6}}.

This was interesting to me because my professor discussed set multiplication using two sets, but never talked about it if there were more than two sets to be multiplied. I thought it would be cool to write a python program to see what it would look like if I multiplied three, four, five, etc. sets together.

I plan on including other functions soon too, such as union of sets, intersection of sets, difference of sets, and more.

I don't remember much python, but once I start using it I will start to get the hang of it again. I also have never used python from the command line, so I will need to learn that too.

So after a Google search, it turns out python from the command line is way simpler than I thought it would be. I literally just use the command "python file.py" and it will compile and run the program. Cool!

I also had to bring up a "Beginning Python" tutorial while doing this, because I forgot most of the python syntax.

I started testing with printing a line to see if command-line Python worked the way I thought it would:

```python
print("test")
```

It worked, so I wrote the following code, that was supposed to take a set from input and then strip the curly braces and split the elements into an array. I figured the code would just end up being pseudocode, since the Python syntax was still fuzzy in my head.

```python
bool set1works = false
bool set2works = false
set1arr[]
set2arr[]
while (set1works == false): #Loops until the user enters a valid set
    set1 = str(input('Please enter the first set, surrounded by curly braces and separated by commas: {1,2,3}'))
        if (set1[0]=='{' & set1[-1]=='}'): #Checks to make sure the set is valid
            set1 = set1[1:-1] #Removes the curly braces from the set
            set1arr = set1.split(',') #Splits the set into an array
            set1works = true
        else:
            print("That input was not a valid set")
while (set2works == false):
    set2 = str(input('Please enter the second set, surrounded by curly braces and separated by commas: {4,5,6}'))
    if (set2[0]=='{' & set2[-1]=='}'):
        set2 = set2[1:-1]
        set2arr = set2.split(',')
        set2works = true
    else:
        print("That input was not a valid set")

print(set1arr)
print(set2arr)
```

This particular code gave me some errors: turns out I forgot you don't have to initialize any variables, and boolean values (true or false) need to be capitalized. Other than this, I had to separate my if statement condition with parentheses. After fixing these errors: here is what the code looks like:

```python
set1works = False
set2works = False
while (set1works == False): #Loops until the user enters a valid set
   set1 = str(input('Please enter the first set, surrounded by curly braces and separated by commas: {1,2,3}'))
    if ((set1[0]=='{') & (set1[-1]=='}')): #Checks to make sure the set is valid
        set1 = set1[1:-1] #Removes the curly braces from the set
        set1arr = set1.split(',') #Splits the set into an array
        set1works = True
    else:
        print("That input was not a valid set")
while (set2works == False):
    set2 = str(input('Please enter the second set, surrounded by curly braces and separated by commas: {4,5,6}'))
    if ((set2[0]=='{') & (set2[-1]=='}')):
        set2 = set2[1:-1]
        set2arr = set2.split(',')
        set2works = True
    else:
        print("That input was not a valid set")

print(set1arr)
print(set2arr)
```

Now the plan is to multiply these two sets. I am going to try to create an array of subarrays, and each subarray will be an element of the product set. The pseudocode for this plan looks like this:

```
i=0
for every element in set1:
    for every element in set2:
        array[i] = [set1 element, set2 element]
        i++
```

We'll see if this works. Here is the python code for this attempt:

```python
i=0
for x in range(0, len(set1arr)):
    for y in range(0, len(set2arr)):
        result[i]=[set1arr[x],set2arr[y]]
        i+=1
print(result)
```

This gives an error that 'result' is not defined. I think I have to assign 'result' to an empty array before I can fill it? I'll add this line, then test it out to see if there's something I have to do other than that.

```python
result = []
```

Now I have another error, so I'm guessing that line fixed my original error. The error I have now is that my list assignment index is out of range. I know the cause of this though, I just need to change the for loop range to the length of the list minus 1. The upper bound of for loops must be inclusive. Now my code goes from this:

```python
for x in range(0, len(set1arr)):
    for y in range(0, len(set2arr)):
        result[i]=[set1arr[x],set2arr[y]]
```

To this:

```python
for x in range(0, len(set1arr)-1):
    for y in range(0, len(set2arr)-1):
        result[i]=[set1arr[x],set2arr[y]]
```

However, this still doesn't work. I'm going to add some print statements so I can tell where the problem is. I'm going to have it print the size of each array and then the array index so I can see if the for loop is going higher than it should be.

Ok, so it prints the correct sizes, and I see now it errors when the indexes are 0. Let's see what happens if I change setting result to these sets and instead just print them.

This works perfectly, so the problem must be that I'm filling my array the wrong way. After searching Google, I realize that I should use array.append() instead. So here's the line I'm going to use:

```
result.append([set1arr[x],set2arr[y]])
```

This worked! Now I just have to change the printing of the sets so that it uses curly braces instead of square brackets. After a Google search, I learned that using print(content, end='') will allow me to print whatever I need without creating a new line. This will be useful so that I can put all the sets on one line. Here is the code that prints the product of the sets, but using curly braces:

```python
print("{", end='')
for x in range(0, len(set1arr)):
    for y in range(0, len(set2arr)):
        print("{" + set1arr[x] + "," + set2arr[y] + "}", end='')
print("}", end='')
```

However, when I run this, it does not separate each set with a comma. To do this, I add an if statement right before printing the array values, which looks like this:

```python
if ((x!=0) | (y!=0)):
    print(",", end='')
```

Now, it prints product of set multiplication in the proper format.

This is all I wanted to do today, maybe sometime in the future I will add more features, including different set functions and multiplication between more than two sets.

#### February 12, 2018

So it turns out I was way too Java-oriented when writing this program. I had semicolons at the end of every line, and also my comments were double-slashes (//) insead of hash characters (#). Today I just fixed that up and re-commited.

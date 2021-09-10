filename = input("Enter file name : ")
fhand = open(filename)
listname = list()
words = list()

for line in fhand:
    line.rstrip()
    words = line.split() 
    for word in words :
        if word not in listname:
            listname.append(word)
listname.sort()
print(listname)
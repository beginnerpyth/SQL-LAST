
name = "hello, world"

#print(name[5])
#print(name[11])

print(name[0:])

name = "hello, world"
print(name[::-1])

name = input("enter a number:")
if name == name[::-1]:
    print("it is palindrome")
else:
    print("its not")

value = "the string"
dam = len(value)
for x in range(4,dam):
    print(value[x])
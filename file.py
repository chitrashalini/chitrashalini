filename = input("enter file name")
file = open(filename,"r")
content = file.read()
print(content)
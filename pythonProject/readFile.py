#file = open('testreadfile.txt')
#file.read()
#print(file.read())
#print(file.readlines())
#file.read(2)

#for line in file.readlines():
    #print(line)
#file.close()#

with open('testreadfile.txt' , 'r' ) as reader:
    content=reader.readlines()#converted to list
    reversed(content) #reversed the list
    with open('testreadfile.txt' , 'w') as writer:
        for line in reversed(content):
            writer.write(line)

try:
    with open('Test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)
    print("there is an error in try block")

finally:
    print("i always execute")



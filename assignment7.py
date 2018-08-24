# Q 1: Create user defined dictionary and print keys and value
# A 1:
dict1 = {}
i = 1
while i != 0:
    key = input('enter the key value for dictionary: ')
    value = input('enter the value for corresponding key: ')
    dict1[key] = value
    i = int(input('enter 0 to print dictionary otherwise anything to continue'))
print(dict1)

# Q 2: nested dictionary
# A 2:
records = {'Rohan':{'Science':80,'Maths':95,'English':75},'Riya':{'Science':76,'Maths':55,'English':78},'Ajay':\
         {'Science':42,'Maths':10,'English':74}}
name = input("Enter the name: ")
for key in records:
    if name == key:
        print(key, records[key])

print("hello word")
num1 = 30
num2 = 50


print("if else Program start")

if ( num1 > num2 ) : 
    num3 =str(num1) + "    is greater"
    print(num3)
else :
   print("num2 is greater")

print("program is end")

# Start basic cast of program : Numeric Type

totalamount = 1000.20 # int
firstName = "Kisan Pawar" # string
quantity = 300 #float

print(type(totalamount),type(firstName),type(quantity))


# 2. Sequence Types
# str :
# list :
# tuple : 

# let see the list  example

studenName = ['Kisan','Ram','Madhuri','Krisha',"Avaneesh"]

print(type(studenName),studenName)


#tuples are immutable , it will not changed or override

monthName = ("jan","feb","march","april","may","JUne","July","august","sept","oct","nov","dec")

#print all the  tuples 
print(type(monthName),monthName)

#please give 10 the element

print(monthName[9])

#itterate the loop and my birthday is on nov 

for birthCheck in monthName :
    if ( birthCheck == 'april') :
        print(birthCheck + " my match birthday")

# add the numbers

studentMark = (10,20,20,40)

totalMark = 0
for mark in studentMark :
    totalMark += mark

print("Total mark is >>>>" + str(totalMark))

# splice the element on student

twoStudentMark = studentMark[2:4]

print(twoStudentMark)

# dict: Represents a collection of key-value pairs

myEmployee = {"name":'kisan',"role":'Admin',"sal":3000}

print(myEmployee)

#find the keys of dict and values
#method .keys() ,.values , items()

print(myEmployee.keys())
print(myEmployee.values())
print(myEmployee.items())

#find all the keys

for key in myEmployee.keys() :
    print(key)

#find the values of dict

for val in myEmployee.values() :
    print(val)
    
#find both and keys 
#we have added f 

for keyandvalues in myEmployee.items() :
    #f is the function to add key name directly on expression
    print(f"key name is {keyandvalues[0]} ",f"value name is {keyandvalues[1] } ")


# list of dict data

# List of dictionaries with data
my_set  = set()

students = [
    {"name": "Alice", "age": 25, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Mathematics"},
    {"name": "kp", "age": 55, "major": "Math5555ematics"}
]


for studentInfo in students :
    my_set.add(studentInfo["name"])

print(my_set)


#check the loop
   




























 





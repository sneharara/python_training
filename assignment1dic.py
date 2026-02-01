#creating a dictionary
d1={"name":"sneha","age":20,"gender":"female"}
print(d1)

#accessing dict values
print(d1["name"])
print(d1["age"])
print(d1["gender"])

#printing dict values as list
value_list=list(d1.values())
print(value_list)

#updating values
d1["name"]="sneha rara"
d1["age"]=21
print(d1)

#printing keys 1 by one
for key in d1.keys():
    print(key)
    
#nested dictionary
students={"student 1":{"name":"bhavya","age":20,"gender":"female"},
"student 2":{"name":"kasish","age":20,"gender":"female"},
"student 3":{"name":"sanya","age":20,"gender":"female"}}
print(students)

#one dictionary that will contain other three dic.

dict1 = {"name": "Amit"}
dict2 = {"age": 21}
dict3 = {"gender": "Male"}


student = {
    "details1": dict1,
    "details2": dict2,
    "details3": dict3
}

print(student)

#convert list into dictionary
list1 = ["name", "age", "gender"]
list2 = ["Sneha", 20, "Female"]

result = dict(zip(list1, list2))

print(result)

#merge 2 dic.
dic4=dict1 | dict2
print(dic4)
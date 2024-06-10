dict1= {"student1":{
    "name": "Ridha",
    "age":23,
    "marks": {
        "Security":78,
        "python":88
    }},
    "student2":{
    "name": "Milu",
    "age":23,
    "marks": {
        "Security":78,
        "python":88
    }
    }
}
print(dict1["student1"])
print(dict1.get("student2").get("age"))
print(dict1["student1"])

#add a new key
dict2={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
dict2["color"]="red"
dict2.update({"year":1989})
print(dict2)
dict2.pop("year")
print(dict2)
dict2.popitem()
print(dict2)


s1={1,2,3,4,5,5,5}  #will only print 1 '5'
s2={'a', 'b','c','d',21,22,23}
print(s1)
print(s2)
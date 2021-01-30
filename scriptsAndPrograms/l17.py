myCat = {"size":"fat", "color":"gray", "disposition":"loud"}
myCat["size"]

"My cat has" + myCat["color"] + " fur".

spam = {12345: "Luggage combination", 42: "The Answer"}
[1,2,3] = [3,2,1]

[1,2,3] == [3,2,1]

eggs = {"name":"Zophie", "species":"cat", "age":8}
ham = {"species":"cat", "name":"Zophie", "age":8}

eggs == ham

eggs["color"]

list(egg:keys())

list(eggs.keys())

list(eggs.items())

eggs.keys()

 for k in eggs.keys():
 	print(k)

 for v in eggs.values():
 	print(v)

 for k,v in eggs.items():
 	print(k,v)

 for i in eggs.items():
 	print(i)

 print(eggs)

 "cat" in egg.values()

 if "color" in eggs:
 	print(eggs["color"])

 eggs.get("age", 0)

 eggs.get("color", "")

 picnicItems = {"apples":5, "cups":2}
 print("I am bringing" + str(picnicItems.get("napkins, 0")) + " to the picnic.")

 if "color" not in eggs:
 	eggs["color"] = "black"

eggs.setdefault("color", "black")

eggs.setdefault("color", "back")

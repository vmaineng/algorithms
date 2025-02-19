def fun():
    # x = 5
    # y = x
    # x = 10
    # print(y)

    # a = [1,2,3]
    # b = a
    # b.append(4)
    # print(a)

    # m ='hello'
    # n = m
    # m = 'world'
    # print(n)

    # p = [10, 20]
    # q = p[:]
    # q.append(30)
    # print(p)

    d = {"key": "value"}
    e = d
    e["key"] = "new_value"
    print(d["key"])

fun()

a = [10,20,30]
b = a
b.append(40)

a = [10,20,30]
b = [10,20,30, 40]

a = [10,20,30, 40] #reference same list object in memory
b = [10,20,30, 40]

x = 'hello'
y = x
x = 'world'
y = 'hello' #Strings are immutable, so when x is reassigned, y still holds "hello".

data = {"score": 100}
copy_data = data
copy_data["score"] = 200
data["score"] = 200
#Since dictionaries are mutable and copy_data = data, both variables point to the same object in memory. Modifying copy_data affects data.

b = a.copy()

"Start", "Inside Timeout", "End"
#Even though setTimeout(..., 0) has zero delay, it is still asynchronous and runs after the synchronous code finishes.

"Waiting...", 'A was called'

x.value = 10
#Objects in JavaScript are reference types, so y = x makes y point to the same object. Modifying y.value also changes x.value.

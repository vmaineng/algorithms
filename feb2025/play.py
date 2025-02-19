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

x = 'hello'
y = x
x = 'world'
y = 'hello'


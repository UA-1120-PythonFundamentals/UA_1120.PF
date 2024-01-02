# ## list
# l = list()
# print(type(l), l)
# l = list("python")
# print(type(l), l)
# l = list(   (1, 2, 3, "text", [1,2,3])  )
# print(type(l), l)
# l = []
# print(type(l), l)
# l = [1, 2, 3, "text", [1,2,3]]
# print(type(l), l)
# print(len(l))
# print(l[3])
# print(l[-2])
# print(l[-1], l[-1][1] )
# print(l[3], l[3][1] )
# l = [1, 2, 3]
# l.append(l)
# print(l)
# print(l[-1], l[-1][-1][-1][-1][1])
# print(l[:3])
# print(dir())
# print(dir(list))
# print([method for method in dir(list) if not method.startswith("__")])
# l = []
# l.append(1)
# print(l)
# l.append("test")
# print(l, id(l))
# l.clear()
# print(l, id(l))
# l = []
# print(l, id(l))


# d = [1,2,3]
# c = [10,20,30]
# l = [1,d,c]
# print(l)
# l[1] = []
# l[2].clear()
# print(l, d, c)

# d = [1,2,3]
# c = [10,20,30]
# l = [1,d,c]
# ll = l.copy()
# lll = l[:]
# import copy
# ld = copy.deepcopy(l)
# print(l, ll, lll, ld)
# l[0] = 99
# lll[0] = "text"
# ll[1][2] = "3"
# print(l, ll, lll, ld)
# l = [1, 2, 3, "text", [1,2,3,4],1]
# print(l.count(1))
# print(l.count([1,2,3]))
# print(l.count("X"))
# l.append("text")
# l.extend("text")
# print(l)
# # print(l.index("text"))
# # print(l.index("text", 4))
# # print(l.index("text", 4, 5))
# l.insert(2, [9,8,7])
# print(l)
# l.insert(90, [90,80,70])
# print(l)

# element = l.pop()
# print(l, element)
# element = l.pop(1)
# print(l, element)
# element = l.remove(1)
# print(l, element)
# l.reverse()
# print(l)
# # l.sort()#error
# l.sort(key=lambda element: len(str(element)))
# print(l)
# l = [1,3,5,2,4,63,2,1,]
# print(l)
# l.sort()
# print(l)

## tuple
# t = tuple()
# print(type(t), t)

# t = tuple("1,2,3,4")
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = (1,)
# print(type(t), t)
# t = (1,1,2,4,5)
# print(type(t), t)

# print([method for method in dir(tuple) if not method.startswith("__")])

# l = [10,20,30,45,10,0]
# # print(all(l))
# # ll = sorted(l)
# # print(l, ll)
# a, b= (1 ,2)
# lll = enumerate(l)
# print(list(lll))
# for i in range(len(l)):
#     print(i, l[i])
# for i, value in enumerate(l):
#     print(i, value, l[i])

# ## set

# s = set()
# print(type(s), s)
# s = set("rewqtreywtqerwyqterwyqterywtq")
# print(type(s), s)
# s = {}  # dict
# print(type(s), s)
# s = {1, 2, 3, 1, 2, 3, 2, 3, 2, 3}
# print(type(s), s)

# methods = [method for method in dir(set) if not method.startswith("__")]
# print(methods[:10])
# print(methods[10:])
# s = set()
# s.add(1)
# s.add(1)
# s.add(2)
# print(s)
# print(s.pop())
# print(s.update("abcdsabfhjfvbdsk"))
# print(s)

## dict
# class A(object):
#     def __repr__(self):
#         return f"A"
# a = A()
# d = {a:1}
# print(d)
# d = {list():1}
# print(d)

# d = dict()
# print(type(d), d)
# d = dict( [(1,1), (2,2)] ) 
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     "a": 10,
#     "b": 20,
#     1: 25,
#     (1,2,3): "a"

# }

# print(type(d), d)
print([method for method in dir(dict) if not method.startswith("__")])
d = {}
dd = d.fromkeys("test", "test")
print(dd)
print(dd.get("e"))
print(dd["e"])
# print(dd["q"])
print(dd.get("q"))
print(dd.items())
print(dd.keys())
print(dd.values())
print(dd.pop("e"))
print(dd)
print(dd.popitem())
dd.setdefault("setdefault")
print(dd)
dd.update({1:2, 2:22})
print(dd)

for key in dd:
    print(key, dd[key])

for key, value  in dd.items():
    print(key, value)
f = input("text value:")
for key, value  in dd.items():
    if value == f:
        print(key)
    
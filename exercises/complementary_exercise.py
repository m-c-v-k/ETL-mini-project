# 1

# 1.a
# a, b = 1, 2
# print(a, b)
# 1 2

# 1.b
#print((a, b))
# (1, 2)

# 1.c
# a, b = b, a
# print(a, b)
# Error not defined

# 1.d
# a, b = b, a
# print(a, b)
# Error not defined

# 1.e
# a, b, c = 1, 2, 3
# print(a, b, c)
# 1 2 3

# 1.f
# a, b, c = b, c, a
# print(a, b, c)
# Error not defined

# 1.g
# a, b, c = b, c, a
# print(a, b, c)
# Error not defined


# 2
# def dup():
#     return 1, 2

# 2.a
# a, b = dup()
# print(a, b)
# 1 2


# 2.b
# a = dup()
# print(a, b)
# Error b not defined

# 3
# d = {'a': 1, 'b': 2, 'y': 3}

# 3.a
# for key, value in d.items():
#     print(key, value)

# a 1
# b 2
# c 3

# 3.b
# for keyval in d.items():
#     print(keyval)

# ('a', 1)
# ('b', 2)
# ('y', 3)

# 3.d
# for keyval in d.items():
#     print(keyval[0], keyval[1])

# a 1
# b 2
# c 3

# 3.d
# for keyval in d.items():
#     key, val = keyval
#     print(key, val)

# a 1
# b 2
# c 3

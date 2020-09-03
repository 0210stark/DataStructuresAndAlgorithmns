# Slicing inde randg [)
l = list(range(10))
print(l)
print(l[0:2])
print(l[2:])
print(l[:])

# Step Index [start,stop,index]
l = list(range(10))
print(l[0::2])
print(l[-3::-2])


# Modifying Value using the exisitng Value..
x = list(range(10))
print(x)
x[1:4] = [99, 98, 97]
print(x)

# deleting elements from the list.
d = list(range(100))
print(d)
del d[0]
print(d)
# Delete Every Alternate element from the list
del d[::2]
print(d)

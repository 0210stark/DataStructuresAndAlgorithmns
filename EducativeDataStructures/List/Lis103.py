# Append FUnction O(1)
l = [1, 2, "Hey"]
l.append(9)
print(l)

# Insert Function O(n) #Takes index and values as the Arguments..
l2 = [1, 2, 'Apple']
l2.insert(2, "Orange")
print(l2)

# remove Function O(n)
# If the Element Doest Occur give sRunt time Error.
# Takes value as the argument..
l3 = [4, 5, "Apple"]
print(l3)
l3.remove("Apple")
print(l3)
try:
    l3.remove("Orange")
except:
    print("Error Occured!")

# poping Element takes O(k) time
# Takes index if index is not given takes out last element
l4 = [5, 2, 3]
l4.pop(0)
print(l4)
l4.pop()
print(l4)

mylist = ["hello", "world", 4, [5, 6], "hii", "hey"]

print(mylist)
print(mylist[0])
print(mylist[0][2])
print(mylist[3][1])

print(mylist[:])
print(mylist[0:3])

print(mylist[3:4])
print(mylist[2:5])

print(mylist[::2])

print(mylist[::-1])

print(mylist[-2:-5])
print(mylist[-2:-5:-1])

# [5, 6] is a nested list because a list is stored inside another list.

# Indexing starts from 0.
# mylist[0] gives the first element: "hello".

# mylist[0][2] first gets mylist[0] -> "hello",
# then gets index 2 from "hello" -> "l".

# mylist[3][1] first gets mylist[3] -> [5, 6],
# then gets index 1 -> 6.

# List slicing syntax:
# mylist[start:end:step]
# The end index is not included.

# If start is omitted, slicing starts from index 0.
# If end is omitted, slicing goes up to the end of the list.
# If step is omitted, the default step is 1.

# mylist[:] gives the complete list.
# It is equivalent to mylist[0:len(mylist):1].

# mylist[0:3] gives indexes 0, 1, and 2.
# Index 3 is not included.

# mylist[3:4] gives only index 3.
# The result is [[5, 6]] because the element at index 3 is itself a list.

# mylist[2:5] gives indexes 2, 3, and 4.
# The result is [4, [5, 6], "hii"].

# mylist[::2] starts from index 0 and takes every 2nd element.
# The result is ["hello", 4, "hii"].

# mylist[::-1] reverses the list.
# A negative step means moving from right to left.

# mylist[-2:-5] gives [] because the default step is +1.
# Start index -2 is to the right of end index -5,
# so moving left-to-right cannot reach the end index.

# mylist[-2:-5:-1] works because the step is -1.
# It moves from right to left and gives ["hii", [5, 6], 4].

# Negative indexes count from the end:
# -1 = last element
# -2 = second-last element
# -3 = third-last element

# General slicing approach:
# list[start:end:step]
# Positive step -> move left to right.
# Negative step -> move right to left.
# The end index is never included.

# mylist[len(mylist)-2 : len(mylist)-5]
# mylist[6-2 : 6-5] 
# mylist[4:1]  = final my list[start index:end index:step]  and step is positive so it will go left to right if it would have been negative then it would have gone right to left   end index is not included in the output / doesn't count
# [0:n:step]     by default everything is [0:n:1] if end index is not given it would go till the end of the list like it is length(n) of the list
# [-10] and [10] are same because -10 is 10th element from the end and 10 is 10th element from the start


mylist.append("new element")
print(mylist) #it has added the new element to the end of the list because list are mutable and we can add new elements to them
# mutable means we can change the list after it has been created. We can add, remove, or modify elements in a mutable list.
mylist.insert(2, "inserted element") # it will insert the new element at index 2 and shift the rest of the elements to the right

# #list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
# squares = []
# for x in range(1, 6):
#     squares.append(x**2)

# #list comprehension
# squares = [x**2 for x in range(1, 6)]
# # Output: [1, 4, 9, 16, 25]
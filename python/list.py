mylist =  ["hello", "world", 4, [5, 6], "hii", "hey"]
# print(mylist) # it will print the list mylist,  [5,6] this is count as a separate index in the list   we use here concept of 2d array because we have a list inside a list
# print(mylist[0]) # it will print the value of the index 0 of the list mylist which is hello output will be hello
# print(mylist[0][2]) # it will print the value of the index 2 of the index 0 of the list mylist which is l output will be l
# print(mylist[3][1]) # it will print the value of the index 1 of the index 3 of the list mylist which is 6 output will be 6 (index starts from 0)


# # this is by default [0:n] (n is length of the list)
# print(mylist[:]) # it will print the value of the index 0 to n of the list mylist which is ['hello', 'world', 4, [5, 6], 'hii', 'hey'] output will be ['hello', 'world', 4, [5, 6], 'hii', 'hey']
# print(mylist[0:3]) # it will print the value of the index 0 to 2 of the list mylist which is ['hello', 'world', 4] output will be ['hello', 'world', 4]

# print(mylist[:]) its means here [0:n] length of the list is 6 so it will print the value of the index 0 to 5 of the list mylist which is ['hello', 'world', 4, [5, 6], 'hii', 'hey'] output will be ['hello', 'world', 4, [5, 6], 'hii', 'hey']

print(mylist[3:4]) # it will print the value of the index 3 to 3 of the list mylist which is [[5, 6]] output will be [[5, 6]]
print(mylist[2:5]) # it will print the value of the index 2 to 4 of the list mylist which is [4, [5, 6], 'hii'] output will be [4, [5, 6], 'hii']

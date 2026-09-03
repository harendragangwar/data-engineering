# mylist = ["hello", "hii", "hey"]

# # for i in mylist:
# #     print(i)             # here i is index of the list and it will print the value of the index in the list


# # # alternate way using range function to get the index of the list
# # for i in range(len(mylist)):
# #     print(mylist[i])    # here i is the index and mylist[i] is the value at that index


# # for i in range(1, 11):
# #     print(i)           # it will print the numbers from 1 to 10
# #     print(i*i)         # it will print the square of the numbers from 1 to 10
# #     print("harendra")  # it will print the string "harendra" 10 times

# # nested for loop
# # for i in mylist:
# #     for j in range(1, 4):
# #         print(i, j)  # it will print the value of i and j in each iteration
# # output:
# # # hello 1
# # # hello 2
# # # hello 3
# # # hii 1
# # # hii 2
# # # hii 3
# # # hey 1
# # # hey 2
# # # hey 3

# # for i in mylist:
# #     print(i)  here output will be:
# # # hello hii hey, now this output eqals to i now we can itrate on i     
# #     for j in i:
# #         print(j) # it will print the value of j in each iteration
# # hello
# # h
# # e
# # l
# # l
# # o
# # hii
# # h
# # i
# # i
# # hey
# # h
# # e
# # y

# # for i in mylist:
# #     if(i.lower() == "hii"):
# #         continue  # it will skip the value of i if it is equal to "hii"
# #         print(i)  # output will be:
# # # hello
# # # hey


# for i in mylist:
#     if(i.lower() == "hii"):
#         break  # it will break the loop if the value of i is equal to "hii"
#         print(i)  # output will be: 
# # hello
for i in mylist:
    if(i.lower() == "hii"):
        pass  # it will do nothing if the value of i is equal to "hii"
        print(i)  # output will be:hello

# while loop
x = 10
while(x<20):
    print(x)  # it will print the value of x in each iteration
    x = x+1    # it will increment the value of x by 1 in each iteration
# x = x+1 if this thing is not there then it will print the value of x infinite times because the condition will always be true
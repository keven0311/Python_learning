# python default setting for print function: end with \n means to new line, sep=" " means arguments are seperated by " "
# print('hello, ', end='\n', sep=" ")

# \"   \"   this is will allow you escape to use " "s
# print("hello, \"friend\"")

# name = input("What's your name? ")

# #remove whitespaces from str
# name = name.strip()

# #capitalize first letter of "name" variable
# # name.capitalize()

# #title base capitalization of "name"
# name = name.title()

# print(f"hello, {name}!")


name = input("whats your name? ")

name = name.strip().title()
first, last = name.split(" ")
print(f"Hello, {first}!")

# testing for github pushes!
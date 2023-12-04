# def meow():
#     for i in range(3):
#         print("Meow")

# meow()

# thelist = [1, 2, 3, 4, 5]


# def loops(list):
#     list.reverse()
#     for i in range(0, len(list), 1):
#         print(list[i])
#         if list[i] == 5:
#             print("hello")
            
#     return list


# print(loops(thelist))


# print("meow\n" * 3 , end='')

def main():
    number = getNumber()
    meow(number)

def getNumber():
    theBool = True
    while theBool:
        n = int(input("What's n? "))
        if n > 0:
            theBool = False
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
    

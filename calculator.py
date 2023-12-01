# x = int(input("what's int x? "))
# y = float(input("what's float y? "))

# # round the number to intiger:
# z = round(x+y)

# # use f string with ":," for a number, it will seperate the number with ","

# print(f'the answer is rounded: {z:,}')

# # use ":.2f" will rounded the float number with two digits after "."

# print(f"{z:.2f}")

# # it also works fine using round method like this:
# zz = round(x / y, 2)


# function part:

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
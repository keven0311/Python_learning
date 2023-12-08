import sys


# sys.argv[1] means in command line if you run: "python3 name.py Kev". 
# the "name.py" is sys.argv[0] and "Kev" is the sys.argv[1]
# if you dont give the sys.argv[1] in this situation, it will casue an IndexError.

# if len(sys.argv) < 2:
#     sys.exit('too few arguments')
# elif len(sys.argv) > 2:
#     sys.exit('too many arguments')
# else:
#     print('hello, my name is', sys.argv[1])
    
#-----------------------------
if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:-1]:
    print('hello, my name is', arg)
    
#-----------------------------
# try:
#     print('hello, my name is', sys.argv[1])
# except IndexError:
#     print('Too few arguments')
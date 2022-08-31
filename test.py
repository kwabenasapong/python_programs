##import sys
#import dis

##for line in sys.stdin:
##    if 'q' == line.rstrip():
##        break
##    print(f'input: {line}')
##print('Exit')

##sys.stdout.write('Boys')

##def print_to_stderr(*a):
##    print(*a, file = sys.stderr)
##
##print_to_stderr("Hello World\n")

##def write_to_stderr(*a):
##    sys.stderr.write(*a)
##    sys.exit(1)
##
##write_to_stderr("and that piece of art is useful - Dora Korpar, 2015-10-19\n")


##def magic_calculation(a, b):
##    return 98 + (a ** b)
##
##dis.dis(magic_calculation)
##    

##for alpha in reversed (range(97, 123)):
##    if alpha % 2 == 1:
##        conv = alpha - 32
##    else:
##        conv = alpha
##    print("{:c}". format(conv), end='')
    
        
##def remove_char_at(str):
##    i = 0
##    for chr in str:
##        print('{0:s}, {1:d}'.format(chr, i))
##        i = i + 1
##
##remove_char_at('The boy is good')

##def remove_char_at(str, n):
##    for i in range(len(str)):
##        result = ""
##        if i != n:
##            #print(str[i], end='')
##            result += str[i]
##            final = print(result, end='')
##    print('')
##    #exit()
##    return final


##def remove_char_at(str, n):
##    if n < 0:
##        return (str)
##    return (str[:n] + str[n+1:])            

##def remove_char_at(str, n):
##    new = ""
##    i = 0
##    for c in str:
##        if i != n:
##            new += c
##        i += 1
##    return new
    
##print(remove_char_at('The boy is good', 14))
##print(remove_char_at("Chicago", 3))

# def magic_calculation(a, b, c):
#     if a < b:
#         return c
#     elif c > b:
#         return a + b
#     else:
#         return a * b - c

# print(magic_calculation(30, 10, 2))

# def no_c(my_string):
#     str = ''
#     for chrs in range(len(my_string)):
#         if 'c' in my_string[chrs] or 'C' in my_string[chrs]:
#             continue
#         else:
#             str = str + my_string[chrs]
#     return str

# print(no_c('abcabcccbaaac'))
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))

##def print_matrix_integer(matrix=[[]]):
##    num = len(matrix)
##    i = 0
##    while (i < num):
##        for m in matrix[i]:
##            print('{:2d}'.format(m), end=' ' if m != matrix[-1][-1] else '\n')
##        i = i + 1
##        print('')
       

""" def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print() """


# def print_matrix_integer(matrix=[[]]):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print("{:d}".format(matrix[i][j]), end="")
#             if j != (len(matrix[i]) - 1):
# #                 print(" ", end="")

#         print("")


##matrix = [
##    [1, 2, 3],
##    [4, 5, 6],
##    [7, 8, 9],
##    [10, 11, 12],
##    [13, 14, 15],
##    [16, 17, 18]
##]
##
##print_matrix_integer(matrix)
##print("--")
##print_matrix_integer()
##    



##def max_integer(my_list=[]):
##    if my_list == []:
##        print('-no list-')
##        return None
##    else:
##        a = 0
##        for i in range(len(my_list)):
##            print(a, i, '-compare-', end='\n')
##            if my_list[a] < my_list[i]:
##                a = i
##                print(a, '-less-',end='\n')
##            elif a == len(my_list) -1:
##                a = -1
##                print(my_list[a], a, 'last')
##            elif i == len(my_list) - 1:
##                print(my_list[a], '--finished--')
##                return my_list[a], a
##            else:
##                print('-great-')
##                continue
                
##def max_integer(my_list=[]):
##    """Find the biggest integer of a list."""
##    if len(my_list) == 0:
##        return (None)
##
##    big = my_list[0]
##    for i in range(len(my_list)):
##        print(big, i, '-compare-', end='\n')
##        if my_list[i] > big:
##            print('-great-')
##            big = my_list[i]
##
##    return (big)        



def divisible_by_2(my_list=[]):
    new_list = [not i % 2 for i in my_list]
    return new_list
##    for i in range(len(my_list)):
##        if my_list[i] % 2 == 0:
##            return my_list[i]
##        else:
##            continue



my_list = [0, -1, 2, 3, -4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
            
tel = {'jack': 4098, 'snape': 5098}
tel2 = {'amaa': 4068, 'kob': 8976}
for n, i in tel.items():
    print(n, i)
for n, i in enumerate(tel):
    print(n, i)
for a, b in zip(tel, tel2):
    print(a, b)

    


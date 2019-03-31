def is_diagonal(lol):
    for row in range(len(lol)):
        for value in range(len(lol[row])):
            if row != value and lol[row][value] != 0:
                return False
    return True





def is_upper_triangular(lol):
    for row in range(1, len(lol)):
        for value in range(0, row):
            if lol[row][value] != 0:
                return False
    return True

    
    



def contains(lol, value):
    '''for row in range(len(lol)):'''
    for row in lol:
        for item in row:
            if item == value:
                return True
    return False





def biggest(lol):
    biggest_item = []
    for row in lol:
        for item in row:
            biggest_item.append(item)
    return max(biggest_item)


            
def indices_biggest(lol):
    if len(lol) == 1 and len(lol[0]) == 1:
        return [0, 0]
    big = biggest(lol)
    for i in range(len(lol)):
        for j in range(len(lol[0])):
            if lol[i][j] == big:
                return [i, j]


def second_biggest(lol):
    return sorted(value for row in lol for value in row)[-2]




'''def indices_second_biggest():
'''



def substr_in_values(dictionary, string):
    lst = []

    for key in dictionary:
        for value in dictionary[key]:
            if string.lower() in value.lower():
                lst.append(key)
                break
    return sorted(lst)






def indices_divisible_by_3(lol):
    number_dict = []
    for row in range(len(lol)):
        for value in range(len(lol[0])):
            if (value + row) % 3 == 0:
                number_dict.append(lol[row][value])
    return number_dict





def sort_int_string(string):
    string = string.strip().split()
    final_lst = []

    for value in string:
        final_lst.append(int(value))
    final_lst = sorted(final_lst)

    return_string = " "

    for value in final_lst:
        return_string += str(value) + " "
    return return_string.strip()



    



def dups_lol(lol):
    duplicate_lst = []

    for row in lol:
        for value in row:
            if value not in duplicate_lst:
                duplicate_lst.append(value)
            else:
                return True
    return False






def dups_dict(dictionary): 
    duplicate_lst = []

    for key in dictionary:
        duplicate_lst.append(dictionary[key])

    return dups_lol(duplicate_lst)














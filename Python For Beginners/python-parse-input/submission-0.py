from typing import List

def read_integers() -> List[int]:
    number_string = str(input())
    string_list = number_string.split(",")
    my_list = list()
    for s in string_list:
        my_list.append(int(s))
    return my_list 




# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

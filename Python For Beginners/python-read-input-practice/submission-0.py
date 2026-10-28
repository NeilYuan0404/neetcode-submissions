def add_two_numbers() -> int:
    number_string = str(input())
    string_list = number_string.split(",")
    first = int(string_list[0])
    second = int(string_list[1])
    return first + second


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

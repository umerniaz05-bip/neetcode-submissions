def add_two_numbers() -> int:
    add_int = input()
    add_string = add_int.split(",")
    add_list = []
    for i in add_string:
        add_list.append(int(i))
    total = add_list[0] + add_list[1]
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

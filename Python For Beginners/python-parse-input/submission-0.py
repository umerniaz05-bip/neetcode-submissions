from typing import List

def read_integers() -> List[int]:
    use_input = input()
    int_list = use_input.split(",")
    fin_list = []

    for i in int_list:
        fin_list.append(int(i))
    return fin_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

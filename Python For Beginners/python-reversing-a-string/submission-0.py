def reverse_string(input_string: str) -> str:
    end = len(input_string)
    start, end, step = 0, end, -1
    return(input_string[end:start:step]) + input_string[0]

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))

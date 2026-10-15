from typing import List

def count_unique_words(words: List[str]) -> int:
    new_set = set(words)
    uni = len(new_set)
    if uni == 0:
        return 0
    return uni


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))

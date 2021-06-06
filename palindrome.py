def palindrome(my_list):
    new_palindrome = []
    for names in my_list:
        if names == names[::-1]:
            new_palindrome.append(names)
    return new_palindrome
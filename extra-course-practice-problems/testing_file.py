# print(is_palindrome("Madam in Eden, I'm Adam"))
# print(is_palindrome("Mister in Eden, I'm Eve"))



def foo(input):
    reverse = ""
    for i in range(len(input) - 1, -1, -1):
        reverse += input[i]

    if reverse == input:
        return input
    return "%s%s" % (input, reverse)

print(foo("Madam in Eden, I'm Adam"))
print(foo("boba"))
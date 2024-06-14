
def reverseString(input):
    return input[::-1]


def reverse(str):
    reversed = ""
    i = len(str) - 1
    while i >= 0:
        reversed = reversed + str[i]
        i = i - 1
    return reversed


print(reverse("Hello"))
print(reverseString("Hello"))
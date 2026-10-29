def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

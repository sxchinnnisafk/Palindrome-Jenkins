def is_palindrome(s: str) -> bool:
    # Clean the string: keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "No 'x' in Nixon"
    ]
    
    print("Running Palindrome Checker...")
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> Palindrome: {result}")
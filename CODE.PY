def is_palindrome(word):
    # Remove any whitespace and convert to lowercase
    word = word.replace(" ", "").lower()
    
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# Test the palindrome checker
user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")

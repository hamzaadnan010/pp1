print("Muhammad Hamza Adnan - 18b-017-cs-Sec-'A'")
print("Practice problem 3.10")


def noVowel(s):
    'return True if string s contains no vowel, False otherwise'
    for char in s:
        if char in 'aeiou'or char in 'AEIOU':
            return False
    return True

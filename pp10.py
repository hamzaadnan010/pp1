print("Muhammad Hamza Adnan - 18b-017-cs-Sec-'A'")
print("Practice Problem 3.11")

def allEven(numList):
    'return True if all integers in numList are even, False otherwise'
    for num in numList:
        if num%2 == 0:
            return True
        else:
            return False
    

print("Muhammad Hamza Adnan 18b-017-cs Sec'A'")
print("Practice problem 3.13")



def average(n1, n2):
    'Calculates and return average of 2 numbers n1 and n2.'
    avg = (n1 + n2) / 2
    return avg



def negatives(list):
    'prints all negative numbers in list list one in a line.'
    for x in list:
        if x < 0:
            print(x)

print("Muhammad Hamza Adnan - 18b-017-cs-Sec-'A'")
print("Practice problem 3.3(a)")

year = int(input("Please Enter the Year Number you wish: "))

if (( year%4 == 0 )):
    print("Could be a leap year")
else:
    print("Definitely not a leap year.")



print("Practice problem 3.3(b)")


ticket = int(input("Enter the number of tickets: "))
lottery = int(input("Enter the value of lottery: "))
if ticket == lottery:
    print("You won!.")
else:
    print("Better luck next time...")

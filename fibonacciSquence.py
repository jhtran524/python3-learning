# Program to display the Fibonacci sequence up to n-th term

nSequence = int(input("How many sequences do you wish to complete? "))

# first two numbers in the sequence
num1, num2 = 0, 1
# initializing a counter
count = 0

# check if the number of squences is valid
if nSequence <= 0:
   print("Please enter a positive integer.")
elif nSequence == 1:
   print("Fibonacci sequence up to",nSequence,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while count < nSequence:
       print(num1)
       nth = num1 + num2
       # update values
       num1 = num2
       num2 = nth
       count += 1
def check_numbers(num):
   if num > 0:
    print("Positive")

   elif num < 0:
    print("negative")
   else:
    print("zero")
number = int(input("Enter your number: "))
check_numbers(number)
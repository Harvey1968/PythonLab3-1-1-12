#3.1.1.12 LAB: Essentials of the if-elif-else statement
#User enters a year
year = int(input("Enter a year: "))

#If the user input is before 1582 the below ouput is shown;
if year < 1582:
	print("Not within the Gregorian calendar period")

#if the year number isn't divisible by four, it's a common year;
elif year % 4:
	print("It's a common year!")

#otherwise, if the year number isn't divisible by 100, it's a leap year;
elif year % 100:
    print("It's a leap year!")

#otherwise, if the year number isn't divisible by 400, it's a common year;
elif year % 400:
	print("It's a common year!")

#Otherwise, it's a leap year.
else:
    print("It's a leap year!")

def is_leap(year):
    # A year is a leap year if it meets the following conditions:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, it's a leap year
            else:
                return False  # Divisible by 100 but not 400, not a leap year
        else:
            return True  # Divisible by 4 but not 100, it's a leap year
    else:
        return False  # Not divisible by 4, not a leap year

# Example usage:
year = int(input("Enter a year: "))
print(is_leap(year))

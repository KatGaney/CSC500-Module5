# Part 1: Rainfall Calculator
# This program calculates the average rainfall over a period of years using nested loops.

def rainfall_calculator():
    """
    Prompts the user for rainfall data and calculates the total and average rainfall.
    """
    print("--- Rainfall Calculator ---")
    
    # Get the number of years from the user.
    num_years = int(input("Enter the number of years: "))
    if num_years < 1:
        print("Number of years must be 1 or greater.")
        return

    total_months = 0
    total_rainfall = 0.0

    # Outer loop iterates through each year.
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")
        # Inner loop iterates through each month.
        for month in range(1, 13):
            # Get the rainfall for the current month.
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            total_rainfall += rainfall
            total_months += 1
    
    # Calculate the average rainfall.
    if total_months > 0:
        average_rainfall = total_rainfall / total_months
        print("\n--- Results ---")
        print(f"Number of months: {total_months}")
        print(f"Total inches of rainfall: {total_rainfall:.2f}")
        print(f"Average rainfall per month: {average_rainfall:.2f}")
    else:
        print("\nNo rainfall data entered.")
# end of part 1

# Part 2: Book Club Points
# This program calculates book club points based on the number of books purchased.

def book_club_points():
    """
    Prompts the user for books purchased and displays the awarded points.
    """
    print("\n--- Book Club Points ---")
    
    # Get the number of books purchased from the user.
    books_purchased = int(input("Enter the number of books purchased this month: "))
    
    points = 0
    if books_purchased < 0:
        print("Number of books cannot be negative.")
    elif books_purchased >= 8:
        points = 60
    elif books_purchased >= 6:
        points = 30
    elif books_purchased >= 4:
        points = 15
    elif books_purchased >= 2:
        points = 5
    else:
        points = 0
        
    print(f"You have been awarded {points} points.")
# end of part 2

# Main program execution
if __name__ == "__main__":
    rainfall_calculator()
    book_club_points()

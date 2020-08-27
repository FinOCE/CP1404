"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

SMALL_BONUS = 10
LARGE_BONUS = 15

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * (SMALL_BONUS/100)
        print(f"You are eligible for a {SMALL_BONUS}% bonus worth ${bonus:.2f}")
    else:
        bonus = sales * (LARGE_BONUS/100)
        print(f"You are eligible for a {LARGE_BONUS}% bonus worth ${bonus:.2f}")
    
    sales = float(input("Enter sales: $"))
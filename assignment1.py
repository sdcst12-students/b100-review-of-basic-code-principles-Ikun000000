"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

x=float(input("Enter inital investment: "))
x1=float(input("Enter the annual interest rate as a percentage: "))
y=x1/100
x2=str(input("Enter the unit(Years, Months, Days): "))
x3=float(input("Enter the lenth of time: "))
if x2==("Years"):
  i=round(x*y*x3, 2)
  print(f"The interest is {i} dollars.")
if x2==("Months"):
  i1= round(x*y*x3/12,2)
  print(f"The interest is {i1} dollars.")
if x2==("Days"):
  i2= round(x*y*x3/365,2)
  print(f"The interest is {i2} dollars.")
else:
  print("Error, please enter again.")
  

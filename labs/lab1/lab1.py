"""
Name: Logan Segal
Lab 1.py

Problem: In this lab I found the monthly interest rate by asking the user a set of questions about their credit statements.
 I used the data I collected and created different functions to help me calculate the monthly interest rate.

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

def monthly_interest():
    annual_interest_rate= eval(input("What is your annual interest rate?"))
    days_in_cycle= eval(input("How many days are in the billing cycle"))
    net_balance= eval(input("What is your net balance?"))
    payment_recieved= eval(input("What is the payment recieved?"))
    day_of_payment=eval(input("On what day of the cycle did you make your payment?"))


    step_1= net_balance*days_in_cycle
    days_subtratction=days_in_cycle-day_of_payment
    step_2=payment_recieved*days_subtratction
    step_3= step_1-step_2
    average_daily_balance= step_3/days_in_cycle
    monthly_interest_rate= annual_interest_rate/12
    decimal_conversion= monthly_interest_rate/100
    monthly_interest_charge= average_daily_balance*decimal_conversion

    rounded_interest=round(monthly_interest_charge,2)
    print("monthly interest rate: $", rounded_interest)










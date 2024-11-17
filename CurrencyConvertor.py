from currency_converter import CurrencyConverter
from datetime import date
import datetime
c=CurrencyConverter()
# Define the exchange rate
limit=['USD','JPY','BGN','CYP','CZK','DKK','EEK','GBP','HUF','LTL','LVL','MTL','PLN','ROL','RON','SEK','SIT','SKK','CHF','ISK','NOK','HRK','RUB','TRL','TRY','AUD','BRL','CAD','CNY','HKD','IDR','ILS','INR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR']

print(f"This code is limited to have database of {limit} only upto 30th September 2024.")

print("Please select any of them...")
while True:
 control=input("Enter 'DONE' to stop! Anything else to continue...").strip().upper()
 if control=='DONE':
        break
 else:
    dates=input("Do you want to get data according to dates (YES/NO) if no it will give upto the latest record:").strip().upper()
    num=int(input("Enter the value of currency: "))
    choice=input("Enter the currency you want to convert: ").upper()
    if choice in limit:
        choice1=input("Enter the currency you want convert to: ").upper()
        if choice1 in limit:
            if dates=='NO':
                print(f"{num} {choice} is equal to {c.convert(num,choice,choice1)} {choice1}")
            elif dates=='YES':
                year=int(input("Enter the year:"))
                month=int(input("Enter the month:"))
                d=int(input("Enter the date:"))
                d1=datetime.datetime(year,month,d)
                d2=datetime.datetime(2024,9,30)
                if d1<d2:
                    print(f"{num} {choice} is equal to {c.convert(num,choice,choice1,date=date(year,month,d))} {choice1}")
                else:
                    print("Enter valid date!!")

        else:
            print("Invalid choice. Please select from the given list.")
    elif control=='DONE':
        break
    else:
        print("Invalid choice. Please select from the given list.")

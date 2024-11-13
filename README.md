# Currency Conversion Code

## Overview
This script allows users to convert currency amounts between various supported currencies. The conversion can be done based on the latest exchange rates or for a specific date, provided the date is on or before September 30, 2024.

## Requirements
- Python 3.x
- `currency_converter` library (install via pip: `pip install currency_converter`)

## Code Structure

### Imports
- **CurrencyConverter**: A class from the `currency_converter` library to handle currency conversion.
- **date** and **datetime**: Modules from the `datetime` library to handle date operations.

### Initialization
- An instance of `CurrencyConverter` is created to perform currency conversions.
- A list of supported currency codes is defined in the `limit` variable.

### User Interaction
- The user is prompted to select currencies and enter the amount they wish to convert.
- The user can choose to convert based on the latest rates or specify a date for historical rates.

### Conversion Logic
The user can input:
- The amount of currency to convert.
- The currency code for the original currency.
- The currency code for the target currency.
- Whether they want to use the latest rates or specify a date.

If a date is specified, it must be on or before September 30, 2024; otherwise, an error message is displayed.

### Error Handling
- The script checks if the entered currency codes are valid by comparing them against the `limit` list.
- It ensures that the specified date is valid and within the allowed range.

### Exit Condition
- The user can exit the loop by entering `DONE`.

## Example Usage
1. Run the script.
2. Follow the prompts to input the desired values:
   - Enter `DONE` to stop the program.
   - Specify whether you want to use a date for conversion.
   - Enter the amount and currency codes.
3. The script will output the converted amount.

## Limitations
- The conversion is limited to the currencies specified in the `limit` list.
- The date for historical conversion is restricted to a maximum of September 30, 2024.

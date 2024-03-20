import requests
import csv
import emoji

def check_if_eurozone(country_name):
    with open('euro_countries.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].upper() == country_name.upper():
                return True
        return False

def get_currency_code(country_name):
    with open('big-mac-2023-index.csv', 'r') as file:
        reader = csv.reader(file)
        if check_if_eurozone(country_name):
            return "EUR"
        else:
            for row in reader:
                if row[3].upper() == country_name.upper():
                    return row[2]
            print(f"Currency code for {country_name} not found.")
            return None

def get_big_mac_price(country_name):
    with open('big-mac-2023-index.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3].upper() == country_name.upper():
                return float(row[4])
        print(f"Big Mac price for {country_name} not found.")
        return None


def get_exchange_rate(base_currency, target_currency):

    api_url = f"https://open.er-api.com/v6/latest/{base_currency}"

    response = requests.get(api_url)

    if response.status_code == 200: # Check if the request was successful
        data = response.json()
        if data['result'] == 'success':
            rate = data['rates'].get(target_currency)
            if rate:
                return rate
            else:
                print(f"Rate for {target_currency} not found.")
                return None
        else:
            print("Failed to fetch data: ", data.get('error-type', 'Unknown error'))
            return None
    else:
        print(f"Failed to connect to the API: Status code {response.status_code}")
        return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)

    if rate is not None:
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Failed to get the conversion rate.")
        return None

if __name__ == "__main__":
    print("Welcome to the Backpacker's Currency Converter! " + emoji.emojize(':world_map: :backpack: :currency_exchange:'))
    print("This tool helps you understand your purchasing power in different countries. " + emoji.emojize(':money_with_wings:' + ' :receipt:'))
    
    while True:
        try:
            amount = float(input("Enter the amount you'd like to convert " + emoji.emojize(':money_bag:')+ ": "))
            if amount < 0:
                print("The amount cannot be negative. Please enter a positive number.")
            else:
                break
        except ValueError:
            print("That's not a valid number. Please enter a numeric value." + emoji.emojize(':plus:'))
    
    while True:
        country_origin = input("Enter the name of the country you're currently in: ").capitalize()
        base_currency = get_currency_code(country_origin)
        if base_currency is not None:
            print(f"Great! The currency code for {country_origin} is {base_currency}.")
            break
        else:
            print(f"Sorry, we couldn't find the currency code for {country_origin}. Please try again." + emoji.emojize(':face_with_rolling_eyes:'))
    
    while True:
        country_target = input("Enter the name of the country you plan to visit: ").capitalize()
        target_currency = get_currency_code(country_target)
        if target_currency is not None:
            print(f"Awesome! The currency code for {country_target} is {target_currency}.")
            break
        else:
            print(f"Sorry, we couldn't find the currency code for {country_target}. Please try again." + emoji.emojize(':face_holding_back_tears:'))
    
    result = convert_currency(amount, base_currency, target_currency)
    
    if check_if_eurozone(country_target):
        target_bigmac_price = get_big_mac_price("Euro area")
    else:
        target_bigmac_price = get_big_mac_price(country_target)
    
    bigmac_result = result / target_bigmac_price if target_bigmac_price else 0
    
    if result is not None:
        print(f"{amount} {base_currency} is equivalent to {result:.2f} {target_currency} {emoji.emojize(':money_bag:')}")
        if bigmac_result:
            print(f"With this amount, you can buy {bigmac_result:.2f} Big Macs in {country_target} {emoji.emojize(':hamburger:')}")
        else:
            print(f"Sorry, we couldn't find the Big Mac price for {country_target}.")
    else:
        print(f"Conversion failed. Please check your inputs or the API availability. {emoji.emojize(':warning:')}")
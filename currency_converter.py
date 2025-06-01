#!/usr/bin/env python3

import os
from datetime import datetime

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': 1.0, 'EUR': 0.85, 'GBP': 0.73,
            'CAD': 1.25, 'JPY': 110.0, 'AUD': 1.35,
            'CHF': 0.92, 'CNY': 6.45
        }
        self.app_env = os.getenv('APP_ENV', 'development')
        self.api_endpoint = os.getenv('API_ENDPOINT', 'localhost:8080')

    def get_supported_currencies(self):
        return list(self.exchange_rates.keys())

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {from_currency}")
        if to_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {to_currency}")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        usd_amount = amount / self.exchange_rates[from_currency]
        converted = usd_amount * self.exchange_rates[to_currency]
        return round(converted, 2)

    def get_exchange_rate(self, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Unsupported currency")
        return round(self.exchange_rates[to_currency] / self.exchange_rates[from_currency], 4)

    def display_info(self):
        print("Currency Converter Application")
        print(f"Environment: {self.app_env}")
        print(f"API Endpoint: {self.api_endpoint}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Supported currencies: {', '.join(self.get_supported_currencies())}")
        print("-" * 50)

def main():
    converter = CurrencyConverter()
    converter.display_info()
    print("Welcome to Currency Converter! Type 'quit' to exit.")

    while True:
        try:
            from_curr = input("From currency: ").upper().strip()
            if from_curr == 'QUIT':
                break
            to_curr = input("To currency: ").upper().strip()
            if to_curr == 'QUIT':
                break
            amount_str = input("Amount: ").strip()
            if amount_str.lower() == 'quit':
                break
            amount = float(amount_str)
            result = converter.convert(amount, from_curr, to_curr)
            rate = converter.get_exchange_rate(from_curr, to_curr)
            print(f"{amount} {from_curr} = {result} {to_curr}")
            print(f"Exchange rate: 1 {from_curr} = {rate} {to_curr}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()


# Backpacker's Currency Converter

## Introduction
Welcome to the Backpacker's Currency Converter! This application is designed to help travelers understand their purchasing power in different countries. By leveraging the Big Mac index and current exchange rates, this tool offers a unique perspective on currency value, going beyond mere numerical conversion.

## Motivation
The motivation behind this project is to provide a more nuanced understanding of currency value when traveling. Exchange rates alone do not offer a complete picture of one's purchasing power in a foreign country. By integrating the Big Mac index, users gain insights into how far their money will go in real terms, enhancing their travel planning and budgeting.

## Features
- Convert currencies using real-time exchange rates provided by an OpenAPI (no key needed).
- Compare the value of currencies based on the Big Mac index.
- Check if a country is part of the Eurozone and use the appropriate currency code.
- Interactive user prompts for an engaging experience.

## How It Works
- **Currency Conversion:** Users can convert an amount from one currency to another using up-to-date exchange rates.
- **Big Mac Index Comparison:** The application calculates how many Big Macs one can buy in the target country with the converted amount, offering a relatable measure of purchasing power.
- **Eurozone Check:** Automatically identifies if the target country uses the Euro, simplifying the process for countries sharing a common currency.
- **Interactive Prompts:** Engages users with step-by-step instructions, ensuring ease of use.

## Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/thiago4go/cs50p-final-project.git
   ```
2. Install required Python packages:
   ```bash
   pip install requests emoji
   ```
3. Run the script:
   ```bash
   python currency_converter.py
   ```

## Code Examples
Show how your project can be used with some code examples. Highlight features like currency conversion and Big Mac index comparison.

## Data Sources
- The Big Mac index data is sourced from [The Economist's latest release](https://github.com/TheEconomist/big-mac-data).
- Exchange rates are fetched from a real-time currency exchange API.

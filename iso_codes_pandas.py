from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd 

iso_codes = pd.read_html("https://www.iban.com/country-codes")

df = iso_codes[0]
df = df['Alpha-3 code'].to_string(index=False)

with open("./countries.txt", "w") as f:
    f.write(df)

my_list = []
file = open("./countries.txt", "r")
countries = file.read()
my_list = countries.split('\n')

countries_string_single_quotes = ','.join(f"'{x}'" for x in my_list)

countries_string_double_quotes = ','.join(f'"{x}"' for x in my_list)

with open("./countries_as_list_single_quotes.txt", "a") as f:
    f.write(countries_string_single_quotes)

with open("./countries_as_list_double_quotes.txt", "a") as f:
    f.write(countries_string_double_quotes)
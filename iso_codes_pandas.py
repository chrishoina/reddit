# Libraries used in this code
from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd 

# I found these ISO country codes on the below URL. Pandas makes it pretty easy to read html and manipulate it. Very cool!
iso_codes = pd.read_html("https://www.iban.com/country-codes")

# I create a dataframe, starting a index of 0.
df = iso_codes[0]

# But really all I care about is the 3-digit country code. So I'll make that the df (dataframe) and strip out the index
df = df['Alpha-3 code'].to_string(index=False)

# From here I'll save this little guy as a text file.
with open("./countries.txt", "w") as f:
    f.write(df)

# I'll set up a list. *** This was my approach, but I'm sure there is a better way, feel free to comment or adjust ***
my_list = []

# Then I'll open that text file and read it in.
file = open("./countries.txt", "r")
countries = file.read()

countries 
# I need to remove the "new line" identifiers; so I'm doing that here. 
my_list = countries.split('\n')

# Once I do that, I can create two new strings. I do this with f-Strings. Great article on using them here: https://realpython.com/python-f-strings/ 

# I have two options here: one where the codes are contained by single quotes, the other with double quotes. Oracle Autonomous Database likes single quotes, but your DB may differ.

countries_string_single_quotes = ','.join(f"'{x}'" for x in my_list)

countries_string_double_quotes = ','.join(f'"{x}"' for x in my_list)

# From here I just take those strings and save them in a text file. You don't have to do this, you can just print out the string and copy/paste. But if you want to refer to these later without having to run all the code, this might be a nice addition. 

with open("./countries_as_list_single_quotes.txt", "a") as f:
    f.write(countries_string_single_quotes)

with open("./countries_as_list_double_quotes.txt", "a") as f:
    f.write(countries_string_double_quotes)
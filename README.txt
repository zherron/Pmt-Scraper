Python dependencies:
datetime
schedule
time
csv
scrapy

This Project is meant to be run in the background on a computer,
and at 9:00am every day, it scrapes pricing data from RemitRate.com
(https://www.remitrate.com/best-exchange-rates/compare-USD-to-PHP) 
This data is exported to quotes.csv

However, due to legacy reasons, scrapy always appends to the end of a
csv file. This results in the headers ("datetime accessed",
"company name", etc.) being duplicated. The daily_runner.py
includes a function "clean_quotes_csv" that reads the "quotes.csv"
file, and writes to "quotes_cleaned.csv" only if the data is not a 
duplicate header.

The time module is used to make sure the program runs at 9 each morning,
so remember to restart the script if you restart your computer. The
frequency with which the program runs is determined in the daily_runner.py
file

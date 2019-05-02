Python dependencies:
datetime
schedule
time
csv
scrapy

HOW TO USE:
Just run the daily_runner.py file. Everything else should work in the background.
Data is exported to quotes_cleaned.csv, so you can do analysis on that data once exported 
to a different file.

------------------EXPLANATION----------------------------
This Project is meant to be run in the background on a computer,
and at 10:00am every day, it scrapes pricing data from RemitRate.com
(https://www.remitrate.com/best-exchange-rates/compare-USD-to-PHP) 
This data is exported to quotes.csv

However, due to legacy reasons, scrapy always appends to the end of a
csv file. This results in the headers ("datetime accessed",
"company name", etc.) being duplicated. The daily_runner.py
includes a function "clean_quotes_csv" that reads the "quotes.csv"
file, and writes to "quotes_cleaned.csv" only if the data is not a 
duplicate header.

The time module is used to make sure the program runs at 10 each morning,
so remember to restart the script if you restart your computer. The
frequency with which the program runs is determined in the daily_runner.py
file

-------------------CSV EXPLANATION--------------------
Columns:
- datetime accessed : time the program was run
- company name : self explanatory
- time units : whether guaranteed delivery date is in hours or days
- time : guaranteed delivery time
- locked-in rate : guaranteed exchange rate
- fees string : (NONINTUITIVE NAME)
    This is calculated by the website by starting with $1,000 USD
    and then subtracting the fee, so the value shown is the amount
    of USD after the fee. 
    E.g. $1,000 (USD) - $5 (fee) = $995 (fees string)
    NOTE: If InstaRem has a value OVER $1,000, it is because they
          are offering promotions (right now of $20). Subtract $20
          to have a fee comparable to the others
- total PHP amt : total amount of PHP received from a hypothetical
    $1,000 USD sent, after accounting for fees and FX spread
- effective rate : effective exchange rate, after accounting for
    fees and FX spread

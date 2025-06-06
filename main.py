#!/opt/anaconda3/bin/python3

import pandas as pd
from datetime import datetime, timedelta
import re
from data_load import load_checkout_data, inspect_rows, inspect_unique_values
from overdue_checker import print_overdue, check_for_overdue, print_overdue_rows
from FuzzyDateParser import FuzzyDateParser




# ------------------------------
# Main Logic
# ------------------------------
if __name__ == "__main__":

    FILE_PATH = "LIB 80 Equipment Checkouts.xlsx"
    df = load_checkout_data(FILE_PATH)

    inspect = input('would you like to inspect the data before parsing?').lower().strip()
    if inspect == 'yes':
        print(df.head())
        inspect_rows(df)
        inspect_unique_values(df)

    if df is not None:
        parser = FuzzyDateParser(df)
        parser.df['Parsed Return Date'] = parser.df.apply(parser.parse_row, axis=1)
        overdue_list = check_for_overdue(parser.df)
        print_overdue(parser.df, overdue_list)

    
    
    print_overdue_rows(df)


# Modules in Python --> Most used library in python is CSV but Request library we will use in API Automation

import pandas as pd

try:
    df = pd.read_csv("TestData.csv")
    print(df)
except FileNotFoundError as fe:
    print("File doesn't exist")


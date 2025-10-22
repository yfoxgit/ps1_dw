# Data Wrangling Optional Exericse

# Creation of Data
import pandas as pd

# Task 1: recreate dataframe
df = pd.DataFrame({"household_id":[1,2,3,3,4,5,5,5],
        "person":[1,1,1,2,1,1,2,3],
        "age":[20, 40, 35, 10, 18, 2,30,70],
        "income": [20000, 50000, 60000, 0, 5000, 0, 40000, 12000],
        "female": [True, False, True, False, False, True, True, True]})
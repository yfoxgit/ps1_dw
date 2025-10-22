# Data Wrangling Optional Exericse

# Task 2:
# Function 1: convert data to long format
def agg_to_hh(df):
    '''aggregates by household
    counts the number of people
    calculates mean age
    calculates mean income
    sums to get the no. females'''
    df = df.groupby("household_id").agg({
       "person":"count",
       "age":"mean",
       "income":"mean",
       "female":"sum"
        })
    return df

# Function 2: rename columns
def rename(df):
    '''renames the columns'''
    df = df.columns['household_size', 'mean_age', 'mean_income', 'num_female']
    return df

# Function 3: reset index
def reset_index(df):
    df = df.reset_index()
    return df
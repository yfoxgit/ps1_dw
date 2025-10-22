# Data Wrangling Optional Exericse

# Task 2:
# Function 1: convert data to long format
def agg_to_hh(df):
    hh_df = df.groupby("household_id").agg({
       "person":"count",
       "age":"mean",
       "income":"mean",
       "female":"sum"
        })
    return hh_df

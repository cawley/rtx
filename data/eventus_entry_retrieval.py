import pandas as pd

# load the dataframe
df = pd.read_csv("eventus_table_match.csv")

# ask the user for the filter column name
filter_col_name = input("Enter the filter column name: ")

# ask the user for the matching column name
match_col_name = input("Enter the matching column name: ")

# get a list of the unique values in the filter column
filter_col_values = df[filter_col_name].unique()

# get all the rows where the matching column values are in the list
df_b = df[df[match_col_name].isin(filter_col_values)]

# save the result to a new csv file
df_b.to_csv(
    "table_with_matching_INPUT_or_duplicate_ID_of_matching_inputs.csv", index=False
)

print(
    "The result has been saved to 'table_with_matching_INPUT_or_duplicate_ID_of_matching_inputs.csv'"
)

import pandas as pd

# load the dataframe
df = pd.read_csv("eventus_table_match.csv")

# ask the user for the column name
col_name = input("Enter the column name: ")

# ask the user for the entry
entry = input("Enter the entry in the column: ")

# get all the rows where the chosen column equals the entry
df_a = df[df[col_name] == entry]

# find the entries in the chosen column that appear elsewhere in the dataframe
entries_in_col_a = df_a[col_name].unique()

# get all the rows where values in other columns are in entries_in_col_a
df_b = df[df.isin(entries_in_col_a).any(axis=1)]

# concatenate the dataframes
result_df = pd.concat([df_a, df_b]).drop_duplicates()

# save the result to a new csv file
result_df.to_csv(
    "table_with_matching_INPUT_or_duplicate_ID_of_matching_inputs.csv", index=False
)

print(
    "The result has been saved to 'table_with_matching_INPUT_or_duplicate_ID_of_matching_inputs.csv'"
)

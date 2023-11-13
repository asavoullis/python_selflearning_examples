# Python practise examples and tasks 9
import numpy as np
import pandas as pd

"""1  Making a Pandas DataFrame with null values and printing the dataframe showing where there are null values """
data = {
    'title': ['Squid Game', 'Angry Birds', 'Jaws', 'A Cinderella Story', 'Charmed'],
    'director': [np.nan, np.nan, 'Steven Spielberg', 'Mark Rosman', np.nan],
    'country': [np.nan, 'Finla', 'United States', 'United States, Cana', 'United Stat'] }
productions = pd.DataFrame(data)
# Print the DataFrame indicating missing values as True 
print(productions.isnull())
print("") 


"""2 Find and print the first duplicate of the entry """
data = {
    'title': ['The Great British Baking Show', 'The Great British Baking Show', 'Jaws', 'A Cinderella Story', 'A Cinderella Story', 'Kung Fu Panda', 'Kung Fu Panda'],
    'release_year': [2021, 2021, 1975, 2004, 2004, 2008, 2008],
    'country': ['UK', 'UK', 'USA', 'USA', 'Canada', 'USA', 'China']}
productions = pd.DataFrame(data)
# Find and print duplicate rows based on the subset of columns, keep='first' only shows the first one - not all its occurances
df = productions[productions.duplicated(subset=['title', 'country'], keep='first')]
print(df['title'])
print("")


"""3  """
data = {
    'title': ['The Great British Baking Show', 'The Great British Baking Show', 'Jaws', 'A Cinderella Story', 'A Cinderella Story', 'Kung Fu Panda', 'Kung Fu Panda'],
    'release_year': [2021, 2021, 1975, 2004, 2004, 2008, 2008],
    'country': ['UK', 'UK', 'USA', 'USA', 'USA', 'USA', 'USA']} # now the countries also match
productions = pd.DataFrame(data)
# Find and print duplicate rows based on the subset of columns, keep='first' only shows the first one - not all its occurances
df = productions[productions.duplicated()]
print(df['title'])
print("")


"""4 Drop the duplicates in the productions Pandas DataFrame NOT in PLACE  """
# This code uses the drop_duplicates() method to remove duplicate rows from the 'productions' DataFrame based on all columns 
# Then prints the 'title' column of the resulting DataFrame.
print(productions.drop_duplicates()['title'])
print("")


"""5 Making new column and summing up the rows """
data = {
    'title': ['Jaws', 'A Cinderella Story', 'Kung Fu Panda'],
    'minutes': [126.0, 95.0, 94.0],
    'hours': [2.1, 1.583333, 1.566667]}
movies = pd.DataFrame(data)
# Calculate 'hours_to_min' column
movies['hours_to_min'] = movies['hours'] * 60
# Print the sum of 'hours_to_min' and 'minutes'
print(movies[['hours_to_min', 'minutes']].sum())
print("")


"""6 Dropping rows with null (None) values """
data = {
    'title': ['Squid Game', 'Angry Birds', 'Jaws', 'A Cinderella Story', 'Charmed'],
    'director': [None, None, 'Steven Spielberg', 'Mark Rosman', None],
    'count': [None, 'Finland', 'United States', 'United States, Canada', 'United States']}
productions = pd.DataFrame(data)
# Drop rows with missing values 
cleaned = productions.dropna()
print(cleaned['title'].head())
print("") 


"""7 You are counting inconsistences in the 'type' column . """
data = {'type': ['TV Show', 'MOVIE', 'movie', 'Movie', 'TV SHOW'],
        'title': ['The Great British Baking Show', 'Jaws', 'A Cinderella Story', 'Kung Fu Panda', 'Dear White People']}
df = pd.DataFrame(data)
# Grouping the DataFrame by the 'title' column and counting the occurrences of each group
counts = df.groupby("type").count()
# Renaming the column containing counts to 'counts'
counts.columns = ['counts']
print(counts.head())
print("")


"""8  """
data = {'title': [41, 61, 127, 573],
        'duration': [2.1, 1.6, 95, 94],
        'dur_unit': ['hrs', 'hrs', 'min', 'min']}
movies = pd.DataFrame(data)
# Extracting rows where the unit is 'min' and calculating the duration in hours
hrs = movies.loc[movies['dur_unit']=='min','duration'] / 60
# Updating the 'duration' column for rows where the unit is 'min' with the calculated hours
movies.loc[movies['dur_unit']=='min','duration'] = hrs

# Updating the 'unit' column for rows where the unit is 'min' to 'hours'
movies.loc[movies['dur_unit']=='min','dur_unit'] = 'hours'

# Rounding the 'duration' column to the nearest whole number and printing the result
print(movies['duration'].round())
print("")


"""9 Setting index to be the Geography column and printing rows that have Spain as index """
data = {'surname': ['Hargrave', 'Hill', 'Onio', 'Boni', 'Mitchell'],
    'credit_score': [619, 608, 502, 699, 850],
    'geography': ['France', 'Spain', 'France', 'France', 'Spain'],
    'age': [42, 41, 42, 39, 43],
    'exited': ['Yes', 'No', 'Yes', 'No', 'No']}
churn = pd.DataFrame(data)
# Setting the index of the DataFrame to be the 'geography' column
churn_ind = churn.set_index("geography")
# Printing the rows where the 'geography' is 'Spain'
print("Rows with 'geography' as 'Spain':")
print(churn_ind.loc['Spain'])
print("")


"""10 Printing the mean and median of the credit_scores column """
print(churn["credit_score"].agg([np.mean, np.median]))
print("")


"""11 Calculating the Cumulative Sum of a Column """
print(churn["credit_score"].cumsum().head())
print("")


"""12  """
data = {'date': ['2018-01-15', '2018-01-15', '2018-01-16', '2018-01-16', '2018-01-17'],
        'product_line': ['Health and beauty', 'Electronic accessories', 'Home and lifestyle', 'Sports', 'Food and beverages'],
        'product': ['Shampoo', 'Headphones', 'Lamp', 'Yoga mat', 'Milk'],
        'unit_price': [6.99, 25.28, 46.33, 39.99, 5.99]}
sales = pd.DataFrame(data)
# Creating a pivot table to analyze sales data by product line, calculating mean and median unit prices
print(sales.pivot_table(values="unit_price", index="product_line", aggfunc=[np.mean, np.median]))
print("")


"""13 Set 2 columns as index of churn  """
data = {'surname': ['Hargrave', 'Hill', 'Onio', 'Boni', 'Mitchell'],
    'geography': ['France', 'Spain', 'France', 'France', 'Spain'],
    'credit_score': [619, 608, 502, 699, 850],
    'age': [42, 41, 42, 39, 43],
    'exited': ['Yes', 'No', 'Yes', 'No', 'No']}
churn2 = pd.DataFrame(data)
# Setting the index of the DataFrame to be a MultiIndex with columns 'surname' and 'geography'
churn_ind = churn2.set_index(['surname', 'geography'])
# Printing rows with surnames 'Hill' and 'Mitchell' using the loc method
print(churn_ind.loc[['Hill', 'Mitchell']])
print("")


"""14 iloc """
# Printing a subset of rows and columns using integer-based indexing
# Rows 2 to 3 (exclusive) and columns 1 to 1 (exclusive) are selected
# Note: In Python, indexing is zero-based, so index 2 corresponds to the third row.
print(churn.iloc[2:4, 1:2])
print("")


"""15 Printing the sum of None/Null Values of each column in the Dataframe """
data = {'surname': ['Hargrave', 'Hill', 'Onio', 'Boni', 'Mitchell', 'Chu'],
        'credit_score': [619.0, 608.0, 502.0, 699.0, 850.0, None],  # Using None to represent NaN
        'geography': ['France', 'Spain', 'France', 'France', 'Spain', 'Spain'],
        'age': [42.0, 41.0, None, 39.0, 43.0, 44.0],  # Using None to represent NaN
        'exited': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes']}
churn = pd.DataFrame(data)
print("Sum of None/Null Values of each column in the Dataframe ")
print(churn.isna().sum())
print("")


"""16 Filling those None/Null values of each column in the Dataframe """
churn_filled = churn.fillna('Not Available')
# Displaying the DataFrame 'churn_filled' after filling NaN values
print("\nDataFrame after filling NaN values:")
print(churn_filled.head(6))
print("")


"""17 Subset of churn2 that contains rows where the Column Geography is either Germany or France """
# Creating a subset of the 'churn2' DataFrame containing only the 'surname', 'geography', and 'exited' columns
churn_subset = churn2[['surname', 'geography', 'exited']]
# Filtering the 'churn_subset' DataFrame to include only rows where 'geography' is either 'Germany' or 'France'
churn_filter = churn_subset[churn_subset["geography"].isin(["Germany", "France"])]
# Displaying the first few rows of the filtered DataFrame 'churn_filter'
print(churn_filter.head())
print("")


"""18  """

print("")


"""19  """

print("")


"""20  """

print("")


"""21  """

print("")


"""22  """

print("")


"""23  """

print("")


"""24  """

print("")


"""25  """

print("")


"""26  """

print("")


"""27 """

print("")


"""28  """

print("")


"""29  """

print("")


"""30   """

print("")


"""31  """

print("")


"""32  """

print("")


"""32  """

print("")


"""32  """

print("")


"""33 """

print("")


"""34 """

print("")


"""35 """

print("")


"""36 """

print("")


"""37 """

print("")


"""38 """

print("")


"""39 """

print("")


"""40 """

print("")


"""41 """

print("")
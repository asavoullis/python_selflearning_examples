# Python practise examples and tasks 9
import numpy as np
import pandas as pd

"""1  Making a Pandas DataFrame with null values and printing the dataframe showing where there are null values """
data = {'title': ['Squid Game', 'Angry Birds', 'Jaws', 'A Cinderella Story', 'Charmed'],
    'director': [np.nan, np.nan, 'Steven Spielberg', 'Mark Rosman', np.nan],
    'country': [np.nan, 'Finla', 'United States', 'United States, Cana', 'United Stat'] }
productions = pd.DataFrame(data)
# Print the DataFrame indicating missing values as True 
print(productions.isnull())
print("") 


"""2 Find and print the first duplicate of the entry """
data = {'title': ['The Great British Baking Show', 'The Great British Baking Show', 'Jaws', 'A Cinderella Story', 'A Cinderella Story', 'Kung Fu Panda', 'Kung Fu Panda'],
    'release_year': [2021, 2021, 1975, 2004, 2004, 2008, 2008],
    'country': ['UK', 'UK', 'USA', 'USA', 'Canada', 'USA', 'China']}
productions = pd.DataFrame(data)
# Find and print duplicate rows based on the subset of columns, keep='first' only shows the first one - not all its occurances
df = productions[productions.duplicated(subset=['title', 'country'], keep='first')]
print(df['title'])
print("")


"""3  """
data = {'title': ['The Great British Baking Show', 'The Great British Baking Show', 'Jaws', 'A Cinderella Story', 'A Cinderella Story', 'Kung Fu Panda', 'Kung Fu Panda'],
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
data = {'title': ['Jaws', 'A Cinderella Story', 'Kung Fu Panda'],
    'minutes': [126.0, 95.0, 94.0],
    'hours': [2.1, 1.583333, 1.566667]}
movies = pd.DataFrame(data)
# Calculate 'hours_to_min' column
movies['hours_to_min'] = movies['hours'] * 60
# Print the sum of 'hours_to_min' and 'minutes'
print(movies[['hours_to_min', 'minutes']].sum())
print("")


"""6 Dropping rows with null (None) values """
data = {'title': ['Squid Game', 'Angry Birds', 'Jaws', 'A Cinderella Story', 'Charmed'],
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


"""12  Creating a pivot table to analyze sales data  """
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


"""14 iloc Printing a subset of rows and columns using integer-based indexing """
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
books_data = {'title': ['Of Mice and Men', 'The Hobbit', 'The Lord of the Rings'],
    'num_pages': [352, 277, 1184],
    'author': ['John Steinbeck', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
    'book_id': [142000671, 261103288, 618517650]}
books_df = pd.DataFrame(books_data)
publication_data = {'publication_date': ['2003-11-01', '2004-06-15', '2007-09-17'],
    'publisher': ['Penguin Books', 'Harper', 'HarperCollins'],
    'book_id': [142000671, 60749911, 261103288]}
publication_df = pd.DataFrame(publication_data)
books_publication = books_df.merge(publication_df, on='book_id', how='left')
print("books and publication left join : \n", books_publication.head())
print("")


"""19 Slicing use loc[:, ] """
# To slice a DataFrame, the index must first besorted using .sort_index() .
# To slice rows at the outer index level, call .loc[] on the DataFrame and pass it the first and last index values
# separated by a : . Unlike lists, the final value is included in the slice.

data = {'geography': ['France', 'France', 'France', 'France', 'France'],
    'surname': ['Bartlett', 'Bearce', 'Boni', 'Chin', 'Hao'],
    'credit_score': [822, 528, 699, 549, 684],
    'age': [50, 31, 39, 25, 27],
    'exited': ['No', 'No', 'No', 'No', 'No']}
churn_srt = pd.DataFrame(data)
churn_srt.set_index(['geography', 'surname'], inplace=True)
# churn_srt = churn.set_index(["geography", "surname"]).sort_index()
print(churn_srt.loc[: , 'credit_score':'age'].head())
print("")


"""20  Replace entries in the type column from TVShow to TV Show """
data = {'type': ['TVShow', 'Movie', 'Movie', 'Movie', 'TVShow'],
    'title': ['The Great British Baking Show', 'Jaws', 'A Cinderella Story', 'Kung Fu Panda', 'Dear White People']}
prod_types = pd.DataFrame(data)
prod_types["type"] = prod_types["type"].replace({"TVShow":"TV Show"})
print(prod_types.head())
print("")


"""21 Filter the productions df to include only the rows where the 'director' column has missing values (NaN / None) """
print(productions)
print("")
not_cleaned = productions[productions['director'].isna()]
print(not_cleaned.head())
print("")


"""22  """
data = {'tv_show_title': ['The Great British Baking Show', 'Squid Game', 'Charmed', 'Never Have I Ever', "Kim's Convenience"],
    'seasons': [9, 1, 3, 2, 5]}
tv = pd.DataFrame(data)
print(tv)
# Updating values in the 'seasons' column where the condition 'tv['seasons'] > 2' is met
# The values in the 'seasons' column for rows where the condition is True will be set to 2
tv.loc[tv['seasons'] > 2, 'seasons'] = 2
print("")
print(tv.head())
print("")


"""23 Change the value from 2 to 5 for the TV show Never Have I Ever """
tv.loc[tv['tv_show_title'] == 'Never Have I Ever', 'seasons'] = 5
print(tv.head())
print("")


"""24 Find unique - distinct values of the tv_show_title from the tv DF """
print(tv['tv_show_title'].unique())
print("")


"""25 Fill the null values in the country column with 'USA' """
data = {'title': ['Squid Game', 'Angry Birds', 'Jaws', 'Charmed', 'The Vault'],
    'director': [None, None, 'Steven Spielberg', None, 'Jaume Balagueró'],
    'country': ['South Korea', 'Finland', None, None, None],
    'year': [1994, 1993, 2002, 2004, 2011]}
productions = pd.DataFrame(data)
productions['country'] = productions['country'].fillna('USA') 
print(productions)
print("")


"""26 Categorize the movies DataFrame into discrete intervals. use pd.cut """
data = {'title': ['Jaws', 'A Cinderella Story', 'Dennis the Menace', 'Kung Fu Panda'],
    'release_year': [1975, 2004, 1993, 2008]}
movies = pd.DataFrame(data)
label_ranges = [1970, 2000, 2010, np.inf]
label_names = ['Pre-millenium', 'Early-2000s', 'Recent']
movies['labels'] = pd.cut(movies["release_year"], bins = label_ranges, labels = label_names)
print(movies[['title','labels']].head())
print("")


"""27 """
data = {'title': ['Dear White People', 'Angry Birds', 'Angry Birds', 'Jaws', 'Jaws'],
    'rating': ['TV-MA', 'TV-Y7', 'TV-Y7', 'PG', 'PG']}
df = pd.DataFrame(data)
# df.duplicated(), it returns a boolean Series where each element is True if the corresponding row is a duplicate 
# (i.e., it has appeared earlier in the DataFrame) and False otherwise.
# df.duplicated(): This generates a boolean Series indicating whether each row is a duplicate.
# df[df.duplicated()]: This filters the DataFrame df to include only the rows where df.duplicated() is True. 
# In other words, it selects only the duplicate rows.
print(df[df.duplicated()])
print("")


"""28 Print the dataframe with True if the entry is null or False if its not """
print(productions.isnull())
print("")


"""29 Strip the min from the duration column and rename the column to duration_in_minutes """
data = {'title': ['Kung Fu Panda', 'Kung Fu Panda 2', 'Life as We Know It', 'Mary Magdalene', 'Memoirs of a Geisha'],
    'duration': ['94 min', '93 min', '115 min', '120 min', '145 min'],
    'year_released': [1993, 1994, 2000, 2020, 2022]}
movies = pd.DataFrame(data)
movies["duration"] = movies['duration'].str.strip(' min') 
movies = movies.rename(columns={'duration': 'duration_in_minutes'})
print(movies.head())
print("")


"""30  Change data type of a column and also assert test  """
# Convert duration_in_minutes to int64
movies['duration_in_minutes'] = movies['duration_in_minutes'].astype('int64')
print(movies.dtypes)
print("")
assert movies['title'].dtype == 'object'
print(movies.dtypes)
print("")


"""31  """
matches = [('TV Show', 100), ('TVShow', 92), ('MOVIE', 31), ('movie', 31), ('Movie', 31)]
for match in matches:
    if match[1] >= 80:
        prod_types.loc[prod_types['type'] == match[0]] = 'TV Show'
print(prod_types['type'].head())
print("")


"""32 Inspect the df and check if the title column contains Fu or Mary """
# Extract the 'title' column from the DataFrame 'movies' and check if each entry contains the substrings "Fu" or "Mary"
# The result is a boolean Series where True indicates a match and False indicates no match
df2 = movies['title'].str.contains("Fu|Mary")
print(df2.head())
print("")


"""33 Extract the 'rating' column and the index column from the DataFrame """
print(sales)
print("")
index = sales.index.get_level_values(0)
print(index)
print("")
result = pd.Index(sales['date'])
print(result)
print(type(result))
print("")


"""34  """
data = {'title': ['Jaws', 'A Cinderella Story', 'Kung Fu Panda', 'The Shawshank Redemption', 'The Godfather', 'Inception', 'Forrest Gump', 'Pulp Fiction'],
    'minutes': [126.0, 95.0, 94.0, 142.0, 175.0, 148.0, 142.0, 154.0],
    'hours': [2.1, 1.583333, 1.566667, 2.366667, 2.916667, 2.466667, 2.366667, 2.566667]}
movies = pd.DataFrame(data)
# Create a new column 'hours_to_min' by multiplying the 'hours' column by 60
movies['hours_to_min'] = movies['hours'] * 60
# Print the DataFrame with only the 'hours_to_min' and 'minutes' columns
print(movies[['hours_to_min', 'minutes']])
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


"""42 """

print("")


"""43 """

print("")
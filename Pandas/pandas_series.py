import numpy as np
import pandas as pd
import matplotlib as plt
# ==============================================================================
# 1. PANDAS SERIES CREATION
# ==============================================================================

# Series using a List
country = ["india", "nepal", "pakistan", "us", "uk"]
print("--- Country Series ---")
print(pd.Series(country))

# Series with defined Data Type
runs = [23, 45, 78, 100, 98, 32, 11, 32, 10, 9, 8]
print("\n--- Runs Series ---")
runs_series=pd.Series(runs, dtype="Int32")

# Custom Indexing and Naming
marks = [30, 60, 80, 90, 100]
subject = ["math", "english", "cs", "sst", "electronics"]
marks_series = pd.Series(marks, index=subject, name="ayan ke marks")
print("\n--- Custom Index Marks ---")
print(marks_series)

# Series using a Dictionary
marks_dict = {"math": 40, "english": 70, "science": 90}
marks_dict_series = pd.Series(marks_dict, name="my marks")
print("\n--- Dictionary Series ---")
print(marks_dict_series)


# ==============================================================================
# 2. SERIES ATTRIBUTES
# ==============================================================================
print("\n=== Series Attributes ===")
print("Size (includes missing values):", marks_dict_series.size)
print("Data Type:", marks_dict_series.dtype)
print("Series Name:", marks_dict_series.name)
print("Are values unique?:", marks_dict_series.is_unique)
print("Index Labels:", marks_dict_series.index)
print("Values Array:", marks_dict_series.values)


# 3. WORKING WITH A CSV FILE

# Loading data as a Series directly using squeeze()
csv_path = r"C:\Users\hp\Python fundamentals\smartphones.csv"

# Note: squeeze=True can also be used inside read_csv depending on pandas version
smartphones = pd.read_csv(csv_path).squeeze("columns")



# 4. SERIES METHODS

print("\n=== Head, Tail & Sample ===")
print(smartphones.head(4))  # Top 4 rows
print(smartphones.tail())  # Last 5 rows (default)
print(smartphones.sample(3))  # 3 random rows

print("\n=== Value Counts (Frequency) ===")
print(smartphones.value_counts())

print("\n=== Sorting ===")
# Corrected typo 'accending' -> 'ascending'
# Note: if it's a 1D Series, sort_values doesn't take a 'by' parameter
print(smartphones.sort_values(by='price'))
print(smartphones.sort_index())



# 5. MATHEMATICAL & STATISTICAL METHODS

print("\n=== Math & Descriptive Statistics ===")
print("Count (excludes NaN):", smartphones.count())
print("Size (includes NaN):", smartphones.size)

# Added () to execute the methods properly
print("Sum:", smartphones.sum(numeric_only=True))
print(smartphones.cumsum())
print(smartphones.columns)
# print("means is :",smartphones['price'].mean())
# print("Median:", smartphones.median(numeric_only=True))
print("Mode:\n", smartphones.mode())
# print("Standard Deviation:", smartphones.std())
# print("Variance:", smartphones.var())
# print("Min:", smartphones.min())
# print("Max:", smartphones.max())

print("\n=== Summary Statistics ===")
print(smartphones.describe())


# 6. SERIES INDEXING & SLICING

print("\n=== Indexing & Slicing ===")
# The Difference Between .loc(original indexing ) and .iloc(absolute indexing like 0,1,2,3,4....)

# Integer Indexing
print("Element at index 10:", smartphones.iloc[10])

# Slicing
print("\nSlicing index 5 to 9:")
print(smartphones.iloc[5:10])

# Fancy Indexing
print("\nFancy Indexing (Specific indices):")
print(smartphones.iloc[[1, 2, 30, 43, 54]])

#series with python functionlietes 

#type/len/dir/sorted/max/min
print('lenght of smarphones :',len(smartphones))
print('type is  :',type(runs_series))
print('dir is :',dir(runs_series))
print('sorted ',sorted(runs_series )) #but store in list    
print('max is ',max(runs_series))
print('min is  :',min(runs_series))

#type conversion 
dict(marks_series)
print(type(marks_series))

#airthmatic operation 
print(100-marks_series)

#realtional operation 
print(marks_series>50)


#booleans indexing (booleans series use as index )
print("marks >40 is :",marks_series[marks_series>40].size )

#ploting graphs (using pandas )
plot_object=runs_series.plot(kind="pie")
print(plot_object.figure.savefig('image.png'))



# 7. DISPLAY FINAL SERIES

# print("\n=== Full Smartphones Series ===")
# print(smartphones)
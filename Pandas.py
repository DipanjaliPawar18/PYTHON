# Pandas 
"""pandas is a python library.
pandas is used to analyze data.
it has functions for analyzing, cleaning, exploring, and manipulating data."""

import pandas as pd

myDataSet = {
    "fruits": ["apple", "mango", "graps"],
    "quantity": [2, 5, 4]
}

myBasket = pd.DataFrame(myDataSet)

print(myBasket)


# checking pandas version
import pandas as pd

print(pd.__version__)

# pandas series: a pandas series is like a column in a table

import pandas as pd
a=[1,2,3,4]
myNum = pd.Series(a)
print(myNum)

# creating our own labels
myNum1 = pd.Series(a, index=["a", "b", "c", "d"])
print(myNum1)

# key/value objects as series

import pandas as pd
myInfo = {"name": "Dipanjali", "sch. no.": 31440, "branch": "ICB"}
aboutme= pd.series(myInfo)
print(aboutme)

# DATAFRAMES
# data sets in pandas are usually multi-dimentional tables,
# called as DataFrames.

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50,40,45]
}
myvar = pd.DataFrame(data)

print(myvar)
import pandas as pd

list_keys = list(['Country','Total'])
list_values = list([['United States', 'Soviet Union', 'Great Britain'],[1022, 395, 263]])

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = tuple(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

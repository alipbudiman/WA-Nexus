import pandas as pd
from prettytable import PrettyTable


print("FEATURE:")
df = pd.read_csv('document/feature.csv')

pt = PrettyTable()

pt.field_names = list(df)

for i in range(len(df)):
    pt.add_row(list(df.iloc[i]))

print(pt)

print("UPDATE:")
df = pd.read_csv('document/update.csv')

pt = PrettyTable()

pt.field_names = list(df)

for i in range(len(df)):
    pt.add_row(list(df.iloc[i]))

print(pt)

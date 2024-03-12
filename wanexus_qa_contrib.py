import pandas as pd

def replace_chars(input_string):
    # Replace "[" , "]" , and "," with "|"
    modified_string = input_string.replace("[", "|").replace("]", "|").replace(",", "|").replace("'", " ")
    return modified_string


df = pd.read_csv('document/feature.csv')

table = ""
table = f"\n{replace_chars(str(list(df.head())))}\n| --- | --- | --- |"
for i, data in enumerate(df):
    table += f"\n{replace_chars(str(list(df.iloc[i])))}\n| --- | --- | --- |" 
    

file = open("README.md", "r")
feature_update = str(file.read()).split("# FEATURE LIST")[0]
feature_update += f"# FEATURE LIST\n\n{table}"
file = open("README.md", "w")
file.write(feature_update.replace("+", "-"))
file.close()
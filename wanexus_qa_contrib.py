import pandas as pd

def replace_chars(input_string):
    # Replace "[" , "]" , and "," with "|"
    modified_string = (
        input_string
        .replace("[", "|")
        .replace("]", "|").replace(",", "|")
        .replace("'", " ")
        .replace(">", "]")
        .replace("<", "["))
    return modified_string

def main():
    df = pd.read_csv('document/feature.csv')

    table = ""
    table = f"\n{replace_chars(str(list(df.head())))}\n| ------- |  ------ | --------- |"
    for i in range(len(df)):
        stat = list(df.iloc[i])
        stat[0] = stat[0].title()
        if stat[1].lower() == "active":
            stat[1] = "!<Active>(https://img.shields.io/badge/Active-brightgreen)"
        elif stat[1].lower() == "error":
            stat[1] = "!<Inactive>(https://img.shields.io/badge/Inactive-red)"
        elif stat[1].lower() == "active-slow":
            stat[1] = "!<Active Slow>(https://img.shields.io/badge/Active%20Slow-blue)"
        elif stat[1].lower() == "wip":
            stat[1] = "!<In Progress>(https://img.shields.io/badge/In%20Progress-yellow)"
        else:
            stat[1] = "!<Inactive>(https://img.shields.io/badge/Will%20Be%20Check-gray)"
        table += f"\n{replace_chars(str(stat))}"
        

    file = open("README.md", "r")
    feature_update = str(file.read()).split("# FEATURE LIST")[0]
    feature_update += f"# FEATURE LIST\n\n{table}"
    file = open("README.md", "w")
    file.write(feature_update.replace("+", "-"))
    file.close()


if __name__ == "__main__":
    main()
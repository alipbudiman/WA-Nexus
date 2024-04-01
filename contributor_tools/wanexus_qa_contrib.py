import os
import time
import pandas as pd
import webbrowser

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

    check_diffrent = open("README.md", "r")

    table = ""
    table = f"\n{replace_chars(str(list(df.head())))}\n| ------- |  ------ | --------- |"
    for i in range(len(df)):
        stat = list(df.iloc[i])
        stat[0] = stat[0].title()
        """
        active: feature active
        active-slow: feature active but slow process
        active-some: some feature active, some not
        error: feature inactive
        wip: feature under maintenance
        """
        if stat[1].lower() == "active":
            stat[1] = "!<Active>(https://img.shields.io/badge/Active-brightgreen)"
        elif stat[1].lower() == "error":
            stat[1] = "!<Inactive>(https://img.shields.io/badge/Inactive-red)"
        elif stat[1].lower() == "active-slow":
            stat[1] = "!<Active Slow>(https://img.shields.io/badge/Active%20Slow-blue)"
        elif stat[1].lower() == "wip":
            stat[1] = "!<In Progress>(https://img.shields.io/badge/In%20Progress-yellow)"
        elif stat[1].lower() == "active-some":
            stat[1] = "!<In Progress>(https://img.shields.io/badge/Active%20Some-green)"
        elif stat[1].lower() == "soon":
            stat[1] = "!<In Progress>(https://img.shields.io/badge/Coming%20Soon-orange)"
        else:
            stat[1] = "!<Will be check>(https://img.shields.io/badge/Will%20Be%20Check-gray)"
        table += f"\n{replace_chars(str(stat))}"
        

    file = open("README.md", "r")
    feature_update = str(file.read()).split("\n# FEATURE LIST")[0]
    feature_update += f"\n# FEATURE LIST\n\n{table}"
    file = open("README.md", "w")
    file.write(feature_update)
    file.close()


    df = pd.read_csv('document/update.csv')
    table = ""
    table = f"\n{replace_chars(str(list(df.head())))}\n| ------- |  ------ |"
    for i in range(len(df)):
        stat = list(df.iloc[i])
        stat[0] = stat[0].title()
        """
        planning: the feature only planning
        ongoing: the feature in progress (code/build)
        wba: the feature alredy done, will be test
        done-test: feature alredy tested and will added
        added: feature alredy added to bot but not publish now
        """
        if stat[1].lower() == "planning":
            stat[1] = "!<planning>(https://img.shields.io/badge/Planning-red)"
        elif stat[1].lower() == "ongoing":
            stat[1] = "!<ongoing>(https://img.shields.io/badge/Ongoing-yellow)"
        elif stat[1].lower() == "wba":
            stat[1] = "!<Will be added>(https://img.shields.io/badge/Will%20Be%20Added-blue)"
        elif stat[1].lower() == "done-test":
            stat[1] = "!<Done test>(https://img.shields.io/badge/Done%20Test-green)"
        elif stat[1].lower() == "added":
            stat[1] = "!<Added>(https://img.shields.io/badge/Added-brightgreen)"
        else:
            stat[1] = "!<Unknow>(https://img.shields.io/badge/Unknow-gray)"
        table += f"\n{replace_chars(str(stat))}"

    file = open("README.md", "r")
    feature_update = str(file.read()).split("\n# FEATURE WILL BE ADDED (UPDATE)")[0]
    feature_update += f"\n# FEATURE WILL BE ADDED (UPDATE)\n\n{table}"
    file = open("README.md", "w")
    file.write(feature_update)
    file.close()

    commit_message = input("Enter Commit Message: ")
    if commit_message == "":commit_message = "NA"
    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")
    
    webbrowser.open("https://github.com/alipbudiman/WA-Nexus")
        

if __name__ == "__main__":
    main()
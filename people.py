import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ruleset(dataset):
    for i in range(n):
        if(dataset.iloc[i]["age"]>=0 and dataset.iloc[i]["age"]<150):
            if(dataset.iloc[i]["age"]<18 and dataset.iloc[i]["agegroup"]=="child"):
                dataset.at[i,"follow_ruleset"] = True
            elif(dataset.iloc[i]["age"]>=18 and dataset.iloc[i]["age"]<65 and dataset.iloc[i]["agegroup"]=="adult"):
                dataset.at[i,"follow_ruleset"] = True
            elif(dataset.iloc[i]["age"]>=65 and dataset.iloc[i]["agegroup"]=="elderly"):
                dataset.at[i,"follow_ruleset"] = True
            else :
                dataset.at[i,"follow_ruleset"] = False
        else :
            dataset.at[i,"follow_ruleset"] = False
        if(dataset.iloc[i]["age"]>dataset.iloc[i]["yearsmarried"] and dataset.at[i,"follow_ruleset"]):
            dataset.at[i,"follow_ruleset"] = True
        else :
            dataset.at[i,"follow_ruleset"] = False
        if((dataset.iloc[i]["status"] in ['married','single','widowed']) and dataset.at[i,"follow_ruleset"]):
            dataset.at[i,"follow_ruleset"] = True
        else :
            dataset.at[i,"follow_ruleset"] = False
    return

dataset = pd.read_csv("people.csv")

dataset["follow_ruleset"] = ""

n = len(dataset)

ruleset(dataset)

print(dataset)

agg = dataset.pivot_table(index=['follow_ruleset'], aggfunc='size')

print("\n\nTotal number of data :",n)
print("\nRuleset followed by :",agg[0])
print("Ruleset NOT followed by :",agg[1])

# plt.bar(n, agg, align='center', alpha=0.5)
# plt.ylabel('Followed by')
# plt.title('Ruleset Follow')

# plt.show()
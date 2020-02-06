import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ruleset(dataset):
    for i in range(n):
        if(dataset.iloc[i]["age"]>=0 and dataset.iloc[i]["age"]<150):
            dataset.at[i,"rule1"] = True
        else :
            dataset.at[i,"rule1"] = False
        if(dataset.iloc[i]["age"]>dataset.iloc[i]["yearsmarried"]):
            dataset.at[i,"rule2"] = True
        else :
            dataset.at[i,"rule2"] = False
        if((dataset.iloc[i]["status"] in ['married','single','widowed'])):
            dataset.at[i,"rule3"] = True
        else :
            dataset.at[i,"rule3"] = False
        if(dataset.iloc[i]["age"]<18 and dataset.iloc[i]["agegroup"]=="child"):
            dataset.at[i,"rule4"] = True
        elif(dataset.iloc[i]["age"]>=18 and dataset.iloc[i]["age"]<65 and dataset.iloc[i]["agegroup"]=="adult"):
            dataset.at[i,"rule4"] = True
        elif(dataset.iloc[i]["age"]>=65 and dataset.iloc[i]["agegroup"]=="elderly"):
            dataset.at[i,"rule4"] = True
        else :
            dataset.at[i,"rule4"] = False
    return

dataset = pd.read_csv("people.csv")

dataset["rule1"] = ""
dataset["rule2"] = ""
dataset["rule3"] = ""
dataset["rule4"] = ""

n = len(dataset)

ruleset(dataset)

print(dataset)

r1 = dataset["rule1"].value_counts()
r2 = dataset["rule2"].value_counts()
r3 = dataset["rule3"].value_counts()
r4 = dataset["rule4"].value_counts()

b_r = (dataset["rule1"] & dataset["rule2"] & dataset["rule3"] & dataset["rule4"]).value_counts()


labels = ['R1', 'R2', 'R3', 'R4', 'R1-R4']
X = [r1[1],r2[1],r3[1],r4[1],b_r[1]]
Y = [n-r1[1],n-r2[1],n-r3[1],n-r4[1],n-b_r[1]]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, X, width, label='Follow Rules')
rects2 = ax.bar(x + width/2, Y, width, label='Don\'t Follow Rules')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

ax.set_ylabel('Observations')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

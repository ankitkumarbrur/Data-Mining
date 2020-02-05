
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

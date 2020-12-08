import pandas as pd
import os
from scipy import stats
import numpy as np
# import matplotlib.pyplot as plt

# directory=os.getcwd()
# os.chdir(str(directory))

def degree(a):
    if a < 0.05:
        if a <0.01:
            if a < 0.001:
                b = 'p < 0.001' 
            else:
                b = 'p < 0.01'
        else:
            b='p < 0.05'
    else:
        if a==1:
            b = 'p = 1'
        else:
            b='p > 0.05'
    return b

def c():
    path = os.getcwd()
    list_sqlite_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".xlsx")]
    return list_sqlite_files

def student(rvs1, rvs2):
    statistic, p_value = stats.ttest_ind(rvs1, rvs2, equal_var = False)
    one = round(statistic, 4)
    two = round(p_value, 4)
    return degree(two)

def uitni(rvs1, rvs2):
    statistic, p_value = stats.mannwhitneyu(rvs1, rvs2, use_continuity=True, alternative=None)
    one = round(statistic, 4)
    two = round(p_value, 4)
    return degree(two)

def ks(rvs1):
    """Разобраться с этой функцией"""
    statistic, p_value = stats.kstest(rvs1, 'norm', mode='asymp')
    one = round(statistic, 4)
    two = round(p_value, 4)
    return degree(two)

def shapiro(rvs1):
    """Разобраться с этой функцией"""
    statistic, p_value = stats.shapiro(rvs1)
    one = round(statistic, 4)
    two = round(p_value, 4)
    return degree(two)

def adddesc(df):
    describe = df.describe()
    describe.loc["m"] = "0"
    describe.loc["Me"] = "0"
    describe.loc["(Q1:Q3)"] = "0"
    describe.loc["M±m"] = "0"
    describe.loc["% to mean control"] = "0"
    describe.loc["% to Me control"] = "0"
    describe.loc["ks-test"] = "0"
    describe.loc["shapiro"] = "0"
    
    for i in list(df):
        describe.loc["m"] = describe.loc["std"]/(describe.loc["count"]-1)*0.5
        describe.loc["Me"][i] = describe.loc["50%"][i]
        z = str(" (") + str(describe.loc["25%"][i]) + str(":") + str(describe.loc["75%"][i]) + str(")")
        describe.loc["(Q1:Q3)"][i] = z
        x = str(round(describe.loc["mean"][i],2))+"±"+str(round(describe.loc["m"][i],2))
        describe.loc["M±m"][i] = x
        describe.loc["% to mean control"][i] = round((((describe.loc["mean"][i]/describe.loc["mean"]["Контроль"])*100)-100),2)
        describe.loc["% to Me control"][i] = round((((describe.loc["50%"][i]/describe.loc["50%"]["Контроль"])*100)-100),2)
        describe.loc["ks-test"][i] = ks(df[i])
        describe.loc["shapiro"][i] = shapiro(df[i])
        describe.loc["{}-t-test".format(i)] = "0"
        for u in list(df):
            describe.loc["{}-t-test".format(i)][u] = "0"
            describe.loc["{}-t-test".format(i)][u] = student(df[i],df[u])
        describe.loc["{}-u-test".format(i)] = "0"
        for z in list(df):
            describe.loc["{}-u-test".format(i)][z] = "0"
            describe.loc["{}-u-test".format(i)][z] = uitni(df[i],df[z])


    return describe

def statstud(df):
    describe = df.describe()
    for i in list(df):
        describe.loc["{}-t-test".format(i)] = "0"
        for u in list(df):
            describe.loc["{}-t-test".format(i)][u] = "0"
            describe.loc["{}-t-test".format(i)][u] = student(df[i],df[u]) 
    return describe

def statsks(df):
    describe = df.describe()
    for i in list(df):
        describe.loc["{}-ks-test".format(i)] = "0"
        for u in list(df):
            describe.loc["{}-ks-test".format(i)][u] = "0"
            describe.loc["{}-ks-test".format(i)][u] = ks(df[u])
    return describe



def create_describe(excel):
    two_up =  os.path.abspath(os.path.join(__file__ ,"../.."))
    writer = pd.ExcelWriter(two_up+'/assets/Describe.xlsx')
    html_list = {}
    xl = pd.ExcelFile(excel)
    lst = xl.sheet_names
    for u in lst:
        df = pd.read_excel(excel, sheet_name=u, index_col=0)
        describ = adddesc(df)
        html_list["Describe-{}".format(u)] = describ.to_html()
        describ.to_excel(writer, sheet_name='Describe_{}'.format(u))
    writer.save()
    return html_list
   
    
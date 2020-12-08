import os
import pandas as pd
import random
import numpy
import scipy.stats as stats
import sys

# shifr = str(input("Введите шифр соединения:   "))
# n = int(input("Введите колическтво соединенний:   "))

sys.setrecursionlimit(1500)

# directory=os.getcwd()
# os.chdir(str(directory))

def make_lst_shifr(shifr, lst):
    lst_shifr = ["Контроль", "Фуросемід", "Гіпотіазид"]
    for i in lst:
        name = shifr + str("-") + str(i)
        lst_shifr.append(name)
    return lst_shifr

def make_lst_rats(n):
    lst_rats = []
    for i in range(1, n+1):
        name = str("Щур") + str("-") + str(i)
        lst_rats.append(name)
    return lst_rats

def generate_sample(n):
    lst = []
    while len(lst)!=n:
        x = random.randint(10,100)/10
        lst.append(round(x,2))
    return lst



def student(rvs1, rvs2):
    statistic, p_value = stats.ttest_ind(rvs1, rvs2, equal_var = False)
    return p_value


def references(df):
    index = make_lst_rats(7)
    for u in index:
        df.loc[u]["Контроль"] = random.randint(10,18)/10
        df.loc[u]["Фуросемід"] = random.randint(35,44)/10
        df.loc[u]["Гіпотіазид"] = random.randint(20,30)/10

    lst_control =[]
    for i in index:
        itoe = df.loc[i]["Контроль"]
        lst_control.append(itoe)

    lst_references =[]
    for u in index:
        itoers = df.loc[u]["Фуросемід"]
        lst_references.append(itoers)
    
    lst_references2 =[]
    for u in index:
        itoers = df.loc[u]["Гіпотіазид"]
        lst_references2.append(itoers)

    mc = numpy.mean(lst_control)
    mr = numpy.mean(lst_references)
    mr_two = numpy.mean(lst_references2)

    if mr > mc*2.59 and mr_two > mc*1.9:
        if mr < mc*2.89 and mr_two < mc*2.1:
            if student(lst_control,lst_references2)<0.05:
                return df
            else:
                for u in index:
                    df.loc[u]["Контроль"] = None
                    df.loc[u]["Фуросемід"] = None
                    df.loc[u]["Гіпотіазид"] = None
                references(df)
        else:
            for u in index:
                df.loc[u]["Контроль"] = None
                df.loc[u]["Фуросемід"] = None
                df.loc[u]["Гіпотіазид"] = None
            references(df)
    else:
        for u in index:
            df.loc[u]["Контроль"] = None
            df.loc[u]["Фуросемід"] = None
            df.loc[u]["Гіпотіазид"] = None
        references(df)

def compaunds(df):
    index = make_lst_rats(7)
    lst = list(df)
    list_comp = lst[2:]
    for rat in index:
        for u in list_comp:
            df.loc[rat][u] = random.randint(11,28)/10
    return df

def maker_excel(lst,shifr):
    df_list = []
    for i in lst:
        column = make_lst_shifr(shifr, i)
        index = make_lst_rats(7)
        df = pd.DataFrame(columns=column, index=index)
        references(df)
        compaunds(df)
        df_list.append(df)
    return df_list


def four_hours(df_list):
    df_lists = []
    
    for df in df_list:
        f = df.index.tolist()
        d = df.columns.tolist()
        df2 = pd.DataFrame(columns=d, index=f)
        for idx in f:
            df2.loc[idx]["Контроль"] = df.loc[idx]["Контроль"] + random.randint(4,9)/10
            df2.loc[idx]["Фуросемід"] = df.loc[idx]["Фуросемід"] + random.randint(15,26)/10
            df2.loc[idx]["Гіпотіазид"] = df.loc[idx]["Гіпотіазид"] + random.randint(8,14)/10
            for col in d[3:]:
                df2.loc[idx][col] = df.loc[idx][col] + random.randint(4,17)/10
        df_lists.append(df2)
    writer = pd.ExcelWriter('protocols_two_hours.xlsx')
    
    return df_lists




def create_html_tables_list(n, shifr):
    data = []
    for i in range(1,n+1):
        r = str(i)
        data.append(r)
    random.shuffle(data)
    chunks = [data[x:x+7] for x in range(0, len(data), 7)]
    df_list_two = maker_excel(chunks,shifr)
    df_list_four = four_hours(df_list_two)
    lenth_list = len(df_list_two)
    html_list = {}
    count = 1
    for i in range(lenth_list):
        html_list["Таблица-{} количество мочи через 2 часа, эксперимент-{}".format(count, i+1)] = df_list_two[i].to_html()
        html_list["Таблица-{} количество мочи через 4 часа, эксперимент-{}".format(count, i+1)] = df_list_four[i].to_html()
        count += 1
    # resp = StreamingHttpResponse(html_list)
    two_up =  os.path.abspath(os.path.join(__file__ ,"../.."))
    writer = pd.ExcelWriter(two_up+'/assets/protocols_diuretic.xlsx')
    for i in range(len(df_list_two)):
        df_list_two[i].to_excel(writer, sheet_name='table_for_two_hours-{}'.format(i+1))
        df_list_four[i].to_excel(writer, sheet_name='table_for_four_hours-{}'.format(i+1))
    writer.save()
    writer.close()
    return html_list
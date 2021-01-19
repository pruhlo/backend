import os
import pandas as pd
import random
import numpy
import scipy.stats as stats
import sys
from .configuration import *
import ast
# from configuration import *

class CreateSamples:
    def __init__(self, kwargs):
        self.efficiency = kwargs['efficiency']
        self.animal = kwargs['animal']
        self.count_animals = kwargs['count_animals']
        self.decimal_point = kwargs['decimal_point']
        self.type = kwargs['type']
        self.control = kwargs['control']
        self.references = kwargs['references']
        self.specimens = kwargs['specimens']
        # self.timeline = kwargs['timeline']

    def generate_samples(self, mini, maxi):
        """Create (generate) samples list specify the length (count animals)
        with decimal of point for each element"""
        sample = []
        counter = self.count_animals
        while counter>0:
            element_samples = random.randint(mini*(10**self.decimal_point), maxi*(10**self.decimal_point))/(10**self.decimal_point)
            sample.append(element_samples)
            counter -= 1
        return sample

    def student(self, sample1, sample2):
        """Calculates the statistical significance of the difference between two samples (t-Students)"""
        p_value = stats.ttest_ind(sample1, sample2, equal_var = False)[1]
        return p_value

    def checking_sample(self, sample_control, mini, maxi, min_per, max_per, statistic=True):
        """checking sample against specification (min&max_percentage_efficiency)"""
        mean_control = numpy.mean(sample_control)
        while  True:
            sample = self.generate_samples(mini,maxi)
            mean_sample = numpy.mean(sample)
            if mean_sample > mean_control*min_per/100:
                if mean_sample < mean_control*max_per/100:
                    if statistic==True:
                        if self.student(sample_control, sample)<0.05:
                            return sample
                    else:
                        return sample

    def create_samples(self, samples, curves, statistic=True):
        """CREATE DICTIONARY with SAMPLES depending on curves from specification"""
        for curve in curves:
            ref_name = curves[curve]['name']
            ref_min = curves[curve]['minimum']
            ref_max = curves[curve]['maximum']
            ref_min_per = curves[curve]['min_percentage_efficiency']
            ref_max_per = curves[curve]['max_percentage_efficiency']
            if ref_min_per==None and ref_max_per==None:
                samples[ref_name] = self.generate_samples(ref_min, ref_max)
            else:
                samples[ref_name] = self.checking_sample(samples[self.control['name']], ref_min, ref_max, ref_min_per, ref_max_per, statistic)

        return samples

    def naming_creating_elements(self, samples, count, name):
        list_name_specimens =[]
        for specimen in self.specimens:
            list_name_specimens.append(self.specimens[specimen]['name'])
        for element in range(1,count+1):
            new_samples = self.create_samples(samples, self.specimens)
            samples[f'{name}-{element}'] = new_samples[random.choice(list_name_specimens)]
        for key in list_name_specimens:
            del samples[key]
        return samples
    
    def create_data_samples(self, name=None, count=None, flag=None):
        if flag is None:
            stat=True
        else:
            stat=False
        """One Main function for creating samples"""
        samples = {}
        samples[self.control['name']] = self.generate_samples(self.control['minimum'], self.control['maximum'])
        self.create_samples(samples, self.references, statistic=stat)
        self.create_samples(samples, self.specimens, statistic=False)
        if name==None and count==None:
            return samples
        else:
            if count is None:
                count=4
                self.naming_creating_elements(samples, count, name)
            if type(count) != int or count<=0:
                print(f'count must be int, not {type(count)}')
                count=4
                self.naming_creating_elements(samples, count, name)
                return samples
            else:
                self.naming_creating_elements(samples, count, name)
            return samples
    
    def sum_dicts(self, dict1, dict2):
        keys=set(list(dict1.keys())+list(dict2.keys()))
        data={}
        for key in keys:
            value1 = dict1.get(key)
            value2 = dict2.get(key)
            if value1 == None:
                value = value2
            elif value2 == None:
                value = value1
            else:
                value = [round((x+y), self.decimal_point) for x, y in zip(value1, value2)]
            data[key]=value
        return data

    def get_index_list(self):
        index_list = []
        for i in range(1, self.count_animals+1):
            index_list.append(self.animal+str(i))
        return index_list


# sys.setrecursionlimit(1500)  




def get_diuretic_data(name=None, count=None):
    diuretics = {}
    two_hour = CreateSamples(diuretic)
    next_two_hour =CreateSamples(diuretic_four)
    data_two_hours = two_hour.create_data_samples(name, count)
    diuretics[0] = data_two_hours
    data_next_two_hours = next_two_hour.create_data_samples(name, count, flag='without_stats') # flag задает поиск статистически значимых отличий если None
    four_hour = two_hour.sum_dicts(data_two_hours, data_next_two_hours)
    diuretics[1] = four_hour
    return diuretics


def get_diuretic_html_data(name=None, count=None):
    data = get_diuretic_data(name, count)
    list_keys = data.keys()
    l = list(data[0].keys())
    index_list = CreateSamples(diuretic).get_index_list()
    # s = pd.Series(index_list)
    
    list_table = ['Таблица количество мочи через 2 часа', 'Таблица количество мочи через 4 часа']
    html_list = {}
    df_list = {}
    for key in range(len(list_keys)):
        df = pd.DataFrame.from_dict(data[key])
        df = df[l]
        df['Тварина'] = index_list
        df.set_index('Тварина', inplace=True, drop=True)
        html_list[list_table[key]] = df.to_html()
        df_list[list_table[key]] = df
    return html_list, df_list

class CreateDescribe():

    def __init__(self, df):
        self.df = df

    def degree(self, a):
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

    def student(self, rvs1, rvs2):
        statistic, p_value = stats.ttest_ind(rvs1, rvs2, equal_var = False)
        one = round(statistic, 4)
        two = round(p_value, 4)
        return self.degree(p_value)

    def uitni(self, rvs1, rvs2):
        statistic, p_value = stats.mannwhitneyu(rvs1, rvs2, use_continuity=True, alternative=None)
        one = round(statistic, 4)
        two = round(p_value, 4)
        return self.degree(p_value)

    def ks(self, rvs1):
        """Разобраться с этой функцией"""
        statistic, p_value = stats.kstest(rvs1, 'norm', mode='asymp')
        one = round(statistic, 4)
        two = round(p_value, 4)
        return self.degree(p_value)

    def shapiro(self, rvs1):
        """Разобраться с этой функцией"""
        statistic, p_value = stats.shapiro(rvs1)
        one = round(statistic, 4)
        two = round(p_value, 4)
        return self.degree(p_value)

    def describe_extend(self):
        describe = self.describe(self.df)
        describe.loc["Me"] = None
        describe.loc["(Q1:Q3)"] = 0
        describe.loc["M±m"] = 0
        describe.loc["% to mean control"] = 0
        describe.loc["% to Me control"] = 0
        describe.loc["ks-test"] = 0
        describe.loc["shapiro"] = 0
        for i in list(self.df):
            describe.loc["Me"][i] = describe.loc["50%"][i]
            z = str(" (") + str(describe.loc["25%"][i]) + str(":") + str(describe.loc["75%"][i]) + str(")")
            describe.loc["(Q1:Q3)"][i] = z
            x = str(round(describe.loc["mean"][i],2))+"±"+str(round(describe.loc["sem"][i],2))
            describe.loc["M±m"][i] = x
            describe.loc["% to mean control"][i] = round((((describe.loc["mean"][i]/describe.loc["mean"]["Контроль"])*100)-100),2)
            describe.loc["% to Me control"][i] = round((((describe.loc["50%"][i]/describe.loc["50%"]["Контроль"])*100)-100),2)
            describe.loc["ks-test"][i] = self.ks(self.df[i])
            describe.loc["shapiro"][i] = self.shapiro(self.df[i])
            describe.loc["{}-t-test".format(i)] = "0"
            for u in list(self.df):
                describe.loc["{}-t-test".format(i)][u] = "0"
                describe.loc["{}-t-test".format(i)][u] = self.student(self.df[i],self.df[u])
            describe.loc["{}-u-test".format(i)] = "0"
            for z in list(self.df):
                describe.loc["{}-u-test".format(i)][z] = "0"
                describe.loc["{}-u-test".format(i)][z] = self.uitni(self.df[i],self.df[z])
        return describe

    def describe(self, df):
        """https://stackoverflow.com/questions/38545828/pandas-describe-by-additional-parameters"""
        return pd.concat([df.describe().T,
                        df.mad().rename('mad'),
                        df.skew().rename('skew'),
                        df.kurt().rename('kurt'),
                        df.sem().rename('sem')
                        ], axis=1).T



def create_describe_list(df_list):
    describe_df_list = {}
    html_list = {}
    for key in df_list:
        df = df_list[key]
        # print(df)
        obj = CreateDescribe(df)
        data = obj.describe_extend()
        describe_df_list[key] = data
        html_list[key] = data.to_html()
    return html_list, describe_df_list

def string_df_to_dict(string):
    dictionary = ast.literal_eval(string) # ckj
    df_list = {} #
    for key in dictionary:
        df_list[key] = pd.DataFrame.from_dict(dictionary[key])
    return df_list

def write_excel(df_list, name_file):
    path_two_up =  os.path.abspath(os.path.join(__file__ ,"../.."))
    writer = pd.ExcelWriter(path_two_up+'/assets/{}.xlsx'.format(name_file))
    for key in list(df_list):
        df_list[key].to_excel(writer, sheet_name='{}'.format(key))
    writer.save()
    writer.close()

def string_protocols_df_to_excel(string):
    df_list = string_df_to_dict(string)
    write_excel(df_list, 'protocols')
    describe_df_list = create_describe_list(df_list)[1]
    write_excel(df_list, 'describe')

# html_list, df_list = get_diuretic_html_data('dfgfd', 4)
# e = create_describe_list(df_list)
# for df in e:
#     print(e[df])


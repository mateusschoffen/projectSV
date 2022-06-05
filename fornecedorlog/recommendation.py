import pandas as pd
import numpy as np
from pkg_resources import get_provider

#Creating the dictionary

table = {
    'Cost': [12000, 6000, 18000, 12000],
    'Cost_transp':[400, 600, 200, 800],
    'Time':[15, 10, 20, 5],
    'Income':[2, 1.5, 3, 1]
    }        
#converting to Dataframe with pandas:::
table_df = pd.DataFrame(data=table,
index=['Provider_A', 'Provider_B', 'Provider_C', 'Provider_D']
)

#creating the crit_array
crit_array = [
[1, 7, 5, 1 /3],
[1/7, 1, 1/3, 1/9],
[1/5, 3, 1, 1/7],
[3, 9, 7, 1]
]
#converting to Dataframe with Pandas
crit_df = pd.DataFrame(data=crit_array,
index= ['cost_feedsto', 'cost_transp', 'approximate_time', 'income'],
columns= ['cost_feedsto', 'cost_transp', 'approximate_time', 'income'],
).round(2)
#Creating the ponderation vector
vet=(
    crit_df['cost_feedsto'] / sum (crit_df['cost_feedsto']) +
    crit_df['cost_transp'] / sum (crit_df['cost_transp'])+
    crit_df['approximate_time'] / sum (crit_df['approximate_time'])+
    crit_df['income'] / sum (crit_df['income'])
)

#adding the ponderatio vector to the dataframe 
vet_pon = (vet / len(table)).round(2)
crit_df['Vect'] = vet_pon

def parity_array_change(criterion: str, dataframe: pd.DataFrame = table_df, debug : bool = False):
    new_df = dataframe.drop(table_df.columns, axis=1)
    for provider in new_df.index:
        new_df.insert(len(new_df.columns), provider, (((dataframe[criterion][0:]-dataframe[criterion][provider])/dataframe[criterion][provider])*100).round(2), False)
    
    if debug: print(new_df) 
    return new_df

def Optimizing_Crit(arr: pd.array, descending : bool = False, debug : bool = False):
    num_providers = len(table_df.columns) #Get num of collumns to define last element to set up
    
    arr = arr.to_numpy().ravel()   #Convert dataframe to a single numpy array
    arr = np.sort(arr)[::-1] if descending else np.sort(arr) #Sort array depending on which case
    arr = arr[0: int((num_providers**2-num_providers)/2)] #Set up N required elements
    
    if debug: print(arr)
    return arr

def scale_Saaty_values(dataframe : pd.DataFrame, case_type : str = 'min', debug : bool = False):
    matrix = dataframe.to_numpy()   #Convert dataframe to matrix
    if case_type == 'max':
        for i, line in enumerate(matrix):
            for j, value in enumerate(line):
                var = value
                intervals = [   
                    (var >= 85), 
                    (85 > var >= 80), 
                    (80 > var >= 65), 
                    (65 > var >= 60), 
                    (60 > var >= 45), 
                    (45 > var >= 40), 
                    (40 > var >= 11), 
                    (11 > var > 0), 
                    (var == 0)
                ]
                if True not in intervals:
                    matrix[i][j] = np.nan
                    continue
                SAATY = len(intervals)-intervals.index(True)
                matrix[i][j] = SAATY

    elif case_type == 'min':
        for i, line in enumerate(matrix):
            for j, value in enumerate(line):
                var = value
                intervals = [   (var <= -85), 
                                (-85 < var <= -80), 
                                (-80 < var <= -65), 
                                (-65 < var <= -60), 
                                (-60 < var <= -45), 
                                (-45 < var <= -40), 
                                (-40 < var <= -11), 
                                (-11 < var < 0), 
                                (var == 0)
                            ]
                if True not in intervals:
                    matrix[i][j] = np.nan
                    continue
                SAATY = len(intervals)-intervals.index(True)
                matrix[i][j] =  SAATY
    df = pd.DataFrame(matrix, index = dataframe.index, columns = dataframe.columns)
    if debug: print(df)
    return df

def dataframe_transpose(dataframe : pd.DataFrame, debug : bool = False):
    array = dataframe.to_numpy()
    array = array.transpose()
    array = (1/array).round(2)
    new_df = pd.DataFrame(array, index = dataframe.index, columns = dataframe.columns)
    if debug: print(new_df)
    return new_df

def merged_dataframes(dataframe : pd.DataFrame, transp : pd.DataFrame, debug : bool = False):
    dataframe.columns = transp.columns
    dataframe.update(transp)
    if debug: print(dataframe)
    return dataframe

def vector_medium(crit_list : pd.DataFrame = [], debug : bool = False):
    aux_array = []
    for criteria in crit_list:
        var = 0
        for provider in criteria:
            var += criteria[provider]/sum(criteria[provider])
        aux_array.append((var/len(criteria)).round(2))
    
    if debug: print(aux_array)
    return aux_array

def main_dataframe_criteries(dataframe: pd.DataFrame = table_df, criteria_array = [], debug : bool = False):
    for index, criterion in enumerate(criteria_array):
        dataframe.insert(len(dataframe.columns), 'c'+str(index+1), criterion)
    
    if debug: print(dataframe) 
    return dataframe

def define_provider(dataframe: pd.DataFrame, criteria: pd.DataFrame, debug : bool = False):
    only_criteria_from_df = dataframe.loc[:, dataframe.columns.str.startswith('c')] #Select criteria columns from dataframe started with c
    matrix_criteria = only_criteria_from_df.to_numpy() #Turn all columns about criteria data to array
    crit_weight = criteria['Vect'].to_numpy() #Turn weights determined by user to array
    dataframe = dataframe.drop(only_criteria_from_df, axis=1) #Drop criteria columns from main dataframe
    result = matrix_criteria.dot(crit_weight).round(2) #Multiply criteria for weights determined by user
    dataframe['Selection'] = result #Add a new column to main dataframe showing all cases
    dataframe = dataframe.sort_values('Selection', ascending=False)
    
    if debug: print(dataframe) 
    return dataframe


#==============================================================================#
######################### Automatization to set up provider C1
#==============================================================================#
c1 = parity_array_change('Cost')
c1_min = Optimizing_Crit(c1)
c1 = scale_Saaty_values(c1, 'min')
tc1 = dataframe_transpose(c1)
c1 = merged_dataframes(c1, tc1)

#==============================================================================#
######################### Automatization to set up provider C2
#==============================================================================#
c2 = parity_array_change('Cost_transp')
c2_min = Optimizing_Crit(c2)
c2 = scale_Saaty_values(c2, 'min')
tc2 = dataframe_transpose(c2)
c2 = merged_dataframes(c2, tc2)

#==============================================================================#
######################### Automatization to set up provider C3

c3 = parity_array_change('Time')
c3_min = Optimizing_Crit(c3)
c3 = scale_Saaty_values(c3, 'min')
tc3 = dataframe_transpose(c3)
c3 = merged_dataframes(c3, tc3)

#==============================================================================#
######################### Automatization to set up provider C4
#==============================================================================#
c4 = parity_array_change('Income')
c4_max = Optimizing_Crit(c4, True)
c4 = scale_Saaty_values(c4, 'max')
tc4 = dataframe_transpose(c4)
c4 = merged_dataframes(c4, tc4)

#==============================================================================#
######################### Selecting Priority Provider
#==============================================================================#
crit = [c1,c2,c3,c4]
medium_vector = vector_medium(crit)
main_dataframe_criteries(table_df, medium_vector)
define_provider(table_df, crit_df, True)

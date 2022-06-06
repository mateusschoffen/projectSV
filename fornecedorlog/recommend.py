#from turtle import distance
from pandas import DataFrame
import numpy as np

#from fornecedorlog.core import get_providersall

class Recomendation(object):

    def __init__(self, providers):
        
        pay = []
        distance = []
        webstore = []
        p_credit = []
        name_df = []
        for item in providers:
            pay.append(item.pay)
            distance.append(item.distance)
            webstore.append(item.webstore)
            p_credit.append(item.credit)
            name_df.append(item.name)

        #Creating the dictionary
        table =  {
            'pay': pay,
            'distance': distance,
            'webstore': webstore,
            'p_credit': p_credit
        }

        #converting to Dataframe with pandas:::
        self.table_df = DataFrame(
            data=table,
            index=name_df
        )

        #creating the crit_array
        crit_array = [
            [1, 7, 5, 1 /3],
            [1/7, 1, 1/3, 1/9],
            [1/5, 3, 1, 1/7],
            [3, 9, 7, 1]
        ]

        #converting to Dataframe with Pandas
        self.crit_df = DataFrame(
            data=crit_array,
            index= ['pay', 'distance', 'webstore', 'p_credit'],
            columns= ['pay', 'distance', 'webstore', 'p_credit'],
        ).round(2)

        #Creating the ponderation vector
        vet=(
            self.crit_df['pay'] / sum (self.crit_df['pay']) +
            self.crit_df['distance'] / sum (self.crit_df['distance'])+
            self.crit_df['webstore'] / sum (self.crit_df['webstore'])+
            self.crit_df['p_credit'] / sum (self.crit_df['p_credit'])
        )

        #adding the ponderatio vector to the dataframe 
        vet_pon = (vet / len(table)).round(2)
        self.crit_df['Vect'] = vet_pon

    #Calc All Automatization to set up
    def calc_all(self):

        c1 = self.calc_criter(parity='pay', value='min')
        c2 = self.calc_criter(parity='distance', value='min')
        c3 = self.calc_criter(parity='webstore', value='min')
        c4 = self.calc_criter(parity='p_credit', value='max', opt=True)

        return [c1,c2,c3,c4]

    def calc_criter(self, parity, value, opt=False):

        c1 = self.parity_array_change(parity, self.table_df)
        c1_min = self.optimizing_crit(c1, opt)
        c1 = self.scale_Saaty_values(c1,value)
        tc1 = self.dataframe_transpose(c1)
        c1 = self.merged_dataframes(c1, tc1)
        return c1

    def parity_array_change(self, criterion: str, dataframe, debug : bool = False):
        new_df = dataframe.drop(self.table_df.columns, axis=1)
        for provider in new_df.index:
            new_df.insert(len(new_df.columns), provider, (((dataframe[criterion][0:]-dataframe[criterion][provider])/dataframe[criterion][provider])*100).round(2), False)
        
        if debug: print(new_df) 
        return new_df

    def optimizing_crit(self, arr, descending : bool = False, debug : bool = False):
        num_providers = len(self.table_df.columns) #Get num of collumns to define last element to set up
        
        arr = arr.to_numpy().ravel()   #Convert dataframe to a single numpy array
        arr = np.sort(arr)[::-1] if descending else np.sort(arr) #Sort array depending on which case
        arr = arr[0: int((num_providers**2-num_providers)/2)] #Set up N required elements
        
        if debug: print(arr)
        return arr

    def scale_Saaty_values(self,dataframe, case_type : str = 'min', debug : bool = False):

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
        df = DataFrame(matrix, index = dataframe.index, columns = dataframe.columns)
        if debug: print(df)
        return df

    def dataframe_transpose(self,dataframe, debug : bool = False):
        array = dataframe.to_numpy()
        array = array.transpose()
        array = (1/array).round(2)
        new_df = DataFrame(array, index = dataframe.index, columns = dataframe.columns)
        if debug: print(new_df)
        return new_df

    def merged_dataframes(self,dataframe, transp, debug : bool = False):
        dataframe.columns = transp.columns
        dataframe.update(transp)
        if debug: print(dataframe)
        return dataframe

    def vector_medium(self,crit_list = [], debug : bool = False):
        aux_array = []
        for criteria in crit_list:
            var = 0
            for provider in criteria:
                var += criteria[provider]/sum(criteria[provider])
            aux_array.append((var/len(criteria)).round(2))
        
        if debug: print(aux_array)
        return aux_array

    def main_dataframe_criteries(self,dataframe, criteria_array = [], debug : bool = False):
        for index, criterion in enumerate(criteria_array):
            dataframe.insert(len(dataframe.columns), 'c'+str(index+1), criterion)
        
        if debug: print(dataframe) 
        return dataframe

    def define_provider(self,dataframe, criteria, debug : bool = False):

        only_criteria_from_df = dataframe.loc[:, dataframe.columns.str.startswith('c')] #Select criteria columns from dataframe started with c
        matrix_criteria = only_criteria_from_df.to_numpy() #Turn all columns about criteria data to array
        crit_weight = criteria['Vect'].to_numpy() #Turn weights determined by user to array
        dataframe = dataframe.drop(only_criteria_from_df, axis=1) #Drop criteria columns from main dataframe
        result = matrix_criteria.dot(crit_weight).round(2) #Multiply criteria for weights determined by user
        dataframe['Selection'] = result #Add a new column to main dataframe showing all cases
        dataframe = dataframe.sort_values('Selection', ascending=False)
        
        if debug: print(dataframe)
        return dataframe.to_dict()

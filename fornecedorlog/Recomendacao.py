import pandas as pd
import numpy as np

#Criando o dicionario:::
tabela = {
    'Custo': [12000, 6000, 18000, 12000],
    'Custo_transporte':[400, 600, 200, 800],
    'Tempo':[15, 10, 20, 5],
    'Rendimento':[2, 1.5, 3, 1]
    }
              
#transformando em Dataframe com pandas:::
tabela_df = pd.DataFrame(data=tabela,
index=['Provedor_A', 'Provedor_B', 'Provedor_C', 'Provedor_D']
)
rows = tabela_df.shape[0] 
cols = tabela_df.shape[1] 
#Mostrando o DF criado:
n = 4
p = 4
crit_array = [
[1, 7, 5, 1 /3],
[1/7, 1, 1/3, 1/9],
[1/5, 3, 1, 1/7],
[3, 9, 7, 1],
]
crit_df = pd.DataFrame(data=crit_array,
index=['custo_MP', 'custo_trans', 'temp_apro', 'rend'],
columns= ['custo_MP', 'custo_trans', 'temp_apro', 'rend'],
).round(2)
rows = crit_df.shape[0] 
cols = crit_df.shape[1] 

vet=(
    crit_df['custo_MP'] / sum (crit_df['custo_MP']) +
    crit_df['custo_trans'] / sum (crit_df['custo_trans'])+
    crit_df['temp_apro'] / sum (crit_df['temp_apro'])+
    crit_df['rend'] / sum (crit_df['rend'])
)

#vetor de ponderação adicionado ao dataframe
vet_pon = (vet / n).round(2)
crit_df ['Vect'] = vet_pon






#transformando o dataframe em um vetor

#print(aux)
def matriz_paridade_variacao_percentual(criterio: str, dataframe: pd.DataFrame = tabela_df, debug : bool = False):
    new_df = dataframe.drop(tabela_df.columns, axis=1)
    for provedor in new_df.index:
        new_df.insert( len(new_df.columns), provedor, (((dataframe[criterio][0:]-dataframe[criterio][provedor])/dataframe[criterio][provedor])*100).round(2), False)
    
    if debug: print(new_df) 
    return new_df

def otimizando_Criterio(arr: pd.array, descending : bool = False, debug : bool = False):
    num_providers = len(tabela_df.columns) #Get num of collumns to define last element to set up
    
    arr = arr.to_numpy().ravel()   #Convert dataframe to a single numpy array
    arr = np.sort(arr)[::-1] if descending else np.sort(arr) #Sort array depending on which case
    arr = arr[0: int((num_providers**2-num_providers)/2)] #Set up N required elements
    
    if debug: print(arr)
    return arr

def valores_escala_saaty(dataframe : pd.DataFrame, case_type : str = 'min', debug : bool = False):
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

def transposta_dataframe(dataframe : pd.DataFrame, debug : bool = False):
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

def vetor_medio(dataframe : pd.DataFrame, debug : bool = False):
    pass

#==============================================================================#
######################### Automatização matriz provedor C1
#==============================================================================#
c1 = matriz_paridade_variacao_percentual('Custo')
c1_min = otimizando_Criterio(c1)
c1 = valores_escala_saaty(c1, 'min')
tc1 = transposta_dataframe(c1)
c1 = merged_dataframes(c1, tc1)

#==============================================================================#
######################### Automatização matriz provedor C2
#==============================================================================#
c2 = matriz_paridade_variacao_percentual('Custo_transporte')
c2_min = otimizando_Criterio(c2)
c2 = valores_escala_saaty(c2, 'min')
tc2 = transposta_dataframe(c2)
c2 = merged_dataframes(c2, tc2)

#==============================================================================#
######################### Automatização matriz provedor C3
#==============================================================================#
c3 = matriz_paridade_variacao_percentual('Tempo')
c3_min = otimizando_Criterio(c3)
c3 = valores_escala_saaty(c3, 'min')
tc3 = transposta_dataframe(c3)
c3 = merged_dataframes(c3, tc3)

#==============================================================================#
######################### Automatização matriz provedor C4
#==============================================================================#
c4 = matriz_paridade_variacao_percentual('Rendimento')
c4_max = otimizando_Criterio(c4, True)
c4 = valores_escala_saaty(c4, 'max')
tc4 = transposta_dataframe(c4)
c4 = merged_dataframes(c4, tc4)

nv1=(
    c1['Provedor_A'] / sum (c1['Provedor_A'])+
    c1['Provedor_B'] / sum (c1['Provedor_B'])+
    c1['Provedor_C'] / sum (c1['Provedor_C'])+
    c1['Provedor_A'] / sum (c1['Provedor_A'])
)

nv2=(
    c2['Provedor_A'] / sum (c2['Provedor_A'])+
    c2['Provedor_B'] / sum (c2['Provedor_B'])+
    c2['Provedor_C'] / sum (c2['Provedor_C'])+
    c2['Provedor_A'] / sum (c2['Provedor_A'])
)

nv3=(
    c3['Provedor_A'] / sum (c3['Provedor_A'])+
    c3['Provedor_B'] / sum (c3['Provedor_B'])+
    c3['Provedor_C'] / sum (c3['Provedor_C'])+
    c3['Provedor_A'] / sum (c3['Provedor_A'])
)

nv4=(
    c4['Provedor_A'] / sum (c4['Provedor_A'])+
    c4['Provedor_B'] / sum (c4['Provedor_B'])+
    c4['Provedor_C'] / sum (c4['Provedor_C'])+
    c4['Provedor_A'] / sum (c4['Provedor_A'])
)

rm1 = (nv1 / p).round(2)
rm2 = (nv2 / p).round(2)
rm3 = (nv3 / p).round(2)
rm4 = (nv4 / p).round(2)
tabela_df.insert(len(tabela_df.columns), 'c1', rm1)
tabela_df.insert(len(tabela_df.columns), 'c2', rm2)
tabela_df.insert(len(tabela_df.columns), 'c3', rm3)
tabela_df.insert(len(tabela_df.columns), 'c4', rm4)

print(tabela_df)
#==============================================================================#
############################### SELECIONAR PROVEDOR DE PRIORIZAÇÃO
#==============================================================================#
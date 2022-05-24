from tkinter.tix import COLUMN
from unicodedata import digit
import pandas as pd
import numpy as np
from sklearn.utils import column_or_1d

#Criando o dicionario:::
table = [
            ['12000', '400', '15', '2'],
            ['6000', '600', '10', '1,5'],
            ['18000', '200','20','3'],
            ['12000', '800','5','1']
]
          
            
#transformando em Dataframe com pandas:::
table_df = pd.DataFrame(data=table,
index=['Provedor_A', 'Provedor_B', 'Provedor_C', 'Provedor_D'],
columns=['Custo', 'Custo_transporte','Tempo','Rendimento' ]
)
rows = table_df.shape[0] 
cols = table_df.shape[1] 
print("Rows: " + str(rows)) 
print("Columns: " + str(cols))   


#Mostrando o DF criado:
print(table_df)
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
).round(6)
#rows = crit_df.shape[0] 
#cols = crit_df.shape[1] 
#print("Rows: " + str(rows)) 
#print("Columns: " + str(cols)) 
#print(crit_df['custo_trans'])
print(crit_df)
rows = crit_df.shape[0] 
cols = crit_df.shape[1] 
print("Rows: " + str(rows)) 
print("Columns: " + str(cols))   


vet=(
    crit_df['custo_MP'] / sum (crit_df['custo_MP']) +
    crit_df['custo_trans'] / sum (crit_df['custo_trans'])+
    crit_df['temp_apro'] / sum (crit_df['temp_apro'])+
    crit_df['rend'] / sum (crit_df['rend'])
)

a = vet / n

print(a)
#print(crite)
rc = np.mean(np.asmatrix(crit_df))



c1 = table_df
print(rc)

#rc concistencia 
# multiplicar a matrix por vet_pon coluna
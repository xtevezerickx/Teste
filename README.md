https://www.mindmeister.com/pt/971413503/data-science?fullscreen=1


import pandas as pd
import numpy as np

df = pd.DataFrame({
'A' : [1., 2., 3., 4., 5.],
'B' : [np.nan, 2., 3., np.nan, 6.]
})
df

idades = pd.DataFrame({
'Chave' : [1., 2., 3., 4., 5.],
'Idades' : [18., 25., 30., 40., 50.]
})
idades

df.loc[(df['B'].isnull()) & (df['A']==1),'B']=36
df.loc[(df['B'].isnull()) & (df['A']==4),'B']=80
df

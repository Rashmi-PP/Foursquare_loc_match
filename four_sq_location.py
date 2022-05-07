import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# chunk_size = 10000
# batch_no = 1
# while batch_no <=4:
#     for chunk in pd.read_csv("D:/Kaggle/fourSquare/pairs.csv", chunksize = chunk_size, iterator=True):
#         name = 'chunk'+str(batch_no)+'.csv'
#         chunk.to_csv(name, index = False)
#         batch_no+=1
#         break

df1 = pd.read_csv('chunk1.csv')
# print(df1.columns)
print(pd.read_sql_query('select * from df1 limit 5', con=connect(':memory')))
# print(df.head())
# df.info(verbose=True, memory_usage='deep')

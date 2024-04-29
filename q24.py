import np 
import pandas as pd

df = pd.DataFrame({"col1": [1,2,3,4], "col2": [1,2,3,3], "col3": [1,2,3,5]})
print(df)
print(df.query('col1 == 4 and col2 == 3'))
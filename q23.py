import np 
import pandas as pd

df = pd.DataFrame({"col1": [1,2,3], "col2": [1,2,3], "col3": [1,2,3]})
print(df)
df = df.rename(columns={"col1":"column1", "col2":"column2", "col3":"column3"})
print(df)
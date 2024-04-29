import np 
import pandas as pd

df = pd.DataFrame({"col1": [1,2,3,4], "col2": [1,2,3,3], "col3": [1,2,3,5]})
print(df)
df[len(df.index)-1] = [1,2,4,1]
print(df)
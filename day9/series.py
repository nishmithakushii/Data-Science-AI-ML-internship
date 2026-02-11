import pandas as pd
df=pd.read_excel("Student_Performance_Dataset.xlsx")
print(df)

import pandas as pd
s=pd.Series([10,20,30,40])
print(s)

marks=pd.Series([85,90,78],index=['Maths','Science','English'])

import pandas as pd
data1={"Name":["Ram","Diya","Chandan","James","Alice"]}
data2={"Maths":[80.0,90.0,77.5,87.5,86.5],"Physics":[81.0,94.0,74.5,83.0,82.5],"Chemistry":[91.5,86.5,85.5,90.0,91.0],"Biology":[82.5,83.5,84.5,85.0,93.0]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
frames=[df1,df2]
result=pd.concat(frames,axis=1)
total=df2.sum(axis=1)
result.insert(5,"Total",total)
print(result)


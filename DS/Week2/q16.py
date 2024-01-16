import pandas as pd
data={"Name":["Annie","Diya","Charles","James","Emily"],"Quiz_1/10":[8.0,9.0,7.5,8.5,6.5],"IN-Sem_/15":[11.0,14.0,14.5,13.0,12.5],"Quiz_2/10":[9.5,6.5,8.5,9.0,9.0],"In-Sem_2/15":[9.5,6.5,8.5,9.0,9.0],"In-Sem_2/15":[12.5,13.5,14.5,15.0,13.0]}
df=pd.DataFrame(data)
total=df.sum(axis=1,numeric_only=True)
df.insert(5,"Total",total)
print(df)
mean=df.mean(axis=0,numeric_only=True)
df.loc['mean']=mean
print(df)

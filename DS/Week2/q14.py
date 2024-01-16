import pandas as pd
data={"Name":["Arnav","Boyas","Vibhu"],"Height":["169","170","175"],"Qualification":["cse","cce","IT"]}
df=pd.DataFrame(data)
address=["Delhi","Gaza Nagar","Gurugram"]
df.insert(3,"Address",address)
print(df)

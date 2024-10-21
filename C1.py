import pandas as pd
arr = {
    'Day_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'steps_walked': [4335, 9552, 7332, 4503, 5335, 7552, 8332, 7552, 6004, 8965]
}
df = pd.DataFrame(arr)
print(df)
arr['steps_walked']=df['steps_walked']+1000
print(arr['steps_walked'])
days_more_than_7k=df.loc[df['steps_walked']>7000]
print(days_more_than_7k)

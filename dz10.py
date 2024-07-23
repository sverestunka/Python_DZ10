import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

for value in set(lst):
    data[value] = (data['whoAmI'] == value).astype(int)
    
data.drop(columns=['whoAmI'], inplace=True)
data.head()
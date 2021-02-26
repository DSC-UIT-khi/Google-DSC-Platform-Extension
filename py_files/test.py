import pandas as pd
import numpy as np

path = 'G:\\University\\Developers Student Club\\bootcamp 101\\data\\Bootcamp 101 final data.csv'

data = pd.read_csv(path)
arr =np.array(data.columns)
column = [i.lower() for i in arr]
data.columns = column
data.sort_values("email", inplace = True)

data.drop_duplicates(subset ="email", keep = "first", inplace = True)
lower_limit = 0
upper_limit= 70

while True:

    f_name = data["first name"][lower_limit:upper_limit]
    l_name = data["last name"][lower_limit:upper_limit]
    eemail = data["email"][lower_limit:upper_limit]
    
    lower_limit = upper_limit
    upper_limit+=70
    
    if len(f_name) ==0:
    	break
    else:
    	print(len(f_name),"lllllllllllllll",f_name,l_name,eemail)

    